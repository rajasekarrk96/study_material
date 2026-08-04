# SQL Server Enterprise Database Architecture — Master Syllabus

**Target Role:** SQL Server DBA / Database Engineer / Enterprise Backend Developer  
**Difficulty Level:** Intermediate  
**Estimated Duration:** 120 Hours  
**Prerequisites:** database-technologies  
**Required Courses:** mysql  
**Optional Courses:** dotnet-full-stack  

---

## Study Flow

### 1. SQL Server Administration & T-SQL

#### 1.1. Module 01 — Relational Querying Foundations & T-SQL Data Types
1. **Relational Database Engine & SQL Server Instance Architecture**
    - SQL Server Architecture: Database Engine, Relational Engine, Storage Engine
    - System Databases: `master`, `model`, `msdb`, `tempdb`, `resource`
    - Connecting via SQL Server Management Studio (SSMS) & Azure Data Studio
    - T-SQL Language Elements & Command Categories (DDL, DML, DCL, TCL)
2. **T-SQL Data Types Deep Dive**
    - Exact Numerics (`INT`, `BIGINT`, `DECIMAL(p,s)`, `MONEY`)
    - String Types & Collations (`VARCHAR` vs `NVARCHAR`, `VARCHAR(MAX)`, Collations)
    - Date and Time Types (`DATE`, `TIME`, `DATETIME2`, `DATETIMEOFFSET`)
    - Binary & Unique Identifiers (`VARBINARY`, `UNIQUEIDENTIFIER`, `NEWID()`, `NEWSEQUENTIALID()`)

#### 1.2. Module 02 — Advanced Relational Joins & Subqueries
1. **Relational Joins Deep Dive**
    - Inner Joins, Left Outer Joins, Right Outer Joins, Full Outer Joins
    - Cross Joins, Self-Joins, Non-EQUI Joins
    - Join Algorithm Mechanics: Nested Loop Join, Hash Match Join, Merge Join
2. **Subqueries & Set Operators**
    - Scalar Subqueries, Correlated Subqueries, Multi-Value Subqueries
    - `EXISTS` vs `IN` Performance Comparison & Execution Plan Differences
    - Set Operators: `UNION`, `UNION ALL`, `INTERSECT`, `EXCEPT`

#### 1.3. Module 03 — Aggregations, Grouping & Window Functions
1. **Data Aggregation & Grouping**
    - Aggregate Functions (`SUM`, `AVG`, `COUNT`, `MIN`, `MAX`, `STRING_AGG`)
    - `GROUP BY` Clause & Filtered Aggregations with `HAVING`
    - Multidimensional Grouping: `GROUPING SETS`, `CUBE`, and `ROLLUP`
2. **Analytical Window Functions**
    - `OVER()` Clause & Framing Specs (`ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`)
    - Ranking Functions: `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `NTILE()`
    - Value Functions: `LAG()`, `LEAD()`, `FIRST_VALUE()`, `LAST_VALUE()`
    - Aggregate Window Functions: Running Totals & Moving Averages

#### 1.4. Module 04 — Advanced T-SQL Programming (CTEs, Views & Functions)
1. **Common Table Expressions & Views**
    - Standard CTEs vs Derived Tables vs Temporary Tables (`#Temp`, `##GlobalTemp`)
    - Recursive CTEs for Hierarchical Tree Traversal
    - Views Creation, Indexed Views (Schema-bound Views), Updatable Views
2. **User-Defined Functions (UDF)**
    - Scalar Functions (Performance Overhead & Inline Scalar UDF Inlining in SQL 2019+)
    - Inline Table-Valued Functions (iTVF) Best Practices
    - Multi-Statement Table-Valued Functions (mTVF) & TempDB Spills

#### 1.5. Module 05 — Stored Procedures, Triggers & Error Handling
1. **Stored Procedures Architecture**
    - Stored Procedures Creation, Input Parameters, Output Parameters, Return Codes
    - Dynamic SQL Execution (`sp_executesql`) & Parameter Sniffing Mitigation
    - Execution Plan Caching & Recompilation (`WITH RECOMPILE`, `OPTIMIZE FOR`)
