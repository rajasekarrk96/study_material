"""
Learning OS — Knowledge Source & Vector Embedding Domain Models.
Models: KnowledgeSource, SourceDocument, KnowledgeChunk, ChunkEmbedding.
"""
import json
from datetime import datetime
from app.core.extensions import db
from app.core.base_model import TimestampMixin


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
    Note: For TiDB/MySQL production, this is stored as LONGTEXT JSON.
    For sqlite-vss, the companion VSS table is created separately via a migration script.
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
