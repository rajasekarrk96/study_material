"""
seed_master_catalog.py
======================
Learning OS — Step 1: Create 27 Missing Stub Courses

Creates all missing courses in the catalog with proper metadata.
Status = 'coming_soon'. Zero modules/lessons.
Idempotent — skips courses that already exist by slug.

Usage:
  python scripts/seed_master_catalog.py
  python scripts/seed_master_catalog.py --dry-run   (preview only)
"""
import sys, argparse
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

from app import create_app
from app.core.extensions import db
from app.domains.content.models import Course

app = create_app()

# ─── 27 Missing Stub Courses ──────────────────────────────────────────────────
# Format: (title, slug, difficulty_level, estimated_hours, description)

MISSING_COURSES = [

    # ── Priority 1: Used by 2+ paths ─────────────────────────────────────────
    (
        "Advanced Python",
        "advanced-python",
        "Intermediate",
        30,
        "Deep-dive into Python: decorators, generators, async/await, metaclasses, "
        "design patterns, memory management, and building production-grade Python packages.",
    ),
    (
        "Docker",
        "docker",
        "Intermediate",
        20,
        "Containerize applications with Docker — images, containers, Dockerfile, "
        "Docker Compose, volumes, networking, and deploying containerized services.",
    ),
    (
        "Linux Administration",
        "linux",
        "Beginner",
        25,
        "Master the Linux command line — file system, permissions, processes, shell scripting, "
        "package management, networking, and system administration fundamentals.",
    ),
    (
        "React.js",
        "react",
        "Intermediate",
        35,
        "Build modern single-page applications with React — components, hooks, state management, "
        "React Router, Context API, and integrating with REST APIs.",
    ),
    (
        "REST API Development",
        "rest-api",
        "Intermediate",
        15,
        "Design and build professional REST APIs — HTTP methods, status codes, versioning, "
        "pagination, error handling, documentation with Swagger/OpenAPI.",
    ),
    (
        "Authentication & JWT",
        "auth-jwt",
        "Intermediate",
        15,
        "Implement secure authentication — JWT tokens, refresh tokens, OAuth2 flows, "
        "session management, role-based access control, and security best practices.",
    ),

    # ── Priority 2: Java Full Stack ───────────────────────────────────────────
    (
        "Servlet & JSP",
        "servlet-jsp",
        "Intermediate",
        20,
        "Java web fundamentals — HTTP Servlets, JSP templating, JSTL, session management, "
        "MVC pattern in plain Java, and deploying on Apache Tomcat.",
    ),
    (
        "Spring Framework",
        "spring",
        "Intermediate",
        25,
        "Core Spring — IoC container, dependency injection, AOP, Spring JDBC, "
        "transaction management, and Spring MVC fundamentals.",
    ),
    (
        "Spring MVC",
        "spring-mvc",
        "Intermediate",
        20,
        "Build web applications with Spring MVC — DispatcherServlet, controllers, "
        "view resolvers, form handling, validation, and Thymeleaf templating.",
    ),
    (
        "Spring Security",
        "spring-security",
        "Advanced",
        20,
        "Secure Spring Boot applications — authentication, authorization, JWT integration, "
        "OAuth2, method-level security, and CSRF protection.",
    ),
    (
        "Maven",
        "maven",
        "Beginner",
        10,
        "Java build automation with Maven — POM structure, dependency management, "
        "lifecycle phases, plugins, multi-module projects, and publishing artifacts.",
    ),

    # ── Priority 3: IoT ───────────────────────────────────────────────────────
    (
        "Electrical Fundamentals",
        "electrical-fundamentals",
        "Beginner",
        20,
        "Essential electrical theory for IoT engineers — Ohm's law, Kirchhoff's laws, "
        "AC/DC circuits, capacitors, inductors, power calculations, and circuit analysis.",
    ),
    (
        "Electronics Basics",
        "electronics-basics",
        "Beginner",
        25,
        "Core electronics for embedded systems — diodes, transistors, op-amps, "
        "logic gates, voltage regulators, breadboard prototyping, and reading datasheets.",
    ),
    (
        "STM32",
        "stm32",
        "Advanced",
        35,
        "Professional embedded development with STM32 — STM32CubeIDE, HAL library, "
        "GPIO, UART, SPI, I2C, timers, DMA, FreeRTOS, and low-power design.",
    ),
    (
        "Firebase",
        "firebase",
        "Beginner",
        15,
        "Build real-time IoT dashboards with Firebase — Realtime Database, Firestore, "
        "Authentication, Cloud Functions, and hosting for IoT web dashboards.",
    ),
    (
        "TinyML",
        "tinyml",
        "Advanced",
        25,
        "Deploy machine learning on microcontrollers — TensorFlow Lite, Edge Impulse, "
        "model optimization, quantization, and running inference on Arduino and ESP32.",
    ),

    # ── Priority 4: DevOps ────────────────────────────────────────────────────
    (
        "Bash Scripting",
        "bash",
        "Beginner",
        15,
        "Automate system tasks with Bash — variables, loops, conditionals, functions, "
        "file I/O, text processing with awk/sed/grep, and cron job scheduling.",
    ),
    (
        "GitHub Actions",
        "github-actions",
        "Intermediate",
        15,
        "CI/CD with GitHub Actions — workflows, triggers, jobs, steps, secrets, "
        "matrix builds, reusable workflows, and deploying to cloud platforms.",
    ),
    (
        "Jenkins",
        "jenkins",
        "Intermediate",
        20,
        "Enterprise CI/CD with Jenkins — pipeline as code, Jenkinsfile, stages, "
        "agents, plugins, integration with Git, Docker, and cloud deployments.",
    ),
    (
        "AWS",
        "aws",
        "Intermediate",
        35,
        "Amazon Web Services core services — EC2, S3, RDS, Lambda, API Gateway, "
        "IAM, VPC, CloudWatch, and deploying full-stack applications on AWS.",
    ),
    (
        "Kubernetes",
        "kubernetes",
        "Advanced",
        30,
        "Container orchestration with Kubernetes — pods, deployments, services, "
        "ingress, ConfigMaps, secrets, scaling, Helm charts, and managed clusters.",
    ),

    # ── Priority 5: QA & Others ───────────────────────────────────────────────
    (
        "Manual Testing",
        "manual-testing",
        "Beginner",
        15,
        "Software QA fundamentals — SDLC, STLC, test planning, test case design, "
        "bug lifecycle, functional/non-functional testing, and JIRA workflow.",
    ),
    (
        "Playwright",
        "playwright",
        "Intermediate",
        20,
        "Modern end-to-end testing with Playwright — browser automation, page objects, "
        "fixtures, API testing, visual regression, and CI/CD integration.",
    ),
    (
        "Postman / API Testing",
        "postman",
        "Beginner",
        15,
        "API testing with Postman — collections, environments, variables, pre-request scripts, "
        "assertions, Newman CLI, and automated API testing workflows.",
    ),
    (
        "Data Structures & Algorithms",
        "python-dsa",
        "Intermediate",
        30,
        "Core DSA in Python — arrays, linked lists, stacks, queues, trees, graphs, "
        "sorting, searching, dynamic programming, and time/space complexity analysis.",
    ),
]


