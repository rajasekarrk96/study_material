-- ==========================================================
-- TITLE: MYSQL SUBQUERIES AND LOGIC ANSWERS
-- ==========================================================

DROP DATABASE IF EXISTS mysql_08_subqueries_logic_answers;
CREATE DATABASE mysql_08_subqueries_logic_answers;
USE mysql_08_subqueries_logic_answers;

CREATE TABLE q_students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    class_name VARCHAR(50),
    marks INT
);

INSERT INTO q_students VALUES
(1, 'Asha', 'A', 78),
(2, 'Balan', 'A', 64),
(3, 'Meera', 'B', 91),
(4, 'Manoj', 'B', 85),
(5, 'Ravi', 'C', 58);

-- Q1
SELECT *
FROM q_students
WHERE marks > (SELECT AVG(marks) FROM q_students);
-- Q2
SELECT *
FROM q_students
WHERE marks = (SELECT MAX(marks) FROM q_students);
-- Q3
SELECT *
FROM q_students
WHERE marks = (
    SELECT MAX(marks)
    FROM q_students
    WHERE marks < (SELECT MAX(marks) FROM q_students)
);
-- Q4
SELECT *
FROM q_students
WHERE class_name IN (
    SELECT class_name
    FROM q_students
    GROUP BY class_name
    HAVING COUNT(*) > 1
);
-- Q5
SELECT DISTINCT class_name
FROM q_students
WHERE class_name IN (
    SELECT class_name
    FROM q_students
    WHERE marks > 80
);
-- Q6
SELECT *
FROM q_students
WHERE EXISTS (
    SELECT 1
    FROM q_students
    WHERE class_name = 'B'
);
-- Q7
SELECT *
FROM q_students
WHERE marks > ANY (
    SELECT marks
    FROM q_students
    WHERE class_name = 'C'
);
-- Q8
SELECT *
FROM q_students
WHERE marks > ALL (
    SELECT marks
    FROM q_students
    WHERE class_name = 'A'
);
-- Q9
SELECT student_name,
CASE
    WHEN marks >= 75 THEN 'PASS_PLUS'
    ELSE 'PASS_OR_LOW'
END AS status_value
FROM q_students;
-- Q10
SELECT student_name, IF(marks >= 90, 'TOP', 'NORMAL') AS mark_flag
FROM q_students;
-- Q11
SELECT *
FROM q_students
WHERE marks = (SELECT MIN(marks) FROM q_students);
-- Q12
SELECT *
FROM q_students
WHERE class_name <> (
    SELECT class_name
    FROM (
        SELECT class_name, AVG(marks) AS avg_marks
        FROM q_students
        GROUP BY class_name
        ORDER BY avg_marks
        LIMIT 1
    ) AS x
);
-- Q13
-- Single-row subquery returns one value.
-- Multi-row subquery returns multiple values and often uses IN, ANY, or ALL.
-- Q14
SELECT s1.*
FROM q_students s1
WHERE EXISTS (
    SELECT 1
    FROM q_students s2
    WHERE s2.class_name = s1.class_name
      AND s2.student_id <> s1.student_id
);
-- Q15
SELECT class_name, AVG(marks) AS avg_marks
FROM q_students
GROUP BY class_name
ORDER BY avg_marks DESC;
