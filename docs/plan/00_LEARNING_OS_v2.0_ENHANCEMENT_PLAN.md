# Learning OS Architecture v2.0 Enhancement Plan

This document details the architecture design and integration specifications for upgrading the **Learning Operating System (Learning OS)** to **v2.0**. It acts as the system blueprint to extend the existing baseline documents (00–21) without introducing breaking changes, maintaining strict backward compatibility.

---

## Document Index & Mapping Table

The following matrix lists the baseline files, their upgrade status for v2.0, and implementation priorities:

| Doc # | Target File | Impact Status | Priority | Core Integration Area |
|---|---|---|---|---|
| 00 | `00_LEARNING_OS_MASTER_PLAN.md` | **Updated** | High | System-wide scope, v2.0 Architecture baseline, Tech Stack modifications |
| 01 | `01_Product_Vision.md` | **Updated** | High | Philosophy shift: Knowledge Processing Pipeline, Ingestion, AI validation |
| 02 | `02_Information_Architecture.md` | **Updated** | Medium | Ingestion catalog endpoints, vector semantic URLs, hierarchy expansions |
| 03 | `03_User_Roles_RBAC.md` | **Updated** | Medium | New fine-grained permissions for AI workflows, knowledge moderation |
| 04 | `04_Database_ERD.md` | **Updated** | High | Vector embeddings, chunks, knowledge sources, citations, graphs schema |
| 05 | `05_Folder_Structure.md` | **Updated** | High | New domains (knowledge, vector, ingestion), background worker files |
| 06 | `06_CMS_Design.md` | **Updated** | High | AI Draft generation workspace, review systems, plagiarism checks |
| 07 | `07_Learning_Engine.md` | **Updated** | High | Adaptive learning pathways, knowledge graph prerequisites tracking |
| 08 | `08_Progress_Engine.md` | **Updated** | Medium | Weak topic metrics, confidence intervals adjustment, skill indexes |
| 09 | `09_Exercise_Engine.md` | **Updated** | Medium | Auto-generating custom practice problems using Local Ollama |
| 10 | `10_Quiz_Engine.md` | **Updated** | Medium | AI-assisted quiz and explanation validation |
| 11 | `11_Achievement_Engine.md` | **Updated** | Low | New criteria metrics for vector curation, citation accuracy |
| 12 | `12_Search_Architecture.md` | **Updated** | High | Hybrid Search architecture (FTS5 + Cosine Similarity Vector Search) |
| 13 | `13_Recommendation_Engine.md` | **Updated** | High | RAG-based search relevance & similarity recommendations service |
| 14 | `14_AI_Integration_Layer.md` | **Updated** | High | Provider abstraction layer, Local Ollama API, Cloud gateways (v2.0 Core) |
| 15 | `15_REST_API_Specification.md` | **Updated** | Medium | Source ingestion endpoints, Vector searching, AI tutor chat sockets |
| 16 | `16_Admin_Dashboard.md` | **Updated** | Medium | Ingestion controls, queue status, similarity thresholds, quality metrics |
| 17 | `17_Student_Dashboard.md` | **Updated** | Medium | Adaptive recommendations widget, AI tutor workspace, weak topics pane |
| 18 | `18_SEO_Strategy.md` | **Updated** | Low | Citation schema mapping, source attribution graphs |
| 19 | `19_Security_Architecture.md` | **Updated** | High | Prompt injection safeguards, local worker network access controls |
| 20 | `20_Deployment_Architecture.md` | **Updated** | High | Ollama local servers, Vector databases infrastructure, S3 bucket storage |
| 21 | `21_Implementation_Roadmap.md` | **Updated** | High | Adding v2.0 tasks to target sprint pipelines |

---

## 1. Master Plan Evolving Plan (Doc 00)
- **File Name**: [00_LEARNING_OS_MASTER_PLAN.md](./00_LEARNING_OS_MASTER_PLAN.md)
- **Current Purpose**: Master index, executive summary, baseline technology stack decisions, and open questions.
- **Enhancement Summary**: Integrate the vector store, hybrid search capabilities, background AI workers, and local LLM runtime (Ollama) into the primary master architecture.
- **New Sections to Add**:
  - `v2.0 Technology Integrations`: Specification for PGVector / SQLite-VSS, Ollama 14B+, and background job scheduler extensions.
  - `Knowledge Engine Pipeline Lifecycle Overview`: Abstract visual representation of data movement from ingestion to student view.
- **Existing Sections to Update**:
  - `Technology Stack Decision`: Update target DB to include Vector capability (e.g., PostgreSQL with pgvector extension / SQLite with sqlite-vss extension for development). Add Ollama to AI Providers.
  - `Architectural Principles`: Append "Vector-First Ingestion" and "Model Agnostic Interfaces".
