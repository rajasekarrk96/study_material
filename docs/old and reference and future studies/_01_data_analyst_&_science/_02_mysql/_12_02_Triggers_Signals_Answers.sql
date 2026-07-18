-- ==========================================================
-- TITLE: MYSQL TRIGGERS AND SIGNALS ANSWERS
-- ==========================================================

DROP DATABASE IF EXISTS mysql_12_triggers_signals_answers;
CREATE DATABASE mysql_12_triggers_signals_answers;
USE mysql_12_triggers_signals_answers;

CREATE TABLE q_employee_hours (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    working_hours INT
);

CREATE TABLE q_employee_hours_log (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT,
    action_text VARCHAR(200)
);

-- Q1
DELIMITER $$
CREATE TRIGGER tr_before_insert_hours
BEFORE INSERT ON q_employee_hours
FOR EACH ROW
BEGIN
    IF NEW.working_hours < 0 THEN
        SET NEW.working_hours = 0;
    END IF;
END $$
DELIMITER ;

-- Q2
INSERT INTO q_employee_hours VALUES (1, 'Asha', -5);

-- Q3
SELECT * FROM q_employee_hours;

-- Q4
DELIMITER $$
CREATE TRIGGER tr_after_insert_hours
AFTER INSERT ON q_employee_hours
FOR EACH ROW
BEGIN
    INSERT INTO q_employee_hours_log(emp_id, action_text)
    VALUES (NEW.emp_id, CONCAT('Inserted employee ', NEW.emp_name));
END $$
DELIMITER ;

-- Q5
INSERT INTO q_employee_hours VALUES (2, 'Balan', 8);

-- Q6
SELECT * FROM q_employee_hours_log;

-- Q7
DELIMITER $$
CREATE TRIGGER tr_before_update_hours
BEFORE UPDATE ON q_employee_hours
FOR EACH ROW
BEGIN
    IF NEW.working_hours > 24 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Working hours cannot exceed 24';
    END IF;
END $$
DELIMITER ;

-- Q8
UPDATE q_employee_hours
SET working_hours = 30
WHERE emp_id = 2;

-- Q9
SHOW TRIGGERS;

-- Q10
DROP TRIGGER tr_after_insert_hours;

-- Q11
-- NEW refers to incoming new row values in INSERT or updated values in UPDATE.

-- Q12
-- OLD refers to existing row values before UPDATE or before DELETE.

-- Q13
-- SIGNAL is useful when a business rule must stop invalid data changes.

-- Q14
-- AFTER DELETE can be used to write deleted row details into an archive log table.

-- Q15
DROP TRIGGER IF EXISTS tr_before_update_hours;
