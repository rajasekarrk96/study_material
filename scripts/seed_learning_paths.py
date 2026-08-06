"""
Learning OS -- Seed: Learning Paths (4-Tier Architecture)
=========================================================
Creates LearningPathCategory records (Web, Data & AI, IoT, Cloud) and
assigns every LearningPath to its browse domain + category.

Also seeds PathCourse.role for all existing path_course records.

IDEMPOTENT -- safe to run multiple times.
Run AFTER migration_add_course_type_lp_category.py and seed_course_types.py.

Usage:
    python scripts/seed_learning_paths.py
    python scripts/seed_learning_paths.py --dry-run
"""
import sys
import argparse

ROOT_DIR = r"d:\My Drive\all files\PROJECT FILES\notes"
sys.path.insert(0, ROOT_DIR)

# -- LearningPathCategory seed data --------------------------------------------
LP_CATEGORIES = [
    {
        "name": "Web Development",
        "slug": "web-development",
        "description": "Full stack web development paths covering frontend, backend, and databases.",
        "icon": "🌐",
        "color": "#4f46e5",
        "sort_order": 1,
    },
    {
        "name": "Data & AI",
        "slug": "data-ai",
        "description": "Data science, machine learning, deep learning, and AI engineering paths.",
        "icon": "🤖",
        "color": "#0891b2",
        "sort_order": 2,
    },
    {
        "name": "IoT & Embedded",
        "slug": "iot-embedded",
        "description": "Internet of Things and embedded systems engineering paths.",
        "icon": "⚙️",
        "color": "#059669",
        "sort_order": 3,
    },
    {
        "name": "Cloud & DevOps",
        "slug": "cloud-devops",
        "description": "Cloud computing, DevOps engineering, and infrastructure paths.",
        "icon": "☁️",
        "color": "#d97706",
        "sort_order": 4,
    },
    {
        "name": "QA & Testing",
        "slug": "qa-testing",
        "description": "Software quality assurance and test automation paths.",
        "icon": "🧪",
        "color": "#7c3aed",
        "sort_order": 5,
    },
]

# -- Learning path domain assignments ------------------------------------------
# Key: LearningPath.slug -> (domain, lp_category_slug)
LP_DOMAIN_MAP = {
    "python-full-stack":      ("web",   "web-development"),
    "java-full-stack":        ("web",   "web-development"),
    "dotnet-full-stack":      ("web",   "web-development"),
    "frontend-engineering":   ("web",   "web-development"),
    "backend-engineering":    ("web",   "web-development"),
    "mern-stack":             ("web",   "web-development"),
    "mean-stack":             ("web",   "web-development"),
    "data-science":           ("data",  "data-ai"),
    "ai-engineering":         ("data",  "data-ai"),
    "iot-full-stack":         ("iot",   "iot-embedded"),
    "embedded-systems-path":  ("iot",   "iot-embedded"),
    "devops-engineering":     ("cloud", "cloud-devops"),
    "cloud-engineering":      ("cloud", "cloud-devops"),
    "qa-automation":          ("qa",    "qa-testing"),
}

# -- PathCourse role assignments -----------------------------------------------
# For existing path_courses: determine role from section_label
ROLE_LABEL_MAP = {
    "prerequisite": "prerequisite",
    "foundation":   "prerequisite",
    "core":         "core",
    "main":         "core",
    "backend":      "core",
    "frontend":     "core",
    "database":     "core",
    "framework":    "core",
    "project":      "project",
    "capstone":     "project",
    "elective":     "elective",
    "optional":     "elective",
}


def run(dry_run: bool = False):
    from app import create_app
    from app.core.extensions import db
    from app.domains.learning_path.models import (
        LearningPath, LearningPathCategory, PathCourse
    )

    app = create_app()

    with app.app_context():
        print(f"\n{'='*60}")
        print(f"  Seed: Learning Path Categories {'[DRY RUN]' if dry_run else '[LIVE]'}")
        print(f"{'='*60}\n")

        # -- 1. Seed LearningPathCategory records -------------------------
        category_map = {}  # slug -> LearningPathCategory object
        for cat_data in LP_CATEGORIES:
            existing = LearningPathCategory.query.filter_by(slug=cat_data["slug"]).first()
            if existing:
                category_map[cat_data["slug"]] = existing
                print(f"  EXISTS  LearningPathCategory: {cat_data['name']}")
            else:
                lpc = LearningPathCategory(**cat_data)
                if not dry_run:
                    db.session.add(lpc)
                    db.session.flush()
                category_map[cat_data["slug"]] = lpc
                print(f"  CREATE  LearningPathCategory: {cat_data['name']}")

        if not dry_run:
            db.session.flush()

        # -- 2. Assign domain + category to every LearningPath ------------
        paths = LearningPath.query.all()
        print(f"\n  Learning paths in DB: {len(paths)}")

        for path in paths:
            mapping = LP_DOMAIN_MAP.get(path.slug)
            if mapping:
                domain, cat_slug = mapping
                cat_obj = category_map.get(cat_slug)
                if path.domain != domain:
                    print(f"  UPDATE  path '{path.slug}' -> domain={domain}")
                    if not dry_run:
                        path.domain = domain
                if cat_obj and path.category_id != getattr(cat_obj, "id", None):
                    print(f"  UPDATE  path '{path.slug}' -> category={cat_slug}")
                    if not dry_run and cat_obj.id:
                        path.category_id = cat_obj.id
            else:
                if not path.domain:
                    print(f"  DEFAULT path '{path.slug}' -> domain=web (no mapping)")
                    if not dry_run:
                        path.domain = "web"

        # -- 3. Assign role to existing PathCourse records -----------------
        pc_records = PathCourse.query.all()
        print(f"\n  PathCourse records: {len(pc_records)}")
        role_updated = 0
        for pc in pc_records:
            if pc.role and pc.role != "core":
                continue  # already set
            if pc.section_label:
                label_lower = pc.section_label.lower()
                for key, role in ROLE_LABEL_MAP.items():
                    if key in label_lower:
                        if not dry_run:
                            pc.role = role
                        role_updated += 1
                        break

        print(f"  PathCourse roles updated: {role_updated}")

        if not dry_run:
            db.session.commit()
            print(f"\n  [OK] Committed all changes.\n")
        else:
            print(f"\n  DRY RUN -- no changes committed.\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    run(dry_run=args.dry_run)

