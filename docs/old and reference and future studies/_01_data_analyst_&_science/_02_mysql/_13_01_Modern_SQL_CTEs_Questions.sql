-- ==========================================================
-- TITLE: MYSQL CTE AND WINDOW FUNCTIONS QUESTIONS
-- ==========================================================

DROP DATABASE IF EXISTS mysql_13_modern_sql_questions;
CREATE DATABASE mysql_13_modern_sql_questions;
USE mysql_13_modern_sql_questions;

CREATE TABLE q_scores (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    class_name VARCHAR(50),
    marks INT
);

INSERT INTO q_scores VALUES
(1, 'Asha', 'A', 78),
(2, 'Balan', 'A', 64),
(3, 'Meera', 'B', 91),
(4, 'Manoj', 'B', 85),
(5, 'Ravi', 'C', 58);

-- Q1: Use a CTE to select students with marks >= 75.
-- Q2: From that CTE, select only class B students.
-- Q3: Use ROW_NUMBER over marks descending.
-- Q4: Use RANK over marks descending.
-- Q5: Use DENSE_RANK over marks descending.
-- Q6: Show class-wise highest marks using MAX() OVER (PARTITION BY class_name).
-- Q7: Show class-wise average marks using AVG() OVER (PARTITION BY class_name).
-- Q8: Show a running total of marks ordered by student_id.
-- Q9: Show row number inside each class using PARTITION BY class_name.
-- Q10: Explain difference between RANK and DENSE_RANK in comments.
-- Q11: Write a recursive CTE generating numbers 1 to 5.
-- Q12: Explain why window functions do not collapse rows.
-- Q13: Show top scoring student per class using ranking and outer filter.
-- Q14: Explain what OVER clause does in comments.
-- Q15: Compare GROUP BY and window function in short comments.
