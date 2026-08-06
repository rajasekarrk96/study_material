"""
Learning OS Content Pipeline — Merge Engine
============================================
Merges an approved package's CURRICULUM/ into docs/curriculum/.

Usage:
    # Dry run first (always)
    python content_pipeline/scripts/merge_package.py --package imports/approved/<id> --dry-run

    # Execute merge after reviewing dry run
    python content_pipeline/scripts/merge_package.py --package imports/approved/<id> --execute --admin "name"

Run from project root.
"""
import sys
import re
import shutil
import argparse
from pathlib import Path
from datetime import datetime, timezone

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT         = Path(r"d:\My Drive\all files\PROJECT FILES\notes")
CP           = ROOT / "content_pipeline"
CURRICULUM   = ROOT / "docs" / "curriculum"
STUB_THRESHOLD = 500  # bytes


def today():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def get_target_folder(pkg_path: Path) -> Path | None:
    """Find the matching docs/curriculum/ folder for a package's CURRICULUM/ subfolder."""
    curr_dir = pkg_path / "CURRICULUM"
    if not curr_dir.is_dir():
        return None

    # Read from manifest what course this is
    manifest_path = pkg_path / "PACKAGE_MANIFEST.md"
    if manifest_path.exists():
        content = manifest_path.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"course_name:\s*(.+)", content)
        if m:
            course_slug = m.group(1).strip().lower().replace(" ", "_").replace("-", "_")
            # Try to find matching folder in docs/curriculum/
            for folder in CURRICULUM.iterdir():
                if folder.is_dir():
                    slug = re.sub(r"^\d+-", "", folder.name).replace("-", "_")
                    if slug == course_slug or course_slug in slug:
                        return folder
    return None


def merge_curriculum(pkg_path: Path, dry_run: bool = True, admin: str = "~") -> dict:
    log = {"created": [], "overwritten": [], "skipped": [], "conflicts": [], "errors": []}

    curr_src = pkg_path / "CURRICULUM"
    if not curr_src.is_dir():
        log["errors"].append("No CURRICULUM/ directory in package")
        return log

    for course_dir in curr_src.iterdir():
        if not course_dir.is_dir():
            continue

        # Find corresponding target in docs/curriculum/
        course_name = course_dir.name
        target_dir = None
        for folder in CURRICULUM.iterdir():
            if folder.is_dir():
                slug = re.sub(r"^\d+-", "", folder.name).replace("-", "_").replace(" ", "_")
                if course_name.replace("-", "_") in slug or slug in course_name.replace("-", "_"):
                    target_dir = folder
                    break

        if not target_dir:
            log["errors"].append(f"No matching target folder found for: {course_name}")
            continue

        for src_file in sorted(course_dir.glob("*.md")):
            target_file = target_dir / src_file.name
            src_size = src_file.stat().st_size

            if target_file.exists():
                target_size = target_file.stat().st_size
                if target_size >= STUB_THRESHOLD:
                    # Complete file exists — skip
                    log["skipped"].append(str(src_file.relative_to(pkg_path)))
                else:
                    # Stub — overwrite with new content
                    if src_size < STUB_THRESHOLD:
                        log["skipped"].append(f"{src_file.relative_to(pkg_path)} (source also stub)")
                    else:
                        if not dry_run:
                            shutil.copy2(src_file, target_file)
                        log["overwritten"].append(str(src_file.relative_to(pkg_path)))
            else:
                # New file — create
                if src_size >= STUB_THRESHOLD:
                    if not dry_run:
                        shutil.copy2(src_file, target_file)
                    log["created"].append(str(src_file.relative_to(pkg_path)))
                else:
                    log["skipped"].append(f"{src_file.relative_to(pkg_path)} (source stub, not merging)")

    return log


def write_merge_report(pkg_path: Path, log: dict, dry_run: bool, admin: str):
    mode = "DRY RUN" if dry_run else "EXECUTED"
    report_name = f"MERGE_REPORT_{pkg_path.name}_{today()}_{'dryrun' if dry_run else 'executed'}.md"
    report_path = CP / "reports" / report_name

    lines = [
        f"# Merge Report\n\n",
        f"**package_id:** {pkg_path.name}  \n",
        f"**mode:** {mode}  \n",
        f"**date:** {today()}  \n",
        f"**admin:** {admin}  \n\n---\n\n",
        f"## Summary\n\n",
        f"| Action | Count |\n|---|---|\n",
        f"| Files CREATED | {len(log['created'])} |\n",
        f"| Stubs OVERWRITTEN | {len(log['overwritten'])} |\n",
        f"| Files SKIPPED | {len(log['skipped'])} |\n",
        f"| Conflicts | {len(log['conflicts'])} |\n",
        f"| Errors | {len(log['errors'])} |\n\n",
    ]

    if log["created"]:
        lines.append("## Files Created\n\n")
        for f in log["created"]:
            lines.append(f"- `{f}`\n")
        lines.append("\n")

    if log["overwritten"]:
        lines.append("## Stubs Overwritten\n\n")
        for f in log["overwritten"]:
            lines.append(f"- `{f}`\n")
        lines.append("\n")

    if log["errors"]:
        lines.append("## Errors\n\n")
        for e in log["errors"]:
            lines.append(f"- ❌ {e}\n")
        lines.append("\n")

    if log["conflicts"]:
        lines.append("## Conflicts\n\n")
        for c in log["conflicts"]:
            lines.append(f"- ⚠️ {c}\n")

    report_path.write_text("".join(lines), encoding="utf-8")
    return report_path


def main():
    parser = argparse.ArgumentParser(description="Merge approved package into Learning OS")
    parser.add_argument("--package", required=True)
    parser.add_argument("--dry-run",  action="store_true", default=False)
    parser.add_argument("--execute",  action="store_true", default=False)
    parser.add_argument("--admin",    default="~")
    args = parser.parse_args()

    if not args.dry_run and not args.execute:
        print("  ERROR: Specify --dry-run or --execute")
        sys.exit(1)

    pkg_path = Path(args.package)
    if not pkg_path.is_absolute():
        pkg_path = ROOT / pkg_path

    dry_run = args.dry_run or not args.execute
    mode = "DRY RUN" if dry_run else "EXECUTING MERGE"

    print(f"\n  Merge Engine — {mode}")
    print(f"  {'='*50}")
    print(f"  Package: {pkg_path.name}\n")

    if not dry_run:
        confirm = input("  ⚠️  This will write to docs/curriculum/. Continue? [yes/N]: ")
        if confirm.strip().lower() != "yes":
            print("  Merge cancelled.")
            sys.exit(0)

    log = merge_curriculum(pkg_path, dry_run=dry_run, admin=args.admin)
    report = write_merge_report(pkg_path, log, dry_run=dry_run, admin=args.admin)

    print(f"  Created:     {len(log['created'])}")
    print(f"  Overwritten: {len(log['overwritten'])}")
    print(f"  Skipped:     {len(log['skipped'])}")
    print(f"  Errors:      {len(log['errors'])}")
    print(f"\n  Report: {report}")

    if not dry_run and not log["errors"]:
        print(f"\n  ✅ Merge complete. Run archive_package.py next.\n")
    elif dry_run:
        print(f"\n  Dry run complete. Review report then run with --execute.\n")


if __name__ == "__main__":
    main()
