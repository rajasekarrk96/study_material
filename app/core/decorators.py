"""
Learning OS — RBAC Authorization Decorators.
Provides @require_role and @require_min_role decorators for view route protection.
"""
from functools import wraps
from flask import abort
from flask_login import current_user
from app.domains.auth.models import Role


def require_role(role_name: str):
    """
    Decorator that restricts route access to users with a specific role name.
    Usage:
        @app.route('/admin')
        @login_required
        @require_role('admin')
        def admin_index():
            ...
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(401)
            if not current_user.role or current_user.role.name != role_name:
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def require_min_role(min_role_name_or_level):
    """
    Decorator that restricts route access to users with at least the specified minimum role level.
    If a string is passed (e.g. 'author'), resolves the corresponding level dynamically.
    Usage:
        @app.route('/edit')
        @login_required
        @require_min_role('author')
        def edit_content():
            ...
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(401)
            
            # Resolve target level
            if isinstance(min_role_name_or_level, int):
                target_level = min_role_name_or_level
            else:
                # Find role by name in db
                role = Role.query.filter_by(name=min_role_name_or_level).first()
                if not role:
                    # Fallback default level safety check
                    target_level = 99
                else:
                    target_level = role.level

            user_level = current_user.role.level if current_user.role else 0
            if user_level < target_level:
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
