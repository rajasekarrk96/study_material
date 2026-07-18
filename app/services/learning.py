"""
Learning OS — Learning & Progression Service Layer
EventService, XPService, StreakService, LearningProgressService, RecommendationService, DashboardService.
"""
from datetime import datetime, date, timedelta
from sqlalchemy import func
from app.core.extensions import db
from app.domains.content.models import Course, Module, Lesson, UserCertificate, LabSubmission, Certificate, Lab
from app.domains.learning_path.models import UserLessonProgress, UserCourseProgress
from app.domains.gamification.models import UserXPLog, UserStreak
from app.domains.assessment.models import Quiz, QuizAttempt


class EventService:
    """Synchronous publish/subscribe event manager."""
    _listeners = {}

    @classmethod
    def subscribe(cls, event_type: str, listener_fn):
        if event_type not in cls._listeners:
            cls._listeners[event_type] = []
        cls._listeners[event_type].append(listener_fn)

    @classmethod
    def publish(cls, event_type: str, *args, **kwargs):
        if event_type in cls._listeners:
            for listener in cls._listeners[event_type]:
                listener(*args, **kwargs)


class XPService:
    @staticmethod
    def award(user_id: int, activity_type: str, xp_amount: int, reference_id: int = None) -> UserXPLog:
        """Award XP to a user and log the event."""
        # Prevent double-awarding XP for completing the same lesson
        if activity_type == "lesson_completed" and reference_id:
            existing = UserXPLog.query.filter_by(
                user_id=user_id,
                activity_type=activity_type,
                reference_id=reference_id
            ).first()
            if existing:
                return existing

        log = UserXPLog(
            user_id=user_id,
            xp_amount=xp_amount,
            activity_type=activity_type,
            reference_id=reference_id,
            created_at=datetime.utcnow()
        )
        db.session.add(log)
        return log


class StreakService:
    @staticmethod
    def update_streak(user_id: int) -> UserStreak:
        """Increment or reset user's daily streak log."""
        streak = UserStreak.query.filter_by(user_id=user_id).first()
        today = date.today()
        if not streak:
            streak = UserStreak(
                user_id=user_id,
                current_streak=1,
                longest_streak=1,
                last_activity_date=today
            )
            db.session.add(streak)
            return streak

        if streak.last_activity_date == today:
            return streak
        elif streak.last_activity_date == today - timedelta(days=1):
            streak.current_streak += 1
            streak.last_activity_date = today
            if streak.current_streak > streak.longest_streak:
                streak.longest_streak = streak.current_streak
        else:
            streak.current_streak = 1
            streak.last_activity_date = today

        return streak


class LearningProgressService:
    @staticmethod
    def complete_lesson(user_id: int, lesson_id: int) -> UserLessonProgress:
        """Mark a lesson completed and publish completion event."""
        lesson = Lesson.query.get(lesson_id)
        if not lesson:
            return None

        progress = UserLessonProgress.query.filter_by(
            user_id=user_id,
            lesson_id=lesson_id
        ).first()

        if not progress:
            progress = UserLessonProgress(
                user_id=user_id,
                lesson_id=lesson_id,
                is_completed=True,
                completed_at=datetime.utcnow()
            )
            db.session.add(progress)
        elif not progress.is_completed:
            progress.is_completed = True
            progress.completed_at = datetime.utcnow()

        db.session.flush()

        # Publish progression event
        EventService.publish("lesson_completed", user_id=user_id, lesson_id=lesson_id)

        return progress

    @staticmethod
    def update_course_progress(user_id: int, course_id: int) -> UserCourseProgress:
        """Recalculate course completion progress and write update."""
        all_lessons = Lesson.query.join(Module).filter(
            Module.course_id == course_id,
            Lesson.status == "published",
            Lesson.is_deleted == False
        ).all()

        if not all_lessons:
            return None

        lesson_ids = [l.id for l in all_lessons]
        completed_count = UserLessonProgress.query.filter(
            UserLessonProgress.user_id == user_id,
            UserLessonProgress.lesson_id.in_(lesson_ids),
            UserLessonProgress.is_completed == True
        ).count()

        is_all_completed = (completed_count == len(all_lessons))

        course_progress = UserCourseProgress.query.filter_by(
            user_id=user_id,
            course_id=course_id
        ).first()

        newly_completed = False
        if not course_progress:
            course_progress = UserCourseProgress(
                user_id=user_id,
                course_id=course_id,
                is_completed=is_all_completed,
                completed_at=datetime.utcnow() if is_all_completed else None
            )
            db.session.add(course_progress)
            if is_all_completed:
                newly_completed = True
        else:
            if is_all_completed and not course_progress.is_completed:
                newly_completed = True
            course_progress.is_completed = is_all_completed
            if is_all_completed and not course_progress.completed_at:
                course_progress.completed_at = datetime.utcnow()

        db.session.flush()

        if newly_completed:
            EventService.publish("course_completed", user_id=user_id, course_id=course_id)

        return course_progress


