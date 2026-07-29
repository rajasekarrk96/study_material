"""
fast_populate_iot_notes.py
==========================
Ultra-fast bulk population script for IoT Full Stack lesson sections.
Uses db.session.bulk_save_objects() for sub-second execution.
"""
import sys
from datetime import datetime
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

from app import create_app
from app.core.extensions import db
from app.domains.content.models import Course, LessonSection

app = create_app()

SECTION_TYPES = ["overview", "concept", "syntax", "example", "pitfall", "qa"]
TARGET_COURSES = ["embedded-c", "arduino", "esp32", "sensors-actuators", "mqtt"]

def ultra_fast_populate():
    with app.app_context():
        # Load all existing section (lesson_id, section_type) pairs into a set in 1 query
        existing_pairs = set(
            db.session.query(LessonSection.lesson_id, LessonSection.section_type).all()
        )

        objects_to_insert = []

        for slug in TARGET_COURSES:
            c = Course.query.filter_by(slug=slug, is_deleted=False).first()
            if not c: continue

            c_count = 0
            for m in c.modules.all():
                for l in m.lessons.filter_by(is_deleted=False).all():
                    l.status = 'published'
                    for idx, stype in enumerate(SECTION_TYPES, start=1):
                        if (l.id, stype) in existing_pairs:
                            continue

                        stitle = stype.capitalize()
                        if stype == "qa": stitle = "Q & A"
                        elif stype == "concept": stitle = "Core Concept"

                        md = f"### {stitle}: {l.title}\n\nComprehensive technical guide and practical examples for {l.title} in {c.title}."
                        if stype == "syntax":
                            md += f"\n\n```c\n// Syntax reference for {l.title}\nvoid setup_{l.slug.replace('-', '_')}(void) {{\n    // Hardware initialization\n}}\n```"
                        elif stype == "example":
                            md += f"\n\n```python\n# Practical test for {l.title}\nprint('Testing {l.title}...')\n```"
                        elif stype == "pitfall":
                            md += "\n\n1. Floating pin configuration.\n2. Overlooking interrupt flags.\n3. Supply voltage mismatch."
                        elif stype == "qa":
                            md += f"\n\n**Q1: What is the primary role of {l.title}?**\nA: Provides core hardware control and data processing."

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
                        objects_to_insert.append(sec)
                        c_count += 1
            
            c.status = 'published'

        if objects_to_insert:
            print(f"Bulk saving {len(objects_to_insert)} LessonSection objects to DB...")
            db.session.bulk_save_objects(objects_to_insert)
            db.session.commit()

        print(f"\n========================================================")
        print(f"SUCCESS: Inserted {len(objects_to_insert)} section notes into DB!")
        print(f"========================================================")

if __name__ == "__main__":
    ultra_fast_populate()
