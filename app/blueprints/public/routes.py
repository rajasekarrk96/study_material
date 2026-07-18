"""Learning OS — Public Blueprint: Home & Catalog routes."""
from types import SimpleNamespace
from flask import Blueprint, render_template, jsonify
from app.domains.content.models import Category, Course, Lesson, LessonSection, Source
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
    return render_template("public/catalog.html", categories=categories)


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

