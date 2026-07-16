"""Learning OS — Learn Blueprint: Course, Module, Lesson viewer routes."""
from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user
from app.domains.content.models import Course, Module, Lesson, LessonSection
from app.domains.learning_path.models import PathPrerequisite, UserCourseProgress

learn_bp = Blueprint("learn", __name__, template_folder="templates")


def _verify_course_prerequisites(course_id: int):
    """Aborts if the user hasn't completed all prerequisite courses."""
    prereqs = PathPrerequisite.query.filter_by(course_id=course_id).all()
    for p in prereqs:
        completed = UserCourseProgress.query.filter_by(
            user_id=current_user.id,
            course_id=p.prerequisite_course_id,
            is_completed=True
        ).first()
        if not completed:
            abort(403, f"Prerequisites not met. You must first complete the prerequisite course: {p.prerequisite.title}")


@learn_bp.route("/<course_slug>/")
@login_required
def course_overview(course_slug: str):
    course = Course.query.filter_by(slug=course_slug, is_deleted=False).first_or_404()
    
    # Check prerequisites
    _verify_course_prerequisites(course.id)

    modules = course.modules.filter_by(is_published=True).order_by(Module.sort_order).all()
    return render_template("learn/course_overview.html", course=course, modules=modules)


@learn_bp.route("/<course_slug>/<module_slug>/<lesson_slug>/")
@login_required
def lesson_view(course_slug: str, module_slug: str, lesson_slug: str):
    course = Course.query.filter_by(slug=course_slug, is_deleted=False).first_or_404()
    
    # Check prerequisites
    _verify_course_prerequisites(course.id)

    module = Module.query.filter_by(course_id=course.id, slug=module_slug).first_or_404()
    lesson = Lesson.query.filter_by(
        module_id=module.id, slug=lesson_slug, is_deleted=False
    ).first_or_404()

    # Increment view count
    lesson.view_count = (lesson.view_count or 0) + 1
    from app.core.extensions import db
    db.session.commit()

    sections = {s.section_type: s for s in lesson.sections if s.is_visible}
    return render_template(
        "learn/lesson.html",
        course=course,
        module=module,
        lesson=lesson,
        sections=sections,
    )

