"""
Create placeholder lesson markdown files for all empty curriculum folders
in the DS Learning Path export, based on their SYLLABUS files.

Run from project root: python scripts/ds_create_placeholders.py
"""
import sys
import re
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE      = Path(r"d:\My Drive\all files\PROJECT FILES\notes\exports\data-science-learning-path")
SYL_DIR   = BASE / "SYLLABUS"
CURR_DIR  = BASE / "CURRICULUM"

LESSON_RE = re.compile(r"^(\d+)\.\s+\*\*(.+?)\*\*")
MODULE_RE = re.compile(r"^#{3,4}\s+[\d.]+\s*[—-]?\s*(.+)")

# Only process courses with ZERO real files (stubs are fine, but 0 curriculum files = needs placeholders)
# data-science, tableau, excel-data-analysis, cloud-ai-services, big-data-fundamentals,
# apache-spark, apache-airflow, mlflow, kubeflow, data-warehousing, snowflake,
# feature-engineering, data-visualization

TARGETS = [
    ("data-science",        "Data Science"),
    ("tableau",             "Tableau"),
    ("excel-data-analysis", "Excel for Data Analysis"),
    ("cloud-ai-services",   "Cloud AI Services"),
    ("big-data-fundamentals","Big Data Fundamentals"),
    ("apache-spark",        "Apache Spark"),
    ("apache-airflow",      "Apache Airflow"),
    ("mlflow",              "MLflow"),
    ("kubeflow",            "Kubeflow"),
    ("data-warehousing",    "Data Warehousing"),
    ("snowflake",           "Snowflake"),
    ("feature-engineering", "Feature Engineering"),
    ("data-visualization",  "Data Visualization"),
]


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9\s]", "", text.lower())
    return re.sub(r"\s+", "_", s.strip())[:55]


def create_placeholders(slug: str, title: str, syl_path: Path, curr_path: Path) -> int:
    curr_path.mkdir(parents=True, exist_ok=True)
    content = syl_path.read_text(encoding="utf-8", errors="replace")
    lines   = content.splitlines()

    module_num   = 0
    lesson_count = {}
    created      = 0

    for line in lines:
        stripped = line.strip()

        # Detect module heading (### or ####)
        m = MODULE_RE.match(stripped)
        if m and "Module" in stripped:
            module_num += 1
            lesson_count[module_num] = 0
            continue

        # Detect numbered lesson
        l = LESSON_RE.match(stripped)
        if l and module_num > 0:
            lesson_count[module_num] = lesson_count.get(module_num, 0) + 1
            n = lesson_count[module_num]
            lesson_title = l.group(2).strip()
            fname = f"_{module_num:02d}_{n:02d}_{slugify(lesson_title)}.md"
            fpath = curr_path / fname
            if not fpath.exists():
                fpath.write_text(
                    f"# {lesson_title}\n\n"
                    f"> **Course:** {title} | **Module:** Module {module_num} | "
                    f"**Difficulty:** intermediate\n\n"
                    f"<!-- Placeholder — Write notes following NOTE_TEMPLATE.md -->\n",
                    encoding="utf-8"
                )
                created += 1

    return created


def main():
    print("\n" + "="*64)
    print("  DS Export — Placeholder Curriculum Generator")
    print("="*64 + "\n")

    total = 0
    for slug, title in TARGETS:
        syl_path  = SYL_DIR  / f"{slug}.md"
        curr_path = CURR_DIR / slug

        # Skip if curriculum already has files
        existing = list(curr_path.glob("*.md")) if curr_path.exists() else []
        if existing:
            print(f"  [SKIP] {slug}/  (already has {len(existing)} files)")
            continue

        if not syl_path.exists():
            print(f"  [MISS] {slug}/  (no syllabus found at SYLLABUS/{slug}.md)")
            continue

        n = create_placeholders(slug, title, syl_path, curr_path)
        total += n
        print(f"  [+] {slug}/  created {n} placeholder files")

    print(f"\n  Done — {total} placeholders created across {len(TARGETS)} courses.\n")


if __name__ == "__main__":
    main()
