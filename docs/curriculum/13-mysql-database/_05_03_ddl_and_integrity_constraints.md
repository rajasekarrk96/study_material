---
id: "05_03"
title: "DDL and Integrity Constraints"
course: "MySQL"
module: 2
module_title: "SQL Fundamentals"
lesson: 3
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["CREATE-TABLE", "ALTER-TABLE", "DROP", "TRUNCATE", "PRIMARY-KEY", "FOREIGN-KEY", "UNIQUE", "CHECK", "DEFAULT", "NOT-NULL", "AUTO-INCREMENT"]
prerequisites: []
lab_required: true
---

## Topics Covered

### 1. CREATE TABLE
```sql
CREATE TABLE employees (
    emp_id      INT AUTO_INCREMENT PRIMARY KEY,
    first_name  VARCHAR(50)     NOT NULL,
    last_name   VARCHAR(50)     NOT NULL,
    email       VARCHAR(100)    NOT NULL UNIQUE,
    salary      DECIMAL(10,2)   DEFAULT 50000.00,
    dept_id     INT,
    hire_date   DATE            DEFAULT (CURRENT_DATE),
    is_active   TINYINT(1)      DEFAULT 1,
    CONSTRAINT fk_dept FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
        ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT chk_salary CHECK (salary > 0)
);
```

### 2. ALTER TABLE
```sql
ALTER TABLE employees
    ADD COLUMN phone VARCHAR(20),
    MODIFY COLUMN first_name VARCHAR(100) NOT NULL,
    DROP COLUMN is_active,
    ADD CONSTRAINT uq_phone UNIQUE (phone);
```

### 3. ON DELETE / ON UPDATE Actions
| Action | Behavior |
|---|---|
| CASCADE | Delete/update child when parent changes |
| SET NULL | Set FK to NULL |
| RESTRICT | Prevent parent delete if children exist |
| NO ACTION | Same as RESTRICT in MySQL |

### 4. Indexes Created Automatically
- PRIMARY KEY → clustered index
- UNIQUE → unique index
- FOREIGN KEY → non-clustered index on FK column

## Lab
Create a complete schema for an e-commerce system with products, categories, customers, orders, and order_items — all constraints enforced.
