---
id: "05_10"
title: "Transactions Concurrency and Locking"
course: "MySQL"
module: 4
module_title: "Programmability"
lesson: 10
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["BEGIN", "COMMIT", "ROLLBACK", "SAVEPOINT", "ACID", "isolation-level", "READ-COMMITTED", "REPEATABLE-READ", "SERIALIZABLE", "deadlock", "row-lock", "gap-lock"]
prerequisites: []
lab_required: true
---

## Topics Covered

### 1. Transactions
```sql
START TRANSACTION;
    UPDATE accounts SET balance = balance - 500 WHERE id = 1;
    UPDATE accounts SET balance = balance + 500 WHERE id = 2;
    -- Check both succeeded
    IF (SELECT balance FROM accounts WHERE id = 1) < 0 THEN
        ROLLBACK;
    ELSE
        COMMIT;
    END IF;

-- SAVEPOINT
START TRANSACTION;
    INSERT INTO orders VALUES (...);
    SAVEPOINT after_order;
    INSERT INTO payments VALUES (...);
    -- If payment fails:
    ROLLBACK TO after_order;
    COMMIT;
```

### 2. ACID Properties
| Property | Meaning |
|---|---|
| **A**tomicity | All or nothing |
| **C**onsistency | DB stays valid |
| **I**solation | Concurrent txns don't interfere |
| **D**urability | Committed data survives crashes |

### 3. Isolation Levels
```sql
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
-- READ UNCOMMITTED → dirty reads
-- READ COMMITTED   → no dirty reads, phantom reads possible
-- REPEATABLE READ  → MySQL default; no dirty/non-repeatable
-- SERIALIZABLE     → strictest; full locking
```

### 4. Lock Types
```sql
-- Shared lock (read)
SELECT * FROM products WHERE id = 5 LOCK IN SHARE MODE;

-- Exclusive lock (write)
SELECT * FROM products WHERE id = 5 FOR UPDATE;

-- Show active locks
SELECT * FROM performance_schema.data_locks;
```

## Lab
Simulate a bank transfer with ACID guarantee, test deadlock scenario (two sessions updating rows in opposite order), verify isolation levels with dirty read experiment.
