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
            email="tester@edusphere.test",
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


if __name__ == "__main__":
    unittest.main()
