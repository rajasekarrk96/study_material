"""
Learning OS — DB Migration: LCMS Enterprise v2.3 Schema Extension
================================================================
Updates existing tables (courses, modules, lessons, lesson_sections,
path_courses, content_quality_scores) by adding columns defined in v2.3.

Safe to run multiple times.
"""
import sys
import os
from sqlalchemy import text

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from run import app

ALTER_QUERIES = [
    # ── 1. courses ──────────────────────────────────────────────────────────
    "ALTER TABLE courses ADD COLUMN IF NOT EXISTS category_id INT NULL;",
    "ALTER TABLE courses ADD COLUMN IF NOT EXISTS difficulty VARCHAR(50) NOT NULL DEFAULT 'BEGINNER';",
    "ALTER TABLE courses ADD COLUMN IF NOT EXISTS estimated_minutes INT NOT NULL DEFAULT 0;",
    
    # ── 2. modules ───────────────────────────────────────────────────────────
    "ALTER TABLE modules ADD COLUMN IF NOT EXISTS slug VARCHAR(280) NULL;",
    "ALTER TABLE modules ADD COLUMN IF NOT EXISTS difficulty VARCHAR(50) NOT NULL DEFAULT 'BEGINNER';",
    "ALTER TABLE modules ADD COLUMN IF NOT EXISTS estimated_minutes INT NOT NULL DEFAULT 0;",

    # ── 3. lessons ───────────────────────────────────────────────────────────
    "ALTER TABLE lessons ADD COLUMN IF NOT EXISTS content_status VARCHAR(50) NOT NULL DEFAULT 'DRAFT';",
    "ALTER TABLE lessons ADD COLUMN IF NOT EXISTS difficulty VARCHAR(50) NOT NULL DEFAULT 'BEGINNER';",

    # ── 4. lesson_sections ───────────────────────────────────────────────────
    "ALTER TABLE lesson_sections ADD COLUMN IF NOT EXISTS content_status VARCHAR(50) NOT NULL DEFAULT 'DRAFT';",
    "ALTER TABLE lesson_sections ADD COLUMN IF NOT EXISTS slug VARCHAR(280) NULL;",
    "ALTER TABLE lesson_sections ADD COLUMN IF NOT EXISTS difficulty VARCHAR(50) NOT NULL DEFAULT 'BEGINNER';",
    "ALTER TABLE lesson_sections ADD COLUMN IF NOT EXISTS estimated_minutes INT NOT NULL DEFAULT 0;",

    # ── 5. path_courses ──────────────────────────────────────────────────────
    "ALTER TABLE path_courses ADD COLUMN IF NOT EXISTS sequence INT NULL;",
    "ALTER TABLE path_courses ADD COLUMN IF NOT EXISTS is_required BOOLEAN NOT NULL DEFAULT 1;",
    "ALTER TABLE path_courses ADD COLUMN IF NOT EXISTS recommended_hours INT NULL;",
    "ALTER TABLE path_courses ADD COLUMN IF NOT EXISTS optional BOOLEAN NOT NULL DEFAULT 0;",
    "ALTER TABLE path_courses ADD COLUMN IF NOT EXISTS unlock_after INT NOT NULL DEFAULT 0;",

    # ── 6. content_quality_scores ────────────────────────────────────────────
    "ALTER TABLE content_quality_scores ADD COLUMN IF NOT EXISTS grammar_score DOUBLE PRECISION NOT NULL DEFAULT 0.0;",
    "ALTER TABLE content_quality_scores ADD COLUMN IF NOT EXISTS technical_accuracy_score DOUBLE PRECISION NOT NULL DEFAULT 0.0;",
    "ALTER TABLE content_quality_scores ADD COLUMN IF NOT EXISTS code_quality_score DOUBLE PRECISION NOT NULL DEFAULT 0.0;",
    "ALTER TABLE content_quality_scores ADD COLUMN IF NOT EXISTS images_score DOUBLE PRECISION NOT NULL DEFAULT 0.0;",
    "ALTER TABLE content_quality_scores ADD COLUMN IF NOT EXISTS examples_score DOUBLE PRECISION NOT NULL DEFAULT 0.0;",
    "ALTER TABLE content_quality_scores ADD COLUMN IF NOT EXISTS quiz_coverage_score DOUBLE PRECISION NOT NULL DEFAULT 0.0;",
    "ALTER TABLE content_quality_scores ADD COLUMN IF NOT EXISTS references_score DOUBLE PRECISION NOT NULL DEFAULT 0.0;",
    "ALTER TABLE content_quality_scores ADD COLUMN IF NOT EXISTS seo_score DOUBLE PRECISION NOT NULL DEFAULT 0.0;",
    "ALTER TABLE content_quality_scores ADD COLUMN IF NOT EXISTS accessibility_score DOUBLE PRECISION NOT NULL DEFAULT 0.0;",
    "ALTER TABLE content_quality_scores ADD COLUMN IF NOT EXISTS overall_quality_percentage INT NOT NULL DEFAULT 0;"
]

FOREIGN_KEY_QUERIES = [
    # Add foreign key constraints if not existing (wrapped in try/except in execution)
    "ALTER TABLE courses ADD CONSTRAINT fk_course_category FOREIGN KEY (category_id) REFERENCES course_categories(id);"
]


def run_migration():
    with app.app_context():
        from app.core.extensions import db
        engine = db.engine
        dialect = engine.dialect.name

        print(f"\n{'='*60}")
        print("  Learning OS — LCMS v2.3 Schema Upgrade")
        print(f"  Dialect: {dialect}")
        print(f"{'='*60}\n")

        with engine.connect() as conn:
            # 1. Execute alter table queries
            for query in ALTER_QUERIES:
                try:
                    print(f"Executing: {query}")
                    conn.execute(text(query))
                    conn.commit()
                except Exception as e:
                    print(f"  [ERROR/INFO] {e}")

            # 2. Execute FK constraints
            for query in FOREIGN_KEY_QUERIES:
                try:
                    print(f"Executing FK Constraint: {query}")
                    conn.execute(text(query))
                    conn.commit()
                except Exception as e:
                    print(f"  [INFO] Skipping FK addition (likely already exists): {e}")

        print(f"\n{'='*60}")
        print("  Migration completed.")
        print(f"{'='*60}\n")


if __name__ == "__main__":
    run_migration()
