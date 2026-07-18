-- ==========================================================
-- TITLE: MYSQL SYSTEM MAINTENANCE QUESTIONS
-- ==========================================================

DROP DATABASE IF EXISTS mysql_10_system_maintenance_questions;
CREATE DATABASE mysql_10_system_maintenance_questions;
USE mysql_10_system_maintenance_questions;

CREATE TABLE q_memberships (
    id INT PRIMARY KEY,
    member_name VARCHAR(100)
);

INSERT INTO q_memberships VALUES
(1, 'Asha'),
(2, 'Balan');

-- Q1: Show current connection id.
-- Q2: Show processlist.
-- Q3: Show system variables.
-- Q4: Create a temporary table named q_temp_data with id and value_text.
-- Q5: Insert one row into q_temp_data.
-- Q6: Select all rows from q_temp_data.
-- Q7: Drop q_temp_data.
-- Q8: Create q_memberships_copy using LIKE.
-- Q9: Create q_memberships_data_copy using CREATE TABLE AS SELECT.
-- Q10: Explain one difference between LIKE copy and AS SELECT copy in comments.
-- Q11: Show status variables.
-- Q12: Write REPAIR TABLE statement for q_memberships.
-- Q13: Lock q_memberships for READ.
-- Q14: Unlock tables.
-- Q15: Explain what a temporary table is in comments.
