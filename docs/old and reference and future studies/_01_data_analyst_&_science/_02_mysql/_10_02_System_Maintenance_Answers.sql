-- ==========================================================
-- TITLE: MYSQL SYSTEM MAINTENANCE ANSWERS
-- ==========================================================

DROP DATABASE IF EXISTS mysql_10_system_maintenance_answers;
CREATE DATABASE mysql_10_system_maintenance_answers;
USE mysql_10_system_maintenance_answers;

CREATE TABLE q_memberships (
    id INT PRIMARY KEY,
    member_name VARCHAR(100)
);

INSERT INTO q_memberships VALUES
(1, 'Asha'),
(2, 'Balan');

-- Q1
SELECT CONNECTION_ID();
-- Q2
SHOW PROCESSLIST;
-- Q3
SHOW VARIABLES;
-- Q4
CREATE TEMPORARY TABLE q_temp_data (
    id INT,
    value_text VARCHAR(100)
);
-- Q5
INSERT INTO q_temp_data VALUES (1, 'sample');
-- Q6
SELECT * FROM q_temp_data;
-- Q7
DROP TEMPORARY TABLE IF EXISTS q_temp_data;
-- Q8
CREATE TABLE q_memberships_copy LIKE q_memberships;
-- Q9
CREATE TABLE q_memberships_data_copy AS
SELECT * FROM q_memberships;
-- Q10
-- LIKE mainly copies structure.
-- AS SELECT copies query result data but may not preserve all indexes and constraints.
-- Q11
SHOW STATUS;
-- Q12
REPAIR TABLE q_memberships;
-- Q13
LOCK TABLES q_memberships READ;
-- Q14
UNLOCK TABLES;
-- Q15
-- A temporary table exists only for the current session and is removed when the session ends.
