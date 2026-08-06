"""Learning OS — Public Blueprint: Home, Catalog & Learning Path routes."""
from collections import defaultdict
from types import SimpleNamespace
from flask import Blueprint, render_template, jsonify, abort, redirect, url_for, flash
from flask_login import current_user, login_required
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from app.core.extensions import db
from app.domains.content.models import Category, Subject, Course, Module, Lesson, LessonSection, Source
from app.domains.learning_path.models import (
    LearningPath, PathCourse, UserLearningPathProgress, UserCourseProgress, LearningPathCategory
)
from app.core.cache import cache_memoize

public_bp = Blueprint("public", __name__, template_folder="templates")


@cache_memoize(timeout_seconds=300)
def _get_cached_categories_data():
    """Retrieve active catalog categories and cache them as plain namespaces."""
    categories = Category.query.filter_by(is_active=True).all()
    cached = []
    for cat in categories:
        cached.append(SimpleNamespace(
            id=cat.id,
            name=cat.name,
            slug=cat.slug,
            description=cat.description,
            icon=cat.icon,
            color=cat.color,
            type=cat.type
        ))
    return cached


@cache_memoize(timeout_seconds=300)
def _get_cached_courses_by_category():
    """
    Single-query fetch of every published course, grouped by category id.
    Replaces the old cat.subjects -> subject.courses template traversal, which
    fired one lazy-loaded query per category and per subject (N+1).
    """
    courses = (
        Course.query
        .join(Subject, Course.subject_id == Subject.id)
        .join(Category, Subject.category_id == Category.id)
        .filter(
            Course.is_deleted == False,
            Course.status == "published",
            Category.is_active == True,
        )
        .options(joinedload(Course.subject))
        .order_by(Category.sort_order, Course.title)
        .add_columns(Category.id.label("category_id"))
        .all()
    )

    by_category = defaultdict(list)
    for course, category_id in courses:
        by_category[category_id].append(course)
    return by_category


@cache_memoize(timeout_seconds=300)
def _get_cached_path_lesson_counts():
    """
    Aggregate lesson count per learning path in one query.
    Replaces LearningPath.total_lessons, which did course.modules.all() +
    mod.lessons.count() per course per path (hundreds of round-trips).
    """
    rows = (
        db.session.query(PathCourse.path_id, func.count(Lesson.id))
        .join(Course, PathCourse.course_id == Course.id)
        .join(Module, Module.course_id == Course.id)
        .join(Lesson, Lesson.module_id == Module.id)
        .filter(Module.is_published == True, Lesson.is_deleted == False)
        .group_by(PathCourse.path_id)
        .all()
    )
    return dict(rows)


@cache_memoize(timeout_seconds=300)
def _get_cached_course_structure_counts():
    """Return published module and lesson totals for every catalog course."""
    rows = (
        db.session.query(
            Course.id,
            func.count(func.distinct(Module.id)).label("module_count"),
            func.count(func.distinct(Lesson.id)).label("lesson_count"),
        )
        .outerjoin(
            Module,
            (Module.course_id == Course.id) & (Module.is_published == True),
        )
        .outerjoin(
            Lesson,
            (Lesson.module_id == Module.id) & (Lesson.is_deleted == False),
        )
        .filter(Course.is_deleted == False, Course.status == "published")
        .group_by(Course.id)
        .all()
    )
    return {
        course_id: {"modules": module_count, "lessons": lesson_count}
        for course_id, module_count, lesson_count in rows
    }


from flask_login import current_user
from app.services.learning import DashboardService

@public_bp.route("/")
def home():
    if current_user.is_authenticated:
        data = DashboardService.get_dashboard_data(current_user.id)
        return render_template(
            "public/dashboard.html",
            dashboard=data
        )
    
    categories = _get_cached_categories_data()
    featured_courses = Course.query.filter_by(
        is_featured=True, status="published", is_deleted=False
    ).limit(6).all()
    return render_template(
        "public/home.html",
        categories=categories,
        featured_courses=featured_courses,
    )


