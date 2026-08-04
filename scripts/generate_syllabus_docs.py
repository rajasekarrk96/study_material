#!/usr/bin/env python3
"""
Bytes and Boards Solutions — Syllabus Doc Generator.
Walks docs/curriculum/_XX_<course>/ and writes a Module -> Lesson -> Topic ->
Sub-topic outline to docs/syllabus/<course-slug>.md for every course found.
Read-only against curriculum sources; writes only under docs/syllabus/.
"""
import re
import sys
from pathlib import Path
from collections import defaultdict

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent))
from app.core.module_grouping import group_modules

CURRICULUM_DIR = Path("docs/curriculum")
OUT_DIR = Path("docs/syllabus")

SKIP_NAME_MARKERS = ("curriculum", "placeholder", "template", "readme", "status", "index")


def roman_lower(n: int) -> str:
    vals = [(1000, "m"), (900, "cm"), (500, "d"), (400, "cd"), (100, "c"), (90, "xc"),
            (50, "l"), (40, "xl"), (10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")]
    out = ""
    for v, sym in vals:
        while n >= v:
            out += sym
            n -= v
    return out


def letter(n: int) -> str:
    out = ""
    while n > 0:
        n, rem = divmod(n - 1, 26)
        out = chr(97 + rem) + out
    return out


def clean_heading(text: str) -> str:
    text = re.sub(r"\[id:\s*[\w_]+\]", "", text)
    text = re.sub(r"^\d+(\.\d+)*\.?\s*", "", text.strip())
    return text.strip()


def clean_module_title(text: str) -> str:
    """Strip a leading "Module N" / "Module N - " prefix already baked into the
    title text, since the caller adds its own "Module N —" heading prefix."""
    return re.sub(r"^Module\s+\d+\s*[-:—]*\s*", "", text.strip()).strip()


def parse_lesson_file(path: Path) -> dict:
    content = path.read_text(encoding="utf-8", errors="ignore")
    frontmatter = {}
    body = content

    fm_match = re.search(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if fm_match:
        try:
            frontmatter = yaml.safe_load(fm_match.group(1)) or {}
            body = content[fm_match.end():]
        except Exception:
            frontmatter = {}

    if not frontmatter:
        cb_match = re.search(r"```yaml\n(.*?)\n```", content, re.DOTALL)
        if cb_match:
            try:
                frontmatter = yaml.safe_load(cb_match.group(1)) or {}
                body = content[cb_match.end():]
            except Exception:
                frontmatter = {}

    metadata = frontmatter.get("metadata") or {}

    module_title = frontmatter.get("module_title") or metadata.get("module_title")
    lesson_title = frontmatter.get("title") or frontmatter.get("lesson_title") or metadata.get("lesson_title")

    sort_order = metadata.get("sort_order")
    module_num = frontmatter.get("module")
    lesson_num = frontmatter.get("lesson")
    if not isinstance(module_num, int) and isinstance(sort_order, int):
        module_num = sort_order // 100
    if not isinstance(lesson_num, int) and isinstance(sort_order, int):
        lesson_num = sort_order % 100

    if not lesson_title:
        h1 = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
        lesson_title = h1.group(1).strip() if h1 else path.stem.replace("_", " ").title()
    if not module_title:
        module_title = f"Module {module_num if isinstance(module_num, int) else 1}"

    topics = []
    current = None
    for line in body.split("\n"):
        h2 = re.match(r"^##\s+(.+)$", line)
        h3 = re.match(r"^###\s+(.+)$", line)
        if h2:
            current = {"title": clean_heading(h2.group(1)), "subtopics": []}
            topics.append(current)
        elif h3 and current is not None:
            current["subtopics"].append(clean_heading(h3.group(1)))

    return {
        "has_frontmatter": bool(frontmatter),
        "module_title": str(module_title),
        "module_num": module_num if isinstance(module_num, int) else 999,
        "lesson_title": str(lesson_title),
        "lesson_num": lesson_num if isinstance(lesson_num, int) else 999,
        "topics": topics,
    }


def build_course_syllabus(course_dir: Path) -> tuple[str, str] | None:
    files = sorted([
        f for f in course_dir.rglob("*.md")
        if not any(marker in f.name.lower() for marker in SKIP_NAME_MARKERS)
    ])
    if not files:
        return None

    lessons = [parse_lesson_file(f) for f in files]
    lessons = [l for l in lessons if l["has_frontmatter"]]
    if not lessons:
        return None

    modules = defaultdict(list)
    for lesson in lessons:
        modules[(lesson["module_num"], lesson["module_title"])].append(lesson)

    course_name_raw = re.sub(r"^_\d+_", "", course_dir.name)
    course_name = course_name_raw.replace("_", " ").title()
    # Match the DB's own slugify() convention (hyphens), not the folder's
    # underscore naming, so this doesn't collide with DB-sourced syllabus
    # files for the same course.
    course_slug = re.sub(r"[\s_-]+", "-", course_name_raw.lower().strip())

    # Curriculum folders sometimes carry leftover files from an abandoned
    # re-draft (e.g. a "Java 21 LTS" rewrite attempt living alongside the
    # real Java course), which collide on module_num with different titles.
    # Merge true duplicates, renumber genuinely distinct modules that were
    # mis-numbered identically.
    raw_groups = [
        (mod_num, clean_module_title(mod_title), sorted(mod_lessons, key=lambda l: l["lesson_num"]))
        for (mod_num, mod_title), mod_lessons in sorted(modules.items(), key=lambda kv: kv[0][0])
    ]
    grouped = group_modules(raw_groups)

    lines = [f"# {course_name} — Syllabus", ""]
    for display_num, display_title, mod_lessons in grouped:
        lines.append(f"## Module {display_num} — {display_title}")
        lines.append("")
        for i, lesson in enumerate(mod_lessons, 1):
            lines.append(f"{roman_lower(i)}. **{lesson['lesson_title']}**")
            for j, topic in enumerate(lesson["topics"], 1):
                lines.append(f"   {letter(j)}. {topic['title']}")
                for sub in topic["subtopics"]:
                    lines.append(f"      - {sub}")
        lines.append("")

    return course_slug, "\n".join(lines)


def main():
    OUT_DIR.mkdir(exist_ok=True)
    target_arg = sys.argv[1].lower() if len(sys.argv) > 1 else None

    course_dirs = sorted([d for d in CURRICULUM_DIR.glob("_*") if d.is_dir()])
    if target_arg:
        course_dirs = [d for d in course_dirs if target_arg in d.name.lower()]

    written = []
    for course_dir in course_dirs:
        result = build_course_syllabus(course_dir)
        if result is None:
            print(f"  [SKIP] {course_dir.name} (no .md lesson files)")
            continue
        slug, content = result
        out_path = OUT_DIR / f"{slug}.md"
        out_path.write_text(content, encoding="utf-8")
        written.append(out_path)
        print(f"  [WRITE] {out_path} ({len(content)} chars)")

    print(f"\nDone. Wrote {len(written)} syllabus files to {OUT_DIR}/")


if __name__ == "__main__":
    main()
