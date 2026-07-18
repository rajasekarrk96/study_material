-- ==========================================================
-- TITLE: MYSQL AGGREGATES AND GROUPING QUESTIONS
-- ==========================================================

DROP DATABASE IF EXISTS mysql_06_aggregates_grouping_questions;
CREATE DATABASE mysql_06_aggregates_grouping_questions;
USE mysql_06_aggregates_grouping_questions;

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

-- Q1: Count total rows in q_sales.
-- Q2: Show total sales amount using SUM.
-- Q3: Show average amount using AVG.
-- Q4: Show minimum amount.
-- Q5: Show maximum amount.
-- Q6: Count distinct regions.
-- Q7: Show total amount per region.
-- Q8: Show total quantity per product_category.
-- Q9: Show average amount per sales_person.
-- Q10: Show number of sales per region.
-- Q11: Show regions where total amount is greater than 2000.
-- Q12: Show product_category where average amount is above 1000.
-- Q13: Show sales_person and total amount ordered by total amount descending.
-- Q14: Show region and count of sales where quantity > 1.
-- Q15: Explain WHERE vs HAVING in one or two comments.
