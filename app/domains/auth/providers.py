"""
Learning OS — Auth Providers
Implements local and external (JWT) authentication provider strategies.
"""
import os
import logging
import json
from abc import ABC, abstractmethod
from typing import Optional
from datetime import datetime
import jwt
from flask import request, has_request_context
from werkzeug.security import check_password_hash
from app.core.extensions import db
from app.domains.auth.models import User, Role, UserCourse
from app.domains.content.models import Course

logger = logging.getLogger("learning_os.auth")

DEFAULT_CLAIM_MAP = {
    "user_id": "user_id",
    "username": "username",
    "email": "email",
    "role": "role",
    "course_ids": "course_ids",
    "subscription_type": "subscription_type",
    "subscription_expiry": "subscription_expiry"
}


class BaseAuthProvider(ABC):
    @abstractmethod
    def authenticate(self, *args, **kwargs) -> Optional[User]:
        """Authenticate user. Returns User object or None."""
        pass


class LocalAuthProvider(BaseAuthProvider):
    """
    Standard standalone authentication provider.
    Validates users against local email/password credentials.
    """
    def authenticate(self, email: str, password: str) -> Optional[User]:
        email_clean = email.strip().lower()
        user = User.query.filter_by(email=email_clean, is_active=True).first()
        if user and check_password_hash(user.password_hash, password):
            return user
        return None


class ExternalAuthProvider(BaseAuthProvider):
    """
    External JWT-based Single Sign-On (SSO) provider.
    Validates signature, decodes token claims, and syncs user details.
    """
    def __init__(self):
        # Fall back to SECRET_KEY if JWT_SECRET_KEY is not defined
        self.secret_key = os.environ.get("JWT_SECRET_KEY") or os.environ.get("SECRET_KEY") or "fallback-secret"
        self.algorithm = os.environ.get("JWT_ALGORITHM", "HS256")
        
        # Load claims map adapter
        claim_map_raw = os.environ.get("JWT_CLAIM_MAP")
        if claim_map_raw:
            try:
                self.claim_map = json.loads(claim_map_raw)
            except Exception as e:
                logger.error("Failed to parse JWT_CLAIM_MAP: %s", e)
                self.claim_map = DEFAULT_CLAIM_MAP
        else:
            self.claim_map = DEFAULT_CLAIM_MAP

    def authenticate(self, token: str) -> Optional[User]:
        """Validate JWT token, parse claims, sync user info, and return the User."""
        try:
            # 1. Decode and verify token signature/expiry
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return self._sync_user(payload)
        except jwt.ExpiredSignatureError:
            logger.warning("External JWT signature expired.")
            return None
        except jwt.InvalidTokenError as e:
            logger.warning("Invalid external JWT token: %s", e)
            return None
        except Exception as e:
            logger.error("Error during JWT authentication: %s", e)
            return None

    def _sync_user(self, payload: dict) -> Optional[User]:
        """Synchronize the decoded JWT payload details to our local User, Role, and Enrollments."""
        # Extract fields using configured claim mapping
        email = payload.get(self.claim_map["email"])
        username = payload.get(self.claim_map["username"])
        ext_role_name = payload.get(self.claim_map["role"], "student").lower()
        ext_course_ids = payload.get(self.claim_map["course_ids"], [])
        sub_type = payload.get(self.claim_map["subscription_type"], "Free")
        sub_expiry_raw = payload.get(self.claim_map["subscription_expiry"])

        if not email or not username:
            logger.error("Missing email or username claims in JWT payload.")
            return None

        # Resolve subscription expiry date
        sub_expiry = None
        if sub_expiry_raw:
            try:
                if isinstance(sub_expiry_raw, (int, float)):
                    sub_expiry = datetime.utcfromtimestamp(sub_expiry_raw)
                else:
                    sub_expiry = datetime.fromisoformat(str(sub_expiry_raw))
            except Exception as e:
                logger.warning("Could not parse subscription expiry claim: %s", e)

        # 2. Retrieve or Provision User
        user = User.query.filter((User.email == email) | (User.username == username)).first()
        is_new = False

        if not user:
            is_new = True
            logger.info("Provisioning new external user for: %s", email)
            # Create a placeholder user
            user = User(
                email=email,
                username=username,
                display_name=username,
                password_hash="EXTERNAL_JWT_ACCOUNT",
                is_active=True,
                is_verified=True,
                bio="External Account synchronized from Bytes & Boards.",
            )
            db.session.add(user)
            db.session.flush()

        # Update last login
        user.last_login_at = datetime.utcnow()

        # 3. Synchronize Role
        # Standard roles mapping: admin, staff, student, public
        role_mapping = {
            "super_admin": "admin",
            "admin": "admin",
            "editor": "staff",
            "staff": "staff",
            "reviewer": "staff",
            "student": "student",
            "guest": "student",
            "public": "student"
        }
        target_role_name = role_mapping.get(ext_role_name, "student")
        local_role = Role.query.filter_by(name=target_role_name).first()
        if local_role:
            user.role_id = local_role.id

        db.session.flush()

        # 4. Synchronize Enrollments (UserCourse)
        # ext_course_ids can be a list of integers or course slugs
        for c_id in ext_course_ids:
            course = None
            if isinstance(c_id, int):
                course = db.session.get(Course, c_id)
            else:
                course = Course.query.filter_by(slug=str(c_id)).first()

            if course:
                # Check if user is already enrolled
                enrollment = UserCourse.query.filter_by(user_id=user.id, course_id=course.id).first()
                if not enrollment:
                    logger.info("Enrolling external user in course %s", course.title)
                    enrollment = UserCourse(
                        user_id=user.id,
                        course_id=course.id,
                        status="Active",
                        purchase_type=sub_type,
                        expiry=sub_expiry
                    )
                    db.session.add(enrollment)
                else:
                    # Update status/expiry if active payload specifies it
                    enrollment.purchase_type = sub_type
                    enrollment.expiry = sub_expiry
                    enrollment.status = "Active"

        db.session.commit()
        return user


def get_auth_provider() -> BaseAuthProvider:
    """
    Returns the appropriate AuthProvider instance according to the AUTH_MODE config.
    Supports LOCAL, JWT, and AUTO dispatching logic.
    """
    auth_mode = os.environ.get("AUTH_MODE", "LOCAL").upper()

    if auth_mode == "JWT":
        return ExternalAuthProvider()
    elif auth_mode == "LOCAL":
        return LocalAuthProvider()
    elif auth_mode == "AUTO":
        # If in request context, check request parameters/cookies/headers for JWT presence
        if has_request_context():
            token = request.args.get("jwt") or request.cookies.get("jwt") or request.cookies.get("token")
            if not token:
                auth_header = request.headers.get("Authorization")
                if auth_header and auth_header.startswith("Bearer "):
                    token = auth_header[7:]
            if token:
                return ExternalAuthProvider()
        return LocalAuthProvider()

    return LocalAuthProvider()
