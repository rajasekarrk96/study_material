"""
migrate_catalog_v3.py
=====================
Learning OS v3.0 — Modular Catalog Architecture Migration

What this script does (SAFE — no deletes, no lesson/progress data touched):
  1. Create 10 new flat skill categories
  2. Move existing subjects to correct new categories
  3. Deactivate old "Full Stack" categories (is_active=False)
  4. Seed 8 Learning Paths with PathCourse references
  5. Add LearningPathCertificate for each path
  6. Sync estimated_hours on each LearningPath
  7. Print full post-migration summary

Run:
  python scripts/migrate_catalog_v3.py
"""
import sys
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

from app import create_app
from app.core.extensions import db
from app.domains.content.models import Category, Subject, Course
from app.domains.learning_path.models import (
    LearningPath, PathCourse, LearningPathCertificate
)

app = create_app()

# ─── New flat categories ──────────────────────────────────────────────────────
NEW_CATEGORIES = [
    dict(name="Programming Languages",  slug="programming-languages",  icon="fas fa-code",           color="#6366f1", sort_order=1,  description="Core programming languages: Python, Java, C, JavaScript and more."),
    dict(name="Frontend Development",   slug="frontend-development",   icon="fas fa-desktop",         color="#0ea5e9", sort_order=2,  description="HTML, CSS, JavaScript frameworks and UI design."),
    dict(name="Backend Development",    slug="backend-development",    icon="fas fa-server",          color="#10b981", sort_order=3,  description="Flask, FastAPI, Django, Node.js, REST APIs and web security."),
    dict(name="Database",               slug="database",               icon="fas fa-database",        color="#f59e0b", sort_order=4,  description="MySQL, PostgreSQL, MongoDB, Redis and database design."),
    dict(name="Git & DevOps",           slug="git-devops",             icon="fab fa-git-alt",         color="#ef4444", sort_order=5,  description="Git, GitHub, Docker, CI/CD, Jenkins, Linux and deployment."),
    dict(name="Testing & QA",           slug="testing-qa",             icon="fas fa-vials",           color="#8b5cf6", sort_order=6,  description="Manual testing, Selenium, Playwright, Postman and performance testing."),
    dict(name="AI & Data Science",      slug="ai-data-science",        icon="fas fa-brain",           color="#ec4899", sort_order=7,  description="Machine Learning, Deep Learning, NLP, Computer Vision, Prompt Engineering and AI Agents."),
    dict(name="IoT & Embedded Systems", slug="iot-embedded-systems",   icon="fas fa-microchip",       color="#14b8a6", sort_order=8,  description="Embedded C, Arduino, ESP32, Raspberry Pi, sensors, MQTT and IoT Cloud."),
    dict(name="Cloud Computing",        slug="cloud-computing",        icon="fas fa-cloud",           color="#64748b", sort_order=9,  description="AWS, Azure, Google Cloud and Firebase."),
    dict(name="Soft Skills",            slug="soft-skills",            icon="fas fa-handshake",       color="#a78bfa", sort_order=10, description="Aptitude, interview prep, resume building and communication skills."),
]

# ─── Subject slug -> new category slug mapping ────────────────────────────────
# key = current subject slug (lowercase), value = new category slug
SUBJECT_REMAP = {
    # Programming Languages
    "python":       "programming-languages",
    "java":         "programming-languages",
    "c":            "programming-languages",
    # Frontend
    "html5":        "frontend-development",
    "css3":         "frontend-development",
    "bootstrap":    "frontend-development",
    "jquery":       "frontend-development",
    "javascript":   "frontend-development",
    # Backend
    "flask":        "backend-development",
    "fastapi":      "backend-development",
    "mongodb":      "database",         # MongoDB is a DB, not backend
    # Database
    "mysql":        "database",
    # Git & DevOps (subjects in Software Engineering & DevOps)
    "git":          "git-devops",
    "jenkins":      "git-devops",
    "linux":        "git-devops",
    "docker":       "git-devops",
    # Testing
    "selenium":     "testing-qa",
    "automation":   "testing-qa",
    # AI & Data Science
    "machine-learning":    "ai-data-science",
    "deep-learning":       "ai-data-science",
    "nlp":                 "ai-data-science",
    "computer-vision":     "ai-data-science",
    "mlops":               "ai-data-science",
    "rag":                 "ai-data-science",
    "ai-agents":           "ai-data-science",
    "prompt-engineering":  "ai-data-science",
    "python-data-science": "ai-data-science",
    "numpy":               "ai-data-science",
    "pandas":              "ai-data-science",
    "matplotlib":          "ai-data-science",
    "genai":               "ai-data-science",
    # IoT
    "arduino":             "iot-embedded-systems",
    "raspberry-pi":        "iot-embedded-systems",
    "iot":                 "iot-embedded-systems",
    "esp32":               "iot-embedded-systems",
    "sensors":             "iot-embedded-systems",
    "mqtt":                "iot-embedded-systems",
    "embedded-c":          "iot-embedded-systems",
    "raspberry-pi-pico":   "iot-embedded-systems",
    "iot-cloud":           "iot-embedded-systems",
    "computer-vision-iot": "iot-embedded-systems",
}

