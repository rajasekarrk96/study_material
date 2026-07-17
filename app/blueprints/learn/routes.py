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

    # Check completion
    from app.domains.learning_path.models import UserLessonProgress
    progress = UserLessonProgress.query.filter_by(
        user_id=current_user.id,
        lesson_id=lesson.id,
        is_completed=True
    ).first()
    is_completed = (progress is not None)

    # Next lesson lookup
    all_lessons = Lesson.query.join(Module).filter(
        Module.course_id == course.id,
        Lesson.status == "published",
        Lesson.is_deleted == False
    ).all()
    sorted_lessons = sorted(
        all_lessons,
        key=lambda l: (l.module.sort_order if l.module else 0, l.sort_order)
    )
    next_lesson = None
    for i, l in enumerate(sorted_lessons):
        if l.id == lesson.id and i + 1 < len(sorted_lessons):
            next_lesson = sorted_lessons[i + 1]
            break

    sections = {s.section_type: s for s in lesson.sections if s.is_visible}
    return render_template(
        "learn/lesson.html",
        course=course,
        module=module,
        lesson=lesson,
        sections=sections,
        is_completed=is_completed,
        next_lesson=next_lesson
    )


from flask import redirect, url_for, flash
from app.services.learning import LearningProgressService

@learn_bp.route("/lessons/<int:lesson_id>/complete", methods=["POST"])
@login_required
def complete_lesson(lesson_id: int):
    lesson = Lesson.query.get_or_404(lesson_id)
    LearningProgressService.complete_lesson(current_user.id, lesson.id)

    course = lesson.module.course
    all_lessons = Lesson.query.join(Module).filter(
        Module.course_id == course.id,
        Lesson.status == "published",
        Lesson.is_deleted == False
    ).all()
    sorted_lessons = sorted(
        all_lessons,
        key=lambda l: (l.module.sort_order if l.module else 0, l.sort_order)
    )
    
    next_lesson = None
    for i, l in enumerate(sorted_lessons):
        if l.id == lesson.id and i + 1 < len(sorted_lessons):
            next_lesson = sorted_lessons[i + 1]
            break

    flash("Lesson completed! +10 XP awarded.", "success")

    if next_lesson:
        return redirect(url_for("learn.lesson_view", 
                               course_slug=course.slug,
                               module_slug=next_lesson.module.slug,
                               lesson_slug=next_lesson.slug))
    else:
        return redirect(url_for("learn.course_overview", course_slug=course.slug))

