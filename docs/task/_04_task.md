# Task 04 — AI Layer & Hybrid Search Engine

> **Goal**: Configure the local AI model (Ollama) gateways, configure the prompt templates, set up text chunking, build the vector index, and design the hybrid search (FTS5 + Vector Similarity) system.

---

## 4.1 Local Ollama Gateway & Provider Abstraction
- [x] Provider Plug-ins (`app/providers/plugins/ollama.py`):
  - Setup gateway hooks targeting `http://localhost:11434` to run model configurations (Qwen, Llama, DeepSeek).
  - Code fallbacks parameters switching to cloud platforms if local servers are unavailable.
- [x] System Prompts Registries:
  - Add templates for concept explanations, code simplifications, quiz/exercise generators, and technology comparisons.

---

## 4.2 Ingestion Chunker & Vector Embeddings Index
- [x] Document Chunker Service:
  - Setup parsers splitting documents into 500-character overlaps.
  - Create models `knowledge_sources`, `source_documents`, `knowledge_chunks`, and `chunk_embeddings`.
- [x] Vector Database Layer (SQLite-VSS / PGVector):
  - Setup sqlite-vss bindings locally.
  - Index chunk text contents by sending float calculations to the embedding service.

---

## 4.3 Hybrid Search & Recommendations Engine
- [x] Search Integration controllers:
  - Write reciprocal rank fusion (RRF) algorithms merging SQLite FTS5 search ranks with vector distance floats.
  - Implement `/api/v1/search/hybrid` REST api.
- [x] Vector Similarity Recommendation Service:
  - Code user interest calculators analyzing tag overlap metrics and cosine similarity matrices.

---

## 🛑 CHECKPOINT & BREAK POINT
- Test Ollama local communication using a mock prompt and checking the terminal response.
- Execute vector queries against the database chunks index and verify returned records align with topic contexts.
- **Action**: Pause and request approval before constructing admin workflows and RBAC decorators.
