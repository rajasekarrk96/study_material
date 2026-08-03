"""
Learning OS — Learning Paths Domain Models  (v3.0 Modular Catalog)
==================================================================
LearningPath          — a curated sequence of courses (Python Full Stack, AI Engineer, etc.)
PathCourse            — join table: path ↔ course, with section label + required flag
PathPrerequisite      — per-course prerequisite graph
UserCourseProgress    — user progress per individual course
UserLessonProgress    — user progress per individual lesson
UserLearningPathProgress  — user progress across an entire learning path
LearningPathCertificate   — certificate definition for completing a path
UserLearningPathCertificate — issued path-level certificates
"""
from datetime import datetime
from app.core.extensions import db
from app.core.base_model import TimestampMixin


# ─────────────────────────────────────────────────────────────
# Learning Path  (single curated program referencing N courses)
# ─────────────────────────────────────────────────────────────

class LearningPath(db.Model, TimestampMixin):
    __tablename__ = "learning_paths"

    id               = db.Column(db.Integer, primary_key=True)
    title            = db.Column(db.String(255), nullable=False)
    slug             = db.Column(db.String(280), unique=True, nullable=False)
    description      = db.Column(db.Text)
    target_role      = db.Column(db.String(150))          # e.g. "Python Full Stack Developer"
    difficulty_level = db.Column(db.String(20), default="beginner")  # beginner|intermediate|advanced
    estimated_hours  = db.Column(db.Integer, default=0)   # auto-calculated from path courses
    icon             = db.Column(db.String(100))           # FontAwesome class e.g. "fab fa-python"
    color            = db.Column(db.String(20))            # hex e.g. "#4f46e5"
    thumbnail_url    = db.Column(db.String(500))
    is_active        = db.Column(db.Boolean, default=True, nullable=False)
    is_featured      = db.Column(db.Boolean, default=False, nullable=False)
    sort_order       = db.Column(db.Integer, default=0)

    courses     = db.relationship(
        "PathCourse",
        back_populates="path",
        order_by="PathCourse.sort_order",
        cascade="all, delete-orphan"
    )
    certificate = db.relationship(
        "LearningPathCertificate",
        back_populates="path",
        uselist=False,
        cascade="all, delete-orphan"
    )

    # ── computed helpers ─────────────────────────────────────
    @property
    def required_courses(self):
        return [pc for pc in self.courses if pc.is_required]

    @property
    def total_courses_count(self):
        return len(self.courses)

    def __repr__(self):
        return f"<LearningPath {self.title}>"


# ─────────────────────────────────────────────────────────────
# PathCourse  (join: LearningPath ↔ Course)
# ─────────────────────────────────────────────────────────────

class PathCourse(db.Model):
    __tablename__ = "path_courses"

    id            = db.Column(db.Integer, primary_key=True)
    path_id       = db.Column(db.Integer, db.ForeignKey("learning_paths.id"), nullable=False)
    course_id     = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    sort_order    = db.Column(db.Integer, default=0, nullable=False)
    is_required   = db.Column(db.Boolean, default=True, nullable=False)
    section_label = db.Column(db.String(100))   # e.g. "Frontend", "Backend", "Database"

    path   = db.relationship("LearningPath", back_populates="courses")
    course = db.relationship("Course")

    def __repr__(self):
        return f"<PathCourse path={self.path_id} course={self.course_id} section={self.section_label}>"


# ─────────────────────────────────────────────────────────────
# PathPrerequisite  (per-course prerequisite graph)
# ─────────────────────────────────────────────────────────────

class PathPrerequisite(db.Model):
    __tablename__ = "path_prerequisites"

    id                     = db.Column(db.Integer, primary_key=True)
    course_id              = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    prerequisite_course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)

    course       = db.relationship("Course", foreign_keys=[course_id])
    prerequisite = db.relationship("Course", foreign_keys=[prerequisite_course_id])

    def __repr__(self):
        return f"<PathPrerequisite course={self.course_id} prereq={self.prerequisite_course_id}>"


# ─────────────────────────────────────────────────────────────
# User Progress Models
# ─────────────────────────────────────────────────────────────

class UserCourseProgress(db.Model, TimestampMixin):
    __tablename__ = "user_course_progress"

    id           = db.Column(db.Integer, primary_key=True)
    user_id      = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    course_id    = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    is_completed = db.Column(db.Boolean, default=False, nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<UserCourseProgress user={self.user_id} course={self.course_id} completed={self.is_completed}>"


class UserLessonProgress(db.Model, TimestampMixin):
    __tablename__ = "user_lesson_progress"

    id           = db.Column(db.Integer, primary_key=True)
    user_id      = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    lesson_id    = db.Column(db.Integer, db.ForeignKey("lessons.id"), nullable=False)
    is_completed = db.Column(db.Boolean, default=False, nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<UserLessonProgress user={self.user_id} lesson={self.lesson_id} completed={self.is_completed}>"


class UserLearningPathProgress(db.Model, TimestampMixin):
    """Tracks a user's overall progress across a full learning path."""
    __tablename__ = "user_learning_path_progress"

    id                  = db.Column(db.Integer, primary_key=True)
    user_id             = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    path_id             = db.Column(db.Integer, db.ForeignKey("learning_paths.id"), nullable=False)
    enrolled_at         = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    completed_courses   = db.Column(db.Integer, default=0, nullable=False)
    total_courses       = db.Column(db.Integer, default=0, nullable=False)   # snapshot at enrollment
    is_completed        = db.Column(db.Boolean, default=False, nullable=False)
    completed_at        = db.Column(db.DateTime, nullable=True)

    path = db.relationship("LearningPath")

    @property
    def progress_percentage(self):
        if not self.total_courses:
            return 0
        return min(100, int((self.completed_courses / self.total_courses) * 100))

    def __repr__(self):
        return f"<UserLearningPathProgress user={self.user_id} path={self.path_id} pct={self.progress_percentage}%>"


# ─────────────────────────────────────────────────────────────
# Learning Path Certificates
# ─────────────────────────────────────────────────────────────

class LearningPathCertificate(db.Model, TimestampMixin):
    """Certificate definition for completing an entire learning path."""
    __tablename__ = "learning_path_certificates"

    id          = db.Column(db.Integer, primary_key=True)
    path_id     = db.Column(db.Integer, db.ForeignKey("learning_paths.id"), nullable=False, unique=True)
    title       = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    path              = db.relationship("LearningPath", back_populates="certificate")
    issued_to_users   = db.relationship(
        "UserLearningPathCertificate",
        back_populates="path_certificate",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<LearningPathCertificate path={self.path_id}>"


class UserLearningPathCertificate(db.Model, TimestampMixin):
    """Issued learning-path-level certificate to a specific user."""
    __tablename__ = "user_learning_path_certificates"

    id                   = db.Column(db.Integer, primary_key=True)
    user_id              = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    path_certificate_id  = db.Column(db.Integer, db.ForeignKey("learning_path_certificates.id"), nullable=False)
    issued_at            = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    path_certificate = db.relationship("LearningPathCertificate", back_populates="issued_to_users")

    def __repr__(self):
        return f"<UserLearningPathCertificate user={self.user_id} cert={self.path_certificate_id}>"
