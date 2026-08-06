"""
Learning OS — Data Science Learning Path Export Package Builder
===============================================================
Creates exports/data-science-learning-path/ with:
- 7 core DS syllabi (extracted from existing sources)
- 15 optional course syllabi (extracted where found, generated where missing)
- Curriculum files (copied if real, created as stubs if missing)
- All package documentation

Run from project root:
    python scripts/build_ds_export.py

Safe: reads from docs/, writes ONLY to exports/data-science-learning-path/.
Never touches existing files.
"""
import sys
import re
import shutil
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE          = Path(r"d:\My Drive\all files\PROJECT FILES\notes")
SYLLABUS_DIR  = BASE / "docs" / "syllabus"
CURRICULUM_DIR = BASE / "docs" / "curriculum"
EXPORT_DIR    = BASE / "exports" / "data-science-learning-path"

# ── Reusable shared courses — referenced only, never copied ──────────────────
REFERENCED_COURSES = [
    {
        "title":   "Computer Fundamentals",
        "folder":  None,
        "syllabus": "_01_computer_fundamentals.md",
        "reason":  "Foundational shared course — prerequisite for all paths",
    },
    {
        "title":   "Engineering Mathematics",
        "folder":  None,
        "syllabus": "_02_engineering_mathematics.md",
        "reason":  "Foundational shared course — linear algebra, calculus, probability",
    },
    {
        "title":   "Core Python",
        "folder":  "09-python-core",
        "syllabus": "_06_python_full_stack.md",
        "reason":  "Reusable course — shared with Web and Backend paths",
    },
    {
        "title":   "Git Version Control",
        "folder":  "03-git-version-control",
        "syllabus": "_03_git_version_control.md",
        "reason":  "Reusable course — shared across all engineering paths",
    },
    {
        "title":   "Database Technologies (MySQL)",
        "folder":  "13-mysql-database",
        "syllabus": "_15_database_technologies.md",
        "reason":  "Reusable course — shared with Backend and Data paths",
    },
    {
        "title":   "Statistics & DS Mathematics",
        "folder":  "38-ds-math-statistics",
        "syllabus": None,
        "reason":  "Reusable shared math course — included separately in DS path",
    },
    {
        "title":   "MongoDB for Data Science",
        "folder":  "15-mongodb-nosql",
        "syllabus": None,
        "reason":  "Reusable NoSQL course — optional, referenced from DS path",
    },
]

# ── Core DS courses — copied from curriculum, syllabus extracted ──────────────
CORE_COURSES = [
    {
        "slug":    "data-analytics",
        "title":   "Data Analytics",
        "folder":  "39-python-data-science",   # closest match
        "syllabus": ("file", "_27_data_analytics.md"),
        "notes":   "10 files — all complete",
    },
    {
        "slug":    "data-science",
        "title":   "Data Science",
        "folder":  None,                        # no dedicated folder yet
        "syllabus": ("file", "_28_data_science.md"),
        "notes":   "No dedicated curriculum folder — placeholders only",
    },
    {
        "slug":    "machine-learning",
        "title":   "Machine Learning",
        "folder":  "41-machine-learning",
        "syllabus": ("file", "_31_ai_engineering.md"),   # ML sections are within AI Engineering
        "notes":   "107 stubs",
    },
    {
        "slug":    "deep-learning",
        "title":   "Deep Learning",
        "folder":  "42-deep-learning",
        "syllabus": ("file", "_31_ai_engineering.md"),
        "notes":   "94 stubs",
    },
    {
        "slug":    "computer-vision",
        "title":   "Computer Vision",
        "folder":  "43-computer-vision",
        "syllabus": ("file", "_29_computer_vision.md"),
        "notes":   "72 stubs",
    },
    {
        "slug":    "nlp-generative-ai",
        "title":   "NLP & Generative AI",
        "folder":  "44-nlp-systems",
        "syllabus": ("file", "_30_nlp_generative_ai.md"),
        "notes":   "72 stubs",
    },
    {
        "slug":    "mlops-engineering",
        "title":   "MLOps Engineering",
        "folder":  "48-mlops-ai-deployment",
        "syllabus": ("file", "_32_mlops_engineering.md"),
        "notes":   "59 stubs",
    },
]

