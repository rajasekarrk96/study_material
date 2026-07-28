# Phase 6: RAG Engineering — Enterprise Syllabus
## Learning OS Enterprise Standard | Curriculum Architecture v2.0

**Classification**: Chief Curriculum Architect — Syllabus Design Document  
**Phase**: 6 of 8  
**Domain**: Retrieval-Augmented Generation Engineering  
**Required Previous Phases**: Phase 4 (NLP), Phase 5 (Gen AI & LLMs)  
**Folder Root**: `docs/curriculum/_15_rag_engineering/`  
**Last Updated**: 2026-07-28

---

## Dependency Graph

```
_13_nlp  (Phase 4 — Dense Retrieval, BM25, Semantic Search)
_14_generative_ai_llms  (Phase 5 — LLM Inference, Prompt Engineering)
    └─> _15_rag_engineering  ◄── THIS PHASE
            └─> _16_ai_agents  (Phase 7)
```

Cross-phase reuse nodes:
- `NLP.13_08` Text Retrieval → extended with RAG-specific pipeline
- `NLP.13_08_07` Passage chunking → extended strategies
- `GenAI.14_05` Prompt Engineering → RAG prompt templates
- `GenAI.14_08` LLM Inference → RAG generation backend
- `GenAI.14_07_03` Hallucination → RAG as mitigation
- `CV.12_05` Document Intelligence → multimodal RAG

---

## Skills Gained (This Phase)

- Design and build production-grade RAG pipelines end-to-end
- Engineer optimal chunking strategies for diverse document types
- Select and configure vector databases for scale
- Implement advanced retrieval: HyDE, RAG-Fusion, multi-hop
- Build re-ranking pipelines for precision improvement
- Evaluate RAG systems with RAGAS, TruLens, DeepEval
- Apply GraphRAG and knowledge graph-enhanced retrieval
- Build multimodal RAG (images, tables, audio)
- Deploy RAG APIs with observability and guardrails
- Implement streaming RAG for real-time applications

---

## Course Structure

```
_15_rag_engineering/
├── _15_01_rag_fundamentals/
├── _15_02_document_processing_and_chunking/
├── _15_03_embeddings_for_rag/
├── _15_04_vector_databases/
├── _15_05_advanced_retrieval/
├── _15_06_generation_and_augmentation/
├── _15_07_rag_evaluation/
├── _15_08_production_rag_systems/
└── _15_09_industry_projects/
```

---

## MODULE 01 — RAG Fundamentals

**Folder**: `_15_01_rag_fundamentals/`  
**Lesson Count**: 6  
**Learning Order**: 1st

### Lessons

#### Lesson 01.01 — What is RAG and Why It Matters
**File**: `_15_01_01_what_is_rag_and_why.md`

| Topics | Subtopics |
|---|---|
| LLM knowledge cutoff | Static parametric knowledge |
| RAG concept | Retrieve → Augment → Generate |
| RAG vs fine-tuning | When to use which |
| RAG vs long context | Trade-offs |
| RAG taxonomy | Naive, Advanced, Modular, Agentic |
| Use cases | QA, search, chatbot, summarization |
| Business value | Factuality, updatability, auditability |

---

#### Lesson 01.02 — Naive RAG Architecture
**File**: `_15_01_02_naive_rag_architecture.md`

| Topics | Subtopics |
|---|---|
| Indexing pipeline | Load → Chunk → Embed → Store |
| Retrieval pipeline | Query → Embed → Search → Top-K |
| Augmentation | Context stuffing into prompt |
| Generation | LLM answer with context |
| `langchain` naive RAG | `RetrievalQA`, `load_qa_chain` |
| `llama_index` naive RAG | `VectorStoreIndex`, `query_engine` |
| Failure modes | Retrieval misses, lost in middle, hallucination |

---

#### Lesson 01.03 — RAG Frameworks Overview
**File**: `_15_01_03_rag_frameworks_overview.md`

| Topics | Subtopics |
|---|---|
| LangChain | LCEL, chains, retrievers, memory |
| LlamaIndex | Document stores, query engines, pipelines |
| Haystack | DocumentStore, Pipeline, REST API |
| DSPy | Declarative RAG, automated optimization |
| `ragas` | Evaluation framework |
| Framework comparison | Use case fit, complexity, community |
| When to go custom | Framework-free pure pipeline |

---

#### Lesson 01.04 — RAG Data Flow and Components
**File**: `_15_01_04_rag_data_flow_components.md`

| Topics | Subtopics |
|---|---|
| Document loader | PDF, DOCX, HTML, CSV, JSON, DB |
| Splitter / Chunker | Strategy, size, overlap |
| Embedding model | Bi-encoder, pooling |
| Vector store | FAISS, Qdrant, Chroma, Pinecone |
| Retriever | ANN search, metadata filter |
| Reranker | Cross-encoder, ColBERT |
| LLM | Generator, with system + context prompt |
| Output parser | Structured response extraction |

---

#### Lesson 01.05 — LangChain LCEL Pipeline
**File**: `_15_01_05_langchain_lcel_pipeline.md`

| Topics | Subtopics |
|---|---|
| LCEL | LangChain Expression Language, composable |
| `RunnablePassthrough` | Pass input through |
| `RunnableParallel` | Parallel execution |
| Chains | `prompt \| llm \| parser` |
| `ChatPromptTemplate` | System + human messages |
| `StrOutputParser` | String extraction |
| RAG chain | `retriever \| format_docs \| prompt \| llm \| parser` |
| Streaming | `.stream()`, `.astream()` |

