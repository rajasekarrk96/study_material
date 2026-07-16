# 03 — User Roles & RBAC Design

---

## 3.1 Role Definitions

| Role | Code | Description |
|------|------|-------------|
| Super Admin | `super_admin` | Platform owner. Full access. Cannot be restricted. |
| Admin | `admin` | Manages all content, users, settings. Cannot manage Super Admin. |
| Author | `author` | Creates and owns content. Limited to own content. |
| Reviewer | `reviewer` | Reviews and approves content. Cannot publish. |
| Editor | `editor` | Edits any published content. Can re-publish. |
| Moderator | `moderator` | Manages comments, flags, user reports. No content edit. |
| Student | `student` | Default authenticated user. Learns, takes quizzes, submits exercises. |
| Guest | `guest` | Unauthenticated visitor. Public content only. |

---

## 3.2 Role Hierarchy

```
super_admin
    └── admin
          ├── author
          │     └── (owns content)
          ├── reviewer
          │     └── (approves content)
          ├── editor
          │     └── (edits published content)
          ├── moderator
          │     └── (manages community)
          └── student (default registered user)
```

---

## 3.3 Permissions Matrix

### Content Permissions

| Permission | super_admin | admin | author | reviewer | editor | moderator | student | guest |
|-----------|:-----------:|:-----:|:------:|:--------:|:------:|:---------:|:-------:|:-----:|
| View published lessons | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| View draft lessons | ✅ | ✅ | ✅ (own) | ✅ | ✅ | ❌ | ❌ | ❌ |
| Create lesson | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Edit own lesson | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Edit any lesson | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| Delete lesson | ✅ | ✅ | ✅ (own, draft) | ❌ | ❌ | ❌ | ❌ | ❌ |
| Submit lesson for review | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Approve / Reject lesson | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Publish lesson | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| Archive lesson | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| Restore version | ✅ | ✅ | ✅ (own) | ❌ | ✅ | ❌ | ❌ | ❌ |
| Manage courses | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Manage learning paths | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

### User Permissions

| Permission | super_admin | admin | author | reviewer | editor | moderator | student |
|-----------|:-----------:|:-----:|:------:|:--------:|:------:|:---------:|:-------:|
| View user list | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ (limited) | ❌ |
| Edit user profile | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ (own) |
| Ban user | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ (temp) | ❌ |
| Assign roles | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Reset passwords | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ (own) |

### Assessment Permissions

| Permission | super_admin | admin | author | reviewer | editor | moderator | student | guest |
|-----------|:-----------:|:-----:|:------:|:--------:|:------:|:---------:|:-------:|:-----:|
| View quiz questions | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| View quiz answers | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (after attempt) | ❌ |
| Create quiz | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Take quiz | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| View exercise problems | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Submit exercise solutions | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Grade submissions | ✅ | ✅ | ✅ (own) | ✅ | ✅ | ❌ | ❌ | ❌ |
| View interview questions | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| View interview answers | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |

### Analytics & Admin Permissions

| Permission | super_admin | admin | author | reviewer | editor | moderator | student |
|-----------|:-----------:|:-----:|:------:|:--------:|:------:|:---------:|:-------:|
| View platform analytics | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| View own content analytics | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| View own progress | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Manage SEO metadata | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ |
| Access admin panel | ✅ | ✅ | ✅ (limited) | ✅ (limited) | ✅ (limited) | ✅ (limited) | ❌ |
| Manage feature flags | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Manage system settings | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

---

## 3.4 RBAC Implementation Pattern

```python
# app/core/rbac.py

from functools import wraps
from flask import abort
from flask_login import current_user

ROLE_HIERARCHY = {
    'super_admin': 7,
    'admin': 6,
    'editor': 5,
    'reviewer': 4,
    'author': 3,
    'moderator': 2,
    'student': 1,
    'guest': 0,
}

def require_role(*roles):
    """Decorator: restrict route to specified roles."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(401)
            if current_user.role not in roles:
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def require_min_role(min_role: str):
    """Decorator: allow this role and all higher roles."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(401)
            if ROLE_HIERARCHY.get(current_user.role, 0) < ROLE_HIERARCHY.get(min_role, 0):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def require_permission(permission: str):
    """Decorator: check fine-grained permission."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(401)
            if not current_user.has_permission(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
```

---

## 3.5 Content Workflow States (For RBAC)

```
DRAFT -> SUBMITTED -> REVIEWED -> APPROVED -> PUBLISHED -> ARCHIVED
          (Author)   (Reviewer)   (Reviewer)  (Editor)    (Editor)
                         |
                     REJECTED -> DRAFT
                    (Reviewer)  (Author revises)
```

| State | Visible To |
|-------|-----------|
| DRAFT | Author (own), Admin, Super Admin |
| SUBMITTED | Author, Reviewer, Editor, Admin, Super Admin |
| REVIEWED | Author, Reviewer, Editor, Admin, Super Admin |
| APPROVED | Author, Editor, Admin, Super Admin |
| PUBLISHED | All users (including guests for free content) |
| ARCHIVED | Admin, Super Admin only |

---

## 3.6 Database Model: Roles & Permissions

```python
# app/domains/auth/models.py (excerpt)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)  # 'admin', 'author'
    display_name = db.Column(db.String(100))
    description = db.Column(db.Text)
    level = db.Column(db.Integer, default=1)  # Hierarchy level
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Permission(db.Model):
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100), unique=True)  # 'lesson.create', 'user.ban'
    description = db.Column(db.Text)
    category = db.Column(db.String(50))  # 'content', 'user', 'admin'

class RolePermission(db.Model):
    __tablename__ = 'role_permissions'
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), primary_key=True)
    permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'), primary_key=True)
    granted_at = db.Column(db.DateTime, default=datetime.utcnow)
    granted_by = db.Column(db.Integer, db.ForeignKey('users.id'))

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    display_name = db.Column(db.String(200))
    password_hash = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_active = db.Column(db.Boolean, default=True)
    is_verified = db.Column(db.Boolean, default=False)
    avatar_url = db.Column(db.String(500))
    bio = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login_at = db.Column(db.DateTime)
    
    role = db.relationship('Role', backref='users')
    
    def has_permission(self, permission_code: str) -> bool:
        return any(p.code == permission_code for p in self.role.permissions)
    
    def has_role(self, *role_names) -> bool:
        return self.role.name in role_names
```
