"""
Learning OS -- Course Exporter Utility
======================================
Queries all published and stand-alone courses in the database, and exports
each course into its own isolated Contributor Work Package under:
    content_pipeline/exports/{category}/{slug}/

Features:
  - Standardizes to 4-tier folder layout (CURRICULUM, SYLLABUS, reports)
  - Copies curriculum files from docs/curriculum/ (if present) or creates stubs
  - Extracts syllabus from docs/syllabus/ or falls back to extracting sections
    from master modular syllabi (_source_modular_courses.md, etc.)
  - Copies content pipeline standard templates (STYLE_GUIDE, NOTE_TEMPLATE, etc.)
  - Computes MISSING_NOTES.md and CURRICULUM_HEALTH.md for each package
  - Generates manifest.json with complete metadata

Usage:
    python scripts/export_all_courses.py
    python scripts/export_all_courses.py --dry-run
"""
import sys
import os
import re
import json
import shutil
import argparse

ROOT_DIR = r"d:\My Drive\all files\PROJECT FILES\notes"
sys.path.insert(0, ROOT_DIR)

from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(r"d:\My Drive\all files\PROJECT FILES\notes")
SYLLABUS_DIR = ROOT / "docs" / "syllabus"
CURRICULUM_DIR = ROOT / "docs" / "curriculum"
PIPELINE_EXPORTS = ROOT / "content_pipeline" / "exports"
TEMPLATES_DIR = ROOT / "content_pipeline" / "templates"
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")

# Classifications for folder categorization
# course_type -> content_pipeline export category
CATEGORY_MAP = {
    "foundation": "shared",
    "specialization": "specializations",
    "elective": "specializations",
}

# Template filenames in content_pipeline/templates
TEMPLATE_MAP = {
    "STYLE_GUIDE.md": "STYLE_GUIDE.md",
    "NOTE_TEMPLATE.md": "NOTE_TEMPLATE.md",
    "CHECKLIST.md": "CHECKLIST_template.md",
}


def clean_title(title):
    return re.sub(r"[^a-z0-9]", "", title.lower())


def extract_syllabus_from_sources(course_slug, course_title):
    """
    Search modular source syllabi to extract section for a course
    using keyword matching on headers.
    """
    source_files = [
        SYLLABUS_DIR / "foundations" / "programming" / "_source_modular_courses.md",
        SYLLABUS_DIR / "foundations" / "programming" / "_source_python_full_stack.md",
        SYLLABUS_DIR / "foundations" / "programming" / "_source_java_full_stack.md",
        SYLLABUS_DIR / "foundations" / "backend" / "_source_python_backend.md"
    ]
    
    slug_clean = clean_title(course_slug)
    title_clean = clean_title(course_title)
    
    for sfile in source_files:
        if not sfile.exists():
            continue
        try:
            lines = sfile.read_text(encoding="utf-8", errors="replace").splitlines()
        except Exception:
            continue
            
        start_idx = -1
        heading_level = 0
        
        for idx, line in enumerate(lines):
            if line.strip().startswith("#"):
                line_clean = clean_title(line)
                # Match if slug or title matches parts of the heading clean text
                if (slug_clean in line_clean and len(slug_clean) >= 3) or (title_clean in line_clean and len(title_clean) >= 3):
                    start_idx = idx
                    heading_level = len(line) - len(line.lstrip("#"))
                    break
                    
        if start_idx != -1:
            extracted_lines = [f"# {course_title} -- Syllabus\n", f"> Source: `{sfile.name}`\n\n"]
            for idx in range(start_idx + 1, len(lines)):
                line = lines[idx]
                if line.strip().startswith("#"):
                    current_level = len(line) - len(line.lstrip("#"))
                    if current_level <= heading_level:
                        break
                extracted_lines.append(line)
            return "\n".join(extracted_lines)
            
    return f"# {course_title} Syllabus\n\nSyllabus placeholder for {course_title}."


def get_curriculum_source_folder(course_slug):
    """
    Locates the corresponding curriculum folder under docs/curriculum/
    by looking for matching folder name.
    """
    for folder in CURRICULUM_DIR.glob("**/*"):
        if folder.is_dir() and (folder.name.endswith(course_slug) or folder.name == course_slug):
            return folder
    return None


def get_syllabus_source_file(course_slug):
    """
    Locates an individual syllabus file in docs/syllabus/
    """
    for sfile in SYLLABUS_DIR.glob("**/*.md"):
        if sfile.name == f"{course_slug}.md":
            return sfile
    return None


