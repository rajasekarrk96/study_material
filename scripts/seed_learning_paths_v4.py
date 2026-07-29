"""
seed_learning_paths_v4.py
=========================
Learning OS — Step 2: Rebuild All 8 Learning Paths (v4.0)

Creates or updates all 8 learning paths and links courses via PathCourse.
Existing paths are updated (not duplicated). PathCourse rows are rebuilt cleanly.

Paths:
  1. python-full-stack       Python Full Stack Developer
  2. java-full-stack         Java Full Stack Developer
  3. iot-full-stack          IoT Full Stack Engineer
  4. ai-engineer             AI Engineer
  5. data-scientist          Data Scientist
  6. ml-engineer             Machine Learning Engineer
  7. devops-engineer         DevOps Engineer
  8. qa-automation           QA Automation Engineer

Usage:
  python scripts/seed_learning_paths_v4.py
  python scripts/seed_learning_paths_v4.py --path python-full-stack
"""
import sys, argparse
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

# Fix Windows console encoding for emoji/unicode output
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from app import create_app
from app.core.extensions import db
from app.domains.content.models import Course
from app.domains.learning_path.models import LearningPath, PathCourse

app = create_app()

# ─── Learning Path Definitions ────────────────────────────────────────────────
# Each course entry: (slug, is_required, section_label)
# is_required: True = Required, False = Optional

