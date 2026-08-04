# Database Technologies — Syllabus

## Study Flow

### 1. MySQL

#### 1.1. Module 1 — MySQL Foundations

1. **Database Architecture and Relational Concepts**
    1. What is a Relational Database?
        - Key Concepts
    2. MySQL Architecture
        - Storage Engines Comparison
    3. ACID Properties
    4. SQL Categories
    5. Connecting to MySQL
    6. Lab Exercise
2. **Database Design ER Modeling and Normalization**
    1. Topics Covered
        - Entity-Relationship Modeling
        - ER to Schema Mapping
        - Normal Forms
        - Normalization Example
    2. Lab

#### 1.2. Module 2 — SQL Fundamentals

1. **DDL and Integrity Constraints**
    1. Topics Covered
        - CREATE TABLE
        - ALTER TABLE
        - ON DELETE / ON UPDATE Actions
        - Indexes Created Automatically
    2. Lab
2. **DML and Basic Retrieval**
    1. Topics Covered
        - INSERT
        - UPDATE
        - DELETE
        - SELECT with Filtering
    2. Lab
3. **Aggregation Grouping and Functions**
    1. Topics Covered
        - Aggregate Functions
        - WITH ROLLUP
        - String Functions
        - Date Functions
        - CASE Expression
    2. Lab
4. **Relational Joins and Set Operations**
    1. Topics Covered
        - JOIN Types
        - Multi-Table Join
        - Set Operations
    2. Lab

#### 1.3. Module 3 — Modern Analytical SQL & Window Functions

