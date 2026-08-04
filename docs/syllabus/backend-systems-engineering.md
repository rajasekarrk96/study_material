# Master Backend Systems & Architecture — Master Syllabus

**Target Role:** Principal Backend Engineer / Distributed Systems Architect / Tech Lead  
**Difficulty Level:** Advanced  
**Estimated Duration:** 250 Hours  
**Prerequisites:** networking-fundamentals, computer-fundamentals, database-technologies  
**Required Courses:** rest-api-development, linux-administration, mysql  
**Optional Courses:** devops, docker, cloud-computing  

---

## Study Flow

### 1. Core Backend Architecture & Request Lifecycle

#### 1.1. Module 1 — Web Transport, Protocols & Routing
1. **HTTP Protocol Deep Dive**
    - HTTP/1.1, HTTP/2 (Multiplexing, Header Compression HPACK), and HTTP/3 (QUIC, UDP-based Transport)
    - Verbs (GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD), Headers, Raw Socket Request-Response Lifecycle
    - Status Codes Classification (1xx, 2xx, 3xx, 4xx, 5xx) & Enterprise Custom Error Contracts
    - Handshake Protocol Mechanics: TLS 1.3 Key Exchange, Certificate Validation, ALPN Negotiation
2. **Routing Engine Architecture & DTO Serialization**
    - URL Routing Algorithms: Trie-Based (Radix Tree) Routers vs Regex Routers vs Static Hash Maps
    - Serialization & Deserialization Engines: JSON (Jackson/Serde/System.Text.Json), Protocol Buffers, FlatBuffers
    - Schema Validation, Type Transformation, DTO Binding & Input Sanitization
    - Content Negotiation (`Accept`, `Content-Type`), Custom Formatter Registration

#### 1.2. Module 2 — Middleware, Context & Layered Architecture
1. **Middleware Pipeline & Request Context Propagation**
    - Interceptor Pattern & Middleware Chaining Execution Order
    - Request-Scoped Context Propagation: Correlation/Trace IDs, Cancellation Tokens, User Principal, Deadlines
    - Global Error Handling Filters, Cross-Origin Resource Sharing (CORS) Security Middleware
    - Rate Limiting Middleware Algorithms: Token Bucket, Leaky Bucket, Fixed Window, Sliding Window Log
2. **Layered Architecture & Business Logic Layer (BLL)**
    - Separation of Concerns: Handlers/Controllers, Business Services, Repositories, Domain Models
    - Domain-Driven Design (DDD): Aggregates, Entities, Value Objects, Domain Events, Ubiquitous Language
    - Clean Architecture / Hexagonal Architecture (Ports and Adapters) Implementation Patterns
    - CRUD Deep Dive: Optimistic Locking, Pessimistic Locking, Cursor-Based Pagination vs Offset Pagination, Soft Deletes

#### 1.3. Module 3 — Data Access, Caching & Task Queuing
1. **Databases, ORM & Transaction Architecture**
    - Relational (SQL) vs NoSQL (Document, Key-Value, Columnar) vs Graph Database Selection Matrix
    - Connection Pooling Mechanics: Pool Sizing Math, Max Idle Connections, Keep-Alive, Connection Leak Detection
    - ACID Guarantees, Isolation Levels (Read Uncommitted, Read Committed, Repeatable Read, Serializable)
    - Distributed Transactions: Saga Pattern (Choreography vs Orchestration), Two-Phase Commit (2PC)
2. **Caching Strategies & In-Memory Data Acceleration**
    - Redis & Memcached Architectural Comparison & Data Structures (Hashes, Sorted Sets, Bitmaps, HyperLogLogs)
    - Caching Design Patterns: Cache-Aside, Write-Through, Write-Behind (Write-Back), Refresh-Ahead
    - Cache Invalidation Strategies, Cache Stampede (Thundering Herd) Mitigation, Eviction Policies (LRU, LFU, ARC)
    - Distributed Caching Consistency & Multi-Tier Caching (Local In-Memory Cache + Redis Cluster)
3. **Asynchronous Task Queues & Job Scheduling**
    - Message Brokers Architectural Comparison: RabbitMQ (AMQP), Apache Kafka (Log-based), BullMQ, Celery
    - Producer-Consumer Pattern, Worker Thread Pools, Message Acknowledgment (ACK/NACK)
    - Dead Letter Queues (DLQ), Exponential Backoff Retries, Poison Pill Message Handling
    - Distributed Cron Scheduling, Job Idempotency, Scheduled Background Worker Infrastructure

#### 1.4. Module 4 — Search Engines, Storage & Real-Time Protocols
1. **Search Engines & Vector Databases**
    - Inverted Index Mechanics: Tokenization, Stemming, Stop Words, TF-IDF, BM25 Scoring
    - Elasticsearch / OpenSearch Integration: Cluster Architecture, Shards, Replicas, Index Mapping, Aggregations
    - Vector Embeddings & Vector Databases: HNSW Indexing, Cosine Similarity, Qdrant, Pinecone, pgvector Integration
2. **Object Storage & Large File Streaming Engine**
    - S3-Compatible Object Storage Architecture: Buckets, Keys, Metadata, Blob Storage
    - High-Throughput Multipart Uploads, Chunked Transfer Encoding, Range Requests for Video Streaming
    - Presigned URLs for Direct Browser-to-S3 Uploads, Lifecycle Rules, Storage Tiering
3. **Real-Time Backend Protocols & Webhook Subscriptions**
    - WebSockets Protocol: Handshake Upgrade, Framing, Ping/Pong Heartbeats, Connection State Management
    - Server-Sent Events (SSE) vs WebSockets vs gRPC Streaming Architectural Selection Matrix
    - Webhook Subscription Engine Architecture: HMAC-SHA256 Payload Signing, Event Delivery Worker Queues, Retry Policies

#### 1.5. Module 5 — Observability, Security & Production Hardening
1. **Logging, Monitoring & OpenTelemetry Observability**
    - Structured Logging (JSON Format), Contextual Enrichment, Log Aggregation (ELK Stack / Loki)
    - Distributed Tracing Mechanics: W3C Trace Context Specification, OpenTelemetry Spans, Jaeger Integration
    - Metrics Collection & Alerting: Prometheus Metric Types (Counter, Gauge, Histogram, Summary), Grafana Dashboards
    - Liveness, Readiness, and Startup Health Check Probes in Distributed Systems
2. **Graceful Shutdown & Process Lifecycle Management**
    - Process OS Signal Handling (`SIGTERM`, `SIGINT`, `SIGHUP`)
    - Connection Draining: Stopping Inbound Requests, Flushing In-Flight Async Tasks, Closing DB Connection Pools
    - Circuit Breaker Pattern (Resilience4j / Polly) & Bulkhead Isolation Mechanics
3. **Backend Security, 12-Factor App & Production Hardening**
    - OWASP Top 10 API Security Risks: Broken Object Level Authorization (BOLA), Mass Assignment, Injection
    - Authentication Protocols: OAuth 2.0 Authorization Code Flow with PKCE, OpenID Connect (OIDC), JWT Revocation Strategies
    - OpenAPI 3.1 Specification, Automated Swagger UI Generation, API Versioning Strategies (URL Path vs Header)
    - The 12-Factor App Methodology: Codebase, Dependencies, Config in Environment, Backing Services, Stateless Processes
