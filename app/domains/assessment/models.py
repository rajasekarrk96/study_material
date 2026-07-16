"""
Learning OS — Assessment Domain Models
Quiz, Question, Option, QuizAttempt, QuizAnswer.
"""
from datetime import datetime
from app.core.extensions import db
from app.core.base_model import TimestampMixin


class Quiz(db.Model, TimestampMixin):
    __tablename__ = "quizzes"

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey("lessons.id"), nullable=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(280), unique=True, nullable=False)
    description = db.Column(db.Text)
    time_limit_seconds = db.Column(db.Integer, default=0)             # 0 means unlimited
    passing_score = db.Column(db.Integer, default=70)                 # Percentage (e.g., 70 for 70%)
    xp_reward = db.Column(db.Integer, default=50)
    is_active = db.Column(db.Boolean, default=True)

    questions = db.relationship("Question", back_populates="quiz", cascade="all, delete-orphan")
    attempts = db.relationship("QuizAttempt", back_populates="quiz", cascade="all, delete")

    def __repr__(self):
        return f"<Quiz {self.title}>"


class Question(db.Model, TimestampMixin):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey("quizzes.id"), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    question_type = db.Column(db.String(50), default="multiple_choice")  # 'multiple_choice', 'true_false', 'text'
    explanation = db.Column(db.Text)
    points = db.Column(db.Integer, default=10)
    sort_order = db.Column(db.Integer, default=0)

    quiz = db.relationship("Quiz", back_populates="questions")
    options = db.relationship("Option", back_populates="question", cascade="all, delete-orphan")
    answers = db.relationship("QuizAnswer", back_populates="question", cascade="all, delete")

    def __repr__(self):
        return f"<Question id={self.id} type={self.question_type}>"


class Option(db.Model):
    __tablename__ = "options"

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)
    option_text = db.Column(db.Text, nullable=False)
    is_correct = db.Column(db.Boolean, default=False, nullable=False)
    sort_order = db.Column(db.Integer, default=0)

    question = db.relationship("Question", back_populates="options")

    def __repr__(self):
        return f"<Option id={self.id} is_correct={self.is_correct}>"


class QuizAttempt(db.Model):
    __tablename__ = "quiz_attempts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey("quizzes.id"), nullable=False)
    started_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True)
    score = db.Column(db.Integer, default=0)                          # Final percentage (0-100)
    is_passed = db.Column(db.Boolean, default=False, nullable=False)
    xp_earned = db.Column(db.Integer, default=0)

    quiz = db.relationship("Quiz", back_populates="attempts")
    answers = db.relationship("QuizAnswer", back_populates="attempt", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<QuizAttempt id={self.id} user={self.user_id} score={self.score}>"


class QuizAnswer(db.Model):
    __tablename__ = "quiz_answers"

    id = db.Column(db.Integer, primary_key=True)
    attempt_id = db.Column(db.Integer, db.ForeignKey("quiz_attempts.id"), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)
    selected_option_id = db.Column(db.Integer, db.ForeignKey("options.id"), nullable=True)
    text_answer = db.Column(db.Text, nullable=True)                   # Used for free-text questions
    is_correct = db.Column(db.Boolean, default=False, nullable=False)

    attempt = db.relationship("QuizAttempt", back_populates="answers")
    question = db.relationship("Question", back_populates="answers")