- **New Database Tables**: None.
- **New Relationships**: None.
- **New Folder Structure**: Include `app/domains/vector/` and `app/services/ingestion/`.
- **New Services**: `VectorStoreService`, `IngestionPipelineService`.
- **New APIs**: `/api/v1/search/hybrid`.
- **New Background Jobs**: `process_ingestion_source`, `rebuild_embeddings_index`.
- **New Configurations**: `OLLAMA_API_BASE_URL`, `VECTOR_DB_URL`, `EMBEDDING_MODEL_NAME`.
- **Migration Strategy**: Add Alembic migration scripts for pgvector/sqlite-vss dependencies.
- **Security Considerations**: Local Ollama execution boundaries (avoid host filesystem access).
- **Performance Considerations**: Batch embedding requests during vector index builds to avoid CPU bottlenecks.
- **Future Scalability**: Seamless scale from SQLite-VSS in dev to PGVector (TiDB/PostgreSQL serverless) in production.
- **Whether Breaking or Backward Compatible**: Fully backward compatible.
- **Implementation Priority**: Critical (Must be configured first).

---

## 2. Product Vision Evolving Plan (Doc 01)
- **File Name**: [01_Product_Vision.md](./01_Product_Vision.md)
- **Current Purpose**: Identifies target user value propositions, core metrics, and scope boundaries.
- **Enhancement Summary**: Evolve the vision from a structured lesson platform into a living **Knowledge Operating System (Learning OS v2.0)** that processes unstructured text into curated learning pathways.
- **New Sections to Add**:
  - `The Source Ingestion Philosophy`: Define how third-party materials (books, blogs, PDFs, YouTube transcripts) undergo automatic ingestion, chunking, formatting, and manual editing steps.
  - `AI-Human Collaborative CMS Vision`: Standardize how human review processes inspect AI-drafted lessons.
- **Existing Sections to Update**:
  - `The Universal Lesson Schema`: Extend to include citations, source backlinks, and references pointing directly to dynamic knowledge graph nodes.
- **New Database Tables**: None.
- **New Relationships**: None.
- **New Folder Structure**: None.
- **New Services**: None.
- **New APIs**: None.
- **New Background Jobs**: None.
- **New Configurations**: None.
- **Migration Strategy**: Document metadata only.
- **Security Considerations**: Compliance with source copyright and licenses when importing text chunks.
- **Performance Considerations**: None.
- **Future Scalability**: Scalability of content pipelines to handle thousands of source imports monthly.
- **Whether Breaking or Backward Compatible**: Backward compatible.
- **Implementation Priority**: High (Guides business goals).

---

## 3. Information Architecture Evolving Plan (Doc 02)
- **File Name**: [02_Information_Architecture.md](./02_Information_Architecture.md)
- **Current Purpose**: Sitemap configuration, taxonomy structure, and content hierarchy rules.
- **Enhancement Summary**: Extend URL paths and taxonomic systems to handle raw imported content, document chunks, and interactive AI tutor chat sessions.
- **New Sections to Add**:
  - `/admin/ingestion/`: Route paths mapping source upload, progress trackers, and ingestion statistics interfaces.
  - `/learn/tutor/`: URL patterns routing live adaptive tutor sessions.
- **Existing Sections to Update**:
  - `URL Structure Design`: Support dynamic ingestion reference mappings, e.g., `/source/youtube/<playlist_id>/<video_id>`.
  - `Content Types`: Add `source_chunk`, `knowledge_node`, and `attribution_citation` structures.
- **New Database Tables**: None.
- **New Relationships**: None.
- **New Folder Structure**: None.
- **New Services**: None.
- **New APIs**: None.
- **New Background Jobs**: None.
- **New Configurations**: None.
- **Migration Strategy**: Updates to Flask Blueprint route maps.
- **Security Considerations**: Limit path manipulation on uploaded source PDF directories.
- **Performance Considerations**: None.
- **Future Scalability**: Unlimited category scale through multi-tier parent-child category hierarchies.
- **Whether Breaking or Backward Compatible**: Backward compatible.
- **Implementation Priority**: Medium.

---

## 4. User Roles & RBAC Evolving Plan (Doc 03)
- **File Name**: [03_User_Roles_RBAC.md](./03_User_Roles_RBAC.md)
- **Current Purpose**: Permission matrices and role hierarchies for Super Admin, Editor, Reviewer, Student, and Guest roles.
- **Enhancement Summary**: Introduce fine-grained permissions specifically covering AI operations, vector indexing, source content ingestion, and manual draft approvals.
- **New Sections to Add**:
  - `AI Operations Access Keys`: Permissions listing who can trigger generation, configure prompts, run plagiarism scans, or modify vector configurations.
- **Existing Sections to Update**:
  - `Permissions Matrix`: Add columns for `source.ingest`, `ai.generate_draft`, `ai.score_quality`, `vector.reindex`.