---

#### Lesson 01.06 — LlamaIndex Core Concepts
**File**: `_15_01_06_llamaindex_core_concepts.md`

| Topics | Subtopics |
|---|---|
| `Document` | Text + metadata |
| `Node` | Chunk of text, relationships |
| `VectorStoreIndex` | Index for retrieval |
| `QueryEngine` | Query → retrieve → synthesize |
| `RetrieverQueryEngine` | Custom retriever + synthesizer |
| `NodePostprocessor` | Re-ranking, filtering |
| `ServiceContext` / `Settings` | LLM, embed model config |
| Response synthesizers | Compact, refine, tree summarize |

---

## MODULE 02 — Document Processing and Chunking

**Folder**: `_15_02_document_processing_and_chunking/`  
**Lesson Count**: 7  
**Learning Order**: 2nd

### Lessons

#### Lesson 02.01 — Document Loaders
**File**: `_15_02_01_document_loaders.md`

| Topics | Subtopics |
|---|---|
| PDF loading | `PyPDFLoader`, `pdfplumber`, `pymupdf` (fitz) |
| DOCX loading | `python-docx`, `UnstructuredWordDocumentLoader` |
| HTML loading | `BeautifulSoup`, `UnstructuredHTMLLoader` |
| Web scraping | `WebBaseLoader`, `AsyncChromiumLoader` |
| CSV/JSON | `CSVLoader`, `JSONLoader`, jq schema |
| Database | SQL → documents pipeline |
| `unstructured` library | Universal document parsing |
| Metadata extraction | Author, date, source, page number |

---

#### Lesson 02.02 — Fixed-Size Chunking
**File**: `_15_02_02_fixed_size_chunking.md`

| Topics | Subtopics |
|---|---|
| `RecursiveCharacterTextSplitter` | `chunk_size`, `chunk_overlap`, separators |
| `CharacterTextSplitter` | Simple delimiter |
| Chunk size selection | 256, 512, 1024 — tradeoffs |
| Overlap | Preserve boundary context |
| Token-based splitting | `TokenTextSplitter`, model-aware |
| Adding metadata | Source, page, chunk index |
| Visualization | Chunk boundaries inspection |

---

#### Lesson 02.03 — Semantic and Sentence Chunking
**File**: `_15_02_03_semantic_sentence_chunking.md`

| Topics | Subtopics |
|---|---|
| Sentence splitting | `SentenceSplitter` (LlamaIndex) |
| Semantic chunking | Group similar sentences |
| `SemanticChunker` (LangChain) | Embedding similarity threshold |
| Propositions chunking | Dense X Retrieval |
| Late chunking | Embed full doc → pool chunk embeddings |
| `chonkie` library | Fast semantic chunking |
| Evaluation | Retrieval recall by chunk strategy |

---

#### Lesson 02.04 — Structure-Aware Chunking
**File**: `_15_02_04_structure_aware_chunking.md`

| Topics | Subtopics |
|---|---|
| Markdown splitter | `MarkdownHeaderTextSplitter` |
| HTML splitter | `HTMLHeaderTextSplitter`, tag-aware |
| Code splitter | `Language.PYTHON`, `Language.JS` |
| Table-aware | Keep tables intact, separate embedding |
| Section-level | Header → subsection hierarchy |
| `unstructured` elements | Title, NarrativeText, Table, Image |

---

#### Lesson 02.05 — Hierarchical and Multi-Granularity Chunking
**File**: `_15_02_05_hierarchical_multi_granularity_chunking.md`

| Topics | Subtopics |
|---|---|
| Parent document retriever | Store small, retrieve parent |
| `ParentDocumentRetriever` | LangChain implementation |
| Sentence-window retrieval | Retrieve sentence, expand window |
| LlamaIndex hierarchical | Chunk sizes: 2048 → 512 → 128 |
| Multi-granularity indexing | Query routing by granularity |
| Proposition indexing | Sub-sentence factual claims |

---

#### Lesson 02.06 — Multimodal Document Processing
**File**: `_15_02_06_multimodal_document_processing.md`

| Topics | Subtopics |
|---|---|
| PDF with images | Extract images + captions + text |
| `pymupdf` image extraction | `page.get_images()` |
| Table extraction | `camelot`, `pdfplumber`, `table-transformer` |
| OCR integration | `surya` for scanned PDFs |
| Caption generation | LLM/LVLM for image description |
| Multimodal nodes | LlamaIndex `ImageNode` |
| Indexing strategy | Separate text + image embeddings |

---

#### Lesson 02.07 — Chunking Evaluation and Selection
**File**: `_15_02_07_chunking_evaluation_selection.md`

| Topics | Subtopics |
|---|---|
| Retrieval recall | Measure chunk contains answer |
| Context precision | Chunks relevant to query |
| Chunk size impact | Short vs long chunk recall/precision |
| Overlap impact | 0% vs 10% vs 20% overlap |
| Strategy comparison | Fixed vs semantic vs hierarchical |
| `ragas` chunking eval | `context_recall`, `context_precision` |
| Decision matrix | Document type → recommended strategy |

---

## MODULE 03 — Embeddings for RAG

**Folder**: `_15_03_embeddings_for_rag/`  
**Lesson Count**: 6  
**Learning Order**: 3rd

### Lessons

#### Lesson 03.01 — Embedding Model Selection
**File**: `_15_03_01_embedding_model_selection.md`

