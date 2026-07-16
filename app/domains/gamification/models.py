"""
Learning OS — Gamification Domain Models
UserXPLog, UserStreak.
"""
from datetime import datetime, date
from app.core.extensions import db


class UserXPLog(db.Model):
    __tablename__ = "user_xp_logs"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    xp_amount = db.Column(db.Integer, nullable=False)
    activity_type = db.Column(db.String(100), nullable=False)          # 'lesson_read', 'quiz_completed', 'exercise_solved'
    reference_id = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<UserXPLog user={self.user_id} xp={self.xp_amount} type={self.activity_type}>"


class UserStreak(db.Model):
    __tablename__ = "user_streaks"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False)
    current_streak = db.Column(db.Integer, default=0, nullable=False)
    longest_streak = db.Column(db.Integer, default=0, nullable=False)
    last_activity_date = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f"<UserStreak user={self.user_id} current={self.current_streak}>"
