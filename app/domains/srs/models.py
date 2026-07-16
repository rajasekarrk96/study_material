"""
Learning OS — Spaced Repetition System (SRS) Domain Models
FlashcardDeck, Flashcard, UserFlashcardProgress.
"""
from datetime import datetime
from app.core.extensions import db
from app.core.base_model import TimestampMixin


class FlashcardDeck(db.Model, TimestampMixin):
    __tablename__ = "flashcard_decks"

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    flashcards = db.relationship("Flashcard", back_populates="deck", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<FlashcardDeck {self.title}>"


class Flashcard(db.Model, TimestampMixin):
    __tablename__ = "flashcards"

    id = db.Column(db.Integer, primary_key=True)
    deck_id = db.Column(db.Integer, db.ForeignKey("flashcard_decks.id"), nullable=False)
    front_side_markdown = db.Column(db.Text, nullable=False)
    back_side_markdown = db.Column(db.Text, nullable=False)
    explanation = db.Column(db.Text)

    deck = db.relationship("FlashcardDeck", back_populates="flashcards")
    progress = db.relationship("UserFlashcardProgress", back_populates="flashcard", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Flashcard id={self.id}>"


class UserFlashcardProgress(db.Model):
    __tablename__ = "user_flashcard_progress"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    flashcard_id = db.Column(db.Integer, db.ForeignKey("flashcards.id"), nullable=False)
    repetitions = db.Column(db.Integer, default=0, nullable=False)
    interval_days = db.Column(db.Integer, default=1, nullable=False)
    ease_factor = db.Column(db.Float, default=2.5, nullable=False)
    next_review_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    last_reviewed_at = db.Column(db.DateTime, nullable=True)

    flashcard = db.relationship("Flashcard", back_populates="progress")

    def __repr__(self):
        return f"<UserFlashcardProgress user={self.user_id} card={self.flashcard_id} interval={self.interval_days} EF={self.ease_factor}>"
