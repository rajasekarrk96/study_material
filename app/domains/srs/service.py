"""
Learning OS — Spaced Repetition System (SRS) Service
Implements the SuperMemo-2 (SM-2) algorithm for adaptive flashcard scheduler sessions.
"""
import math
from datetime import datetime, timedelta
from app.core.extensions import db
from app.domains.srs.models import UserFlashcardProgress


def review_flashcard(user_id: int, flashcard_id: int, grade: int) -> dict:
    """
    Applies the SuperMemo-2 (SM-2) algorithm to recalculate card repetition intervals and ease factors.
    Grade scale: 0 (complete blackout) to 5 (perfect recall response).
    """
    # Ensure grade is within correct bounds
    grade = max(0, min(5, grade))

    # Retrieve or create flashcard review state
    progress = UserFlashcardProgress.query.filter_by(
        user_id=user_id,
        flashcard_id=flashcard_id
    ).first()

    if not progress:
        progress = UserFlashcardProgress(
            user_id=user_id,
            flashcard_id=flashcard_id,
            repetitions=0,
            interval_days=1,
            ease_factor=2.5
        )
        db.session.add(progress)

    # SM-2 repetitions and interval parameters logic
    if grade >= 3:
        if progress.repetitions == 0:
            progress.interval_days = 1
        elif progress.repetitions == 1:
            progress.interval_days = 6
        else:
            progress.interval_days = int(math.ceil(progress.interval_days * progress.ease_factor))
        
        progress.repetitions += 1
    else:
        # Incorrect recall, reset repetitions sequence
        progress.repetitions = 0
        progress.interval_days = 1

    # Recalculate Ease Factor (EF)
    # EF' = EF + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
    factor_diff = 0.1 - (5 - grade) * (0.08 + (5 - grade) * 0.02)
    progress.ease_factor = max(1.3, progress.ease_factor + factor_diff)

    # Set scheduling audit timestamps
    now = datetime.utcnow()
    progress.last_reviewed_at = now
    progress.next_review_at = now + timedelta(days=progress.interval_days)

    db.session.commit()

    return {
        "repetitions": progress.repetitions,
        "interval_days": progress.interval_days,
        "ease_factor": round(progress.ease_factor, 2),
        "next_review_at": progress.next_review_at
    }
