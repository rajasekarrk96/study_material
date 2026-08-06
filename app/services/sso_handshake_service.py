"""
Learning OS — SSO Handshake & API Service.
Manages JWKS public key rotation and user entitlements syncing with external identity providers.
"""
import json
import logging
from typing import Dict, List, Optional
from datetime import datetime
from app.core.extensions import db
from app.domains.auth.models import UserCourse
from app.domains.auth.providers import ExternalAuthProvider

logger = logging.getLogger("learning_os.sso")


class SSOHandshakeService:
    # Simulating a dynamic key storage in memory or cache for rotation
    _mock_key_store = {
        "keys": [
            {
                "kty": "oct",
                "kid": "learning-os-secret-key-v1",
                "alg": "HS256",
                "use": "sig"
            }
        ]
    }

    @classmethod
    def get_jwks(cls) -> Dict:
        """Retrieve JWKS public key metadata for JWT validations."""
        return cls._mock_key_store

    @classmethod
    def rotate_keys(cls) -> Dict:
        """Simulate rotation of the JWT signing key for SSO security rotations."""
        new_kid = f"learning-os-secret-key-v{int(datetime.utcnow().timestamp())}"
        cls._mock_key_store["keys"] = [
            {
                "kty": "oct",
                "kid": new_kid,
                "alg": "HS256",
                "use": "sig"
            }
        ]
        logger.info(f"JWKS key rotated successfully. New kid: {new_kid}")
        return cls._mock_key_store

    @classmethod
    def sync_external_entitlements(cls, user_id: int, external_courses: List[Dict]) -> int:
        """
        Synchronize UserCourse entitlements from external claims.
        Updates status/expiry for existing mappings, and creates new ones if missing.
        """
        synced_count = 0
        from app.domains.content.models import Course

        for c_data in external_courses:
            course_slug = c_data.get("slug")
            status = c_data.get("status", "Active")
            
            course = Course.query.filter_by(slug=course_slug).first()
            if not course:
                continue

            # Find existing entitlement
            ent = UserCourse.query.filter_by(user_id=user_id, course_id=course.id).first()
            if not ent:
                ent = UserCourse(
                    user_id=user_id,
                    course_id=course.id,
                    status=status,
                    purchase_type="Subscription"
                )
                db.session.add(ent)
            else:
                ent.status = status
            
            synced_count += 1

        db.session.commit()
        return synced_count