| Topics | Subtopics |
|---|---|
| MTEB benchmark | Leaderboard for retrieval/STS |
| `text-embedding-3-small/large` | OpenAI embeddings |
| `all-MiniLM-L6-v2` | Fast 384-dim |
| `all-mpnet-base-v2` | 768-dim, general purpose |
| `e5-large-v2` / `e5-mistral-7b` | Strong retrieval models |
| `bge-large-en` / `bge-m3` | BAAI state-of-the-art |
| `nomic-embed-text` | Local, 8192 context |
| Multilingual | `multilingual-e5`, `bge-m3` |

---

#### Lesson 03.02 — Embedding APIs and Local Models
**File**: `_15_03_02_embedding_apis_local_models.md`

| Topics | Subtopics |
|---|---|
| OpenAI `embeddings.create` | `text-embedding-3-*`, dimensions |
| Cohere `embed.create` | `input_type` parameter |
| `sentence-transformers` | `model.encode()`, batch_size |
| `fastembed` | Fast C++ inference, `TextEmbedding` |
| `Ollama` embeddings | `ollama.embeddings()`, local |
| Batching | Efficient bulk embedding |
| Caching | `CacheBackedEmbeddings` (LangChain) |

---

#### Lesson 03.03 — Late Interaction Models (ColBERT)
**File**: `_15_03_03_late_interaction_colbert.md`

| Topics | Subtopics |
|---|---|
| ColBERT concept | Token-level embeddings, MaxSim |
| Full vs late interaction | Bi-encoder vs ColBERT |
| `colbert-ir/colbertv2.0` | Pretrained ColBERT |
| `RAGatouille` | Easy ColBERT indexing + retrieval |
| PLAID | Efficient ColBERT inference |
| ColBERT vs bi-encoder | Accuracy vs speed tradeoff |

---

#### Lesson 03.04 — Fine-Tuning Embedding Models
**File**: `_15_03_04_fine_tuning_embedding_models.md`

| Topics | Subtopics |
|---|---|
| When to fine-tune | Domain-specific terminology |
| Training data | (query, positive, negative) triplets |
| Loss functions | MultipleNegativesRankingLoss, TripletLoss |
| `sentence-transformers` training | `SentenceTransformerTrainer` |
| Hard negative mining | BM25 negatives, cross-encoder negatives |
| Evaluation | NDCG, Recall@K before/after |
| `Matryoshka` embeddings | Variable dimension at inference |

---

#### Lesson 03.05 — Sparse and Hybrid Embeddings
**File**: `_15_03_05_sparse_hybrid_embeddings.md`

| Topics | Subtopics |
|---|---|
| BM25 sparse vectors | Term-frequency weighted |
| SPLADE | Learned sparse representations |
| `fastembed` SPLADE | `SparseTextEmbedding` |
| Hybrid embeddings | Dense + sparse combined |
| Qdrant hybrid search | Sparse + dense in one query |
| Weaviate hybrid | BM25F + vector |
| Alpha weighting | Blend ratio tuning |

---

#### Lesson 03.06 — Embedding Storage and Management
**File**: `_15_03_06_embedding_storage_management.md`

| Topics | Subtopics |
|---|---|
| Embedding dimensionality | 384 / 768 / 1536 / 3072 |
| Storage formats | float32, float16, int8 |
| Materialized embeddings | Pre-compute, store, reuse |
| Embedding caching | Redis, DiskCache |
| Re-embedding triggers | Source update detection |
| Versioning | Model change → re-index strategy |
| Cost estimation | Tokens × price per 1M tokens |

---

## MODULE 04 — Vector Databases

**Folder**: `_15_04_vector_databases/`  
**Lesson Count**: 7  
**Learning Order**: 4th

### Lessons

#### Lesson 04.01 — Vector Database Fundamentals
**File**: `_15_04_01_vector_database_fundamentals.md`

| Topics | Subtopics |
|---|---|
| ANN algorithms | HNSW, IVF, PQ, LSH |
| HNSW | Hierarchical navigable small world |
| IVF | Inverted file index, k-means partitioning |
| PQ | Product quantization, subvector codes |
| Exact vs approximate | Recall vs speed tradeoff |
| Filtering | Pre-filter vs post-filter vs in-filter |
| Distance metrics | Cosine, dot product, L2 |

---

#### Lesson 04.02 — FAISS (Deep Dive)
**File**: `_15_04_02_faiss_deep_dive.md`

| Topics | Subtopics |
|---|---|
| `faiss.IndexFlatL2` | Exact search baseline |
| `faiss.IndexFlatIP` | Inner product (cosine with normalization) |
| `faiss.IndexIVFFlat` | Approximate with IVF |
| `faiss.IndexIVFPQ` | IVF + product quantization |
| `faiss.IndexHNSWFlat` | HNSW graph index |
| GPU FAISS | `faiss.StandardGpuResources` |
| `faiss.write_index` / `read_index` | Persistence |
| LangChain FAISS | `FAISS.from_documents` |

---

#### Lesson 04.03 — Chroma
**File**: `_15_04_03_chroma.md`

| Topics | Subtopics |
|---|---|
| `chromadb` | Embedded local or HTTP server |
| `PersistentClient` | Disk persistence |
| `HttpClient` | Remote Chroma server |
| Collections | `create_collection`, `get_or_create` |
| `add` / `query` / `delete` | CRUD operations |
| Metadata filtering | `where`, `where_document` |
| LangChain Chroma | `Chroma.from_documents` |
| LlamaIndex Chroma | `ChromaVectorStore` |

