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

#### 1.1. Module 01 — C# Language Architecture & Runtime Mechanics (C# 12 / 13)
1. **.NET SDK & Common Language Runtime (CLR)**
    - .NET SDK, CLI Commands, Solution Structure (`.sln`), Project Files (`.csproj`)
    - CLR Architecture: Intermediate Language (MSIL/CIL), JIT Compiler (RyuJIT), Assemblies
    - Managed vs Unmanaged Code Execution & P/Invoke Interop
    - Global Assembly Cache (GAC) vs Local Package Resolution & NuGet Package Management
2. **C# Data Types & Type System**
    - Value Types vs Reference Types, Primitive Types, Enums, Structs
    - Stack Allocation vs Managed Heap Allocation
    - Type Casting, Boxing, and Unboxing Overhead
    - Nullable Value Types (`Nullable<T>`) & Nullable Reference Types (`#nullable enable`)

#### 1.2. Module 02 — Modern C# Language Features (C# 10 to C# 13)
1. **Object-Oriented & Immutable Programming**
    - Classes, Interfaces, Inheritance, Abstract Classes, Polymorphism
    - Record Types (`record class`, `record struct`), Nondestructive Mutation (`with` expression)
    - Primary Constructors, Required Members (`required`), Init-Only Setters (`init`)
    - Extension Methods, Top-Level Statements, Global Using Directives
2. **Pattern Matching & Advanced Syntax**
    - Type Patterns, Constant Patterns, Relational Patterns, Logical Patterns
    - Property Patterns, Positional Patterns, Tuple Patterns, List Patterns
    - Switch Expressions & Guard Clauses (`when` keyword)
    - Pattern Matching with Sealed Hierarchies

#### 1.3. Module 03 — Advanced Memory Management & Zero-Allocation C#
1. **Garbage Collection (GC) Mechanics**
    - GC Generations: Generation 0, Generation 1, Generation 2, Large Object Heap (LOH), Pinned Object Heap (POH)
    - GC Modes: Workstation GC vs Server GC, Background GC, Concurrent GC
    - Finalizers, Destructors, `GC.SuppressFinalize()`, and `SafeHandle`
    - Standard `IDisposable` Pattern Implementation & `await using` (`IAsyncDisposable`)
2. **High-Performance Memory Abstractions**
    - `Span<T>` and `ReadOnlySpan<T>` for Contiguous Memory Manipulation
    - `Memory<T>` and `ReadOnlyMemory<T>` for Async Heap Allocations
    - `ref struct` Rules, `stackalloc` Memory Allocation, `MemoryMarshal` Utility
    - Array Pooling (`ArrayPool<T>`) & Buffer Recycling to Prevent GC Pressure

#### 1.4. Module 04 — Generics, Collections & Performance LINQ
1. **Generics & Collection Framework**
    - Custom Generic Classes, Structs, Interfaces, and Methods
    - Generic Constraints (`where T : class`, `struct`, `new()`, `unmanaged`, `notnull`)
    - Covariance (`out`) and Contravariance (`in`) in Generic Interfaces
    - Standard Collections (`List<T>`, `Dictionary<K,V>`) vs Concurrent Collections (`ConcurrentDictionary`, `Channel<T>`)
2. **LINQ Engine & Performance Optimization**
    - LINQ to Objects Architecture: Deferred Execution vs Immediate Execution
    - Standard Query Operators: `Where`, `Select`, `SelectMany`, `GroupBy`, `Join`, `Zip`
    - Expression Trees (`Expression<Func<T>>`) & Dynamic Query Parsing
    - Performance Tuning LINQ: Avoiding Allocations, `StructEnumerable`, BenchmarkDotNet Profiling

#### 1.5. Module 05 — Asynchronous & Multithreaded Programming
1. **Task-Based Asynchronous Pattern (TAP)**
    - Async/Await Keyword Mechanics, State Machine Generation by Compiler
    - `Task` vs `Task<T>` vs `ValueTask` vs `ValueTask<T>` Selection Matrix
    - SynchronizationContext, `ConfigureAwait(false)`, and Thread Pool Scheduling
    - Exception Handling in Async Code & `AggregateException`
2. **Concurrency & Multithreading**
    - Thread Pool Mechanics, Worker Threads vs I/O Completion Threads
    - Synchronization Primitives: `SemaphoreSlim`, `Mutex`, `AutoResetEvent`, `ReaderWriterLockSlim`
    - Interlocked Operations (`Interlocked.Increment`, `CompareExchange`)
    - `CancellationToken` and `CancellationTokenSource` Cancellation Mechanics

