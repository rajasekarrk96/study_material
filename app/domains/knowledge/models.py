"""
Learning OS — Knowledge Domain Models
Includes both the original vector search tables (KnowledgeSource, SourceDocument, KnowledgeChunk, ChunkEmbedding)
and the new v2.3 Media and Search indexes (Media, MediaFolder, MediaTag, MediaReference, SearchDocument, SearchChunk, SearchKeyword).
"""
import json
from datetime import datetime
from app.core.extensions import db
from app.core.base_model import TimestampMixin


# ─────────────────────────────────────────────────────────────
# Original Knowledge Search & Vector Embeddings
# ─────────────────────────────────────────────────────────────

class KnowledgeSource(db.Model, TimestampMixin):
    """
    A tracked external knowledge origin (YouTube channel, docs page, book, blog, repo).
    """
    __tablename__ = "knowledge_sources"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    source_type = db.Column(db.String(50), nullable=False)   # youtube | docs | book | blog | github
    base_url = db.Column(db.String(512), nullable=True)
    is_active = db.Column(db.Boolean, default=True)

    documents = db.relationship("SourceDocument", back_populates="source", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<KnowledgeSource {self.name}>"


class SourceDocument(db.Model, TimestampMixin):
    """
    A single page, article, video transcript, or chapter imported from a KnowledgeSource.
    """
    __tablename__ = "source_documents"

    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.Integer, db.ForeignKey("knowledge_sources.id"), nullable=False)
    title = db.Column(db.String(512), nullable=False)
    url = db.Column(db.String(1024), nullable=True)
    raw_text = db.Column(db.Text, nullable=False)
    is_chunked = db.Column(db.Boolean, default=False)

    source = db.relationship("KnowledgeSource", back_populates="documents")
    chunks = db.relationship("KnowledgeChunk", back_populates="document", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<SourceDocument {self.title[:40]}>"


class KnowledgeChunk(db.Model):
    """
    A 500-character text segment extracted from a SourceDocument for vector indexing.
    """
    __tablename__ = "knowledge_chunks"

    id = db.Column(db.Integer, primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey("source_documents.id"), nullable=False)
    chunk_index = db.Column(db.Integer, nullable=False)
    chunk_text = db.Column(db.Text, nullable=False)
    is_embedded = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    document = db.relationship("SourceDocument", back_populates="chunks")
    embedding = db.relationship("ChunkEmbedding", back_populates="chunk", uselist=False, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<KnowledgeChunk doc={self.document_id} idx={self.chunk_index}>"


class ChunkEmbedding(db.Model):
    """
    Stores the float vector embedding for a KnowledgeChunk as a JSON-encoded list.
    """
    __tablename__ = "chunk_embeddings"

    id = db.Column(db.Integer, primary_key=True)
    chunk_id = db.Column(db.Integer, db.ForeignKey("knowledge_chunks.id"), nullable=False, unique=True)
    embedding_json = db.Column(db.Text, nullable=False)   # JSON-encoded float list
    embedding_model = db.Column(db.String(100), default="nomic-embed-text")
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    chunk = db.relationship("KnowledgeChunk", back_populates="embedding")

    def get_vector(self) -> list[float]:
        return json.loads(self.embedding_json)

    def set_vector(self, vector: list[float]) -> None:
        self.embedding_json = json.dumps(vector)

    def __repr__(self):
        return f"<ChunkEmbedding chunk={self.chunk_id}>"


# ─────────────────────────────────────────────────────────────
# v2.3 Media & Decoupled Search Library
# ─────────────────────────────────────────────────────────────

class MediaFolder(db.Model, TimestampMixin):
    __tablename__ = "media_folders"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    media_items = db.relationship("Media", back_populates="folder", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<MediaFolder {self.name}>"


class Media(db.Model, TimestampMixin):
    __tablename__ = "media"

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(1000), nullable=False)
    file_type = db.Column(db.String(100), nullable=False)
    file_size = db.Column(db.Integer, nullable=False)
    folder_id = db.Column(db.Integer, db.ForeignKey("media_folders.id"), nullable=True)
    created_by_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)

    folder = db.relationship("MediaFolder", back_populates="media_items")
    references = db.relationship("MediaReference", back_populates="media", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Media {self.filename}>"


class MediaTag(db.Model):
    __tablename__ = "media_tags"

    media_id = db.Column(db.Integer, db.ForeignKey("media.id"), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"), primary_key=True)


class MediaReference(db.Model, TimestampMixin):
    __tablename__ = "media_references"

    id = db.Column(db.Integer, primary_key=True)
    media_id = db.Column(db.Integer, db.ForeignKey("media.id"), nullable=False)
    target_type = db.Column(db.String(50), nullable=False)  # 'lesson', 'topic' etc.
    target_id = db.Column(db.Integer, nullable=False)

    media = db.relationship("Media", back_populates="references")

    def __repr__(self):
        return f"<MediaReference media={self.media_id} target={self.target_type}:{self.target_id}>"


class SearchDocument(db.Model):
    __tablename__ = "search_documents"

    id = db.Column(db.Integer, primary_key=True)
    target_type = db.Column(db.String(50), nullable=False)  # 'course', 'lesson', 'topic'
    target_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)

    chunks = db.relationship("SearchChunk", back_populates="document", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<SearchDocument {self.target_type}:{self.target_id}>"


class SearchChunk(db.Model):
    __tablename__ = "search_chunks"

    id = db.Column(db.Integer, primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey("search_documents.id"), nullable=False)
    chunk_index = db.Column(db.Integer, nullable=False)
    text_chunk = db.Column(db.Text, nullable=False)

    document = db.relationship("SearchDocument", back_populates="chunks")
    keywords = db.relationship("SearchKeyword", back_populates="chunk", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<SearchChunk doc={self.document_id} idx={self.chunk_index}>"


class SearchKeyword(db.Model):
    __tablename__ = "search_keywords"

    id = db.Column(db.Integer, primary_key=True)
    chunk_id = db.Column(db.Integer, db.ForeignKey("search_chunks.id"), nullable=False)
    keyword = db.Column(db.String(255), nullable=False, index=True)

    chunk = db.relationship("SearchChunk", back_populates="keywords")

    def __repr__(self):
        return f"<SearchKeyword {self.keyword}>"