---

#### Lesson 04.04 — Qdrant
**File**: `_15_04_04_qdrant.md`

| Topics | Subtopics |
|---|---|
| Qdrant architecture | Collections, points, payloads |
| `qdrant-client` | `QdrantClient`, local and cloud |
| Collection creation | `VectorParams`, distance, HNSW |
| `upsert` / `search` / `delete` | Point operations |
| Payload filtering | `FieldCondition`, `Filter` |
| Named vectors | Multiple vectors per point |
| Sparse vector support | Hybrid search built-in |
| `qdrant_client.models` | Pydantic data types |

---

#### Lesson 04.05 — Pinecone
**File**: `_15_04_05_pinecone.md`

| Topics | Subtopics |
|---|---|
| Pinecone serverless | No infrastructure management |
| Index creation | `pc.create_index()`, dimension, metric |
| Namespace | Logical partitioning |
| `upsert` / `query` / `delete` | Managed operations |
| Metadata filtering | Key-value filter in query |
| `LangchainEmbeddings` | LangChain Pinecone integration |
| Pinecone Assistant | Built-in RAG API |
| Cost model | Serverless: queries + storage |

---

#### Lesson 04.06 — Weaviate
**File**: `_15_04_06_weaviate.md`

| Topics | Subtopics |
|---|---|
| Weaviate schema | Class, properties, vectorizer |
| Vectorizer modules | `text2vec-openai`, `text2vec-cohere` |
| `weaviate-client` v4 | `client.collections` API |
| `near_text` search | Semantic search |
| `hybrid` search | BM25F + vector |
| Generative module | `generative-openai`, RAG built-in |
| GraphQL queries | Advanced filtering |

---

#### Lesson 04.07 — Vector DB Selection and Operations
**File**: `_15_04_07_vector_db_selection_operations.md`

| Topics | Subtopics |
|---|---|
| Selection criteria | Scale, cost, filtering, hybrid |
| Comparison table | FAISS / Chroma / Qdrant / Pinecone / Weaviate |
| Batch upsert patterns | Efficient bulk insert |
| Index management | HNSW config tuning |
| Backup and restore | Snapshot strategies |
| Monitoring | Query latency, index size, recall |
| Multi-tenancy | Namespace, collection per tenant |

---

## MODULE 05 — Advanced Retrieval

**Folder**: `_15_05_advanced_retrieval/`  
**Lesson Count**: 8  
**Learning Order**: 5th

### Lessons

#### Lesson 05.01 — Hybrid Search
**File**: `_15_05_01_hybrid_search.md`

| Topics | Subtopics |
|---|---|
| BM25 + dense fusion | Why hybrid beats pure dense |
| Reciprocal Rank Fusion (RRF) | Score fusion formula |
| `BM25Retriever` (LangChain) | `rank_bm25` integration |
| `EnsembleRetriever` | Merge multiple retrievers |
| Qdrant hybrid search | Sparse + dense in one call |
| Weaviate hybrid | Built-in hybrid |
| Alpha tuning | Optimal blend ratio |

---

#### Lesson 05.02 — HyDE — Hypothetical Document Embeddings
**File**: `_15_05_02_hyde_hypothetical_documents.md`

| Topics | Subtopics |
|---|---|
| HyDE concept | Generate hypothetical answer → embed → retrieve |
| Why it works | Bridging query-document gap |
| `HypotheticalDocumentEmbedder` | LangChain implementation |
| LlamaIndex HyDE | `HyDEQueryTransform` |
| When HyDE helps | Complex questions, sparse queries |
| When HyDE hurts | Short factual queries |
| Evaluation | Recall comparison |

---

#### Lesson 05.03 — Query Transformation
**File**: `_15_05_03_query_transformation.md`

| Topics | Subtopics |
|---|---|
| Query rewriting | LLM improves query phrasing |
| Multi-query | Generate N variants, union results |
| `MultiQueryRetriever` | LangChain implementation |
| Step-back prompting | Generalize query before retrieval |
| Query decomposition | Break complex → sub-queries |
| `SubQuestionQueryEngine` | LlamaIndex |
| Query routing | Route to specialized retriever |

---

#### Lesson 05.04 — RAG-Fusion
**File**: `_15_05_04_rag_fusion.md`

| Topics | Subtopics |
|---|---|
| RAG-Fusion concept | Multiple queries + RRF |
| Pipeline | Query → N queries → N retrievals → RRF → Generate |
| Implementation | LangChain custom chain |
| Diversity | Different sub-queries cover different aspects |
| Evaluation | Recall vs naive RAG |

---

#### Lesson 05.05 — Multi-Hop and Iterative Retrieval
**File**: `_15_05_05_multi_hop_iterative_retrieval.md`

| Topics | Subtopics |
|---|---|
| Multi-hop question | Requires chaining multiple retrievals |
| IRCoT | Interleaved Retrieve + CoT |
| ReAct retrieval | Reason → retrieve → reason loop |
| `MultiStepQueryEngine` | LlamaIndex |
| Graph traversal retrieval | Follow entity relations |
| HotpotQA / 2WikiMultiHop | Multi-hop benchmarks |

---

#### Lesson 05.06 — Metadata Filtering and Routing
**File**: `_15_05_06_metadata_filtering_routing.md`

