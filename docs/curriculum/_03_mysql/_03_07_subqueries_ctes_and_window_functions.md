# Subqueries CTEs and Window Functions

> **Course**: MySQL | **Module**: Advanced SQL | **Difficulty**: intermediate

---

### 1. Subqueries
```sql
-- Scalar subquery
SELECT name, price,
    (SELECT AVG(price) FROM products) AS avg_price
FROM products;

-- IN subquery
SELECT * FROM customers
WHERE id IN (SELECT customer_id FROM orders WHERE total > 1000);

-- Correlated subquery (runs once per outer row)
SELECT name, salary FROM employees e1
WHERE salary > (SELECT AVG(salary) FROM employees e2 WHERE e2.dept_id = e1.dept_id);

-- EXISTS
SELECT * FROM products p
WHERE EXISTS (SELECT 1 FROM order_items oi WHERE oi.product_id = p.id);
```

### 2. Common Table Expressions (CTEs)
```sql
WITH monthly_sales AS (
    SELECT MONTH(order_date) AS month, SUM(total) AS revenue
    FROM orders WHERE YEAR(order_date) = 2024
    GROUP BY month
),
ranked AS (
    SELECT *, RANK() OVER (ORDER BY revenue DESC) AS rnk
    FROM monthly_sales
)
SELECT * FROM ranked WHERE rnk <= 3;
```

### 3. Recursive CTE — Org Chart
```sql
WITH RECURSIVE org AS (
    SELECT id, name, manager_id, 0 AS depth
    FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.name, e.manager_id, o.depth + 1
    FROM employees e JOIN org o ON e.manager_id = o.id
)
SELECT * FROM org ORDER BY depth, name;
```

### 4. Window Functions
```sql
SELECT name, dept_id, salary,
    ROW_NUMBER()   OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rn,
    RANK()         OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk,
    DENSE_RANK()   OVER (PARTITION BY dept_id ORDER BY salary DESC) AS drnk,
    LAG(salary, 1) OVER (PARTITION BY dept_id ORDER BY salary)     AS prev_salary,
    LEAD(salary,1) OVER (PARTITION BY dept_id ORDER BY salary)     AS next_salary,
    SUM(salary)    OVER (PARTITION BY dept_id)                     AS dept_total
FROM employees;
```

---

Find: top 3 products per category (using ROW_NUMBER), month-over-month growth (using LAG), full org hierarchy (recursive CTE), customers who never ordered (EXISTS NOT).

---
