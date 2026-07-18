-- ==========================================================
-- TITLE: MYSQL AGGREGATES AND GROUPING ANSWERS
-- ==========================================================

DROP DATABASE IF EXISTS mysql_06_aggregates_grouping_answers;
CREATE DATABASE mysql_06_aggregates_grouping_answers;
USE mysql_06_aggregates_grouping_answers;

CREATE TABLE q_sales (
    sale_id INT PRIMARY KEY,
    sales_person VARCHAR(100),
    region VARCHAR(50),
    product_category VARCHAR(50),
    amount DECIMAL(10,2),
    quantity INT
);

INSERT INTO q_sales VALUES
(1, 'Asha', 'North', 'Electronics', 1200.00, 2),
(2, 'Balan', 'South', 'Stationery', 300.00, 10),
(3, 'Meera', 'North', 'Electronics', 1800.00, 3),
(4, 'Manoj', 'East', 'Furniture', 2200.00, 1),
(5, 'Ravi', 'South', 'Electronics', 950.00, 1),
(6, 'Asha', 'North', 'Furniture', 1600.00, 2),
(7, 'Meera', 'West', 'Stationery', 450.00, 15),
(8, 'Balan', 'South', 'Furniture', 1300.00, 1);

-- Q1
SELECT COUNT(*) AS total_rows FROM q_sales;
-- Q2
SELECT SUM(amount) AS total_amount FROM q_sales;
-- Q3
SELECT AVG(amount) AS avg_amount FROM q_sales;
-- Q4
SELECT MIN(amount) AS min_amount FROM q_sales;
-- Q5
SELECT MAX(amount) AS max_amount FROM q_sales;
-- Q6
SELECT COUNT(DISTINCT region) AS total_regions FROM q_sales;
-- Q7
SELECT region, SUM(amount) AS total_amount
FROM q_sales
GROUP BY region;
-- Q8
SELECT product_category, SUM(quantity) AS total_quantity
FROM q_sales
GROUP BY product_category;
-- Q9
SELECT sales_person, AVG(amount) AS avg_amount
FROM q_sales
GROUP BY sales_person;
-- Q10
SELECT region, COUNT(*) AS total_sales
FROM q_sales
GROUP BY region;
-- Q11
SELECT region, SUM(amount) AS total_amount
FROM q_sales
GROUP BY region
HAVING SUM(amount) > 2000;
-- Q12
SELECT product_category, AVG(amount) AS avg_amount
FROM q_sales
GROUP BY product_category
HAVING AVG(amount) > 1000;
-- Q13
SELECT sales_person, SUM(amount) AS total_amount
FROM q_sales
GROUP BY sales_person
ORDER BY total_amount DESC;
-- Q14
SELECT region, COUNT(*) AS total_sales
FROM q_sales
WHERE quantity > 1
GROUP BY region;
-- Q15
-- WHERE filters rows before grouping.
-- HAVING filters grouped results after GROUP BY.
