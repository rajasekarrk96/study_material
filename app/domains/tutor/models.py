"""
Learning OS — AI Tutor Domain Models
AITutorSession, AITutorMessage.
"""
from datetime import datetime
from app.core.extensions import db
from app.core.base_model import TimestampMixin


class AITutorSession(db.Model, TimestampMixin):
    __tablename__ = "ai_tutor_sessions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey("lessons.id"), nullable=True)  # Optional context
    title = db.Column(db.String(255), nullable=True)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    messages = db.relationship("AITutorMessage", back_populates="session", cascade="all, delete-orphan")
    user = db.relationship("User")
    lesson = db.relationship("Lesson")

    def __repr__(self):
        return f"<AITutorSession id={self.id} user={self.user_id} title={self.title}>"


class AITutorMessage(db.Model, TimestampMixin):
    __tablename__ = "ai_tutor_messages"

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey("ai_tutor_sessions.id"), nullable=False)
    sender = db.Column(db.String(50), nullable=False)  # 'user' or 'tutor'
    content = db.Column(db.Text, nullable=False)

    session = db.relationship("AITutorSession", back_populates="messages")

    def __repr__(self):
        return f"<AITutorMessage id={self.id} sender={self.sender} session={self.session_id}>"
