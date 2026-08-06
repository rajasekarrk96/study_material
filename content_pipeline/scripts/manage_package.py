"""
Learning OS Content Pipeline — Package State Manager
=====================================================
Moves packages between pipeline states and maintains the registry.

Usage:
    python content_pipeline/scripts/manage_package.py --action <action> --package <path> [options]

Actions:
    move_to_review   --package imports/pending_review/<id>
    approve          --package imports/under_review/<id> --reviewer "name" --score 4.5
    reject           --package imports/under_review/<id> --reviewer "name" --reason "..."
    archive          --package imports/approved/<id>
    list             --state <state>  (exported|pending_review|under_review|approved|rejected|archived)

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

ROOT = Path(r"d:\My Drive\all files\PROJECT FILES\notes")
CP   = ROOT / "content_pipeline"


def today():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def update_manifest(pkg_path: Path, updates: dict):
    """Update YAML-like fields in PACKAGE_MANIFEST.md"""
    manifest_path = pkg_path / "PACKAGE_MANIFEST.md"
    if not manifest_path.exists():
        print(f"  WARNING: No PACKAGE_MANIFEST.md found in {pkg_path}")
        return

    content = manifest_path.read_text(encoding="utf-8", errors="replace")
    for key, value in updates.items():
        # Replace the field's value (handles "key:  ~" or "key:  old_value")
        content = re.sub(
            rf"^({re.escape(key)}:\s*).*$",
            rf"\g<1>{value}",
            content,
            flags=re.MULTILINE
        )
    manifest_path.write_text(content, encoding="utf-8")


def update_registry(package_id: str, updates: dict):
    """Update a row in the registry (simple text-based approach)."""
    reg_path = CP / "registry" / "PACKAGE_REGISTRY.md"
    if not reg_path.exists():
        return
    content = reg_path.read_text(encoding="utf-8", errors="replace")
    if package_id in content:
        for key, val in updates.items():
            print(f"  Registry update: {key} = {val}")
    # In production this would update the table row
    # For now, log the update
    reg_path.write_text(content, encoding="utf-8")


def move_to_review(args):
    src = Path(args.package)
    if not src.is_absolute():
        src = ROOT / src
    dst_dir = CP / "imports" / "under_review"
    dst = dst_dir / src.name
    dst_dir.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dst))
    update_manifest(dst, {
        "status":             "UNDER_REVIEW",
        "review_start_date":  today(),
    })
    print(f"  [OK] Moved to under_review: {src.name}")
    print(f"  Path: {dst}")


def approve(args):
    src = Path(args.package)
    if not src.is_absolute():
        src = ROOT / src
    dst_dir = CP / "imports" / "approved"
    dst = dst_dir / src.name
    dst_dir.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dst))
    reviewer = getattr(args, "reviewer", "~")
    score    = getattr(args, "score", "~")
    update_manifest(dst, {
        "status":           "APPROVED",
        "decision":         "APPROVED",
        "decision_date":    today(),
        "reviewed_by":      reviewer,
        "review_score":     str(score),
        "review_end_date":  today(),
    })
    print(f"  [APPROVED] {src.name}")
    print(f"  Reviewer: {reviewer} | Score: {score}")
    print(f"  Path: {dst}")


def reject(args):
    src = Path(args.package)
    if not src.is_absolute():
        src = ROOT / src
    dst_dir = CP / "imports" / "rejected"
    dst = dst_dir / src.name
    dst_dir.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dst))
    reviewer = getattr(args, "reviewer", "~")
    reason   = getattr(args, "reason", "See review comments")
    update_manifest(dst, {
        "status":           "REJECTED",
        "decision":         "REJECTED",
        "decision_date":    today(),
        "reviewed_by":      reviewer,
        "review_end_date":  today(),
        "decision_notes":   reason,
    })
    print(f"  [REJECTED] {src.name}")
    print(f"  Reviewer: {reviewer}")
    print(f"  Reason: {reason}")
    print(f"  Path: {dst}")


def archive(args):
    src = Path(args.package)
    if not src.is_absolute():
        src = ROOT / src

    # Read package type from manifest
    manifest_path = src / "PACKAGE_MANIFEST.md"
    pkg_type = "shared"
    version  = "1.0.0"
    if manifest_path.exists():
        content = manifest_path.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"package_type:\s*(\S+)", content)
        if m: pkg_type = m.group(1)
        v = re.search(r"version:\s*(\S+)", content)
        if v: version = v.group(1)

    archive_name = f"{src.name}_v{version}_{today()}"
    dst_dir = CP / "completed" / pkg_type
    dst = dst_dir / archive_name
    dst_dir.mkdir(parents=True, exist_ok=True)
    shutil.copytree(str(src), str(dst))
    shutil.rmtree(str(src))

    # Update archive index
    idx_path = CP / "registry" / "ARCHIVE_INDEX.md"
    if idx_path.exists():
        idx = idx_path.read_text(encoding="utf-8", errors="replace")
        if "_(no archived packages yet)_" in idx:
            idx = idx.replace("| _(no archived packages yet)_ | | | | | | |", "")
        idx += f"\n| {src.name} | | {pkg_type} | {version} | {today()} | completed/{pkg_type}/{archive_name} | |"
        idx_path.write_text(idx, encoding="utf-8")

    print(f"  [ARCHIVED] {src.name}")
    print(f"  Archive: {dst}")


def list_packages(args):
    state_map = {
        "exported":       CP / "exports",
        "pending_review": CP / "imports" / "pending_review",
        "under_review":   CP / "imports" / "under_review",
        "approved":       CP / "imports" / "approved",
        "rejected":       CP / "imports" / "rejected",
        "archived":       CP / "completed",
    }
    state = getattr(args, "state", "all")
    dirs_to_check = [state_map[state]] if state in state_map else list(state_map.values())

    print(f"\n  Packages — state: {state}")
    print(f"  {'─'*50}")
    found = 0
    for d in dirs_to_check:
        if d.exists():
            for pkg in sorted(d.rglob("PACKAGE_MANIFEST.md")):
                print(f"  {pkg.parent.relative_to(CP)}")
                found += 1
    if found == 0:
        print(f"  (none found)")
    print()


def main():
    parser = argparse.ArgumentParser(description="Content Pipeline Package Manager")
    parser.add_argument("--action", required=True,
        choices=["move_to_review", "approve", "reject", "archive", "list"])
    parser.add_argument("--package",  default=None)
    parser.add_argument("--reviewer", default="~")
    parser.add_argument("--score",    default="~")
    parser.add_argument("--reason",   default="See review comments")
    parser.add_argument("--state",    default="all")
    args = parser.parse_args()

    print(f"\n  Content Pipeline — {args.action.upper()}")
    print(f"  {'='*50}\n")

    actions = {
        "move_to_review": move_to_review,
        "approve":        approve,
        "reject":         reject,
        "archive":        archive,
        "list":           list_packages,
    }
    actions[args.action](args)


if __name__ == "__main__":
    main()
