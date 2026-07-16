# 08 — Progress Engine

> The Progress Engine monitors student actions, logs XP, manages user levels, recalculates streaks, and handles user analytics.

---

## 8.1 XP (Experience Points) Architecture

XP drives gamification and course level calculation. Every productive user interaction generates an asynchronous XP audit record.

```
       [Student Action]
              │
              ▼
   [Progress Engine Service]
      ├── Check daily cap (Max 500 XP/day)
      ├── Create transaction in user_xp_log
      └── Update user_progress (total_xp, level)
              │
              ▼
   [Trigger Achievement Engine Check]
```

### XP Value Allocations

| Action Type | XP Value | Daily Cap |
|-------------|----------|-----------|
| Lesson Complete | 10 | 100 |
| Quiz Passed | 25 | 100 |
| Exercise Solved | 30 | 150 |
| Streak Maintained | 5 | 5 |
| Post a Note | 2 | 20 |
| Flashcard Session | 15 | 45 |
| Course Complete | 200 | None |
| Path Complete | 500 | None |

---

## 8.2 Level Calculation

User Level ($L$) is calculated dynamically from their cumulative XP ($XP$) using a scaling curve:

$$L = \lfloor 0.1 \times \sqrt{XP} \rfloor + 1$$

To reach Level $L$, the total cumulative XP required is:

$$XP_{required} = 100 \times (L - 1)^2$$

### Level Threshold Table

| Level | Cumulative XP Required | XP Needed for Next Level |
|-------|------------------------|--------------------------|
| 1     | 0                      | 100                      |
| 2     | 100                    | 300                      |
| 3     | 400                    | 500                      |
| 4     | 900                    | 700                      |
| 5     | 1,600                  | 900                      |
| 10    | 8,100                  | 1,900                    |

---

## 8.3 Streak Engine

Streaks measure daily learning consistency. A streak increment occurs when a student completes a lesson, passes a quiz, or submits an exercise.

```python
# app/domains/progress/service.py

from datetime import date, timedelta
from app.domains.progress.models import Streak

class StreakService:
    def __init__(self, streak_repo, db_session):
        self.streak_repo = streak_repo
        self.db = db_session

    def record_activity(self, user_id: int) -> Streak:
        """
        Processes a daily user activity.
        Increments current streak, updates longest streak if exceeded, 
        or restores an expired streak.
        """
        streak = self.streak_repo.get_by_user_id(user_id)
        today = date.today()

        if not streak:
            streak = Streak(
                user_id=user_id,
                current_streak=1,
                longest_streak=1,
                last_activity_date=today
            )
            self.streak_repo.save(streak)
            return streak

        if streak.last_activity_date == today:
            # Already active today, streak remains unchanged
            return streak

        yesterday = today - timedelta(days=1)
        if streak.last_activity_date == yesterday:
            # Active consecutive day: increment
            streak.current_streak += 1
            streak.last_activity_date = today
            if streak.current_streak > streak.longest_streak:
                streak.longest_streak = streak.current_streak
        else:
            # Missed a day: reset streak to 1
            streak.current_streak = 1
            streak.last_activity_date = today

        self.streak_repo.save(streak)
        return streak
```

---

## 8.4 Lesson Progress Tracking Lifecycle

Lesson progress shifts across 3 main statuses:

```
[NOT STARTED] ──(Student Opens)──► [IN PROGRESS] ──(Exercises Solved + Checkbox)──► [COMPLETED]
```

### Complete Conditions
A lesson is considered `COMPLETED` when:
1. **Interactive Elements Complete**: Corresponding Quizzes have a passing attempt AND Exercises have at least one accepted submission.
2. **Read Status Marked**: Student manually marks the lesson as complete.
3. **Trigger**: Progress Engine captures the event, marks the status, and inserts the `Lesson Complete` XP logs.
