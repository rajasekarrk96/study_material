-- ==========================================================
-- TITLE: MYSQL JOINS ANSWERS
-- ==========================================================

DROP DATABASE IF EXISTS mysql_07_joins_answers;
CREATE DATABASE mysql_07_joins_answers;
USE mysql_07_joins_answers;

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

-- Q1
SELECT e.emp_name, d.dept_name
FROM q_employees e
INNER JOIN q_departments d
    ON e.dept_id = d.dept_id;
-- Q2
SELECT e.emp_name, d.dept_name
FROM q_employees e
LEFT JOIN q_departments d
    ON e.dept_id = d.dept_id;
-- Q3
SELECT d.dept_name, e.emp_name
FROM q_departments d
LEFT JOIN q_employees e
    ON d.dept_id = e.dept_id;
-- Q4
SELECT *
FROM q_employees
WHERE dept_id IS NULL;
-- Q5
SELECT e.emp_name, d.dept_name
FROM q_employees e
INNER JOIN q_departments d
    ON e.dept_id = d.dept_id
WHERE d.dept_name = 'IT';
-- Q6
SELECT e.emp_name, m.emp_name AS manager_name
FROM q_employees e
LEFT JOIN q_employees m
    ON e.manager_id = m.emp_id;
-- Q7
SELECT e.emp_name, d.dept_name
FROM q_employees e
CROSS JOIN q_departments d;
-- Q8
SELECT d.dept_name, COUNT(e.emp_id) AS total_employees
FROM q_departments d
LEFT JOIN q_employees e
    ON d.dept_id = e.dept_id
GROUP BY d.dept_name;
-- Q9
SELECT d.dept_name
FROM q_departments d
LEFT JOIN q_employees e
    ON d.dept_id = e.dept_id
WHERE e.emp_id IS NULL;
-- Q10
SELECT e.emp_name, d.dept_name
FROM q_employees e
LEFT JOIN q_departments d
    ON e.dept_id = d.dept_id
ORDER BY d.dept_name, e.emp_name;
-- Q11
SELECT e.emp_name, d.dept_name
FROM q_employees e
INNER JOIN q_departments d
    ON e.dept_id = d.dept_id;
-- Q12
SELECT e.emp_name, d.dept_name
FROM q_employees e, q_departments d
WHERE e.dept_id = d.dept_id;
-- Q13
-- INNER JOIN returns matching rows only.
-- LEFT JOIN returns all left table rows plus matching right rows.
-- Q14
SELECT e.emp_name, m.emp_name AS manager_name
FROM q_employees e
INNER JOIN q_employees m
    ON e.manager_id = m.emp_id;
-- Q15
SELECT d.dept_name, e.emp_name
FROM q_departments d
LEFT JOIN q_employees e
    ON d.dept_id = e.dept_id
UNION
SELECT d.dept_name, e.emp_name
FROM q_departments d
RIGHT JOIN q_employees e
    ON d.dept_id = e.dept_id;
