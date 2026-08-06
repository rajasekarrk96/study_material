"""
Learning OS — Frontend Development Export Package Builder
=========================================================
Creates exports/frontend-development/ with all 6 course syllabi,
curriculum copies, and package documentation.

Run from project root:
    python scripts/build_frontend_export.py

Safe: reads from docs/, writes only to exports/frontend-development/.
"""
import sys
import re
import shutil
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE        = Path(r"d:\My Drive\all files\PROJECT FILES\notes")
SYLLABUS_DIR = BASE / "docs" / "syllabus"
CURRICULUM_DIR = BASE / "docs" / "curriculum"
EXPORT_DIR  = BASE / "exports" / "frontend-development"

# ── Course map ──────────────────────────────────────────────────────────────
# Each entry: (export_slug, curriculum_folder, syllabus_source, extra)
# syllabus_source = ("modular", start_line_0idx, end_line_0idx_exclusive)
#                OR ("file", filename)
COURSES = [
    {
        "slug":       "html5",
        "title":      "HTML5 Essentials",
        "folder":     "04-html5-essentials",
        "syllabus":   ("modular", 3044, 3679),   # lines 3045–3679 (0-indexed)
    },
    {
        "slug":       "css3",
        "title":      "CSS3 Styling",
        "folder":     "05-css3-styling",
        "syllabus":   ("modular", 3679, 4235),
    },
    {
        "slug":       "bootstrap",
        "title":      "Bootstrap Framework",
        "folder":     "06-bootstrap-framework",
        "syllabus":   ("modular", 4235, 4328),
    },
    {
        "slug":       "javascript",
        "title":      "JavaScript Core",
        "folder":     "08-javascript-core",
        "syllabus":   ("modular", 4328, 5373),
    },
    {
        "slug":       "jquery",
        "title":      "jQuery Library",
        "folder":     "07-jquery-library",
        "syllabus":   ("modular", 5373, 5435),
    },
    {
        "slug":       "react",
        "title":      "React.js Frontend",
        "folder":     "20-react-frontend",
        "syllabus":   ("file", "_12_react_frontend.md"),
    },
]


def banner(msg):
    print(f"\n{'='*64}")
    print(f"  {msg}")
    print(f"{'='*64}")


def load_modular_lines():
    path = SYLLABUS_DIR / "_33_modular_courses.md"
    return path.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)


def extract_syllabus(course: dict, modular_lines: list) -> str:
    src = course["syllabus"]
    if src[0] == "modular":
        _, start, end = src
        extracted = modular_lines[start:end]
        # Replace leading "### N. CourseName" with a proper syllabus header
        header = f"# {course['title']} — Master Syllabus\n\n"
        # Skip the first line (the ### header) and add our own
        if extracted and extracted[0].startswith("### "):
            extracted = extracted[1:]
        return header + "".join(extracted)
    else:
        path = SYLLABUS_DIR / src[1]
        return path.read_text(encoding="utf-8", errors="replace")


def count_stubs(folder: Path, threshold=500) -> tuple:
    files = list(folder.glob("*.md"))
    stubs = [f for f in files if f.stat().st_size < threshold]
    return len(files), len(stubs)


def build():
    banner("Frontend Development Export Package Builder")
    print(f"  Source : {BASE}")
    print(f"  Target : {EXPORT_DIR}\n")

    # Load modular syllabus once
    modular_lines = load_modular_lines()
    print(f"  Loaded _33_modular_courses.md — {len(modular_lines)} lines")

    # ── Step 1: Create directory structure ─────────────────────────────────
    dirs_to_create = [
        EXPORT_DIR,
        EXPORT_DIR / "SYLLABUS",
        EXPORT_DIR / "reports",
    ]
    for course in COURSES:
        dirs_to_create.append(EXPORT_DIR / "CURRICULUM" / course["slug"])

    for d in dirs_to_create:
        d.mkdir(parents=True, exist_ok=True)

    print(f"\n  [OK] Directory structure created")

    # ── Step 2: Extract and write syllabi ──────────────────────────────────
    banner("Step 2 — Extracting Syllabi")
    syllabus_stats = {}
    for course in COURSES:
        content = extract_syllabus(course, modular_lines)
        dest = EXPORT_DIR / "SYLLABUS" / f"{course['slug']}.md"
        dest.write_text(content, encoding="utf-8")
        lines = content.count("\n")
        size_kb = len(content.encode()) / 1024
        syllabus_stats[course["slug"]] = {"lines": lines, "size_kb": round(size_kb, 1)}
        print(f"  [+] SYLLABUS/{course['slug']}.md  ({lines} lines, {size_kb:.1f} KB)")

    # ── Step 3: Copy curriculum ────────────────────────────────────────────
    banner("Step 3 — Copying Curriculum")
    curriculum_stats = {}
    for course in COURSES:
        src_dir = CURRICULUM_DIR / course["folder"]
        dst_dir = EXPORT_DIR / "CURRICULUM" / course["slug"]

        files = sorted(src_dir.glob("*.md"))
        copied = 0
        stubs = 0

        for f in files:
            shutil.copy2(f, dst_dir / f.name)
            copied += 1
            if f.stat().st_size < 500:
                stubs += 1

        curriculum_stats[course["slug"]] = {
            "total": copied,
            "real": copied - stubs,
            "stubs": stubs,
        }
        print(
            f"  [+] CURRICULUM/{course['slug']}/  "
            f"files={copied}  real={copied-stubs}  stubs={stubs}"
        )

    # Return stats for document generation
    return syllabus_stats, curriculum_stats


if __name__ == "__main__":
    build()
    print("\n  Builder complete — documents will be written next.\n")
