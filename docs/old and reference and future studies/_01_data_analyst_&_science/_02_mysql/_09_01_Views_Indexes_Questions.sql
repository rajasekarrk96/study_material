-- ==========================================================
-- TITLE: MYSQL VIEWS AND INDEXES QUESTIONS
-- ==========================================================

DROP DATABASE IF EXISTS mysql_09_views_indexes_questions;
CREATE DATABASE mysql_09_views_indexes_questions;
USE mysql_09_views_indexes_questions;

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

-- Q1: Create a view that shows product_name and price from q_products.
-- Q2: Select all rows from that view.
-- Q3: Drop the created view.
-- Q4: Create an index on product_name.
-- Q5: Show indexes from q_products.
-- Q6: Drop the index on product_name.
-- Q7: Describe q_products structure.
-- Q8: Show create table statement for q_products.
-- Q9: Explain a query filtering product_name = 'Pen'.
-- Q10: Explain why indexes help SELECT performance in comments.
-- Q11: Show columns from q_products.
-- Q12: Create a view with only Electronics products.
-- Q13: Query the Electronics view ordered by price desc.
-- Q14: Explain difference between view and table in comments.
-- Q15: Mention one case where index may not help much.
