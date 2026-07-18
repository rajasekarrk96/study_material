from flask import Blueprint, render_template, abort, jsonify, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.domains.content.models import Course, Module, Lesson, LessonSection, Lab, LabStep, LabSubmission, UserCertificate
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

    # Calculate progress for current user
    completed_lesson_ids = set()
    next_lesson = None
    progress_percentage = 0
    total_lessons_count = 0
    completed_lessons_count = 0
    
    # Query all published, non-deleted lessons in this course
    all_lessons = Lesson.query.join(Module).filter(
        Module.course_id == course.id,
        Lesson.status == "published",
        Lesson.is_deleted == False
    ).order_by(Module.sort_order, Lesson.sort_order).all()
    
    total_lessons_count = len(all_lessons)
    
    from app.domains.learning_path.models import UserLessonProgress
    from app.domains.assessment.models import Quiz
    
    if current_user.is_authenticated:
        completed_lessons = UserLessonProgress.query.filter(
            UserLessonProgress.user_id == current_user.id,
            UserLessonProgress.is_completed == True,
            UserLessonProgress.lesson_id.in_([l.id for l in all_lessons])
        ).all() if all_lessons else []
        completed_lesson_ids = {lp.lesson_id for lp in completed_lessons}
        completed_lessons_count = len(completed_lesson_ids)
        if total_lessons_count > 0:
            progress_percentage = int((completed_lessons_count / total_lessons_count) * 100)
            
        # Find next lesson (first lesson that is not completed)
        for l in all_lessons:
            if l.id not in completed_lesson_ids:
                next_lesson = l
                break
    else:
        if all_lessons:
            next_lesson = all_lessons[0]
            
    # Calculate additional metrics
    labs_count = Lab.query.join(Lesson).join(Module).filter(
        Module.course_id == course.id,
        Lesson.status == "published",
        Lesson.is_deleted == False
    ).count()
    
    quizzes_count = Quiz.query.join(Lesson).join(Module).filter(
        Module.course_id == course.id,
        Lesson.status == "published",
        Lesson.is_deleted == False
    ).count()

    return render_template(
        "learn/course_overview.html",
        course=course,
        modules=modules,
        completed_lesson_ids=completed_lesson_ids,
        next_lesson=next_lesson,
        progress_percentage=progress_percentage,
        total_lessons_count=total_lessons_count,
        completed_lessons_count=completed_lessons_count,
        labs_count=labs_count,
        quizzes_count=quizzes_count
    )


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


from app.core.extensions import db
from app.services.learning import LearningProgressService
from app.services.lab import LabService

@learn_bp.route("/lessons/<int:lesson_id>/complete", methods=["POST"])
@login_required
def complete_lesson(lesson_id: int):
    lesson = db.session.get(Lesson, lesson_id)
    if not lesson:
        abort(404)
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


@learn_bp.route("/labs/<int:lab_id>/")
@login_required
def lab_view(lab_id: int):
    lab = LabService.get_lab(lab_id)
    if not lab:
        abort(404, "Lab not found")
        
    steps = LabStep.query.filter_by(lab_id=lab_id).order_by(LabStep.step_number).all()
    sub = LabService.get_submission(current_user.id, lab_id)
    
    completed_steps = []
    repo_path = ""
    if sub:
        completed_steps = sub.submission_data.get("completed_steps", [])
        repo_path = sub.submission_data.get("repo_path", "")

    course = None
    if lab.lesson and lab.lesson.module:
        course = lab.lesson.module.course

    return render_template(
        "learn/lab.html",
        lab=lab,
        steps=steps,
        completed_steps=completed_steps,
        repo_path=repo_path,
        submission=sub,
        course=course
    )


@learn_bp.route("/labs/<int:lab_id>/steps/<int:step_number>", methods=["POST"])
@login_required
def save_lab_step_progress(lab_id: int, step_number: int):
    data = request.get_json() or {}
    is_completed = data.get("completed", False)
    
    sub = LabService.submit_step_progress(
        user_id=current_user.id,
        lab_id=lab_id,
        step_number=step_number,
        is_completed=is_completed
    )
    
    return jsonify({
        "status": "success",
        "completed_steps": sub.submission_data.get("completed_steps", [])
    })


@learn_bp.route("/labs/<int:lab_id>/verify", methods=["POST"])
@login_required
def verify_lab(lab_id: int):
    data = request.get_json() or {}
    repo_path = data.get("repo_path", "").strip() or None
    
    sub = LabService.verify_and_grade_lab(
        user_id=current_user.id,
        lab_id=lab_id,
        repo_path=repo_path
    )
    
    if not sub:
        return jsonify({"status": "error", "message": "Lab or submission error"}), 400
        
    return jsonify({
        "status": sub.status,
        "feedback": sub.feedback,
        "completed_steps": sub.submission_data.get("completed_steps", [])
    })


from app.services.learning import CertificateService

@learn_bp.route("/certificates/")
@login_required
def certificate_list():
    user_certs = CertificateService.get_user_certificates(current_user.id)
    certs_data = []
    for uc in user_certs:
        certs_data.append({
            "record": uc,
            "hash": CertificateService.generate_verification_hash(uc.id)
        })
    return render_template(
        "learn/certificate_list.html",
        certificates=certs_data
    )


@learn_bp.route("/certificates/<int:user_cert_id>/")
@login_required
def certificate_detail(user_cert_id: int):
    user_cert = db.session.get(UserCertificate, user_cert_id)
    if not user_cert:
        abort(404, "Certificate not found")
    if user_cert.user_id != current_user.id:
        abort(403, "You do not have access to this certificate")
        
    verification_hash = CertificateService.generate_verification_hash(user_cert.id)
    return render_template(
        "learn/certificate_detail.html",
        user_cert=user_cert,
        verification_hash=verification_hash,
        public_view=False
    )


@learn_bp.route("/verify/certificate/<string:hash_str>")
def public_certificate_verify(hash_str: str):
    user_cert = CertificateService.verify_certificate_hash(hash_str)
    if not user_cert:
        return render_template("learn/certificate_verification_failed.html"), 404
        
    return render_template(
        "learn/certificate_detail.html",
        user_cert=user_cert,
        verification_hash=hash_str,
        public_view=True
    )


@learn_bp.route("/tutor/")
@login_required
def ai_tutor():
    """Renders the standalone AI Tutor workspace page."""
    return render_template("learn/tutor.html")

