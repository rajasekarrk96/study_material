#!/usr/bin/env python3
"""
Bytes and Boards Solutions — Syllabus Doc Generator (database-sourced).
Companion to generate_syllabus_docs.py: that script reads docs/curriculum/
source files, which only cover 31 of the 76 live courses. This script pulls
the remaining courses straight from the database (Course -> Module -> Lesson
-> LessonSection), so every live course gets a syllabus doc under
docs/syllabus/. Read-only against the DB; writes only under docs/syllabus/.
"""
import os
import re
import sys
from pathlib import Path

import pymysql
from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).parent.parent))
from app.core.module_grouping import group_modules

load_dotenv()

OUT_DIR = Path("docs/syllabus")


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
    text = re.sub(r"\[id:\s*[\w_]+\]", "", text or "")
    text = re.sub(r"^\d+(\.\d+)*\.?\s*", "", text.strip())
    return text.strip()


def extract_subtopics(content_markdown: str) -> list[str]:
    if not content_markdown:
        return []
    return [clean_heading(m) for m in re.findall(r"^###\s+(.+)$", content_markdown, re.MULTILINE)]


def connect():
    return pymysql.connect(
        host=os.environ["TIDB_HOST"],
        port=int(os.environ.get("TIDB_PORT", 4000)),
        user=os.environ["TIDB_USER"],
        password=os.environ["TIDB_PASSWORD"],
        database=os.environ["TIDB_DATABASE"],
        ssl_ca=os.environ.get("TIDB_CA_PATH") or None,
        connect_timeout=30,
    )


def build_course_syllabus(cur, course_id: int, course_title: str) -> str:
    cur.execute("SELECT id, title, sort_order FROM modules WHERE course_id=%s ORDER BY sort_order", (course_id,))
    modules = cur.fetchall()

    # Some courses have pre-existing duplicate lesson rows (same title,
    # re-ingested more than once historically, sometimes under a different
    # module than the original) — dedupe by title across the whole course,
    # not just within one module.
    seen_titles = set()
    raw_groups = []  # (mod_sort, mod_title, [lesson_dict, ...]) — one entry per raw module row

    for mod_id, mod_title, mod_sort in modules:
        cur.execute("SELECT id, title, sort_order FROM lessons WHERE module_id=%s ORDER BY sort_order", (mod_id,))
        lessons = []
        for lesson_id, lesson_title, _ in cur.fetchall():
            if lesson_title in seen_titles:
                continue
            seen_titles.add(lesson_title)
            cur.execute(
                "SELECT title, content_markdown FROM lesson_sections WHERE lesson_id=%s ORDER BY sort_order",
                (lesson_id,),
            )
            lessons.append({"title": lesson_title, "sections": cur.fetchall()})
        if lessons:
            raw_groups.append((mod_sort, mod_title, lessons))

    # Many DB-sourced courses have multiple module rows sharing the same
    # sort_order from historical re-ingestion — merge true duplicates,
    # renumber genuinely distinct modules that were mis-numbered identically.
    grouped = group_modules(raw_groups)

    lines = [f"# {course_title} — Syllabus", ""]
    for display_num, display_title, lessons in grouped:
        lines.append(f"## Module {display_num} — {display_title}")
        lines.append("")
        for i, lesson in enumerate(lessons, 1):
            lines.append(f"{roman_lower(i)}. **{lesson['title']}**")
            for j, (sec_title, sec_content) in enumerate(lesson["sections"], 1):
                lines.append(f"   {letter(j)}. {clean_heading(sec_title) or sec_title}")
                for sub in extract_subtopics(sec_content):
                    lines.append(f"      - {sub}")
        lines.append("")
    return "\n".join(lines)


def main():
    OUT_DIR.mkdir(exist_ok=True)
    force = "--force" in sys.argv

    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, slug, title FROM courses ORDER BY slug")
    courses = cur.fetchall()

    written, skipped = [], []
    for course_id, slug, title in courses:
        out_path = OUT_DIR / f"{slug}.md"
        if out_path.exists() and not force:
            skipped.append(slug)
            continue
        try:
            content = build_course_syllabus(cur, course_id, title)
        except pymysql.err.OperationalError:
            # TiDB Cloud connection can drop on long-running sessions; reconnect once and retry.
            conn = connect()
            cur = conn.cursor()
            content = build_course_syllabus(cur, course_id, title)
        out_path.write_text(content, encoding="utf-8")
        written.append(out_path)
        print(f"  [WRITE] {out_path} ({len(content)} chars)")

    conn.close()
    print(f"\nDone. Wrote {len(written)} files, skipped {len(skipped)} already covered by curriculum docs.")


if __name__ == "__main__":
    main()