| Topics | Subtopics |
|---|---|
| Metadata at index time | `source`, `date`, `author`, `category` |
| Self-query retriever | LLM extracts metadata filter from query |
| `SelfQueryRetriever` | LangChain, `AttributeInfo` |
| Time-based filtering | Recent docs preference |
| Multi-source routing | Route to correct collection |
| `RouterQueryEngine` | LlamaIndex topic routing |
| Ensemble + filter | Hybrid with metadata filter |

---

#### Lesson 05.07 — Contextual Retrieval
**File**: `_15_05_07_contextual_retrieval.md`

| Topics | Subtopics |
|---|---|
| Contextual retrieval | Anthropic technique: add context to chunks |
| Chunk context generation | LLM summarizes chunk role in doc |
| `ContextualCompressionRetriever` | LangChain |
| `LLMChainExtractor` | Compress retrieved chunks |
| `EmbeddingsFilter` | Post-retrieval relevance filter |
| Reranking as compression | Cross-encoder to trim |

---

#### Lesson 05.08 — Re-Ranking
**File**: `_15_05_08_re_ranking.md`

| Topics | Subtopics |
|---|---|
| Why re-rank | ANN recall ≠ precision |
| Cross-encoder re-ranker | Full (query, doc) attention |
| `cross-encoder/ms-marco-*` | Standard re-rankers |
| `FlashRank` | Fast lightweight re-ranker |
| `Cohere Rerank` | API-based re-ranker |
| `ColBERT re-ranking` | MaxSim token-level |
| `RankLLM` | LLM-based listwise re-ranking |
| `ContextualCompressionRetriever` | LangChain rerank integration |

---

## MODULE 06 — Generation and Augmentation

**Folder**: `_15_06_generation_and_augmentation/`  
**Lesson Count**: 6  
**Learning Order**: 6th

### Lessons

#### Lesson 06.01 — RAG Prompt Templates
**File**: `_15_06_01_rag_prompt_templates.md`

| Topics | Subtopics |
|---|---|
| System prompt for RAG | "Answer based on context only" |
| Context formatting | Passage separator, numbering |
| Citation instruction | "Cite [Source N]" |
| No-answer instruction | "Say I don't know if not in context" |
| Few-shot RAG | Example Q+context+A in prompt |
| Language-specific templates | Multilingual RAG |
| `ChatPromptTemplate` | LangChain template |

---

#### Lesson 06.02 — Response Synthesis Strategies
**File**: `_15_06_02_response_synthesis_strategies.md`

| Topics | Subtopics |
|---|---|
| Stuff | Concatenate all chunks → one LLM call |
| Map-Reduce | LLM on each chunk → reduce |
| Refine | Iteratively refine answer per chunk |
| Map-Rerank | Score each chunk → best wins |
| Tree Summarize | Hierarchical summarization |
| LlamaIndex synthesizers | `compact`, `refine`, `tree_summarize` |
| When to use each | Token limit, accuracy, speed |

---

#### Lesson 06.03 — Streaming RAG
**File**: `_15_06_03_streaming_rag.md`

| Topics | Subtopics |
|---|---|
| Streaming LLM output | Token-by-token streaming |
| `chain.stream()` | LangChain streaming |
| `query_engine.aquery()` | LlamaIndex async |
| FastAPI SSE | `StreamingResponse`, `EventSourceResponse` |
| WebSocket streaming | `send_text()` per token |
| Token buffer | Client-side rendering |
| Latency optimization | Overlap retrieval + generation |

---

#### Lesson 06.04 — Citations and Source Attribution
**File**: `_15_06_04_citations_source_attribution.md`

| Topics | Subtopics |
|---|---|
| Inline citations | [1], [Source: doc_name] format |
| Citation extraction | Parse LLM output for citations |
| Faithfulness | Is answer grounded in citations? |
| `LLMChainExtractor` + verify | Post-hoc faithfulness check |
| LlamaIndex citation | `CitationQueryEngine` |
| `AttributedQA` | Attribution with token-level evidence |
| Frontend display | Highlight source passage |

---

#### Lesson 06.05 — Conversational RAG (RAG with Memory)
**File**: `_15_06_05_conversational_rag_memory.md`

| Topics | Subtopics |
|---|---|
| Chat history in RAG | Contextualize follow-up questions |
| `ConversationalRetrievalChain` | LangChain |
| `create_history_aware_retriever` | LCEL version |
| `RunnableWithMessageHistory` | Session-based memory |
| History condensation | Summarize long history |
| `ChatMessageHistory` | In-memory store |
| Redis / DynamoDB | Persistent chat history |
| Multi-turn evaluation | History-dependent questions |

---

#### Lesson 06.06 — Corrective RAG and Self-RAG
**File**: `_15_06_06_corrective_rag_self_rag.md`

| Topics | Subtopics |
|---|---|
| Self-RAG | Retrieve → critic → generate |
| Self-RAG tokens | [Retrieve], [ISREL], [ISSUP], [ISUSE] |
| Corrective RAG (CRAG) | Evaluate retrieved docs, correct if poor |
| Fallback strategy | Web search when vector retrieval fails |
| `Tavily` search | Fallback web retrieval |
| LangGraph CRAG | State machine for corrective flow |
| Evaluation | Answer correctness with vs without correction |

---

## MODULE 07 — RAG Evaluation

**Folder**: `_15_07_rag_evaluation/`  
**Lesson Count**: 6  
**Learning Order**: 7th

### Lessons

