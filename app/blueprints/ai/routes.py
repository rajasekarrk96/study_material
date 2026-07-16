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