- **New Database Tables**: None (Permissions seeded into `permissions` table).
- **New Relationships**: None.
- **New Folder Structure**: None.
- **New Services**: None.
- **New APIs**: None.
- **New Background Jobs**: None.
- **New Configurations**: None.
- **Migration Strategy**: Run Alembic migrations executing seed records insertion into `permissions` and `role_permissions` tables.
- **Security Considerations**: Prevent Students from bypassing controls via `/api/v1/ai` endpoints.
- **Performance Considerations**: Cache current user permissions mapping in Redis to avoid database checks on every request.
- **Future Scalability**: Role-based access matches scalable cloud standard profiles.
- **Whether Breaking or Backward Compatible**: Backward compatible.
- **Implementation Priority**: Medium.

---

## 5. Database ERD Evolving Plan (Doc 04)
- **File Name**: [04_Database_ERD.md](./04_Database_ERD.md)
- **Current Purpose**: Logical schema tables covering content, users, quizzes, progress, and gamification layers.
- **Enhancement Summary**: Integrate 12 new tables to support vector search indexes, citation pathways, adaptive knowledge nodes, source ingestion files, and weak topic logs.
- **New Database Tables to Add**:
  1. `knowledge_sources`: Stores metadata of books, playlists, files, URLs.
  2. `source_documents`: Tracks parsed sub-documents (e.g., individual PDF pages or YouTube videos).
  3. `knowledge_chunks`: Stores clean text segments ready for vector embedding calculation.
  4. `chunk_embeddings`: Stores vector representation floats ($d=384$ or $d=1536$) with a spatial index.
  5. `knowledge_nodes`: Represents distinct atomic concepts in the knowledge graph.
  6. `knowledge_edges`: Models relationships between concepts (`prerequisite_of`, `extends`, `related_to`).
  7. `citations`: Maps specific chunks inside `knowledge_chunks` to `lesson_sections`.
  8. `ai_tutor_sessions`: Tracks student interactive chat threads with AI models.
  9. `ai_tutor_messages`: Keeps individual messages within a session.
  10. `user_weak_topics`: Logs topics/concepts where a student scores $<70\%$ on quizzes/exercises.
  11. `content_quality_scores`: Tracks plagiarism score, readability Index, grammar checks, completeness.
  12. `ai_generation_jobs`: Tracks parameters, models, prompts, and output for auditable AI drafts.

- **New Relationships**:
  - `knowledge_sources ||--o{ source_documents`
  - `source_documents ||--o{ knowledge_chunks`
  - `knowledge_chunks ||--|| chunk_embeddings`
  - `knowledge_chunks ||--o{ citations`
  - `lessons ||--o{ citations`
  - `knowledge_nodes ||--o{ knowledge_edges : "starts at"`
  - `knowledge_nodes ||--o{ knowledge_edges : "ends at"`
  - `users ||--o{ ai_tutor_sessions`
  - `ai_tutor_sessions ||--o{ ai_tutor_messages`
  - `users ||--o{ user_weak_topics`
  - `lessons ||--|| content_quality_scores`

- **Existing Sections to Update**:
  - Update `lessons` model: Add `knowledge_node_id` foreign key.
  - Update `user_progress` model: Add overall `knowledge_mastery_index` metric.
- **New Folder Structure**: None.
- **New Services**: None.
- **New APIs**: None.
- **New Background Jobs**: None.
- **New Configurations**: None.
- **Migration Strategy**: Define SQL migrations utilizing standard Alembic versions. Conditionally support `pgvector` index creation (`CREATE INDEX ON chunk_embeddings USING ivfflat...`).
- **Security Considerations**: Ensure `user_id` values scope user-specific tutor logs.
- **Performance Considerations**: Use HNSW indexes for high-speed vector similarity queries under scale.
- **Whether Breaking or Backward Compatible**: Backward compatible.
- **Implementation Priority**: High.

---

## 6. Folder Structure Evolving Plan (Doc 05)
- **File Name**: [05_Folder_Structure.md](./05_Folder_Structure.md)
- **Current Purpose**: Folder blueprints for application code, services, domains, static layers, templates, and scripts.
- **Enhancement Summary**: Structure new directories to accommodate the ingestion engines, vector interfaces, and background queue workers without altering existing patterns.
- **New Folder Structures to Add**:
```
learning_os/
├── app/
│   ├── domains/
│   │   ├── knowledge/               <- NEW: Source, Document, Chunk models/repos
│   │   ├── vector/                  <- NEW: Embedding models, vectors repos
│   │   ├── graph/                   <- NEW: Node, Edge models/repos
│   │   └── tutor/                   <- NEW: Session, Message models/repos
│   ├── services/
│   │   ├── ingestion/               <- NEW: Parsers, Chunkers, Attributors
│   │   │   ├── pdf_parser.py
│   │   │   ├── youtube_parser.py
│   │   │   ├── chunker.py
│   │   │   └── pipeline.py
│   │   ├── vector_store.py          <- NEW: pgvector/sqlite-vss interface wrapper
│   │   ├── adaptive_learning.py     <- NEW: Weak topic detection, pathway adjustments
│   │   ├── quality_scorer.py        <- NEW: Readability, grammar, plagiarism hooks
│   │   └── graph_service.py         <- NEW: Relation builders, graph traversers
│   └── templates/
│       └── learn/
│           └── tutor.html           <- NEW: Tutor chatbot window
└── scripts/
    ├── ingest_source.py             <- NEW: CLI ingestion tool
    └── evaluate_quality.py          <- NEW: CLI content scoring utility
```
- **Existing Sections to Update**: None.
- **New Database Tables**: None.
- **New Relationships**: None.
- **New Folder Structure**: Described above.
- **New Services**: Described above.
- **New APIs**: None.
- **New Background Jobs**: None.
- **New Configurations**: None.
- **Migration Strategy**: Directory trees can be created manually or bootstrapped via startup utilities.
- **Security Considerations**: Ensure Python execution constraints protect imports.
- **Performance Considerations**: None.
- **Future Scalability**: Clear separation ensures separate microservices can pull out domain sub-folders if required.
- **Whether Breaking or Backward Compatible**: Backward compatible.
- **Implementation Priority**: High (Must be setup before writing new code).

