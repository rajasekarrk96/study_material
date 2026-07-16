# 07 — Learning Engine

> The Learning Engine controls course enrollment, progression, lesson sequencing, prerequisites, and learning paths.

---

## 7.1 Learning Paths & Course Sequences

A **Learning Path** is a structured curriculum containing multiple courses.
Courses within a path can be sequential, parallel, or optional.

```
                  ┌───────────────┐
                  │ Python Basics │
                  └───────┬───────┘
                          │
            ┌─────────────┴─────────────┐
            ▼                           ▼
┌───────────────────────┐   ┌───────────────────────┐
│  Advanced Python OOP  │   │  Flask Web Framework  │
└───────────┬───────────┘   └───────────┬───────────┘
            │                           │
            └─────────────┬─────────────┘
                          ▼
             ┌─────────────────────────┐
             │ AI & Machine Learning   │
             └─────────────────────────┘
```

---

## 7.2 Prerequisites Validation

Prerequisites can exist at multiple levels:
1. **Path Level**: Path B requires Path A to be completed first.
2. **Course Level**: Course Y requires Course X to be completed first.
3. **Lesson Level**: Lesson 2 requires Lesson 1 to be completed first (within a course/module).

### Prerequisites Evaluation Engine

```python
# app/domains/learning_paths/service.py

class LearningEngineService:
    def __init__(self, course_repo, progress_repo):
        self.course_repo = course_repo
        self.progress_repo = progress_repo

    def can_student_access_lesson(self, user_id: int, lesson_id: int) -> bool:
        """
        Verify if a student has completed all prerequisites for a given lesson.
        """
        lesson = self.course_repo.get_lesson_by_id(lesson_id)
        if not lesson:
            return False

        # 1. Check Course-level prerequisites
        course = lesson.module.course
        course_prereqs = self.course_repo.get_course_prerequisites(course.id)
        for prereq in course_prereqs:
            completed = self.progress_repo.is_course_completed(user_id, prereq.prerequisite_course_id)
            if not completed:
                return False

        # 2. Check Module-level sequencing (if enabled)
        if course.sequencing_enabled:
            # Get previous modules in the course
            prev_modules = self.course_repo.get_previous_modules(course.id, lesson.module.sort_order)
            for module in prev_modules:
                if not self.progress_repo.is_module_completed(user_id, module.id):
                    return False

            # Get previous lessons in current module
            prev_lessons = self.course_repo.get_previous_lessons(lesson.module_id, lesson.sort_order)
            for prev_lesson in prev_lessons:
                if not self.progress_repo.is_lesson_completed(user_id, prev_lesson.id):
                    return False

        return True
```

---

## 7.3 Study Planners & Revision Schedules

To prevent knowledge decay, the Learning OS uses a **Spaced Repetition System (SRS)** to schedule review sessions for completed lessons.

```
Lesson Completed (Day 0)
    │
    ├─► Review 1 (Day 1) ─── Success? ───► Review 2 (Day 4) ─── Success? ───► Review 3 (Day 10)
    │                                          │                                   │
    └─► Review Failure ────────────────────────┴───────────────────────────────────┴─► Reset (Day +1)
```

### Spaced Repetition Scheduling Algorithm (Modified SuperMemo-2)

The SM-2 algorithm calculates the next interval ($I$) and Ease Factor ($EF$) for reviewing card decks or revision summaries:

$$I(1) = 1 \text{ day}$$
$$I(2) = 6 \text{ days}$$
$$\text{For } n > 2: I(n) = I(n-1) \times EF$$

Where the Ease Factor is adjusted based on student feedback confidence (0-5 scale):

$$EF' = EF + (0.1 - (5 - q) \times (0.08 + (5 - q) \times 0.02))$$

```python
# app/domains/flashcard/service.py

def calculate_next_review(confidence: int, prev_interval: int, prev_ease_factor: float) -> tuple[int, float]:
    """
    confidence: User response score (0 = Forgot, 5 = Perfect recall)
    returns: (next_interval_days, next_ease_factor)
    """
    if confidence < 3:
        # User forgot/struggled: reset interval but maintain base review sequence
        return 1, max(1.3, prev_ease_factor - 0.2)

    if prev_interval == 0:
        new_interval = 1
        new_ease_factor = prev_ease_factor
    elif prev_interval == 1:
        new_interval = 6
        new_ease_factor = prev_ease_factor
    else:
        new_ease_factor = prev_ease_factor + (0.1 - (5 - confidence) * (0.08 + (5 - confidence) * 0.02))
        new_ease_factor = max(1.3, new_ease_factor)
        new_interval = int(round(prev_interval * new_ease_factor))

    # Cap interval at 365 days
    new_interval = min(new_interval, 365)
    return new_interval, new_ease_factor
```

---

## 7.4 Content Delivery Options

1. **Self-Paced / Open Catalog**: Students can browse and enroll in any course at any time. Prerequisites are evaluated before entering lessons.
2. **Locked / Structured Sequencing**: Students must complete courses and paths in absolute sequential order. Recommended for institutional learning deployments.
3. **Cohort-Based Drip Feed**: Modules unlock based on time since enrollment (e.g., Module 2 unlocks exactly 7 days after enrollment). Managed through background job queue checks.
