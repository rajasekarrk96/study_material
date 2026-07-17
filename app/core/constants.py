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
