"""
Learning OS -- Curriculum 4-Tier Reorganizer
=============================================
Moves (not copies) all numbered curriculum folders into the same
4-tier hierarchy used by docs/syllabus/:

  foundations/programming/
  foundations/frontend/
  foundations/backend/
  foundations/core/
  specializations/
  learning_paths/
  electives/

SAFE:
  - Moves folders (no duplicates left behind)
  - Idempotent: skips folders already in correct location
  - Generates CURRICULUM_MIGRATION_MAP.md

Usage:
    python scripts/reorganize_curriculum.py --dry-run
    python scripts/reorganize_curriculum.py
"""
import sys
import shutil
import argparse
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(r"d:\My Drive\all files\PROJECT FILES\notes")
CURRICULUM = ROOT / "docs" / "curriculum"
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")

# ── Complete mapping: source folder -> target subfolder ────────────────────────
# Format: "source_folder_name": "tier/sub-tier"
CURRICULUM_MAP = {
    # ── FOUNDATIONS / Programming ──────────────────────────────────────────────
    "01-c-programming":         "foundations/programming",
    "02-cpp-programming":       "foundations/programming",
    "03-git-version-control":   "foundations/programming",
    "09-python-core":           "foundations/programming",
    "10-advanced-python":       "foundations/programming",
    "11-java-core":             "foundations/programming",
    "12-spring-boot":           "foundations/programming",
    "50-python-dsa":            "foundations/programming",
    "27-embedded-c":            "foundations/programming",
    "39-python-data-science":   "foundations/programming",
    "51-dotnet-full-stack":     "foundations/programming",

    # ── FOUNDATIONS / Frontend ─────────────────────────────────────────────────
    "04-html5-essentials":      "foundations/frontend",
    "05-css3-styling":          "foundations/frontend",
    "06-bootstrap-framework":   "foundations/frontend",
    "07-jquery-library":        "foundations/frontend",
    "08-javascript-core":       "foundations/frontend",
    "20-react-frontend":        "foundations/frontend",

    # ── FOUNDATIONS / Backend ──────────────────────────────────────────────────
    "13-mysql-database":        "foundations/backend",
    "14-sql-server":            "foundations/backend",
    "15-mongodb-nosql":         "foundations/backend",
    "16-flask-backend":         "foundations/backend",
    "17-fastapi-backend":       "foundations/backend",
    "18-rest-api-design":       "foundations/backend",
    "19-auth-jwt-security":     "foundations/backend",
    "55-database-technologies": "foundations/backend",

    # ── FOUNDATIONS / Core ─────────────────────────────────────────────────────
    "22-linux-administration":  "foundations/core",
    "23-docker-containers":     "foundations/core",
    "24-electrical-fundamentals":"foundations/core",
    "25-electronics-basics":    "foundations/core",
    "28-arduino-platform":      "foundations/core",
    "29-esp32-microcontroller": "foundations/core",
    "30-raspberry-pi":          "foundations/core",
    "31-sensors-actuators":     "foundations/core",
    "36-iot-hardware":          "foundations/core",
    "37-iot-projects":          "foundations/core",
    "38-ds-math-statistics":    "foundations/core",

    # ── SPECIALIZATIONS ────────────────────────────────────────────────────────
    "21-selenium-automation":   "specializations",
    "26-pcb-design":            "specializations",
    "32-mqtt-protocol":         "specializations",
    "33-stm32-firmware":        "specializations",
    "34-firebase-cloud":        "specializations",
    "41-machine-learning":      "specializations",
    "42-deep-learning":         "specializations",
    "43-computer-vision":       "specializations",
    "44-nlp-systems":           "specializations",
    "48-mlops-ai-deployment":   "specializations",
    "53-cloud-computing":       "specializations",
    "54-software-testing":      "specializations",

    # ── ELECTIVES ──────────────────────────────────────────────────────────────
    "35-tinyml-edge-ai":        "electives",
    "40-power-bi":              "electives",
    "45-generative-ai-llms":    "electives",
    "46-rag-engineering":       "electives",
    "47-ai-agents":             "electives",
    "49-prompt-engineering":    "electives",
    "52-matlab-simulation":     "electives",
}


def run(dry_run: bool = False):
    print(f"\n{'='*60}")
    print(f"  Curriculum Reorganizer {'[DRY RUN]' if dry_run else '[EXECUTE]'}")
    print(f"{'='*60}\n")

    migration_log = []
    moved = 0
    skipped = 0
    errors = []

    # Create all target directories upfront
    target_dirs = set(CURRICULUM_MAP.values())
    for tdir in sorted(target_dirs):
        dest_dir = CURRICULUM / tdir
        if not dry_run:
            dest_dir.mkdir(parents=True, exist_ok=True)

    for src_name, target_subfolder in CURRICULUM_MAP.items():
        src = CURRICULUM / src_name
        dest_dir = CURRICULUM / target_subfolder
        dest = dest_dir / src_name

        if not src.exists():
            # Check if it was already moved
            if dest.exists():
                skipped += 1
                print(f"  ALREADY   {target_subfolder}/{src_name}")
                migration_log.append(f"| `{src_name}` | `{target_subfolder}/{src_name}` | ALREADY MOVED |")
            else:
                errors.append(f"NOT FOUND: {src_name}")
                print(f"  MISSING   {src_name}")
                migration_log.append(f"| `{src_name}` | `{target_subfolder}/{src_name}` | NOT FOUND |")
            continue

        # Count lessons inside for reporting
        lesson_count = len(list(src.rglob("*.md")))

        if not dry_run:
            dest_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dest))
        
        moved += 1
        action = "DRYRUN" if dry_run else "MOVED"
        print(f"  {action}     {src_name}  ({lesson_count} md files)")
        print(f"             -> {target_subfolder}/")
        migration_log.append(f"| `{src_name}` | `{target_subfolder}/{src_name}` | {action} |")

    # ── Check for any unmapped folders left in root ───────────────────────────
    remaining = [
        d for d in CURRICULUM.iterdir()
        if d.is_dir() and d.name not in ("foundations", "specializations", "learning_paths", "electives")
    ]
    if remaining:
        print(f"\n  Unmapped folders remaining in root ({len(remaining)}):")
        for r in remaining:
            print(f"    {r.name}  <-- review manually")
            migration_log.append(f"| `{r.name}` | _(unmapped)_ | REVIEW |")

    # ── Write migration map ────────────────────────────────────────────────────
    map_content = f"# Curriculum Migration Map\n\n"
    map_content += f"**Generated:** {TODAY}  \n"
    map_content += f"**Status:** {'DRY RUN' if dry_run else 'EXECUTED'}\n\n"
    map_content += "Maps original numbered folders -> new 4-tier hierarchy.\n\n"
    map_content += "| Original Folder | New Location | Action |\n|---|---|---|\n"
    map_content += "\n".join(migration_log)

    if not dry_run:
        map_path = CURRICULUM / "CURRICULUM_MIGRATION_MAP.md"
        map_path.write_text(map_content, encoding="utf-8")

    # ── Summary ────────────────────────────────────────────────────────────────
    print(f"\n{'--'*30}")
    print(f"  Moved:    {moved}")
    print(f"  Skipped:  {skipped}")
    print(f"  Errors:   {len(errors)}")
    if errors:
        for e in errors:
            print(f"    {e}")
    print(f"{'--'*30}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    run(dry_run=args.dry_run)
