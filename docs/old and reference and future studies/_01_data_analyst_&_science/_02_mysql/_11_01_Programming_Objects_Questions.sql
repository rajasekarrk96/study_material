-- ==========================================================
-- TITLE: MYSQL PROGRAMMING OBJECTS QUESTIONS
-- ==========================================================

DROP DATABASE IF EXISTS mysql_11_programming_objects_questions;
CREATE DATABASE mysql_11_programming_objects_questions;
USE mysql_11_programming_objects_questions;

CREATE TABLE q_marks (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    mark INT
);

INSERT INTO q_marks VALUES
(1, 'Asha', 78),
(2, 'Balan', 64),
(3, 'Meera', 91);

-- Q1: Set a user variable @student_count to 3 and display it.
-- Q2: Create a function fn_add_two_numbers(a,b) returning their sum.
-- Q3: Call fn_add_two_numbers with 10 and 20.
-- Q4: Create a function fn_mark_label(mark_value) returning PASS if >= 50 else FAIL.
-- Q5: Call fn_mark_label for mark 40.
-- Q6: Create a procedure pr_show_marks() that selects all rows from q_marks.
-- Q7: Call pr_show_marks().
-- Q8: Create a procedure pr_get_top_mark(OUT highest_mark INT).
-- Q9: Call pr_get_top_mark using a user variable and display it.
-- Q10: Create a procedure pr_limit_rows(IN row_count INT) that selects limited rows.
-- Q11: Call pr_limit_rows(2).
-- Q12: Explain function vs procedure in comments.
-- Q13: Write a small WHILE loop example inside a comment block.
-- Q14: Explain IN and OUT parameters in comments.
-- Q15: Drop created function fn_add_two_numbers if it exists.
