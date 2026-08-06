"""
Fixed placeholder generator — creates curriculum placeholder files for
all empty optional DS course folders.

Run from project root: python scripts/ds_create_placeholders_v2.py
"""
import sys
import re
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE      = Path(r"d:\My Drive\all files\PROJECT FILES\notes\exports\data-science-learning-path")
SYL_DIR   = BASE / "SYLLABUS"
CURR_DIR  = BASE / "CURRICULUM"

# Matches any ###/#### heading with a number prefix like "1.1." or "1."
MODULE_RE = re.compile(r"^#{3,4}\s+[\d]+[.\d]*\s*")
LESSON_RE = re.compile(r"^(\d+)\.\s+\*\*(.+?)\*\*")

TARGETS = [
    ("tableau",              "Tableau"),
    ("excel-data-analysis",  "Excel for Data Analysis"),
    ("cloud-ai-services",    "Cloud AI Services"),
    ("big-data-fundamentals","Big Data Fundamentals"),
    ("apache-spark",         "Apache Spark"),
    ("apache-airflow",       "Apache Airflow"),
    ("mlflow",               "MLflow"),
    ("kubeflow",             "Kubeflow"),
    ("data-warehousing",     "Data Warehousing"),
    ("snowflake",            "Snowflake"),
    ("feature-engineering",  "Feature Engineering"),
    ("data-visualization",   "Data Visualization"),
]


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9\s]", "", text.lower())
    return re.sub(r"\s+", "_", s.strip())[:55]


def create_placeholders(slug: str, title: str) -> int:
    syl_path  = SYL_DIR  / f"{slug}.md"
    curr_path = CURR_DIR / slug
    curr_path.mkdir(parents=True, exist_ok=True)

    # Skip if already has files
    if list(curr_path.glob("*.md")):
        return -1

    content = syl_path.read_text(encoding="utf-8", errors="replace")
    lines   = content.splitlines()

    module_num    = 0
    lesson_count  = {}
    created       = 0

    for line in lines:
        stripped = line.strip()

        # Any numbered heading (###/####) bumps module counter
        if MODULE_RE.match(stripped):
            module_num += 1
            lesson_count[module_num] = 0
            continue

        # Numbered bold lesson
        m = LESSON_RE.match(stripped)
        if m and module_num > 0:
            lesson_count[module_num] = lesson_count.get(module_num, 0) + 1
            n = lesson_count[module_num]
            lesson_title = m.group(2).strip()
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
    print("  DS Export — Placeholder Curriculum Generator v2")
    print("="*64 + "\n")

    total = 0
    for slug, title in TARGETS:
        n = create_placeholders(slug, title)
        if n == -1:
            print(f"  [SKIP] {slug}/  (already has files)")
        else:
            total += n
            print(f"  [+] {slug}/  {n} placeholders")

    print(f"\n  Done — {total} total placeholders created.\n")


if __name__ == "__main__":
    main()