---

## 7. CMS Design Evolving Plan (Doc 06)
- **File Name**: [06_CMS_Design.md](./06_CMS_Design.md)
- **Current Purpose**: CMS authoring view, publishing states, manual revisions, and lesson metrics.
- **Enhancement Summary**: Integrate the AI-drafting workspace, dynamic citations linkage, automated plagiarism checking, and content quality scoring interfaces.
- **New Sections to Add**:
  - `AI Draft Generation Portal`: A workflow workspace where authors select high-quality source documents, define target lesson criteria, and trigger Local/Cloud LLMs to output draft lesson proposals.
  - `Quality Scoring Pane`: Real-time visual meters showing: Grammar Accuracy, Plagiarism Rating ($<5\%$), Comprehensiveness Score, and Readability Grade (Flesch-Kincaid).
- **Existing Sections to Update**:
  - `Publishing Workflow States`: Introduce intermediate review flags, e.g., `ai_drafted` and `quality_failed`.
- **New Database Tables**: `ai_generation_jobs`, `content_quality_scores`.
- **New Relationships**: `lessons` to `content_quality_scores`.
- **New Folder Structure**: `app/blueprints/admin/ingestion/` templates.
- **New Services**: `AIContentGeneratorService`, `ContentQualityService`.
- **New APIs**: `/api/v1/admin/ai/generate-draft`, `/api/v1/admin/ai/check-quality`.
- **New Background Jobs**: `generate_draft_job`, `run_plagiarism_scan`.
- **New Configurations**: `PLAGIARISM_API_KEY`, `MIN_QUALITY_THRESHOLD`.
- **Migration Strategy**: Update template views via Blueprints. Add database fields.
- **Security Considerations**: Ensure generated content is filtered for toxic prompts.
- **Performance Considerations**: Execute CPU-heavy checks (plagiarism API call, Flesch index computation) asynchronously.
- **Future Scalability**: Quality score models can be fine-tuned or swapped out without UI re-writes.
- **Whether Breaking or Backward Compatible**: Backward compatible.
- **Implementation Priority**: High.

---

## 8. Learning Engine Evolving Plan (Doc 07)
- **File Name**: [07_Learning_Engine.md](./07_Learning_Engine.md)
- **Current Purpose**: Prerequisite logic, modules sequence enforcement, Spaced Repetition algorithms.
- **Enhancement Summary**: Upgrade the learning sequencer into an **Adaptive Learning Engine** utilizing the knowledge graph and prerequisite tracking patterns.
- **New Sections to Add**:
  - `Knowledge Graph Traversals`: Specifications for topological sorting to construct dynamic student pathways based on concept connections.
  - `Weak Topic Remediation Engine`: Workflow for re-routing students through alternative nodes when key concepts are not mastered.
- **Existing Sections to Update**:
  - `Prerequisites Validation`: Integrate checks against the `knowledge_edges` table instead of relying only on hardcoded course sequences.
- **New Database Tables**: `knowledge_nodes`, `knowledge_edges`.
- **New Relationships**: Defined in ERD.
- **New Folder Structure**: `app/domains/graph/`.
- **New Services**: `AdaptiveLearningService`, `GraphService`.
- **New APIs**: `/api/v1/learn/adaptive-path`.
- **New Background Jobs**: `rebuild_knowledge_map`.
- **New Configurations**: None.
- **Migration Strategy**: Seed basic node relationships mapping existing Python, Java, and SQL structures.
- **Security Considerations**: None.
- **Performance Considerations**: Use networkx-like graph traversals cached in memory to avoid query overhead during student clicks.
- **Future Scalability**: Adapts to millions of lessons via fast path traversal algorithms.
- **Whether Breaking or Backward Compatible**: Backward compatible.
- **Implementation Priority**: High.

---

## 9. Progress Engine Evolving Plan (Doc 08)
- **File Name**: [08_Progress_Engine.md](./08_Progress_Engine.md)
- **Current Purpose**: User level calculators, XP values allocation, streaks trackers.
- **Enhancement Summary**: Track topic-level skill mastery indexes and weak concepts alongside user progress metrics.
- **New Sections to Add**:
  - `Skill Mastery Index Calculations`: Define dynamic equations determining mastery level based on correct quiz answers, coding exercises, and active revision reviews.
