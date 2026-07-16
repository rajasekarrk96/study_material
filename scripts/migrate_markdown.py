#!/usr/bin/env python3
"""
Bytes and Boards Solutions — Markdown Notes to Database Ingestion Script.
Parses structured markdown knowledge blocks with YAML frontmatter and heading section anchors,
and imports them directly into the Learning OS SQLAlchemy schema database.
"""
import os
import re
import sys
import yaml
from pathlib import Path

# Add root folder to python path to resolve app imports
sys.path.append(str(Path(__file__).parent.parent))

from app import create_app
from app.core.extensions import db
from app.domains.content.models import Category, Subject, Course, Module, Lesson, LessonSection
from app.core.constants import ContentStatus, DifficultyLevel


def slugify(text: str) -> str:
    """Helper to convert string into a URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text


def parse_markdown_lesson(file_path: Path) -> dict:
    """
    Parses a markdown lesson file.
    Extracts the YAML metadata frontmatter and splits the body into sections by id anchors.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Parse YAML metadata block
    yaml_match = re.search(r"```yaml\n(.*?)\n```", content, re.DOTALL)
    if not yaml_match:
        print(f"  [Warning] Missing YAML metadata header in {file_path.name}. Skipping.")
        return {}

    frontmatter_str = yaml_match.group(1)
    try:
        metadata = yaml.safe_load(frontmatter_str)
    except Exception as e:
        print(f"  [Error] Failed to parse YAML in {file_path.name}: {e}")
        return {}

    body_text = content[yaml_match.end():]

    # 2. Split body into sections by ## headers with [id: section_type] anchors
    # Pattern matches: ## 1. Header Title [id: overview]
    section_pattern = re.compile(
        r"^##\s+\d+\.\s+(.*?)\s+\[id:\s*([\w_]+)\]\s*\n",
        re.MULTILINE
    )

    matches = list(section_pattern.finditer(body_text))
    sections = []

    for i, match in enumerate(matches):
        title = match.group(1).strip()
        section_type = match.group(2).strip()
        
        # Determine where this section's content ends (either start of next match or end of file)
        start_idx = match.end()
        end_idx = matches[i + 1].start() if i + 1 < len(matches) else len(body_text)
        section_content = body_text[start_idx:end_idx].strip()

        sections.append({
            "title": title,
            "section_type": section_type,
            "content_markdown": section_content,
            "sort_order": i + 1
        })

    metadata["sections"] = sections
    return metadata


