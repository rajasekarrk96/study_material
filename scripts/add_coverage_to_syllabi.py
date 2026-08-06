"""
Learning OS — Syllabus Course Coverage Injector
================================================
Adds `**Course Coverage:** 🟢 Covered in Class` to every numbered lesson entry
in every syllabus Markdown file under docs/syllabus/.

Rules:
  - A numbered lesson is a line matching:  ^(\d+)\. \*\*.*\*\*
    e.g.  1. **Python Overview and Philosophy**
  - The field is appended as a sub-bullet IMMEDIATELY after the lesson line
    (before any existing sub-bullets).
  - The script is IDEMPOTENT: if the field already exists under a lesson,
    it is NOT added again.
  - Topics (sub-bullets) within a lesson are NOT individually tagged —
    the field is added at the lesson level.

Usage:
    python scripts/add_coverage_to_syllabi.py           # live run
    python scripts/add_coverage_to_syllabi.py --dry-run # preview only
    python scripts/add_coverage_to_syllabi.py --file _01_computer_fundamentals.md

Output:
    Per-file summary: lessons found, fields added, fields already present.
"""

import os
import re
import sys
import glob
from pathlib import Path

# Force UTF-8 stdout so emoji in file content doesn't crash on Windows console
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ── Configuration ──────────────────────────────────────────────────────────────
BASE_DIR     = Path(__file__).resolve().parent.parent
SYLLABUS_DIR = BASE_DIR / "docs" / "syllabus"
FIELD_TEXT   = "    - **Course Coverage:** 🟢 Covered in Class"

DRY_RUN  = "--dry-run" in sys.argv
SPECIFIC = next((a for a in sys.argv[1:] if not a.startswith("--")), None)

# Matches a numbered lesson line, e.g.:  1. **Title Here**
# Supports both bold and non-bold titles (some syllabi use plain numbered items)
LESSON_LINE_RE = re.compile(r"^(\d+)\.\s+\*\*(.+?)\*\*")

# ── Helper ─────────────────────────────────────────────────────────────────────

def already_has_coverage(lines: list[str], lesson_idx: int) -> bool:
    """
    Checks the lines immediately following `lesson_idx` (up to the next lesson
    or blank-line cluster) to see if Course Coverage is already present.
    """
    i = lesson_idx + 1
    while i < len(lines):
        stripped = lines[i].strip()
        if not stripped:
            break
        if LESSON_LINE_RE.match(lines[i]):
            break
        if "**Course Coverage:**" in stripped:
            return True
        i += 1
    return False


def process_file(filepath: Path) -> dict:
    """
    Reads a syllabus file, injects Course Coverage after each lesson heading,
    and writes back (unless DRY_RUN). Returns stats dict.
    """
    text   = filepath.read_text(encoding="utf-8")
    lines  = text.splitlines(keepends=True)

    new_lines = []
    stats = {"lessons_found": 0, "added": 0, "already_present": 0}

    i = 0
    while i < len(lines):
        line = lines[i]
        if LESSON_LINE_RE.match(line.lstrip()):
            stats["lessons_found"] += 1
            new_lines.append(line)
            if already_has_coverage(lines, i):
                stats["already_present"] += 1
            else:
                # Inject the Course Coverage field right after the lesson heading
                new_lines.append(FIELD_TEXT + "\n")
                stats["added"] += 1
        else:
            new_lines.append(line)
        i += 1

    if stats["added"] > 0 and not DRY_RUN:
        filepath.write_text("".join(new_lines), encoding="utf-8")

    return stats


def run():
    if SPECIFIC:
        target = SYLLABUS_DIR / SPECIFIC
        if not target.exists():
            print(f"❌ File not found: {target}")
            sys.exit(1)
        files = [target]
    else:
        files = sorted(SYLLABUS_DIR.glob("_*.md"))

    print(f"\n{'='*70}")
    print("  Learning OS — Syllabus Course Coverage Injector")
    print(f"  Dry Run  : {DRY_RUN}")
    print(f"  Directory: {SYLLABUS_DIR}")
    print(f"  Files    : {len(files)}")
    print(f"{'='*70}\n")

    totals = {"lessons_found": 0, "added": 0, "already_present": 0}

    for fp in files:
        stats = process_file(fp)
        for k in totals:
            totals[k] += stats[k]

        if stats["added"] > 0:
            status = "[+]"
        elif stats["already_present"] > 0:
            status = "[=]"
        else:
            status = "[-]"
        print(
            f"  {status} {fp.name:<55} "
            f"lessons={stats['lessons_found']:>4}  "
            f"added={stats['added']:>4}  "
            f"skip={stats['already_present']:>4}"
        )

    print(f"\n{'─'*70}")
    print(f"  TOTAL  lessons_found={totals['lessons_found']}  "
          f"added={totals['added']}  "
          f"already_present={totals['already_present']}")
    print(f"{'─'*70}")

    if DRY_RUN:
        print("\n  [DRY RUN] No files were modified.")
    else:
        print(f"\n  ✅ Done. {totals['added']} lesson entries updated across {len(files)} files.")
    print()


if __name__ == "__main__":
    run()