#### Lesson 07.01 — RAG Evaluation Dimensions
**File**: `_15_07_01_rag_evaluation_dimensions.md`

| Topics | Subtopics |
|---|---|
| Retrieval quality | Context precision, context recall |
| Generation quality | Faithfulness, answer relevance |
| End-to-end | Answer correctness |
| Retrieval speed | P95 latency |
| Cost | Tokens per query |
| Reference-free vs reference-based | Without ground truth |

---

#### Lesson 07.02 — RAGAS Framework
**File**: `_15_07_02_ragas_framework.md`

| Topics | Subtopics |
|---|---|
| `ragas` library | `evaluate()`, dataset format |
| Faithfulness | Answer claims ⊆ retrieved context |
| Answer Relevancy | Answer relevant to question |
| Context Precision | Retrieved items ranked by relevance |
| Context Recall | Retrieved items cover gold answer |
| `EvaluationDataset` | `question`, `answer`, `contexts`, `ground_truth` |
| LLM evaluator | `ragas.llms.LangchainLLMWrapper` |
| CI integration | Regression testing RAG changes |

---

#### Lesson 07.03 — TruLens Evaluation
**File**: `_15_07_03_trulens_evaluation.md`

| Topics | Subtopics |
|---|---|
| TruLens-Eval | Groundedness, relevance, sentiment |
| `TruChain` | LangChain wrapper |
| `TruLlama` | LlamaIndex wrapper |
| `Feedback` functions | Modular evaluation functions |
| RAG Triad | Groundedness, Answer Relevance, Context Relevance |
| Dashboard | TruLens leaderboard UI |
| `tru.get_leaderboard()` | Compare configurations |

---

#### Lesson 07.04 — DeepEval
**File**: `_15_07_04_deepeval.md`

| Topics | Subtopics |
|---|---|
| `deepeval` | Python-based LLM testing |
| `GEval` | Custom criteria evaluation |
| `HallucinationMetric` | Score hallucination |
| `FaithfulnessMetric` | Faithfulness to context |
| `RAGASMetric` | Integrated RAGAS |
| `deepeval test run` | Pytest plugin |
| CI/CD integration | GitHub Actions pipeline |

---

#### Lesson 07.05 — Building a RAG Test Dataset
**File**: `_15_07_05_building_rag_test_dataset.md`

| Topics | Subtopics |
|---|---|
| Synthetic QA generation | LLM generates Q+A from chunks |
| `ragas.testset` | `TestsetGenerator` |
| `Giskard` | Adversarial test set generation |
| Question types | Simple, multi-hop, reasoning, conversational |
| Human annotation | Labeling ground truth answers |
| Dataset format | JSON: question, contexts, ground_truth |
| Size recommendation | 100–500 Q&A pairs |

---

#### Lesson 07.06 — RAG Experimentation and A/B Testing
**File**: `_15_07_06_rag_experimentation_ab_testing.md`

| Topics | Subtopics |
|---|---|
| Experiment variables | Chunk size, overlap, top-K, reranker |
| MLflow for RAG | Log retrieval + generation metrics |
| `langsmith` tracing | Request-level trace |
| `Langfuse` | Open-source observability |
| A/B test design | Control vs treatment group |
| Statistical significance | Sample size, t-test |
| Iterative improvement | Metric-driven RAG tuning |

---

## MODULE 08 — Production RAG Systems

**Folder**: `_15_08_production_rag_systems/`  
**Lesson Count**: 7  
**Learning Order**: 8th

### Lessons

#### Lesson 08.01 — Graph RAG
**File**: `_15_08_01_graph_rag.md`

| Topics | Subtopics |
|---|---|
| GraphRAG concept | Microsoft: community summarization |
| Knowledge graph extraction | Entity + relation triples from docs |
| Community detection | Leiden algorithm |
| Global + local search | Community summary vs entity search |
| `graphrag` library | `graphrag.index`, `graphrag.query` |
| Neo4j RAG | `langchain-neo4j`, Cypher generation |
| LlamaIndex Knowledge Graph | `KnowledgeGraphIndex` |
| When to use GraphRAG | Complex, multi-document reasoning |

---

#### Lesson 08.02 — Multimodal RAG
**File**: `_15_08_02_multimodal_rag.md`

| Topics | Subtopics |
|---|---|
| Image retrieval in RAG | CLIP embeddings for images |
| Table RAG | Table → text → embed or direct SQL |
| PDF with figures | Extract → caption → index |
| `LlamaIndex MultiModal` | `MultiModalVectorStoreIndex` |
| `GPT-4o` as generator | Vision + retrieved context |
| Audio RAG | Whisper → text → RAG pipeline |
| Evaluation | Multimodal answer accuracy |

---

#### Lesson 08.03 — Long Context RAG
**File**: `_15_08_03_long_context_rag.md`

| Topics | Subtopics |
|---|---|
| 128K+ context LLMs | Gemini 1.5, GPT-4o, Claude 3.5 |
| RAG vs long context | When to use which |
| Lost-in-the-middle | Context position effects |
| Hybrid: retrieve + long context | Best of both |
| LongRAG | Full doc retrieval in 128K window |
| Evaluation | Answer accuracy vs position |

---

#### Lesson 08.04 — Agentic RAG
**File**: `_15_08_04_agentic_rag.md`

