#!/usr/bin/env python3
"""
EduSphere — HTML → Database Migration Script
=============================================
Scans existing HTML lesson files in Core_Python/, Core_Java/,
Java_Selenium/, My_Sql/ and imports them as structured CMS content
into the database.

Usage:
    python scripts/migrate_html.py [--dry-run]
"""
import sys
import os
import re
import argparse
from pathlib import Path
from datetime import datetime

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from bs4 import BeautifulSoup

# ── COURSE MAP ────────────────────────────────────────────────
# Maps source folder → (Category, Subject, Course) metadata
COURSE_MAP = {
    "Core_Python": {
        "subpath": "",
        "category": {"name": "Programming Languages", "slug": "programming-languages",
                     "type": "technical", "icon": "fas fa-code", "color": "#3b82f6"},
        "subject":  {"name": "Python", "slug": "python",
                     "icon": "fab fa-python", "difficulty": "beginner"},
        "course":   {"title": "Core Python", "slug": "core-python",
                     "description": "Master Python from fundamentals to advanced concepts.",
                     "difficulty": "beginner", "estimated_hours": 40},
        "module":   {"title": "Core Concepts", "slug": "core-concepts"},
    },
    "Core_Java": {
        "subpath": "",
        "category": {"name": "Programming Languages", "slug": "programming-languages",
                     "type": "technical", "icon": "fas fa-code", "color": "#3b82f6"},
        "subject":  {"name": "Java", "slug": "java",
                     "icon": "fab fa-java", "difficulty": "intermediate"},
        "course":   {"title": "Core Java", "slug": "core-java",
                     "description": "Comprehensive Java programming from OOP to streams.",
                     "difficulty": "intermediate", "estimated_hours": 50},
        "module":   {"title": "Core Concepts", "slug": "core-concepts"},
    },
    "Java_Selenium": {
        "subpath": "content",
        "category": {"name": "Automation & Testing", "slug": "automation-testing",
                     "type": "technical", "icon": "fas fa-robot", "color": "#22c55e"},
        "subject":  {"name": "Selenium", "slug": "selenium",
                     "icon": "fas fa-robot", "difficulty": "intermediate"},
        "course":   {"title": "Java Selenium", "slug": "java-selenium",
                     "description": "End-to-end browser automation with Java and Selenium WebDriver.",
                     "difficulty": "intermediate", "estimated_hours": 35},
        "module":   {"title": "Selenium Fundamentals", "slug": "selenium-fundamentals"},
    },
    "My_Sql": {
        "subpath": "topics",
        "category": {"name": "Databases", "slug": "databases",
                     "type": "technical", "icon": "fas fa-database", "color": "#f59e0b"},
        "subject":  {"name": "MySQL", "slug": "mysql",
                     "icon": "fas fa-database", "difficulty": "beginner"},
        "course":   {"title": "MySQL", "slug": "mysql",
                     "description": "Relational database design, queries, and optimization.",
                     "difficulty": "beginner", "estimated_hours": 25},
        "module":   {"title": "SQL Fundamentals", "slug": "sql-fundamentals"},
    },
}

# HTML files to skip (navigation/index files)
SKIP_FILES = {"index.html", "index.htm", "_template.html"}

# ── HELPERS ───────────────────────────────────────────────────

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")


def extract_title(soup: BeautifulSoup, filename: str) -> str:
    """Extract page title from <title> or <h1>."""
    title_tag = soup.find("title")
    if title_tag:
        raw = title_tag.get_text(strip=True)
        # Remove common suffixes like "- EduSphere"
        for suffix in [" - EduSphere", " — EduSphere", " | EduSphere"]:
            raw = raw.replace(suffix, "")
        if raw:
            return raw.strip()
    h1 = soup.find("h1")
    if h1:
        return h1.get_text(strip=True)
    # Fallback: filename without extension, formatted
    return Path(filename).stem.replace("_", " ").replace("-", " ").title()


def extract_main_content(soup: BeautifulSoup) -> str:
    """
    Extract the primary content section from the existing HTML structure.
    Removes nav, header, sidebar, footer boilerplate.
    """
    # Remove known navigation/layout elements
    for tag in soup.find_all(["header", "footer", "nav", "script", "style",
                               "aside", "noscript"]):
        tag.decompose()

    # Try known content wrapper selectors
    for selector in [
        "main", ".content", "#content", ".main-content",
        ".lesson-content", ".topic-content", "article"
    ]:
        content = soup.select_one(selector)
        if content:
            return str(content)

    # Try the biggest div
    divs = soup.find_all("div")
    if divs:
        biggest = max(divs, key=lambda d: len(d.get_text()))
        return str(biggest)

    return str(soup.body or soup)


def guess_summary(soup: BeautifulSoup) -> str:
    """Pull first meaningful paragraph as the lesson summary."""
    # Try meta description first
    meta = soup.find("meta", attrs={"name": "description"})
    if meta and meta.get("content", "").strip():
        return meta["content"].strip()
    for p in soup.find_all("p"):
        text = p.get_text(strip=True)
        if len(text) > 60:
            return text[:300]
    return ""


