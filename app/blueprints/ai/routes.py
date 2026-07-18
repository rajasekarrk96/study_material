"""
Learning OS — AI & Search Blueprint.
Exposes REST endpoints for hybrid search, AI chat completions, and document chunking.
"""
from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.domains.knowledge.search import hybrid_search
from app.domains.knowledge.chunker import process_document
from app.providers.registry import get_provider
from app.providers.prompts import get_prompt

ai_bp = Blueprint("ai", __name__)


@ai_bp.route("/api/v1/search/hybrid", methods=["GET"])
@login_required
def search_hybrid():
    """Hybrid full-text + vector similarity search across all lesson content."""
    query = request.args.get("q", "").strip()
    top_k = min(int(request.args.get("k", 10)), 50)

    if not query:
        return jsonify({"status": "error", "message": "Query parameter 'q' is required"}), 400

    results = hybrid_search(query, top_k=top_k)
    return jsonify({
        "status": "success",
        "query": query,
        "count": len(results),
        "results": results
    })


@ai_bp.route("/api/v1/ai/explain", methods=["POST"])
@login_required
def ai_explain():
    """Explain a concept using the local AI provider."""
    data = request.get_json() or {}
    concept = data.get("concept", "").strip()
    context = data.get("context", "")
    level = data.get("level", "beginner")

    if not concept:
        return jsonify({"status": "error", "message": "Field 'concept' is required"}), 400

    prompt = get_prompt("explain_concept", concept=concept, context=context, level=level)
    provider = get_provider()
    response = provider.chat(prompt)

    return jsonify({"status": "success", "explanation": response})


@ai_bp.route("/api/v1/ai/summarize", methods=["POST"])
@login_required
def ai_summarize():
    """Summarize lesson content using the local AI provider."""
    data = request.get_json() or {}
    content = data.get("content", "").strip()

    if not content:
        return jsonify({"status": "error", "message": "Field 'content' is required"}), 400

    prompt = get_prompt("summarize_lesson", content=content)
    provider = get_provider()
    response = provider.chat(prompt)

    return jsonify({"status": "success", "summary": response})


@ai_bp.route("/api/v1/ai/flashcards", methods=["POST"])
@login_required
def ai_generate_flashcards():
    """Generate flashcards from lesson content using the local AI provider."""
    data = request.get_json() or {}
    content = data.get("content", "").strip()
    count = data.get("count", 5)

    if not content:
        return jsonify({"status": "error", "message": "Field 'content' is required"}), 400

    prompt = get_prompt("generate_flashcards", content=content, count=count)
    provider = get_provider()
    response = provider.chat(prompt)

    return jsonify({"status": "success", "raw_output": response})


@ai_bp.route("/api/v1/knowledge/chunk", methods=["POST"])
@login_required
def chunk_document():
    """Trigger chunking and embedding for a SourceDocument by ID."""
    data = request.get_json() or {}
    document_id = data.get("document_id")

    if not document_id:
        return jsonify({"status": "error", "message": "Field 'document_id' is required"}), 400

    chunk_count = process_document(int(document_id))
    return jsonify({
        "status": "success",
        "document_id": document_id,
        "chunks_created": chunk_count
    })


from flask import Response
from flask_login import current_user
from app.core.extensions import db
from app.domains.tutor.models import AITutorSession, AITutorMessage
from app.domains.content.models import Lesson, LessonSection

@ai_bp.route("/api/v1/tutor/sessions", methods=["POST"])
@login_required
def create_tutor_session():
    """Create a new AI Tutor session, optionally context-bound to a lesson."""
    data = request.get_json() or {}
    lesson_id = data.get("lesson_id")
    
    title = "General Tutoring Session"
    if lesson_id:
        lesson = db.session.get(Lesson, lesson_id)
        if lesson:
            title = f"Tutor Session: {lesson.title}"
            
    session = AITutorSession(user_id=current_user.id, lesson_id=lesson_id, title=title)
    db.session.add(session)
    db.session.commit()
    
    return jsonify({
        "status": "success",
        "session_id": session.id,
        "title": session.title
    })


