"""
Learning OS — Navbar Navigation Service.
Builds the Category -> Subject -> Course tree used by the "Courses" dropdown,
so the flat alphabetical course list can be browsed by domain/subdomain instead.
"""
from types import SimpleNamespace
from app.domains.content.models import Category, Subject, Course
from app.core.cache import cache_memoize


@cache_memoize(timeout_seconds=300)
def get_nav_catalog_tree():
    """One query, grouped in Python into Category -> Subject -> [Course]."""
    rows = (
        Course.query
        .join(Subject, Course.subject_id == Subject.id)
        .join(Category, Subject.category_id == Category.id)
        .filter(
            Course.is_deleted == False,
            Course.status == "published",
            Category.is_active == True,
            Subject.is_active == True,
        )
        .order_by(Category.sort_order, Subject.sort_order, Course.title)
        .add_columns(
            Subject.id.label("subject_id"),
            Subject.name.label("subject_name"),
            Category.id.label("category_id"),
            Category.name.label("category_name"),
            Category.icon.label("category_icon"),
        )
        .all()
    )

    categories = {}
    for course, subject_id, subject_name, category_id, category_name, category_icon in rows:
        cat = categories.setdefault(category_id, SimpleNamespace(
            id=category_id, name=category_name, icon=category_icon, subjects={}
        ))
        subj = cat.subjects.setdefault(subject_id, SimpleNamespace(
            id=subject_id, name=subject_name, courses=[]
        ))
        subj.courses.append(SimpleNamespace(title=course.title, slug=course.slug))

    tree = []
    for cat in categories.values():
        cat.subjects = list(cat.subjects.values())
        tree.append(cat)
    return tree