| Topics | Subtopics |
|---|---|
| Agentic RAG concept | Agent decides when/what to retrieve |
| ReAct-based RAG | Reason-Act loop with tools |
| `create_retriever_tool` | LangChain tool wrapper |
| LlamaIndex `ReActAgent` | Agent with query engine tool |
| Multi-retriever agent | Route between specialized indexes |
| Self-correction | CRAG + agent loop |
| Full detail | Phase 7 (AI Agents) |

---

#### Lesson 08.05 — RAG Observability
**File**: `_15_08_05_rag_observability.md`

| Topics | Subtopics |
|---|---|
| `Langfuse` | Tracing, scores, datasets |
| `Langsmith` | LangChain native tracing |
| `Phoenix (Arize)` | Open-source LLM observability |
| Trace components | Retrieval latency, generation latency |
| Token usage | Per-trace token cost |
| Feedback collection | User thumbs up/down → Langfuse |
| Alerting | Latency + error rate thresholds |

---

#### Lesson 08.06 — RAG Security and Guardrails
**File**: `_15_08_06_rag_security_guardrails.md`

| Topics | Subtopics |
|---|---|
| Indirect prompt injection | Malicious content in retrieved docs |
| Input sanitization | Strip injection patterns |
| Output guardrails | `nemo-guardrails` |
| `guardrails-ai` | `Guard`, `Validator` |
| PII in retrieval | Redact before indexing |
| Source authorization | Access control on documents |
| Rate limiting | Per-user query limits |

---

#### Lesson 08.07 — Scaling and Optimizing RAG
**File**: `_15_08_07_scaling_optimizing_rag.md`

| Topics | Subtopics |
|---|---|
| Embedding throughput | Batch + async embedding |
| Async retrieval | `asyncio.gather` parallel retrievers |
| Caching | Query → result cache, semantic cache |
| `GPTCache` | Semantic caching for LLM calls |
| Index sharding | Horizontal scaling vector DB |
| Pre-filtering | Reduce ANN search space |
| Cost optimization | Cache hit rate, token reduction |

---

## MODULE 09 — Industry Projects

**Folder**: `_15_09_industry_projects/`  
**Lesson Count**: 6  
**Learning Order**: 9th (Capstone)

### Lessons

#### Lesson 09.01 — Enterprise Document Q&A System
**File**: `_15_09_01_enterprise_document_qa_system.md`

| Topics | Subtopics |
|---|---|
| Stack | LangChain + Qdrant + OpenAI/Llama |
| Loaders | PDF, DOCX, HTML, SharePoint |
| Chunking | Hierarchical + semantic |
| Retrieval | Hybrid BM25 + dense + reranker |
| Memory | Conversational RAG |
| API | FastAPI, auth, rate limit |
| Observability | Langfuse tracing |

---

#### Lesson 09.02 — Codebase Q&A Assistant
**File**: `_15_09_02_codebase_qa_assistant.md`

| Topics | Subtopics |
|---|---|
| Stack | LangChain + Chroma + CodeLlama |
| Loaders | `GitLoader`, `DirectoryLoader` |
| Chunking | `Language.PYTHON`, function-level |
| Retrieval | Code-specific embeddings |
| Query types | "How does X work?", "Find usages of Y" |
| GitHub integration | Auto-index on push |

---

#### Lesson 09.03 — Research Paper Assistant
**File**: `_15_09_03_research_paper_assistant.md`

| Topics | Subtopics |
|---|---|
| Stack | LlamaIndex + Qdrant + GPT-4o |
| Sources | arXiv API, Semantic Scholar |
| Multi-paper | Cross-paper comparison |
| GraphRAG | Paper → entities → citation graph |
| Multi-hop | "Papers citing X that also study Y" |
| API | FastAPI + streaming response |

---

#### Lesson 09.04 — Customer Support RAG Bot
**File**: `_15_09_04_customer_support_rag_bot.md`

| Topics | Subtopics |
|---|---|
| Stack | LangChain + Weaviate + Claude |
| Knowledge base | FAQ, manuals, ticket history |
| Fallback | Escalate to human if low confidence |
| Multi-language | Detect language → route |
| Conversational | Session memory per user |
| Evaluation | RAGAS + human CSAT scores |

---

#### Lesson 09.05 — Financial Report RAG
**File**: `_15_09_05_financial_report_rag.md`

| Topics | Subtopics |
|---|---|
| Stack | Haystack + Qdrant + GPT-4o |
| Documents | EDGAR 10-K, earnings transcripts |
| Table extraction | `table-transformer` + RAG |
| Numerical QA | Arithmetic over retrieved figures |
| Self-RAG | Verify answer against source |
| Citation | Inline source with page number |

---

#### Lesson 09.06 — GraphRAG Knowledge Platform (Capstone)
**File**: `_15_09_06_graphrag_knowledge_platform_capstone.md`

| Topics | Subtopics |
|---|---|
| Stack | GraphRAG + Neo4j + vLLM + LlamaIndex |
| Indexing | Entity extraction → Neo4j → community |
| Retrieval | Global (community) + local (entity) |
| Hybrid | Vector + graph traversal |
| API | FastAPI with streaming |
| Evaluation | RAGAS + TruLens + Langfuse |
| Use case | Enterprise knowledge management |

---

## Full Folder Structure

