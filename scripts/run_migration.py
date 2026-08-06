"""
Learning OS -- Direct Database Migration Runner
================================================
Adds the 4-tier architecture columns directly via raw SQL.
Works without flask-migrate since the project uses db.create_all().

This script:
  1. Reads DB credentials from .env
  2. Checks which columns/tables already exist (idempotent)
  3. Applies only missing DDL statements
  4. Runs seed_course_types and seed_learning_paths

Usage:
    python scripts/run_migration.py --check    (check what needs to run)
    python scripts/run_migration.py            (apply all pending changes)
"""
import sys
import os
import argparse

ROOT_DIR = r"d:\My Drive\all files\PROJECT FILES\notes"
sys.path.insert(0, ROOT_DIR)

# Load .env so we have DB credentials
from dotenv import load_dotenv
load_dotenv(os.path.join(ROOT_DIR, ".env"))


def get_connection():
    """Get a raw PyMySQL connection using TiDB SSL settings from .env."""
    import pymysql
    import re
    from app.core.config import config

    uri = config.db.database_uri
    ca_path = config.db.tidb_ssl_ca

    # Parse URI: mysql+pymysql://user:pass@host:port/dbname
    # URL-decode %40 -> @, %23 -> # etc. in password
    from urllib.parse import unquote
    m = re.match(r"mysql\+pymysql://([^:]+):(.+)@([^@:/]+(?::\d+)?)/([^\?]+)", uri)
    if not m:
        raise ValueError(f"Cannot parse DB URI: {uri[:40]}...")
    user_raw, pass_raw, hostport, dbname = m.groups()
    user = unquote(user_raw)
    password = unquote(pass_raw)
    if ":" in hostport:
        host, port_str = hostport.rsplit(":", 1)
        port = int(port_str)
    else:
        host = hostport
        port = 4000  # TiDB default

    # Strip query string from dbname if present
    dbname = dbname.split("?")[0]

    # Build SSL dict -- TiDB serverless requires TLS
    ssl_params = {}
    if ca_path and os.path.isfile(ca_path):
        ssl_params = {"ca": ca_path}
    else:
        # No CA file -- use SSL without verification (for serverless)
        ssl_params = {"ssl_disabled": False}

    connect_kwargs = dict(
        host=host,
        port=port,
        user=user,
        password=password,
        database=dbname,
        charset="utf8mb4",
        autocommit=False,
    )
    if ca_path and os.path.isfile(ca_path):
        connect_kwargs["ssl"] = {"ca": ca_path}
    else:
        # Enable SSL without cert verification for TiDB serverless
        import ssl as ssl_module
        ssl_ctx = ssl_module.create_default_context()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl_module.CERT_NONE
        connect_kwargs["ssl"] = ssl_ctx

    conn = pymysql.connect(**connect_kwargs)
    return conn, dbname


def column_exists(cursor, table, column, dbname):
    cursor.execute("""
        SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s AND COLUMN_NAME = %s
    """, (dbname, table, column))
    return cursor.fetchone()[0] > 0


def table_exists(cursor, table, dbname):
    cursor.execute("""
        SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s
    """, (dbname, table))
    return cursor.fetchone()[0] > 0


def index_exists(cursor, table, index_name, dbname):
    cursor.execute("""
        SELECT COUNT(*) FROM INFORMATION_SCHEMA.STATISTICS
        WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s AND INDEX_NAME = %s
    """, (dbname, table, index_name))
    return cursor.fetchone()[0] > 0