# ─── Old category names to deactivate ────────────────────────────────────────
OLD_CATEGORY_NAMES = [
    "Python Full Stack",
    "Python AI & Data Science",
    "IoT & Hardware Full Stack",
    "Software Engineering & DevOps",
    "Databases & Business Intelligence",
    "Automation & Testing",
    "Databases",
    "Development Tools",
    # NOTE: Do NOT include "Programming Languages" here — it is a new flat category
]

# ─── Learning Paths definition ────────────────────────────────────────────────
# Each entry: (path_slug, course_slug, section_label, sort_order, is_required)
LEARNING_PATHS = [
    {
        "title": "Python Full Stack",
        "slug": "python-full-stack",
        "description": "Master end-to-end web development with Python, Flask, FastAPI, HTML, CSS, JavaScript and MySQL.",
        "target_role": "Python Full Stack Developer",
        "difficulty_level": "beginner",
        "icon": "fab fa-python",
        "color": "#4f46e5",
        "is_featured": True,
        "courses": [
            ("core-python",    "Programming",     1,  True),
            ("html5",          "Frontend",        2,  True),
            ("css3",           "Frontend",        3,  True),
            ("bootstrap",      "Frontend",        4,  True),
            ("javascript",     "Frontend",        5,  True),
            ("jquery",         "Frontend",        6,  False),  # optional
            ("mysql",          "Database",        7,  True),
            ("flask",          "Backend",         8,  True),
            ("fastapi",        "Backend",         9,  False),  # optional
            ("mongodb",        "Database",        10, False),  # optional
            ("git",            "Version Control", 11, True),
        ],
    },
    {
        "title": "Java Full Stack",
        "slug": "java-full-stack",
        "description": "Build full-stack web applications using Core Java, Spring MVC concepts, HTML, CSS, JavaScript and MySQL.",
        "target_role": "Java Full Stack Developer",
        "difficulty_level": "intermediate",
        "icon": "fab fa-java",
        "color": "#f59e0b",
        "is_featured": True,
        "courses": [
            ("core-java",     "Programming",   1,  True),
            ("java",          "Programming",   2,  False),
            ("html5",         "Frontend",      3,  True),
            ("css3",          "Frontend",      4,  True),
            ("bootstrap",     "Frontend",      5,  True),
            ("javascript",    "Frontend",      6,  True),
            ("mysql",         "Database",      7,  True),
        ],
    },
    {
        "title": "IoT Full Stack",
        "slug": "iot-full-stack",
        "description": "Build complete IoT systems with embedded hardware, cloud backends, and web dashboards.",
        "target_role": "IoT Full Stack Engineer",
        "difficulty_level": "intermediate",
        "icon": "fas fa-microchip",
        "color": "#14b8a6",
        "is_featured": True,
        "courses": [
            ("core-python",       "Programming",  1,  True),
            ("c-programming",     "Programming",  2,  True),
            ("html5",             "Frontend",     3,  True),
            ("css3",              "Frontend",     4,  True),
            ("bootstrap",         "Frontend",     5,  True),
            ("javascript",        "Frontend",     6,  True),
            ("flask",             "Backend",      7,  True),
            ("mysql",             "Database",     8,  True),
        ],
    },
    {
        "title": "AI Engineer",
        "slug": "ai-engineer",
        "description": "Build production AI systems: LLMs, RAG pipelines, AI Agents, Prompt Engineering and MLOps.",
        "target_role": "AI Engineer",
        "difficulty_level": "advanced",
        "icon": "fas fa-robot",
        "color": "#ec4899",
        "is_featured": True,
        "courses": [
            ("core-python",   "Programming",      1,  True),
            ("flask",         "Backend",          2,  False),
            ("fastapi",       "Backend",          3,  False),
            ("mysql",         "Database",         4,  False),
        ],
    },
    {
        "title": "Data Scientist",
        "slug": "data-scientist",
        "description": "Master data analysis, visualization, machine learning and deep learning with Python.",
        "target_role": "Data Scientist",
        "difficulty_level": "intermediate",
        "icon": "fas fa-chart-line",
        "color": "#8b5cf6",
        "is_featured": False,
        "courses": [
            ("core-python",   "Programming",     1,  True),
            ("mysql",         "Database",        2,  False),
        ],
    },
    {
        "title": "ML Engineer",
        "slug": "ml-engineer",
        "description": "Design, train, deploy and monitor machine learning models in production.",
        "target_role": "Machine Learning Engineer",
        "difficulty_level": "advanced",
        "icon": "fas fa-brain",
        "color": "#6366f1",
        "is_featured": False,
        "courses": [
            ("core-python",   "Programming",     1,  True),
        ],
    },
    {
        "title": "DevOps Engineer",
        "slug": "devops-engineer",
        "description": "Master CI/CD pipelines, containerisation, Linux administration and cloud deployments.",
        "target_role": "DevOps Engineer",
        "difficulty_level": "intermediate",
        "icon": "fas fa-infinity",
        "color": "#ef4444",
        "is_featured": False,
        "courses": [
            ("core-python",   "Scripting",       1,  False),
        ],
    },
    {
        "title": "QA Automation Engineer",
        "slug": "qa-automation-engineer",
        "description": "Master manual testing, Selenium, Playwright, API testing and CI integration.",
        "target_role": "QA Automation Engineer",
        "difficulty_level": "intermediate",
        "icon": "fas fa-vials",
        "color": "#10b981",
        "is_featured": False,
        "courses": [
            ("core-java",     "Programming",     1,  True),
            ("core-python",   "Programming",     2,  False),
            ("mysql",         "Database",        3,  False),
        ],
    },
]