def get_subject_id():
    """Get a default subject_id from any existing course, or None."""
    existing = Course.query.filter(Course.subject_id.isnot(None)).first()
    return existing.subject_id if existing else None


def seed_catalog(dry_run: bool = False):
    with app.app_context():
        default_subject_id = get_subject_id()
        print(f"Default subject_id: {default_subject_id}")

        created = 0
        skipped = 0

        for (title, slug, difficulty, hours, desc) in MISSING_COURSES:
            existing = Course.query.filter_by(slug=slug, is_deleted=False).first()
            if existing:
                print(f"  [SKIP]  {slug:40s} already exists (lessons={sum(m.lessons.filter_by(is_deleted=False).count() for m in existing.modules.all())})")
                skipped += 1
                continue

            if dry_run:
                print(f"  [DRY]   {slug:40s} would create: '{title}'")
                created += 1
                continue

            course = Course(
                subject_id=default_subject_id,
                created_by=1,
                title=title,
                slug=slug,
                description=desc,
                long_description=desc,
                difficulty_level=difficulty,
                status='coming_soon',
                language='English',
                estimated_hours=hours,
                is_free=True,
                is_featured=False,
                is_deleted=False,
            )
            db.session.add(course)
            db.session.flush()
            print(f"  [ADD]   {slug:40s} '{title}' ({difficulty}, {hours}h)")
            created += 1

        if not dry_run:
            db.session.commit()

        print(f"\n{'[DRY RUN] ' if dry_run else ''}Done.")
        print(f"  Created: {created} | Skipped: {skipped}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Seed missing catalog stub courses")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing to DB")
    args = parser.parse_args()
    seed_catalog(dry_run=args.dry_run)
