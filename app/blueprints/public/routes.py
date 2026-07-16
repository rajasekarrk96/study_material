"""Learning OS — Public Blueprint: Home & Catalog routes."""
from flask import Blueprint, render_template, jsonify
from app.domains.content.models import Category, Course, Lesson, LessonSection, Source

public_bp = Blueprint("public", __name__, template_folder="templates")


@public_bp.route("/")
def home():
    categories = Category.query.filter_by(is_active=True).order_by(Category.sort_order).all()
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
    categories = Category.query.filter_by(is_active=True).all()
    return render_template("public/catalog.html", categories=categories)


@public_bp.route("/api/v1/stats")
def stats():
    return jsonify({
        "courses": Course.query.filter_by(is_deleted=False).count(),
        "lessons": Lesson.query.filter_by(is_deleted=False).count(),
        "topics": LessonSection.query.count(),
        "sources": Source.query.count()
    })

