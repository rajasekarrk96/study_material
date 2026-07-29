"""
fix_catalog_issues.py
=====================
Fixes catalog problems with proper flush ordering to avoid slug conflicts:

1. Python duplicate  -> Rename stub id=1 slug to temp, flush, then rename id=30006
                        to 'Core Python'/'core-python', soft-delete stub id=1
2. Java courses      -> Move subject id=2 to 'Programming Languages' category
3. C courses         -> Move subject id=6 to 'Programming Languages' category,
                        soft-delete thin stub id=6, rename id=60002 to 'C Programming'
4. Python Data Sci   -> Move subject id=60009 to 'Python AI & Data Science' category
5. Estimated hours   -> Recalculate from lesson minutes for all affected courses
"""
import sys
from datetime import datetime

sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

from app import create_app
from app.core.extensions import db
from app.domains.content.models import Category, Subject, Course

app = create_app()

def recalc_hours(course):
    """Recalculate estimated_hours from sum of lesson minutes."""
    total_minutes = 0
    for mod in course.modules.all():
        for les in mod.lessons.all():
            total_minutes += (les.estimated_minutes or 0)
    course.estimated_hours = max(1, round(total_minutes / 60)) if total_minutes else 0

def soft_delete_course(course):
    now = datetime.utcnow()
    course.deleted_at = now
    for mod in course.modules.all():
        for les in mod.lessons.all():
            les.deleted_at = now
    print(f"  [SOFT-DELETE] Course id={course.id} '{course.title}'")

