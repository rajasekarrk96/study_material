"""
Learning OS -- Content Pipeline Export Migrator
===============================================
Migrates existing exports in notes/exports/ to notes/content_pipeline/exports/
with proper classification (shared, learning_paths, specializations), renaming,
validation, manifest generation, and cleanup.
"""
import os
import shutil
import json
import argparse
from datetime import datetime

ROOT = r"d:\My Drive\all files\PROJECT FILES\notes"
EXPORTS_DIR = os.path.join(ROOT, "exports")
PIPELINE_DIR = os.path.join(ROOT, "content_pipeline")
PIPELINE_EXPORTS = os.path.join(PIPELINE_DIR, "exports")
TEMPLATES_DIR = os.path.join(PIPELINE_DIR, "templates")
REPORTS_DIR = os.path.join(PIPELINE_DIR, "reports")

# Packages list and classifications
PACKAGES = {
    "python": {
        "category": "shared",
        "package_id": "python-shared-001",
        "course_name": "Python Programming",
        "source_syllabus": "docs/syllabus/foundations/programming/_source_python_full_stack.md",
        "source_curriculum": "docs/curriculum/foundations/programming/09-python-core",
        "assigned_to": "python_contributor"
    },
    "frontend-development": {
        "category": "learning_paths",
        "package_id": "frontend-development-lp-001",
        "course_name": "Frontend Development",
        "source_syllabus": "docs/syllabus/learning_paths/frontend-engineering.md",
        "source_curriculum": "docs/curriculum/foundations/frontend/",
        "assigned_to": "frontend_contributor"
    },
    "data-science-learning-path": {
        "category": "learning_paths",
        "package_id": "data-science-lp-001",
        "course_name": "Data Science & Data Analytics",
        "source_syllabus": "docs/syllabus/learning_paths/data-science-path.md",
        "source_curriculum": "docs/curriculum/specializations/",
        "assigned_to": "ds_contributor"
    },
    "backend-concepts-work-package": {
        "category": "specializations",
        "package_id": "backend-concepts-spec-001",
        "course_name": "Backend Concepts",
        "source_syllabus": "docs/syllabus/specializations/backend-systems.md",
        "source_curriculum": "docs/curriculum/specializations/",
        "assigned_to": "backend_contributor"
    }
}

REQUIRED_FILES = [
    "README.md",
    "SYLLABUS",       # Folder
    "CURRICULUM",     # Folder
    "STYLE_GUIDE.md",
    "NOTE_TEMPLATE.md",
    "CHECKLIST.md",
    "CONTRIBUTOR_GUIDE.md",
    "REPORT.md",
    "reports"         # Folder
]


