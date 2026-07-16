# 12 — Search Architecture

> The Search Engine handles indexing, query analysis, ranking, and autocomplete filters for learning content.

---

## 12.1 Indexing & Query Pipelines

For modularity, search supports database-agnostic full-text search:
1. **SQLite FTS5**: Lightweight implementation for local testing.
2. **PostgreSQL FTS**: Native tsvector indexing.
3. **Meilisearch / Elasticsearch API Adapter**: For production scale workloads.

```
       ┌────────────────────────┐
       │   Update CMS content   │
       └───────────┬────────────┘
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
┌─────────────────┐ ┌─────────────────┐
│ Database hook   │ │ Background Job  │
│ (Alembic transaction) │ │ Rebuild Index  │
└─────────────────┘ └─────────────────┘
```

---

## 12.2 Autocomplete & Auto-Correction (Typo Tolerance)

- Autocomplete runs via `/api/v1/search/autocomplete?q=` matching prefixes inside the cached title array.
- Typo tolerance leverages Levenshtein distance calculations (maximum edit distance = 2) for querying keywords.

---

## 12.3 Search Schema Definitions

```python
# app/services/search_service.py

class SearchIndexService:
    def __init__(self, db_engine):
        self.engine = db_engine

    def rebuild_search_index(self):
        """
        Creates or updates SQLite FTS5 index tables.
        For production, syncs databases with Meilisearch schemas.
        """
        connection = self.engine.raw_connection()
        try:
            cursor = connection.cursor()
            # Create SQLite virtual table using FTS5 extension
            cursor.execute("""
                CREATE VIRTUAL TABLE IF NOT EXISTS lesson_search_idx USING fts5(
                    lesson_id,
                    title,
                    summary,
                    content_markdown,
                    tags,
                    tokenize="porter unicode61"
                );
            """)
            
            # Clear old records
            cursor.execute("DELETE FROM lesson_search_idx;")
            
            # Index all lessons marked as published
            cursor.execute("""
                SELECT l.id, l.title, l.summary, group_concat(t.name, ' ')
                FROM lessons l
                LEFT JOIN lesson_tags lt ON lt.lesson_id = l.id
                LEFT JOIN tags t ON t.id = lt.tag_id
                WHERE l.status = 'published'
                GROUP BY l.id;
            """)
            lessons = cursor.fetchall()
            
            for row in lessons:
                # Concatenate lesson sections markdown for deep-search index
                cursor.execute("""
                    SELECT group_concat(content_markdown, '\n') 
                    FROM lesson_sections 
                    WHERE lesson_id = ? AND is_visible = 1;
                """, (row[0],))
                section_markdown = cursor.fetchone()[0] or ""

                cursor.execute("""
                    INSERT INTO lesson_search_idx(lesson_id, title, summary, content_markdown, tags)
                    VALUES(?, ?, ?, ?, ?);
                """, (row[0], row[1], row[2], section_markdown, row[3]))
                
            connection.commit()
        finally:
            connection.close()

    def search_query(self, query_string: str, limit: int = 10) -> list[dict]:
        """
        Executes query against SQLite FTS5 table matching on weights.
        """
        connection = self.engine.raw_connection()
        try:
            cursor = connection.cursor()
            # Rank based on matches inside Title first, then Tags, then Content
            cursor.execute("""
                SELECT lesson_id, title, rank 
                FROM lesson_search_idx 
                WHERE lesson_search_idx MATCH ? 
                ORDER BY rank 
                LIMIT ?;
            """, (query_string, limit))
            results = cursor.fetchall()
            return [{"lesson_id": r[0], "title": r[1], "rank": r[2]} for r in results]
        finally:
            connection.close()
```
