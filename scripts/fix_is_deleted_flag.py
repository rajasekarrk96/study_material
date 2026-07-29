"""
fix_is_deleted_flag.py
Set is_deleted=True for all courses where deleted_at is set but is_deleted is False.
"""
import sys
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

from app import create_app
from app.core.extensions import db
from app.domains.content.models import Course, Lesson

app = create_app()

with app.app_context():
    # Fix courses: set is_deleted=True where deleted_at is populated
    courses = Course.query.filter(
        Course.deleted_at.isnot(None),
        Course.is_deleted == False
    ).all()

    print(f"Found {len(courses)} course(s) with deleted_at set but is_deleted=False:")
    for c in courses:
        c.is_deleted = True
        print(f"  [FIX] Course id={c.id} '{c.title}' -> is_deleted=True")

    # Fix lessons inside those courses too
    lessons = Lesson.query.filter(
        Lesson.deleted_at.isnot(None),
        Lesson.is_deleted == False
    ).all()

    print(f"\nFound {len(lessons)} lesson(s) with deleted_at set but is_deleted=False:")
    for l in lessons:
        l.is_deleted = True
        print(f"  [FIX] Lesson id={l.id} '{l.title}' -> is_deleted=True")

    db.session.commit()
    print("\n[OK] Committed. Deprecated courses will no longer appear in catalog.")
