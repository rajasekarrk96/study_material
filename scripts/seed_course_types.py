"""
Learning OS -- Seed: Course Types (4-Tier Architecture)
=======================================================
Classifies all 55 courses in the database into the 4-tier system:
  foundation | specialization | elective

Also seeds the Category.type sub-groups:
  foundation_programming | foundation_frontend | foundation_backend | foundation_core
  specialization | elective

This script is IDEMPOTENT -- safe to run multiple times.
Run AFTER migration_add_course_type_lp_category.py.

Usage:
    python scripts/seed_course_types.py
    python scripts/seed_course_types.py --dry-run
"""
import sys
import argparse

ROOT_DIR = r"d:\My Drive\all files\PROJECT FILES\notes"
sys.path.insert(0, ROOT_DIR)

# -- Course classification data ------------------------------------------------
#
# Key: course slug (matches Course.slug in the database)
# Value: (course_type, sub_category)
#
# sub_category maps to the Category.type that the course's Subject belongs to.
# Used for the Foundations tab sub-group cards.
#
COURSE_TYPE_MAP = {
    # -- Foundations -> Programming -----------------------------------------
    "c-programming":          ("foundation", "foundation_programming"),
    "cpp-programming":        ("foundation", "foundation_programming"),
    "git-version-control":    ("foundation", "foundation_programming"),
    "python-core":            ("foundation", "foundation_programming"),
    "advanced-python":        ("foundation", "foundation_programming"),
    "java-core":              ("foundation", "foundation_programming"),
    "python-dsa":             ("foundation", "foundation_programming"),
    "embedded-c":             ("foundation", "foundation_programming"),
    "python-data-science":    ("foundation", "foundation_programming"),
    "dotnet":                 ("foundation", "foundation_programming"),

    # -- Foundations -> Frontend --------------------------------------------
    "html5":                  ("foundation", "foundation_frontend"),
    "css3":                   ("foundation", "foundation_frontend"),
    "bootstrap":              ("foundation", "foundation_frontend"),
    "javascript-core":        ("foundation", "foundation_frontend"),
    "jquery":                 ("foundation", "foundation_frontend"),
    "react":                  ("foundation", "foundation_frontend"),

    # -- Foundations -> Backend ---------------------------------------------
    "mysql":                  ("foundation", "foundation_backend"),
    "mongodb":                ("foundation", "foundation_backend"),
    "flask":                  ("foundation", "foundation_backend"),
    "fastapi":                ("foundation", "foundation_backend"),
    "rest-api":               ("foundation", "foundation_backend"),
    "auth-jwt":               ("foundation", "foundation_backend"),
    "spring-boot":            ("foundation", "foundation_backend"),
    "database-technologies":  ("foundation", "foundation_backend"),

    # -- Foundations -> Core Engineering -----------------------------------
    "computer-fundamentals":  ("foundation", "foundation_core"),
    "engineering-mathematics":("foundation", "foundation_core"),
    "networking":             ("foundation", "foundation_core"),
    "linux":                  ("foundation", "foundation_core"),
    "docker":                 ("foundation", "foundation_core"),
    "math-statistics":        ("foundation", "foundation_core"),
    "electrical-fundamentals":("foundation", "foundation_core"),
    "electronics-basics":     ("foundation", "foundation_core"),

    # -- Foundations -> Embedded/IoT ---------------------------------------
    "arduino":                ("foundation", "foundation_core"),
    "esp32":                  ("foundation", "foundation_core"),
    "raspberry-pi":           ("foundation", "foundation_core"),
    "sensors-actuators":      ("foundation", "foundation_core"),
    "iot-hardware":           ("foundation", "foundation_core"),
    "iot-projects":           ("foundation", "foundation_core"),

    # -- Specializations ---------------------------------------------------
    "data-analytics":         ("specialization", "specialization"),
    "data-science":           ("specialization", "specialization"),
    "machine-learning":       ("specialization", "specialization"),
    "deep-learning":          ("specialization", "specialization"),
    "computer-vision":        ("specialization", "specialization"),
    "nlp-generative-ai":      ("specialization", "specialization"),
    "mlops":                  ("specialization", "specialization"),
    "devops":                 ("specialization", "specialization"),
    "cloud-computing":        ("specialization", "specialization"),
    "software-testing":       ("specialization", "specialization"),
    "backend-systems":        ("specialization", "specialization"),
    "sql-server":             ("specialization", "specialization"),
    "firebase":               ("specialization", "specialization"),
    "pcb-design":             ("specialization", "specialization"),
    "embedded-systems":       ("specialization", "specialization"),
    "mqtt":                   ("specialization", "specialization"),
    "stm32":                  ("specialization", "specialization"),
    "selenium":               ("specialization", "specialization"),
    "advanced-iot":           ("specialization", "specialization"),
    "computer-vision-iot":    ("specialization", "specialization"),

    # -- Electives ---------------------------------------------------------
    "tinyml":                 ("elective", "elective"),
    "power-bi":               ("elective", "elective"),
    "tableau":                ("elective", "elective"),
    "excel-data-analysis":    ("elective", "elective"),
    "prompt-engineering":     ("elective", "elective"),
    "rag-engineering":        ("elective", "elective"),
    "ai-agents":              ("elective", "elective"),
    "matlab":                 ("elective", "elective"),
    "generative-ai-llms":     ("elective", "elective"),
}


def run(dry_run: bool = False):
    from app import create_app
    from app.core.extensions import db
    from app.domains.content.models import Course, Category, Subject

    app = create_app()

    with app.app_context():
        print(f"\n{'='*60}")
        print(f"  Seed: Course Types {'[DRY RUN]' if dry_run else '[LIVE]'}")
        print(f"{'='*60}\n")

        courses = Course.query.filter_by(is_deleted=False).all()
        print(f"  Total courses in DB: {len(courses)}")

        updated = 0
        skipped = 0
        unmatched = []

        for course in courses:
            # Try exact slug match first
            match = COURSE_TYPE_MAP.get(course.slug)

            # Try partial slug match as fallback
            if not match:
                for map_slug, val in COURSE_TYPE_MAP.items():
                    if map_slug in course.slug or course.slug in map_slug:
                        match = val
                        break

            if match:
                course_type, sub_category = match
                if course.course_type != course_type:
                    print(f"  UPDATE  {course.slug:<45} -> {course_type}")
                    if not dry_run:
                        course.course_type = course_type
                    updated += 1
                else:
                    skipped += 1
            else:
                # Default unmatched to foundation
                unmatched.append(course.slug)
                if course.course_type != "foundation":
                    print(f"  DEFAULT {course.slug:<45} -> foundation (no mapping)")
                    if not dry_run:
                        course.course_type = "foundation"
                    updated += 1
                else:
                    skipped += 1

        if not dry_run:
            db.session.commit()

        print(f"\n  Updated:   {updated}")
        print(f"  Already correct: {skipped}")

        if unmatched:
            print(f"\n  Unmatched slugs ({len(unmatched)}) -- defaulted to 'foundation':")
            for s in unmatched:
                print(f"    {s}")

        # -- Distribution report -------------------------------------------
        if not dry_run:
            from sqlalchemy import func
            dist = db.session.query(
                Course.course_type, func.count(Course.id)
            ).filter_by(is_deleted=False).group_by(Course.course_type).all()
            print(f"\n  Distribution after seed:")
            for ct, cnt in sorted(dist):
                print(f"    {ct:<20} {cnt} courses")

        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    run(dry_run=args.dry_run)

