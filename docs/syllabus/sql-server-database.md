# SQL Server Enterprise Database Architecture — Master Syllabus

**Target Role:** SQL Server DBA / Database Engineer / Enterprise Backend Developer  
**Difficulty Level:** Intermediate  
**Estimated Duration:** 100 Hours  
**Prerequisites:** database-technologies  
**Required Courses:** mysql  
**Optional Courses:** dotnet-full-stack  

---

## Study Flow

### 1. SQL Server Administration & T-SQL

#### 1.1. Module 1 — Advanced T-SQL Programming & Data Types
1. **Relational Querying & Complex Joins**
    - Inner, Left Outer, Right Outer, Full Outer, Cross Joins, and Self-Joins
    - Subqueries: Correlated vs Non-Correlated, `EXISTS`, `IN`, `ALL`, `ANY` Operators
    - Data Types Deep Dive: `VARCHAR` vs `NVARCHAR`, `DATETIME2`, `DECIMAL`, `UNIQUEIDENTIFIER`
2. **Advanced T-SQL Programming Constructs**
    - Stored Procedures: Input/Output Parameters, Return Values, Error Handling (`TRY...CATCH`, `XACT_STATE()`)
    - User-Defined Functions (UDF): Scalar vs Inline Table-Valued vs Multi-Statement Table-Valued Functions
    - DML Triggers: `AFTER` Triggers, `INSTEAD OF` Triggers, `INSERTED` and `DELETED` Pseudo-Tables
    - Common Table Expressions (CTE), Recursive CTEs, and Window Functions (`ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, `LEAD`)

#### 1.2. Module 2 — SQL Server Storage Architecture & Indexing Engine
1. **Physical Storage Architecture**
    - Database Files: Master Data File (`.mdf`), Secondary Data File (`.ndf`), Transaction Log (`.ldf`)
    - Storage Structure: Data Pages (8KB), Page Header, Slot Array, Extents (64KB Uniform vs Mixed)
    - Allocation Maps: GAM, SGAM, PFS, DCM, BCM Pages
2. **Indexing Engine & B-Tree Mechanics**
    - Clustered Indexes vs Non-Clustered Indexes Architecture
    - Index B-Tree Structure: Root Level, Intermediate Level, Leaf Level (Data Pages vs RID / Clustering Key)
    - Filtered Indexes, Included Columns (`INCLUDE`), Columnstore Indexes for Analytics (OLAP)
    - Index Fragmentation Metrics, Maintenance Plans: `ALTER INDEX REORGANIZE` vs `REBUILD`

#### 1.3. Module 3 — Query Optimization, Diagnostics & Performance Tuning
1. **Execution Plan Analysis & Optimizer Mechanics**
    - Graphical Execution Plans: Index Scans vs Index Seeks, Key Lookups, Hash Match, Nested Loops, Sort Spills
    - Statistics Engine: Histograms, Density Vector, Auto-Update Statistics, Cardinality Estimator
    - Identifying Performance Bottlenecks using Query Store & Extended Events (Xe)
2. **Dynamic Management Views (DMVs) & Profiling**
    - Troubleshooting Slow Queries with DMVs (`sys.dm_exec_query_stats`, `sys.dm_exec_requests`, `sys.dm_db_index_usage_stats`)
    - TempDB Contention Diagnosis & Allocation Page Latch Contention (`PFS`, `GAM`)
    - Extended Events Sessions Creation vs Legacy SQL Server Profiler

#### 1.4. Module 4 — Transactions, Concurrency & Locking Mechanics
1. **Locking Infrastructure & Isolation Levels**
    - Lock Hierarchy: Database, Table, Page, Key, Row Locks
    - Lock Modes: Shared (S), Exclusive (X), Update (U), Intent (IS/IX), Schema Locks
    - Transaction Isolation Levels: Read Uncommitted, Read Committed, Repeatable Read, Serializable, Read Committed Snapshot Isolation (RCSI)
2. **Deadlock Analysis & Concurrency Tuning**
    - Deadlock Graph Analysis (`XML Deadlock Report`, Event Class 122)
    - Pessimistic Concurrency vs Optimistic Concurrency in SQL Server
    - Explicit Transaction Boundaries (`BEGIN TRAN`, `COMMIT TRAN`, `ROLLBACK TRAN`) & Savepoints

#### 1.5. Module 5 — SQL Server Security, Encryption & Compliance
1. **Security & Principal Architecture**
    - Authentication Modes: Windows Authentication vs SQL Server Authentication
    - Server Principals (Logins) vs Database Principals (Users), Database Roles
    - Granting, Denying, and Revoking Permissions (GRANT, DENY, REVOKE)
2. **Data Protection & Encryption Features**
    - Transparent Data Encryption (TDE) for Database Encryption at Rest
    - Always Encrypted Architecture for Sensitive Column Security
    - Dynamic Data Masking (DDM) & Row-Level Security (RLS)

#### 1.6. Module 6 — High Availability & Disaster Recovery (HADR)
1. **Backup Strategies & Point-in-Time Recovery**
    - Database Recovery Models: Simple, Full, Bulk-Logged
    - Backup Types: Full Backups, Differential Backups, Transaction Log Backups
    - Point-in-Time Database Restore Sequence & Tail-Log Backups
2. **Enterprise High Availability Architectures**
    - AlwaysOn Availability Groups (AG): Synchronous vs Asynchronous Commit, Read-Only Routing
    - Failover Cluster Instances (FCI), Database Mirroring, Log Shipping Mechanics
    - Log Shipping Setup, Monitor Server, and Manual / Automatic Failover Protocols

#### 1.7. Module 7 — Database Automation, Maintenance & ETL
1. **SQL Server Agent & Automated Maintenance**
    - SQL Server Agent Jobs, Steps, Schedules, Alerts, and Operators
    - Automated Database Integrity Checks (`DBCC CHECKDB`)
    - Transaction Log Maintenance & VLF (Virtual Log File) Management
2. **Data Integration & ETL (SSIS / Bulk Operations)**
    - Bulk Insert Operations (`BULK INSERT`, `bcp` utility)
    - SQL Server Integration Services (SSIS) Control Flow & Data Flow Packages

#### 1.8. Module 8 — Cloud Database & Azure SQL Migration
1. **Azure SQL Database & Managed Instance**
    - Azure SQL Database vCore vs DTU Purchasing Models
    - Azure SQL Managed Instance Compatibility & Feature Differences
    - Database Migration Assistant (DMA) & Azure Database Migration Service (DMS)
2. **Enterprise Capstone & DBA Checklist**
    - Enterprise Database Performance Audit Report Generation
    - Comprehensive SQL Server Production Health Checklist