class CertificateService:
    @staticmethod
    def _get_serializer():
        from itsdangerous import URLSafeSerializer
        from flask import current_app
        secret = "fallback-secret-key"
        try:
            if current_app and current_app.config.get("SECRET_KEY"):
                secret = current_app.config["SECRET_KEY"]
        except RuntimeError:
            pass
        return URLSafeSerializer(secret, salt="certificate-verification")

    @staticmethod
    def generate_verification_hash(user_cert_id: int) -> str:
        """Generate a secure, verifiable token/hash from the user certificate ID."""
        serializer = CertificateService._get_serializer()
        return serializer.dumps(user_cert_id)

    @staticmethod
    def verify_certificate_hash(hash_str: str) -> UserCertificate:
        """Decode and verify a certificate hash, returning the UserCertificate if valid."""
        serializer = CertificateService._get_serializer()
        try:
            user_cert_id = serializer.loads(hash_str)
            return db.session.get(UserCertificate, user_cert_id)
        except Exception:
            return None

    @staticmethod
    def get_user_certificates(user_id: int) -> list[UserCertificate]:
        """Fetch all earned certificates for a user."""
        return UserCertificate.query.filter_by(user_id=user_id).order_by(UserCertificate.issued_at.desc()).all()

    @staticmethod
    def check_and_award_certificate(user_id: int, course_id: int) -> UserCertificate:
        """Check if user has finished the course and award certificate if configured."""
        cert = Certificate.query.filter_by(course_id=course_id).first()
        if not cert:
            return None

        # Check if already awarded
        existing = UserCertificate.query.filter_by(
            user_id=user_id,
            certificate_id=cert.id
        ).first()
        if existing:
            return existing

        # Verify the course progress is actually 100% completed
        progress = UserCourseProgress.query.filter_by(
            user_id=user_id,
            course_id=course_id,
            is_completed=True
        ).first()
        if not progress:
            return None

        # Award the certificate
        user_cert = UserCertificate(
            user_id=user_id,
            certificate_id=cert.id,
            issued_at=datetime.utcnow()
        )
        db.session.add(user_cert)
        db.session.commit()
        return user_cert