@public_bp.route("/catalog")
def catalog():
    categories = Category.query.filter_by(is_active=True).order_by(Category.sort_order).all()
    courses_by_category = _get_cached_courses_by_category()
    course_structure_counts = _get_cached_course_structure_counts()
    learning_paths = LearningPath.query.filter_by(is_active=True).order_by(
        LearningPath.is_featured.desc(), LearningPath.sort_order
    ).all()
    path_lesson_counts = _get_cached_path_lesson_counts()

    user_path_progress = {}
    if current_user.is_authenticated:
        for prog in UserLearningPathProgress.query.filter_by(user_id=current_user.id).all():
            user_path_progress[prog.path_id] = prog

    # ── 4-tier architecture data ──────────────────────────────────────────────
    # Build foundation sub-groups from course_type + Category.type
    foundation_groups = {
        "programming": {"label": "Programming Languages", "icon": "fa-code",    "color": "#4f46e5", "courses": []},
        "frontend":    {"label": "Frontend Development",  "icon": "fa-desktop",  "color": "#0891b2", "courses": []},
        "backend":     {"label": "Backend & Databases",   "icon": "fa-server",   "color": "#059669", "courses": []},
        "core":        {"label": "Core Engineering",      "icon": "fa-microchip","color": "#d97706", "courses": []},
    }
    specializations = []
    electives = []

    all_published = (
        Course.query
        .join(Subject, Course.subject_id == Subject.id)
        .join(Category, Subject.category_id == Category.id)
        .filter(Course.is_deleted == False, Course.status == "published")
        .options(joinedload(Course.subject))
        .all()
    )

    for course in all_published:
        ct = getattr(course, "course_type", "foundation")
        cat_type = (course.subject.category.type or "") if course.subject and course.subject.category else ""

        if ct == "specialization":
            specializations.append(course)
        elif ct == "elective":
            electives.append(course)
        else:
            # foundation — route to sub-group by Category.type
            if "frontend" in cat_type:
                foundation_groups["frontend"]["courses"].append(course)
            elif "backend" in cat_type:
                foundation_groups["backend"]["courses"].append(course)
            elif "core" in cat_type:
                foundation_groups["core"]["courses"].append(course)
            else:
                foundation_groups["programming"]["courses"].append(course)

    # Group learning paths by domain
    lp_domain_groups = defaultdict(list)
    for lp in learning_paths:
        domain = getattr(lp, "domain", None) or "web"
        lp_domain_groups[domain].append(lp)

    lp_category_obj = LearningPathCategory.query.filter_by(is_active=True).order_by(
        LearningPathCategory.sort_order
    ).all()

    return render_template(
        "public/catalog.html",
        # Existing variables (unchanged — backward compat)
        categories=categories,
        courses_by_category=courses_by_category,
        course_structure_counts=course_structure_counts,
        course_count=sum(len(courses) for courses in courses_by_category.values()),
        learning_paths=learning_paths,
        path_lesson_counts=path_lesson_counts,
        user_path_progress=user_path_progress,
        path_count=len(learning_paths),
        # 4-tier architecture variables (new)
        foundation_groups=foundation_groups,
        specializations=specializations,
        electives=electives,
        lp_domain_groups=lp_domain_groups,
        lp_categories=lp_category_obj,
    )


from flask_login import login_required
from flask import request

@public_bp.route("/search")
@login_required
def search_view():
    """Renders the hybrid search results workspace page."""
    from app.domains.knowledge.search import hybrid_search
    query = request.args.get("q", "").strip()
    results = []
    if query:
        results = hybrid_search(query, top_k=15)
    return render_template(
        "public/search.html",
        query=query,
        results=results
    )


@public_bp.route("/api/v1/stats")
def stats():
    return jsonify({
        "courses": Course.query.filter_by(is_deleted=False).count(),
        "lessons": Lesson.query.filter_by(is_deleted=False).count(),
        "topics": LessonSection.query.count(),
        "sources": Source.query.count()
    })


from flask import Response, url_for

@public_bp.route("/sitemap.xml")
def sitemap():
    """Generate dynamic XML sitemap for SEO crawlers."""
    import xml.etree.ElementTree as ET

    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    def add_url(loc, priority="0.5", changefreq="daily"):
        url = ET.SubElement(urlset, "url")
        loc_el = ET.SubElement(url, "loc")
        loc_el.text = loc
        freq_el = ET.SubElement(url, "changefreq")
        freq_el.text = changefreq
        priority_el = ET.SubElement(url, "priority")
        priority_el.text = priority

    # Static pages
    add_url(url_for("public.home", _external=True), priority="1.0", changefreq="daily")
    add_url(url_for("public.catalog", _external=True), priority="0.9", changefreq="weekly")

    # Courses & Lessons
    courses = Course.query.filter_by(status="published", is_deleted=False).all()
    for c in courses:
        add_url(url_for("learn.course_overview", course_slug=c.slug, _external=True), priority="0.8", changefreq="weekly")
        
        # Lessons in course modules
        for module in c.modules.filter_by(is_published=True).all():
            for lesson in module.lessons.filter_by(status="published", is_deleted=False).all():
                add_url(
                    url_for("learn.lesson_view", course_slug=c.slug, module_slug=module.slug, lesson_slug=lesson.slug, _external=True),
                    priority="0.7",
                    changefreq="weekly"
                )

    xml_str = ET.tostring(urlset, encoding="utf-8", method="xml")
    xml_declaration = b'<?xml version="1.0" encoding="UTF-8"?>\n'
    return Response(xml_declaration + xml_str, mimetype="application/xml")


