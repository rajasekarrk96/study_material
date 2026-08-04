# Database Architecture and Relational Concepts

> **Course**: MySQL | **Module**: MySQL Foundations | **Difficulty**: beginner

---

A **Relational Database Management System (RDBMS)** organises data into **tables** (relations) with rows (tuples) and columns (attributes), enforcing relationships through keys.

### Key Concepts

| Term | Definition |
|---|---|
| **Table** | 2-D structure with rows and columns |
| **Row** | One record (instance of an entity) |
| **Column** | One attribute with a defined data type |
| **Primary Key** | Uniquely identifies each row |
| **Foreign Key** | References PK in another table (enforces referential integrity) |
| **Schema** | Blueprint of the database structure |
| **Index** | Data structure that speeds up queries |
| **View** | Virtual table defined by a SELECT query |

---

```
Client Layer       → mysql CLI, MySQL Workbench, application drivers
   ↓
Connection/Thread  → Each client gets a thread; connection pool
   ↓
SQL Interface      → Parser → Optimizer → Executor
   ↓
Storage Engine     → InnoDB (default), MyISAM, MEMORY, CSV
   ↓
File System        → Data files (.ibd), redo log, undo log, binary log
```

### Storage Engines Comparison

| Feature | InnoDB | MyISAM |
|---|---|---|
| ACID | Yes | No |
| Transactions | Yes | No |
| Foreign Keys | Yes | No |
| Row-level locking | Yes | Table-level only |
| Full-text search | Yes (5.6+) | Yes |
| Use case | General OLTP | Read-heavy archives |

---

```
A — Atomicity   : All operations in a transaction succeed or ALL are rolled back
C — Consistency : DB moves from one valid state to another
I — Isolation   : Concurrent transactions don't interfere
D — Durability  : Committed data survives crashes (written to disk)
```

---

| Category | Commands | Purpose |
|---|---|---|
| **DDL** — Data Definition | CREATE, ALTER, DROP, TRUNCATE | Structure |
| **DML** — Data Manipulation | INSERT, UPDATE, DELETE | Data |
| **DQL** — Data Query | SELECT | Retrieve |
| **DCL** — Data Control | GRANT, REVOKE | Permissions |
| **TCL** — Transaction Control | BEGIN, COMMIT, ROLLBACK, SAVEPOINT | Transactions |

---

```bash
# CLI
mysql -u root -p
mysql -u root -p mydb

# Inside MySQL shell
SHOW DATABASES;
USE mydb;
SHOW TABLES;
DESCRIBE employees;
SHOW CREATE TABLE employees;
```

---

1. Install MySQL 8.0, create a database `school`, create tables `students` and `courses`
2. Insert 10 rows into each table and verify with `SELECT * FROM ...`
3. Use `DESCRIBE` and `SHOW CREATE TABLE` to inspect your schema

---