# ── Optional courses — syllabus from modular or generated; copy curriculum ────
# (section line numbers in _33_modular_courses.md, 0-indexed)
OPTIONAL_COURSES = [
    {
        "slug":    "power-bi",
        "title":   "Power BI",
        "folder":  "40-power-bi",
        "syllabus": ("generate", "power-bi"),
    },
    {
        "slug":    "tableau",
        "title":   "Tableau",
        "folder":  None,
        "syllabus": ("generate", "tableau"),
    },
    {
        "slug":    "excel-data-analysis",
        "title":   "Excel for Data Analysis",
        "folder":  None,
        "syllabus": ("generate", "excel"),
    },
    {
        "slug":    "cloud-ai-services",
        "title":   "Cloud AI Services",
        "folder":  None,
        "syllabus": ("generate", "cloud-ai"),
    },
    {
        "slug":    "big-data-fundamentals",
        "title":   "Big Data Fundamentals",
        "folder":  None,
        "syllabus": ("generate", "big-data"),
    },
    {
        "slug":    "apache-spark",
        "title":   "Apache Spark",
        "folder":  None,
        "syllabus": ("generate", "spark"),
    },
    {
        "slug":    "apache-airflow",
        "title":   "Apache Airflow",
        "folder":  None,
        "syllabus": ("generate", "airflow"),
    },
    {
        "slug":    "mlflow",
        "title":   "MLflow",
        "folder":  None,
        "syllabus": ("generate", "mlflow"),
    },
    {
        "slug":    "kubeflow",
        "title":   "Kubeflow",
        "folder":  None,
        "syllabus": ("generate", "kubeflow"),
    },
    {
        "slug":    "data-warehousing",
        "title":   "Data Warehousing",
        "folder":  None,
        "syllabus": ("generate", "data-warehousing"),
    },
    {
        "slug":    "snowflake",
        "title":   "Snowflake",
        "folder":  None,
        "syllabus": ("generate", "snowflake"),
    },
    {
        "slug":    "feature-engineering",
        "title":   "Feature Engineering",
        "folder":  None,
        "syllabus": ("generate", "feature-engineering"),
    },
    {
        "slug":    "data-visualization",
        "title":   "Data Visualization",
        "folder":  None,
        "syllabus": ("generate", "data-visualization"),
    },
]


def banner(msg):
    print(f"\n{'='*64}")
    print(f"  {msg}")
    print(f"{'='*64}\n")


def count_stubs(folder: Path, threshold=500):
    files = list(folder.glob("*.md"))
    stubs = [f for f in files if f.stat().st_size < threshold]
    return len(files), len(stubs)


def copy_curriculum(src_folder_name: str, dest_slug: str) -> tuple:
    """Copy curriculum from docs/curriculum/<src> to CURRICULUM/<dest>."""
    src = CURRICULUM_DIR / src_folder_name
    dst = EXPORT_DIR / "CURRICULUM" / dest_slug
    dst.mkdir(parents=True, exist_ok=True)

    if not src.exists():
        return 0, 0

    files = sorted(src.glob("*.md"))
    stubs = 0
    for f in files:
        shutil.copy2(f, dst / f.name)
        if f.stat().st_size < 500:
            stubs += 1
    return len(files), stubs