@ai_bp.route("/api/v1/tutor/sessions", methods=["GET"])
@login_required
def get_tutor_sessions():
    """List all AI Tutor sessions for the current user."""
    sessions = AITutorSession.query.filter_by(user_id=current_user.id, is_active=True).order_by(AITutorSession.created_at.desc()).all()
    return jsonify({
        "status": "success",
        "sessions": [{
            "id": s.id,
            "title": s.title,
            "lesson_id": s.lesson_id,
            "created_at": s.created_at.isoformat()
        } for s in sessions]
    })


@ai_bp.route("/api/v1/tutor/sessions/<int:session_id>", methods=["GET"])
@login_required
def get_tutor_session_details(session_id: int):
    """Retrieve details and chat history of a specific AI Tutor session."""
    session = db.session.get(AITutorSession, session_id)
    if not session or session.user_id != current_user.id:
        return jsonify({"status": "error", "message": "Session not found"}), 404
        
    messages = AITutorMessage.query.filter_by(session_id=session.id).order_by(AITutorMessage.created_at.asc()).all()
    return jsonify({
        "status": "success",
        "session": {
            "id": session.id,
            "title": session.title,
            "lesson_id": session.lesson_id,
        },
        "messages": [{
            "id": m.id,
            "sender": m.sender,
            "content": m.content,
            "created_at": m.created_at.isoformat()
        } for m in messages]
    })


@ai_bp.route("/api/v1/tutor/sessions/<int:session_id>/messages", methods=["POST"])
@login_required
def post_tutor_message(session_id: int):
    """Post a student message to a session and stream the AI Tutor response via SSE."""
    session = db.session.get(AITutorSession, session_id)
    if not session or session.user_id != current_user.id:
        return jsonify({"status": "error", "message": "Session not found"}), 404
        
    data = request.get_json() or {}
    message_text = data.get("message", "").strip()
    if not message_text:
        return jsonify({"status": "error", "message": "Message is required"}), 400
        
    # Save user message
    user_msg = AITutorMessage(session_id=session_id, sender="user", content=message_text)
    db.session.add(user_msg)
    db.session.commit()
    
    # Retrieve chat history (excluding the new user message for prompt structure formatting)
    history_msgs = AITutorMessage.query.filter_by(session_id=session_id).order_by(AITutorMessage.created_at.asc()).all()
    history_str = ""
    for m in history_msgs[:-1]:
        history_str += f"{m.sender.capitalize()}: {m.content}\n"
        
    lesson_title = "None"
    lesson_context = "None"
    if session.lesson_id:
        lesson = db.session.get(Lesson, session.lesson_id)
        if lesson:
            lesson_title = lesson.title
            sections = LessonSection.query.filter_by(lesson_id=lesson.id).order_by(LessonSection.sort_order.asc()).all()
            lesson_context = "\n".join([f"## {s.title}\n{s.content_markdown}" for s in sections])
            
    prompt = get_prompt("ai_tutor", lesson_title=lesson_title, lesson_context=lesson_context, history=history_str, message=message_text)
    
    provider = get_provider()
    
    def generate():
        from flask import current_app
        with current_app.app_context():
            full_response = []
            if hasattr(provider, "chat_stream"):
                stream = provider.chat_stream(prompt)
            else:
                stream = [provider.chat(prompt)]
                
            for chunk in stream:
                full_response.append(chunk)
                import json
                yield f"data: {json.dumps({'chunk': chunk})}\n\n"
                
            tutor_response_text = "".join(full_response).strip()
            # Save tutor message to database
            tutor_msg = AITutorMessage(session_id=session_id, sender="tutor", content=tutor_response_text)
            db.session.add(tutor_msg)
            db.session.commit()
            
    return Response(generate(), mimetype="text/event-stream")


@ai_bp.route("/api/v1/search/autocomplete", methods=["GET"])
@login_required
def autocomplete_search():
    """Retrieve prefix-matching lesson title recommendations for autocomplete search bar."""
    query = request.args.get("q", "").strip()
    if not query:
        return jsonify({"status": "success", "results": []})
        
    pattern = f"{query}%"
    lessons = Lesson.query.filter(
        (Lesson.title.ilike(pattern)) &
        (Lesson.status == "published") &
        (Lesson.is_deleted == False)
    ).limit(5).all()
    
    return jsonify({
        "status": "success",
        "results": [{
            "id": l.id,
            "title": l.title,
            "slug": l.slug,
            "course_slug": l.module.course.slug if l.module and l.module.course else ""
        } for l in lessons]
    })
