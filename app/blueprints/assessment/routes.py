"""
Learning OS — Assessment Blueprint
Handles Quiz attempts, question submissions, and evaluations.
"""
from datetime import datetime
from flask import Blueprint, jsonify, request, abort
from flask_login import login_required, current_user
from app.core.extensions import db
from app.domains.assessment.models import Quiz, Question, Option, QuizAttempt, QuizAnswer
from app.domains.gamification.models import UserXPLog

assessment_bp = Blueprint("assessment", __name__)


@assessment_bp.route("/api/v1/quizzes/<int:quiz_id>/attempts", methods=["POST"])
@login_required
def create_attempt(quiz_id: int):
    quiz = db.session.get(Quiz, quiz_id)
    if not quiz or not quiz.is_active:
        return jsonify({"status": "error", "message": "Quiz not found or inactive"}), 404

    # Create a new quiz attempt
    attempt = QuizAttempt(
        user_id=current_user.id,
        quiz_id=quiz.id,
        started_at=datetime.utcnow()
    )
    db.session.add(attempt)
    db.session.commit()

    return jsonify({
        "status": "success",
        "attempt_id": attempt.id,
        "quiz_title": quiz.title,
        "time_limit_seconds": quiz.time_limit_seconds
    }), 201


@assessment_bp.route("/api/v1/quizzes/attempts/<int:attempt_id>/submit", methods=["POST"])
@login_required
def submit_attempt(attempt_id: int):
    attempt = db.session.get(QuizAttempt, attempt_id)
    if not attempt or attempt.user_id != current_user.id:
        return jsonify({"status": "error", "message": "Attempt not found"}), 404

    if attempt.completed_at is not None:
        return jsonify({"status": "error", "message": "Attempt already submitted"}), 400

    quiz = attempt.quiz
    data = request.get_json() or {}
    submitted_answers = data.get("answers", [])  # List of {"question_id": X, "selected_option_id": Y}

    # Map question_id -> selected_option_id for easy lookup
    answer_map = {int(a["question_id"]): int(a["selected_option_id"]) for a in submitted_answers if "question_id" in a and "selected_option_id" in a}

    total_questions = len(quiz.questions)
    if total_questions == 0:
        return jsonify({"status": "error", "message": "Quiz has no questions"}), 400

    correct_count = 0
    total_score_earned = 0
    max_possible_score = sum(q.points for q in quiz.questions)

    # Process each question in the quiz
    for question in quiz.questions:
        selected_option_id = answer_map.get(question.id)
        is_correct = False

        if selected_option_id:
            option = db.session.get(Option, selected_option_id)
            if option and option.question_id == question.id and option.is_correct:
                is_correct = True
                correct_count += 1
                total_score_earned += question.points

        # Record answer
        quiz_ans = QuizAnswer(
            attempt_id=attempt.id,
            question_id=question.id,
            selected_option_id=selected_option_id,
            is_correct=is_correct
        )
        db.session.add(quiz_ans)

    # Calculate percentage score
    score_percentage = int((total_score_earned / max_possible_score) * 100) if max_possible_score > 0 else 0
    is_passed = score_percentage >= quiz.passing_score

    # Determine XP reward
    xp_earned = 0
    if is_passed:
        # Check if user already passed this quiz before to avoid infinite farming
        prev_pass = QuizAttempt.query.filter_by(
            user_id=current_user.id,
            quiz_id=quiz.id,
            is_passed=True
        ).filter(QuizAttempt.id != attempt.id).first()
        
        if not prev_pass:
            xp_earned = quiz.xp_reward

    # Finalize attempt status
    attempt.completed_at = datetime.utcnow()
    attempt.score = score_percentage
    attempt.is_passed = is_passed
    attempt.xp_earned = xp_earned

    # Trigger Central Event Service
    from app.services.learning import EventService
    EventService.publish("quiz_completed", user_id=current_user.id, quiz_id=quiz.id, xp_reward=xp_earned, score=score_percentage)

    db.session.commit()

    return jsonify({
        "status": "success",
        "score": score_percentage,
        "is_passed": is_passed,
        "xp_earned": xp_earned,
        "correct_answers": correct_count,
        "total_questions": total_questions
    })
