"""
Learning OS — Sandbox Domain Models
Exercise, ExerciseTestCase, ExerciseSubmission.
"""
from datetime import datetime
from app.core.extensions import db
from app.core.base_model import TimestampMixin


class Exercise(db.Model, TimestampMixin):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey("lessons.id"), nullable=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(280), unique=True, nullable=False)
    description = db.Column(db.Text)
    instruction_markdown = db.Column(db.Text)
    starter_code = db.Column(db.Text)
    programming_language = db.Column(db.String(50), default="python")  # 'python', 'java', 'sql', 'javascript'
    xp_reward = db.Column(db.Integer, default=30)
    is_active = db.Column(db.Boolean, default=True)

    test_cases = db.relationship("ExerciseTestCase", back_populates="exercise", cascade="all, delete-orphan")
    submissions = db.relationship("ExerciseSubmission", back_populates="exercise", cascade="all, delete")

    def __repr__(self):
        return f"<Exercise {self.title}>"


class ExerciseTestCase(db.Model):
    __tablename__ = "exercise_test_cases"

    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"), nullable=False)
    input_data = db.Column(db.Text)                                    # Standard input passed to program
    expected_output = db.Column(db.Text, nullable=False)               # Expected standard output
    is_hidden = db.Column(db.Boolean, default=False, nullable=False)

    exercise = db.relationship("Exercise", back_populates="test_cases")

    def __repr__(self):
        return f"<ExerciseTestCase id={self.id} hidden={self.is_hidden}>"


class ExerciseSubmission(db.Model):
    __tablename__ = "exercise_submissions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"), nullable=False)
    source_code = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default="pending")               # 'accepted', 'wrong_answer', 'runtime_error', 'compile_error'
    stdout = db.Column(db.Text)
    stderr = db.Column(db.Text)
    runtime = db.Column(db.Float)                                      # runtime in seconds
    memory_usage = db.Column(db.Integer)                               # memory usage in KB
    language = db.Column(db.String(50))                                # programming language used
    test_results = db.Column(db.JSON)                                  # detailed breakdown of test case results
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    exercise = db.relationship("Exercise", back_populates="submissions")

    def __repr__(self):
        return f"<ExerciseSubmission id={self.id} status={self.status}>"