PATHS = [

    # ── PATH 1: Python Full Stack Developer ───────────────────────────────────
    {
        "title": "Python Full Stack Developer",
        "slug": "python-full-stack",
        "description": (
            "Master Python full stack development — from core programming and DSA to "
            "HTML/CSS/JS frontend, Flask backend, REST APIs, MySQL, and deployment with Docker. "
            "Build real-world web applications from scratch."
        ),
        "target_role": "Python Full Stack Developer",
        "difficulty_level": "Beginner",
        "estimated_hours": 280,
        "icon": "🐍",
        "color": "#3776AB",
        "courses": [
            ("core-python",        True,  "Programming"),
            ("advanced-python",    True,  "Programming"),
            ("python-dsa",         True,  "Programming"),
            ("git-fundamentals",   True,  "Programming"),
            ("html5",              True,  "Frontend"),
            ("css3",               True,  "Frontend"),
            ("bootstrap",          True,  "Frontend"),
            ("javascript",         True,  "Frontend"),
            ("jquery",             False, "Frontend"),
            ("react",              False, "Frontend"),
            ("mysql",              True,  "Database"),
            ("mongodb",            False, "Database"),
            ("flask",              True,  "Backend"),
            ("rest-api",           True,  "Backend"),
            ("auth-jwt",           True,  "Backend"),
            ("fastapi",            False, "Backend"),
            ("linux",              False, "Deployment"),
            ("docker",             False, "Deployment"),
        ],
    },

    # ── PATH 2: Java Full Stack Developer ─────────────────────────────────────
    {
        "title": "Java Full Stack Developer",
        "slug": "java-full-stack",
        "description": (
            "Build enterprise-grade Java applications — Core Java, Spring Boot, Spring MVC, "
            "Spring Security, Hibernate, REST APIs, and MySQL/MongoDB, with optional React frontend."
        ),
        "target_role": "Java Full Stack Developer",
        "difficulty_level": "Beginner",
        "estimated_hours": 350,
        "icon": "☕",
        "color": "#5382A1",
        "courses": [
            ("core-java",          True,  "Programming"),
            ("java",               True,  "Programming"),
            ("git-fundamentals",   True,  "Programming"),
            ("html5",              True,  "Frontend"),
            ("css3",               True,  "Frontend"),
            ("bootstrap",          True,  "Frontend"),
            ("javascript",         True,  "Frontend"),
            ("react",              False, "Frontend"),
            ("mysql",              True,  "Database"),
            ("mongodb",            False, "Database"),
            ("servlet-jsp",        True,  "Backend"),
            ("spring",             True,  "Backend"),
            ("spring-boot",        True,  "Backend"),
            ("spring-mvc",         True,  "Backend"),
            ("spring-security",    True,  "Backend"),
            ("maven",              True,  "Build"),
            ("docker",             False, "Deployment"),
        ],
    },

    # ── PATH 3: IoT Full Stack Engineer ───────────────────────────────────────
    {
        "title": "IoT Full Stack Engineer",
        "slug": "iot-full-stack",
        "description": (
            "End-to-end IoT engineering — C, Embedded C, Arduino, ESP32, sensors, "
            "MQTT, Flask backend, and real-time web dashboards. Build production IoT systems "
            "from hardware to cloud."
        ),
        "target_role": "IoT Full Stack Engineer",
        "difficulty_level": "Beginner",
        "estimated_hours": 380,
        "icon": "🔌",
        "color": "#00B4D8",
        "courses": [
            ("c-programming",             True,  "Programming"),
            ("embedded-c",                True,  "Programming"),
            ("core-python",               True,  "Programming"),
            ("git-fundamentals",          True,  "Programming"),
            ("electrical-fundamentals",   True,  "Electronics"),
            ("electronics-basics",        True,  "Electronics"),
            ("pcb",                       False, "Electronics"),
            ("arduino",                   True,  "Hardware"),
            ("esp32",                     True,  "Hardware"),
            ("sensors-actuators",         True,  "Hardware"),
            ("iot-hardware",              True,  "Hardware"),
            ("stm32",                     False, "Hardware"),
            ("raspberry-pi",              False, "Hardware"),
            ("html5",                     True,  "Web Stack"),
            ("css3",                      True,  "Web Stack"),
            ("bootstrap",                 True,  "Web Stack"),
            ("javascript",                True,  "Web Stack"),
            ("mysql",                     True,  "Web Stack"),
            ("flask",                     True,  "Web Stack"),
            ("mqtt",                      True,  "Connectivity"),
            ("firebase",                  False, "Connectivity"),
            ("computer-vision",           False, "AI for IoT"),
            ("tinyml",                    False, "AI for IoT"),
        ],
    },

    # ── PATH 4: AI Engineer ───────────────────────────────────────────────────
    {
        "title": "AI Engineer",
        "slug": "ai-engineer",
        "description": (
            "Master the complete AI engineering stack — Python, mathematics, machine learning, "
            "deep learning, computer vision, NLP, generative AI, RAG, AI agents, and MLOps. "
            "Build and deploy production AI systems."
        ),
        "target_role": "AI Engineer",
        "difficulty_level": "Intermediate",
        "estimated_hours": 420,
        "icon": "🤖",
        "color": "#7B2FBE",
        "courses": [
            ("core-python",          True,  "Programming"),
            ("git-fundamentals",     True,  "Programming"),
            ("ds-math",              True,  "Mathematics"),
            ("python-data-science",  True,  "Data Science"),
            ("mysql",                True,  "Data Science"),
            ("machine-learning",     True,  "Machine Learning"),
            ("deep-learning",        True,  "Machine Learning"),
            ("computer-vision",      True,  "AI"),
            ("nlp",                  True,  "AI"),
            ("generative-ai-llms",   True,  "AI"),
            ("prompt-engineering",   True,  "AI"),
            ("rag-engineering",      True,  "AI"),
            ("ai-agents",            True,  "AI"),
            ("fastapi",              True,  "Deployment"),
            ("mlops-ai-deployment",  True,  "Deployment"),
            ("docker",               False, "Deployment"),
        ],
    },

    # ── PATH 5: Data Scientist ────────────────────────────────────────────────
    {
        "title": "Data Scientist",
        "slug": "data-scientist",
        "description": (
            "Learn data science from scratch — Python, statistics, NumPy, Pandas, "
            "data visualization, machine learning, and Power BI. "
            "Extract insights and build predictive models from real-world datasets."
        ),
        "target_role": "Data Scientist",
        "difficulty_level": "Beginner",
        "estimated_hours": 250,
        "icon": "📊",
        "color": "#E07A5F",
        "courses": [
            ("core-python",          True,  "Programming"),
            ("git-fundamentals",     True,  "Programming"),
            ("mysql",                True,  "Database"),
            ("ds-math",              True,  "Mathematics"),
            ("python-data-science",  True,  "Data Science"),
            ("power-bi",             True,  "Visualization"),
            ("machine-learning",     True,  "Machine Learning"),
            ("deep-learning",        False, "Machine Learning"),
        ],
    },

    # ── PATH 6: Machine Learning Engineer ─────────────────────────────────────
    {
        "title": "Machine Learning Engineer",
        "slug": "ml-engineer",
        "description": (
            "Build and deploy production ML systems — Python, mathematics, machine learning, "
            "deep learning, FastAPI, MLOps, and Docker. Go from model training to scalable API."
        ),
        "target_role": "Machine Learning Engineer",
        "difficulty_level": "Intermediate",
        "estimated_hours": 300,
        "icon": "⚙️",
        "color": "#F4A261",
        "courses": [
            ("core-python",          True, "Programming"),
            ("git-fundamentals",     True, "Programming"),
            ("ds-math",              True, "Mathematics"),
            ("python-data-science",  True, "Data Science"),
            ("machine-learning",     True, "Machine Learning"),
            ("deep-learning",        True, "Machine Learning"),
            ("fastapi",              True, "Deployment"),
            ("mlops-ai-deployment",  True, "Deployment"),
            ("docker",               True, "Deployment"),
        ],
    },

    # ── PATH 7: DevOps Engineer ───────────────────────────────────────────────
    {
        "title": "DevOps Engineer",
        "slug": "devops-engineer",
        "description": (
            "Master DevOps — Linux, Bash, Docker, CI/CD with GitHub Actions and Jenkins, "
            "AWS cloud, and Kubernetes orchestration. "
            "Automate the entire software delivery pipeline."
        ),
        "target_role": "DevOps Engineer",
        "difficulty_level": "Intermediate",
        "estimated_hours": 280,
        "icon": "🚀",
        "color": "#2EC4B6",
        "courses": [
            ("core-python",       True, "Programming"),
            ("bash",              True, "Programming"),
            ("git-fundamentals",  True, "Programming"),
            ("linux",             True, "Operating System"),
            ("docker",            True, "Containers"),
            ("github-actions",    True, "CI/CD"),
            ("jenkins",           True, "CI/CD"),
            ("aws",               True, "Cloud"),
            ("kubernetes",        True, "Orchestration"),
        ],
    },

    # ── PATH 8: QA Automation Engineer ────────────────────────────────────────
    {
        "title": "QA Automation Engineer",
        "slug": "qa-automation",
        "description": (
            "Become a QA automation expert — manual testing fundamentals, Selenium (Java & Python), "
            "Playwright, Postman API testing, Maven, Jenkins CI/CD, and building reusable "
            "test frameworks."
        ),
        "target_role": "QA Automation Engineer",
        "difficulty_level": "Beginner",
        "estimated_hours": 230,
        "icon": "🧪",
        "color": "#06D6A0",
        "courses": [
            ("core-java",         True,  "Programming"),
            ("core-python",       True,  "Programming"),
            ("git-fundamentals",  True,  "Programming"),
            ("manual-testing",    True,  "Testing"),
            ("java-selenium",     True,  "Automation"),
            ("selenium",          False, "Automation"),
            ("playwright",        True,  "Automation"),
            ("postman",           True,  "API Testing"),
            ("mysql",             True,  "Database"),
            ("maven",             True,  "Build"),
            ("jenkins",           True,  "CI/CD"),
        ],
    },
]


