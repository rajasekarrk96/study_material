"""
Learning OS — Admin & Enterprise CMS Blueprint.
Handles content ingestion, quality checks, analytics metrics, and dashboard management.
"""
from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request
from flask_login import login_required
from app.core.decorators import require_min_role
from app.core.extensions import db
from app.domains.content.models import Lesson, Course, Subject
from app.domains.content.quality import run_quality_check, calculate_flesch_reading_ease
from app.domains.learning_path.models import UserCourseProgress

admin_bp = Blueprint("admin", __name__, url_prefix="/admin", template_folder="templates")


@admin_bp.route("/")
@login_required
@require_min_role("admin")
def dashboard():
    """Main administrative dashboard view."""
    stats = {
        "total_subjects": Subject.query.count(),
        "total_courses": Course.query.count(),
        "total_lessons": Lesson.query.count(),
    }
    
    # Get latest lessons with their quality scores
    lessons = Lesson.query.order_by(Lesson.id.desc()).limit(10).all()
    
    return render_template(
        "admin/dashboard.html",
        stats=stats,
        lessons=lessons
    )


@admin_bp.route("/lessons/<int:lesson_id>/quality", methods=["POST"])
@login_required
@require_min_role("admin")
def trigger_quality_check(lesson_id: int):
    """Triggers and calculates Flesch readability analysis for a lesson."""
    try:
        score = run_quality_check(lesson_id)
        return jsonify({
            "status": "success",
            "readability_score": score.readability_score,
            "plagiarism_percentage": score.plagiarism_percentage,
            "feedback": score.automated_feedback
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400
