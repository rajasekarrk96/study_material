-- ==========================================================
-- TITLE: MYSQL JOINS QUESTIONS
-- ==========================================================

DROP DATABASE IF EXISTS mysql_07_joins_questions;
CREATE DATABASE mysql_07_joins_questions;
USE mysql_07_joins_questions;

CREATE TABLE q_departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100)
);

CREATE TABLE q_employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    dept_id INT,
    manager_id INT NULL
);

INSERT INTO q_departments VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Finance'),
(4, 'Sales');

INSERT INTO q_employees VALUES
(101, 'Asha', 1, NULL),
(102, 'Balan', 2, 101),
(103, 'Meera', 3, 101),
(104, 'Manoj', 2, 102),
(105, 'Ravi', NULL, 103);

-- Q1: Show employee names with department names using INNER JOIN.
-- Q2: Show all employees with department names using LEFT JOIN.
-- Q3: Show all departments with employee names using RIGHT JOIN logic or reversed LEFT JOIN.
-- Q4: Show employees who do not have a department assigned.
-- Q5: Show employees whose department is IT.
-- Q6: Show employee name and manager name using SELF JOIN.
-- Q7: Show all combinations of employees and departments using CROSS JOIN.
-- Q8: Count employees per department using JOIN and GROUP BY.
-- Q9: Show departments with no employees.
-- Q10: Show employee name, department name ordered by department.
-- Q11: Show only matching employee-department rows using explicit INNER JOIN.
-- Q12: Write the same matching query using implicit join syntax.
-- Q13: Explain difference between INNER JOIN and LEFT JOIN in comments.
-- Q14: Show manager records only where manager exists.
-- Q15: Simulate a full join idea by combining left and right perspectives in words or SQL.