class RecommendationService:
    """Core personalization and suggestion engine."""
    @staticmethod
    def get_resume_recommendation(user_id: int) -> dict:
        """Find the next lesson the user should resume."""
        completed_lessons = UserLessonProgress.query.filter_by(
            user_id=user_id,
            is_completed=True
        ).all()
        completed_lesson_ids = [lp.lesson_id for lp in completed_lessons]

        # Fetch latest completed lesson's course as active course
        if completed_lessons:
            # Get latest completion record
            latest_completion = sorted(completed_lessons, key=lambda lp: lp.completed_at or datetime.min)[-1]
            latest_lesson = db.session.get(Lesson, latest_completion.lesson_id)
            if latest_lesson and latest_lesson.module:
                course = latest_lesson.module.course
                if course and not course.is_deleted:
                    # Find first uncompleted lesson in this course
                    total_course_lessons = Lesson.query.join(Module).filter(
                        Module.course_id == course.id,
                        Lesson.status == "published",
                        Lesson.is_deleted == False
                    ).all()
                    
                    uncompleted_lessons = [l for l in total_course_lessons if l.id not in completed_lesson_ids]
                    if uncompleted_lessons:
                        uncompleted_lessons_sorted = sorted(
                            uncompleted_lessons,
                            key=lambda l: (l.module.sort_order if l.module else 0, l.sort_order)
                        )
                        next_lesson = uncompleted_lessons_sorted[0]
                        return {
                            "title": course.title,
                            "slug": course.slug,
                            "next_lesson": {
                                "title": next_lesson.title,
                                "slug": next_lesson.slug,
                                "module_slug": next_lesson.module.slug
                            }
                        }

        # Fallback: Default to Git Fundamentals first lesson
        git_course = Course.query.filter_by(slug="git-fundamentals", is_deleted=False).first()
        if git_course:
            first_lesson = Lesson.query.join(Module).filter(
                Module.course_id == git_course.id,
                Lesson.status == "published",
                Lesson.is_deleted == False
            ).order_by(Module.sort_order, Lesson.sort_order).first()
            if first_lesson:
                return {
                    "title": git_course.title,
                    "slug": git_course.slug,
                    "next_lesson": {
                        "title": first_lesson.title,
                        "slug": first_lesson.slug,
                        "module_slug": first_lesson.module.slug
                    }
                }
        return None

    @staticmethod
    def get_suggested_lab(user_id: int) -> dict:
        """Find the next uncompleted lab in the user's active course."""
        # Find active course based on last completed lesson
        completed_lessons = UserLessonProgress.query.filter_by(
            user_id=user_id,
            is_completed=True
        ).all()
        
        active_course_id = None
        if completed_lessons:
            latest_completion = sorted(completed_lessons, key=lambda lp: lp.completed_at or datetime.min)[-1]
            latest_lesson = db.session.get(Lesson, latest_completion.lesson_id)
            if latest_lesson and latest_lesson.module:
                active_course_id = latest_lesson.module.course_id
        
        if not active_course_id:
            git_course = Course.query.filter_by(slug="git-fundamentals", is_deleted=False).first()
            if git_course:
                active_course_id = git_course.id
                
        if not active_course_id:
            return None
            
        # Get all labs in this course
        labs = Lab.query.join(Lesson).join(Module).filter(
            Module.course_id == active_course_id,
            Lesson.is_deleted == False
        ).all()
        
        if not labs:
            return None
            
        # Filter completed labs
        passed_submissions = LabSubmission.query.filter_by(
            user_id=user_id,
            status="passed"
        ).all()
        passed_lab_ids = [s.lab_id for s in passed_submissions]
        
        uncompleted_labs = [lab for lab in labs if lab.id not in passed_lab_ids]
        if uncompleted_labs:
            # Sort by lesson sort order
            uncompleted_labs_sorted = sorted(
                uncompleted_labs,
                key=lambda l: (l.lesson.module.sort_order if l.lesson.module else 0, l.lesson.sort_order)
            )
            suggested = uncompleted_labs_sorted[0]
            return {
                "id": suggested.id,
                "title": suggested.title,
                "description": suggested.description,
                "estimated_minutes": suggested.estimated_minutes,
                "lesson": {
                    "title": suggested.lesson.title,
                    "slug": suggested.lesson.slug,
                    "module_slug": suggested.lesson.module.slug,
                    "course_slug": suggested.lesson.module.course.slug
                }
            }
        return None

    @staticmethod
    def get_suggested_review(user_id: int) -> dict:
        """Find a review topic based on weak quiz attempts or older completed lessons."""
        # 1. Look for sub-100% quiz attempts
        weak_attempt = QuizAttempt.query.filter(
            QuizAttempt.user_id == user_id,
            QuizAttempt.score < 100
        ).order_by(QuizAttempt.completed_at.desc()).first()
        
        if weak_attempt:
            quiz = db.session.get(Quiz, weak_attempt.quiz_id)
            if quiz and quiz.lesson_id:
                lesson = db.session.get(Lesson, quiz.lesson_id)
                if lesson and lesson.module and lesson.module.course:
                    return {
                        "reason": f"Strengthen skills in this lesson (Last Quiz Score: {weak_attempt.score}%)",
                        "lesson_title": lesson.title,
                        "lesson_slug": lesson.slug,
                        "module_slug": lesson.module.slug,
                        "course_slug": lesson.module.course.slug
                    }
                
        # 2. Look for lessons completed more than 7 days ago
        seven_days_ago = datetime.utcnow() - timedelta(days=7)
        old_progress = UserLessonProgress.query.filter(
            UserLessonProgress.user_id == user_id,
            UserLessonProgress.is_completed == True,
            UserLessonProgress.completed_at < seven_days_ago
        ).order_by(UserLessonProgress.completed_at.asc()).first()
        
        if old_progress:
            lesson = db.session.get(Lesson, old_progress.lesson_id)
            if lesson and lesson.module and lesson.module.course:
                return {
                    "reason": "Spaced repetition review: refresh your memory on this topic.",
                    "lesson_title": lesson.title,
                    "lesson_slug": lesson.slug,
                    "module_slug": lesson.module.slug,
                    "course_slug": lesson.module.course.slug
                }
        return None

    @staticmethod
    def get_recommended_next_course(user_id: int) -> dict:
        """Suggest the next course for the user to start once they finish the active one."""
        completed_course_progress = UserCourseProgress.query.filter_by(
            user_id=user_id,
            is_completed=True
        ).all()
        completed_course_ids = [cp.course_id for cp in completed_course_progress]
        
        # Get all published courses
        all_courses = Course.query.filter_by(status="published", is_deleted=False).order_by(Course.id).all()
        
        for course in all_courses:
            if course.id not in completed_course_ids:
                return {
                    "id": course.id,
                    "title": course.title,
                    "slug": course.slug,
                    "description": course.description
                }
        return None