def get_or_create_category(name, slug, **kwargs):
    cat = Category.query.filter_by(slug=slug).first()
    if not cat:
        cat = Category(name=name, slug=slug, is_active=True, **kwargs)
        db.session.add(cat)
        db.session.flush()
        print(f"  [CREATE] Category '{name}'")
    else:
        # Update fields even if exists
        for k, v in kwargs.items():
            setattr(cat, k, v)
        cat.is_active = True
        print(f"  [EXISTS] Category '{name}' (id={cat.id})")
    return cat


def remap_subjects(cat_map):
    """Move subjects to new categories based on SUBJECT_REMAP."""
    all_subjects = Subject.query.all()
    moved = 0
    for subj in all_subjects:
        slug_key = subj.slug.lower().strip()
        new_cat_slug = SUBJECT_REMAP.get(slug_key)
        if new_cat_slug and new_cat_slug in cat_map:
            new_cat_id = cat_map[new_cat_slug].id
            if subj.category_id != new_cat_id:
                print(f"  [MOVE] Subject '{subj.name}' (slug={subj.slug}) -> '{new_cat_slug}'")
                subj.category_id = new_cat_id
                moved += 1
    return moved


def deactivate_old_categories():
    """Set is_active=False on old stacked categories."""
    deactivated = 0
    for name in OLD_CATEGORY_NAMES:
        cats = Category.query.filter(Category.name.ilike(name)).all()
        for cat in cats:
            if cat.is_active:
                cat.is_active = False
                deactivated += 1
                print(f"  [DEACTIVATE] Category '{cat.name}' (id={cat.id})")
    return deactivated


