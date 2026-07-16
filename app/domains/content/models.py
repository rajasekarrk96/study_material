"""
Learning OS — Content Domain Models
Category, Subject, Course, Module, Lesson, LessonSection, LessonVersion, Tag, Source.
"""
from datetime import datetime
from app.core.extensions import db
from app.core.base_model import TimestampMixin, SoftDeleteMixin
from app.core.constants import ContentStatus, DifficultyLevel, SectionType


class Category(db.Model, TimestampMixin):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    slug = db.Column(db.String(120), unique=True, nullable=False)
    type = db.Column(db.String(50), default="technical")               # 'technical', 'non_technical'
    description = db.Column(db.Text)
    icon = db.Column(db.String(100))
    color = db.Column(db.String(20))
    sort_order = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)

    subjects = db.relationship("Subject", back_populates="category", lazy="dynamic")

    def __repr__(self):
        return f"<Category {self.name}>"


class Subject(db.Model, TimestampMixin):
    __tablename__ = "subjects"

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(170), unique=True, nullable=False)
    description = db.Column(db.Text)
    icon = db.Column(db.String(100))
    logo_url = db.Column(db.String(500))
    difficulty_level = db.Column(db.String(20), default=DifficultyLevel.BEGINNER)
    sort_order = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)

    category = db.relationship("Category", back_populates="subjects")
    courses = db.relationship("Course", back_populates="subject", lazy="dynamic")

    def __repr__(self):
        return f"<Subject {self.name}>"


class Course(db.Model, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(280), unique=True, nullable=False)
    description = db.Column(db.Text)
    long_description = db.Column(db.Text)
    thumbnail_url = db.Column(db.String(500))
    difficulty_level = db.Column(db.String(20), default=DifficultyLevel.BEGINNER)
    status = db.Column(db.String(30), default=ContentStatus.DRAFT)
    language = db.Column(db.String(10), default="en")
    estimated_hours = db.Column(db.Integer, default=0)
    is_free = db.Column(db.Boolean, default=True)
    is_featured = db.Column(db.Boolean, default=False)
    meta_title = db.Column(db.String(255))
    meta_description = db.Column(db.String(500))
    view_count = db.Column(db.Integer, default=0)
    enrollment_count = db.Column(db.Integer, default=0)
    published_at = db.Column(db.DateTime)

    subject = db.relationship("Subject", back_populates="courses")
    modules = db.relationship("Module", back_populates="course",
                               order_by="Module.sort_order", lazy="dynamic")

    def __repr__(self):
        return f"<Course {self.slug}>"


class Module(db.Model, TimestampMixin):
    __tablename__ = "modules"

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(280), nullable=False)
    description = db.Column(db.Text)
    sort_order = db.Column(db.Integer, default=0)
    is_published = db.Column(db.Boolean, default=False)

    course = db.relationship("Course", back_populates="modules")
    lessons = db.relationship("Lesson", back_populates="module",
                               order_by="Lesson.sort_order", lazy="dynamic")

    def __repr__(self):
        return f"<Module {self.title}>"


class Lesson(db.Model, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "lessons"

    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey("modules.id"), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(280), nullable=False)
    summary = db.Column(db.Text)
    status = db.Column(db.String(30), default=ContentStatus.DRAFT)
    sort_order = db.Column(db.Integer, default=0)
    estimated_minutes = db.Column(db.Integer, default=15)
    difficulty_level = db.Column(db.String(20), default=DifficultyLevel.BEGINNER)
    completeness_score = db.Column(db.Integer, default=0)
    meta_title = db.Column(db.String(255))
    meta_description = db.Column(db.String(500))
    canonical_url = db.Column(db.String(500))
    view_count = db.Column(db.Integer, default=0)
    published_at = db.Column(db.DateTime)

    module = db.relationship("Module", back_populates="lessons")
    sections = db.relationship("LessonSection", back_populates="lesson",
                                order_by="LessonSection.sort_order")
    versions = db.relationship("LessonVersion", back_populates="lesson",
                                order_by="LessonVersion.version_number.desc()")
    tags = db.relationship("Tag", secondary="lesson_tags", backref="lessons")

    def __repr__(self):
        return f"<Lesson {self.slug}>"


class LessonSection(db.Model, TimestampMixin):
    __tablename__ = "lesson_sections"

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey("lessons.id"), nullable=False)
    section_type = db.Column(db.String(50), nullable=False)           # SectionType enum value
    title = db.Column(db.String(255))
    content_markdown = db.Column(db.Text)
    content_html = db.Column(db.Text)
    sort_order = db.Column(db.Integer, default=0)
    is_visible = db.Column(db.Boolean, default=True)

    lesson = db.relationship("Lesson", back_populates="sections")

    def __repr__(self):
        return f"<LessonSection {self.section_type} for lesson {self.lesson_id}>"


class LessonVersion(db.Model):
    __tablename__ = "lesson_versions"

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey("lessons.id"), nullable=False)
    version_number = db.Column(db.Integer, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    content_snapshot = db.Column(db.JSON)
    change_summary = db.Column(db.String(500))
    status = db.Column(db.String(30))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    lesson = db.relationship("Lesson", back_populates="versions")

    def __repr__(self):
        return f"<LessonVersion {self.lesson_id} v{self.version_number}>"


class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    slug = db.Column(db.String(120), unique=True, nullable=False)
    category = db.Column(db.String(50))
    usage_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Tag {self.name}>"


# Association table for Lesson <-> Tag
lesson_tags = db.Table(
    "lesson_tags",
    db.Column("lesson_id", db.Integer, db.ForeignKey("lessons.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id"), primary_key=True),
    db.Column("added_at", db.DateTime, default=datetime.utcnow),
)


class Source(db.Model, TimestampMixin):
    __tablename__ = "sources"

    id = db.Column(db.Integer, primary_key=True)
    source_type = db.Column(db.String(50))    # 'youtube_video', 'official_docs', 'book' etc.
    title = db.Column(db.String(500), nullable=False)
    url = db.Column(db.String(1000))
    author_name = db.Column(db.String(200))
    platform = db.Column(db.String(100))
    description = db.Column(db.Text)
    thumbnail_url = db.Column(db.String(500))
    published_date = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Source {self.source_type}: {self.title[:40]}>"


class ContentQualityScore(db.Model):
    __tablename__ = "content_quality_scores"

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey("lessons.id"), nullable=False)
    readability_score = db.Column(db.Float, nullable=False)       # Flesch Reading Ease
    plagiarism_percentage = db.Column(db.Float, default=0.0, nullable=False)
    automated_feedback = db.Column(db.Text)
    checked_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    lesson = db.relationship("Lesson")

    def __repr__(self):
        return f"<ContentQualityScore lesson={self.lesson_id} readability={self.readability_score}>"