class DashboardService:
    @staticmethod
    def get_dashboard_data(user_id: int) -> dict:
        """Fetch and aggregate dashboard statistics for the logged-in learner."""
        # 1. Total XP
        total_xp = db.session.query(func.sum(UserXPLog.xp_amount)).filter(
            UserXPLog.user_id == user_id
        ).scalar() or 0

        # 2. Daily Streak
        streak_record = UserStreak.query.filter_by(user_id=user_id).first()
        streak = streak_record.current_streak if streak_record else 0

        # 3. Active Courses
        completed_lessons = UserLessonProgress.query.filter_by(
            user_id=user_id,
            is_completed=True
        ).all()

        completed_lesson_ids = [lp.lesson_id for lp in completed_lessons]
        active_courses = []

        if completed_lesson_ids:
            lessons = Lesson.query.filter(Lesson.id.in_(completed_lesson_ids)).all()
            active_course_ids = list(set([l.module.course_id for l in lessons if l.module]))
            
            for cid in active_course_ids:
                course = db.session.get(Course, cid)
                if not course or course.is_deleted:
                    continue

                total_course_lessons = Lesson.query.join(Module).filter(
                    Module.course_id == cid,
                    Lesson.status == "published",
                    Lesson.is_deleted == False
                ).all()
                total_count = len(total_course_lessons)
                if total_count == 0:
                    continue

                course_completed_ids = [l.id for l in total_course_lessons if l.id in completed_lesson_ids]
                completed_count = len(course_completed_ids)
                progress_percentage = int((completed_count / total_count) * 100)

                uncompleted_lessons = [l for l in total_course_lessons if l.id not in completed_lesson_ids]
                est_minutes_remaining = sum([l.estimated_minutes or 15 for l in uncompleted_lessons])
                est_hours_remaining = round(est_minutes_remaining / 60, 1)

                next_lesson = None
                if uncompleted_lessons:
                    uncompleted_lessons_sorted = sorted(
                        uncompleted_lessons,
                        key=lambda l: (l.module.sort_order if l.module else 0, l.sort_order)
                    )
                    next_lesson = uncompleted_lessons_sorted[0]

                active_courses.append({
                    "id": course.id,
                    "title": course.title,
                    "slug": course.slug,
                    "thumbnail_url": course.thumbnail_url or "/static/img/course-placeholder.jpg",
                    "progress_percentage": progress_percentage,
                    "completed_count": completed_count,
                    "total_count": total_count,
                    "est_hours_remaining": est_hours_remaining,
                    "next_lesson": {
                        "title": next_lesson.title,
                        "slug": next_lesson.slug,
                        "module_slug": next_lesson.module.slug
                    } if next_lesson else None
                })

        # 4. Global Counts & Earned Certificates
        certificates_count = UserCertificate.query.filter_by(user_id=user_id).count()
        earned_certificates = UserCertificate.query.filter_by(user_id=user_id).order_by(UserCertificate.issued_at.desc()).limit(3).all()
        completed_labs_count = LabSubmission.query.filter_by(
            user_id=user_id,
            status="passed"
        ).count()

        # 5. Normalized Recent Activity Feed
        recent_xp_logs = UserXPLog.query.filter_by(user_id=user_id).order_by(
            UserXPLog.created_at.desc()
        ).limit(5).all()

        activity_feed = []
        for log in recent_xp_logs:
            title = ""
            icon = "star"
            if log.activity_type == "lesson_completed":
                lesson = db.session.get(Lesson, log.reference_id)
                title = f"Completed: {lesson.title}" if lesson else "Completed a lesson"
                icon = "check-circle"
            elif log.activity_type == "quiz_completed":
                title = "Passed a quiz"
                icon = "award"
            elif log.activity_type == "exercise_solved":
                title = "Solved coding exercise"
                icon = "code"
            elif log.activity_type == "lab_completed":
                lab = db.session.get(Lab, log.reference_id)
                title = f"Completed Lab: {lab.title}" if lab else "Completed interactive lab"
                icon = "flask"
            else:
                title = log.activity_type.replace("_", " ").title()

            activity_feed.append({
                "title": title,
                "icon": icon,
                "time": log.created_at.strftime("%b %d, %Y"),
                "xp": log.xp_amount
            })

        # 6. Retrieve Recommendations
        resume_recommendation = RecommendationService.get_resume_recommendation(user_id)
        suggested_lab = RecommendationService.get_suggested_lab(user_id)
        suggested_review = RecommendationService.get_suggested_review(user_id)
        recommended_next_course = RecommendationService.get_recommended_next_course(user_id)

        return {
            "total_xp": total_xp,
            "streak": streak,
            "active_courses": active_courses,
            "certificates_count": certificates_count,
            "earned_certificates": earned_certificates,
            "completed_labs_count": completed_labs_count,
            "activity_feed": activity_feed,
            "default_course": resume_recommendation,
            "resume_recommendation": resume_recommendation,
            "suggested_lab": suggested_lab,
            "suggested_review": suggested_review,
            "recommended_next_course": recommended_next_course
        }


