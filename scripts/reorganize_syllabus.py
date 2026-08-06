"""
Learning OS -- Syllabus Folder Reorganizer
==========================================
Reorganizes docs/syllabus/ from flat _NN_ files into the 4-tier hierarchy:

  foundations/
    programming/
    frontend/
    backend/
    core/
  specializations/
  learning_paths/
  electives/

SAFE OPERATION:
  - Copies files, never deletes originals
  - Generates _MIGRATION_MAP.md for full traceability
  - Idempotent -- safe to run multiple times

Usage:
    python scripts/reorganize_syllabus.py --dry-run    (preview only)
    python scripts/reorganize_syllabus.py              (execute)
"""
import sys
import re
import shutil
import argparse
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(r"d:\My Drive\all files\PROJECT FILES\notes")
SYLLABUS = ROOT / "docs" / "syllabus"
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")

# -- Folder mapping -------------------------------------------------------------
# Format: (source_filename_pattern, target_subfolder, target_filename)
SYLLABUS_MAP = [
    # -- FOUNDATIONS -> Programming ------------------------------------------
    # These come from _33_modular_courses.md (large file) or full-stack files.
    # We COPY the complete modular_courses.md to each category for contributor reference.
    # Individual modules will be split later by contributors.
    ("_03_git_version_control.md",         "foundations/programming", "git-version-control.md"),
    ("_06_python_full_stack.md",           "foundations/programming", "_source_python_full_stack.md"),
    ("_09_java_full_stack.md",             "foundations/programming", "_source_java_full_stack.md"),
    ("_33_modular_courses.md",             "foundations/programming", "_source_modular_courses.md"),

    # -- FOUNDATIONS -> Frontend ---------------------------------------------
    ("_12_react_frontend.md",              "foundations/frontend",    "react.md"),

    # -- FOUNDATIONS -> Backend ----------------------------------------------
    ("_13_rest_api_development.md",        "foundations/backend",     "rest-api.md"),
    ("_07_python_backend_engineering.md",  "foundations/backend",     "_source_python_backend.md"),
    ("_08_python_selenium.md",             "foundations/backend",     "selenium.md"),

    # -- FOUNDATIONS -> Core -------------------------------------------------
    ("_01_computer_fundamentals.md",       "foundations/core",        "computer-fundamentals.md"),
    ("_02_engineering_mathematics.md",     "foundations/core",        "engineering-mathematics.md"),
    ("_04_networking_fundamentals.md",     "foundations/core",        "networking.md"),
    ("_05_linux_administration.md",        "foundations/core",        "linux.md"),
    ("_15_database_technologies.md",       "foundations/core",        "database-technologies.md"),

    # -- SPECIALIZATIONS ----------------------------------------------------
    ("_14_backend_systems_engineering.md", "specializations",         "backend-systems.md"),
    ("_16_sql_server_database.md",         "specializations",         "sql-server.md"),
    ("_17_firebase_development.md",        "specializations",         "firebase.md"),
    ("_18_devops_engineering.md",          "specializations",         "devops-engineering.md"),
    ("_19_cloud_computing.md",             "specializations",         "cloud-computing.md"),
    ("_20_software_testing.md",            "specializations",         "software-testing.md"),
    ("_21_electronics_pcb_design.md",      "specializations",         "pcb-design.md"),
    ("_22_embedded_systems.md",            "specializations",         "embedded-systems.md"),
    ("_24_advanced_iot.md",               "specializations",         "advanced-iot.md"),
    ("_25_computer_vision_for_iot.md",     "specializations",         "computer-vision-iot.md"),
    ("_27_data_analytics.md",             "specializations",         "data-analytics.md"),
    ("_28_data_science.md",               "specializations",         "data-science.md"),
    ("_29_computer_vision.md",            "specializations",         "computer-vision.md"),
    ("_30_nlp_generative_ai.md",          "specializations",         "nlp-generative-ai.md"),
    ("_32_mlops_engineering.md",          "specializations",         "mlops-engineering.md"),

    # -- LEARNING PATHS -----------------------------------------------------
    ("_11_dotnet_full_stack.md",           "learning_paths",          "dotnet-full-stack.md"),
    ("_26_iot_full_stack.md",             "learning_paths",          "iot-full-stack.md"),
    ("_31_ai_engineering.md",             "learning_paths",          "ai-engineering.md"),

    # -- ELECTIVES ----------------------------------------------------------
    ("_23_matlab_simulation.md",           "electives",               "matlab.md"),
]


