"""
Learning OS — Auth Domain Models
Users, Roles, Permissions, Sessions, UserRoleMapping, UserCourse, PermissionMatrix.
"""
from datetime import datetime
from flask_login import UserMixin
from app.core.extensions import db
from app.core.base_model import TimestampMixin


class Role(db.Model, TimestampMixin):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)       # 'admin', 'student'
    display_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    level = db.Column(db.Integer, default=1)                           # hierarchy level

    users = db.relationship("User", back_populates="role")

    def __repr__(self):
        return f"<Role {self.name}>"


class Permission(db.Model):
    __tablename__ = "permissions"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100), unique=True, nullable=False)      # 'lesson.create'
    description = db.Column(db.Text)
    category = db.Column(db.String(50))                                # 'content', 'user'

    def __repr__(self):
        return f"<Permission {self.code}>"


class RolePermission(db.Model):
    __tablename__ = "role_permissions"

    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), primary_key=True)
    permission_id = db.Column(db.Integer, db.ForeignKey("permissions.id"), primary_key=True)
    granted_at = db.Column(db.DateTime, default=datetime.utcnow)
    granted_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)


class UserRoleMapping(db.Model):
    __tablename__ = "user_role_mappings"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)

    user = db.relationship("User", foreign_keys=[user_id])
    role = db.relationship("Role", foreign_keys=[role_id])


class PermissionMatrix(db.Model):
    __tablename__ = "permission_matrix"

    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)
    permission_code = db.Column(db.String(100), nullable=False)
    is_granted = db.Column(db.Boolean, default=False, nullable=False)

    role = db.relationship("Role")


class UserCourse(db.Model, TimestampMixin):
    __tablename__ = "user_courses"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    status = db.Column(db.String(50), default="Active", nullable=False)  # Active, Expired, Suspended, Pending, Trial, Lifetime, Corporate, Demo
    expiry = db.Column(db.DateTime, nullable=True)
    purchase_type = db.Column(db.String(50), default="Free", nullable=False)  # Free, Subscription, Paid
    progress = db.Column(db.Integer, default=0, nullable=False)  # 0 to 100 percentage

    user = db.relationship("User", back_populates="enrollments")
    course = db.relationship("Course")

    def __repr__(self):
        return f"<UserCourse user={self.user_id} course={self.course_id} status={self.status}>"


class User(db.Model, UserMixin, TimestampMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    display_name = db.Column(db.String(200))
    password_hash = db.Column(db.String(255), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=True)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    is_verified = db.Column(db.Boolean, default=False, nullable=False)
    avatar_url = db.Column(db.String(500))
    bio = db.Column(db.Text)
    last_login_at = db.Column(db.DateTime)
    timezone = db.Column(db.String(50), default="UTC")

    role = db.relationship("Role", back_populates="users")
    enrollments = db.relationship("UserCourse", back_populates="user", cascade="all, delete-orphan")

    def has_role(self, *role_names: str) -> bool:
        return self.role is not None and self.role.name in role_names

    def is_admin(self) -> bool:
        return self.has_role("super_admin", "admin")

    def __repr__(self):
        return f"<User {self.username}>"
