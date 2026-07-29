"""
fix_course_estimated_hours.py
==============================
Fixes 0h / NULL estimated_hours across all 74 courses in the master catalog.
Uses short per-course transactions to avoid database lock timeouts.
"""
import sys
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

from app import create_app
from app.core.extensions import db
from app.domains.content.models import Course, Module, Lesson

app = create_app()

COURSE_HOURS_MAP = {
    "c-programming": 10,
    "embedded-c": 24,
    "core-python": 15,
    "git-fundamentals": 12,
    "electrical-fundamentals": 8,
    "electronics-basics": 10,
    "pcb": 12,
    "arduino": 18,
    "esp32": 24,
    "sensors-actuators": 15,
    "iot-hardware": 25,
    "stm32": 18,
    "raspberry-pi": 12,
    "html5": 8,
    "css3": 12,
    "bootstrap": 8,
    "javascript": 18,
    "mysql": 18,
    "flask": 12,
    "mqtt": 10,
    "firebase": 8,
    "computer-vision": 25,
    "tinyml": 10,
    "advanced-python": 15,
    "python-dsa": 16,
    "react": 18,
    "rest-api": 8,
    "auth-jwt": 8,
    "fastapi": 14,
    "linux": 15,
    "docker": 15,
    "core-java": 35,
    "java": 12,
    "servlet-jsp": 8,
    "spring": 10,
    "spring-boot": 15,
    "spring-mvc": 10,
    "spring-security": 10,
    "maven": 6,
    "machine-learning": 35,
    "deep-learning": 30,
    "nlp": 24,
    "generative-ai-llms": 25,
    "prompt-engineering": 10,
    "rag-engineering": 20,
    "ai-agents": 20,
    "mlops-ai-deployment": 20,
    "power-bi": 15,
    "ds-math": 8,
    "python-data-science": 6,
    "aws": 20,
    "kubernetes": 16,
    "jenkins": 10,
    "github-actions": 8,
    "bash": 8,
    "manual-testing": 8,
    "java-selenium": 15,
    "selenium": 12,
    "playwright": 10,
    "postman": 8,
}

def fix_hours():
    with app.app_context():
        courses = Course.query.filter_by(is_deleted=False).all()
        updated = 0
        for c in courses:
            target_h = COURSE_HOURS_MAP.get(c.slug)
            if not target_h:
                # Calculate from lesson count (approx 20 mins per lesson)
                mods = c.modules.all()
                tot_l = sum(m.lessons.filter_by(is_deleted=False).count() for m in mods)
                target_h = max(2, round(tot_l * 20 / 60))

            if c.estimated_hours != target_h:
                print(f"Updating {c.slug:30s}: {c.estimated_hours}h -> {target_h}h")
                c.estimated_hours = target_h
                db.session.commit()
                updated += 1

            # Also update estimated_minutes on individual lessons if 0
            for m in c.modules.all():
                for l in m.lessons.filter_by(is_deleted=False).all():
                    if not l.estimated_minutes or l.estimated_minutes == 0:
                        l.estimated_minutes = 20
                db.session.commit()

        print(f"\n========================================================")
        print(f"SUCCESS: Updated estimated hours for {updated} courses!")
        print(f"========================================================")

if __name__ == "__main__":
    fix_hours()
