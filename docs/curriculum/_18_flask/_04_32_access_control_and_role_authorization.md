# Access Control and Role Authorization

> **Course**: Flask | **Module**: Advanced Flask Patterns | **Difficulty**: advanced

---

### 1. Role-Based Access Control (RBAC) Pattern
```python
from enum import Enum
from functools import wraps
from flask_login import current_user
from flask import abort

class Role(str, Enum):
    ADMIN = 'admin'
    EDITOR = 'editor'
    VIEWER = 'viewer'

# User model with role field
class User(db.Model, UserMixin):
    role = db.Column(db.Enum(Role), default=Role.VIEWER)

    def has_role(self, *roles):
        return self.role in roles
```

### 2. Role-Required Decorator
```python
def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(401)
            if not current_user.has_role(*roles):
                abort(403)
            return f(*args, **kwargs)
        return decorated
    return decorator

@app.route('/admin/dashboard')
@login_required
@role_required(Role.ADMIN)
def admin_dashboard():
    return render_template('admin.html')
```

### 3. Permission-Based Access (Fine-Grained)
```python
PERMISSIONS = {
    Role.ADMIN:  {'read', 'write', 'delete', 'manage'},
    Role.EDITOR: {'read', 'write'},
    Role.VIEWER: {'read'},
}

def can(permission):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            user_perms = PERMISSIONS.get(current_user.role, set())
            if permission not in user_perms:
                abort(403)
            return f(*args, **kwargs)
        return decorated
    return decorator

@app.route('/posts/<int:id>', methods=['DELETE'])
@login_required
@can('delete')
def delete_post(id):
    ...
```

### 4. Flask-Principal Integration
```python
from flask_principal import Principal, Permission, RoleNeed
principal = Principal(app)

admin_permission = Permission(RoleNeed('admin'))

@app.route('/admin')
@admin_permission.require(http_exception=403)
def admin():
    return 'Admin only'
```

---

Build a content management system with three roles (Admin/Editor/Viewer), role-required decorators, a permission matrix, and 403/401 error pages.

---
