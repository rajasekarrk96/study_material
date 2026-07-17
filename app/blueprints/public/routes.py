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


@public_bp.route("/api/v1/stats")
def stats():
    return jsonify({
        "courses": Course.query.filter_by(is_deleted=False).count(),
        "lessons": Lesson.query.filter_by(is_deleted=False).count(),
        "topics": LessonSection.query.count(),
        "sources": Source.query.count()
    })