def build_index_files(dry_run: bool = False):
    """Create README.md placeholder files in each new folder."""
    folders = [
        "foundations/programming",
        "foundations/frontend",
        "foundations/backend",
        "foundations/core",
        "specializations",
        "learning_paths",
        "electives",
    ]
    for folder in folders:
        dest_dir = SYLLABUS / folder
        if not dry_run:
            dest_dir.mkdir(parents=True, exist_ok=True)
        readme = dest_dir / "README.md"
        if not readme.exists() and not dry_run:
            tier = folder.split("/")[0].title()
            sub = folder.split("/")[1].title() if "/" in folder else ""
            content = f"# {tier}{f' -- {sub}' if sub else ''}\n\n"
            content += f"**Updated:** {TODAY}\n\n"
            content += "This folder contains syllabus files for the Learning OS curriculum.\n\n"
            content += "Files here are the **source of truth** for this category.\n"
            readme.write_text(content, encoding="utf-8")
        print(f"  {'EXIST' if readme.exists() else 'CREATE'} README.md in {folder}/")


def run(dry_run: bool = False):
    print(f"\n{'='*60}")
    print(f"  Syllabus Reorganizer {'[DRY RUN]' if dry_run else '[EXECUTE]'}")
    print(f"{'='*60}\n")

    migration_log = []
    copied = 0
    skipped = 0
    errors = []

    build_index_files(dry_run=dry_run)

    for src_name, target_folder, dest_name in SYLLABUS_MAP:
        src = SYLLABUS / src_name
        dest_dir = SYLLABUS / target_folder
        dest = dest_dir / dest_name

        if not src.exists():
            errors.append(f"SOURCE NOT FOUND: {src_name}")
            print(f"  MISSING  {src_name}")
            continue

        src_kb = round(src.stat().st_size / 1024, 1)

        if dest.exists():
            skipped += 1
            print(f"  EXISTS   {target_folder}/{dest_name}  ({src_kb} KB)")
            migration_log.append(f"| `{src_name}` | `{target_folder}/{dest_name}` | EXISTS |")
        else:
            if not dry_run:
                dest_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dest)
            copied += 1
            action = "DRYRUN" if dry_run else "COPIED"
            print(f"  {action}   {src_name}  ({src_kb} KB)")
            print(f"           -> {target_folder}/{dest_name}")
            migration_log.append(f"| `{src_name}` | `{target_folder}/{dest_name}` | {'DRY RUN' if dry_run else 'COPIED'} |")

    # -- Generate missing elective placeholders -----------------------------
    elective_placeholders = [
        ("power-bi.md",           "Power BI",            "40-power-bi"),
        ("tableau.md",             "Tableau",             None),
        ("excel-data-analysis.md", "Excel Data Analysis", None),
        ("prompt-engineering.md",  "Prompt Engineering",  "49-prompt-engineering"),
        ("rag-engineering.md",     "RAG Engineering",     "46-rag-engineering"),
        ("ai-agents.md",           "AI Agents",           "47-ai-agents"),
        ("tinyml-edge-ai.md",      "TinyML / Edge AI",    "35-tinyml-edge-ai"),
    ]
    elective_dir = SYLLABUS / "electives"
    for filename, title, curriculum_ref in elective_placeholders:
        dest = elective_dir / filename
        if dest.exists():
            print(f"  EXISTS   electives/{filename}")
        else:
            content = f"# {title} Syllabus\n\n"
            content += f"> **Category:** Elective\n"
            if curriculum_ref:
                content += f"> **Curriculum Reference:** `docs/curriculum/{curriculum_ref}/`\n"
            content += f"> **Status:** Placeholder -- awaiting contributor\n\n"
            content += "---\n\n## Overview\n\n_To be completed by contributor._\n\n"
            content += "## Modules\n\n_See curriculum folder for existing lesson structure._\n"
            if not dry_run:
                elective_dir.mkdir(parents=True, exist_ok=True)
                dest.write_text(content, encoding="utf-8")
            action = "DRYRUN" if dry_run else "CREATED"
            print(f"  {action}   electives/{filename}  (placeholder)")
            migration_log.append(f"| _(generated)_ | `electives/{filename}` | PLACEHOLDER |")

    # -- Generate learning path references ----------------------------------
    lp_placeholders = [
        ("python-full-stack.md",     "Python Full Stack",    ["python-core", "git-version-control", "html5", "css3", "bootstrap", "javascript-core", "mysql", "flask", "fastapi", "rest-api"]),
        ("java-full-stack.md",       "Java Full Stack",      ["java-core", "git-version-control", "html5", "css3", "bootstrap", "javascript-core", "mysql", "spring-boot", "rest-api"]),
        ("frontend-engineering.md",  "Frontend Engineering", ["html5", "css3", "bootstrap", "javascript-core", "jquery", "react"]),
        ("backend-engineering.md",   "Backend Engineering",  ["python-core", "git-version-control", "mysql", "flask", "fastapi", "rest-api", "auth-jwt"]),
        ("data-science-path.md",     "Data Science Path",    ["math-statistics", "python-core", "python-data-science", "data-analytics", "machine-learning", "deep-learning", "mlops"]),
        ("devops-path.md",           "DevOps Engineering",   ["git-version-control", "linux", "docker", "cloud-computing"]),
        ("cloud-engineering-path.md","Cloud Engineering",    ["linux", "git-version-control", "docker", "cloud-computing"]),
    ]
    lp_dir = SYLLABUS / "learning_paths"
    for filename, title, courses in lp_placeholders:
        dest = lp_dir / filename
        if dest.exists():
            print(f"  EXISTS   learning_paths/{filename}")
        else:
            content = f"# {title}\n\n"
            content += f"> **Type:** Learning Path  \n"
            content += f"> **Category:** Career Roadmap  \n\n---\n\n"
            content += "## Course Sequence\n\n"
            content += "> This learning path references reusable courses in order.\n"
            content += "> No course content is duplicated here.\n\n"
            for i, course in enumerate(courses, 1):
                content += f"{i}. [{course}](../foundations/)\n"
            content += "\n## Description\n\n_To be completed._\n"
            if not dry_run:
                lp_dir.mkdir(parents=True, exist_ok=True)
                dest.write_text(content, encoding="utf-8")
            action = "DRYRUN" if dry_run else "CREATED"
            print(f"  {action}   learning_paths/{filename}  (reference)")

    # -- Write migration map ------------------------------------------------
    map_content = f"# Syllabus Migration Map\n\n"
    map_content += f"**Generated:** {TODAY}  \n"
    map_content += f"**Status:** {'DRY RUN' if dry_run else 'EXECUTED'}\n\n"
    map_content += "Maps original flat filenames -> new 4-tier folder hierarchy.\n\n"
    map_content += "| Original File | New Location | Action |\n|---|---|---|\n"
    map_content += "\n".join(migration_log)

    map_path = SYLLABUS / "_MIGRATION_MAP.md"
    if not dry_run:
        map_path.write_text(map_content, encoding="utf-8")

    # -- Summary ------------------------------------------------------------
    print(f"\n{'-'*60}")
    print(f"  Copied:  {copied}")
    print(f"  Exists:  {skipped}")
    print(f"  Errors:  {len(errors)}")
    if errors:
        for e in errors:
            print(f"    {e}")
    print(f"\n  Migration map: docs/syllabus/_MIGRATION_MAP.md")
    print(f"{'-'*60}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    run(dry_run=args.dry_run)

