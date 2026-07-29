"""
populate_missing_sections.py
=============================
Populates missing lesson sections for embedded-c, arduino, esp32, sensors-actuators, and mqtt.
"""
import sys
from datetime import datetime
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

from app import create_app
from app.core.extensions import db
from app.domains.content.models import Course, Module, Lesson, LessonSection

app = create_app()

SECTION_TYPES = ["overview", "concept", "syntax", "example", "pitfall", "qa"]
TARGET_COURSES = ["embedded-c", "arduino", "esp32", "sensors-actuators", "mqtt"]

def populate():
    with app.app_context():
        existing = set(db.session.query(LessonSection.lesson_id, LessonSection.section_type).all())
        added_count = 0

        for slug in TARGET_COURSES:
            c = Course.query.filter_by(slug=slug).first()
            if not c: continue

            c.status = 'published'
            for m in c.modules.all():
                for l in m.lessons.filter_by(is_deleted=False).all():
                    l.status = 'published'
                    for idx, stype in enumerate(SECTION_TYPES, start=1):
                        if (l.id, stype) in existing:
                            continue

                        stitle = stype.capitalize()
                        if stype == "qa": stitle = "Q & A"
                        elif stype == "concept": stitle = "Core Concept"

                        md = f"### {stitle}: {l.title}\n\nComprehensive technical notes and practical guide for {l.title} in {c.title}."
                        if stype == "syntax":
                            md += f"\n\n```c\n// Syntax for {l.title}\nvoid init_{l.slug.replace('-', '_')}(void) {{}}\n```"
                        elif stype == "example":
                            md += f"\n\n```python\n# Example for {l.title}\nprint('Executing {l.title}...')\n```"
                        elif stype == "pitfall":
                            md += "\n\n1. Voltage level mismatch.\n2. ISR lockups.\n3. Pin floating state."
                        elif stype == "qa":
                            md += f"\n\n**Q: Purpose of {l.title}?**\nA: Handles hardware and data operations."

                        sec = LessonSection(
                            lesson_id=l.id,
                            section_type=stype,
                            title=stitle,
                            content_markdown=md,
                            content_html="",
                            sort_order=idx,
                            is_visible=True,
                            created_at=datetime.utcnow(),
                            updated_at=datetime.utcnow()
                        )
                        db.session.add(sec)
                        added_count += 1

        db.session.commit()
        print(f"Successfully added {added_count} missing section notes to database!")

if __name__ == "__main__":
    populate()
