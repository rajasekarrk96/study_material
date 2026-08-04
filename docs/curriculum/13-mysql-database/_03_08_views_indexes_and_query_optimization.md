# Views Indexes and Query Optimization

> **Course**: MySQL | **Module**: Advanced SQL | **Difficulty**: advanced

---

### 1. Views
```sql
-- Simple view
CREATE OR REPLACE VIEW active_customers AS
SELECT id, name, email, total_orders
FROM customers WHERE is_active = 1;

-- View with JOIN
CREATE VIEW product_inventory AS
SELECT p.id, p.name, p.price, c.name AS category, i.quantity
FROM products p JOIN categories c ON p.category_id = c.id
JOIN inventory i ON i.product_id = p.id;

-- Updatable view (no GROUP BY, DISTINCT, subqueries)
UPDATE active_customers SET email = 'new@mail.com' WHERE id = 5;
```

### 2. Indexes
```sql
-- Single column
CREATE INDEX idx_email ON customers(email);

-- Composite (order matters — most selective first)
CREATE INDEX idx_dept_salary ON employees(dept_id, salary);

-- Covering index (query served entirely from index)
CREATE INDEX idx_cover ON orders(customer_id, status, created_at);

-- Full-text
CREATE FULLTEXT INDEX idx_ft_name ON products(name, description);
SELECT * FROM products WHERE MATCH(name, description) AGAINST ('wireless headphones');

-- Drop index
DROP INDEX idx_email ON customers;
```

### 3. EXPLAIN and Query Analysis
```sql
EXPLAIN SELECT * FROM orders WHERE customer_id = 5 AND status = 'shipped';
-- Look for: type (range > ref > all), key, rows, Extra
EXPLAIN ANALYZE SELECT ...;  -- MySQL 8.0.18+: actual execution stats
```

### 4. Slow Query Log
```sql
SET GLOBAL slow_query_log = ON;
SET GLOBAL long_query_time = 1;  -- log queries > 1 second
SHOW STATUS LIKE 'Slow_queries';
```

---

Add indexes to a 1M-row orders table. Use EXPLAIN ANALYZE to compare before/after query plans. Build a covering index for the most common API query pattern.

---
