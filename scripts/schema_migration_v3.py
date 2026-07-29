"""
schema_migration_v3.py
======================
Adds new columns to existing tables and creates new tables for v3.0.
Uses raw ALTER TABLE because db.create_all() won't add columns to existing tables.
Safe to re-run — all statements use IF NOT EXISTS / try/except.
"""
import sys
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

from app import create_app
from app.core.extensions import db

app = create_app()

ALTER_STATEMENTS = [
    # ── learning_paths: new columns ───────────────────────────────────────────
    "ALTER TABLE learning_paths ADD COLUMN target_role      VARCHAR(150)  NULL",
    "ALTER TABLE learning_paths ADD COLUMN difficulty_level VARCHAR(20)   NOT NULL DEFAULT 'beginner'",
    "ALTER TABLE learning_paths ADD COLUMN estimated_hours  INT           NOT NULL DEFAULT 0",
    "ALTER TABLE learning_paths ADD COLUMN icon             VARCHAR(100)  NULL",
    "ALTER TABLE learning_paths ADD COLUMN color            VARCHAR(20)   NULL",
    "ALTER TABLE learning_paths ADD COLUMN thumbnail_url    VARCHAR(500)  NULL",
    "ALTER TABLE learning_paths ADD COLUMN is_featured      TINYINT(1)    NOT NULL DEFAULT 0",
    "ALTER TABLE learning_paths ADD COLUMN sort_order       INT           NOT NULL DEFAULT 0",

    # ── path_courses: new columns ─────────────────────────────────────────────
    "ALTER TABLE path_courses ADD COLUMN is_required    TINYINT(1)    NOT NULL DEFAULT 1",
    "ALTER TABLE path_courses ADD COLUMN section_label  VARCHAR(100)  NULL",
]

CREATE_STATEMENTS = [
    # ── user_learning_path_progress ───────────────────────────────────────────
    """
    CREATE TABLE IF NOT EXISTS user_learning_path_progress (
        id                  INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
        user_id             INT          NOT NULL,
        path_id             INT          NOT NULL,
        enrolled_at         DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
        completed_courses   INT          NOT NULL DEFAULT 0,
        total_courses       INT          NOT NULL DEFAULT 0,
        is_completed        TINYINT(1)   NOT NULL DEFAULT 0,
        completed_at        DATETIME     NULL,
        created_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (path_id) REFERENCES learning_paths(id)
    )
    """,

    # ── learning_path_certificates ────────────────────────────────────────────
    """
    CREATE TABLE IF NOT EXISTS learning_path_certificates (
        id          INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
        path_id     INT          NOT NULL UNIQUE,
        title       VARCHAR(255) NOT NULL,
        description TEXT         NULL,
        created_at  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (path_id) REFERENCES learning_paths(id)
    )
    """,

    # ── user_learning_path_certificates ───────────────────────────────────────
    """
    CREATE TABLE IF NOT EXISTS user_learning_path_certificates (
        id                   INT       NOT NULL AUTO_INCREMENT PRIMARY KEY,
        user_id              INT       NOT NULL,
        path_certificate_id  INT       NOT NULL,
        issued_at            DATETIME  NOT NULL DEFAULT CURRENT_TIMESTAMP,
        created_at           DATETIME  NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at           DATETIME  NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id)             REFERENCES users(id),
        FOREIGN KEY (path_certificate_id) REFERENCES learning_path_certificates(id)
    )
    """,
]

with app.app_context():
    print("\n" + "="*65)
    print("SCHEMA MIGRATION v3.0")
    print("="*65)

    conn = db.engine.connect()

    print("\n[ALTER] Adding new columns to existing tables...")
    for sql in ALTER_STATEMENTS:
        col_name = sql.split("ADD COLUMN")[1].strip().split()[0]
        try:
            conn.execute(db.text(sql))
            print(f"  [OK]   Added column: {col_name}")
        except Exception as e:
            err = str(e)
            if "Duplicate column name" in err or "already exists" in err.lower():
                print(f"  [SKIP] Column already exists: {col_name}")
            else:
                print(f"  [ERR]  {col_name}: {err[:120]}")

    print("\n[CREATE] Creating new tables...")
    for sql in CREATE_STATEMENTS:
        # Extract table name from CREATE TABLE IF NOT EXISTS <name>
        table_name = sql.strip().split()[5]
        try:
            conn.execute(db.text(sql))
            print(f"  [OK]   Table: {table_name}")
        except Exception as e:
            print(f"  [ERR]  {table_name}: {str(e)[:120]}")

    conn.commit()
    conn.close()
    print("\n[OK] Schema migration v3.0 complete.")
