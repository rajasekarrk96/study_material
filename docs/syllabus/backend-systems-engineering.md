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

#### 1.1. Module 01 — Web Transport Protocols (HTTP/1.1 to HTTP/3)
1. **HTTP Protocol Fundamentals & Evolution**
    - HTTP/1.1 Architecture: Text-Based Frames, Head-of-Line (HOL) Blocking, Keep-Alive Connections
    - HTTP/2 Architecture: Binary Framing Layer, Multiplexing, Stream Priorities, HPACK Header Compression
    - HTTP/3 & QUIC Protocol: UDP-based Transport, 0-RTT Handshake, Connection Migration
2. **Sockets, Connection Handshakes & TLS Cryptography**
    - Raw TCP Socket Mechanics, Buffer Management, Socket Options (`SO_REUSEADDR`, `TCP_NODELAY`)
    - TLS 1.3 Encryption Handshake, Cipher Suites, Elliptic Curve Diffie-Hellman (ECDHE)
    - Application-Layer Protocol Negotiation (ALPN) & PKI Certificate Verification

#### 1.2. Module 02 — Routing Engines & DTO Serialization Architecture
1. **High-Performance Routing Algorithms**
    - Router Internal Mechanics: Static Hash Mapping vs Regex Matching vs Radix Tree (Trie) Routers
    - URL Parameter Extraction, Query String Parsing, Matrix Parameters
    - Routing Middleware Pipeline & Wildcard / Catch-All Route Resolution
2. **Data Serialization & DTO Transformation**
    - Serialization Benchmarks: JSON (Jackson / Serde / System.Text.Json), Protocol Buffers, FlatBuffers, MessagePack
    - Schema Validation Engines: JSON Schema Validation, Pydantic, FluentValidation
    - Data Transfer Object (DTO) Mapping Patterns, Input Sanitization, Preventing Mass Assignment

#### 1.3. Module 03 — Request Context, Interceptors & Middleware Pipeline
1. **Middleware Architecture & Pipeline Execution**
    - Interceptor Pattern & Middleware Chaining Mechanisms
    - Short-Circuiting Requests, Global Error Handling, Exception Formatting Standards
    - Cross-Origin Resource Sharing (CORS) Mechanics: Preflight `OPTIONS` Requests, Access-Control Headers
2. **Request Context Propagation**
    - Context Propagation Across Threads & Async Calls (Correlation ID, W3C Trace Context)
    - Deadline Propagation & Request Timeout Cancellation Tokens
    - User Principal, Claims, and Request-Scoped Dependency Injection

#### 1.4. Module 04 — Rate Limiting, Throttling & Traffic Management
1. **Rate Limiting Algorithms**
    - Token Bucket Algorithm Mechanics & Mathematical Implementation
    - Leaky Bucket Algorithm Mechanics & Smooth Output Rate Shaping
    - Fixed Window Counter vs Sliding Window Log vs Sliding Window Counter
2. **Distributed Traffic Management**
    - Distributed Rate Limiting with Redis & Lua Scripts for Atomic Operations
    - API Throttling Headers (`X-RateLimit-Limit`, `X-RateLimit-Remaining`, `Retry-After`)
    - DDoS Mitigation & IP Reputation Filtering at API Gateway Layer

#### 1.5. Module 05 — Layered Architecture & Business Logic Layer (BLL)
1. **Architectural Patterns for Backend Applications**
    - Separation of Concerns: Controllers/Handlers ➔ Application Services ➔ Domain Layer ➔ Infrastructure
    - Domain-Driven Design (DDD): Aggregates, Entities, Value Objects, Domain Events, Repositories
    - Clean Architecture / Hexagonal Architecture (Ports and Adapters) Decoupling
2. **CRUD Mechanics Deep Dive & Transactional Workflows**
    - Optimistic Locking (Version Column) vs Pessimistic Locking (`SELECT FOR UPDATE`)
    - Pagination Mechanics: Offset-Based Pagination vs Cursor-Based (Seek) Pagination
    - Soft Deletes Pattern, Audit Logging, and Historical State Tracking

#### 1.6. Module 06 — Database Selection, Connection Pooling & ORM Architecture
1. **Database Selection Matrix & Storage Engine Mechanics**
    - Relational (RDBMS) vs Document (MongoDB) vs Key-Value (Redis) vs Graph (Neo4j) Selection Matrix
    - Storage Engine Internals: B-Tree Indexes vs Log-Structured Merge (LSM) Trees
2. **Connection Pooling & ORM Optimization**
    - Connection Pool Internal Mechanics: HikariCP / Asyncpg Pool Sizing, Idle Timeouts, Connection Leak Detection
    - Object-Relational Mapping (ORM) Pitfalls: N+1 Select Problem, Lazy Loading Bottlenecks
    - Database Migrations Engine (Flyway, Liquibase, Alembic, EF Migrations)

#### 1.7. Module 07 — Advanced Database Transactions & Distributed Consistency
1. **ACID Guarantees & Transaction Isolation**
    - ACID Properties Breakdown (Atomicity, Consistency, Isolation, Durability)
    - Transaction Isolation Levels: Read Uncommitted, Read Committed, Repeatable Read, Serializable
    - Read Phenomena: Dirty Reads, Non-Repeatable Reads, Phantom Reads, Serialization Anomalies
2. **Distributed Transactions & Consensus**
    - Two-Phase Commit (2PC) Protocol & Blocking Coordinator Limitations
    - Saga Pattern Architecture: Choreography-based Sagas vs Orchestration-based Sagas
    - Eventual Consistency, CAP Theorem, and PACELC Theorem Trade-Off Analysis