- **Existing Sections to Update**:
  - `Lesson Progress Tracking`: Complete condition triggers check for weak topic resolution metrics.
- **New Database Tables**: `user_weak_topics`.
- **New Relationships**: `users` to `user_weak_topics`.
- **New Folder Structure**: None.
- **New Services**: `SkillTrackingService`.
- **New APIs**: `/api/v1/progress/weak-topics`.
- **New Background Jobs**: `evaluate_weak_topics`.
- **New Configurations**: None.
- **Migration Strategy**: Add new table configuration to user progress schemas.
- **Security Considerations**: Ensure user profile endpoints isolate database access.
- **Performance Considerations**: Calculate mastery indices asynchronously to minimize latency during quiz submissions.
- **Future Scalability**: High performance scoring matrices scale efficiently.
- **Whether Breaking or Backward Compatible**: Backward compatible.
- **Implementation Priority**: Medium.

---

## 10. Exercise Engine Evolving Plan (Doc 09)
- **File Name**: [09_Exercise_Engine.md](./09_Exercise_Engine.md)
- **Current Purpose**: Graded coding sandbox integrations, problem validations, and database specifications.
- **Enhancement Summary**: Support AI-assisted exercise generation via the AI Gateway using local Ollama model instances.
- **New Sections to Add**:
  - `AI Problem Generator`: Parameters and prompt matrices to compile exercise prompts, custom test cases, and solution templates.
- **Existing Sections to Update**:
  - `Auto-Grading Flow`: Validate generated test inputs during editorial cycles before publishing to students.
- **New Database Tables**: None.
- **New Relationships**: None.
- **New Folder Structure**: None.
- **New Services**: `AIExerciseGeneratorService`.
- **New APIs**: `/api/v1/admin/exercises/generate`.
- **New Background Jobs**: `generate_exercises_job`.
- **New Configurations**: `OLLAMA_CODER_MODEL`.
- **Migration Strategy**: Deploy standard API controllers.
- **Security Considerations**: Prevent sandbox escapes during generated test suite validation checks.
- **Performance Considerations**: None.
- **Future Scalability**: Swap coder engines (Ollama local coder, GPT-4o, Claude) dynamically depending on context load.
- **Whether Breaking or Backward Compatible**: Backward compatible.
- **Implementation Priority**: Medium.

---

## 11. Quiz Engine Evolving Plan (Doc 10)
- **File Name**: [10_Quiz_Engine.md](./10_Quiz_Engine.md)
- **Current Purpose**: Question bank structures, MCQs evaluations, attempt trackers.
- **Enhancement Summary**: Deploy automated AI quiz generation directly linked to ingested lesson sources.
- **New Sections to Add**:
  - `AI Quiz Ingestor`: Prompts that extract structured MCQs (with multiple choice options, correct flags, and explanations) using lesson text.
- **Existing Sections to Update**:
  - `Auto-Grading & Validation Engine`: Ensure AI-generated option layouts map correctly to active database option rows.
- **New Database Tables**: None.
- **New Relationships**: None.
- **New Folder Structure**: None.
- **New Services**: `AIQuizGeneratorService`.
- **New APIs**: `/api/v1/admin/quizzes/generate`.
- **New Background Jobs**: `generate_quiz_job`.
- **New Configurations**: None.
- **Migration Strategy**: Integrate endpoint into standard admin dashboard.
- **Security Considerations**: Mitigate quiz content generation model hallucinations through structural validators.
- **Performance Considerations**: Cache generated questions inside review tables to support editing before integration into question banks.
- **Future Scalability**: High.
- **Whether Breaking or Backward Compatible**: Backward compatible.
- **Implementation Priority**: Medium.

---

## 12. Achievement Engine Evolving Plan (Doc 11)
- **File Name**: [11_Achievement_Engine.md](./11_Achievement_Engine.md)
- **Current Purpose**: Badges schemas, criteria evaluators, XP assignments.
- **Enhancement Summary**: Support new badge criteria targeting vector searches, tutoring involvement, and weak topics cleanup.
- **New Sections to Add**:
  - `v2.0 Gamification Criteria`: Define rules for awarding badges (e.g., "Weakness Cleared", "Deep Inquirer" for using the AI tutor, or "Cite Collector").
- **Existing Sections to Update**:
  - `Asynchronous Badge Evaluator`: Expand `criteria_type` logic to handle the new v2.0 parameters.
- **New Database Tables**: None.
- **New Relationships**: None.
- **New Folder Structure**: None.
- **New Services**: None.
- **New APIs**: None.
- **New Background Jobs**: None.
- **New Configurations**: None.
- **Migration Strategy**: Run Alembic migrations to seed new badge records.
- **Security Considerations**: None.
- **Performance Considerations**: None.
- **Future Scalability**: Scalable architecture accommodates infinite criteria mappings.
- **Whether Breaking or Backward Compatible**: Backward compatible.
- **Implementation Priority**: Low.

