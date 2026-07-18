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
    from app.domains.auth.models import Role, User
    
    stats = {
        "total_subjects": Subject.query.count(),
        "total_courses": Course.query.count(),
        "total_lessons": Lesson.query.count(),
    }
    
    # Get latest lessons with their quality scores
    lessons = Lesson.query.order_by(Lesson.id.desc()).limit(10).all()
    
    # Calculate Course Lesson Counts for Chart
    courses = Course.query.filter_by(is_deleted=False).all()
    course_labels = [c.title for c in courses]
    from app.domains.content.models import Module
    course_lesson_counts = [
        Lesson.query.join(Module).filter(Module.course_id == c.id, Lesson.is_deleted == False).count()
        for c in courses
    ]
    
    # Calculate Role distribution
    roles = Role.query.all()
    role_labels = []
    role_counts = []
    for r in roles:
        cnt = User.query.filter_by(role_id=r.id).count()
        if cnt > 0:
            role_labels.append(r.display_name)
            role_counts.append(cnt)
            
    return render_template(
        "admin/dashboard.html",
        stats=stats,
        lessons=lessons,
        course_labels=course_labels,
        course_lesson_counts=course_lesson_counts,
        role_labels=role_labels,
        role_counts=role_counts
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


from app.domains.auth.models import User, Role

@admin_bp.route("/users")
@login_required
@require_min_role("admin")
def users_list():
    """Retrieve and display a list of all users and their respective roles."""
    users = User.query.order_by(User.id.asc()).all()
    roles = Role.query.order_by(Role.level.asc()).all()
    return render_template("admin/users.html", users=users, roles=roles)


@admin_bp.route("/users/<int:user_id>/role", methods=["POST"])
@login_required
@require_min_role("admin")
def update_user_role(user_id: int):
    """Update a user's assigned RBAC role."""
    user = db.session.get(User, user_id)
    if not user:
        flash("User not found.", "error")
        return redirect(url_for("admin.users_list"))
        
    role_id = request.form.get("role_id")
    if role_id:
        user.role_id = int(role_id)
        db.session.commit()
        flash(f"Successfully updated role for {user.username}.", "success")
    else:
        flash("Invalid role ID.", "error")
        
    return redirect(url_for("admin.users_list"))


@admin_bp.route("/review-queue")
@login_required
@require_min_role("reviewer")
def review_queue():
    """Retrieve and display the list of lessons pending draft review."""
    lessons = Lesson.query.filter_by(status="review", is_deleted=False).all()
    return render_template("admin/review_queue.html", lessons=lessons)


@admin_bp.route("/review-queue/<int:lesson_id>/status", methods=["POST"])
@login_required
@require_min_role("reviewer")
def process_review(lesson_id: int):
    """Approve (publish) or reject a lesson draft in the review queue."""
    lesson = db.session.get(Lesson, lesson_id)
    if not lesson:
        flash("Lesson not found.", "error")
        return redirect(url_for("admin.review_queue"))
        
    action = request.form.get("action")
    if action == "approve":
        lesson.status = "published"
        db.session.commit()
        # Also rebuild search index since new content has been published!
        from app.services.search_service import SearchIndexService
        SearchIndexService.rebuild_search_index()
        flash(f"Draft '{lesson.title}' has been successfully approved and published!", "success")
    elif action == "reject":
        lesson.status = "draft"
        db.session.commit()
        flash(f"Draft '{lesson.title}' rejected and sent back to author drafts.", "warning")
    else:
        flash("Invalid review action.", "error")
        
    return redirect(url_for("admin.review_queue"))
