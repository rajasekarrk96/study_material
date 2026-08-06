"""
Learning OS — DB Migration: Four-Tier Architecture Extension
============================================================
Adds course_type, is_standalone, subtitle to courses;
domain, prerequisite_count, category_id to learning_paths;
role, estimated_hours_in_path to path_courses;
creates learning_path_categories table.

All changes are fully additive (new columns + new table only).
Existing rows keep their server_default values on upgrade.
Fully reversible via downgrade().

Run with:
    flask db upgrade
Or directly:
    alembic upgrade head
"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers — fill in after generating via: flask db migrate
revision = 'add_course_type_lp_category'
down_revision = None          # update this to your current head revision
branch_labels = None
depends_on = None


def upgrade():
    # ── 1. learning_path_categories (must exist before FK on learning_paths) ─
    op.create_table(
        "learning_path_categories",
        sa.Column("id",          sa.Integer(),    primary_key=True,  autoincrement=True),
        sa.Column("name",        sa.String(100),  nullable=False),
        sa.Column("slug",        sa.String(120),  nullable=False),
        sa.Column("description", sa.Text(),       nullable=True),
        sa.Column("icon",        sa.String(100),  nullable=True),
        sa.Column("color",       sa.String(20),   nullable=True),
        sa.Column("sort_order",  sa.Integer(),    nullable=False, server_default="0"),
        sa.Column("is_active",   sa.Boolean(),    nullable=False, server_default="1"),
        sa.Column("created_at",  sa.DateTime(),   nullable=True,  default=datetime.utcnow),
        sa.Column("updated_at",  sa.DateTime(),   nullable=True,  onupdate=datetime.utcnow),
        sa.UniqueConstraint("name", name="uq_lpc_name"),
        sa.UniqueConstraint("slug", name="uq_lpc_slug"),
    )

    # ── 2. courses — 3 new columns ───────────────────────────────────────────
    with op.batch_alter_table("courses") as batch_op:
        batch_op.add_column(
            sa.Column("course_type", sa.String(30), nullable=False, server_default="foundation")
        )
        batch_op.add_column(
            sa.Column("is_standalone", sa.Boolean(), nullable=False, server_default="1")
        )
        batch_op.add_column(
            sa.Column("subtitle", sa.String(255), nullable=True)
        )
        batch_op.create_index("ix_courses_course_type", ["course_type"])

    # ── 3. learning_paths — 3 new columns ───────────────────────────────────
    with op.batch_alter_table("learning_paths") as batch_op:
        batch_op.add_column(
            sa.Column("domain", sa.String(50), nullable=True)
        )
        batch_op.add_column(
            sa.Column("prerequisite_count", sa.Integer(), nullable=False, server_default="0")
        )
        batch_op.add_column(
            sa.Column("category_id", sa.Integer(), nullable=True)
        )
        batch_op.create_index("ix_learning_paths_domain", ["domain"])
        batch_op.create_foreign_key(
            "fk_lp_category_id",
            "learning_path_categories",
            ["category_id"], ["id"],
        )

    # ── 4. path_courses — 2 new columns ─────────────────────────────────────
    with op.batch_alter_table("path_courses") as batch_op:
        batch_op.add_column(
            sa.Column("role", sa.String(30), nullable=False, server_default="core")
        )
        batch_op.add_column(
            sa.Column("estimated_hours_in_path", sa.Integer(), nullable=True)
        )


def downgrade():
    # Reverse order — remove FK dependencies first
    with op.batch_alter_table("path_courses") as batch_op:
        batch_op.drop_column("estimated_hours_in_path")
        batch_op.drop_column("role")

    with op.batch_alter_table("learning_paths") as batch_op:
        batch_op.drop_constraint("fk_lp_category_id", type_="foreignkey")
        batch_op.drop_index("ix_learning_paths_domain")
        batch_op.drop_column("category_id")
        batch_op.drop_column("prerequisite_count")
        batch_op.drop_column("domain")

    with op.batch_alter_table("courses") as batch_op:
        batch_op.drop_index("ix_courses_course_type")
        batch_op.drop_column("subtitle")
        batch_op.drop_column("is_standalone")
        batch_op.drop_column("course_type")

    op.drop_table("learning_path_categories")
