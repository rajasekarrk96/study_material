"""
Learning OS — Hybrid Search Service.
Merges full-text search (SQLite FTS5 LIKE fallback) and vector cosine similarity
using Reciprocal Rank Fusion (RRF) to produce a unified relevance-ranked result set.
"""
import logging
from sqlalchemy import text
from app.core.extensions import db
from app.domains.content.models import Lesson
from app.domains.knowledge.chunker import vector_search

logger = logging.getLogger(__name__)

# RRF constant — higher k = softer rank weighting differences
RRF_K = 60


def _fts_search(query: str, limit: int = 20) -> list[dict]:
    """
    Full-text search across lesson titles, descriptions, and content body.
    Uses SQLite FTS5 matching, falling back to LIKE matches.
    """
    from app.services.search_service import SearchIndexService
    hits = SearchIndexService.search_query(query, limit=limit)
    
    ranked = []
    for idx, hit in enumerate(hits):
        lesson = db.session.get(Lesson, hit["lesson_id"])
        if lesson:
            ranked.append({
                "type": "lesson",
                "id": lesson.id,
                "title": lesson.title,
                "slug": lesson.slug,
                "course_slug": lesson.module.course.slug if lesson.module and lesson.module.course else "",
                "module_slug": lesson.module.slug if lesson.module else "",
                "description": lesson.summary or "",
                "fts_rank": idx + 1
            })
    return ranked


def hybrid_search(query: str, top_k: int = 10) -> list[dict]:
    """
    Combine FTS results and vector similarity results using Reciprocal Rank Fusion.
    Returns the top_k merged and re-ranked results.
    """
    # ── Step 1: FTS results ──────────────────────────────────────────────────
    fts_results = _fts_search(query, limit=20)
    fts_map: dict[str, dict] = {}
    for rank, item in enumerate(fts_results):
        key = f"lesson:{item['id']}"
        fts_map[key] = {"rank": rank + 1, "item": item}

    # ── Step 2: Vector similarity results ───────────────────────────────────
    vector_results = vector_search(query, top_k=20)
    vec_map: dict[str, dict] = {}
    for rank, chunk_hit in enumerate(vector_results):
        key = f"chunk:{chunk_hit['chunk_id']}"
        vec_map[key] = {"rank": rank + 1, "chunk": chunk_hit}

    # ── Step 3: Merge all candidates ────────────────────────────────────────
    all_keys = set(fts_map.keys()) | set(vec_map.keys())
    fused: list[dict] = []

    for key in all_keys:
        fts_rank = fts_map[key]["rank"] if key in fts_map else len(all_keys) + 1
        vec_rank = vec_map[key]["rank"] if key in vec_map else len(all_keys) + 1

        rrf_score = (1 / (RRF_K + fts_rank)) + (1 / (RRF_K + vec_rank))

        if key.startswith("lesson:"):
            data = fts_map[key]["item"]
            result = {
                "result_type": "lesson",
                "id": data["id"],
                "title": data["title"],
                "slug": data["slug"],
                "course_slug": data["course_slug"],
                "module_slug": data["module_slug"],
                "description": data["description"],
                "rrf_score": rrf_score,
            }
        else:
            from app.domains.knowledge.models import SourceDocument
            chunk = vec_map[key]["chunk"]
            doc = db.session.get(SourceDocument, chunk["document_id"])
            result = {
                "result_type": "chunk",
                "chunk_id": chunk["chunk_id"],
                "document_id": chunk["document_id"],
                "document_title": doc.title if doc else "External Source Document",
                "document_url": doc.url if doc else "#",
                "excerpt": chunk["chunk_text"][:300],
                "rrf_score": rrf_score,
            }

        fused.append(result)

    # ── Step 4: Sort by RRF score descending ────────────────────────────────
    fused.sort(key=lambda x: x["rrf_score"], reverse=True)
    return fused[:top_k]
