"""
generate_iot_fullstack_content.py
==================================
Learning OS — IoT Full Stack Course Content Generator

Generates AI lesson content for all courses in the IoT Full Stack path
that have lessons in 'draft' status with empty sections.

Processing order (required courses first):
  1. electrical-fundamentals   [REQ] DRAFT — 15 lessons
  2. electronics-basics        [REQ] DRAFT — 20 lessons
  3. raspberry-pi              [OPT] STUB  — seed structure first
  4. stm32                     [OPT] DRAFT — 25 lessons
  5. firebase                  [OPT] DRAFT — 15 lessons
  6. tinyml                    [OPT] DRAFT — 15 lessons

For each lesson, generates 6 sections:
  overview | concept | syntax | example | pitfall | qa

Already FULL (skipped):
  c-programming(partial), embedded-c, core-python, git,
  arduino, esp32, sensors-actuators, iot-hardware, html5, css3,
  bootstrap, javascript, mysql, flask, mqtt, computer-vision

Usage:
  python scripts/generate_iot_fullstack_content.py
  python scripts/generate_iot_fullstack_content.py --course electrical-fundamentals
  python scripts/generate_iot_fullstack_content.py --dry-run
  python scripts/generate_iot_fullstack_content.py --model qwen3-coder:30b
"""
import sys, re, time, argparse
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

from app import create_app
from app.core.extensions import db
from app.domains.content.models import Course, Module, Lesson, LessonSection
from app.providers.registry import get_provider
from app.providers.prompts import get_prompt

app = create_app()

# ─── Courses to generate content for ─────────────────────────────────────────
IOT_CONTENT_QUEUE = [
    {"slug": "electrical-fundamentals", "domain": "Electrical Engineering", "difficulty": "Beginner"},
    {"slug": "electronics-basics",      "domain": "Electronics",            "difficulty": "Beginner"},
    {"slug": "stm32",                   "domain": "Embedded Systems",       "difficulty": "Advanced"},
    {"slug": "firebase",                "domain": "Cloud / IoT Backend",    "difficulty": "Beginner"},
    {"slug": "tinyml",                  "domain": "AI / Embedded",          "difficulty": "Advanced"},
    # Raspberry Pi — has 0 lessons, handled by raspberry pi seeder
]

# ─── Section types to generate ───────────────────────────────────────────────
SECTION_TYPES = [
    ("overview",  "Overview",            1),
    ("concept",   "Core Concept",        2),
    ("syntax",    "Syntax & API",        3),
    ("example",   "Practical Example",   4),
    ("pitfall",   "Common Pitfalls",     5),
    ("qa",        "Q & A",               6),
]


def generate_section(provider, course_title, module_title, lesson_title,
                     domain, difficulty, section_type) -> str:
    """Call AI to generate one section. Returns content string."""
    prompt = get_prompt(
        "generate_lesson_section",
        section_type=section_type,
        course_title=course_title,
        module_title=module_title,
        lesson_title=lesson_title,
        domain=domain,
        difficulty=difficulty,
    )
    return provider.chat(prompt).strip()


