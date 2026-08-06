"""
Learning OS — Constants & Enums
Single source of truth for all status codes and type enumerations.
"""
from enum import Enum


class ContentStatus(str, Enum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    IN_REVIEW = "in_review"
    CHANGES_REQUESTED = "changes_requested"
    APPROVED = "approved"
    PUBLISHED = "published"
    ARCHIVED = "archived"
    SCHEDULED = "scheduled"


class DifficultyLevel(str, Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"


class SectionType(str, Enum):
    OVERVIEW = "overview"
    CONCEPTS = "concepts"
    SYNTAX = "syntax"
    EXAMPLES = "examples"
    DIAGRAM = "diagram"
    BEST_PRACTICES = "best_practices"
    COMMON_MISTAKES = "common_mistakes"
    INTERVIEW_QA = "interview_qa"
    EXERCISES = "exercises"
    QUIZ = "quiz"
    CHEATSHEET = "cheatsheet"
    REVISION_NOTES = "revision_notes"
    FLASHCARDS = "flashcards"
    REFERENCES = "references"
    THEORY = "theory"
    LAB = "lab"
    SUMMARY = "summary"


class UserRole(str, Enum):
    SUPER_ADMIN = "super_admin"
    ADMIN = "admin"
    EDITOR = "editor"
    REVIEWER = "reviewer"
    AUTHOR = "author"
    MODERATOR = "moderator"
    STUDENT = "student"


class CourseCoverage(str, Enum):
    """
    Indicates how a lesson/topic is delivered in the classroom.

    COVERED_IN_CLASS    — Official classroom teaching (default).
                          Included in lectures and practical sessions.
    OPTIONAL_DISCUSSION — Notes available. Faculty may explain during
                          doubt-clearing sessions. Not guaranteed in class.
    SELF_LEARNING       — Complete notes available. Students study
                          independently. Not part of classroom teaching.
                          Useful for interview prep and industry learning.
    """
    COVERED_IN_CLASS    = "covered_in_class"
    OPTIONAL_DISCUSSION = "optional_discussion"
    SELF_LEARNING       = "self_learning"


class CourseType(str, Enum):
    """
    Four-tier catalog architecture for the Learning OS.

    FOUNDATION     — Reusable standalone course (building block).
                     Referenced by learning paths. Never duplicated.
                     Sub-categories: programming, frontend, backend, core.

    SPECIALIZATION — Domain-specific advanced course.
                     Enrollable independently.
                     Learning paths may also reference these.

    LEARNING_PATH  — Career roadmap. References courses only.
                     Never owns lesson content directly.

    ELECTIVE       — Optional add-on technology.
                     Not required by any learning path.
    """
    FOUNDATION     = "foundation"
    SPECIALIZATION = "specialization"
    LEARNING_PATH  = "learning_path"
    ELECTIVE       = "elective"


# Human-readable labels used in templates and admin UI
COURSE_COVERAGE_LABELS = {
    CourseCoverage.COVERED_IN_CLASS:    ("🟢", "Covered in Class"),
    CourseCoverage.OPTIONAL_DISCUSSION: ("🟡", "Optional Discussion"),
    CourseCoverage.SELF_LEARNING:       ("🔴", "Self Learning"),
}

COURSE_TYPE_LABELS = {
    CourseType.FOUNDATION:     ("🧱", "Foundation",     "Building block courses — reusable across all paths"),
    CourseType.SPECIALIZATION: ("🎯", "Specialization",  "Domain-specific advanced skills"),
    CourseType.LEARNING_PATH:  ("🗺️", "Learning Path",   "Career roadmap — references reusable courses"),
    CourseType.ELECTIVE:       ("⚡", "Elective",        "Optional technologies for extended skills"),
}