# ==========================================
# EVENT HANDLERS REGISTRATION
# ==========================================
def _on_lesson_completed_award_xp(user_id: int, lesson_id: int):
    XPService.award(user_id, "lesson_completed", 10, reference_id=lesson_id)


def _on_lesson_completed_update_streak(user_id: int, lesson_id: int):
    StreakService.update_streak(user_id)


def _on_lesson_completed_course_progress(user_id: int, lesson_id: int):
    lesson = db.session.get(Lesson, lesson_id)
    if lesson and lesson.module:
        course = lesson.module.course
        if course:
            LearningProgressService.update_course_progress(user_id, course.id)


def _on_lab_completed_award_xp(user_id: int, lab_id: int):
    XPService.award(user_id, "lab_completed", 50, reference_id=lab_id)


def _on_lab_completed_update_streak(user_id: int, lab_id: int):
    StreakService.update_streak(user_id)


def _on_quiz_completed_award_xp(user_id: int, quiz_id: int, xp_reward: int, score: int):
    if xp_reward > 0:
        XPService.award(user_id, "quiz_completed", xp_reward, reference_id=quiz_id)


def _on_quiz_completed_update_streak(user_id: int, quiz_id: int, xp_reward: int, score: int):
    StreakService.update_streak(user_id)


def _on_course_completed_award_cert(user_id: int, course_id: int):
    CertificateService.check_and_award_certificate(user_id, course_id)


EventService.subscribe("lesson_completed", _on_lesson_completed_award_xp)
EventService.subscribe("lesson_completed", _on_lesson_completed_update_streak)
EventService.subscribe("lesson_completed", _on_lesson_completed_course_progress)
EventService.subscribe("lab_completed", _on_lab_completed_award_xp)
EventService.subscribe("lab_completed", _on_lab_completed_update_streak)
EventService.subscribe("quiz_completed", _on_quiz_completed_award_xp)
EventService.subscribe("quiz_completed", _on_quiz_completed_update_streak)
EventService.subscribe("course_completed", _on_course_completed_award_cert)
