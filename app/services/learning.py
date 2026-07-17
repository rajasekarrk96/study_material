"""
Learning OS — Learning & Progression Service Layer
XPService, StreakService, LearningProgressService, DashboardService.
"""
from datetime import datetime, date, timedelta
from sqlalchemy import func
from app.core.extensions import db
from app.domains.content.models import Course, Module, Lesson, UserCertificate, LabSubmission
from app.domains.learning_path.models import UserLessonProgress, UserCourseProgress
from app.domains.gamification.models import UserXPLog, UserStreak

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
        """Mark a lesson completed, award XP, update streak, check course completion."""
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

        # Award XP and log activity
        XPService.award(user_id, "lesson_completed", 10, reference_id=lesson_id)

        # Update Streak
        StreakService.update_streak(user_id)

        # Check course completion
        if lesson.module:
            course = lesson.module.course
            if course:
                LearningProgressService.update_course_progress(user_id, course.id)

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

        if not course_progress:
            course_progress = UserCourseProgress(
                user_id=user_id,
                course_id=course_id,
                is_completed=is_all_completed,
                completed_at=datetime.utcnow() if is_all_completed else None
            )
            db.session.add(course_progress)
        else:
            course_progress.is_completed = is_all_completed
            if is_all_completed and not course_progress.completed_at:
                course_progress.completed_at = datetime.utcnow()

        return course_progress


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

        # 3. Active Courses & Next Resume Lessons
        completed_lessons = UserLessonProgress.query.filter_by(
            user_id=user_id,
            is_completed=True
        ).all()

        completed_lesson_ids = [lp.lesson_id for lp in completed_lessons]
        active_courses = []

        # Find active course enrollments
        if completed_lesson_ids:
            lessons = Lesson.query.filter(Lesson.id.in_(completed_lesson_ids)).all()
            active_course_ids = list(set([l.module.course_id for l in lessons if l.module]))
            
            for cid in active_course_ids:
                course = Course.query.get(cid)
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

        # 4. Global Counts
        certificates_count = UserCertificate.query.filter_by(user_id=user_id).count()
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
                lesson = Lesson.query.get(log.reference_id)
                title = f"Completed: {lesson.title}" if lesson else "Completed a lesson"
                icon = "check-circle"
            elif log.activity_type == "quiz_completed":
                title = "Passed a quiz"
                icon = "award"
            elif log.activity_type == "exercise_solved":
                title = "Solved coding exercise"
                icon = "code"
            else:
                title = log.activity_type.replace("_", " ").title()

            activity_feed.append({
                "title": title,
                "icon": icon,
                "time": log.created_at.strftime("%b %d, %Y"),
                "xp": log.xp_amount
            })

        # Provide a default active course if none started yet
        default_course = None
        if not active_courses:
            git_course = Course.query.filter_by(slug="git-fundamentals", is_deleted=False).first()
            if git_course:
                first_lesson = Lesson.query.join(Module).filter(
                    Module.course_id == git_course.id,
                    Lesson.status == "published",
                    Lesson.is_deleted == False
                ).order_by(Module.sort_order, Lesson.sort_order).first()
                if first_lesson:
                    default_course = {
                        "title": git_course.title,
                        "slug": git_course.slug,
                        "next_lesson": {
                            "title": first_lesson.title,
                            "slug": first_lesson.slug,
                            "module_slug": first_lesson.module.slug
                        }
                    }

        return {
            "total_xp": total_xp,
            "streak": streak,
            "active_courses": active_courses,
            "certificates_count": certificates_count,
            "completed_labs_count": completed_labs_count,
            "activity_feed": activity_feed,
            "default_course": default_course
        }
