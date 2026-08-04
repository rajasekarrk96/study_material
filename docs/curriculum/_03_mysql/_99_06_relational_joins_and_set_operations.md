# Relational Joins and Set Operations

> **Course**: MySQL | **Module**: SQL Fundamentals | **Difficulty**: intermediate

---

### 1. JOIN Types
```sql
-- INNER JOIN — only matching rows
SELECT o.id, c.name FROM orders o
INNER JOIN customers c ON o.customer_id = c.id;

-- LEFT JOIN — all orders, including those without a customer
SELECT o.id, c.name FROM orders o
LEFT JOIN customers c ON o.customer_id = c.id;

-- SELF JOIN — employee manager hierarchy
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;

-- CROSS JOIN — all combinations (use carefully!)
SELECT s.size, c.color FROM sizes s CROSS JOIN colors c;
```

### 2. Multi-Table Join
```sql
SELECT o.id, c.name, p.name AS product, oi.quantity
FROM orders o
JOIN customers c     ON o.customer_id = c.id
JOIN order_items oi  ON oi.order_id = o.id
JOIN products p      ON oi.product_id = p.id
WHERE o.status = 'shipped';
```

### 3. Set Operations
```sql
-- UNION (removes duplicates)
SELECT email FROM customers
UNION
SELECT email FROM newsletter_subscribers;

-- UNION ALL (keeps duplicates — faster)
SELECT product_id FROM sales_2023
UNION ALL
SELECT product_id FROM sales_2024;
```

> **Note**: MySQL does not natively support INTERSECT/EXCEPT before 8.0.31.  
> Use `INNER JOIN` for intersection, `LEFT JOIN ... WHERE IS NULL` for difference.

---

Write queries for: all customers with their orders (including those with no orders), product sales with category rollup, employee org chart via self-join.

---