2. **DML Triggers & Error Handling**
    - `AFTER` Triggers vs `INSTEAD OF` Triggers on Tables & Views
    - Virtual Pseudo-Tables: `INSERTED` and `DELETED`
    - Structured Error Handling: `BEGIN TRY ... END CATCH`, `THROW` vs `RAISERROR`
    - Transaction State Validation with `XACT_STATE()`

#### 1.6. Module 06 — SQL Server Storage Architecture & Page Management
1. **Physical Storage Architecture**
    - Database Files: Master Data File (`.mdf`), Secondary Data File (`.ndf`), Transaction Log (`.ldf`)
    - Filegroups: `PRIMARY` Filegroup, Custom User Filegroups, Read-Only Filegroups
    - Storage Structure: Data Pages (8KB), Page Header, Slot Array, Extents (64KB Uniform vs Mixed)
2. **Allocation Map Pages & Space Management**
    - Global Allocation Map (GAM) & Shared Global Allocation Map (SGAM) Pages
    - Page Free Space (PFS), Differential Changed Map (DCM), Bulk Changed Map (BCM) Pages
    - TempDB Allocation Page Latch Contention (`PFS`/`GAM` Bottlenecks) & Multi-File Fixes

#### 1.7. Module 07 — Indexing Engine Architecture & B-Tree Mechanics
1. **B-Tree Indexing Fundamentals**
    - Clustered Index Architecture: Leaf Level = Actual Table Data Pages
    - Non-Clustered Index Architecture: Leaf Level = Index Keys + Clustering Key / RID Pointer
    - Heap Tables (Tables without Clustered Index) & Forwarded Record Performance Impact
2. **Advanced Index Design Strategies**
    - Composite Indexes & Key Column Ordering Rules
    - Included Columns (`INCLUDE`) for Covering Index Creation & Key Lookup Avoidance
    - Filtered Indexes for Sparse Columns & Partial Data Indexing
    - Columnstore Indexes (Clustered vs Non-Clustered) for Data Warehouse Analytical Workloads

#### 1.8. Module 08 — Index Maintenance, Fragmentation & Partitions
1. **Index Fragmentation Diagnostics**
    - Internal Fragmentation (Page Splits) vs External Fragmentation (Logical Order)
    - Querying `sys.dm_db_index_physical_stats` for Fragmentation Percentage
    - Index Maintenance Strategies: `ALTER INDEX REORGANIZE` vs `ALTER INDEX REBUILD`
2. **Table & Index Partitioning**
    - Partition Functions & Partition Schemes Construction
    - Partitioned Tables Creation, Partition Switching for Fast Data Archiving
    - Aligned vs Non-Aligned Partitioned Indexes

#### 1.9. Module 09 — Query Optimizer Mechanics & Execution Plans
1. **Cost-Based Query Optimizer (CBO)**
    - Query Parsing, Algebrization, Optimization Phases (Simplified, Project, Full)
    - Cardinality Estimator (Legacy vs New CE) & Statistics Engine
    - Statistics Architecture: Histograms, Step Density, Density Vector, Auto-Update Stats
2. **Graphical Execution Plan Analysis**
    - Estimated vs Actual Execution Plans Analysis in SSMS
    - Identifying Operators: Table Scan, Index Scan, Index Seek, Key Lookup
    - Join Operators Analysis: Nested Loops, Hash Match, Merge Join
    - Warnings Analysis: Implicit Conversions, Sort Spills, TempDB Spills

#### 1.10. Module 10 — Query Store, Extended Events & DMVs
1. **Query Store Diagnostics**
    - Enabling & Configuring Query Store for Regressed Query Detection
    - Query Store Views: Top Resource Consuming Queries, Forced Execution Plans
    - Query Store Hints in SQL Server 2022
2. **Extended Events (Xe) & DMVs**
    - Extended Events Sessions Creation vs Legacy SQL Profiler
    - DMVs Diagnostics: `sys.dm_exec_query_stats`, `sys.dm_exec_requests`, `sys.dm_exec_sessions`
    - Identifying Blocking Queries & Long-Running Transactions