---

## 13. Search Architecture Evolving Plan (Doc 12)
- **File Name**: [12_Search_Architecture.md](./12_Search_Architecture.md)
- **Current Purpose**: SQLite FTS5 configuration, ranking metrics, query autocomplete logic.
- **Enhancement Summary**: Upgrade search infrastructure to support **Hybrid Search**, merging vector semantic matches with traditional full-text keywords.
- **New Sections to Add**:
  - `Hybrid Reciprocal Rank Fusion (RRF)`: Implement RRF algorithm to combine keyword rankings with vector distance results.
  - `Semantic Query Analysis`: Extract intent vectors to search database embedding spaces.
- **Existing Sections to Update**:
  - `Search Indexing Services`: Maintain synchronous triggers to update keyword text indexes alongside chunk vector calculations.
- **New Database Tables**: `chunk_embeddings`.
- **New Relationships**: `knowledge_chunks` to `chunk_embeddings`.
- **New Folder Structure**: `app/domains/vector/`.
- **New Services**: `HybridSearchService`.
- **New APIs**: `/api/v1/search/hybrid`.
- **New Background Jobs**: `generate_vectors_job`.
- **New Configurations**: `VECTOR_DIMENSION`, `SEARCH_RRF_K_CONSTANT`.
- **Migration Strategy**: Add SQLite extension wrappers (sqlite-vss) for developers, target PostgreSQL/pgvector for deployments.
- **Security Considerations**: Strip script injections before vector ingestion steps.
- **Performance Considerations**: Scale database connections via thread pools to support vector similarity operations.
- **Future Scalability**: Hybrid engine scales efficiently to millions of items.
- **Whether Breaking or Backward Compatible**: Backward compatible.
- **Implementation Priority**: High.

---

## 14. Recommendation Engine Evolving Plan (Doc 13)
- **File Name**: [13_Recommendation_Engine.md](./13_Recommendation_Engine.md)
- **Current Purpose**: Dynamic course selection, cosine similarity matching over metadata tags.
- **Enhancement Summary**: Upgrade the recommender system to evaluate knowledge graphs and user weak topics for highly personalized content pathways.
- **New Sections to Add**:
  - `Adaptive Graph Pathways Recommender`: Select course paths dynamically using graph node connections and student weak topics profiles.
- **Existing Sections to Update**:
  - `Vector Similarity Recommendations`: Replace basic tag-matching heuristics with vector similarity checks across user progress embeddings and target course nodes.
- **New Database Tables**: None.
- **New Relationships**: None.
- **New Folder Structure**: None.
- **New Services**: None.
- **New APIs**: `/api/v1/recommendations/adaptive`.
- **New Background Jobs**: None.
- **New Configurations**: None.
- **Migration Strategy**: Standard updates to recommender services logic.
- **Security Considerations**: Secure tenant boundaries to prevent cross-user recommendations.
- **Performance Considerations**: Cache recommendation payloads in Redis with 1-hour expirations.
- **Future Scalability**: High.
- **Whether Breaking or Backward Compatible**: Backward compatible.
- **Implementation Priority**: High.

---

## 15. AI Integration Layer Evolving Plan (Doc 14)
- **File Name**: [14_AI_Integration_Layer.md](./14_AI_Integration_Layer.md)
- **Current Purpose**: AI Gateway configurations, prompt templates, API response schemas.
- **Enhancement Summary**: Introduce a model-agnostic Provider Registry to support local Ollama servers (14B+ models) alongside cloud APIs, with fallback mechanisms.
- **New Sections to Add**:
  - `Ollama Provider Registry Integration`: Provider plugin classes targeting local port 11434 endpoints, supporting Qwen, DeepSeek, and Llama instances.
  - `Dynamic Failover Architecture`: Failover routing rules (e.g., if local Ollama GPU queue exceeds capacity, route to Groq Cloud / Gemini API).
- **Existing Sections to Update**:
  - `Provider Abstract Interface`: Ensure `BaseProviderPlugin` supports system features like prompt temperature configuration and token cost tracking.
- **New Database Tables**: None.
- **New Relationships**: None.
- **New Folder Structure**: `app/providers/plugins/ollama.py`.
- **New Services**: `MultiModelRouterService`.
- **New APIs**: None.
- **New Background Jobs**: None.
- **New Configurations**: `OLLAMA_TIMEOUT_SECONDS`, `AI_FALLBACK_PROVIDER`.
- **Migration Strategy**: Add target config metrics inside environmental `.env` files.
- **Security Considerations**: API calls must prevent exposing raw prompt inputs to external servers.
- **Performance Considerations**: Configure thread-pool processing for slow local Ollama text generations.
- **Future Scalability**: High. Allows upgrading models (e.g. from Gemma-2 to Llama-3) by updating simple configuration records.
- **Whether Breaking or Backward Compatible**: Backward compatible.
- **Implementation Priority**: Critical.

