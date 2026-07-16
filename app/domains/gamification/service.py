"""
Learning OS — Gamification Service
Manages XP allocation, level calculations, and daily user streak validation.
"""
from datetime import datetime, date, timedelta
from app.core.extensions import db
from app.domains.gamification.models import UserXPLog, UserStreak

DAILY_XP_CAP = 500


def award_xp(user_id: int, amount: int, activity_type: str, reference_id: int = None) -> int:
    """Awards XP to user while enforcing a daily maximum cap of 500 XP."""
    if amount <= 0:
        return 0

    # Calculate starting timestamp for current day in UTC
    start_of_day = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)

    # Calculate total XP already earned today
    today_xp = db.session.query(db.func.sum(UserXPLog.xp_amount)).filter(
        UserXPLog.user_id == user_id,
        UserXPLog.created_at >= start_of_day
    ).scalar() or 0

    if today_xp >= DAILY_XP_CAP:
        return 0  # Cap reached

    # Award only what is remaining under the cap
    allowed_xp = min(amount, DAILY_XP_CAP - today_xp)
    if allowed_xp <= 0:
        return 0

    # Record XP log entry
    xp_log = UserXPLog(
        user_id=user_id,
        xp_amount=allowed_xp,
        activity_type=activity_type,
        reference_id=reference_id
    )
    db.session.add(xp_log)

    # Process and update user daily active streak
    update_streak(user_id)

    db.session.commit()
    return allowed_xp


def calculate_level(total_xp: int) -> int:
    """Calculates user level based on progression curve formula: L = floor(0.1 * sqrt(XP)) + 1."""
    if total_xp <= 0:
        return 1
    import math
    return int(math.floor(0.1 * math.sqrt(total_xp))) + 1


def update_streak(user_id: int) -> None:
    """Updates user current and longest streak of active daily learning."""
    today = date.today()
    streak = UserStreak.query.filter_by(user_id=user_id).first()

    if not streak:
        # First learning activity: start streak of 1
        streak = UserStreak(
            user_id=user_id,
            current_streak=1,
            longest_streak=1,
            last_activity_date=today
        )
        db.session.add(streak)
        return

    # User already has a streak history, compute difference in days
    if streak.last_activity_date:
        delta = today - streak.last_activity_date
        
        if delta.days == 1:
            # Active on consecutive day, increment streak
            streak.current_streak += 1
            streak.longest_streak = max(streak.longest_streak, streak.current_streak)
            streak.last_activity_date = today
        elif delta.days > 1:
            # Missed a day or more, reset streak to 1
            streak.current_streak = 1
            streak.last_activity_date = today
        # If delta.days == 0 (already active today), keep streak unchanged
    else:
        # Fallback if last_activity_date is null
        streak.current_streak = 1
        streak.longest_streak = max(streak.longest_streak, 1)
        streak.last_activity_date = today