#### 1.6. Module 06 — ASP.NET Core Web API Architecture (.NET 8 / 9)
1. **Kestrel Web Server & Request Pipeline**
    - Kestrel High-Performance Web Server Configuration & HTTP/2, HTTP/3 Protocols
    - Program.cs Minimal API Setup vs Controller-Based API Architecture
    - Middleware Pipeline Construction, Middleware Order, Custom Middleware Classes
    - Request Routing Map (`MapGet`, `MapPost`, Attribute Routing) & Endpoint Metadata
2. **Dependency Injection (DI) Engine**
    - Built-in Service Container: Service Descriptors & Registration Methods
    - Service Lifetimes: Transient, Scoped, Singleton Scope Rules
    - Service Lifetime Validation, Captive Dependencies Detection
    - Keyed Services (`AddKeyedScoped`, `AddKeyedSingleton`) in .NET 8/9

#### 1.7. Module 07 — ASP.NET Core Middleware, Filters & Validation
1. **Filters Pipeline Architecture**
    - Action Filters, Result Filters, Resource Filters, Authorization Filters, Exception Filters
    - Creating Custom Attribute Filters & Registering Global Filters
    - Model Binding Engine (`[FromBody]`, `[FromQuery]`, `[FromRoute]`, `[FromHeader]`)
    - Request Validation with FluentValidation Library & Automatic Validation Pipeline
2. **Configuration & Options Pattern**
    - AppSettings.json Configuration Providers, Environment Variables, Command Line Args
    - Strongly-Typed Options Pattern (`IOptions<T>`, `IOptionsSnapshot<T>`, `IOptionsMonitor<T>`)
    - Options Validation with DataAnnotations & FluentValidation

#### 1.8. Module 08 — Entity Framework Core 8/9 Persistence Engine
1. **DbContext & Code-First Mapping**
    - `DbContext` Architecture, Connection Pooling (`AddDbContextPool`)
    - Entity Configuration: Data Annotations vs Fluent API (`IEntityTypeConfiguration<T>`)
    - Complex Types, Value Converters, Shadow Properties, Owned Entity Types
    - Code-First Migrations Workflow, Migration Scripts Generation, Database Seeding
2. **Querying, Performance & Change Tracking**
    - LINQ to Entities: Eager Loading (`Include`, `ThenInclude`), Explicit Loading, Lazy Loading
    - Compiled Queries, Split Queries (`AsSplitQuery`), No-Tracking Queries (`AsNoTracking`)
    - Change Tracker Mechanics, Entity States (`Added`, `Modified`, `Unchanged`, `Deleted`)
    - Bulk Operations (`ExecuteUpdateAsync`, `ExecuteDeleteAsync`) in EF Core 8/9

#### 1.9. Module 09 — EF Core Advanced Transactions & Diagnostics
1. **Transactions & Concurrency Control**
    - Database Transactions (`IDbContextTransaction`) & Savepoints
    - Optimistic Concurrency Control with RowVersion (`[Timestamp]`) Attributes
    - Handling `DbUpdateConcurrencyException` & Resolution Strategies
    - Execution Strategies, Connection Resiliency, and Retries (`EnableRetryOnFailure`)
2. **Interceptors & Performance Tuning**
    - EF Core Interceptors (`DbCommandInterceptor`, `DbTransactionInterceptor`)
    - Logging Raw Generated SQL Queries & OpenTelemetry Integration
    - Database Indexing Strategies & Raw SQL Execution (`FromSqlRaw`, `SqlQuery`)

#### 1.10. Module 10 — ASP.NET Core Security & Authentication Systems
1. **Identity & Token Authentication**
    - ASP.NET Core Identity Architecture: UserManager, RoleManager, SignInManager
    - JWT (JSON Web Token) Bearer Authentication: Token Generation, Validation Parameters, Claims
    - Refresh Token Rotation Pattern & Revocation Lists in Redis
    - OAuth2 & OpenID Connect (OIDC) Integration with Duende IdentityServer
2. **Authorization & API Hardening**
    - Role-Based Authorization (`[Authorize(Roles = "...")]`)
    - Claim-Based & Policy-Based Authorization (`IAuthorizationHandler`, `IAuthorizationRequirement`)
    - Protection against OWASP Top 10 API Security Risks
    - Rate Limiting Middleware (`AddFixedWindowLimiter`, `AddSlidingWindowLimiter`)

#### 1.11. Module 11 — Real-Time Communications with SignalR
1. **SignalR Architecture & Hubs**
    - SignalR Hubs Setup, Transport Protocols (WebSockets, Server-Sent Events, Long Polling)
    - Strongly-Typed Hubs (`Hub<T>`) & Client Method Invocations
    - Group Messaging, User-Targeted Notifications, Connection Lifecycle Events
2. **SignalR Scaling & Performance**
    - Redis Backplane for Horizontal SignalR Scaling across Multiple Servers
    - Binary Protocol Support with MessagePack Serialization
    - SignalR Security & JWT Authentication over WebSockets

