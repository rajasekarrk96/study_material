"""
Learning OS — Study Annotations Blueprint
API endpoints for toggling lesson bookmarks and managing personal markdown notes.
"""
from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.core.extensions import db
from app.domains.study.models import Bookmark, UserNote

study_bp = Blueprint("study", __name__)


@study_bp.route("/api/v1/bookmarks", methods=["POST"])
@login_required
def toggle_bookmark():
    data = request.get_json() or {}
    lesson_id = data.get("lesson_id")

    if not lesson_id:
        return jsonify({"status": "error", "message": "lesson_id is required"}), 400

    existing = Bookmark.query.filter_by(
        user_id=current_user.id,
        lesson_id=lesson_id
    ).first()

    if existing:
        db.session.delete(existing)
        db.session.commit()
        return jsonify({"status": "success", "bookmarked": False, "message": "Bookmark removed"})
    else:
        new_bookmark = Bookmark(user_id=current_user.id, lesson_id=lesson_id)
        db.session.add(new_bookmark)
        db.session.commit()
        return jsonify({"status": "success", "bookmarked": True, "message": "Bookmark added"})


@study_bp.route("/api/v1/notes", methods=["POST"])
@login_required
def save_user_note():
    data = request.get_json() or {}
    lesson_id = data.get("lesson_id")
    content_markdown = data.get("content_markdown", "").strip()

    if not lesson_id:
        return jsonify({"status": "error", "message": "lesson_id is required"}), 400

    note = UserNote.query.filter_by(
        user_id=current_user.id,
        lesson_id=lesson_id
    ).first()

    if note:
        if not content_markdown:
            db.session.delete(note)
            db.session.commit()
            return jsonify({"status": "success", "message": "Note deleted"})
        else:
            note.content_markdown = content_markdown
            db.session.commit()
            return jsonify({"status": "success", "message": "Note updated"})
    else:
        if not content_markdown:
            return jsonify({"status": "success", "message": "No note to save"})
        new_note = UserNote(
            user_id=current_user.id,
            lesson_id=lesson_id,
            content_markdown=content_markdown
        )
        db.session.add(new_note)
        db.session.commit()
        return jsonify({"status": "success", "message": "Note created"})