---

## 16. REST API Specification Evolving Plan (Doc 15)
- **File Name**: [15_REST_API_Specification.md](./15_REST_API_Specification.md)
- **Current Purpose**: Core JSON APIs references mapping, parameters, responses schemas.
- **Enhancement Summary**: Introduce new REST routes handling source ingestion, vector hybrid search, and the AI tutor chatbot workspace.
- **New Sections to Add**:
  - `Ingestion & Vector search API Specifications`: Definition maps for:
    - `POST /api/v1/admin/sources/ingest` - Upload files/links for ingestion.
    - `GET /api/v1/search/hybrid` - Query the unified search index.
    - `POST /api/v1/tutor/sessions` - Create interactive chat session.
    - `POST /api/v1/tutor/sessions/<id>/messages` - Post messages to tutor thread.
- **Existing Sections to Update**:
  - Update `GET /api/v1/lessons/<id>` schema: Return metadata arrays for citations, source links, and quality scores.
- **New Database Tables**: None.
- **New Relationships**: None.
- **New Folder Structure**: `app/blueprints/api/v1/tutor.py`, `app/blueprints/api/v1/ingestion.py`.
- **New Services**: None.
- **New APIs**: Defined above.
- **New Background Jobs**: None.
- **New Configurations**: None.
- **Migration Strategy**: Deploy updated API endpoints alongside the corresponding Blueprints.
- **Security Considerations**: Strict validation of JWT authentication headers across new tutor endpoints.
- **Performance Considerations**: Use server-sent events (SSE) for tutor responses to allow streaming output.
- **Future Scalability**: High.
- **Whether Breaking or Backward Compatible**: Backward compatible.
- **Implementation Priority**: Medium.

---

## 17. Admin Dashboard Evolving Plan (Doc 16)
- **File Name**: [16_Admin_Dashboard.md](./16_Admin_Dashboard.md)
- **Current Purpose**: Admin interfaces maps, course controls, logs checks.
- **Enhancement Summary**: Integrate the ingestion control panel, AI draft reviewer workspace, and vector index monitoring tools.
- **New Sections to Add**:
  - `Ingestion Pipeline Dashboard UI`: File drag-and-drop ingestion cards, link parsing progress meters, and source chunk lists.
  - `Draft Review Workspace Interface`: Multi-column view showing raw source document chunks, generated AI drafts, editor inputs, and content quality metrics.
- **Existing Sections to Update**:
  - `CMS Management Portal`: Add access points for triggering draft generations, checking grammar, and launching plagiarism scans.
- **New Database Tables**: None.
- **New Relationships**: None.
- **New Folder Structure**: None.
- **New Services**: None.
- **New APIs**: None.
- **New Background Jobs**: None.
- **New Configurations**: None.
- **Migration Strategy**: Integrate new dashboard views using Jinja2 admin templates.
- **Security Considerations**: Lock ingestion endpoints using RBAC min-role checks (`admin` or higher).
- **Performance Considerations**: Optimize page loads by loading dynamic job statuses via AJAX.
- **Future Scalability**: Modular UI panels easily adapt to new features.
- **Whether Breaking or Backward Compatible**: Backward compatible.
- **Implementation Priority**: Medium.

---

## 18. Student Dashboard Evolving Plan (Doc 17)
- **File Name**: [17_Student_Dashboard.md](./17_Student_Dashboard.md)
- **Current Purpose**: Streaks tracking screens, revision schedules, and personal bookmarks panels.
- **Enhancement Summary**: Add the AI Tutor overlay interface, weak topics alerts, and recommendations widgets.
- **New Sections to Add**:
  - `AI Tutor Overlay Component`: Chat widget that allows students to query lessons, compare technologies, or ask questions directly inside the lesson workspace.
  - `Weak Topic Alerts widget`: Highlights weak topics and suggests review resources.
- **Existing Sections to Update**:
  - `Dynamic Recommendation Panel`: Update to display adaptive course pathways.
- **New Database Tables**: None.
- **New Relationships**: None.
- **New Folder Structure**: `app/templates/learn/tutor/`.
- **New Services**: None.
- **New APIs**: None.
- **New Background Jobs**: None.
- **New Configurations**: None.
- **Migration Strategy**: Standard Blueprint integration.
- **Security Considerations**: Prevent CSS-injection via sanitized chatbot markdown outputs.
- **Performance Considerations**: Optimize chatbot response rendering using client-side JavaScript.
- **Future Scalability**: High.
- **Whether Breaking or Backward Compatible**: Backward compatible.
- **Implementation Priority**: Medium.

---

## 19. SEO Strategy Evolving Plan (Doc 18)
- **File Name**: [18_SEO_Strategy.md](./18_SEO_Strategy.md)
- **Current Purpose**: Schema.org definitions, dynamic JSON-LD tag maps, XML sitemaps builders.
- **Enhancement Summary**: Extend structured schema definitions to attribute content to original ingestion sources.
- **New Sections to Add**:
  - `Attribution & Citation Schema`: Maps external links to sources (e.g., official docs, books) using schema.org citation tags, providing clean semantic graphs for search crawlers.