def create_placeholder(dest_slug: str, title: str, syllabus_path: Path):
    """Create placeholder stub files based on syllabus lessons."""
    dst = EXPORT_DIR / "CURRICULUM" / dest_slug
    dst.mkdir(parents=True, exist_ok=True)

    # Parse lesson titles from syllabus for placeholder names
    content = syllabus_path.read_text(encoding="utf-8", errors="replace")
    lines = content.splitlines()

    lesson_re = re.compile(r"^(\d+)\.\s+\*\*(.+?)\*\*")
    module_re = re.compile(r"^#{3,4}\s+[\d.]+\s+(.+)")

    placeholders_created = 0
    module_num = 0
    lesson_counters = {}

    for line in lines:
        m = module_re.match(line.strip())
        if m:
            module_num += 1
            lesson_counters[module_num] = 0

        l = lesson_re.match(line.strip())
        if l and module_num > 0:
            lesson_counters[module_num] = lesson_counters.get(module_num, 0) + 1
            lesson_num = lesson_counters[module_num]
            lesson_title = l.group(2).strip()
            # Convert to filename
            slug = re.sub(r"[^a-z0-9\s]", "", lesson_title.lower())
            slug = re.sub(r"\s+", "_", slug.strip())[:60]
            filename = f"_{module_num:02d}_{lesson_num:02d}_{slug}.md"
            fpath = dst / filename
            if not fpath.exists():
                fpath.write_text(
                    f"# {lesson_title}\n\n"
                    f"> **Course:** {title} | **Module:** Module {module_num} | **Difficulty:** intermediate\n\n"
                    f"<!-- Placeholder — Write notes following NOTE_TEMPLATE.md -->\n",
                    encoding="utf-8"
                )
                placeholders_created += 1

    return placeholders_created


def build():
    banner("Data Science Learning Path Export Builder")
    print(f"  Target: {EXPORT_DIR}\n")

    # ── Create directory structure ──────────────────────────────────────────
    for course in CORE_COURSES + OPTIONAL_COURSES:
        (EXPORT_DIR / "CURRICULUM" / course["slug"]).mkdir(parents=True, exist_ok=True)
    (EXPORT_DIR / "SYLLABUS").mkdir(parents=True, exist_ok=True)
    (EXPORT_DIR / "REPORTS").mkdir(parents=True, exist_ok=True)
    print("  [OK] Directory structure created")

    # ── Step 2: Copy core course syllabi ───────────────────────────────────
    banner("Step 2 — Core Course Syllabi")
    for course in CORE_COURSES:
        src_type, src_name = course["syllabus"]
        dest = EXPORT_DIR / "SYLLABUS" / f"{course['slug']}.md"
        if src_type == "file":
            src_path = SYLLABUS_DIR / src_name
            shutil.copy2(src_path, dest)
            size_kb = dest.stat().st_size / 1024
            print(f"  [COPY] {course['slug']}.md  ({size_kb:.1f} KB) from {src_name}")

    # ── Step 3: Copy core curricula ────────────────────────────────────────
    banner("Step 3 — Core Curriculum")
    for course in CORE_COURSES:
        folder = course.get("folder")
        if folder:
            total, stubs = copy_curriculum(folder, course["slug"])
            print(f"  [COPY] CURRICULUM/{course['slug']}/  files={total}  stubs={stubs}")
        else:
            print(f"  [SKIP] CURRICULUM/{course['slug']}/  No source folder — will create placeholders separately")

    # ── Step 4: Optional course syllabi (copied or to be generated) ────────
    banner("Step 4 — Optional Courses")
    for course in OPTIONAL_COURSES:
        folder = course.get("folder")
        dest_syl = EXPORT_DIR / "SYLLABUS" / f"{course['slug']}.md"
        if folder:
            total, stubs = copy_curriculum(folder, course["slug"])
            print(f"  [COPY] CURRICULUM/{course['slug']}/  files={total}  stubs={stubs}")
        else:
            print(f"  [PEND] CURRICULUM/{course['slug']}/  No source — placeholder syllabus needed")
        if not dest_syl.exists():
            dest_syl.write_text(f"# {course['title']} — Syllabus\n\n<!-- GENERATED SYLLABUS PLACEHOLDER — To be expanded -->\n", encoding="utf-8")

    print("\n  Builder phase 1 complete.\n")
    return CORE_COURSES, OPTIONAL_COURSES


if __name__ == "__main__":
    build()
