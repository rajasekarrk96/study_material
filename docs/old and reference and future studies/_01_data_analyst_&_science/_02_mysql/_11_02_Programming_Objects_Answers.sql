-- ==========================================================
-- TITLE: MYSQL PROGRAMMING OBJECTS ANSWERS
-- ==========================================================

DROP DATABASE IF EXISTS mysql_11_programming_objects_answers;
CREATE DATABASE mysql_11_programming_objects_answers;
USE mysql_11_programming_objects_answers;

CREATE TABLE q_marks (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    mark INT
);

INSERT INTO q_marks VALUES
(1, 'Asha', 78),
(2, 'Balan', 64),
(3, 'Meera', 91);

-- Q1
SET @student_count = 3;
SELECT @student_count;

-- Q2
DELIMITER $$
CREATE FUNCTION fn_add_two_numbers(a INT, b INT)
RETURNS INT
DETERMINISTIC
BEGIN
    RETURN a + b;
END $$
DELIMITER ;

-- Q3
SELECT fn_add_two_numbers(10, 20) AS total_value;

-- Q4
DELIMITER $$
CREATE FUNCTION fn_mark_label(mark_value INT)
RETURNS VARCHAR(10)
DETERMINISTIC
BEGIN
    RETURN IF(mark_value >= 50, 'PASS', 'FAIL');
END $$
DELIMITER ;

-- Q5
SELECT fn_mark_label(40) AS result_value;

-- Q6
DELIMITER $$
CREATE PROCEDURE pr_show_marks()
BEGIN
    SELECT * FROM q_marks;
END $$
DELIMITER ;

-- Q7
CALL pr_show_marks();

-- Q8
DELIMITER $$
CREATE PROCEDURE pr_get_top_mark(OUT highest_mark INT)
BEGIN
    SELECT MAX(mark) INTO highest_mark
    FROM q_marks;
END $$
DELIMITER ;

-- Q9
CALL pr_get_top_mark(@top_mark);
SELECT @top_mark;

-- Q10
DELIMITER $$
CREATE PROCEDURE pr_limit_rows(IN row_count INT)
BEGIN
    SELECT * FROM q_marks LIMIT row_count;
END $$
DELIMITER ;

-- Q11
CALL pr_limit_rows(2);

-- Q12
-- Function returns one value and can be used in expressions.
-- Procedure is called with CALL and can return result sets or perform actions.

-- Q13
/*
WHILE counter_value <= 5 DO
    SET counter_value = counter_value + 1;
END WHILE;
*/

-- Q14
-- IN passes a value into a procedure.
-- OUT passes a value back from a procedure.

-- Q15
DROP FUNCTION IF EXISTS fn_add_two_numbers;
