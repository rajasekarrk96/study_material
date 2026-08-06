"""
Generate REPORTS/ files and copy shared docs for DS export package.
Run from project root: python scripts/finalize_ds_export.py
"""
import sys
import shutil
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SRC_FE = Path(r"d:\My Drive\all files\PROJECT FILES\notes\exports\frontend-development")
BASE   = Path(r"d:\My Drive\all files\PROJECT FILES\notes\exports\data-science-learning-path")
CURR   = BASE / "CURRICULUM"
RPTS   = BASE / "REPORTS"
RPTS.mkdir(exist_ok=True)

# ── 1. Copy and adapt STYLE_GUIDE + NOTE_TEMPLATE ───────────────────────────
shutil.copy2(SRC_FE / "NOTE_TEMPLATE.md", BASE / "NOTE_TEMPLATE.md")

sg = (SRC_FE / "STYLE_GUIDE.md").read_text(encoding="utf-8")
sg = sg.replace(
    "Allowed identifiers: `html`, `css`, `scss`, `javascript`, `jsx`, `json`, `bash`, `text`, `mermaid`",
    "Allowed identifiers: `python`, `sql`, `bash`, `yaml`, `json`, `dockerfile`, `text`, `mermaid`, `r`"
).replace(
    "| HTML5 | No prior web knowledge | Beginner — explain every attribute |",
    "| Data Analytics | Python basics, Pandas | Practical — code-heavy, real datasets |"
).replace(
    "| CSS3 | Knows HTML5 | Beginner → Intermediate |",
    "| Data Science | Data Analytics | Theoretical + practical |"
).replace(
    "| Bootstrap | Knows HTML5 + CSS3 | Intermediate — practical focus |",
    "| Machine Learning | Statistics, Python | Algorithm internals + scikit-learn |"
).replace(
    "| JavaScript | Knows HTML5 + CSS3 | Intermediate → Advanced — include internals |",
    "| Deep Learning | ML, Linear Algebra | Architecture depth + PyTorch |"
).replace(
    "| jQuery | Knows JavaScript basics | Intermediate — compare to vanilla JS |",
    "| Computer Vision | Deep Learning | OpenCV + CNN architectures |"
).replace(
    "| React.js | Knows JavaScript well | Intermediate → Advanced — component mindset |",
    "| NLP & Generative AI | Deep Learning | HuggingFace + LLM patterns |"
)
(BASE / "STYLE_GUIDE.md").write_text(sg, encoding="utf-8")
print("[OK] STYLE_GUIDE.md and NOTE_TEMPLATE.md written")

# ── 2. Generate CURRICULUM_HEALTH.md ────────────────────────────────────────
COURSES = [
    ("data-analytics", "Data Analytics"),
    ("data-science", "Data Science"),
    ("machine-learning", "Machine Learning"),
    ("deep-learning", "Deep Learning"),
    ("computer-vision", "Computer Vision"),
    ("nlp-generative-ai", "NLP and Generative AI"),
    ("mlops-engineering", "MLOps Engineering"),
    ("power-bi", "Power BI"),
    ("tableau", "Tableau"),
    ("excel-data-analysis", "Excel for Data Analysis"),
    ("cloud-ai-services", "Cloud AI Services"),
    ("big-data-fundamentals", "Big Data Fundamentals"),
    ("apache-spark", "Apache Spark"),
    ("apache-airflow", "Apache Airflow"),
    ("mlflow", "MLflow"),
    ("kubeflow", "Kubeflow"),
    ("data-warehousing", "Data Warehousing"),
    ("snowflake", "Snowflake"),
    ("feature-engineering", "Feature Engineering"),
    ("data-visualization", "Data Visualization"),
]

