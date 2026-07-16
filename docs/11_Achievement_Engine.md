# 11 — Achievement Engine

> The Achievement Engine parses user actions, awards badges, calculates thresholds, and grants progression achievements.

---

## 11.1 Gamification Design System

Badges and Achievements reward consistency, topic mastery, community involvement, and challenge completion.

```
       ┌────────────────────────┐
       │   Achievement Engine   │
       └───────────┬────────────┘
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
┌─────────────────┐ ┌─────────────────┐
│     Badges      │ │  Achievements   │
│ Tiered rewards  │ │ Progress meters │
│ (Bronze/Gold)   │ │ (10/50 Lessons) │
└─────────────────┘ └─────────────────┘
```

---

## 11.2 Badge System Definitions

### Tiers
- **Bronze**: Foundational achievements (e.g., first lesson finished).
- **Silver**: Consistency goals (e.g., maintaining a 7-day streak).
- **Gold**: Advanced challenges (e.g., completing 5 programming courses).
- **Platinum**: Platform mastery achievements (e.g., solving all advanced exercises).

---

## 11.3 Criteria Evaluation Database Model

```python
# app/domains/achievement/models.py

class Badge(db.Model):
    __tablename__ = 'badges'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    icon_url = db.Column(db.String(255))
    tier = db.Column(db.String(50), default='bronze')  # 'bronze', 'silver', 'gold', 'platinum'
    xp_reward = db.Column(db.Integer, default=50)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class BadgeCriteria(db.Model):
    __tablename__ = 'badge_criteria'
    id = db.Column(db.Integer, primary_key=True)
    badge_id = db.Column(db.Integer, db.ForeignKey('badges.id'), nullable=False)
    criteria_type = db.Column(db.String(100), nullable=False)  # 'lesson_count', 'streak_days', 'course_complete'
    criteria_value = db.Column(db.Integer, nullable=False)
    operator = db.Column(db.String(10), default='>=')  # '>=', '=='
    
    badge = db.relationship('Badge', backref=db.backref('criteria', lazy=True))
```

---

## 11.4 Asynchronous Badge Evaluator

Badge checks are performed asynchronously after progress updates via the background worker queue.

```python
# app/domains/achievement/service.py

from app.domains.achievement.models import Badge, UserBadge
from app.domains.progress.models import UserProgress

class AchievementService:
    def __init__(self, db_session, progress_repo):
        self.db = db_session
        self.progress_repo = progress_repo

    def evaluate_eligible_badges(self, user_id: int) -> list[Badge]:
        """
        Scans all badges the user has not yet earned.
        If all criteria match, user_badges is updated and extra XP is logged.
        """
        # Get unearned badges
        earned_badge_ids = [ub.badge_id for ub in self.db.query(UserBadge).filter_by(user_id=user_id).all()]
        unearned_badges = self.db.query(Badge).filter(~Badge.id.in_(earned_badge_ids)).all()
        
        user_stats = self.progress_repo.get_user_progress(user_id)
        if not user_stats:
            return []

        newly_earned = []

        for badge in unearned_badges:
            criteria_met = True
            for criterion in badge.criteria:
                metric_val = self._resolve_metric_value(user_id, user_stats, criterion.criteria_type)
                
                # Check condition
                if criterion.operator == '>=':
                    if not (metric_val >= criterion.criteria_value):
                        criteria_met = False
                        break
                elif criterion.operator == '==':
                    if not (metric_val == criterion.criteria_value):
                        criteria_met = False
                        break
            
            if criteria_met and badge.criteria: # must have at least one criteria
                # Award badge
                self._award_badge(user_id, badge)
                newly_earned.append(badge)

        return newly_earned

    def _resolve_metric_value(self, user_id: int, stats: UserProgress, criteria_type: str) -> int:
        mapping = {
            'lesson_count': stats.lessons_completed,
            'quiz_count': stats.quizzes_passed,
            'exercise_count': stats.exercises_solved,
            'streak_days': stats.current_streak_days,
        }
        return mapping.get(criteria_type, 0)

    def _award_badge(self, user_id: int, badge: Badge):
        user_badge = UserBadge(user_id=user_id, badge_id=badge.id)
        self.db.add(user_badge)
        
        # Dispatch XP reward increment asynchronously
        # user_xp_log will contain 'badge_earned' reference
        self.db.commit()
```