```
docs/curriculum/_15_rag_engineering/
│
├── _15_01_rag_fundamentals/
│   ├── _15_01_01_what_is_rag_and_why.md
│   ├── _15_01_02_naive_rag_architecture.md
│   ├── _15_01_03_rag_frameworks_overview.md
│   ├── _15_01_04_rag_data_flow_components.md
│   ├── _15_01_05_langchain_lcel_pipeline.md
│   └── _15_01_06_llamaindex_core_concepts.md
│
├── _15_02_document_processing_and_chunking/
│   ├── _15_02_01_document_loaders.md
│   ├── _15_02_02_fixed_size_chunking.md
│   ├── _15_02_03_semantic_sentence_chunking.md
│   ├── _15_02_04_structure_aware_chunking.md
│   ├── _15_02_05_hierarchical_multi_granularity_chunking.md
│   ├── _15_02_06_multimodal_document_processing.md
│   └── _15_02_07_chunking_evaluation_selection.md
│
├── _15_03_embeddings_for_rag/
│   ├── _15_03_01_embedding_model_selection.md
│   ├── _15_03_02_embedding_apis_local_models.md
│   ├── _15_03_03_late_interaction_colbert.md
│   ├── _15_03_04_fine_tuning_embedding_models.md
│   ├── _15_03_05_sparse_hybrid_embeddings.md
│   └── _15_03_06_embedding_storage_management.md
│
├── _15_04_vector_databases/
│   ├── _15_04_01_vector_database_fundamentals.md
│   ├── _15_04_02_faiss_deep_dive.md
│   ├── _15_04_03_chroma.md
│   ├── _15_04_04_qdrant.md
│   ├── _15_04_05_pinecone.md
│   ├── _15_04_06_weaviate.md
│   └── _15_04_07_vector_db_selection_operations.md
│
├── _15_05_advanced_retrieval/
│   ├── _15_05_01_hybrid_search.md
│   ├── _15_05_02_hyde_hypothetical_documents.md
│   ├── _15_05_03_query_transformation.md
│   ├── _15_05_04_rag_fusion.md
│   ├── _15_05_05_multi_hop_iterative_retrieval.md
│   ├── _15_05_06_metadata_filtering_routing.md
│   ├── _15_05_07_contextual_retrieval.md
│   └── _15_05_08_re_ranking.md
│
├── _15_06_generation_and_augmentation/
│   ├── _15_06_01_rag_prompt_templates.md
│   ├── _15_06_02_response_synthesis_strategies.md
│   ├── _15_06_03_streaming_rag.md
│   ├── _15_06_04_citations_source_attribution.md
│   ├── _15_06_05_conversational_rag_memory.md
│   └── _15_06_06_corrective_rag_self_rag.md
│
├── _15_07_rag_evaluation/
│   ├── _15_07_01_rag_evaluation_dimensions.md
│   ├── _15_07_02_ragas_framework.md
│   ├── _15_07_03_trulens_evaluation.md
│   ├── _15_07_04_deepeval.md
│   ├── _15_07_05_building_rag_test_dataset.md
│   └── _15_07_06_rag_experimentation_ab_testing.md
│
├── _15_08_production_rag_systems/
│   ├── _15_08_01_graph_rag.md
│   ├── _15_08_02_multimodal_rag.md
│   ├── _15_08_03_long_context_rag.md
│   ├── _15_08_04_agentic_rag.md
│   ├── _15_08_05_rag_observability.md
│   ├── _15_08_06_rag_security_guardrails.md
│   └── _15_08_07_scaling_optimizing_rag.md
│
└── _15_09_industry_projects/
    ├── _15_09_01_enterprise_document_qa_system.md
    ├── _15_09_02_codebase_qa_assistant.md
    ├── _15_09_03_research_paper_assistant.md
    ├── _15_09_04_customer_support_rag_bot.md
    ├── _15_09_05_financial_report_rag.md
    └── _15_09_06_graphrag_knowledge_platform_capstone.md
```

---

## Learning Order

```
01 RAG Fundamentals  (What, Why, Frameworks, LCEL, LlamaIndex)
    ↓
02 Document Processing & Chunking  (Loaders → Fixed → Semantic → Hierarchical)
    ↓
03 Embeddings for RAG  (Model selection → Fine-tune → Sparse/Hybrid)
    ↓
04 Vector Databases  (FAISS → Chroma → Qdrant → Pinecone → Weaviate)
    ↓
05 Advanced Retrieval  (Hybrid → HyDE → Query Transform → Multi-hop → Rerank)
    ↓
06 Generation & Augmentation  (Prompt → Synthesis → Streaming → Memory → Self-RAG)
    ↓
07 RAG Evaluation  (RAGAS → TruLens → DeepEval → A/B Testing)
    ↓
08 Production Systems  (GraphRAG → Multimodal → Agentic → Observability → Scale)
    ↓
09 Industry Projects (Capstone)
```

---

## Summary Statistics

| Module | Title | Lessons |
|---|---|---|
| 01 | RAG Fundamentals | 6 |
| 02 | Document Processing & Chunking | 7 |
| 03 | Embeddings for RAG | 6 |
| 04 | Vector Databases | 7 |
| 05 | Advanced Retrieval | 8 |
| 06 | Generation & Augmentation | 6 |
| 07 | RAG Evaluation | 6 |
| 08 | Production RAG Systems | 7 |
| 09 | Industry Projects | 6 |
| **TOTAL** | | **59 lessons** |

---

## Phase 7 Handoff (AI Agents & Multi-Agent Systems)

Nodes from Phase 6 extended in Phase 7:
- Agentic RAG → full agent loop with tools
- LangGraph (introduced in CRAG) → full agent orchestration
- RAG as one tool among many agent tools
- Observability → extended to agent traces
