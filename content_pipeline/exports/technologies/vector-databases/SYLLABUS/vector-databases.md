# Vector Databases & Semantic Search — Master Syllabus

**Target Role:** AI Engineer / RAG Specialist / Search Infrastructure Engineer  
**Difficulty Level:** Intermediate  
**Estimated Duration:** 15 Hours  
**Prerequisites:** foundations/core-python, foundations/ds-math  
**Required Courses:** foundations/core-python, foundations/ds-math  
**Optional Courses:** specializations/rag-engineering, technologies/docker  

---

## Study Flow

### Module 1 — Vector Embeddings & Similarity Mathematics
1. **Vector Space Geometry** (Dense vectors, embeddings, dimensionality, vector normalization)
2. **Distance & Similarity Metrics** (Cosine similarity, Dot product, Euclidean distance L2, Manhattan distance L1)
3. **High-Dimensional Geometry Challenges** (Curse of dimensionality, hubness problem in vector space)

### Module 2 — Approximate Nearest Neighbor (ANN) Indexing
1. **ANN vs Exact k-NN Search** (Recall vs latency trade-offs, index build time)
2. **Hierarchical Navigable Small World (HNSW)** (Graphs, entry points, multi-layer graph navigation, `efConstruction`, `M` parameter)
3. **Inverted File Index (IVF)** (Voronoi cells, centroids, `nlist`, `nprobe` tuning)
4. **Vector Quantization (Product Quantization - PQ)** (Scalar quantization, vector compression, memory reduction)

### Module 3 — ChromaDB (Local Embedded Vector Database)
1. **ChromaDB Architecture** (In-memory and persistent local storage, SQLite/DuckDB backing)
2. **Collections & Document Operations** (Creating collections, inserting text & embeddings, metadata attachments)
3. **Querying & Filtering** (Similarity querying, `where` metadata filtering, `where_document` text filtering)

### Module 4 — Cloud & Production Vector Databases (Qdrant & Pinecone)
1. **Qdrant Architecture** (Payload-based filtering, Rust engine, gRPC/REST clients, HNSW indexing)
2. **Pinecone Cloud Architecture** (Serverless indexes, pods, namespaces, pod sizing, read/write units)
3. **Hybrid Search Integration** (Combining dense vector search with sparse BM25 keyword search, Reciprocal Rank Fusion - RRF)

### Module 5 — Vector Database Operations & Production Scale
1. **Index Optimization & Sharding** (Memory sizing, RAM vs SSD caching, horizontal sharding)
2. **Evaluation & Benchmarking** (Measuring Recall@k, QPS throughput, p95/p99 query latency)
3. **Vector Database Security & Multi-Tenancy** (Tenant isolation via namespaces, metadata partitioning)
