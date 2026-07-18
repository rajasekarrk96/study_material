-- ==========================================================
-- TITLE: MYSQL VIEWS AND INDEXES ANSWERS
-- ==========================================================

DROP DATABASE IF EXISTS mysql_09_views_indexes_answers;
CREATE DATABASE mysql_09_views_indexes_answers;
USE mysql_09_views_indexes_answers;

CREATE TABLE q_products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

INSERT INTO q_products VALUES
(101, 'Notebook', 'Stationery', 45.00),
(102, 'Pen', 'Stationery', 12.00),
(103, 'Monitor', 'Electronics', 11500.00),
(104, 'Keyboard', 'Electronics', 1700.00);

-- Q1
CREATE VIEW v_product_price AS
SELECT product_name, price
FROM q_products;
-- Q2
SELECT * FROM v_product_price;
-- Q3
DROP VIEW v_product_price;
-- Q4
CREATE INDEX idx_product_name ON q_products(product_name);
-- Q5
SHOW INDEX FROM q_products;
-- Q6
DROP INDEX idx_product_name ON q_products;
-- Q7
DESCRIBE q_products;
-- Q8
SHOW CREATE TABLE q_products;
-- Q9
EXPLAIN SELECT * FROM q_products WHERE product_name = 'Pen';
-- Q10
-- Indexes help MySQL find matching rows faster instead of scanning every row.
-- Q11
SHOW COLUMNS FROM q_products;
-- Q12
CREATE VIEW v_electronics AS
SELECT *
FROM q_products
WHERE category = 'Electronics';
-- Q13
SELECT * FROM v_electronics ORDER BY price DESC;
-- Q14
-- A table stores actual data.
-- A view stores a query definition and shows result data virtually.
-- Q15
-- Index may not help much on very small tables or leading wildcard searches like LIKE '%pen%'.