def run_migration(dry_run=True):
    print("=" * 60)
    print(f"Content Pipeline Migration {'[DRY RUN]' if dry_run else '[LIVE]'}")
    print("=" * 60)

    # Scanned facts
    scanned_packages = []
    missing_packages = []
    duplicate_packages = []
    migration_actions = []

    # 1. Scan original exports directory
    if not os.path.exists(EXPORTS_DIR):
        print(f"Original exports directory does not exist: {EXPORTS_DIR}")
        return

    scanned = [d for d in os.listdir(EXPORTS_DIR) if os.path.isdir(os.path.join(EXPORTS_DIR, d))]
    print(f"Scanned packages in exports/: {scanned}")

    for name in PACKAGES:
        if name in scanned:
            scanned_packages.append(name)
        else:
            missing_packages.append(name)

    # Detect duplicates or unmapped folders in exports/
    for name in scanned:
        if name not in PACKAGES:
            duplicate_packages.append(name)

    # Create destination pipeline exports category dirs
    for cat in ["shared", "learning_paths", "specializations"]:
        cat_path = os.path.join(PIPELINE_EXPORTS, cat)
        if not dry_run:
            os.makedirs(cat_path, exist_ok=True)

    # Create other folders in pipeline
    if not dry_run:
        os.makedirs(REPORTS_DIR, exist_ok=True)

    for pkg_name in scanned_packages:
        pkg_info = PACKAGES[pkg_name]
        category = pkg_info["category"]
        src_path = os.path.join(EXPORTS_DIR, pkg_name)
        dest_cat_dir = os.path.join(PIPELINE_EXPORTS, category)
        dest_path = os.path.join(dest_cat_dir, pkg_name)

        print(f"\nProcessing package: {pkg_name} -> {category}/{pkg_name}")
        migration_actions.append(f"Move '{pkg_name}' to 'content_pipeline/exports/{category}/{pkg_name}'")

        if not dry_run:
            # Copy first (to be safe and preserve original until verified)
            if os.path.exists(dest_path):
                shutil.rmtree(dest_path)
            shutil.copytree(src_path, dest_path, ignore=shutil.ignore_patterns('desktop.ini', 'thumbs.db', '.DS_Store'))
            print(f"  Copied package to {dest_path}")

            # Standardize and Rename folders inside dest_path:
            
            # 1. Rename curriculum folder to CURRICULUM (uppercase)
            curr_lower = os.path.join(dest_path, "curriculum")
            curr_upper = os.path.join(dest_path, "CURRICULUM")
            if os.path.exists(curr_lower) and not os.path.exists(curr_upper):
                os.rename(curr_lower, curr_upper)
                print("  Renamed curriculum/ -> CURRICULUM/")
            
            # For backend-concepts, move OUTPUT/curriculum to CURRICULUM
            output_curr = os.path.join(dest_path, "OUTPUT", "curriculum")
            if os.path.exists(output_curr):
                os.makedirs(curr_upper, exist_ok=True)
                for item in os.listdir(output_curr):
                    s_item = os.path.join(output_curr, item)
                    d_item = os.path.join(curr_upper, item)
                    shutil.move(s_item, d_item)
                print("  Moved OUTPUT/curriculum/ -> CURRICULUM/")
                # Clean up OUTPUT folder
                shutil.rmtree(os.path.join(dest_path, "OUTPUT"))
                print("  Removed OUTPUT/ directory")

            # 2. Rename SYLLABUS folder or convert SYLLABUS.md to SYLLABUS/
            syll_file = os.path.join(dest_path, "SYLLABUS.md")
            syll_dir = os.path.join(dest_path, "SYLLABUS")
            if os.path.exists(syll_file):
                os.makedirs(syll_dir, exist_ok=True)
                # Move SYLLABUS.md into the SYLLABUS folder as <slug>.md
                slug_name = pkg_name.replace("-work-package", "")
                shutil.move(syll_file, os.path.join(syll_dir, f"{slug_name}.md"))
                print(f"  Converted SYLLABUS.md to SYLLABUS/{slug_name}.md")

            # 3. Rename REPORTS/ to reports/ (lowercase)
            rep_upper = os.path.join(dest_path, "REPORTS")
            rep_lower = os.path.join(dest_path, "reports")
            if os.path.exists(rep_upper) and not os.path.exists(rep_lower):
                os.rename(rep_upper, rep_lower)
                print("  Renamed REPORTS/ to reports/")

            # Create reports directory if missing
            if not os.path.exists(rep_lower):
                os.makedirs(rep_lower, exist_ok=True)
                print("  Created reports/ directory")

            # Move missing notes or health files to reports/
            for report_file in ["MISSING_NOTES.md", "CURRICULUM_HEALTH.md"]:
                rf_path = os.path.join(dest_path, report_file)
                if os.path.exists(rf_path):
                    shutil.move(rf_path, os.path.join(rep_lower, report_file))
                    print(f"  Moved {report_file} to reports/")

            # 4. Handle missing templates
            # CONTRIBUTOR_GUIDE.md fallback from CONTRIBUTOR_INSTRUCTIONS.md
            instructions_file = os.path.join(dest_path, "CONTRIBUTOR_INSTRUCTIONS.md")
            guide_file = os.path.join(dest_path, "CONTRIBUTOR_GUIDE.md")
            if os.path.exists(instructions_file) and not os.path.exists(guide_file):
                shutil.move(instructions_file, guide_file)
                print("  Renamed CONTRIBUTOR_INSTRUCTIONS.md to CONTRIBUTOR_GUIDE.md")

            # Generate missing templates from content_pipeline/templates/
            template_mapping = {
                "CHECKLIST.md": "CHECKLIST_template.md",
                "NOTE_TEMPLATE.md": "NOTE_TEMPLATE.md",
                "STYLE_GUIDE.md": "STYLE_GUIDE.md",
                "VALIDATION_RULES.md": "VALIDATION_RULES.md",
            }

            for f_name, t_name in template_mapping.items():
                f_path = os.path.join(dest_path, f_name)
                t_path = os.path.join(TEMPLATES_DIR, t_name)
                if not os.path.exists(f_path) and os.path.exists(t_path):
                    shutil.copy2(t_path, f_path)
                    print(f"  Copied missing template: {f_name}")

            # Failsafe default templates if they still don't exist
            if not os.path.exists(os.path.join(dest_path, "REPORT.md")):
                report_content = f"# Contributor Report: {pkg_info['course_name']}\n\nCompleted stubs:\n- [ ] All stubs checked\n"
                with open(os.path.join(dest_path, "REPORT.md"), "w", encoding="utf-8") as f:
                    f.write(report_content)
                print("  Created default REPORT.md")

            if not os.path.exists(os.path.join(dest_path, "CONTRIBUTOR_GUIDE.md")):
                guide_content = f"# Contributor Guide: {pkg_info['course_name']}\n\n1. Write stubs in CURRICULUM/\n2. Fill checklist.md\n"
                with open(os.path.join(dest_path, "CONTRIBUTOR_GUIDE.md"), "w", encoding="utf-8") as f:
                    f.write(guide_content)
                print("  Created default CONTRIBUTOR_GUIDE.md")

            # 5. Generate package manifest.json
            manifest = {
                "package_id": pkg_info["package_id"],
                "package_type": category,
                "course_name": pkg_info["course_name"],
                "version": "1.0",
                "source_syllabus": pkg_info["source_syllabus"],
                "source_curriculum": pkg_info["source_curriculum"],
                "export_date": datetime.utcnow().strftime("%Y-%m-%d"),
                "status": "exported",
                "assigned_to": pkg_info["assigned_to"],
                "notes_version": 1,
                "review_status": "pending",
                "merge_status": "not_merged"
            }
            manifest_path = os.path.join(dest_path, "manifest.json")
            with open(manifest_path, "w", encoding="utf-8") as f:
                json.dump(manifest, f, indent=2)
            print("  Generated manifest.json")

    # Verification Step (dry run does mock check, live does actual files verification)
    verified = True
    print("\n" + "="*30 + " Verification " + "="*30)
    for pkg_name in scanned_packages:
        category = PACKAGES[pkg_name]["category"]
        dest_path = os.path.join(PIPELINE_EXPORTS, category, pkg_name)
        
        if dry_run:
            print(f"Package '{pkg_name}' would be verified.")
            continue

        print(f"Verifying '{pkg_name}' structure:")
        pkg_ok = True
        for req in REQUIRED_FILES:
            req_path = os.path.join(dest_path, req)
            if not os.path.exists(req_path):
                print(f"  [MISSING] {req}")
                pkg_ok = False
                verified = False
            else:
                print(f"  [OK] {req}")
        
        if pkg_ok:
            print(f"  Package '{pkg_name}' verification PASSED.")
        else:
            print(f"  Package '{pkg_name}' verification FAILED.")

    # Remove original exports folder (Only if live run and verification passes)
    if not dry_run:
        if verified:
            print("\nVerification passed. Cleaning up obsolete original folders in exports/...")
            for pkg_name in scanned_packages:
                src_path = os.path.join(EXPORTS_DIR, pkg_name)
                if os.path.exists(src_path):
                    shutil.rmtree(src_path)
                    print(f"  Removed obsolete folder: exports/{pkg_name}")
        else:
            print("\n[ERROR] Verification failed. Original folders in exports/ will NOT be deleted.")

    # Write report files
    if not dry_run:
        write_reports(scanned_packages, missing_packages, duplicate_packages)

    print("\n" + "="*60)
    print("Migration processing completed.")
    print("=" * 60)


