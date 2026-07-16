# 10 — Quiz Engine

> The Quiz Engine creates, validates, grades, and logs MCQ, True/False, and fill-in-the-blank assessments.

---

## 10.1 Question Bank Schema

A **Question Bank** holds reusable questions tagged by difficulty, course, subject, and topic keywords.

```
       ┌────────────────────────┐
       │     Question Bank      │
       └───────────┬────────────┘
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
┌─────────────────┐ ┌─────────────────┐
│ Course: Python  │ │   Subject: SQL  │
│ Topic: Loop     │ │   Topic: JOIN   │
└─────────────────┘ └─────────────────┘
```

---

## 10.2 Quiz Attempts Lifecycle

```
[Student Start] ──► [Generate Session] ──► [Record Start Time] ──► [Collect Answers]
                                                                          │
[Complete Results] ◄── [Verify Timeout] ◄── [Calculate Score] ◄─────── [Submit]
```

To prevent answer leakages, options are shuffled dynamically per user session if `shuffle_options` is enabled on the Quiz model.

---

## 10.3 Dynamic Options Model

```python
# app/domains/quiz/models.py

class Quiz(db.Model):
    __tablename__ = 'quizzes'
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'))
    title = db.Column(db.String(255), nullable=False)
    passing_score_percent = db.Column(db.Integer, default=70)
    time_limit_seconds = db.Column(db.Integer, default=600)  # 10 mins default
    max_attempts = db.Column(db.Integer, default=3)
    shuffle_questions = db.Column(db.Boolean, default=True)

class Question(db.Model):
    __tablename__ = 'quiz_questions'
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'))
    question_text = db.Column(db.Text, nullable=False)
    question_type = db.Column(db.String(50))  # 'MCQ', 'TF', 'FIB'
    explanation_text = db.Column(db.Text)
    sort_order = db.Column(db.Integer, default=0)

class Option(db.Model):
    __tablename__ = 'quiz_options'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('quiz_questions.id'))
    option_text = db.Column(db.Text, nullable=False)
    is_correct = db.Column(db.Boolean, default=False)
```

---

## 10.4 Auto-Grading & Validation Engine

Answers are verified on submission. If a session times out, the score calculation handles only answers stored up to the expiry timestamp.

```python
# app/domains/quiz/service.py

from datetime import datetime
from app.domains.quiz.models import QuizAttempt, QuizAnswer

class QuizGradingService:
    def __init__(self, db_session):
        self.db = db_session

    def grade_attempt(self, attempt_id: int, student_answers: list[dict]) -> QuizAttempt:
        """
        student_answers format: [{'question_id': 1, 'selected_option_id': 3}]
        """
        attempt = self.db.query(QuizAttempt).filter_by(id=attempt_id).first()
        if not attempt or attempt.completed_at is not None:
            return attempt

        quiz = attempt.quiz
        questions = quiz.questions
        total_questions = len(questions)

        # Timeout validation
        time_limit = quiz.time_limit_seconds
        now = datetime.utcnow()
        elapsed_seconds = (now - attempt.started_at).total_seconds()
        
        is_timed_out = elapsed_seconds > time_limit if time_limit else False

        correct_count = 0
        points_earned = 0

        # Preload options to avoid N+1 queries
        for q in questions:
            # Match answer payload
            ans_payload = next((item for item in student_answers if item['question_id'] == q.id), None)
            
            selected_id = ans_payload.get('selected_option_id') if ans_payload else None
            is_correct = False
            
            if selected_id:
                # Retrieve correct options
                correct_option = next((opt for opt in q.options if opt.is_correct), None)
                if correct_option and correct_option.id == selected_id:
                    is_correct = True
                    correct_count += 1

            # Log dynamic answers
            answer = QuizAnswer(
                attempt_id=attempt.id,
                question_id=q.id,
                selected_option_id=selected_id,
                is_correct=is_correct
            )
            self.db.add(answer)

        # Update attempt totals
        attempt.completed_at = now
        attempt.score = correct_count
        attempt.total_points = total_questions
        attempt.percentage = (correct_count / total_questions) * 100 if total_questions > 0 else 0
        attempt.passed = attempt.percentage >= quiz.passing_score_percent
        attempt.time_taken_seconds = int(elapsed_seconds)

        self.db.commit()
        return attempt
```
