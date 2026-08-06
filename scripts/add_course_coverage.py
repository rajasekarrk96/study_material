"""
Learning OS — Migration Script
Add `course_coverage` column to the `lessons` table.

Usage:
    python scripts/add_course_coverage.py [--dry-run]

Options:
    --dry-run   Show SQL that would run without executing it.

Safe to run multiple times (idempotent — checks if column exists first).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from run import app

DRY_RUN = "--dry-run" in sys.argv

SQL_ADD_COLUMN = """
ALTER TABLE lessons
    ADD COLUMN course_coverage VARCHAR(30) NOT NULL DEFAULT 'covered_in_class';
""".strip()

SQL_CHECK_COLUMN = """
SELECT COUNT(*)
FROM information_schema.columns
WHERE table_name = 'lessons'
  AND column_name = 'course_coverage';
""".strip()

# SQLite fallback check (SQLite doesn't have information_schema)
SQL_CHECK_SQLITE = "PRAGMA table_info(lessons);"

SQL_UPDATE_EXISTING = """
UPDATE lessons
    SET course_coverage = 'covered_in_class'
    WHERE course_coverage IS NULL OR course_coverage = '';
""".strip()

SQL_VERIFY = "SELECT COUNT(*) FROM lessons WHERE course_coverage = 'covered_in_class';"
SQL_TOTAL  = "SELECT COUNT(*) FROM lessons;"


def column_exists(conn, dialect_name: str) -> bool:
    """Returns True if course_coverage already exists in lessons."""
    if "sqlite" in dialect_name:
        result = conn.execute(SQL_CHECK_SQLITE)
        columns = [row[1] for row in result.fetchall()]
        return "course_coverage" in columns
    else:
        result = conn.execute(SQL_CHECK_COLUMN)
        return result.scalar() > 0


def run_migration():
    with app.app_context():
        from app.core.extensions import db
        engine = db.engine
        dialect = engine.dialect.name

        print(f"\n{'='*60}")
        print("  Learning OS — Course Coverage Migration")
        print(f"  Dialect: {dialect}")
        print(f"  Dry Run: {DRY_RUN}")
        print(f"{'='*60}\n")

        with engine.connect() as conn:
            # 1. Check if column already exists
            exists = column_exists(conn, dialect)
            if exists:
                print("✅ Column `course_coverage` already exists in `lessons`.")
                print("   Skipping ALTER TABLE — migration is idempotent.\n")
            else:
                # 2. Add column
                print(f"SQL to execute:\n  {SQL_ADD_COLUMN}\n")
                if not DRY_RUN:
                    conn.execute(SQL_ADD_COLUMN)
                    conn.commit()
                    print("✅ Column `course_coverage` added to `lessons`.\n")
                else:
                    print("   [DRY RUN] Skipped execution.\n")

            if not DRY_RUN:
                # 3. Back-fill any NULLs just in case
                conn.execute(SQL_UPDATE_EXISTING)
                conn.commit()

                # 4. Verify
                covered = conn.execute(SQL_VERIFY).scalar()
                total   = conn.execute(SQL_TOTAL).scalar()
                print(f"📊 Verification:")
                print(f"   Total lessons        : {total}")
                print(f"   course_coverage set  : {covered}")
                pct = (covered / total * 100) if total else 0
                print(f"   Coverage             : {pct:.1f}%\n")

                if covered == total:
                    print("✅ All lessons have course_coverage = 'covered_in_class'.")
                else:
                    diff = total - covered
                    print(f"⚠️  {diff} lessons still have NULL or non-default coverage.")
            else:
                print("[DRY RUN] Verification skipped.")

        print(f"\n{'='*60}")
        print("  Migration complete.")
        print(f"{'='*60}\n")


if __name__ == "__main__":
    run_migration()