def ingest_lesson_metadata(metadata: dict) -> None:
    """Ingests parsed lesson metadata and sections into the database tables."""
    # Ensure Development Tools category exists
    category = Category.query.filter_by(slug="development-tools").first()
    if not category:
        category = Category(
            name="Development Tools",
            slug="development-tools",
            type="technical",
            icon="fas fa-tools",
            color="#4f46e5"
        )
        db.session.add(category)
        db.session.flush()

    # Ensure Subject exists
    subject_name = metadata.get("subject", "Git")
    subject_slug = slugify(subject_name)
    subject = Subject.query.filter_by(slug=subject_slug).first()
    if not subject:
        subject = Subject(
            category_id=category.id,
            name=subject_name,
            slug=subject_slug,
            icon="fab fa-git-alt",
            difficulty_level="beginner"
        )
        db.session.add(subject)
        db.session.flush()

    # Ensure Course exists
    course_name = metadata.get("course", "Git Fundamentals")
    course_slug = slugify(course_name)
    course = Course.query.filter_by(slug=course_slug).first()
    if not course:
        course = Course(
            subject_id=subject.id,
            title=course_name,
            slug=course_slug,
            description=f"Learn {course_name} from scratch.",
            difficulty_level="beginner",
            status="published",
            language="en"
        )
        db.session.add(course)
        db.session.flush()

    # Ensure Module exists
    module_name = metadata.get("module", "Introduction")
    module_slug = slugify(module_name)
    module = Module.query.filter_by(course_id=course.id, slug=module_slug).first()
    if not module:
        module = Module(
            course_id=course.id,
            title=module_name,
            slug=module_slug,
            is_published=True
        )
        db.session.add(module)
        db.session.flush()

    # Create or update Lesson
    lesson_id = metadata.get("lesson_id", "GIT-001")
    lesson_title = metadata.get("lesson_title", "Git Lesson")
    
    # Check if lesson exists by slug in this module
    lesson_slug = slugify(lesson_title)
    lesson = Lesson.query.filter_by(module_id=module.id, slug=lesson_slug).first()
    
    # Map difficulty rating
    diff_str = metadata.get("difficulty", "⭐")
    diff_level = DifficultyLevel.BEGINNER
    if len(diff_str) >= 3:
        diff_level = DifficultyLevel.ADVANCED
    elif len(diff_str) == 2:
        diff_level = DifficultyLevel.INTERMEDIATE

    # Extract reading time minutes
    time_breakdown = metadata.get("time_breakdown", {})
    reading_min = int(time_breakdown.get("reading", "10 min").split()[0])

    if not lesson:
        lesson = Lesson(
            module_id=module.id,
            title=lesson_title,
            slug=lesson_slug,
            summary="",
            difficulty_level=diff_level,
            estimated_minutes=reading_min,
            status=ContentStatus.PUBLISHED
        )
        db.session.add(lesson)
        db.session.flush()
    else:
        lesson.title = lesson_title
        lesson.difficulty_level = diff_level
        lesson.estimated_minutes = reading_min

    # Update overview section content as the lesson summary
    for sec in metadata.get("sections", []):
        if sec["section_type"] == "overview":
            lesson.summary = sec["content_markdown"]

    # Delete existing sections to override fresh content ingestion
    LessonSection.query.filter_by(lesson_id=lesson.id).delete()

    # Recreate sections
    for sec in metadata.get("sections", []):
        # Generate simple HTML render fallback if needed, or leave it to frontend markdown parsers
        section_el = LessonSection(
            lesson_id=lesson.id,
            section_type=sec["section_type"],
            title=sec["title"],
            content_markdown=sec["content_markdown"],
            content_html="",  # will be compiled dynamically in lesson page render templates
            sort_order=sec["sort_order"],
            is_visible=True
        )
        db.session.add(section_el)

    db.session.commit()
    print(f"  [Success] Ingested Lesson: '{lesson_title}' ({lesson_id})")


def run_markdown_migration():
    """Finds and parses all markdown notes, importing them into the database."""
    print("=" * 60)
    print("  Bytes and Boards Solutions - Markdown Curriculum Ingestion")
    print("=" * 60)

    app = create_app()
    with app.app_context():
        notes_dir = Path("docs/notes preparing implementation/_01_git")
        if not notes_dir.exists():
            print(f"[Error] Notes folder '{notes_dir}' does not exist.")
            return

        # Scan all .md files in notes preparing implementation folder (exclude template and curriculum outline)
        files = sorted(notes_dir.glob("*.md"))
        for file in files:
            if file.name.startswith("_01_01_") or file.name.startswith("_01_02_"):
                # Skip outline and template
                continue

            print(f"Processing: {file.name}...")
            lesson_metadata = parse_markdown_lesson(file)
            if lesson_metadata:
                # Use filename stem title (excluding prefix) as the lesson title if not inside yaml
                if "lesson_title" not in lesson_metadata:
                    title_clean = file.stem
                    # Remove sequential prefix like _01_03_
                    title_clean = re.sub(r"^_\d+_\d+_", "", title_clean)
                    title_clean = title_clean.replace("_", " ").replace("-", " ").title()
                    lesson_metadata["lesson_title"] = title_clean

                ingest_lesson_metadata(lesson_metadata)

    print("\nMigration finished successfully!")


if __name__ == "__main__":
    run_markdown_migration()
