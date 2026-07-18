"""
Learning OS — Quiz & Assessment Integration Tests
===================================================
Tests quiz creation, start attempt, submit answers, score calculation,
and correct XP reward checks.
"""
import os
os.environ["DATABASE_TYPE"] = "sqlite-test"

import unittest
from datetime import datetime
from app import create_app
from app.core.extensions import db
from app.domains.auth.models import User, Role
from app.domains.content.models import Category, Subject, Course, Module, Lesson
from app.domains.assessment.models import Quiz, Question, Option, QuizAttempt, QuizAnswer
from app.domains.gamification.models import UserXPLog
from app.domains.learning_path.models import UserCourseProgress, UserLessonProgress


class QuizEngineTestCase(unittest.TestCase):
    def setUp(self):
        # Configure app for testing in memory SQLite database
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.app.config["WTF_CSRF_ENABLED"] = False

        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()

        # Re-create database schema in memory
        db.create_all()

        # Seed data
        self._seed_test_data()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def _seed_test_data(self):
        # Create Student Role
        role = Role.query.filter_by(name="student").first()
        if not role:
            role = Role(name="student", display_name="Student", level=1)
            db.session.add(role)
            db.session.commit()

        # Create user
        self.user = User(
            email="tester@bytesandboards.test",
            username="tester",
            password_hash="fake-hash",
            role_id=role.id,
            display_name="Tester User"
        )
        db.session.add(self.user)

        # Create category, subject, course, module, lesson
        cat = Category(name="Tech", slug="tech")
        db.session.add(cat)
        db.session.flush()

        subj = Subject(category_id=cat.id, name="Python", slug="python")
        db.session.add(subj)
        db.session.flush()

        course = Course(subject_id=subj.id, title="Python 101", slug="python-101")
        db.session.add(course)
        db.session.flush()

        mod = Module(course_id=course.id, title="Basics", slug="basics")
        db.session.add(mod)
        db.session.flush()

        self.lesson = Lesson(module_id=mod.id, title="Variables", slug="variables")
        db.session.add(self.lesson)
        db.session.flush()

        # Create Quiz
        self.quiz = Quiz(
            lesson_id=self.lesson.id,
            title="Variables Basics Quiz",
            slug="variables-basics",
            description="Test your variable knowledge",
            passing_score=70,
            xp_reward=100
        )
        db.session.add(self.quiz)
        db.session.flush()

        # Create Question 1 (Multiple Choice)
        self.q1 = Question(
            quiz_id=self.quiz.id,
            question_text="What is the output of print(type(10))?",
            question_type="multiple_choice",
            points=10,
            sort_order=1
        )
        db.session.add(self.q1)
        db.session.flush()

        self.o1_1 = Option(question_id=self.q1.id, option_text="int", is_correct=True)
        self.o1_2 = Option(question_id=self.q1.id, option_text="str", is_correct=False)
        self.o1_3 = Option(question_id=self.q1.id, option_text="float", is_correct=False)
        db.session.add_all([self.o1_1, self.o1_2, self.o1_3])

        # Create Question 2 (True/False)
        self.q2 = Question(
            quiz_id=self.quiz.id,
            question_text="Variables in Python must be declared with a type.",
            question_type="true_false",
            points=10,
            sort_order=2
        )
        db.session.add(self.q2)
        db.session.flush()

        self.o2_1 = Option(question_id=self.q2.id, option_text="True", is_correct=False)
        self.o2_2 = Option(question_id=self.q2.id, option_text="False", is_correct=True)
        db.session.add_all([self.o2_1, self.o2_2])

        db.session.commit()

    def test_quiz_attempt_creation(self):
        # Mock active session
        with self.client.session_transaction() as sess:
            sess["_user_id"] = str(self.user.id)

        res = self.client.post(f"/api/v1/quizzes/{self.quiz.id}/attempts")
        self.assertEqual(res.status_code, 201)
        data = res.get_json()
        self.assertEqual(data["status"], "success")
        self.assertIn("attempt_id", data)

    def test_quiz_submission_success(self):
        # Create attempt
        attempt = QuizAttempt(user_id=self.user.id, quiz_id=self.quiz.id, started_at=datetime.utcnow())
        db.session.add(attempt)
        db.session.commit()

        # Mock active session
        with self.client.session_transaction() as sess:
            sess["_user_id"] = str(self.user.id)

        # Submit all correct answers
        payload = {
            "answers": [
                {"question_id": self.q1.id, "selected_option_id": self.o1_1.id},
                {"question_id": self.q2.id, "selected_option_id": self.o2_2.id}
            ]
        }
        res = self.client.post(f"/api/v1/quizzes/attempts/{attempt.id}/submit", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()

        self.assertTrue(data["is_passed"])
        self.assertEqual(data["score"], 100)
        self.assertEqual(data["xp_earned"], 100)

        # Check XP logs
        xp_log = UserXPLog.query.filter_by(user_id=self.user.id, activity_type="quiz_completed").first()
        self.assertIsNotNone(xp_log)
        self.assertEqual(xp_log.xp_amount, 100)

    def test_quiz_submission_failure(self):
        # Create attempt
        attempt = QuizAttempt(user_id=self.user.id, quiz_id=self.quiz.id, started_at=datetime.utcnow())
        db.session.add(attempt)
        db.session.commit()

        with self.client.session_transaction() as sess:
            sess["_user_id"] = str(self.user.id)

        # Submit wrong answers (0%)
        payload = {
            "answers": [
                {"question_id": self.q1.id, "selected_option_id": self.o1_2.id},
                {"question_id": self.q2.id, "selected_option_id": self.o2_1.id}
            ]
        }
        res = self.client.post(f"/api/v1/quizzes/attempts/{attempt.id}/submit", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()

        self.assertFalse(data["is_passed"])
        self.assertEqual(data["score"], 0)
        self.assertEqual(data["xp_earned"], 0)

        # Check no XP is logged
        xp_log = UserXPLog.query.filter_by(user_id=self.user.id, activity_type="quiz_completed").first()
        self.assertIsNone(xp_log)

    def test_sandbox_python_execution(self):
        from app.domains.sandbox.models import Exercise, ExerciseTestCase, ExerciseSubmission

        # Create coding exercise
        ex = Exercise(
            title="Addition Exercise",
            slug="addition",
            description="Write code that prints 5+10",
            programming_language="python",
            xp_reward=40
        )
        db.session.add(ex)
        db.session.flush()

        # Add test case
        tc = ExerciseTestCase(
            exercise_id=ex.id,
            input_data="",
            expected_output="15"
        )
        db.session.add(tc)
        db.session.commit()

        # Submit code that returns correct output
        payload = {"source_code": "print(5 + 10)"}
        with self.client.session_transaction() as sess:
            sess["_user_id"] = str(self.user.id)

        res = self.client.post(f"/api/v1/exercises/{ex.id}/submit", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["result_status"], "accepted")
        self.assertTrue(data["all_passed"])
        self.assertEqual(data["xp_earned"], 40)

        # Check database submission entry
        sub = ExerciseSubmission.query.filter_by(user_id=self.user.id, exercise_id=ex.id).first()
        self.assertIsNotNone(sub)
        self.assertEqual(sub.status, "accepted")

    def test_gamification_xp_cap(self):
        from app.domains.gamification.service import award_xp
        
        # Award 300 XP
        awarded1 = award_xp(self.user.id, 300, "manual_test")
        self.assertEqual(awarded1, 300)

        # Award 300 XP (should cap at remaining 200 XP)
        awarded2 = award_xp(self.user.id, 300, "manual_test")
        self.assertEqual(awarded2, 200)

        # Award 50 XP (should award 0)
        awarded3 = award_xp(self.user.id, 50, "manual_test")
        self.assertEqual(awarded3, 0)

    def test_level_progression(self):
        from app.domains.gamification.service import calculate_level
        self.assertEqual(calculate_level(0), 1)
        self.assertEqual(calculate_level(100), 2)    # 0.1 * 10 + 1 = 2
        self.assertEqual(calculate_level(400), 3)    # 0.1 * 20 + 1 = 3
        self.assertEqual(calculate_level(10000), 11)  # 0.1 * 100 + 1 = 11

    def test_streak_mechanics(self):
        from datetime import date, timedelta
        from app.domains.gamification.models import UserStreak
        from app.domains.gamification.service import update_streak

        # Initial streak calculation
        update_streak(self.user.id)
        streak = UserStreak.query.filter_by(user_id=self.user.id).first()
        self.assertIsNotNone(streak)
        self.assertEqual(streak.current_streak, 1)

        # Streak today again (should remain 1)
        update_streak(self.user.id)
        self.assertEqual(streak.current_streak, 1)

        # Mock last activity date back by 1 day and trigger consecutive day streak
        streak.last_activity_date = date.today() - timedelta(days=1)
        db.session.commit()
        update_streak(self.user.id)
        self.assertEqual(streak.current_streak, 2)
        self.assertEqual(streak.longest_streak, 2)

        # Mock last activity date back by 3 days (streak broken)
        streak.last_activity_date = date.today() - timedelta(days=3)
        db.session.commit()
        update_streak(self.user.id)
        self.assertEqual(streak.current_streak, 1)

    def test_prerequisite_course_locking(self):
        from app.domains.learning_path.models import PathPrerequisite, UserCourseProgress
        from app.domains.content.models import Course

        # Create Course A and Course B
        course_a = Course(subject_id=self.lesson.module.course.subject_id, title="Course A", slug="course-a")
        course_b = Course(subject_id=self.lesson.module.course.subject_id, title="Course B", slug="course-b")
        db.session.add_all([course_a, course_b])
        db.session.flush()

        # Set Course A as prerequisite for Course B
        prereq = PathPrerequisite(course_id=course_b.id, prerequisite_course_id=course_a.id)
        db.session.add(prereq)
        db.session.commit()

        # Mock session
        with self.client.session_transaction() as sess:
            sess["_user_id"] = str(self.user.id)

        # Access Course B overview (should fail with 403 Forbidden)
        res = self.client.get(f"/learn/{course_b.slug}/")
        self.assertEqual(res.status_code, 403)

        # Mark Course A as completed by user
        progress = UserCourseProgress(user_id=self.user.id, course_id=course_a.id, is_completed=True)
        db.session.add(progress)
        db.session.commit()

        # Try accessing Course B again (should now succeed, return 200/404 overview since it has no modules yet)
        res = self.client.get(f"/learn/{course_b.slug}/")
        self.assertIn(res.status_code, [200, 404])

    def test_flashcard_spaced_repetition(self):
        from app.domains.srs.models import FlashcardDeck, Flashcard, UserFlashcardProgress

        # Create Deck and card
        deck = FlashcardDeck(title="Git Deck")
        db.session.add(deck)
        db.session.flush()

        card = Flashcard(deck_id=deck.id, front_side_markdown="What is init?", back_side_markdown="Initializer")
        db.session.add(card)
        db.session.commit()

        # Mock session
        with self.client.session_transaction() as sess:
            sess["_user_id"] = str(self.user.id)

        # Review card with grade 4 (should succeed and initialize progress parameters)
        res = self.client.post(f"/api/v1/flashcards/{card.id}/review", json={"grade": 4})
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["repetitions"], 1)
        self.assertEqual(data["interval_days"], 1)

        # Review again with grade 5 (should increment repetitions and change interval to 6)
        res2 = self.client.post(f"/api/v1/flashcards/{card.id}/review", json={"grade": 5})
        self.assertEqual(res2.status_code, 200)
        data2 = res2.get_json()
        self.assertEqual(data2["repetitions"], 2)
        self.assertEqual(data2["interval_days"], 6)

    def test_bookmarks_and_notes(self):
        from app.domains.study.models import Bookmark, UserNote

        # Mock session
        with self.client.session_transaction() as sess:
            sess["_user_id"] = str(self.user.id)

        # Toggle bookmark (should add)
        res = self.client.post("/api/v1/bookmarks", json={"lesson_id": self.lesson.id})
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.get_json()["bookmarked"])

        # Toggle bookmark again (should remove)
        res2 = self.client.post("/api/v1/bookmarks", json={"lesson_id": self.lesson.id})
        self.assertEqual(res2.status_code, 200)
        self.assertFalse(res2.get_json()["bookmarked"])

        # Save note
        res3 = self.client.post("/api/v1/notes", json={"lesson_id": self.lesson.id, "content_markdown": "# My notes"})
        self.assertEqual(res3.status_code, 200)
        self.assertIn("created", res3.get_json()["message"])

    def test_text_chunker_splits_correctly(self):
        from app.domains.knowledge.chunker import chunk_text
        text = "A" * 1200  # 1200 chars
        chunks = chunk_text(text, chunk_size=500, overlap=50)
        # chunks: [0:500], [450:950], [900:1200] = 3 chunks
        self.assertEqual(len(chunks), 3)
        # Each chunk should not exceed 500 chars
        for chunk in chunks:
            self.assertLessEqual(len(chunk), 500)
        # First chunk should start at 0
        self.assertEqual(chunks[0], "A" * 500)

    def test_text_chunker_document_pipeline(self):
        from app.domains.knowledge.models import KnowledgeSource, SourceDocument, KnowledgeChunk
        from app.domains.knowledge.chunker import process_document

        # Create knowledge source
        source = KnowledgeSource(name="Test Docs", source_type="docs")
        db.session.add(source)
        db.session.flush()

        # Create a source document with 600-char text
        doc = SourceDocument(
            source_id=source.id,
            title="Git Introduction",
            raw_text="Git is a distributed version control system. " * 15  # ~675 chars
        )
        db.session.add(doc)
        db.session.commit()

        # Process chunking (Ollama will return zero-vector fallback in test)
        count = process_document(doc.id)
        self.assertGreater(count, 0)

        # Verify chunks were stored
        chunks = KnowledgeChunk.query.filter_by(document_id=doc.id).all()
        self.assertEqual(len(chunks), count)

        # Verify document is marked as chunked
        db.session.refresh(doc)
        self.assertTrue(doc.is_chunked)

    def test_hybrid_search_returns_results(self):
        with self.client.session_transaction() as sess:
            sess["_user_id"] = str(self.user.id)

        # Search for a term that matches the seeded lesson title
        res = self.client.get("/api/v1/search/hybrid?q=git")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["status"], "success")
        self.assertIn("results", data)

    def test_hybrid_search_requires_query(self):
        with self.client.session_transaction() as sess:
            sess["_user_id"] = str(self.user.id)

        res = self.client.get("/api/v1/search/hybrid")
        self.assertEqual(res.status_code, 400)

    def test_ai_explain_endpoint_with_fallback(self):
        with self.client.session_transaction() as sess:
            sess["_user_id"] = str(self.user.id)

        payload = {
            "concept": "Git staging area",
            "context": "Git has three states: working directory, staging area, repository.",
            "level": "beginner"
        }
        res = self.client.post("/api/v1/ai/explain", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["status"], "success")
        # Explanation may be fallback string when Ollama is offline
        self.assertIn("explanation", data)
        self.assertIsInstance(data["explanation"], str)
        self.assertGreater(len(data["explanation"]), 0)

    def test_ai_explain_requires_concept(self):
        with self.client.session_transaction() as sess:
            sess["_user_id"] = str(self.user.id)

        res = self.client.post("/api/v1/ai/explain", json={})
        self.assertEqual(res.status_code, 400)

    def test_admin_rbac_restrict_student(self):
        # Student user tries to access /admin/ (should return 403 Forbidden)
        with self.client.session_transaction() as sess:
            sess["_user_id"] = str(self.user.id)

        res = self.client.get("/admin/")
        self.assertEqual(res.status_code, 403)

    def test_admin_rbac_allow_admin(self):
        # Create role Admin
        admin_role = Role.query.filter_by(name="admin").first()
        if not admin_role:
            admin_role = Role(name="admin", display_name="Admin", level=6)
            db.session.add(admin_role)
            db.session.commit()

        # Create admin user
        admin_user = User(
            email="admin@bytesandboards.test",
            username="adminuser",
            password_hash="fake-hash",
            role_id=admin_role.id
        )
        db.session.add(admin_user)
        db.session.commit()

        with self.client.session_transaction() as sess:
            sess["_user_id"] = str(admin_user.id)

        res = self.client.get("/admin/")
        self.assertEqual(res.status_code, 200)

    def test_flesch_readability_calculations(self):
        from app.domains.content.quality import calculate_flesch_reading_ease
        # Simple textbook sentences
        text = "The cat sat on the mat. It was a nice day."
        score = calculate_flesch_reading_ease(text)
        self.assertGreater(score, 60.0)  # simple sentences have high Flesch Reading Ease scores

    def test_quality_score_trigger_and_check(self):
        from app.domains.content.quality import run_quality_check
        from app.domains.content.models import ContentQualityScore

        # Run quality check on the default seeded lesson
        q_score = run_quality_check(self.lesson.id)
        self.assertIsNotNone(q_score)
        
        # Verify db insert
        db_score = ContentQualityScore.query.filter_by(lesson_id=self.lesson.id).first()
        self.assertIsNotNone(db_score)
        self.assertEqual(db_score.readability_score, q_score.readability_score)

    def test_sitemap_xml_generation(self):
        from app.domains.content.sitemap import generate_sitemap_xml
        # Verify sitemap runs and returns xml content string
        xml_content = generate_sitemap_xml()
        self.assertIn("<urlset", xml_content)
        self.assertIn("https://bytesandboards.com", xml_content)

    def test_caching_decorator(self):
        from app.core.cache import cache_memoize, clear_cache

        call_count = 0

        @cache_memoize(timeout_seconds=5)
        def dummy_calc(x):
            nonlocal call_count
            call_count += 1
            return x * 2

        clear_cache()
        # First call calculates
        self.assertEqual(dummy_calc(10), 20)
        self.assertEqual(call_count, 1)

        # Second call returns cached value
        self.assertEqual(dummy_calc(10), 20)
        self.assertEqual(call_count, 1)

        # Different parameter calculates again
        self.assertEqual(dummy_calc(5), 10)
        self.assertEqual(call_count, 2)


class LearningServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.app.config["WTF_CSRF_ENABLED"] = False
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()
        self._seed_test_data()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def _seed_test_data(self):
        # Create student role
        role = Role.query.filter_by(name="student").first()
        if not role:
            role = Role(name="student", display_name="Student", level=1)
            db.session.add(role)
            db.session.commit()

        # Create user
        self.user = User(
            email="tester@bytesandboards.test",
            username="tester",
            password_hash="fake-hash",
            role_id=role.id,
            display_name="Tester User"
        )
        db.session.add(self.user)

        # Create technical course
        cat = Category(name="Tech", slug="tech")
        db.session.add(cat)
        db.session.flush()

        subj = Subject(category_id=cat.id, name="Git", slug="git")
        db.session.add(subj)
        db.session.flush()

        self.course = Course(
            subject_id=subj.id,
            title="Git Fundamentals",
            slug="git-fundamentals",
            status="published"
        )
        db.session.add(self.course)
        db.session.flush()

        mod = Module(course_id=self.course.id, title="Module 1", slug="module-1", is_published=True)
        db.session.add(mod)
        db.session.flush()

        self.lesson1 = Lesson(module_id=mod.id, title="Lesson 1", slug="lesson-1", status="published")
        self.lesson2 = Lesson(module_id=mod.id, title="Lesson 2", slug="lesson-2", status="published")
        db.session.add(self.lesson1)
        db.session.add(self.lesson2)
        db.session.commit()

    def test_xp_service_award(self):
        from app.services.learning import XPService
        # Award initial XP
        XPService.award(self.user.id, "lesson_completed", 10, reference_id=self.lesson1.id)
        db.session.commit()

        logs = UserXPLog.query.filter_by(user_id=self.user.id).all()
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0].xp_amount, 10)

        # Ensure double completions don't reward XP twice
        XPService.award(self.user.id, "lesson_completed", 10, reference_id=self.lesson1.id)
        db.session.commit()
        logs_after = UserXPLog.query.filter_by(user_id=self.user.id).all()
        self.assertEqual(len(logs_after), 1)

    def test_streak_service(self):
        from app.services.learning import StreakService
        # Start streak
        streak = StreakService.update_streak(self.user.id)
        db.session.commit()
        self.assertEqual(streak.current_streak, 1)

        # Update again today (retains same streak day count)
        streak = StreakService.update_streak(self.user.id)
        db.session.commit()
        self.assertEqual(streak.current_streak, 1)

    def test_learning_progress_completes_course(self):
        from app.services.learning import LearningProgressService
        
        # Complete Lesson 1
        LearningProgressService.complete_lesson(self.user.id, self.lesson1.id)
        course_prog = UserCourseProgress.query.filter_by(
            user_id=self.user.id,
            course_id=self.course.id
        ).first()
        self.assertIsNotNone(course_prog)
        self.assertFalse(course_prog.is_completed)

        # Complete Lesson 2 (all lessons complete)
        LearningProgressService.complete_lesson(self.user.id, self.lesson2.id)
        course_prog_after = UserCourseProgress.query.filter_by(
            user_id=self.user.id,
            course_id=self.course.id
        ).first()
        self.assertTrue(course_prog_after.is_completed)

    def test_dashboard_service_data(self):
        from app.services.learning import LearningProgressService, DashboardService
        
        # Initial empty active course dashboard
        data = DashboardService.get_dashboard_data(self.user.id)
        self.assertEqual(data["total_xp"], 0)
        self.assertEqual(data["streak"], 0)
        self.assertIsNotNone(data["default_course"])
        self.assertEqual(data["default_course"]["slug"], "git-fundamentals")

        # Complete lesson and query again
        LearningProgressService.complete_lesson(self.user.id, self.lesson1.id)
        db.session.commit()
        data_after = DashboardService.get_dashboard_data(self.user.id)
        self.assertEqual(data_after["total_xp"], 10)
        self.assertEqual(len(data_after["active_courses"]), 1)
        self.assertEqual(data_after["active_courses"][0]["progress_percentage"], 50)
        self.assertEqual(len(data_after["activity_feed"]), 1)


class EventServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.app.config["WTF_CSRF_ENABLED"] = False
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()
        self._seed_test_data()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def _seed_test_data(self):
        role = Role.query.filter_by(name="student").first()
        if not role:
            role = Role(name="student", display_name="Student", level=1)
            db.session.add(role)
            db.session.commit()

        self.user = User(
            email="event_tester@bytesandboards.test",
            username="event_tester",
            password_hash="fake-hash",
            role_id=role.id,
            display_name="Event Tester"
        )
        db.session.add(self.user)

        cat = Category(name="Tech", slug="tech")
        db.session.add(cat)
        db.session.flush()

        subj = Subject(category_id=cat.id, name="Git", slug="git")
        db.session.add(subj)
        db.session.flush()

        self.course = Course(
            subject_id=subj.id,
            title="Git Fundamentals",
            slug="git-fundamentals",
            status="published"
        )
        db.session.add(self.course)
        db.session.flush()

        mod = Module(course_id=self.course.id, title="Module 1", slug="module-1", sort_order=1, is_published=True)
        db.session.add(mod)
        db.session.flush()

        self.lesson1 = Lesson(module_id=mod.id, title="Lesson 1", slug="lesson-1", status="published", sort_order=1)
        self.lesson2 = Lesson(module_id=mod.id, title="Lesson 2", slug="lesson-2", status="published", sort_order=2)
        db.session.add(self.lesson1)
        db.session.add(self.lesson2)
        db.session.commit()

    def test_event_service_publish_and_subscribe(self):
        """Published events should invoke all registered listeners."""
        from app.services.learning import EventService
        received = []
        EventService.subscribe("test_event", lambda **kwargs: received.append(kwargs.get("value")))
        EventService.publish("test_event", value="hello")
        self.assertIn("hello", received)

    def test_event_service_no_double_xp_via_complete_lesson(self):
        """Completing the same lesson twice should only award XP once."""
        from app.services.learning import LearningProgressService
        LearningProgressService.complete_lesson(self.user.id, self.lesson1.id)
        db.session.commit()
        LearningProgressService.complete_lesson(self.user.id, self.lesson1.id)
        db.session.commit()
        xp_logs = UserXPLog.query.filter_by(
            user_id=self.user.id,
            activity_type="lesson_completed",
            reference_id=self.lesson1.id
        ).all()
        self.assertEqual(len(xp_logs), 1)

    def test_recommendation_service_returns_first_lesson(self):
        """Before any progress, RecommendationService should suggest first lesson of git-fundamentals."""
        from app.services.learning import RecommendationService
        rec = RecommendationService.get_resume_recommendation(self.user.id)
        self.assertIsNotNone(rec)
        self.assertEqual(rec["slug"], "git-fundamentals")
        self.assertEqual(rec["next_lesson"]["slug"], "lesson-1")

    def test_recommendation_service_advances_after_completion(self):
        """After completing lesson 1, RecommendationService should suggest lesson 2."""
        from app.services.learning import LearningProgressService, RecommendationService
        LearningProgressService.complete_lesson(self.user.id, self.lesson1.id)
        db.session.commit()
        rec = RecommendationService.get_resume_recommendation(self.user.id)
        self.assertIsNotNone(rec)
        self.assertEqual(rec["next_lesson"]["slug"], "lesson-2")

    def test_recommendation_service_generalized(self):
        """Test suggested labs, reviews, and next course recommendations."""
        from app.services.learning import RecommendationService
        from app.domains.content.models import Lab, LabStep
        from app.domains.assessment.models import Quiz, QuizAttempt
        
        # 1. Create a lab for lesson 1
        lab = Lab(lesson_id=self.lesson1.id, title="Init Lab", description="Learn git init")
        db.session.add(lab)
        db.session.flush()
        
        # Check suggested lab
        sugg_lab = RecommendationService.get_suggested_lab(self.user.id)
        self.assertIsNotNone(sugg_lab)
        self.assertEqual(sugg_lab["id"], lab.id)
        self.assertEqual(sugg_lab["title"], "Init Lab")
        
        # 2. Check suggested review - initially None
        sugg_review = RecommendationService.get_suggested_review(self.user.id)
        self.assertIsNone(sugg_review)
        
        # Create a quiz and failed quiz attempt to test review suggestion
        quiz = Quiz(lesson_id=self.lesson1.id, title="Quiz 1", slug="quiz-1", passing_score=70)
        db.session.add(quiz)
        db.session.flush()
        
        attempt = QuizAttempt(user_id=self.user.id, quiz_id=quiz.id, score=50, is_passed=False, started_at=datetime.utcnow(), completed_at=datetime.utcnow())
        db.session.add(attempt)
        db.session.commit()
        
        sugg_review = RecommendationService.get_suggested_review(self.user.id)
        self.assertIsNotNone(sugg_review)
        self.assertIn("Quiz Score: 50%", sugg_review["reason"])
        self.assertEqual(sugg_review["lesson_slug"], "lesson-1")

        # 3. Check recommended next course
        next_course = RecommendationService.get_recommended_next_course(self.user.id)
        self.assertIsNotNone(next_course)
        self.assertEqual(next_course["slug"], "git-fundamentals")

    def test_lab_service_and_event_integration(self):
        """Test lab progress saving and auto-grading via local Git validator mock."""
        from app.services.lab import LabService
        from app.domains.content.models import Lab, LabStep
        
        # Create lab and step with a rule
        lab = Lab(lesson_id=self.lesson1.id, title="Git Branch Lab", description="Create a branch")
        db.session.add(lab)
        db.session.flush()
        
        step = LabStep(lab_id=lab.id, step_number=1, title="Create branch", instruction="Run git branch <!-- rule:git_branch expected:feature -->")
        db.session.add(step)
        db.session.commit()
        
        # 1. Save step checkpoints manually
        sub = LabService.submit_step_progress(self.user.id, lab.id, 1, True)
        self.assertIn(1, sub.submission_data["completed_steps"])
        
        # 2. Mocking validation command output inside the engine
        sub_fail = LabService.verify_and_grade_lab(self.user.id, lab.id, repo_path="invalid_path_abc")
        self.assertEqual(sub_fail.status, "failed")
        self.assertIn("does not exist", sub_fail.feedback)
        
        from unittest.mock import patch
        from subprocess import CompletedProcess
        
        with patch("subprocess.run") as mock_run:
            mock_run.returncode = 0
            mock_run.return_value = CompletedProcess(args=["git", "branch"], returncode=0, stdout="* main\n  feature\n")
            
            with patch("os.path.exists", return_value=True), patch("os.path.isdir", return_value=True):
                sub_pass = LabService.verify_and_grade_lab(self.user.id, lab.id, repo_path="/some/fake/repo")
                self.assertEqual(sub_pass.status, "passed")
                
                # Check that XP log was created for lab completion
                xp_log = UserXPLog.query.filter_by(user_id=self.user.id, activity_type="lab_completed").first()
                self.assertIsNotNone(xp_log)
                self.assertEqual(xp_log.xp_amount, 50)

    def test_certificate_auto_award(self):
        """Completing all lessons in a course should trigger course_completed and award a Certificate if configured."""
        from app.services.learning import LearningProgressService
        from app.domains.content.models import Certificate, UserCertificate
        
        # Configure certificate for the course
        cert = Certificate(course_id=self.course.id, title="Git Master Cert", description="Successfully completed Git Fundamentals")
        db.session.add(cert)
        db.session.commit()
        
        # Complete lesson 1
        LearningProgressService.complete_lesson(self.user.id, self.lesson1.id)
        db.session.commit()
        
        # Verify no certificate awarded yet
        user_cert = UserCertificate.query.filter_by(user_id=self.user.id, certificate_id=cert.id).first()
        self.assertIsNone(user_cert)
        
        # Complete lesson 2 (finishing course)
        LearningProgressService.complete_lesson(self.user.id, self.lesson2.id)
        db.session.commit()
        
        # Verify certificate is awarded automatically
        user_cert = UserCertificate.query.filter_by(user_id=self.user.id, certificate_id=cert.id).first()
        self.assertIsNotNone(user_cert)
        self.assertEqual(user_cert.certificate.title, "Git Master Cert")

    def test_certificate_secure_hash_and_verification(self):
        """Test secure verification hash generation, decoding, and public verification endpoints."""
        from app.services.learning import CertificateService, LearningProgressService
        from app.domains.content.models import Certificate, UserCertificate
        
        # 1. Setup course certificate
        cert = Certificate(course_id=self.course.id, title="Git Master Cert", description="Successfully completed Git Fundamentals")
        db.session.add(cert)
        db.session.commit()
        
        # Complete all lessons
        LearningProgressService.complete_lesson(self.user.id, self.lesson1.id)
        LearningProgressService.complete_lesson(self.user.id, self.lesson2.id)
        db.session.commit()
        
        # Retrieve user certificate
        user_cert = UserCertificate.query.filter_by(user_id=self.user.id, certificate_id=cert.id).first()
        self.assertIsNotNone(user_cert)
        
        # 2. Test generation & validation service helpers
        sec_hash = CertificateService.generate_verification_hash(user_cert.id)
        self.assertIsNotNone(sec_hash)
        
        verified_cert = CertificateService.verify_certificate_hash(sec_hash)
        self.assertIsNotNone(verified_cert)
        self.assertEqual(verified_cert.id, user_cert.id)
        
        # Ensure invalid hash returns None
        self.assertIsNone(CertificateService.verify_certificate_hash("invalid-token-xyz"))
        
        # 3. Test HTTP routes
        with self.client.session_transaction() as sess:
            sess["_user_id"] = str(self.user.id)
            
        # Get certificate list
        res_list = self.client.get("/learn/certificates/")
        self.assertEqual(res_list.status_code, 200)
        self.assertIn(b"Git Master Cert", res_list.data)
        
        # Get certificate detail
        res_detail = self.client.get(f"/learn/certificates/{user_cert.id}/")
        self.assertEqual(res_detail.status_code, 200)
        self.assertIn(b"Certificate of Completion", res_detail.data)
        
        # Get public verification route (no session required!)
        with self.client.session_transaction() as sess:
            sess.clear()
            
        res_pub_verify = self.client.get(f"/learn/verify/certificate/{sec_hash}")
        self.assertEqual(res_pub_verify.status_code, 200)
        self.assertIn(b"Verification Verified", res_pub_verify.data)
        self.assertIn(b"Certificate of Completion", res_pub_verify.data)
        
        # Test public verification with invalid hash
        res_pub_fail = self.client.get("/learn/verify/certificate/invalid-hash-abc")
        self.assertEqual(res_pub_fail.status_code, 404)
        self.assertIn(b"Invalid Certificate Token", res_pub_fail.data)

    def test_ai_tutor_integration(self):
        """Test AI Tutor session creation, listing, details retrieval, and SSE message response streaming."""
        from app.domains.tutor.models import AITutorSession, AITutorMessage
        
        # Authenticate user session
        with self.client.session_transaction() as sess:
            sess["_user_id"] = str(self.user.id)
            
        # 1. Create a general tutor session
        res_create = self.client.post("/api/v1/tutor/sessions", json={})
        self.assertEqual(res_create.status_code, 200)
        data_create = res_create.get_json()
        self.assertEqual(data_create["status"], "success")
        session_id = data_create["session_id"]
        self.assertEqual(data_create["title"], "General Tutoring Session")
        
        # Verify in DB
        session = db.session.get(AITutorSession, session_id)
        self.assertIsNotNone(session)
        self.assertEqual(session.user_id, self.user.id)
        self.assertIsNone(session.lesson_id)
        
        # 2. Create a lesson-specific tutor session
        res_create_lesson = self.client.post("/api/v1/tutor/sessions", json={"lesson_id": self.lesson1.id})
        self.assertEqual(res_create_lesson.status_code, 200)
        data_create_lesson = res_create_lesson.get_json()
        session_lesson_id = data_create_lesson["session_id"]
        self.assertEqual(data_create_lesson["title"], f"Tutor Session: {self.lesson1.title}")
        
        session_lesson = db.session.get(AITutorSession, session_lesson_id)
        self.assertEqual(session_lesson.lesson_id, self.lesson1.id)
        
        # 3. List tutor sessions
        res_list = self.client.get("/api/v1/tutor/sessions")
        self.assertEqual(res_list.status_code, 200)
        data_list = res_list.get_json()
        self.assertEqual(data_list["status"], "success")
        self.assertEqual(len(data_list["sessions"]), 2)
        
        # 4. Get session details (empty message list initially)
        res_details = self.client.get(f"/api/v1/tutor/sessions/{session_id}")
        self.assertEqual(res_details.status_code, 200)
        data_details = res_details.get_json()
        self.assertEqual(data_details["status"], "success")
        self.assertEqual(len(data_details["messages"]), 0)
        
        # 5. Post message and stream tutor response (SSE)
        res_msg = self.client.post(
            f"/api/v1/tutor/sessions/{session_id}/messages",
            json={"message": "Explain git rebase"}
        )
        self.assertEqual(res_msg.status_code, 200)
        self.assertEqual(res_msg.mimetype, "text/event-stream")
        
        # Read the stream content
        stream_data = res_msg.data.decode("utf-8")
        self.assertIn("data: ", stream_data)
        self.assertIn("chunk", stream_data)
        
        # Verify messages are saved in database
        user_msg = AITutorMessage.query.filter_by(session_id=session_id, sender="user").first()
        self.assertIsNotNone(user_msg)
        self.assertEqual(user_msg.content, "Explain git rebase")
        
        tutor_msg = AITutorMessage.query.filter_by(session_id=session_id, sender="tutor").first()
        self.assertIsNotNone(tutor_msg)
        self.assertIn("AI Unavailable", tutor_msg.content)
        
        # 6. Retrieve details again (should now have 2 messages)
        res_details2 = self.client.get(f"/api/v1/tutor/sessions/{session_id}")
        self.assertEqual(res_details2.status_code, 200)
        data_details2 = res_details2.get_json()
        self.assertEqual(len(data_details2["messages"]), 2)
        self.assertEqual(data_details2["messages"][0]["sender"], "user")
        self.assertEqual(data_details2["messages"][1]["sender"], "tutor")
        
        # 7. Render front-end page
        res_ui = self.client.get("/learn/tutor/")
        self.assertEqual(res_ui.status_code, 200)
        self.assertIn(b"AI Programming Tutor", res_ui.data)

    def test_hybrid_search_and_autocomplete(self):
        """Test FTS5 search index building, hybrid search query results, and autocomplete filtering."""
        from app.services.search_service import SearchIndexService
        from app.domains.knowledge.search import hybrid_search
        from app.domains.knowledge.models import SourceDocument, KnowledgeChunk, ChunkEmbedding
        
        # 1. Verify index rebuild is functional
        SearchIndexService.rebuild_search_index()
        
        # 2. Add an external source document & chunk to test semantic chunk hits
        from app.domains.knowledge.models import KnowledgeSource
        source = KnowledgeSource(name="Git Docs", source_type="docs", base_url="https://git-scm.com")
        db.session.add(source)
        db.session.flush()
        
        doc = SourceDocument(source_id=source.id, title="Git Branching Guide", url="https://git-scm.com/branches", raw_text="Git rebase allows rewriting commit history on a branch.")
        db.session.add(doc)
        db.session.flush()
        
        chunk = KnowledgeChunk(document_id=doc.id, chunk_index=0, chunk_text="Git rebase allows rewriting commit history on a branch.")
        db.session.add(chunk)
        db.session.flush()
        
        # Add embedding vector
        emb = ChunkEmbedding(chunk_id=chunk.id)
        emb.set_vector([0.0] * 384)
        db.session.add(emb)
        db.session.commit()
        
        # 3. Test Service helper functions
        fts_hits = SearchIndexService.search_query("Lesson")
        self.assertGreater(len(fts_hits), 0)
        self.assertEqual(fts_hits[0]["lesson_id"], self.lesson1.id)
        
        # 4. Test Autocomplete Route
        with self.client.session_transaction() as sess:
            sess["_user_id"] = str(self.user.id)
            
        res_auto = self.client.get("/api/v1/search/autocomplete?q=Less")
        self.assertEqual(res_auto.status_code, 200)
        data_auto = res_auto.get_json()
        self.assertEqual(data_auto["status"], "success")
        self.assertGreater(len(data_auto["results"]), 0)
        self.assertEqual(data_auto["results"][0]["title"], "Lesson 1")
        
        # 5. Test Search UI View page
        res_view = self.client.get("/search?q=Lesson")
        self.assertEqual(res_view.status_code, 200)
        self.assertIn(b"Search Results", res_view.data)
        self.assertIn(b"Lesson 1", res_view.data)
        
        # 6. Test REST API hybrid search endpoint
        res_hybrid = self.client.get("/api/v1/search/hybrid?q=Lesson")
        self.assertEqual(res_hybrid.status_code, 200)
        data_hybrid = res_hybrid.get_json()
        self.assertEqual(data_hybrid["status"], "success")
        self.assertGreater(data_hybrid["count"], 0)

    def test_enterprise_dashboard_and_rbac(self):
        """Test user role listings, updates, peer review queue transitions, sitemap xml builder, and role protections."""
        from app.domains.auth.models import User, Role
        from app.domains.content.models import Lesson
        
        # Create user roles for testing (e.g. editor, reviewer, student)
        reviewer_role = Role.query.filter_by(name="reviewer").first()
        if not reviewer_role:
            reviewer_role = Role(name="reviewer", display_name="Reviewer", level=10)
            db.session.add(reviewer_role)
            db.session.commit()
            
        admin_role = Role.query.filter_by(name="admin").first()
        if not admin_role:
            admin_role = Role(name="admin", display_name="Admin", level=20)
            db.session.add(admin_role)
            db.session.commit()
            
        # Create a test reviewer user
        reviewer_user = User(
            email="reviewer@bytesandboards.test",
            username="reviewer",
            password_hash="fake-hash",
            role_id=reviewer_role.id,
            display_name="Reviewer User"
        )
        db.session.add(reviewer_user)
        db.session.commit()
        
        # 1. Test role permissions restrict (Student role user has level=1, cannot access admin dashboard)
        with self.client.session_transaction() as sess:
            sess["_user_id"] = str(self.user.id) # student role
        res_denied = self.client.get("/admin/")
        self.assertEqual(res_denied.status_code, 403)
        
        # Promote our user to admin
        self.user.role_id = admin_role.id
        db.session.commit()
        
        # Get admin dashboard (should pass now)
        res_dashboard = self.client.get("/admin/")
        self.assertEqual(res_dashboard.status_code, 200)
        self.assertIn(b"CMS Admin Dashboard", res_dashboard.data)
        self.assertIn(b"System Analytics", res_dashboard.data)
        
        # 2. Test user roles listing view
        res_users = self.client.get("/admin/users")
        self.assertEqual(res_users.status_code, 200)
        self.assertIn(b"User Role Management", res_users.data)
        
        # Promote reviewer_user to admin via POST
        res_promo = self.client.post(
            f"/admin/users/{reviewer_user.id}/role",
            data={"role_id": str(admin_role.id)}
        )
        self.assertEqual(res_promo.status_code, 302) # Redirect to users list
        db.session.refresh(reviewer_user)
        self.assertEqual(reviewer_user.role_id, admin_role.id)
        
        # Demote back to reviewer
        reviewer_user.role_id = reviewer_role.id
        db.session.commit()
        
        # 3. Test review queue transitions
        # Set lesson1 status to "review"
        self.lesson1.status = "review"
        db.session.commit()
        
        # Reviewer session login
        with self.client.session_transaction() as sess:
            sess["_user_id"] = str(reviewer_user.id) # reviewer role
            
        res_queue = self.client.get("/admin/review-queue")
        self.assertEqual(res_queue.status_code, 200)
        self.assertIn(b"Peer Review Queue", res_queue.data)
        self.assertIn(self.lesson1.title.encode("utf-8"), res_queue.data)
        
        # Approve the draft (publishes it)
        res_approve = self.client.post(
            f"/admin/review-queue/{self.lesson1.id}/status",
            data={"action": "approve"}
        )
        self.assertEqual(res_approve.status_code, 302)
        db.session.refresh(self.lesson1)
        self.assertEqual(self.lesson1.status, "published")
        
        # Reject lesson2 draft (set status to review first)
        self.lesson2.status = "review"
        db.session.commit()
        
        res_reject = self.client.post(
            f"/admin/review-queue/{self.lesson2.id}/status",
            data={"action": "reject"}
        )
        self.assertEqual(res_reject.status_code, 302)
        db.session.refresh(self.lesson2)
        self.assertEqual(self.lesson2.status, "draft")
        
        # 4. Test SEO dynamic Sitemap XML View (public endpoint, no session required)
        with self.client.session_transaction() as sess:
            sess.clear()
            
        res_sitemap = self.client.get("/sitemap.xml")
        self.assertEqual(res_sitemap.status_code, 200)
        self.assertEqual(res_sitemap.mimetype, "application/xml")
        sitemap_data = res_sitemap.data
        self.assertIn(b"<loc>", sitemap_data)
        self.assertIn(b"git-fundamentals", sitemap_data)


if __name__ == "__main__":
    unittest.main()
