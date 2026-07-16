"""
Learning OS — Spaced Repetition (SRS) Blueprint
API endpoints for reviewing flashcards and querying active decks.
"""
from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.core.extensions import db
from app.domains.srs.models import FlashcardDeck, Flashcard, UserFlashcardProgress
from app.domains.srs.service import review_flashcard

srs_bp = Blueprint("srs", __name__)


@srs_bp.route("/api/v1/flashcards/<int:card_id>/review", methods=["POST"])
@login_required
def submit_flashcard_review(card_id: int):
    card = db.session.get(Flashcard, card_id)
    if not card:
        return jsonify({"status": "error", "message": "Flashcard not found"}), 404

    data = request.get_json() or {}
    grade = data.get("grade")

    if grade is None or not isinstance(grade, int) or grade < 0 or grade > 5:
        return jsonify({"status": "error", "message": "Grade must be an integer between 0 and 5"}), 400

    result = review_flashcard(
        user_id=current_user.id,
        flashcard_id=card.id,
        grade=grade
    )

    return jsonify({
        "status": "success",
        "repetitions": result["repetitions"],
        "interval_days": result["interval_days"],
        "ease_factor": result["ease_factor"],
        "next_review_at": result["next_review_at"].isoformat()
    })