with app.app_context():
    print("\n" + "="*65)
    print("CATALOG FIX SCRIPT")
    print("="*65)

    # Look up categories
    cat_pfs = Category.query.filter(Category.name.ilike('%python full stack%')).first()
    cat_pl  = Category.query.filter(Category.name.ilike('%programming languages%')).first()
    cat_ai  = Category.query.filter(Category.name.ilike('%python ai%')).first()

    assert cat_pfs, "ERROR: Python Full Stack category not found"
    assert cat_pl,  "ERROR: Programming Languages category not found"
    assert cat_ai,  "ERROR: Python AI & Data Science category not found"

    print(f"\n  Python Full Stack     -> id={cat_pfs.id}")
    print(f"  Programming Languages -> id={cat_pl.id}")
    print(f"  Python AI & DS        -> id={cat_ai.id}")

    # ─── FIX 1: Python duplicate ──────────────────────────────────
    # STEP 1a: Move the stub (id=1) to a temp slug FIRST, then flush
    # This frees the 'core-python' slug before we assign it to id=30006
    print("\n[FIX 1] Python duplicate")

    c_stub = Course.query.get(1)
    c_rich = Course.query.get(30006)
    assert c_stub, "Course id=1 not found"
    assert c_rich, "Course id=30006 not found"

    # 1a. Rename stub to temp slug and flush to release the unique key
    c_stub.slug  = "core-python-to-delete"
    c_stub.title = "Core Python (deprecated)"
    db.session.flush()
    print(f"  [FLUSH] Stub id=1 slug freed -> 'core-python-to-delete'")

    # 1b. Now rename the rich course to the proper slug
    c_rich.title      = "Core Python"
    c_rich.slug       = "core-python"
    c_rich.meta_title = "Core Python"
    recalc_hours(c_rich)
    print(f"  [UPDATE] Course id=30006 -> title='Core Python', slug='core-python', hours={c_rich.estimated_hours}")

    # 1c. Soft-delete the stub
    soft_delete_course(c_stub)

    # ─── FIX 2: Move Java subject to Programming Languages ────────
    print("\n[FIX 2] Java subject -> Programming Languages")
    subj_java = Subject.query.get(2)
    assert subj_java, "Subject id=2 (Java) not found"

    old_cat = subj_java.category_id
    subj_java.category_id = cat_pl.id
    print(f"  [MOVE] Subject '{subj_java.name}' (id=2): category {old_cat} -> {cat_pl.id}")

    db.session.flush()

    for cid in [2, 60001]:
        c = Course.query.get(cid)
        if c:
            recalc_hours(c)
            print(f"  [HOURS] Course id={cid} '{c.title}' -> {c.estimated_hours}h")

    # ─── FIX 3: C subject -> Programming Languages ────────────────
    print("\n[FIX 3] C subject -> Programming Languages")
    subj_c = Subject.query.get(6)
    assert subj_c, "Subject id=6 (C) not found"

    old_cat = subj_c.category_id
    subj_c.category_id = cat_pl.id
    print(f"  [MOVE] Subject '{subj_c.name}' (id=6): category {old_cat} -> {cat_pl.id}")

    # Soft-delete thin stub (id=6, C Programming Fundamentals - 1 mod / 2 lessons)
    c_c_stub = Course.query.get(6)
    assert c_c_stub, "Course id=6 not found"

    # Free slug first
    c_c_stub.slug  = "c-programming-fundamentals-deprecated"
    c_c_stub.title = "C Programming Fundamentals (deprecated)"
    db.session.flush()
    print(f"  [FLUSH] C stub id=6 slug freed")

    soft_delete_course(c_c_stub)

    # Rename the rich C course
    c_c_rich = Course.query.get(60002)
    assert c_c_rich, "Course id=60002 not found"
    c_c_rich.title      = "C Programming"
    c_c_rich.slug       = "c-programming"
    c_c_rich.meta_title = "C Programming"
    recalc_hours(c_c_rich)
    print(f"  [UPDATE] Course id=60002 -> title='C Programming', hours={c_c_rich.estimated_hours}")

    # ─── FIX 4: Python Data Science -> Python AI & DS ─────────────
    print("\n[FIX 4] Python Data Science subject -> Python AI & Data Science")
    subj_ds = Subject.query.get(60009)
    assert subj_ds, "Subject id=60009 (Python Data Science) not found"

    old_cat = subj_ds.category_id
    subj_ds.category_id = cat_ai.id
    print(f"  [MOVE] Subject '{subj_ds.name}' (id=60009): category {old_cat} -> {cat_ai.id}")

    c_ds = Course.query.get(60013)
    if c_ds:
        recalc_hours(c_ds)
        print(f"  [HOURS] Course id=60013 '{c_ds.title}' -> {c_ds.estimated_hours}h")

    # ─── FIX 5: Recalc 0h courses remaining in Python Full Stack ──
    print("\n[FIX 5] Recalc 0h courses in Python Full Stack")
    db.session.flush()
    for subj in cat_pfs.subjects.all():
        for c in subj.courses.all():
            if c.deleted_at:
                continue
            if c.estimated_hours == 0:
                recalc_hours(c)
                print(f"  [HOURS] Course id={c.id:5d} '{c.title}' -> {c.estimated_hours}h")

    # ─── Commit ───────────────────────────────────────────────────
    print("\n  Committing all changes...")
    db.session.commit()
    print("  [OK] All changes committed successfully.\n")

    # ─── Post-fix summary ─────────────────────────────────────────
    print("="*65)
    print("POST-FIX: Python Full Stack")
    print("="*65)
    for subj in Category.query.get(cat_pfs.id).subjects.all():
        print(f"\n  SUBJECT: {subj.name}")
        for c in subj.courses.filter_by(deleted_at=None).all():
            mod_count    = c.modules.count()
            lesson_count = sum(m.lessons.count() for m in c.modules.all())
            print(f"    id={c.id:5d}  '{c.title}'  {c.estimated_hours}h  "
                  f"mods={mod_count}  lessons={lesson_count}")

    print("\n" + "="*65)
    print("POST-FIX: Programming Languages")
    print("="*65)
    for subj in Category.query.get(cat_pl.id).subjects.all():
        print(f"\n  SUBJECT: {subj.name}")
        for c in subj.courses.filter_by(deleted_at=None).all():
            mod_count    = c.modules.count()
            lesson_count = sum(m.lessons.count() for m in c.modules.all())
            print(f"    id={c.id:5d}  '{c.title}'  {c.estimated_hours}h  "
                  f"mods={mod_count}  lessons={lesson_count}")

    print("\nDone.")