1. **Lesson 3.1 MySQL 8.4 Analytical Window Functions**
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `GROUP BY` vs Window Functions (`OVER`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `RANK()` and `DENSE_RANK()` in SQL?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Existing SQL Reference Files

#### 1.4. Module 4 — Advanced SQL

1. **Subqueries CTEs and Window Functions**
    1. Topics Covered
        - Subqueries
        - Common Table Expressions (CTEs)
        - Recursive CTE — Org Chart
        - Window Functions
    2. Lab

#### 1.5. Module 5 — Programmability

1. **Stored Procedures Functions Triggers and Events**
    1. Topics Covered
        - Stored Procedures
        - User-Defined Functions
        - Triggers
        - Events (Scheduled Jobs)
    2. Lab
2. **Transactions Concurrency and Locking**
    1. Topics Covered
        - Transactions
        - ACID Properties
        - Isolation Levels
        - Lock Types
    2. Lab

#### 1.6. Module 6 — Administration

1. **Database Security Administration and Replication**
    1. Topics Covered
        - User Management
        - MySQL Roles (8.0+)
        - Backup and Restore
        - Replication Overview
    2. Lab
2. **MySQL Integration with Python**
    1. Topics Covered
        - mysql-connector-python
        - Connection Pooling
        - SQLAlchemy ORM (MySQL)
        - Async MySQL (aiomysql)
    2. Lab

### 2. SQL Server

#### 2.1. Module 1 — Setup and TSQL Fundamentals

1. **SQL Server Setup and SSMS**
    1. Overview of SQL Server Setup and SSMS
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
2. **DDL Fundamentals: CREATE, ALTER, DROP**
    1. Overview of DDL Fundamentals: CREATE, ALTER, DROP
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
3. **DML: INSERT, UPDATE, DELETE, MERGE**
    1. Overview of DML: INSERT, UPDATE, DELETE, MERGE
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
4. **SQL Server Data Types and NULL Handling**
    1. Overview of SQL Server Data Types and NULL Handling
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
5. **Built-in System Functions (Date, String, Math)**
    1. Overview of Built-in System Functions (Date, String, Math)
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise

#### 2.2. Module 2 — Retrieval and Filtering

1. **SELECT and Filtering with WHERE**
    1. Overview of SELECT and Filtering with WHERE
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
2. **Sorting and Paging (OFFSET-FETCH)**
    1. Overview of Sorting and Paging (OFFSET-FETCH)
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
3. **JOINS: INNER, LEFT, RIGHT, FULL, CROSS**
    1. Overview of JOINS: INNER, LEFT, RIGHT, FULL, CROSS
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
4. **Subqueries: Correlated and Uncorrelated**
    1. Overview of Subqueries: Correlated and Uncorrelated
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
5. **Common Table Expressions (CTEs)**
    1. Overview of Common Table Expressions (CTEs)
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
6. **Set Operators: UNION, UNION ALL, INTERSECT, EXCEPT**
    1. Overview of Set Operators: UNION, UNION ALL, INTERSECT, EXCEPT
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise

#### 2.3. Module 3 — Aggregations and Window Functions

1. **GROUP BY and HAVING Clause**
    1. Overview of GROUP BY and HAVING Clause
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
2. **Window Functions: ROW_NUMBER, RANK, DENSE_RANK**
    1. Overview of Window Functions: ROW_NUMBER, RANK, DENSE_RANK
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
3. **Analytic Functions: LEAD, LAG, FIRST_VALUE**
    1. Overview of Analytic Functions: LEAD, LAG, FIRST_VALUE
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
4. **GROUPING SETS, ROLLUP, and CUBE**
    1. Overview of GROUPING SETS, ROLLUP, and CUBE
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
5. **PIVOT and UNPIVOT Operators**
    1. Overview of PIVOT and UNPIVOT Operators
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise

#### 2.4. Module 4 — Indexes and Optimization

1. **Execution Plans and Query Tuning**
    1. Overview of Execution Plans and Query Tuning
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise

#### 2.5. Module 5 — Programmability and Transactions

1. **Stored Procedures and Parameters**
    1. Overview of Stored Procedures and Parameters
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
2. **User-Defined Functions (Scalar and Table-Valued)**
    1. Overview of User-Defined Functions (Scalar and Table-Valued)
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
3. **Triggers: AFTER and INSTEAD OF**
    1. Overview of Triggers: AFTER and INSTEAD OF
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
4. **Transactions and Isolation Levels**
    1. Overview of Transactions and Isolation Levels
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
5. **Error Handling with TRY...CATCH**
    1. Overview of Error Handling with TRY...CATCH
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
6. **Dynamic SQL and sp_executesql**
    1. Overview of Dynamic SQL and sp_executesql
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
7. **Cursors vs Set-Based Operations**
    1. Overview of Cursors vs Set-Based Operations
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise

#### 2.6. Module 6 — Administration and Security

1. **Backup and Restore Strategies**
    1. Overview of Backup and Restore Strategies
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
2. **Logins, Users, Roles, and Permissions**
    1. Overview of Logins, Users, Roles, and Permissions
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
3. **SQL Server Agent and Job Scheduling**
    1. Overview of SQL Server Agent and Job Scheduling
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
4. **TempDB Management and Concurrency**
    1. Overview of TempDB Management and Concurrency
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
5. **Always On Availability Groups Overview**
    1. Overview of Always On Availability Groups Overview
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
6. **Auditing and Compliance Features**
    1. Overview of Auditing and Compliance Features
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise

#### 2.7. Module 7 — Enterprise Architecture

1. **Capstone Enterprise Database Architecture**
    1. Overview of Capstone Enterprise Database Architecture
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
2. **Introduction to SSIS (SQL Server Integration Services)**
    1. Overview of Introduction to SSIS (SQL Server Integration Services)
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
3. **Introduction to SSRS (SQL Server Reporting Services)**
    1. Overview of Introduction to SSRS (SQL Server Reporting Services)
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise

### 3. MongoDB

#### 3.1. Module 1 — Core Concepts and CRUD

1. **MongoDB Setup and Core Concepts**
    1. What is MongoDB?
        - Key Terminology Comparison
    2. Lab Exercise
2. **Basic CRUD Operations**
    1. Fundamentals of CRUD in MongoDB
    2. Lab Exercise
3. **Querying and Filtering**
    1. Comparison Query Operators
    2. Lab Exercise

#### 3.2. Module 2 — Advanced Querying

1. **Logical and Array Operators**
    1. Logical and Array Searching
    2. Lab Exercise
2. **Update Operators**
    1. Modifying Documents with Update Operators
    2. Lab Exercise
3. **Projections and Pagination**
    1. Controlling Returned Fields & Pagination
    2. Lab Exercise

#### 3.3. Module 3 — Aggregation Framework

1. **Aggregation Pipeline Basics**
    1. Introduction to Aggregation
    2. Lab Exercise
2. **Advanced Aggregation Stages**
    1. Joins and Deconstruction
    2. Lab Exercise

#### 3.4. Module 4 — Data Modeling and Administration

1. **Schema Design Patterns**
    1. Embedding vs Referencing
    2. Lab Exercise
2. **Transactions and ACID**
    1. Multi-Document ACID Transactions
    2. Lab Exercise
3. **Replica Sets and Sharding**
    1. High Availability & Horizontal Scaling
    2. Lab Exercise
4. **PyMongo Integration**
    1. Interfacing MongoDB with Python (PyMongo)
    2. Lab Exercise

### 4. Firebase

#### 4.1. Module 1 — Firebase Introduction

1. **What Is Firebase**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Firebase What Is Firebase Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
2. **Firebase Console Setup**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - ESP32 Firebase Client Configuration Struct
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
3. **Firebase Authentication**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - ESP32 Firebase Anonymous Authentication
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
4. **Firebase SDK in Python**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Streaming Real-Time Updates in Python
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
5. **Firebase SDK in JavaScript**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Real-Time Web Dashboard Gauge Listener
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References

#### 4.2. Module 2 — Firebase Database

1. **Realtime Database**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Firebase Realtime Database Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
2. **Firestore**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Firebase Firestore Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
3. **Realtime Database vs Firestore**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Firebase Realtime Database vs Firestore Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
4. **Security Rules**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Firebase Security Rules Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
5. **IoT Data to Firebase**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Firebase IoT Data to Firebase Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References

#### 4.3. Module 3 — Firebase Hosting and Functions

1. **Firebase Hosting**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Firebase Firebase Hosting Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
2. **Cloud Functions**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Firebase Cloud Functions Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
3. **Firebase Storage**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Firebase Firebase Storage Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
4. **Firebase Notifications**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Firebase Firebase Notifications Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
5. **Full IoT Dashboard with Firebase**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Firebase Full IoT Dashboard with Firebase Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