#### 1.11. Module 11 — Transactions, Concurrency & Locking Engine
1. **Locking Architecture & Lock Modes**
    - Granular Lock Hierarchy: Database, Table, Page, Key (Row), Extent
    - Lock Modes: Shared (S), Exclusive (X), Update (U), Intent (IS/IX/IU), Schema (Sch-S/Sch-M)
    - Transaction Isolation Levels: Read Uncommitted, Read Committed, Repeatable Read, Serializable
2. **Snapshot Isolation & Deadlocks**
    - Read Committed Snapshot Isolation (RCSI) & Snapshot Isolation via TempDB Version Store
    - Deadlock Analysis: XML Deadlock Graph Capture & Deadlock Priority (`SET DEADLOCK_PRIORITY`)
    - Handling Optimistic vs Pessimistic Concurrency

#### 1.12. Module 12 — SQL Server Security, Encryption & Hardening
1. **Authentication & Authorization**
    - Windows Authentication vs SQL Server Authentication Mode
    - Server Logins, Database Users, Database Roles, Application Roles
    - Permission Hierarchy: `GRANT`, `DENY`, `REVOKE` at Server, Schema, and Object Levels
2. **Encryption & Data Masking**
    - Transparent Data Encryption (TDE) for Database Encryption at Rest
    - Always Encrypted Architecture for Sensitive Column Data
    - Dynamic Data Masking (DDM) & Row-Level Security (RLS) Policies

#### 1.13. Module 13 — High Availability (HA) & AlwaysOn Availability Groups
1. **AlwaysOn Availability Groups (AG)**
    - AlwaysOn AG Architecture: WSFC Cluster, Availability Replicas, Availability Databases
    - Synchronous-Commit vs Asynchronous-Commit Modes
    - Automatic Failover, Manual Failover, Read-Only Routing Configuration
2. **Failover Cluster Instances (FCI) & Log Shipping**
    - SQL Server FCI with Shared Storage Architecture
    - Log Shipping Architecture: Primary, Secondary, Monitor Server Roles
    - Database Mirroring Mechanics & Legacy HADR Technologies Comparison

#### 1.14. Module 14 — Backup Strategies & Disaster Recovery (DR)
1. **Recovery Models & Backup Types**
    - Database Recovery Models: Simple, Full, Bulk-Logged
    - Backup Types: Full Backups, Differential Backups, Transaction Log Backups
    - Virtual Log Files (VLF) Count & Impact on Transaction Log Backup Performance
2. **Disaster Recovery Restore Sequences**
    - Point-in-Time Database Restore Sequence
    - Tail-Log Backup Execution & Emergency Recovery (`STOPAT` Clause)
    - Automated Backup Verification (`RESTORE VERIFYONLY`) & DBCC CHECKDB Integrity Checks

#### 1.15. Module 15 — Automation, Agent Jobs & SSIS ETL
1. **SQL Server Agent Automation**
    - SQL Server Agent Architecture: Jobs, Steps, Schedules, Alerts, Operators
    - Setting up Mail Alerts (Database Mail) for Job Failures & Critical Events
    - Automated Maintenance Plans for Index Optimization and Statistics Updating
2. **Bulk Data Loading & SSIS ETL Integration**
    - High-Performance Bulk Import: `BULK INSERT`, `bcp` Command Line Utility
    - SQL Server Integration Services (SSIS): Control Flow Tasks, Data Flow Pipelines

#### 1.16. Module 16 — Azure SQL Migration & Enterprise Capstone
1. **Azure SQL Database & Managed Instance**
    - Azure SQL Database Deployment Models: Single Database, Elastic Pool, Managed Instance
    - Purchasing Models: vCore Model vs DTU Model
    - Database Migration Assistant (DMA) & Azure Database Migration Service (DMS)
2. **Enterprise Capstone & Production Audit**
    - Generating an Enterprise SQL Server Database Performance & Security Audit Report
    - Complete Production Database Administrator (DBA) Operations Checklist