def seed_learning_paths(cat_map):
    """Seed LearningPath rows and PathCourse join rows."""
    created_paths = 0
    for path_def in LEARNING_PATHS:
        path = LearningPath.query.filter_by(slug=path_def["slug"]).first()
        if not path:
            path = LearningPath(
                title=path_def["title"],
                slug=path_def["slug"],
                description=path_def["description"],
                target_role=path_def["target_role"],
                difficulty_level=path_def["difficulty_level"],
                icon=path_def["icon"],
                color=path_def["color"],
                is_featured=path_def.get("is_featured", False),
                is_active=True,
            )
            db.session.add(path)
            db.session.flush()
            print(f"\n  [CREATE] LearningPath '{path.title}' (id={path.id})")
            created_paths += 1
        else:
            # Update metadata
            path.description      = path_def["description"]
            path.target_role      = path_def["target_role"]
            path.difficulty_level = path_def["difficulty_level"]
            path.icon             = path_def["icon"]
            path.color            = path_def["color"]
            path.is_featured      = path_def.get("is_featured", False)
            path.is_active        = True
            print(f"\n  [UPDATE] LearningPath '{path.title}' (id={path.id})")

        # Remove old PathCourse entries for this path and rebuild
        PathCourse.query.filter_by(path_id=path.id).delete()
        db.session.flush()

        hours_total = 0
        for (course_slug, section_label, sort_order, is_required) in path_def["courses"]:
            course = Course.query.filter_by(slug=course_slug, is_deleted=False).first()
            if not course:
                print(f"    [SKIP] Course slug='{course_slug}' not found in DB")
                continue
            pc = PathCourse(
                path_id=path.id,
                course_id=course.id,
                sort_order=sort_order,
                is_required=is_required,
                section_label=section_label,
            )
            db.session.add(pc)
            hours_total += (course.estimated_hours or 0)
            status = "required" if is_required else "optional"
            print(f"    [ADD] {section_label}: '{course.title}' ({status})")

        path.estimated_hours = hours_total

        # Seed LearningPathCertificate
        cert = LearningPathCertificate.query.filter_by(path_id=path.id).first()
        if not cert:
            cert = LearningPathCertificate(
                path_id=path.id,
                title=f"{path.title} Program Certificate",
                description=f"Awarded upon completing all required courses in the {path.title} learning path."
            )
            db.session.add(cert)
            print(f"    [CERT] Created path certificate")

    return created_paths


def print_summary():
    print("\n" + "="*65)
    print("POST-MIGRATION SUMMARY")
    print("="*65)

    print("\n  ACTIVE CATEGORIES:")
    for cat in Category.query.filter_by(is_active=True).order_by(Category.sort_order).all():
        subj_count   = cat.subjects.count()
        course_count = sum(s.courses.filter_by(is_deleted=False).count() for s in cat.subjects.all())
        print(f"    {cat.name:35s}  subjects={subj_count:2d}  courses={course_count:3d}")

    print("\n  LEARNING PATHS:")
    for lp in LearningPath.query.filter_by(is_active=True).order_by(LearningPath.sort_order).all():
        pc_count = len(lp.courses)
        print(f"    {lp.title:35s}  courses={pc_count:2d}  hours={lp.estimated_hours:3d}h  "
              f"featured={'yes' if lp.is_featured else 'no '}")


with app.app_context():
    print("\n" + "="*65)
    print("LEARNING OS v3.0 — CATALOG MIGRATION")
    print("="*65)

    # Step 1: Create new flat categories
    print("\n[STEP 1] Creating new flat skill categories...")
    cat_map = {}
    for cat_def in NEW_CATEGORIES:
        slug = cat_def.pop("slug")
        name = cat_def.pop("name")
        cat = get_or_create_category(name, slug, **cat_def)
        cat_map[cat.slug] = cat
        cat_def["name"] = name
        cat_def["slug"] = slug
    db.session.flush()

    # Step 2: Remap subjects
    print("\n[STEP 2] Moving subjects to new categories...")
    moved = remap_subjects(cat_map)
    print(f"  Total moved: {moved}")
    db.session.flush()

    # Step 3: Deactivate old categories
    print("\n[STEP 3] Deactivating old stacked categories...")
    deactivated = deactivate_old_categories()
    print(f"  Total deactivated: {deactivated}")
    db.session.flush()

    # Step 4: Seed Learning Paths
    print("\n[STEP 4] Seeding Learning Paths...")
    created = seed_learning_paths(cat_map)
    db.session.flush()

    # Commit everything
    print("\n  Committing all changes...")
    db.session.commit()
    print("  [OK] Migration committed successfully.")

    # Summary
    print_summary()
    print("\nDone. Learning OS v3.0 catalog migration complete.")
