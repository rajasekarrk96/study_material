---
id: "05_04"
title: "DML and Basic Retrieval"
course: "MySQL"
module: 2
module_title: "SQL Fundamentals"
lesson: 4
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["INSERT", "UPDATE", "DELETE", "SELECT", "WHERE", "ORDER-BY", "LIMIT", "OFFSET", "DISTINCT", "aliases", "LIKE", "BETWEEN", "IN", "IS-NULL"]
prerequisites: []
lab_required: true
---

## Topics Covered

### 1. INSERT
```sql
-- Single row
INSERT INTO products (name, price, category_id) VALUES ('Widget', 9.99, 1);

-- Multiple rows
INSERT INTO products (name, price) VALUES
    ('Gadget', 29.99), ('Doohickey', 4.99), ('Thingamajig', 49.99);

-- INSERT from SELECT
INSERT INTO archive_orders SELECT * FROM orders WHERE created_at < '2024-01-01';
```

### 2. UPDATE
```sql
UPDATE products SET price = price * 1.1 WHERE category_id = 2;
UPDATE employees SET salary = 60000, dept_id = 3 WHERE emp_id = 42;
```

### 3. DELETE
```sql
DELETE FROM cart_items WHERE session_expired = 1;
TRUNCATE TABLE temp_log;          -- Fast, non-logged, no WHERE
DELETE FROM orders WHERE id = 5;  -- Logged, triggers fire
```

### 4. SELECT with Filtering
```sql
SELECT p.name, p.price, c.name AS category
FROM products p
JOIN categories c ON p.category_id = c.id
WHERE p.price BETWEEN 10 AND 50
  AND c.name IN ('Electronics', 'Books')
  AND p.name LIKE '%pro%'
  AND p.deleted_at IS NULL
ORDER BY p.price DESC
LIMIT 20 OFFSET 40;
```

## Lab
Write DML statements to: insert 10 products, update prices by category, delete expired records, and build a paginated search query.
