"""
audit_catalog.py
Audits the Python Full Stack catalog category for:
  1. Wrong courses (Java in Python Full Stack)
  2. Duplicate Python courses
  3. Duplicate C Programming courses
  4. Empty courses (0h / no modules / no lessons)
  5. Repeated courses across the catalog
"""
import sys, os
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

from app import create_app
from app.domains.content.models import Category, Subject, Course, Module, Lesson

app = create_app()

with app.app_context():
    # ── 1. Find the Python Full Stack category ────────────────────
    cat = Category.query.filter(Category.name.ilike('%python full stack%')).first()
    if not cat:
        print("ERROR: Could not find 'Python Full Stack' category")
        sys.exit(1)

    print(f"\n{'='*65}")
    print(f"CATEGORY: {cat.name}  (id={cat.id}, slug={cat.slug})")
    print(f"{'='*65}")

    subjects = cat.subjects.all()
    print(f"  Subjects in this category: {len(subjects)}")

    for subj in subjects:
        print(f"\n  SUBJECT: {subj.name}  (id={subj.id})")
        courses = subj.courses.all()
        for c in courses:
            mod_count  = c.modules.count()
            lesson_count = sum(m.lessons.count() for m in c.modules.all())
            print(f"    COURSE id={c.id:4d}  est={c.estimated_hours:3d}h  "
                  f"mods={mod_count:2d}  lessons={lesson_count:3d}  "
                  f"status={c.status:10s}  slug={c.slug}")

    # ── 2. Global duplicate check ─────────────────────────────────
    print(f"\n{'='*65}")
    print("GLOBAL DUPLICATE COURSES (same title, different ids)")
    print(f"{'='*65}")
    all_courses = Course.query.filter_by(deleted_at=None).all()
    from collections import defaultdict
    by_title = defaultdict(list)
    for c in all_courses:
        by_title[c.title.strip().lower()].append(c)

    dups_found = False
    for title, group in sorted(by_title.items()):
        if len(group) > 1:
            dups_found = True
            print(f"\n  DUPLICATE: '{group[0].title}'")
            for c in group:
                mod_count    = c.modules.count()
                lesson_count = sum(m.lessons.count() for m in c.modules.all())
                subj = c.subject
                cat2  = subj.category if subj else None
                print(f"    id={c.id:4d}  category={cat2.name if cat2 else 'N/A':30s}  "
                      f"mods={mod_count}  lessons={lesson_count}  hours={c.estimated_hours}")
    if not dups_found:
        print("  No global duplicates found.")

    # ── 3. Empty courses (0 modules or 0 lessons) ─────────────────
    print(f"\n{'='*65}")
    print("EMPTY COURSES in Python Full Stack category")
    print(f"{'='*65}")
    empty_found = False
    for subj in subjects:
        for c in subj.courses.all():
            mod_count    = c.modules.count()
            lesson_count = sum(m.lessons.count() for m in c.modules.all())
            if mod_count == 0 or lesson_count == 0:
                empty_found = True
                print(f"  id={c.id:4d}  title='{c.title}'  mods={mod_count}  lessons={lesson_count}")
    if not empty_found:
        print("  None found.")

    # ── 4. Summary of all categories ──────────────────────────────
    print(f"\n{'='*65}")
    print("ALL CATEGORIES SUMMARY")
    print(f"{'='*65}")
    for cat2 in Category.query.order_by(Category.name).all():
        subj_count   = cat2.subjects.count()
        course_count = sum(s.courses.count() for s in cat2.subjects.all())
        print(f"  {cat2.name:40s}  subjects={subj_count}  courses={course_count}")

    print("\nAudit complete.")