# ─────────────────────────────────────────────────────────────
# Learning Path Routes
# ─────────────────────────────────────────────────────────────

@public_bp.route("/paths/")
def learning_paths():
    """List all active learning paths."""
    paths = LearningPath.query.filter_by(is_active=True).order_by(
        LearningPath.is_featured.desc(), LearningPath.sort_order
    ).all()

    # Attach user progress if logged in
    user_progress = {}
    if current_user.is_authenticated:
        for prog in UserLearningPathProgress.query.filter_by(user_id=current_user.id).all():
            user_progress[prog.path_id] = prog

    return render_template(
        "public/learning_paths.html",
        paths=paths,
        user_progress=user_progress,
    )


@public_bp.route("/paths/<path_slug>/")
def learning_path_detail(path_slug: str):
    """Detail view for a single learning path."""
    path = LearningPath.query.filter_by(slug=path_slug, is_active=True).first_or_404()

    # Build section-grouped course list
    sections = {}
    for pc in path.courses:
        label = pc.section_label or "Core"
        sections.setdefault(label, [])
        sections[label].append(pc)

    # User progress
    user_prog = None
    completed_course_ids = set()
    if current_user.is_authenticated:
        user_prog = UserLearningPathProgress.query.filter_by(
            user_id=current_user.id, path_id=path.id
        ).first()
        for cp in UserCourseProgress.query.filter_by(
            user_id=current_user.id, is_completed=True
        ).all():
            completed_course_ids.add(cp.course_id)

    path_lesson_counts = _get_cached_path_lesson_counts()

    return render_template(
        "public/learning_path_detail.html",
        path=path,
        sections=sections,
        user_prog=user_prog,
        completed_course_ids=completed_course_ids,
        total_lessons=path_lesson_counts.get(path.id, 0),
    )


@public_bp.route("/paths/<path_slug>/enroll", methods=["POST"])
@login_required
def enroll_learning_path(path_slug: str):
    """Enroll current user into a learning path."""
    from app.core.extensions import db
    path = LearningPath.query.filter_by(slug=path_slug, is_active=True).first_or_404()

    existing = UserLearningPathProgress.query.filter_by(
        user_id=current_user.id, path_id=path.id
    ).first()

    if not existing:
        total = len([pc for pc in path.courses if pc.is_required])
        prog = UserLearningPathProgress(
            user_id=current_user.id,
            path_id=path.id,
            total_courses=total,
            completed_courses=0,
        )
        db.session.add(prog)
        db.session.commit()
        flash(f"Enrolled in '{path.title}'! Start your first course below.", "success")
    else:
        flash(f"You are already enrolled in '{path.title}'.", "info")

    return redirect(url_for("public.learning_path_detail", path_slug=path.slug))


# ─────────────────────────────────────────────────────────────
# 4-Tier Architecture Browse Routes
# ─────────────────────────────────────────────────────────────

# Sub-category labels for foundations tab
FOUNDATION_SUBCATEGORIES = {
    "programming": {
        "label": "Programming Languages",
        "icon": "fa-code",
        "color": "#4f46e5",
        "description": "Core programming languages and DSA",
    },
    "frontend": {
        "label": "Frontend Development",
        "icon": "fa-desktop",
        "color": "#0891b2",
        "description": "HTML, CSS, JavaScript, React and UI frameworks",
    },
    "backend": {
        "label": "Backend & Databases",
        "icon": "fa-server",
        "color": "#059669",
        "description": "Server frameworks, APIs, and database technologies",
    },
    "core": {
        "label": "Core Engineering",
        "icon": "fa-microchip",
        "color": "#d97706",
        "description": "Mathematics, networking, Linux, Docker, and embedded systems",
    },
}


@cache_memoize(timeout_seconds=300)
def _get_courses_by_type_and_category():
    """
    Single-query fetch of all published courses grouped by:
      (course_type, category.type or subject.name)
    Powers the foundations tab sub-groups.
    """
    courses = (
        Course.query
        .join(Subject, Course.subject_id == Subject.id)
        .join(Category, Subject.category_id == Category.id)
        .filter(
            Course.is_deleted == False,
            Course.status == "published",
            Course.is_standalone == True,
        )
        .options(joinedload(Course.subject))
        .order_by(Category.sort_order, Course.title)
        .all()
    )

    by_type = {
        "foundation_programming": [],
        "foundation_frontend": [],
        "foundation_backend": [],
        "foundation_core": [],
        "specialization": [],
        "elective": [],
    }

    for course in courses:
        cat_type = course.subject.category.type if course.subject and course.subject.category else ""
        ctype = course.course_type  # foundation|specialization|elective

        if ctype == "foundation":
            if cat_type in ("foundation_programming", "foundation_frontend",
                            "foundation_backend", "foundation_core"):
                by_type[cat_type].append(course)
            else:
                # Fallback — put uncategorized foundations in programming
                by_type["foundation_programming"].append(course)
        elif ctype == "specialization":
            by_type["specialization"].append(course)
        elif ctype == "elective":
            by_type["elective"].append(course)

    return by_type


