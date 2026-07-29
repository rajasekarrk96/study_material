"""
setup_iot_fullstack_v3.py
=========================
Rebuilds the IoT Full Stack learning path with the correct 20-course sequence:
Phase 1: C Basics → Embedded C → Python → MATLAB → Simulation
Phase 2: HTML5 → CSS3 → Bootstrap → JavaScript → MySQL → Flask
Phase 3: Arduino → ESP32 → Raspberry Pi → Sensors → Advanced Components
Phase 4: MQTT → IoT Cloud
Phase 5: Basic ML for IoT → Computer Vision IoT
"""
import sys
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')
from app import create_app
from app.core.extensions import db
from app.domains.content.models import Category, Subject, Course
from app.domains.learning_path.models import LearningPath, PathCourse

app = create_app()

# ─── Stub course definitions ──────────────────────────────────────────────────
# (name, slug, description, hours, difficulty, category_slug, subject_slug)
STUB_COURSES = [
    (
        "Embedded C",
        "embedded-c",
        "Program microcontrollers using C — memory management, pointers, peripherals, interrupts, timers and register-level programming.",
        25, "intermediate", "iot-embedded-systems", "embedded-c"
    ),
    (
        "Basic MATLAB",
        "basic-matlab",
        "Introduction to MATLAB for engineers — matrix operations, signal processing, data visualization, and algorithm prototyping.",
        20, "beginner", "iot-embedded-systems", "matlab"
    ),
    (
        "Simulation (Proteus / Wokwi)",
        "simulation",
        "Design and simulate electronic circuits virtually using Proteus and Wokwi before building on real hardware.",
        15, "beginner", "iot-embedded-systems", "simulation"
    ),
    (
        "Arduino",
        "arduino",
        "Get started with Arduino — GPIO, sensors, actuators, PWM, serial communication, I2C, SPI and real-world projects.",
        25, "beginner", "iot-embedded-systems", "arduino"
    ),
    (
        "ESP32",
        "esp32",
        "Build WiFi and BLE IoT devices with ESP32 — wireless communication, deep sleep, OTA updates and cloud connectivity.",
        25, "intermediate", "iot-embedded-systems", "esp32"
    ),
    (
        "Raspberry Pi",
        "raspberry-pi",
        "Use Raspberry Pi as a Linux-based IoT gateway — GPIO, camera, networking, Docker and remote access.",
        20, "intermediate", "iot-embedded-systems", "raspberry-pi"
    ),
    (
        "Sensors & Actuators",
        "sensors-actuators",
        "Interface real-world sensors (temperature, humidity, motion, ultrasonic, gas) and actuators (LEDs, buzzers, motors) with microcontrollers.",
        20, "beginner", "iot-embedded-systems", "sensors"
    ),
    (
        "Advanced Components",
        "advanced-components",
        "Work with advanced IoT components — servo motors, stepper motors, OLED/LCD displays, relay modules and power management.",
        20, "intermediate", "iot-embedded-systems", "advanced-components"
    ),
    (
        "MQTT Protocol",
        "mqtt",
        "Implement lightweight IoT messaging with MQTT — broker setup, publish/subscribe, QoS levels, and integration with Node-RED and cloud.",
        15, "intermediate", "iot-embedded-systems", "mqtt"
    ),
    (
        "IoT Cloud",
        "iot-cloud",
        "Connect IoT devices to the cloud — AWS IoT Core, MQTT dashboards, time-series databases, alerts and remote monitoring.",
        20, "intermediate", "cloud-computing", "iot-cloud"
    ),
    (
        "Basic ML for IoT",
        "basic-ml-iot",
        "Deploy machine learning at the edge — TensorFlow Lite, model quantization, anomaly detection on microcontrollers.",
        20, "advanced", "ai-data-science", "machine-learning"
    ),
    (
        "Computer Vision for IoT",
        "computer-vision-iot",
        "Add vision intelligence to IoT — OpenCV on Raspberry Pi, object detection with YOLO, face recognition and edge inference.",
        20, "advanced", "iot-embedded-systems", "computer-vision-iot"
    ),
]