#### 1.12. Module 12 — Enterprise Microservices Architecture with gRPC & MassTransit
1. **High-Performance gRPC Services**
    - Protocol Buffers (`.proto`) Contract Definitions & C# Code Generation
    - Unary RPCs, Server Streaming, Client Streaming, Bi-Directional Streaming Services
    - gRPC Interceptors, Authentication, Metadata Headers, Deadline Management
2. **Event-Driven Messaging with MassTransit & RabbitMQ**
    - Event-Driven Microservices Architecture: Commands vs Events
    - MassTransit Bus Configuration: Consumers, Handlers, Saga State Machines
    - Outbox Pattern Implementation for Reliable Message Publishing
    - Dead Letter Queues (DLQ), Exponential Backoff Retries, Circuit Breaker Policies

#### 1.13. Module 13 — Modern Frontend Integration (Blazor United / Server / WASM)
1. **Blazor Component Architecture**
    - Blazor Render Modes (.NET 8/9 Interactive Server, Interactive WASM, Interactive Auto)
    - Component Lifecycle Methods (`OnInitializedAsync`, `OnParametersSetAsync`)
    - Parameter Binding, Event Callback Binding, Cascading Values
2. **State Management & JS Interop**
    - Application State Management & Custom State Containers
    - JavaScript Interop (`IJSRuntime`): Calling JS from C# and C# from JS
    - Building Offline Progressive Web Apps (PWA) with Blazor WebAssembly

#### 1.14. Module 14 — React & Angular Integration with ASP.NET Core
1. **React SPA Integration**
    - Single Page Application (SPA) Hosting & Vite Dev Server Integration
    - Consuming ASP.NET Core REST APIs with Axios / Fetch API & TanStack Query (React Query)
    - State Management (Zustand / Redux Toolkit) in Full-Stack .NET Apps
2. **Angular SPA Integration**
    - Angular Services, RxJS Observables, HttpClient Module Integration
    - JWT Interceptors in Angular & Route Guards

#### 1.15. Module 15 — Testing Infrastructure & Code Quality
1. **Unit Testing with xUnit & Moq**
    - Unit Testing Principles, AAA (Arrange, Act, Assert) Pattern
    - xUnit Test Runner, `@Fact`, `@Theory`, `@InlineData`, `@MemberData`
    - Mocking Dependencies with Moq Framework (`Mock<T>`, `.Setup()`, `.Returns()`, `.Verify()`)
    - Asserting Exceptions & FluentAssertions Library Integration
2. **Integration Testing & Testcontainers**
    - Integration Testing with `WebApplicationFactory<TEntryPoint>`
    - Custom In-Memory Test Server Configuration & Service Overrides
    - Spinning up Real SQL Server / Redis Containers with Testcontainers for .NET

#### 1.16. Module 16 — Observability, Logging & Health Management
1. **Structured Logging & OpenTelemetry**
    - Serilog Configuration: Sinks (Console, File, Seq, Elasticsearch), Enrichers
    - Contextual Logging (`LogContext.PushProperty`) & Trace Correlation IDs
    - OpenTelemetry Distributed Tracing & Metrics Collection
2. **Health Checks & Monitoring**
    - ASP.NET Core Health Checks Infrastructure (`AddHealthChecks()`)
    - Custom Health Check Implementations (`IHealthCheck`) for SQL Server, Redis, RabbitMQ
    - Health Check UI Dashboard & Kubernetes Liveness / Readiness Probes Integration

#### 1.17. Module 17 — Multi-Stage Dockerization & Azure Cloud Deployment
1. **Containerization with Docker**
    - Multi-Stage Dockerfile Optimization for .NET 8/9 Applications
    - Alpine-based Lightweight Images & Non-Root Security Configuration
    - Docker Compose Configuration for API, SQL Server, Redis, RabbitMQ Stack
2. **Azure Cloud Deployment & CI/CD**
    - Azure App Service & Azure Container Apps Deployment
    - Azure SQL Database & Azure Key Vault Secrets Integration
    - GitHub Actions CI/CD Pipeline Configuration for Automated Build, Test, and Deploy

#### 1.18. Module 18 — Enterprise Capstone & System Design
1. **Enterprise .NET System Design**
    - Clean Architecture / Domain-Driven Design Solution Blueprint
    - CQRS & MediatR Pattern Architecture
    - SDET & Senior .NET Developer Technical Interview Preparation
2. **Capstone Project: Multi-Tenant Enterprise E-Commerce Engine**
    - Building Microservices API, Blazor Admin Dashboard, and React Storefront
    - Complete CI/CD, Containerization, and Performance Audit Delivery
