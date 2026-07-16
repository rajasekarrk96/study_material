"""
Learning OS — Learning Paths Domain Models
LearningPath, PathCourse, PathPrerequisite, UserCourseProgress, UserLessonProgress.
"""
from datetime import datetime
from app.core.extensions import db
from app.core.base_model import TimestampMixin


class LearningPath(db.Model, TimestampMixin):
    __tablename__ = "learning_paths"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(280), unique=True, nullable=False)
    description = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    courses = db.relationship("PathCourse", back_populates="path", order_by="PathCourse.sort_order", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<LearningPath {self.title}>"


class PathCourse(db.Model):
    __tablename__ = "path_courses"

    id = db.Column(db.Integer, primary_key=True)
    path_id = db.Column(db.Integer, db.ForeignKey("learning_paths.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    sort_order = db.Column(db.Integer, default=0, nullable=False)

    path = db.relationship("LearningPath", back_populates="courses")
    course = db.relationship("Course")

    def __repr__(self):
        return f"<PathCourse path={self.path_id} course={self.course_id}>"


class PathPrerequisite(db.Model):
    __tablename__ = "path_prerequisites"

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    prerequisite_course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)

    course = db.relationship("Course", foreign_keys=[course_id])
    prerequisite = db.relationship("Course", foreign_keys=[prerequisite_course_id])

    def __repr__(self):
        return f"<PathPrerequisite course={self.course_id} prereq={self.prerequisite_course_id}>"


class UserCourseProgress(db.Model, TimestampMixin):
    __tablename__ = "user_course_progress"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    is_completed = db.Column(db.Boolean, default=False, nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<UserCourseProgress user={self.user_id} course={self.course_id} completed={self.is_completed}>"


class UserLessonProgress(db.Model, TimestampMixin):
    __tablename__ = "user_lesson_progress"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey("lessons.id"), nullable=False)
    is_completed = db.Column(db.Boolean, default=False, nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<UserLessonProgress user={self.user_id} lesson={self.lesson_id} completed={self.is_completed}>"