#### 1.8. Module 08 — Caching Architecture & In-Memory Data Acceleration
1. **Caching Patterns & Topology**
    - Multi-Tier Caching Architecture: Local In-Memory Cache (Guava/Caffeine) + Distributed Cache (Redis Cluster)
    - Caching Design Patterns: Cache-Aside (Lazy Loading), Write-Through, Write-Behind (Write-Back), Refresh-Ahead
2. **Cache Management & Failure Mitigation**
    - Cache Invalidation Strategies & TTL Management
    - Cache Stampede (Thundering Herd) Mitigation using Mutex Locks & Probabilistic Early Expiration
    - Eviction Policies: Least Recently Used (LRU), Least Frequently Used (LFU), Adaptive Replacement Cache (ARC)

#### 1.9. Module 09 — Asynchronous Task Queues & Distributed Messaging
1. **Message Broker Architecture**
    - Queue-Based Brokers (RabbitMQ AMQP) vs Log-Based Event Streams (Apache Kafka)
    - Producer-Consumer Pattern, Exchange Types (Direct, Fanout, Topic, Headers)
    - Consumer Thread Pools, Prefetch Count Tuning, Message Acknowledgments (ACK/NACK)
2. **Fault-Tolerant Queue Processing**
    - Dead Letter Queues (DLQ) & Poison Pill Message Isolation
    - Exponential Backoff Retries & Jitter Implementation
    - Transactional Outbox Pattern for Guaranteed At-Least-Once Delivery
    - Distributed Job Scheduling & Idempotent Consumer Design

#### 1.10. Module 10 — Search Engines & Vector Database Systems
1. **Full-Text Search Engine Architecture**
    - Inverted Index Data Structure: Tokenization, Stemming, Stop Words, TF-IDF, BM25 Scoring
    - Elasticsearch / OpenSearch Integration: Shards, Replicas, Index Mapping, Aggregations Query Engine
2. **Vector Embeddings & Vector Search**
    - Vector Embeddings Generation & High-Dimensional Vector Spaces
    - Approximate Nearest Neighbor (ANN) Indexing: HNSW (Hierarchical Navigable Small World) & IVFFlat
    - Vector Databases Integration: Qdrant, Pinecone, Milvus, pgvector

#### 1.11. Module 11 — Object Storage & Large File Streaming Architecture
1. **S3-Compatible Object Storage**
    - Object Storage Architecture: Buckets, Keys, Objects, Metadata, Flat Namespace
    - High-Throughput Multipart Upload Protocol & Chunked Transfer Encoding
    - Direct Client-to-S3 Uploads via Presigned URLs & Access Control Policies
2. **Large File Streaming Engine**
    - HTTP Range Requests (`Range: bytes=0-1023`) & Partial Content Responses (`206 Partial Content`)
    - Streaming Large Files without RAM Exhaustion (Node.js Streams, Python Generators, C# `IAsyncEnumerable`)

#### 1.12. Module 12 — Real-Time Protocols & Webhook Infrastructure
1. **Real-Time Web Communication**
    - WebSockets Protocol: Handshake Upgrade (`101 Switching Protocols`), Framing, Heartbeats
    - Server-Sent Events (SSE) Protocol: HTTP/2 Multiplexed Event Streaming vs WebSockets
    - gRPC Streaming: Unary vs Server Streaming vs Client Streaming vs Bi-Directional Streaming
2. **Enterprise Webhook Subscription Engine**
    - Webhook Architecture: Event Triggers, Subscriber Registration, Payload Delivery Workers
    - Webhook Security: Payload HMAC-SHA256 Signing & Verification
    - Webhook Reliability: Exponential Backoff Retries, Delivery Logs, Idempotency Keys

#### 1.13. Module 13 — Distributed Tracing, Logging & OpenTelemetry Observability
1. **Structured Logging & Log Aggregation**
    - Structured JSON Logging, Contextual Property Injection, Log Levels Management
    - Centralized Log Aggregation Pipeline (ELK Stack / Grafana Loki)
2. **Distributed Tracing & Metrics Collection**
    - W3C Trace Context Specification: Trace ID, Span ID, Trace Parent Headers
    - OpenTelemetry Collector Setup, Span Instrumentation, Jaeger / Zipkin Visualization
    - Metrics Collection with Prometheus: Counters, Gauges, Histograms, Summaries & Grafana Dashboards

#### 1.14. Module 14 — Process Lifecycle, Resilience & Circuit Breakers
1. **Graceful Shutdown & Lifecycle Management**
    - Process OS Signal Handling (`SIGTERM`, `SIGINT`, `SIGHUP`)
    - Connection Draining Mechanics: Stopping New Traffic, Completing In-Flight Tasks, Closing Pools
    - Kubernetes Liveness, Readiness, and Startup Health Check Probes Implementation
2. **Resilience Engineering Patterns**
    - Circuit Breaker Pattern Architecture (Closed, Open, Half-Open States) via Resilience4j / Polly
    - Bulkhead Isolation Pattern to Prevent Cascading Failures
    - Fallback Responses, Rate-Limiting Degradation, Load Shedding

#### 1.15. Module 15 — Security, 12-Factor App & Production Hardening
1. **Backend Security & OAuth2 / OIDC**
    - OWASP Top 10 API Security Risks Mitigation
    - OAuth 2.0 Authorization Code Flow with PKCE & OpenID Connect (OIDC) Setup
    - JWT Revocation Strategies: Blacklisting in Redis, Short-Lived Tokens, Refresh Token Rotation
2. **OpenAPI Standards & 12-Factor App Hardening**
    - OpenAPI 3.1 Specification & Automated Swagger UI Documentation Generation
    - The 12-Factor App Methodology Deep Dive
    - Production Architecture Hardening & Capstone Backend System Audit