# ─── Final ordered path: (course_slug, section_label, sort_order, is_required)
IOT_PATH_COURSES = [
    # Phase 1 — Programming Foundations
    ("c-programming",         "Programming",    1,  True),
    ("embedded-c",            "Programming",    2,  True),
    ("core-python",           "Programming",    3,  True),
    ("basic-matlab",          "Programming",    4,  False),
    ("simulation",            "Programming",    5,  False),
    # Phase 2 — Web Stack
    ("html5",                 "Web Stack",      6,  True),
    ("css3",                  "Web Stack",      7,  True),
    ("bootstrap",             "Web Stack",      8,  True),
    ("javascript",            "Web Stack",      9,  True),
    ("mysql",                 "Web Stack",      10, True),
    ("flask",                 "Web Stack",      11, True),
    # Phase 3 — Hardware
    ("arduino",               "Hardware",       12, True),
    ("esp32",                 "Hardware",       13, True),
    ("raspberry-pi",          "Hardware",       14, False),
    ("sensors-actuators",     "Hardware",       15, True),
    ("advanced-components",   "Hardware",       16, False),
    # Phase 4 — Connectivity
    ("mqtt",                  "Connectivity",   17, True),
    ("iot-cloud",             "Connectivity",   18, False),
    # Phase 5 — Intelligence
    ("basic-ml-iot",          "Intelligence",   19, False),
    ("computer-vision-iot",   "Intelligence",   20, False),
]


def get_or_create_subject(name, slug, cat_slug):
    cat = Category.query.filter_by(slug=cat_slug).first()
    if not cat:
        print(f"  [WARN] Category '{cat_slug}' not found, skipping subject '{name}'")
        return None
    subj = Subject.query.filter_by(slug=slug).first()
    if not subj:
        subj = Subject(name=name, slug=slug, category_id=cat.id,
                       description=f"{name} subject")
        db.session.add(subj)
        db.session.flush()
    return subj


def get_or_create_stub_course(name, slug, desc, hours, diff, cat_slug, subj_slug):
    course = Course.query.filter_by(slug=slug, is_deleted=False).first()
    if course:
        print(f"  [EXISTS] {name} (id={course.id})")
        return course

    subj = get_or_create_subject(name, subj_slug, cat_slug)
    if not subj:
        return None

    course = Course(
        subject_id=subject_id if (subject_id := subj.id) else None,
        title=name,
        slug=slug,
        description=desc,
        difficulty_level=diff,
        status='published',
        is_deleted=False,
        estimated_hours=hours,
        is_featured=False,
    )
    db.session.add(course)
    db.session.flush()
    print(f"  [CREATE] {name} (id={course.id}, {hours}h)")
    return course


with app.app_context():
    print("\n" + "="*65)
    print("IoT Full Stack v3 — Path Rebuild")
    print("="*65)

    # Step 1: Create all stub courses
    print("\n[STEP 1] Creating stub courses...")
    for (name, slug, desc, hours, diff, cat_slug, subj_slug) in STUB_COURSES:
        get_or_create_stub_course(name, slug, desc, hours, diff, cat_slug, subj_slug)
    db.session.flush()

    # Step 2: Rebuild path
    print("\n[STEP 2] Rebuilding IoT Full Stack path...")
    path = LearningPath.query.filter_by(slug='iot-full-stack').first()
    if not path:
        print("  [ERROR] IoT Full Stack path not found!")
        exit(1)

    # Delete existing PathCourse entries
    old_count = PathCourse.query.filter_by(path_id=path.id).delete()
    db.session.flush()
    print(f"  Cleared {old_count} old course entries")

    # Add new ordered entries
    total_hours = 0
    skipped = []
    for (slug, section, sort, required) in IOT_PATH_COURSES:
        course = Course.query.filter_by(slug=slug, is_deleted=False).first()
        if not course:
            print(f"  [SKIP] slug='{slug}' not found")
            skipped.append(slug)
            continue
        pc = PathCourse(
            path_id=path.id,
            course_id=course.id,
            sort_order=sort,
            is_required=required,
            section_label=section,
        )
        db.session.add(pc)
        total_hours += (course.estimated_hours or 0)
        req_label = "required" if required else "optional"
        print(f"  [{sort:2d}] [{section:14s}] {course.title:35s} ({req_label})")

    path.estimated_hours = total_hours
    path.description = (
        "A complete IoT engineering program: C → Embedded C → Python → MATLAB → "
        "Web Stack → Arduino → ESP32 → Sensors → MQTT → IoT Cloud → Edge ML."
    )

    db.session.commit()
    print(f"\n  [OK] Committed. Total estimated_hours={total_hours}h")
    if skipped:
        print(f"  [WARN] Skipped slugs: {skipped}")

    print("\n" + "="*65)
    print(f"FINAL IoT Full Stack — {len(path.courses)} courses, {path.estimated_hours}h")
    print("="*65)
    for pc in path.courses:
        req = "✅" if pc.is_required else "🔵"
        print(f"  {req} [{pc.section_label:14s}] {pc.course.title}")
