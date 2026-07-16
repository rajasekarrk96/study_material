"""
Learning OS — Document Chunker & Vector Embedding Service.
Splits raw text into overlapping 500-character chunks and stores embeddings via the AI provider.
"""
import logging
from app.core.extensions import db
from app.domains.knowledge.models import SourceDocument, KnowledgeChunk, ChunkEmbedding
from app.providers.registry import get_provider

logger = logging.getLogger(__name__)

CHUNK_SIZE = 500       # characters per chunk
CHUNK_OVERLAP = 50     # overlap to preserve context across boundaries


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    """
    Split raw text into overlapping character-level chunks.
    Returns a list of chunk strings.
    """
    chunks = []
    start = 0
    text = text.strip()
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks


def process_document(document_id: int) -> int:
    """
    Chunk and embed all text for a SourceDocument.
    Returns the count of chunks created.
    """
    doc = db.session.get(SourceDocument, document_id)
    if not doc:
        logger.error("SourceDocument id=%d not found.", document_id)
        return 0

    if doc.is_chunked:
        logger.info("Document id=%d already chunked. Skipping.", document_id)
        return 0

    raw_chunks = chunk_text(doc.raw_text)
    provider = get_provider()
    count = 0

    for idx, chunk_text_str in enumerate(raw_chunks):
        # Create chunk record
        chunk = KnowledgeChunk(
            document_id=doc.id,
            chunk_index=idx,
            chunk_text=chunk_text_str
        )
        db.session.add(chunk)
        db.session.flush()  # get chunk.id

        # Get embedding vector
        vector = provider.embeddings(chunk_text_str)

        # Store embedding
        emb = ChunkEmbedding(chunk_id=chunk.id)
        emb.set_vector(vector)
        emb.embedding_model = provider.name
        chunk.is_embedded = True
        db.session.add(emb)
        count += 1

    doc.is_chunked = True
    db.session.commit()
    logger.info("Chunked document id=%d into %d chunks.", document_id, count)
    return count


def cosine_similarity(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two embedding vectors."""
    if len(a) != len(b) or not a:
        return 0.0
    dot = sum(x * y for x, y in zip(a, b))
    mag_a = sum(x * x for x in a) ** 0.5
    mag_b = sum(x * x for x in b) ** 0.5
    if mag_a == 0 or mag_b == 0:
        return 0.0
    return dot / (mag_a * mag_b)


def vector_search(query: str, top_k: int = 10) -> list[dict]:
    """
    Retrieve the top-k most semantically similar chunks using cosine similarity.
    Returns a list of dicts: {chunk_id, document_id, chunk_text, score}.
    """
    provider = get_provider()
    query_vector = provider.embeddings(query)

    # Fetch all stored embeddings (batched in production; fine for dev scale)
    all_embeddings = ChunkEmbedding.query.all()
    scored = []

    for emb in all_embeddings:
        stored_vector = emb.get_vector()
        score = cosine_similarity(query_vector, stored_vector)
        scored.append({
            "chunk_id": emb.chunk_id,
            "document_id": emb.chunk.document_id,
            "chunk_text": emb.chunk.chunk_text,
            "score": score
        })

    # Sort by similarity descending
    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:top_k]
