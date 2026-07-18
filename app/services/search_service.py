"""
Learning OS — FTS5 Indexing & Search Service.
Manages the virtual SQLite search index table.
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

    @staticmethod
    def rebuild_search_index():
        """Create and populate the SQLite FTS5 virtual table for lessons search."""
        if not SearchIndexService.is_sqlite():
            logger.info("SearchIndexService: Database dialect is not SQLite. Skipping FTS5 indexing.")
            return

        connection = db.engine.raw_connection()
        try:
            cursor = connection.cursor()
            
            # 1. Create virtual table using FTS5 extension
            cursor.execute("""
                CREATE VIRTUAL TABLE IF NOT EXISTS lesson_search_idx USING fts5(
                    lesson_id,
                    title,
                    summary,
                    content_markdown,
                    tokenize="porter unicode61"
                );
            """)
            
            # 2. Clear old index records
            cursor.execute("DELETE FROM lesson_search_idx;")
            
            # 3. Query all published lessons
            cursor.execute("""
                SELECT id, title, summary
                FROM lessons
                WHERE status = 'published' AND is_deleted = 0;
            """)
            lessons = cursor.fetchall()
            
            for row in lessons:
                lesson_id, title, summary = row
                # Query content markdown from visible lesson sections
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
            # Fallback to standard LIKE matching
            pattern = f"%{query_string}%"
            results = Lesson.query.filter(
                (Lesson.title.ilike(pattern)) |
                (Lesson.summary.ilike(pattern))
            ).limit(limit).all()
            return [{"lesson_id": l.id, "title": l.title, "rank": idx + 1} for idx, l in enumerate(results)]

        connection = db.engine.raw_connection()
        try:
            cursor = connection.cursor()
            # Verify if FTS5 table exists
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='lesson_search_idx';")
            if not cursor.fetchone():
                # Rebuild index if missing
                SearchIndexService.rebuild_search_index()
            
            # Perform MATCH search
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
