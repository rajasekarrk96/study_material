# .NET Full Stack Engineering — Master Syllabus

**Target Role:** .NET Full Stack Developer / C# Solutions Architect / Enterprise Application Engineer  
**Difficulty Level:** Advanced  
**Estimated Duration:** 350 Hours  
**Prerequisites:** computer-fundamentals, networking-fundamentals  
**Required Courses:** c-programming, mysql  
**Optional Courses:** react, docker, aws  

---

## Study Flow

### 1. C# & .NET Core Foundations

#### 1.1. Module 1 — C# Language Architecture & Memory Management (C# 12 / 13)
1. **C# Fundamentals & Runtime Architecture**
    - .NET SDK, CLR (Common Language Runtime), JIT Compiler, and MSIL (CIL)
    - Value Types vs Reference Types, Stack vs Managed Heap Allocation
    - Nullable Reference Types, Required Members, Primary Constructors, Record Types
    - Pattern Matching (Switch Expressions, Positional/Property Patterns)
2. **Advanced Memory Management & High Performance**
    - Garbage Collection Mechanics (Gen 0, Gen 1, Gen 2, Large Object Heap LOH)
    - High-Performance Memory Abstractions: `Span<T>`, `ReadOnlySpan<T>`, `Memory<T>`
    - `ref struct` Types, Stackalloc, and Zero-Allocation Programming Patterns
    - Finalizers, `IDisposable` Pattern, and `SafeHandle` Mechanics

#### 1.2. Module 2 — Generics, Collections & Asynchronous Programming
1. **Generics, Collections & LINQ**
    - Custom Generic Classes, Interfaces, Constraints, Covariance, and Contravariance
    - System.Collections.Generic vs System.Collections.Concurrent Collections
    - LINQ to Objects: deferred execution, expression trees, custom extension methods
    - Performance Tuning LINQ Queries & Memory Benchmarking with BenchmarkDotNet
2. **Asynchronous & Concurrent Programming**
    - Task-Based Asynchronous Pattern (TAP): `Task`, `Task<T>`, `async` / `await`
    - `ValueTask<T>` Optimization for High-Throughput Paths
    - Synchronization Primitives: `SemaphoreSlim`, `Monitor`, `ReaderWriterLockSlim`
    - `IAsyncEnumerable<T>` for Asynchronous Data Streaming

#### 1.3. Module 3 — ASP.NET Core Web API Architecture (.NET 8 / 9)
1. **API Pipeline & Server Infrastructure**
    - Kestrel High-Performance Web Server & Program.cs Setup
    - Dependency Injection Container: Transient, Scoped, Singleton Lifetimes
    - Action Filters, Result Filters, Resource Filters, and Custom Exception Filters
    - Request Routing, DTO Binding, Model Validation with FluentValidation
2. **Configuration, Logging & Observability**
    - Options Pattern (`IOptions`, `IOptionsSnapshot`, `IOptionsMonitor`)
    - Structured Logging with Serilog & OpenTelemetry Integration
    - Middleware Construction & Global Exception Handler (`IExceptionHandler`)

#### 1.4. Module 4 — Entity Framework Core 8/9 Enterprise Persistence
1. **EF Core Architecture & Code-First Mapping**
    - `DbContext` Configuration, Connection Pooling, and DbContext Lifecycle
    - Entity Mapping (Fluent API, Value Converters, Shadow Properties, Owned Types)
    - Database Migrations, Seeding, and Schema Version Control
2. **Querying, Performance Tuning & Transactions**
    - LINQ to Entities: Eager Loading (`Include`), Lazy Loading, Explicit Loading
    - Compiled Queries, Split Queries (`AsSplitQuery`), and No-Tracking (`AsNoTracking`)
    - EF Core Interceptors, Global Query Filters, Command Batching, and Execution Strategy
    - Database Transactions: `IDbContextTransaction` and Distributed Transactions

#### 1.5. Module 5 — ASP.NET Core Security & Authentication Systems
1. **Identity Management & Token Security**
    - ASP.NET Core Identity Architecture: Users, Roles, Claims, Store Implementation
    - JWT (JSON Web Token) Authentication: Signing Keys, Issuance, Validation, Token Refresh
    - Policy-Based & Role-Based Authorization, Custom Authorization Handlers
2. **Web Security Hardening**
    - Protection against OWASP Top 10: XSS, CSRF, SQL Injection, CORS Hardening
    - Rate Limiting Middleware (`System.Threading.RateLimiting`)
    - Data Protection API (`IDataProtectionProvider`) for Sensitive Field Encryption

#### 1.6. Module 6 — Microservices, gRPC & Distributed Messaging
1. **gRPC & High-Throughput Service Communication**
    - Protocol Buffers (`.proto`) Schema Definition & Code Generation
    - Unary, Server Streaming, Client Streaming, and Bi-Directional Streaming gRPC
    - Interceptors, Channel Management, and HTTP/2 Infrastructure
2. **Distributed Messaging with MassTransit & RabbitMQ**
    - Event-Driven Architecture: Publish/Subscribe, Commands vs Events
    - MassTransit Setup: Message Handlers, Consumers, Outbox Pattern
    - Message Dead-Letter Queues (DLQ), Retries, and Circuit Breaker Policies

#### 1.7. Module 7 — Modern Frontend Integration (Blazor & React)
1. **Blazor Web Architecture (Blazor United / Server / WASM)**
    - Component Lifecycle Methods (`OnInitializedAsync`, `OnParametersSetAsync`)
    - State Management, Cascading Parameters, and Event Callback Binding
    - Blazor WebAssembly Interop with JavaScript & Offline PWA Capability
2. **React Integration with ASP.NET Core**
    - SPA Middleware Configuration & Vite Integration
    - Building REST API Consumers with Axios / Fetch API & React Query
    - State Management & Component Communication in Full-Stack Apps

#### 1.8. Module 8 — Testing, DevOps & Production Deployment
1. **Testing Infrastructure (xUnit & Moq)**
    - Unit Testing with xUnit, FluentAssertions, and Moq Framework
    - Integration Testing with `WebApplicationFactory` and Testcontainers for .NET
    - API Contract Testing & EF Core In-Memory / SQLite Test Setup
2. **Dockerization, Azure & CI/CD Pipeline**
    - Multi-Stage Dockerfile Optimization for .NET 8/9 Applications
    - Azure App Services, Azure SQL Database, and Azure Key Vault Integration
    - GitHub Actions Workflow for Automated Build, Test, and Deployment