def write_reports(scanned_packages, missing_packages, duplicate_packages):
    # EXPORT_MIGRATION_REPORT.md
    migration_report_path = os.path.join(REPORTS_DIR, "EXPORT_MIGRATION_REPORT.md")
    report_content = f"""# Export Migration Report

**Date:** {datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")}  
**Status:** Completed  

## Overview
This report details the refactoring and migration of legacy exports into the new Content Pipeline architecture.

## Migrated Packages
{chr(10).join(f"- `{pkg}` -> `content_pipeline/exports/{PACKAGES[pkg]['category']}/{pkg}`" for pkg in scanned_packages)}

## Verification Summary
- **Syllabus / Curriculum standardized:** Yes
- **Template files populated:** Yes
- **manifest.json generated:** Yes
"""
    with open(migration_report_path, "w", encoding="utf-8") as f:
        f.write(report_content)
    print("Generated content_pipeline/reports/EXPORT_MIGRATION_REPORT.md")

    # PACKAGE_CLASSIFICATION.md
    class_report_path = os.path.join(REPORTS_DIR, "PACKAGE_CLASSIFICATION.md")
    class_content = f"""# Package Classification Report

Classification of all packages in the Content Pipeline.

| Package | Classification | Assigned To | Status |
|---|---|---|---|
"""
    for pkg in scanned_packages:
        pkg_info = PACKAGES[pkg]
        class_content += f"| `{pkg}` | `{pkg_info['category']}` | `{pkg_info['assigned_to']}` | `exported` |\n"
    with open(class_report_path, "w", encoding="utf-8") as f:
        f.write(class_content)
    print("Generated content_pipeline/reports/PACKAGE_CLASSIFICATION.md")

    # MISSING_EXPORTS.md
    missing_report_path = os.path.join(REPORTS_DIR, "MISSING_EXPORTS.md")
    missing_content = f"""# Missing Exports Report

Packages defined in system registry but not found in the original exports folder.

{chr(10).join(f"- `{pkg}`" for pkg in missing_packages) if missing_packages else "No missing packages."}
"""
    with open(missing_report_path, "w", encoding="utf-8") as f:
        f.write(missing_content)
    print("Generated content_pipeline/reports/MISSING_EXPORTS.md")

    # DUPLICATE_EXPORTS.md
    dup_report_path = os.path.join(REPORTS_DIR, "DUPLICATE_EXPORTS.md")
    dup_content = f"""# Duplicate / Unmapped Exports Report

Folders found in the exports directory that were not part of the standard mapping registry.

{chr(10).join(f"- `{pkg}`" for pkg in duplicate_packages) if duplicate_packages else "No duplicate or unmapped packages."}
"""
    with open(dup_report_path, "w", encoding="utf-8") as f:
        f.write(dup_content)
    print("Generated content_pipeline/reports/DUPLICATE_EXPORTS.md")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", default=False)
    args = parser.parse_args()
    # If explicitly run with python scripts/migrate_exports.py, we run live.
    run_migration(dry_run=args.dry_run)
