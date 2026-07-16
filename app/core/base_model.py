"""
Learning OS — Base Model Mixin
Provides created_at / updated_at audit fields to all domain models.
"""
from datetime import datetime
from app.core.extensions import db


class TimestampMixin:
    """Adds created_at and updated_at to any model."""
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,
                           onupdate=datetime.utcnow, nullable=False)


class SoftDeleteMixin:
    """Adds soft-delete support: is_deleted, deleted_at, deleted_by."""
    is_deleted = db.Column(db.Boolean, default=False, nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)
    deleted_by = db.Column(db.Integer, nullable=True)