def upsert_path(spec: dict, dry_run: bool = False) -> bool:
    """Create or update a LearningPath and its PathCourse entries."""
    slug = spec["slug"]

    path = LearningPath.query.filter_by(slug=slug).first()
    if not path:
        if dry_run:
            print(f"  [DRY] Would create path: {slug}")
        else:
            path = LearningPath(
                title=spec["title"],
                slug=slug,
                description=spec["description"],
                target_role=spec["target_role"],
                difficulty_level=spec["difficulty_level"],
                estimated_hours=spec["estimated_hours"],
                icon=spec.get("icon", ""),
                color=spec.get("color", "#333"),
                is_active=True,
                is_featured=True,
                sort_order=PATHS.index(spec) + 1,
            )
            db.session.add(path)
            db.session.flush()
            print(f"  [PATH+] {slug} — '{spec['title']}'")
    else:
        if not dry_run:
            path.title = spec["title"]
            path.description = spec["description"]
            path.target_role = spec["target_role"]
            path.difficulty_level = spec["difficulty_level"]
            path.estimated_hours = spec["estimated_hours"]
            path.icon = spec.get("icon", "")
            path.color = spec.get("color", "#333")
            path.is_active = True
            print(f"  [PATH=] {slug} — updated")

    if dry_run:
        for (course_slug, is_req, section) in spec["courses"]:
            c = Course.query.filter_by(slug=course_slug, is_deleted=False).first()
            status = "OK" if c else "MISSING"
            req = "Required" if is_req else "Optional"
            print(f"    [{status:7s}] [{req:8s}] {section:20s} {course_slug}")
        return True

    # Rebuild PathCourse entries for this path
    PathCourse.query.filter_by(path_id=path.id).delete()
    db.session.flush()

    missing = []
    for sort_idx, (course_slug, is_required, section_label) in enumerate(spec["courses"], start=1):
        course = Course.query.filter_by(slug=course_slug, is_deleted=False).first()
        if not course:
            missing.append(course_slug)
            print(f"    [WARN] Course not found: {course_slug} — skipping")
            continue

        pc = PathCourse(
            path_id=path.id,
            course_id=course.id,
            sort_order=sort_idx,
            is_required=is_required,
            section_label=section_label,
        )
        db.session.add(pc)

    req_count = sum(1 for (_, r, _) in spec["courses"] if r)
    opt_count = sum(1 for (_, r, _) in spec["courses"] if not r)
    print(f"    Linked: {len(spec['courses']) - len(missing)} courses "
          f"({req_count} required, {opt_count} optional) | Missing: {len(missing)}")
    return len(missing) == 0


def seed_paths(path_filter=None, dry_run=False):
    paths = (
        [p for p in PATHS if p["slug"] == path_filter]
        if path_filter else PATHS
    )
    if path_filter and not paths:
        print(f"Path not found: {path_filter}")
        return

    with app.app_context():
        print(f"\n{'='*65}")
        print(f"Learning OS — Seeding {len(paths)} Learning Path(s)")
        if dry_run:
            print("  [DRY RUN — no DB writes]")
        print(f"{'='*65}\n")

        for spec in paths:
            print(f"\n[{spec['icon']}] {spec['title']} ({spec['slug']})")
            print(f"   Role: {spec['target_role']} | "
                  f"Level: {spec['difficulty_level']} | "
                  f"Hours: {spec['estimated_hours']}h")
            upsert_path(spec, dry_run=dry_run)

        if not dry_run:
            db.session.commit()

        print(f"\n{'='*65}")
        print(f"DONE. {len(paths)} path(s) seeded successfully.")
        print(f"{'='*65}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Seed Learning OS v4.0 Learning Paths")
    parser.add_argument("--path", help="Seed only this path slug")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview without writing to DB")
    args = parser.parse_args()
    seed_paths(path_filter=args.path, dry_run=args.dry_run)