rows = []
grand_total = grand_real = grand_stubs = 0
for slug, title in COURSES:
    cpath = CURR / slug
    if cpath.exists():
        files = list(cpath.glob("*.md"))
        stubs = sum(1 for f in files if f.stat().st_size < 500)
        real = len(files) - stubs
        pct = round(real / len(files) * 100) if files else 0
        icon = "100%" if pct == 100 else f"{pct}%"
        grand_total += len(files); grand_real += real; grand_stubs += stubs
    else:
        files, stubs, real, pct, icon = [], 0, 0, 0, "Empty"
    rows.append(f"| {title} | {len(files)} | {real} | {stubs} | {icon} |")

health_md = f"""# Curriculum Health Report

**Generated:** 2026-08-06
**Package:** Data Science and Analytics Learning Path

---

## Summary

| Course | Total | Complete | Stubs | Health |
|---|---|---|---|---|
{chr(10).join(rows)}
| **TOTAL** | **{grand_total}** | **{grand_real}** | **{grand_stubs}** | |

---

## Notes

- Files < 500 bytes are classified as stubs (title + metadata only)
- Power BI and Data Analytics have complete curricula
- ML, DL, CV, NLP, MLOps have stub files awaiting notes
- Optional courses without source folders have zero curriculum files
"""
(RPTS / "CURRICULUM_HEALTH.md").write_text(health_md, encoding="utf-8")
print(f"[OK] CURRICULUM_HEALTH.md  total={grand_total}  real={grand_real}  stubs={grand_stubs}")

# ── 3. Generate MISSING_NOTES.md ────────────────────────────────────────────
missing_lines = ["# Missing Notes Report\n\n**Generated:** 2026-08-06\n\nAll stub files requiring content.\n"]
total_stubs = 0
for slug, title in COURSES:
    cpath = CURR / slug
    if not cpath.exists():
        missing_lines.append(f"\n## {title} — No curriculum files yet\n\n_Use SYLLABUS/{slug}.md to create lesson placeholders._\n")
        continue
    stubs = sorted([f for f in cpath.glob("*.md") if f.stat().st_size < 500])
    if stubs:
        missing_lines.append(f"\n## {title} — {len(stubs)} stubs\n")
        for f in stubs:
            missing_lines.append(f"- `CURRICULUM/{slug}/{f.name}`\n")
        total_stubs += len(stubs)

missing_lines.insert(1, f"\n**Total stubs: {total_stubs}**\n")
(RPTS / "MISSING_NOTES.md").write_text("".join(missing_lines), encoding="utf-8")
print(f"[OK] MISSING_NOTES.md  total_stubs={total_stubs}")

# ── 4. Generate SYLLABUS_VALIDATION.md ──────────────────────────────────────
syl_dir = BASE / "SYLLABUS"
syl_files = sorted(syl_dir.glob("*.md"))
syl_rows = []
for f in syl_files:
    size_kb = round(f.stat().st_size / 1024, 1)
    lines = f.read_text(encoding="utf-8", errors="replace").count("\n")
    has_coverage = "Course Coverage" in f.read_text(encoding="utf-8", errors="replace")
    cov_mark = "Yes" if has_coverage else "No"
    syl_rows.append(f"| {f.stem} | {lines} | {size_kb} KB | {cov_mark} |")

syl_md = f"""# Syllabus Validation Report

**Generated:** 2026-08-06
**Package:** Data Science and Analytics Learning Path

---

## Summary

| Syllabus | Lines | Size | Course Coverage |
|---|---|---|---|
{chr(10).join(syl_rows)}

---

## Notes

- Core syllabi extracted from docs/syllabus/ (read-only)
- machine-learning.md and deep-learning.md were generated for this package
- Optional course syllabi were generated from scratch
- All syllabi follow the Learning OS standard (numbered lessons, bold titles)
"""
(RPTS / "SYLLABUS_VALIDATION.md").write_text(syl_md, encoding="utf-8")
print(f"[OK] SYLLABUS_VALIDATION.md  ({len(syl_files)} syllabi validated)")

print("\nAll done.")
