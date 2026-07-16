"""
Learning OS — Sandbox Blueprint
API endpoint to compile, execute, and submit code exercises.
"""
from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.core.extensions import db
from app.domains.sandbox.models import Exercise, ExerciseTestCase, ExerciseSubmission
from app.domains.sandbox.service import SandboxService
from app.domains.gamification.models import UserXPLog

sandbox_bp = Blueprint("sandbox", __name__)
sandbox_service = SandboxService()


@sandbox_bp.route("/api/v1/exercises/<int:exercise_id>/submit", methods=["POST"])
@login_required
def submit_exercise(exercise_id: int):
    exercise = db.session.get(Exercise, exercise_id)
    if not exercise or not exercise.is_active:
        return jsonify({"status": "error", "message": "Exercise not found"}), 404

    data = request.get_json() or {}
    source_code = data.get("source_code", "").strip()

    if not source_code:
        return jsonify({"status": "error", "message": "Source code cannot be empty"}), 400

    test_cases = exercise.test_cases
    if not test_cases:
        return jsonify({"status": "error", "message": "Exercise has no test cases configured"}), 400

    all_passed = True
    submission_status = "accepted"
    last_stdout = ""
    last_stderr = ""

    # Evaluate the code against each test case
    for tc in test_cases:
        result = sandbox_service.execute_code(
            source_code=source_code,
            language=exercise.programming_language,
            input_data=tc.input_data or ""
        )

        # Check stdout vs expected output (strip trailing/leading spaces)
        expected = tc.expected_output.strip()
        actual = result.get("stdout", "").strip()

        # If it failed to compile or run, fail immediately
        if result["status"] != "accepted":
            all_passed = False
            submission_status = result["status"]
            last_stdout = result.get("stdout", "")
            last_stderr = result.get("stderr", "")
            break

        # Check correctness of output
        if actual != expected:
            all_passed = False
            submission_status = "wrong_answer"
            last_stdout = result.get("stdout", "")
            last_stderr = f"Test case failed.\nExpected: {expected}\nActual: {actual}"
            break

        last_stdout = result.get("stdout", "")
        last_stderr = result.get("stderr", "")

    # Award XP if passed and not solved before
    xp_earned = 0
    if all_passed:
        prev_solve = ExerciseSubmission.query.filter_by(
            user_id=current_user.id,
            exercise_id=exercise.id,
            status="accepted"
        ).first()

        if not prev_solve:
            xp_earned = exercise.xp_reward
            xp_log = UserXPLog(
                user_id=current_user.id,
                xp_amount=xp_earned,
                activity_type="exercise_solved",
                reference_id=exercise.id
            )
            db.session.add(xp_log)

    # Save user submission records
    submission = ExerciseSubmission(
        user_id=current_user.id,
        exercise_id=exercise.id,
        source_code=source_code,
        status=submission_status,
        stdout=last_stdout,
        stderr=last_stderr
    )
    db.session.add(submission)
    db.session.commit()

    return jsonify({
        "status": "success",
        "result_status": submission_status,
        "all_passed": all_passed,
        "xp_earned": xp_earned,
        "stdout": last_stdout,
        "stderr": last_stderr
    })