# ── MAIN MIGRATION LOGIC ──────────────────────────────────────

def run_migration(dry_run: bool = False):
    from app import create_app
    from app.core.extensions import db
    from app.domains.content.models import (
        Category, Subject, Course, Module, Lesson, LessonSection
    )
    from app.core.constants import ContentStatus

    app = create_app()
    project_root = Path(__file__).resolve().parent.parent

    with app.app_context():
        total_lessons = 0
        skipped = 0

        for folder_name, meta in COURSE_MAP.items():
            folder_path = project_root / folder_name
            if meta.get("subpath"):
                folder_path = folder_path / meta["subpath"]
                
            if not folder_path.exists():
                print(f"  [SKIP] Folder not found: {folder_path}")
                continue

            html_files = sorted([
                f for f in folder_path.glob("*.html")
                if f.name.lower() not in SKIP_FILES
            ])

            if not html_files:
                print(f"  [SKIP] No HTML files in: {folder_name}")
                continue

            print(f"\n[DIR] Processing: {folder_name} ({len(html_files)} files)")

            if not dry_run:
                # ── Category
                cat_data = meta["category"]
                category = Category.query.filter_by(slug=cat_data["slug"]).first()
                if not category:
                    category = Category(
                        name=cat_data["name"],
                        slug=cat_data["slug"],
                        type=cat_data["type"],
                        icon=cat_data["icon"],
                        color=cat_data["color"],
                        is_active=True,
                    )
                    db.session.add(category)
                    db.session.flush()

                # ── Subject
                subj_data = meta["subject"]
                subject = Subject.query.filter_by(slug=subj_data["slug"]).first()
                if not subject:
                    subject = Subject(
                        category_id=category.id,
                        name=subj_data["name"],
                        slug=subj_data["slug"],
                        icon=subj_data["icon"],
                        difficulty_level=subj_data["difficulty"],
                        is_active=True,
                    )
                    db.session.add(subject)
                    db.session.flush()

                # ── Course
                course_data = meta["course"]
                course = Course.query.filter_by(slug=course_data["slug"]).first()
                if not course:
                    course = Course(
                        subject_id=subject.id,
                        title=course_data["title"],
                        slug=course_data["slug"],
                        description=course_data["description"],
                        difficulty_level=course_data["difficulty"],
                        estimated_hours=course_data["estimated_hours"],
                        status=ContentStatus.PUBLISHED,
                        is_free=True,
                        is_featured=True,
                        published_at=datetime.utcnow(),
                    )
                    db.session.add(course)
                    db.session.flush()

                # ── Module
                mod_data = meta["module"]
                module = Module.query.filter_by(
                    course_id=course.id, slug=mod_data["slug"]
                ).first()
                if not module:
                    module = Module(
                        course_id=course.id,
                        title=mod_data["title"],
                        slug=mod_data["slug"],
                        is_published=True,
                        sort_order=1,
                    )
                    db.session.add(module)
                    db.session.flush()

            for sort_idx, html_file in enumerate(html_files, start=1):
                raw = html_file.read_bytes()
                soup = BeautifulSoup(raw, "html.parser")

                title = extract_title(soup, html_file.name)
                summary = guess_summary(soup)
                main_html = extract_main_content(soup)
                lesson_slug = slugify(html_file.stem)

                print(f"  {'[DRY]' if dry_run else '[IMPORT]'} {html_file.name} -> {title}")

                if dry_run:
                    continue

                # Skip if already exists
                existing = Lesson.query.filter_by(
                    module_id=module.id, slug=lesson_slug
                ).first()
                if existing:
                    print(f"    - Already exists, skipping.")
                    skipped += 1
                    continue

                lesson = Lesson(
                    module_id=module.id,
                    title=title,
                    slug=lesson_slug,
                    summary=summary,
                    status=ContentStatus.PUBLISHED,
                    sort_order=sort_idx,
                    estimated_minutes=15,
                    meta_title=title,
                    meta_description=summary[:160] if summary else "",
                    published_at=datetime.utcnow(),
                )
                db.session.add(lesson)
                db.session.flush()

                # Store full HTML as the 'overview' section
                section = LessonSection(
                    lesson_id=lesson.id,
                    section_type="overview",
                    title=f"{title} - Overview",
                    content_html=main_html,
                    content_markdown="",
                    sort_order=1,
                    is_visible=True,
                )
                db.session.add(section)
                total_lessons += 1

        if not dry_run:
            db.session.commit()
            print(f"\n[OK] Migration complete: {total_lessons} lessons imported, {skipped} skipped.")
        else:
            print(f"\n[OK] Dry run complete. {total_lessons} lessons would be imported.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Migrate HTML lessons to Learning OS database.")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing to DB.")
    args = parser.parse_args()

    print("=" * 60)
    print("  EduSphere - HTML to Database Migration")
    print(f"  Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print("=" * 60)

    run_migration(dry_run=args.dry_run)
