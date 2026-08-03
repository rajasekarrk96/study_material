#!/usr/bin/env python3
"""
Bytes and Boards Solutions — Ultra High-Performance Master Ingestion Script.
Caches categories, subjects, courses, modules, and lessons in memory to achieve
10x faster bulk operations over TiDB Cloud MySQL SSL.
"""
import os
import re
import sys
import yaml
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

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


CATEGORIES = [
    {
        "name": "Python Full Stack",
        "slug": "python-full-stack",
        "type": "technical",
        "description": "End-to-end web development with HTML5, CSS3, JavaScript, Python, Flask, FastAPI, MySQL, and MongoDB.",
        "icon": "fas fa-laptop-code",
        "color": "#3b82f6",
        "sort_order": 1,
        "courses": ["html5", "css3", "bootstrap", "jquery", "javascript", "python", "mysql", "mongodb", "flask", "fastapi"]
    },
    {
        "name": "IoT & Hardware Full Stack",
        "slug": "iot-full-stack",
        "type": "technical",
        "description": "Embedded hardware, C/C++ microcontrollers, circuit design, PCB layout with KiCad, and end-to-end IoT projects.",
        "icon": "fas fa-microchip",
        "color": "#10b981",
        "sort_order": 2,
        "courses": ["c", "cpp", "iot-hardware", "pcb-design", "pcb", "iot-projects"]
    },
    {
        "name": "Python AI & Data Science",
        "slug": "python-ai-data-science",
        "type": "technical",
        "description": "Complete Artificial Intelligence track: Math, Data Science, Machine Learning, Deep Learning, CV, NLP, GenAI, RAG, Agents, MLOps, and Prompt Engineering.",
        "icon": "fas fa-brain",
        "color": "#8b5cf6",
        "sort_order": 3,
        "courses": ["ds-math", "python-data-science", "machine-learning", "deep-learning", "computer-vision", "nlp", "generative-ai-llms", "rag-engineering", "ai-agents", "mlops-ai-deployment", "prompt-engineering"]
    },
    {
        "name": "Databases & Business Intelligence",
        "slug": "database-bi",
        "type": "technical",
        "description": "Enterprise data management, T-SQL querying, database administration, and Power BI dashboard analytics.",
        "icon": "fas fa-database",
        "color": "#f59e0b",
        "sort_order": 4,
        "courses": ["sql-server", "power-bi"]
    },
    {
        "name": "Software Engineering & DevOps",
        "slug": "software-devops",
        "type": "technical",
        "description": "Version control with Git, Java enterprise applications, and automated browser testing with Selenium.",
        "icon": "fas fa-tools",
        "color": "#ef4444",
        "sort_order": 5,
        "courses": ["git", "java", "selenium"]
    }
]


def get_category_info(course_slug: str) -> dict:
    for cat in CATEGORIES:
        for match_key in cat["courses"]:
            if match_key in course_slug or course_slug in match_key:
                return cat
    return CATEGORIES[0]