@public_bp.route("/browse/")
def browse_index():
    """Redirect to the enhanced catalog as the main browse entry point."""
    return redirect(url_for("public.catalog"))


@public_bp.route("/browse/foundations/")
def browse_foundations():
    """Browse all foundation courses, grouped by sub-category."""
    course_groups = _get_courses_by_type_and_category()
    foundation_data = {
        sub: {
            "meta": meta,
            "courses": course_groups.get(f"foundation_{sub}", []),
        }
        for sub, meta in FOUNDATION_SUBCATEGORIES.items()
    }
    total = sum(len(g["courses"]) for g in foundation_data.values())
    return render_template(
        "public/browse_foundations.html",
        foundation_data=foundation_data,
        total_courses=total,
        active_sub="all",
    )


@public_bp.route("/browse/foundations/<sub_category>/")
def browse_foundations_sub(sub_category: str):
    """Browse a specific foundation sub-category: programming|frontend|backend|core."""
    if sub_category not in FOUNDATION_SUBCATEGORIES:
        abort(404)
    course_groups = _get_courses_by_type_and_category()
    courses = course_groups.get(f"foundation_{sub_category}", [])
    meta = FOUNDATION_SUBCATEGORIES[sub_category]
    return render_template(
        "public/browse_foundations.html",
        foundation_data={sub_category: {"meta": meta, "courses": courses}},
        total_courses=len(courses),
        active_sub=sub_category,
    )


@public_bp.route("/browse/specializations/")
def browse_specializations():
    """Browse all specialization courses."""
    course_groups = _get_courses_by_type_and_category()
    courses = course_groups.get("specialization", [])
    return render_template(
        "public/browse_specializations.html",
        courses=courses,
        total_courses=len(courses),
    )


@public_bp.route("/browse/electives/")
def browse_electives():
    """Browse all elective courses."""
    course_groups = _get_courses_by_type_and_category()
    courses = course_groups.get("elective", [])
    return render_template(
        "public/browse_electives.html",
        courses=courses,
        total_courses=len(courses),
    )


@public_bp.route("/browse/paths/")
def browse_paths():
    """Browse all learning paths grouped by domain category."""
    lp_categories = LearningPathCategory.query.filter_by(is_active=True).order_by(
        LearningPathCategory.sort_order
    ).all()

    paths_by_category = {}
    for lpc in lp_categories:
        paths = LearningPath.query.filter_by(
            is_active=True, category_id=lpc.id
        ).order_by(LearningPath.is_featured.desc(), LearningPath.sort_order).all()
        if paths:
            paths_by_category[lpc] = paths

    # Uncategorized paths
    uncategorized = LearningPath.query.filter_by(
        is_active=True, category_id=None
    ).order_by(LearningPath.sort_order).all()

    path_lesson_counts = _get_cached_path_lesson_counts()

    return render_template(
        "public/browse_paths.html",
        paths_by_category=paths_by_category,
        uncategorized_paths=uncategorized,
        path_lesson_counts=path_lesson_counts,
    )


@public_bp.route("/browse/paths/<domain>/")
def browse_paths_domain(domain: str):
    """Browse learning paths filtered by domain: web|data|iot|cloud|devops|qa."""
    VALID_DOMAINS = {"web", "data", "iot", "cloud", "devops", "qa"}
    if domain not in VALID_DOMAINS:
        abort(404)

    paths = LearningPath.query.filter_by(
        is_active=True, domain=domain
    ).order_by(LearningPath.is_featured.desc(), LearningPath.sort_order).all()

    path_lesson_counts = _get_cached_path_lesson_counts()

    return render_template(
        "public/browse_paths.html",
        paths_by_category={},
        uncategorized_paths=paths,
        path_lesson_counts=path_lesson_counts,
        active_domain=domain,
    )


@public_bp.route("/api/v1/courses/type/<course_type>")
def api_courses_by_type(course_type: str):
    """JSON API: list courses by type (foundation|specialization|elective)."""
    VALID_TYPES = {"foundation", "specialization", "elective"}
    if course_type not in VALID_TYPES:
        return jsonify({"error": "Invalid course type"}), 400

    courses = (
        Course.query
        .filter_by(course_type=course_type, is_deleted=False, status="published")
        .order_by(Course.title)
        .all()
    )
    return jsonify({
        "course_type": course_type,
        "count": len(courses),
        "courses": [
            {
                "id": c.id,
                "slug": c.slug,
                "title": c.title,
                "subtitle": c.subtitle,
                "difficulty_level": c.difficulty_level,
                "estimated_hours": c.estimated_hours,
            }
            for c in courses
        ],
    })
