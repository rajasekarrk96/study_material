-- ==========================================================
-- TITLE: MYSQL TRIGGERS AND SIGNALS QUESTIONS
-- ==========================================================

DROP DATABASE IF EXISTS mysql_12_triggers_signals_questions;
CREATE DATABASE mysql_12_triggers_signals_questions;
USE mysql_12_triggers_signals_questions;

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

-- Q1: Create a BEFORE INSERT trigger that changes negative working_hours to 0.
-- Q2: Insert a row with negative working_hours.
-- Q3: Select rows from q_employee_hours to verify working_hours became 0.
-- Q4: Create an AFTER INSERT trigger that logs inserted emp_id into q_employee_hours_log.
-- Q5: Insert another employee row to test the log trigger.
-- Q6: Select rows from q_employee_hours_log.
-- Q7: Create a BEFORE UPDATE trigger that blocks working_hours above 24 using SIGNAL.
-- Q8: Write an UPDATE statement that would fail because working_hours is too high.
-- Q9: Show triggers.
-- Q10: Drop the AFTER INSERT trigger.
-- Q11: Explain NEW keyword in comments.
-- Q12: Explain OLD keyword in comments.
-- Q13: Mention when SIGNAL is useful.
-- Q14: Write one AFTER DELETE use case in comments.
-- Q15: Drop the BEFORE UPDATE trigger if it exists.
