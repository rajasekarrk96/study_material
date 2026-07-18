-- ==========================================================
-- TITLE: MYSQL CTE AND WINDOW FUNCTIONS ANSWERS
-- ==========================================================

DROP DATABASE IF EXISTS mysql_13_modern_sql_answers;
CREATE DATABASE mysql_13_modern_sql_answers;
USE mysql_13_modern_sql_answers;

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

-- Q1
WITH high_scores AS (
    SELECT * FROM q_scores WHERE marks >= 75
)
SELECT * FROM high_scores;

-- Q2
WITH high_scores AS (
    SELECT * FROM q_scores WHERE marks >= 75
)
SELECT * FROM high_scores WHERE class_name = 'B';

-- Q3
SELECT student_name, marks,
ROW_NUMBER() OVER (ORDER BY marks DESC) AS row_num
FROM q_scores;

-- Q4
SELECT student_name, marks,
RANK() OVER (ORDER BY marks DESC) AS rank_num
FROM q_scores;

-- Q5
SELECT student_name, marks,
DENSE_RANK() OVER (ORDER BY marks DESC) AS dense_rank_num
FROM q_scores;

-- Q6
SELECT student_name, class_name, marks,
MAX(marks) OVER (PARTITION BY class_name) AS class_highest
FROM q_scores;

-- Q7
SELECT student_name, class_name, marks,
AVG(marks) OVER (PARTITION BY class_name) AS class_average
FROM q_scores;

-- Q8
SELECT student_id, student_name, marks,
SUM(marks) OVER (ORDER BY student_id) AS running_total
FROM q_scores;

-- Q9
SELECT student_name, class_name, marks,
ROW_NUMBER() OVER (PARTITION BY class_name ORDER BY marks DESC) AS class_row_num
FROM q_scores;

-- Q10
-- RANK leaves gaps after ties.
-- DENSE_RANK does not leave gaps after ties.

-- Q11
WITH RECURSIVE nums AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1 FROM nums WHERE n < 5
)
SELECT * FROM nums;

-- Q12
-- Window functions return values alongside each original row instead of collapsing rows into one summary row.

-- Q13
WITH ranked_scores AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY class_name ORDER BY marks DESC) AS rn
    FROM q_scores
)
SELECT * FROM ranked_scores WHERE rn = 1;

-- Q14
-- OVER defines the window used by a window function, including ordering and partitioning.

-- Q15
-- GROUP BY collapses rows into summary groups.
-- Window functions keep all rows and add analytic values beside them.
