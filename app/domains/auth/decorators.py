"""
Learning OS — Auth Decorators
Enforces role-based permissions using the dynamic database PermissionMatrix.
"""
from functools import wraps
from flask import abort
from flask_login import current_user
from app.domains.auth.models import PermissionMatrix


def permission_required(permission_code: str):
    """
    Decorator to restrict view access based on the database PermissionMatrix.
    Super admin/admin roles bypass permission checks automatically.
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(401)

            # Admins bypass permission checks
            if current_user.is_admin():
                return f(*args, **kwargs)

            # Resolve user's role
            role_id = current_user.role_id
            if not role_id:
                abort(403)

            # Query PermissionMatrix for matching permission code
            allowed = PermissionMatrix.query.filter_by(
                role_id=role_id,
                permission_code=permission_code,
                is_granted=True
            ).first()

            if not allowed:
                abort(403)

            return f(*args, **kwargs)
        return decorated_function
    return decorator