def run_migration(check_only: bool = False):
    conn, dbname = get_connection()
    cursor = conn.cursor()

    print(f"\n{'='*60}")
    print(f"  DB Migration: 4-Tier Architecture {'[CHECK]' if check_only else '[APPLY]'}")
    print(f"  Database: {dbname}")
    print(f"{'='*60}\n")

    pending = []
    applied = []

    # -- DDL Statements --------------------------------------------------------

    # 1. Create learning_path_categories table
    if not table_exists(cursor, "learning_path_categories", dbname):
        pending.append(("CREATE TABLE learning_path_categories", """
            CREATE TABLE learning_path_categories (
                id          INT AUTO_INCREMENT PRIMARY KEY,
                name        VARCHAR(100) NOT NULL UNIQUE,
                slug        VARCHAR(120) NOT NULL UNIQUE,
                description TEXT,
                icon        VARCHAR(100),
                color       VARCHAR(20),
                sort_order  INT NOT NULL DEFAULT 0,
                is_active   TINYINT(1) NOT NULL DEFAULT 1,
                created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at  DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """))
    else:
        applied.append("learning_path_categories table already exists OK")

    # 2. courses.course_type
    if not column_exists(cursor, "courses", "course_type", dbname):
        pending.append(("ADD courses.course_type", """
            ALTER TABLE courses
            ADD COLUMN course_type VARCHAR(30) NOT NULL DEFAULT 'foundation'
            AFTER published_at
        """))
    else:
        applied.append("courses.course_type already exists OK")

    # 3. courses.is_standalone
    if not column_exists(cursor, "courses", "is_standalone", dbname):
        pending.append(("ADD courses.is_standalone", """
            ALTER TABLE courses
            ADD COLUMN is_standalone TINYINT(1) NOT NULL DEFAULT 1
            AFTER course_type
        """))
    else:
        applied.append("courses.is_standalone already exists OK")

    # 4. courses.subtitle
    if not column_exists(cursor, "courses", "subtitle", dbname):
        pending.append(("ADD courses.subtitle", """
            ALTER TABLE courses
            ADD COLUMN subtitle VARCHAR(255)
            AFTER is_standalone
        """))
    else:
        applied.append("courses.subtitle already exists OK")

    # 5. Index on courses.course_type
    if not index_exists(cursor, "courses", "ix_courses_course_type", dbname):
        pending.append(("INDEX ix_courses_course_type", """
            ALTER TABLE courses
            ADD INDEX ix_courses_course_type (course_type)
        """))
    else:
        applied.append("ix_courses_course_type index already exists OK")

    # 6. learning_paths.domain
    if not column_exists(cursor, "learning_paths", "domain", dbname):
        pending.append(("ADD learning_paths.domain", """
            ALTER TABLE learning_paths
            ADD COLUMN domain VARCHAR(50)
            AFTER sort_order
        """))
    else:
        applied.append("learning_paths.domain already exists OK")

    # 7. learning_paths.prerequisite_count
    if not column_exists(cursor, "learning_paths", "prerequisite_count", dbname):
        pending.append(("ADD learning_paths.prerequisite_count", """
            ALTER TABLE learning_paths
            ADD COLUMN prerequisite_count INT NOT NULL DEFAULT 0
            AFTER domain
        """))
    else:
        applied.append("learning_paths.prerequisite_count already exists OK")

    # 8. learning_paths.category_id
    if not column_exists(cursor, "learning_paths", "category_id", dbname):
        pending.append(("ADD learning_paths.category_id", """
            ALTER TABLE learning_paths
            ADD COLUMN category_id INT
            AFTER prerequisite_count
        """))
        # FK is added separately after table exists
        pending.append(("FK fk_lp_category_id", """
            ALTER TABLE learning_paths
            ADD CONSTRAINT fk_lp_category_id
            FOREIGN KEY (category_id) REFERENCES learning_path_categories(id)
            ON DELETE SET NULL
        """))
    else:
        applied.append("learning_paths.category_id already exists OK")

    # 9. path_courses.role
    if not column_exists(cursor, "path_courses", "role", dbname):
        pending.append(("ADD path_courses.role", """
            ALTER TABLE path_courses
            ADD COLUMN role VARCHAR(30) NOT NULL DEFAULT 'core'
            AFTER section_label
        """))
    else:
        applied.append("path_courses.role already exists OK")

    # 10. path_courses.estimated_hours_in_path
    if not column_exists(cursor, "path_courses", "estimated_hours_in_path", dbname):
        pending.append(("ADD path_courses.estimated_hours_in_path", """
            ALTER TABLE path_courses
            ADD COLUMN estimated_hours_in_path INT
            AFTER role
        """))
    else:
        applied.append("path_courses.estimated_hours_in_path already exists OK")
        applied.append("path_courses.estimated_hours_in_path already exists OK")

    # -- Report ----------------------------------------------------------------
    if applied:
        print(f"  Already applied ({len(applied)}):")
        for a in applied:
            print(f"    OK  {a}")

    if pending:
        print(f"\n  Pending ({len(pending)}):")
        for name, sql in pending:
            print(f"    -> {name}")

    if not pending:
        print("\n  [OK] Database is up to date. Nothing to apply.\n")
        cursor.close()
        conn.close()
        return True

    if check_only:
        print(f"\n  DRY CHECK -- run without --check to apply.\n")
        cursor.close()
        conn.close()
        return False

    # -- Apply -----------------------------------------------------------------
    print(f"\n  Applying {len(pending)} changes...")
    errors = []
    for name, sql in pending:
        try:
            cursor.execute(sql.strip())
            conn.commit()
            print(f"    [DONE] {name}")
        except Exception as e:
            conn.rollback()
            print(f"    [FAIL] {name}: {e}")
            errors.append((name, str(e)))

    cursor.close()
    conn.close()

    if errors:
        print(f"\n  [ERRORS] {len(errors)} error(s) -- review above.")
        return False
    else:
        print("\n  [SUCCESS] All changes applied successfully.\n")
        return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Check only, don't apply")
    args = parser.parse_args()
    success = run_migration(check_only=args.check)
    sys.exit(0 if success else 1)