def run_export(dry_run=False):
    # Initialize Flask app to read DB courses
    from app import create_app
    from app.core.extensions import db
    from app.domains.content.models import Course

    app = create_app()

    with app.app_context():
        courses = Course.query.filter_by(is_deleted=False).all()
        print(f"Total courses loaded from DB: {len(courses)}")

        exported_count = 0
        
        for course in courses:
            slug = course.slug
            title = course.title
            ctype = getattr(course, "course_type", "foundation")
            category = CATEGORY_MAP.get(ctype, "specializations")

            dest_pkg_dir = PIPELINE_EXPORTS / category / slug
            
            print(f"\nExporting Course: {title} ({slug}) -> {category}/{slug}")

            if dry_run:
                print("  [DRY RUN] Would create export package directory")
                exported_count += 1
                continue

            # 1. Create directory structure
            dest_pkg_dir.mkdir(parents=True, exist_ok=True)
            curr_dir = dest_pkg_dir / "CURRICULUM"
            syll_dir = dest_pkg_dir / "SYLLABUS"
            rep_dir = dest_pkg_dir / "reports"
            
            curr_dir.mkdir(parents=True, exist_ok=True)
            syll_dir.mkdir(parents=True, exist_ok=True)
            rep_dir.mkdir(parents=True, exist_ok=True)

            # 2. Copy curriculum files
            src_curr = get_curriculum_source_folder(slug)
            total_files = 0
            empty_stubs = 0
            
            if src_curr and src_curr.exists():
                print(f"  Curriculum source: {src_curr.relative_to(ROOT)}")
                # Copy files inside (ignoring desktop.ini)
                for item in src_curr.glob("**/*"):
                    if item.is_file() and item.name not in ("desktop.ini", "thumbs.db", ".DS_Store"):
                        # Calculate relative path
                        rel = item.relative_to(src_curr)
                        dest_file = curr_dir / rel
                        dest_file.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(item, dest_file)
                        total_files += 1
                        if item.stat().st_size < 500:
                            empty_stubs += 1
            else:
                print("  No curriculum source folder found. Created empty CURRICULUM directory.")

            # 3. Export/Extract syllabus
            src_syll = get_syllabus_source_file(slug)
            syllabus_content = ""
            if src_syll and src_syll.exists():
                print(f"  Syllabus source file: {src_syll.relative_to(ROOT)}")
                syllabus_content = src_syll.read_text(encoding="utf-8", errors="replace")
            else:
                print("  Syllabus file not found. Extracting from modular sources...")
                syllabus_content = extract_syllabus_from_sources(slug, title)

            (syll_dir / f"{slug}.md").write_text(syllabus_content, encoding="utf-8")

            # 4. Copy templates
            for f_name, t_name in TEMPLATE_MAP.items():
                t_path = TEMPLATES_DIR / t_name
                if t_path.exists():
                    shutil.copy2(t_path, dest_pkg_dir / f_name)

            # 5. Create default REPORT.md and CONTRIBUTOR_GUIDE.md
            report_md = f"# Contributor Report: {title}\n\nAssigned to: contributor_name\n\nStubs completed: {total_files - empty_stubs} / {total_files}\n"
            (dest_pkg_dir / "REPORT.md").write_text(report_md, encoding="utf-8")

            guide_md = f"# Contributor Guide -- {title}\n\n1. Write stubs in CURRICULUM/\n2. Verify files using templates\n"
            (dest_pkg_dir / "CONTRIBUTOR_GUIDE.md").write_text(guide_md, encoding="utf-8")

            readme_md = f"# Work Package: {title}\n\nIsolated workspace for {title} course notes writing.\n"
            (dest_pkg_dir / "README.md").write_text(readme_md, encoding="utf-8")

            # 6. Generate reports/MISSING_NOTES.md & CURRICULUM_HEALTH.md
            missing_notes_list = []
            if src_curr and src_curr.exists():
                for item in src_curr.glob("**/*.md"):
                    if item.stat().st_size < 500:
                        missing_notes_list.append(item.stem)

            missing_md = f"# Missing Notes in {title}\n\nThe following lessons need content:\n\n"
            for m in missing_notes_list:
                missing_md += f"- [ ] {m}\n"
            (rep_dir / "MISSING_NOTES.md").write_text(missing_md, encoding="utf-8")

            health_md = f"# Curriculum Health Report: {title}\n\n- **Total Lessons:** {total_files}\n- **Empty Stubs:** {empty_stubs}\n"
            (rep_dir / "CURRICULUM_HEALTH.md").write_text(health_md, encoding="utf-8")

            # 7. Generate manifest.json
            manifest = {
                "package_id": f"{slug}-package-001",
                "package_type": category,
                "course_name": title,
                "version": "1.0",
                "source_syllabus": str(src_syll.relative_to(ROOT)) if src_syll else "modular_sources",
                "source_curriculum": str(src_curr.relative_to(ROOT)) if src_curr else "none",
                "export_date": TODAY,
                "status": "exported",
                "assigned_to": "contributor_name",
                "notes_version": 1,
                "review_status": "pending",
                "merge_status": "not_merged"
            }
            with open(dest_pkg_dir / "manifest.json", "w", encoding="utf-8") as f:
                json.dump(manifest, f, indent=2)

            exported_count += 1
            print(f"  Successfully exported package.")

        print(f"\nTotal packages processed: {exported_count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", default=False)
    args = parser.parse_args()
    run_export(dry_run=args.dry_run)
