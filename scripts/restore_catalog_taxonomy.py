#!/usr/bin/env python3
"""Restore subject-to-category catalog mappings from a SQL backup.

The operation is intentionally narrow: it updates only ``subjects.category_id``.
Courses, modules, lessons, users, enrollments, and progress are never replaced.

Examples:
    python scripts/restore_catalog_taxonomy.py backups/backup_20260803_062930.sql
    python scripts/restore_catalog_taxonomy.py backups/backup_20260803_062930.sql --apply
"""
import argparse
import re
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from app import create_app  # noqa: E402
from app.core.cache import clear_cache  # noqa: E402
from app.core.extensions import db  # noqa: E402
from app.domains.content.models import Category, Subject  # noqa: E402


CATEGORY_ROW = re.compile(
    r"VALUES \((?P<id>\d+), '(?:[^']|'')*', '(?P<slug>[^']+)'"
)
SUBJECT_ROW = re.compile(
    r"VALUES \((?P<id>\d+), (?P<category_id>\d+), "
    r"'(?:[^']|'')*', '(?P<slug>[^']+)'"
)


def load_backup_taxonomy(backup_path: Path) -> dict[str, str]:
    """Return a subject slug -> category slug mapping from a SQL backup."""
    category_slugs_by_id: dict[int, str] = {}
    subject_category_ids: dict[str, int] = {}

    with backup_path.open(encoding="utf-8") as backup_file:
        for line in backup_file:
            if line.startswith("INSERT INTO `categories`"):
                match = CATEGORY_ROW.search(line)
                if match:
                    category_slugs_by_id[int(match.group("id"))] = match.group("slug")
            elif line.startswith("INSERT INTO `subjects`"):
                match = SUBJECT_ROW.search(line)
                if match:
                    subject_category_ids[match.group("slug")] = int(
                        match.group("category_id")
                    )

    if not category_slugs_by_id or not subject_category_ids:
        raise ValueError(
            f"No catalog taxonomy records were found in backup: {backup_path}"
        )

    missing_category_ids = sorted(
        set(subject_category_ids.values()) - set(category_slugs_by_id)
    )
    if missing_category_ids:
        raise ValueError(
            "Backup subjects reference missing category IDs: "
            + ", ".join(map(str, missing_category_ids))
        )

    return {
        subject_slug: category_slugs_by_id[category_id]
        for subject_slug, category_id in subject_category_ids.items()
    }


def restore_taxonomy(backup_path: Path, apply_changes: bool = False) -> int:
    backup_mapping = load_backup_taxonomy(backup_path)
    app = create_app()

    with app.app_context():
        categories_by_slug = {category.slug: category for category in Category.query.all()}
        subjects_by_slug = {subject.slug: subject for subject in Subject.query.all()}

        missing_categories = sorted(
            set(backup_mapping.values()) - set(categories_by_slug)
        )
        if missing_categories:
            raise RuntimeError(
                "Current database is missing backup categories: "
                + ", ".join(missing_categories)
            )

        changes = []
        for subject_slug, target_category_slug in sorted(backup_mapping.items()):
            subject = subjects_by_slug.get(subject_slug)
            if subject is None:
                continue
            target_category = categories_by_slug[target_category_slug]
            if subject.category_id == target_category.id:
                continue
            changes.append(
                (
                    subject,
                    subject.category.slug,
                    target_category,
                )
            )

        mode = "APPLY" if apply_changes else "DRY RUN"
        print(f"[{mode}] Source backup: {backup_path}")
        print(f"[{mode}] Subject mappings to restore: {len(changes)}")
        for subject, current_slug, target_category in changes:
            print(f"  {subject.slug}: {current_slug} -> {target_category.slug}")
            subject.category_id = target_category.id

        if apply_changes:
            db.session.commit()
            clear_cache()
            print(f"[APPLY] Restored {len(changes)} subject mappings.")
        else:
            db.session.rollback()
            print("[DRY RUN] No database changes were committed.")

        return len(changes)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("backup", type=Path, help="SQL backup to use as taxonomy source")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Commit the mapping changes (default is a dry run)",
    )
    args = parser.parse_args()

    backup_path = args.backup.resolve()
    if not backup_path.is_file():
        parser.error(f"Backup file not found: {backup_path}")
    restore_taxonomy(backup_path, apply_changes=args.apply)


if __name__ == "__main__":
    main()
