-- ==========================================================
-- TITLE: MYSQL SUBQUERIES AND LOGIC QUESTIONS
-- ==========================================================

DROP DATABASE IF EXISTS mysql_08_subqueries_logic_questions;
CREATE DATABASE mysql_08_subqueries_logic_questions;
USE mysql_08_subqueries_logic_questions;

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

-- Q1: Show students whose marks are greater than the average marks.
-- Q2: Show student with the highest marks.
-- Q3: Show student(s) with the second highest marks using subquery logic.
-- Q4: Show students whose class_name appears more than once.
-- Q5: Show classes that have at least one student with marks > 80 using IN.
-- Q6: Show students where a student exists in class B using EXISTS.
-- Q7: Show students whose marks are greater than any mark in class C.
-- Q8: Show students whose marks are greater than all marks in class A.
-- Q9: Use CASE to label marks >= 75 as 'PASS_PLUS', else 'PASS_OR_LOW'.
-- Q10: Use IF to label marks >= 90 as 'TOP', else 'NORMAL'.
-- Q11: Show students whose marks equal the minimum marks.
-- Q12: Show students not in the class with lowest average marks.
-- Q13: Explain single-row vs multi-row subquery in comments.
-- Q14: Show only students where another student exists in same class.
-- Q15: Show class_name and class average ordered descending.