def parse_markdown_lesson(file_path: Path) -> dict:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    frontmatter = {}
    body_text = content

    fm_match = re.search(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if fm_match:
        try:
            frontmatter = yaml.safe_load(fm_match.group(1)) or {}
            body_text = content[fm_match.end():]
        except Exception:
            pass

    if not frontmatter:
        cb_match = re.search(r"```yaml\n(.*?)\n```", content, re.DOTALL)
        if cb_match:
            try:
                frontmatter = yaml.safe_load(cb_match.group(1)) or {}
                body_text = content[cb_match.end():]
            except Exception:
                pass

    if not frontmatter and not body_text.strip():
        return {}

    # Schema v2.0 curriculum files nest module/lesson/pedagogy info under
    # "metadata" and "pedagogy" instead of the flat keys below. Promote them
    # so the rest of this script (and the ingestion loop) can keep reading
    # flat keys without knowing which schema a given file uses.
    metadata_block = frontmatter.get("metadata") or {}
    pedagogy_block = frontmatter.get("pedagogy") or {}

    if "module_title" not in frontmatter and metadata_block.get("module_title"):
        frontmatter["module_title"] = metadata_block["module_title"]

    nested_sort_order = metadata_block.get("sort_order")
    if isinstance(nested_sort_order, int):
        if "module" not in frontmatter:
            frontmatter["module"] = nested_sort_order // 100
        if "lesson" not in frontmatter:
            frontmatter["lesson"] = nested_sort_order % 100

    if "difficulty" not in frontmatter and pedagogy_block.get("difficulty"):
        frontmatter["difficulty"] = pedagogy_block["difficulty"]

    total_minutes = (pedagogy_block.get("estimated_time") or {}).get("total_minutes")
    if "duration_minutes" not in frontmatter and total_minutes:
        frontmatter["duration_minutes"] = total_minutes

    title = frontmatter.get("title") or frontmatter.get("lesson_title") or metadata_block.get("lesson_title")
    if not title:
        h1_match = re.search(r"^#\s+(.+)$", body_text, re.MULTILINE)
        if h1_match:
            title = h1_match.group(1).strip()
        else:
            title = file_path.stem.replace("_", " ").title()

    frontmatter["lesson_title"] = title

    section_pattern = re.compile(r"^##\s+(.+)$", re.MULTILINE)
    matches = list(section_pattern.finditer(body_text))
    sections = []

    if matches:
        for i, match in enumerate(matches):
            raw_title = match.group(1).strip()
            anchor_match = re.search(r"\[id:\s*([\w_]+)\]", raw_title)
            if anchor_match:
                section_type = anchor_match.group(1)
                sec_title = raw_title[:anchor_match.start()].strip()
            else:
                section_type = "content"
                sec_title = raw_title

            sec_title = re.sub(r"^\d+\.\s*", "", sec_title).strip()
            start_idx = match.end()
            end_idx = matches[i + 1].start() if i + 1 < len(matches) else len(body_text)
            sec_content = body_text[start_idx:end_idx].strip()

            sections.append({
                "title": sec_title,
                "section_type": section_type,
                "content_markdown": sec_content,
                "sort_order": i + 1
            })
    else:
        sections.append({
            "title": title,
            "section_type": "content",
            "content_markdown": body_text.strip(),
            "sort_order": 1
        })

    frontmatter["sections"] = sections
    return frontmatter


def run_markdown_migration():
    print("=" * 60)
    print("  Bytes and Boards Solutions — Ultra High-Performance Master Ingestion")
    print("=" * 60)

    app = create_app()
    with app.app_context():
        category_cache = {}
        for cdef in CATEGORIES:
            cat = Category.query.filter_by(slug=cdef["slug"]).first()
            if not cat:
                cat = Category(
                    name=cdef["name"],
                    slug=cdef["slug"],
                    type=cdef["type"],
                    description=cdef["description"],
                    icon=cdef["icon"],
                    color=cdef["color"],
                    sort_order=cdef["sort_order"],
                    is_active=True
                )
                db.session.add(cat)
                db.session.flush()
            else:
                cat.name = cdef["name"]
                cat.description = cdef["description"]
                cat.icon = cdef["icon"]
                cat.color = cdef["color"]
                cat.sort_order = cdef["sort_order"]

            category_cache[cdef["slug"]] = cat.id

        db.session.commit()

        base_dir = Path("docs/curriculum")
        if not base_dir.exists():
            print(f"[Error] Base folder '{base_dir}' does not exist.")
            return

        target_arg = sys.argv[1].lower() if len(sys.argv) > 1 else None

        course_dirs = sorted([d for d in base_dir.glob("_*") if d.is_dir()])
        if target_arg:
            course_dirs = [d for d in course_dirs if target_arg in d.name.lower()]
            print(f"  [Targeting single course]: {target_arg} -> {[d.name for d in course_dirs]}")

        total_ingested = 0

        for cdir in course_dirs:
            course_name_clean = re.sub(r"^_\d+_", "", cdir.name)
            raw_course_title = course_name_clean.replace("_", " ").title()
            course_slug = slugify(raw_course_title)


            cat_info = get_category_info(course_slug)
            cat_id = category_cache[cat_info["slug"]]

            # Ensure Subject
            subject = Subject.query.filter_by(slug=course_slug).first()
            if not subject:
                subject = Subject(
                    category_id=cat_id,
                    name=raw_course_title,
                    slug=course_slug,
                    icon=cat_info["icon"],
                    difficulty_level="beginner"
                )
                db.session.add(subject)
                db.session.flush()
            else:
                subject.category_id = cat_id

            # Ensure Course
            course = Course.query.filter_by(slug=course_slug).first()
            if not course:
                course = Course(
                    subject_id=subject.id,
                    title=raw_course_title,
                    slug=course_slug,
                    description=f"Comprehensive {raw_course_title} mastery course.",
                    difficulty_level="beginner",
                    status="published",
                    is_featured=True,
                    language="en"
                )
                db.session.add(course)
                db.session.flush()

            # Cache existing modules and lessons for this course
            modules = Module.query.filter_by(course_id=course.id).all()
            module_cache = {m.slug: m for m in modules}

            lesson_cache = {}
            for m in modules:
                for l in m.lessons:
                    lesson_cache[l.slug] = l

            files = sorted([f for f in cdir.rglob("*.md") if not f.name.startswith(".")])

            for file in files:
                if any(x in file.name.lower() for x in ["curriculum", "placeholder", "template"]):
                    continue

                meta = parse_markdown_lesson(file)
                if not meta:
                    continue

                module_name = meta.get("module_title") or f"Module {meta.get('module', 1)}"
                if isinstance(module_name, (int, float)):
                    module_name = f"Module {module_name}"
                module_slug = slugify(str(module_name))

                if module_slug not in module_cache:
                    mod = Module(
                        course_id=course.id,
                        title=str(module_name),
                        slug=module_slug,
                        is_published=True,
                        sort_order=int(meta.get("module", 1)) if str(meta.get("module", 1)).isdigit() else 1
                    )
                    db.session.add(mod)
                    db.session.flush()
                    module_cache[module_slug] = mod
                else:
                    mod = module_cache[module_slug]

                lesson_title = meta.get("lesson_title") or meta.get("title") or "Lesson"
                lesson_slug = slugify(str(lesson_title))

                diff_str = str(meta.get("difficulty", "beginner")).lower()
                if "adv" in diff_str or "3" in diff_str:
                    diff_level = DifficultyLevel.ADVANCED
                elif "inter" in diff_str or "2" in diff_str:
                    diff_level = DifficultyLevel.INTERMEDIATE
                else:
                    diff_level = DifficultyLevel.BEGINNER

                duration = int(meta.get("duration_minutes", 15))

                if lesson_slug not in lesson_cache:
                    lesson = Lesson(
                        module_id=mod.id,
                        title=str(lesson_title),
                        slug=lesson_slug,
                        summary="",
                        difficulty_level=diff_level,
                        estimated_minutes=duration,
                        status=ContentStatus.PUBLISHED,
                        sort_order=int(meta.get("lesson", 1)) if str(meta.get("lesson", 1)).isdigit() else 1
                    )
                    db.session.add(lesson)
                    db.session.flush()
                    lesson_cache[lesson_slug] = lesson
                else:
                    lesson = lesson_cache[lesson_slug]
                    lesson.module_id = mod.id
                    lesson.title = str(lesson_title)
                    lesson.difficulty_level = diff_level
                    lesson.estimated_minutes = duration
                    lesson.status = ContentStatus.PUBLISHED
                    lesson.sort_order = int(meta.get("lesson", 1)) if str(meta.get("lesson", 1)).isdigit() else 1
                    LessonSection.query.filter_by(lesson_id=lesson.id).delete()

                sections = meta.get("sections", [])
                if sections:
                    paragraphs = [p.strip() for p in sections[0]["content_markdown"].split("\n\n") if p.strip()]
                    lesson.summary = paragraphs[0][:250] if paragraphs else ""

                for sec in sections:
                    sec_el = LessonSection(
                        lesson_id=lesson.id,
                        section_type=sec["section_type"],
                        title=sec["title"],
                        content_markdown=sec["content_markdown"],
                        content_html="",
                        sort_order=sec["sort_order"],
                        is_visible=True
                    )
                    db.session.add(sec_el)

                total_ingested += 1

            # Remove placeholder modules left empty after their lessons were
            # reassigned to the correctly-split module above.
            for m in module_cache.values():
                if m.lessons.count() == 0:
                    db.session.delete(m)

            db.session.commit()
            print(f"  [DB COMMIT] Saved '{raw_course_title}' ({len(files)} files)")

        print(f"\n============================================================")
        print(f"MASTER MIGRATION COMPLETE — Total lessons ingested: {total_ingested}")
        print(f"============================================================")


if __name__ == "__main__":
    run_markdown_migration()
