"""
Learning OS — Study Annotations Domain Models
Bookmark, UserNote.
"""
from datetime import datetime
from app.core.extensions import db
from app.core.base_model import TimestampMixin


class Bookmark(db.Model):
    __tablename__ = "bookmarks"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey("lessons.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    __table_args__ = (
        db.UniqueConstraint("user_id", "lesson_id", name="uq_user_lesson_bookmark"),
    )

    def __repr__(self):
        return f"<Bookmark user={self.user_id} lesson={self.lesson_id}>"


class UserNote(db.Model, TimestampMixin):
    __tablename__ = "user_notes"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey("lessons.id"), nullable=False)
    content_markdown = db.Column(db.Text, nullable=False)

    __table_args__ = (
        db.UniqueConstraint("user_id", "lesson_id", name="uq_user_lesson_note"),
    )

    def __repr__(self):
        return f"<UserNote user={self.user_id} lesson={self.lesson_id}>"
