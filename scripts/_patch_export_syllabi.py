"""
Injects Course Coverage field into export SYLLABUS.md files.
Run from project root: python scripts/_patch_export_syllabi.py
"""
import sys
import re
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIELD_TEXT = "    - **Course Coverage:** 🟢 Covered in Class"
LESSON_LINE_RE = re.compile(r"^(\d+)\.\s+\*\*(.+?)\*\*")


def already_has_coverage(lines: list, lesson_idx: int) -> bool:
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
    text = filepath.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
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
                new_lines.append(FIELD_TEXT + "\n")
                stats["added"] += 1
        else:
            new_lines.append(line)
        i += 1
    if stats["added"] > 0:
        filepath.write_text("".join(new_lines), encoding="utf-8")
    return stats


base = Path(r"d:\My Drive\all files\PROJECT FILES\notes\exports")
targets = [
    base / "python" / "SYLLABUS.md",
    base / "backend-concepts-work-package" / "SYLLABUS.md",
]

print("\n" + "=" * 60)
print("  Export SYLLABUS — Course Coverage Injector")
print("=" * 60 + "\n")

for fp in targets:
    if not fp.exists():
        print(f"  SKIP (not found): {fp}")
        continue
    stats = process_file(fp)
    tag = "[+]" if stats["added"] > 0 else "[=]"
    print(
        f"  {tag} {fp.parent.name}/{fp.name}  "
        f"lessons={stats['lessons_found']}  "
        f"added={stats['added']}  "
        f"skip={stats['already_present']}"
    )

print("\nDone.\n")
