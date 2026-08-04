"""
audit_curriculum_markdown_files.py
==================================
Audits the physical markdown file archives in docs/curriculum/ vs Database.
Exports database section notes to docs/curriculum/ markdown files so 100% of published
courses exist both in the database AND as local markdown files in docs/curriculum/.
"""
import os, sys
from re import sub
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

from app import create_app
from app.core.extensions import db
from app.domains.content.models import Course, Module, Lesson, LessonSection

app = create_app()

CURRICULUM_DIR = r'd:\My Drive\all files\PROJECT FILES\notes\docs\curriculum'

def sanitize_filename(name):
    clean = sub(r'[^\w\s-]', '', name.lower())
    return sub(r'[-\s]+', '_', clean).strip('_')

def audit_and_export():
    with app.app_context():
        courses = Course.query.filter_by(is_deleted=False).order_by(Course.id).all()

        print("===================================================================================")
        print("          CURRICULUM MARKDOWN FILES vs DATABASE AUDIT & ARCHIVAL EXPORT")
        print("===================================================================================")

        total_courses = len(courses)
        exported_files = 0

        for c_idx, course in enumerate(courses, start=1):
            folder_name = f"_{c_idx:02d}_{sanitize_filename(course.slug)}"
            course_dir = os.path.join(CURRICULUM_DIR, folder_name)

            # Check if directory exists or contains files
            existing_files = []
            if os.path.exists(course_dir):
                existing_files = [f for f in os.listdir(course_dir) if f.endswith('.md')]

            modules = course.modules.order_by(Module.sort_order).all()
            tot_lessons = sum(m.lessons.filter_by(is_deleted=False).count() for m in modules)

            print(f"{c_idx:2d}. {course.title:35s} ({course.slug:22s}) | DB Lessons: {tot_lessons:3d} | MD Files in docs/curriculum: {len(existing_files):3d}")

            # If course is published and has lessons, ensure markdown files exist
            if course.status == 'published' and tot_lessons > 0:
                os.makedirs(course_dir, exist_ok=True)

                for m in modules:
                    for l in m.lessons.filter_by(is_deleted=False).order_by(Lesson.sort_order).all():
                        filename = f"_{m.sort_order:02d}_{l.sort_order:02d}_{sanitize_filename(l.slug)}.md"
                        filepath = os.path.join(course_dir, filename)

                        if not os.path.exists(filepath):
                            secs = LessonSection.query.filter_by(lesson_id=l.id).order_by(LessonSection.sort_order).all()
                            
                            md_content = []
                            md_content.append(f"# {l.title}\n")
                            md_content.append(f"> **Course**: {course.title} | **Module**: {m.title} | **Difficulty**: {l.difficulty_level}\n")
                            md_content.append("---\n")

                            if secs:
                                for s in secs:
                                    md_content.append(f"{s.content_markdown}\n\n---\n")
                            else:
                                md_content.append(f"### Overview: {l.title}\n\n{l.summary or 'Detailed lesson content.'}\n")

                            with open(filepath, 'w', encoding='utf-8') as f:
                                f.write("\n".join(md_content))
                            exported_files += 1

        print("===================================================================================")
        print(f"AUDIT SUMMARY: Processed {total_courses} Master Courses.")
        print(f"EXPORT RESULT: Created/Archived {exported_files} missing markdown lesson files into docs/curriculum/")
        print("===================================================================================")

if __name__ == "__main__":
    audit_and_export()
