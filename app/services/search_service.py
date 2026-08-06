"""
Learning OS — FTS5 Indexing & Decoupled Search Service.
Manages both SQLite virtual search tables and decoupled keyword search indices.
"""
import logging
from app.core.extensions import db
from app.domains.content.models import Lesson

logger = logging.getLogger(__name__)


class SearchIndexService:
    @staticmethod
    def is_sqlite() -> bool:
        try:
            return db.engine.dialect.name == "sqlite"
        except Exception:
            return True

    # ── 1. Decoupled Production-Safe Search Index ──────────────────────────────
    @staticmethod
    def index_document(target_type: str, target_id: int, content: str) -> None:
        """Indexes a course, lesson, or topic into the decoupled SearchDocument structures."""
        from app.domains.knowledge.models import SearchDocument, SearchChunk, SearchKeyword
        
        # Clean query: find or create document
        doc = SearchDocument.query.filter_by(target_type=target_type, target_id=target_id).first()
        if not doc:
            doc = SearchDocument(target_type=target_type, target_id=target_id, content=content)
            db.session.add(doc)
            db.session.flush()
        else:
            doc.content = content
            # Delete old chunks and keywords cascade
            SearchChunk.query.filter_by(document_id=doc.id).delete()
            db.session.flush()

        # Split content into chunks of e.g. 500 characters
        chunk_size = 500
        chunks_text = [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]
        
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'is', 'are', 'was', 'were', 'to', 'for', 'of', 'in', 'on', 'at', 'by', 'with', 'from', 'as', 'it', 'this', 'that', 'these', 'those', 'they', 'them', 'their', 'his', 'her', 'its'}
        
        for idx, text_val in enumerate(chunks_text):
            if not text_val.strip():
                continue
            chunk = SearchChunk(document_id=doc.id, chunk_index=idx, text_chunk=text_val)
            db.session.add(chunk)
            db.session.flush()
            
            # Extract keywords (words of length 3 to 50)
            import re
            words = re.findall(r'\b\w{3,50}\b', text_val.lower())
            unique_words = set(words) - stop_words
            
            for word in unique_words:
                kw = SearchKeyword(chunk_id=chunk.id, keyword=word)
                db.session.add(kw)
        
        db.session.commit()

    @staticmethod
    def decoupled_search(query_string: str, limit: int = 20) -> list[dict]:
        """Perform a keywords matching search against the search index tables, return target documents."""
        from app.domains.knowledge.models import SearchDocument, SearchChunk, SearchKeyword
        import re
        
        query_words = re.findall(r'\b\w{3,50}\b', query_string.lower())
        if not query_words:
            return []
            
        # Count frequency of matches per chunk
        from sqlalchemy import func
        matches = db.session.query(
            SearchChunk.document_id,
            SearchChunk.chunk_index,
            SearchChunk.text_chunk,
            func.count(SearchKeyword.id).label("score")
        ).join(
            SearchKeyword, SearchKeyword.chunk_id == SearchChunk.id
        ).filter(
            SearchKeyword.keyword.in_(query_words)
        ).group_by(
            SearchChunk.document_id,
            SearchChunk.chunk_index,
            SearchChunk.text_chunk
        ).order_by(
            func.count(SearchKeyword.id).desc()
        ).limit(limit).all()
        
        results = []
        for doc_id, chunk_idx, chunk_text, score in matches:
            doc = db.session.get(SearchDocument, doc_id)
            if doc:
                results.append({
                    "target_type": doc.target_type,
                    "target_id": doc.target_id,
                    "chunk_index": chunk_idx,
                    "text_chunk": chunk_text,
                    "score": score
                })
        return results

    # ── 2. Legacy SQLite-only FTS5 Search Index ────────────────────────────────
    @staticmethod
    def rebuild_search_index():
        """Create and populate the SQLite FTS5 virtual table for lessons search."""
        if not SearchIndexService.is_sqlite():
            logger.info("SearchIndexService: Database dialect is not SQLite. Skipping FTS5 indexing.")
            return

        connection = db.engine.raw_connection()
        try:
            cursor = connection.cursor()
            
            cursor.execute("""
                CREATE VIRTUAL TABLE IF NOT EXISTS lesson_search_idx USING fts5(
                    lesson_id,
                    title,
                    summary,
                    content_markdown,
                    tokenize="porter unicode61"
                );
            """)
            
            cursor.execute("DELETE FROM lesson_search_idx;")
            
            cursor.execute("""
                SELECT id, title, summary
                FROM lessons
                WHERE status = 'published' AND is_deleted = 0;
            """)
            lessons = cursor.fetchall()
            
            for row in lessons:
                lesson_id, title, summary = row
                cursor.execute("""
                    SELECT content_markdown 
                    FROM lesson_sections 
                    WHERE lesson_id = ? AND is_visible = 1;
                """, (lesson_id,))
                sections = cursor.fetchall()
                section_markdown = "\n".join([s[0] for s in sections if s[0]])
                
                cursor.execute("""
                    INSERT INTO lesson_search_idx(lesson_id, title, summary, content_markdown)
                    VALUES(?, ?, ?, ?);
                """, (lesson_id, title, summary or "", section_markdown))
                
            connection.commit()
            logger.info("FTS5 search index rebuilt successfully.")
        except Exception as e:
            logger.error("Error rebuilding FTS5 search index: %s", e)
        finally:
            connection.close()

    @staticmethod
    def search_query(query_string: str, limit: int = 20) -> list[dict]:
        """Execute query against SQLite FTS5 table matching on weights, falling back to LIKE matches if not SQLite."""
        if not query_string.strip():
            return []

        if not SearchIndexService.is_sqlite():
            pattern = f"%{query_string}%"
            results = Lesson.query.filter(
                (Lesson.title.ilike(pattern)) |
                (Lesson.summary.ilike(pattern))
            ).limit(limit).all()
            return [{"lesson_id": l.id, "title": l.title, "rank": idx + 1} for idx, l in enumerate(results)]

        connection = db.engine.raw_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='lesson_search_idx';")
            if not cursor.fetchone():
                SearchIndexService.rebuild_search_index()
            
            cursor.execute("""
                SELECT lesson_id, title, rank 
                FROM lesson_search_idx 
                WHERE lesson_search_idx MATCH ? 
                ORDER BY rank 
                LIMIT ?;
            """, (query_string, limit))
            results = cursor.fetchall()
            return [{"lesson_id": int(r[0]), "title": r[1], "rank": idx + 1} for idx, r in enumerate(results)]
        except Exception as e:
            logger.warning("FTS5 MATCH search failed, falling back to LIKE: %s", e)
            pattern = f"%{query_string}%"
            results = Lesson.query.filter(
                (Lesson.title.ilike(pattern)) |
                (Lesson.summary.ilike(pattern))
            ).limit(limit).all()
            return [{"lesson_id": l.id, "title": l.title, "rank": idx + 1} for idx, l in enumerate(results)]
        finally:
            connection.close()