def process_course(course_info: dict, provider, dry_run: bool = False) -> dict:
    """Generate AI content for all draft lessons in a course."""
    slug = course_info["slug"]
    course = Course.query.filter_by(slug=slug, is_deleted=False).first()
    if not course:
        print(f"  [ERROR] Course not found: {slug}")
        return {}

    mods = course.modules.all()
    if not mods:
        print(f"  [SKIP] {slug} — no modules (STUB). Run raspberry_pi seeder first.")
        return {}

    # Collect all lessons needing content
    queue = []
    for mod in mods:
        for lesson in mod.lessons.filter_by(is_deleted=False).all():
            filled = LessonSection.query.filter_by(
                lesson_id=lesson.id
            ).filter(LessonSection.content_markdown != "").count()
            if filled < len(SECTION_TYPES):
                queue.append({
                    "lesson": lesson,
                    "module": mod,
                    "course": course,
                })

    if not queue:
        print(f"  [DONE] {slug} — all lessons already have content.")
        return {"skipped": True}

    print(f"  {len(queue)} lessons need content generation")

    if dry_run:
        for item in queue[:3]:
            print(f"    [DRY] Would generate: {item['lesson'].title}")
        if len(queue) > 3:
            print(f"    ... and {len(queue)-3} more")
        return {"dry_run": True, "count": len(queue)}

    stats = {"lessons": 0, "sections": 0, "errors": 0}
    start = time.time()

    for idx, item in enumerate(queue, start=1):
        lesson = item["lesson"]
        mod = item["module"]
        elapsed = time.time() - start
        avg = elapsed / idx if idx > 1 else 30
        eta = int((len(queue) - idx) * avg / 60)
        print(f"    [{idx:3d}/{len(queue)}] {lesson.title[:55]} (ETA ~{eta}min)")

        sections_created = 0
        for (stype, stitle, sort_order) in SECTION_TYPES:
            # Check if section already has content
            existing = LessonSection.query.filter_by(
                lesson_id=lesson.id,
                section_type=stype
            ).first()

            if existing and existing.content_markdown:
                continue  # Already generated

            try:
                t0 = time.time()
                content = generate_section(
                    provider,
                    course_title=course.title,
                    module_title=mod.title,
                    lesson_title=lesson.title,
                    domain=course_info["domain"],
                    difficulty=course_info["difficulty"],
                    section_type=stype,
                )
                elapsed_s = time.time() - t0

                if existing:
                    existing.content_markdown = content
                    existing.is_visible = True
                else:
                    db.session.add(LessonSection(
                        lesson_id=lesson.id,
                        section_type=stype,
                        title=stitle,
                        content_markdown=content,
                        content_html="",
                        sort_order=sort_order,
                        is_visible=True,
                    ))

                sections_created += 1
                print(f"         [{stype:8s}] {len(content):4d} chars in {elapsed_s:.1f}s")

            except Exception as e:
                print(f"         [{stype:8s}] ERROR: {str(e)[:60]}")
                stats["errors"] += 1

        # Mark lesson as published after content generated
        if sections_created >= 4:  # At least 4 of 6 sections succeeded
            lesson.status = 'published'
            stats["lessons"] += 1
            stats["sections"] += sections_created

        db.session.commit()

    total_min = int((time.time() - start) / 60)
    print(f"\n  Done: {stats['lessons']} lessons | {stats['sections']} sections | "
          f"{stats['errors']} errors | {total_min} min")
    return stats


def run(course_filter=None, dry_run=False, model="qwen3:14b"):
    queue = (
        [c for c in IOT_CONTENT_QUEUE if c["slug"] == course_filter]
        if course_filter else IOT_CONTENT_QUEUE
    )
    if not queue:
        print(f"Course not found in IoT queue: {course_filter}")
        return

    with app.app_context():
        provider = get_provider(model=model)
        # Quick connectivity test
        try:
            test = provider.chat("Reply with: OK")
            if "Unavailable" in test or "offline" in test.lower():
                raise ConnectionError("Ollama not responding")
            print(f"Ollama OK — model: {model}")
        except Exception as e:
            print(f"[ERROR] Ollama not available: {e}")
            print("  Make sure Ollama is running and the model is loaded.")
            return

        print(f"\n{'='*65}")
        print(f"IoT Full Stack Content Generator")
        print(f"Model: {model} | Courses: {len(queue)} | Dry run: {dry_run}")
        print(f"{'='*65}")

        total_lessons = 0
        total_sections = 0

        for course_info in queue:
            slug = course_info["slug"]
            print(f"\n[COURSE] {slug}")
            print(f"  Domain: {course_info['domain']} | Level: {course_info['difficulty']}")

            result = process_course(course_info, provider, dry_run=dry_run)
            total_lessons += result.get("lessons", 0)
            total_sections += result.get("sections", 0)

        print(f"\n{'='*65}")
        print(f"COMPLETE: {total_lessons} lessons published | {total_sections} sections generated")
        print(f"{'='*65}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IoT Full Stack Content Generator")
    parser.add_argument("--course", help="Generate only this course slug")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    parser.add_argument("--model", default="qwen3:14b",
                        choices=["qwen3:14b", "qwen3-coder:30b"],
                        help="Ollama model to use")
    args = parser.parse_args()
    run(course_filter=args.course, dry_run=args.dry_run, model=args.model)