- **Existing Sections to Update**:
  - `Lesson Pages JSON-LD`: Append citation links arrays.
- **New Database Tables**: None.
- **New Relationships**: None.
- **New Folder Structure**: None.
- **New Services**: `SEOService` enhancements.
- **New APIs**: None.
- **New Background Jobs**: None.
- **New Configurations**: None.
- **Migration Strategy**: Update Jinja header templates.
- **Security Considerations**: None.
- **Performance Considerations**: Keep schema generation operations computational overhead to a minimum.
- **Future Scalability**: High.
- **Whether Breaking or Backward Compatible**: Backward compatible.
- **Implementation Priority**: Low.

---

## 20. Security Architecture Evolving Plan (Doc 19)
- **File Name**: [19_Security_Architecture.md](./19_Security_Architecture.md)
- **Current Purpose**: Auth structures, session verification, cryptographies, rate limit controls.
- **Enhancement Summary**: Secure systems against prompt injection, safeguard local AI daemon endpoints, and isolate sandbox executions.
- **New Sections to Add**:
  - `Prompt Injection Defense Pipeline`: Content filters validating user-provided prompts before execution.
  - `Ollama API Token Authentication`: Validates API access keys between local daemon processes and cloud hosts.
- **Existing Sections to Update**:
  - `Rate Limiting Policies`: Define limits for AI endpoints to prevent resource depletion (e.g., `/api/v1/tutor`: max 15 runs/min per user).
- **New Database Tables**: None.
- **New Relationships**: None.
- **New Folder Structure**: None.
- **New Services**: `PromptFilterService`.
- **New APIs**: None.
- **New Background Jobs**: None.
- **New Configurations**: `OLLAMA_AUTH_TOKEN`.
- **Migration Strategy**: Configure middlewares checking token mappings.
- **Security Considerations**: Critical to prevent malicious actors from exploiting backend LLMs.
- **Performance Considerations**: Keep validation checks lightweight to prevent request overhead.
- **Future Scalability**: High.
- **Whether Breaking or Backward Compatible**: Backward compatible.
- **Implementation Priority**: High.

---

## 21. Deployment Architecture Evolving Plan (Doc 20)
- **File Name**: [20_Deployment_Architecture.md](./20_Deployment_Architecture.md)
- **Current Purpose**: Production databases connection profiles, deployment scripts, backup routines.
- **Enhancement Summary**: Define the infrastructure design for running local Ollama servers alongside cloud components, and manage the vector database.
- **New Sections to Add**:
  - `Local GPU Worker Daemon Configuration`: Configures local agent processes to listen for background compilation tasks or run vector calculations, exposing results securely via WebSockets.
  - `Vector Databases Hosting Topology`: Specifications for scaling postgres/pgvector setups on TiDB/Render environments.
- **Existing Sections to Update**:
  - `Database Backup Protocols`: Include backups for vector database values.
- **New Database Tables**: None.
- **New Relationships**: None.
- **New Folder Structure**: None.
- **New Services**: None.
- **New APIs**: None.
- **New Background Jobs**: None.
- **New Configurations**: `PGVECTOR_URL`.
- **Migration Strategy**: Integrate Alembic scripts updating databases schemas to include vector structures.
- **Security Considerations**: Enforce SSL connections for all external vector database calls.
- **Performance Considerations**: Monitor CPU utilization on local worker daemons during heavy rendering tasks.
- **Future Scalability**: Dynamic scaling allows expanding worker daemons as traffic grows.
- **Whether Breaking or Backward Compatible**: Backward compatible.
- **Implementation Priority**: High.

---

## 22. Implementation Roadmap Evolving Plan (Doc 21)
- **File Name**: [21_Implementation_Roadmap.md](./21_Implementation_Roadmap.md)
- **Current Purpose**: 6-phase implementation roadmap.
- **Enhancement Summary**: Integrate v2.0 requirements (Knowledge pipeline, vector stores, hybrid search, adaptive pathing, and Ollama providers) into the existing roadmap.
- **New Sections to Add**:
  - `Learning OS v2.0 Extended Phased Pipeline`: Checklists detailing how to merge the new systems into the implementation phases.
- **Existing Sections to Update**:
  - Update Phase 1 to Phase 6 checklists to incorporate v2.0 features, ensuring dependencies are built in logical order.
- **New Database Tables**: None.
- **New Relationships**: None.
- **New Folder Structure**: None.
- **New Services**: None.
- **New APIs**: None.
- **New Background Jobs**: None.
- **New Configurations**: None.
- **Migration Strategy**: Align code sprints with the updated Roadmap checklists.
- **Security Considerations**: None.
- **Performance Considerations**: None.
- **Future Scalability**: None.
- **Whether Breaking or Backward Compatible**: Backward compatible.
- **Implementation Priority**: High.
