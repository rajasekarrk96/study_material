-- ==========================================================
-- TITLE: MYSQL DATA DML BASICS ANSWERS
-- ==========================================================

DROP DATABASE IF EXISTS mysql_02_data_dml_answers;
CREATE DATABASE mysql_02_data_dml_answers;
USE mysql_02_data_dml_answers;

CREATE TABLE q_students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    course_name VARCHAR(100),
    score INT
);

CREATE TABLE q_products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0
);

CREATE TABLE q_orders (
    order_id INT PRIMARY KEY,
    product_id INT,
    quantity INT,
    order_date DATE
);

CREATE TABLE q_bank (
    account_id INT PRIMARY KEY,
    account_name VARCHAR(100) NOT NULL,
    balance DECIMAL(10,2) NOT NULL
);

CREATE TABLE q_tasks (
    task_id INT PRIMARY KEY AUTO_INCREMENT,
    task_name VARCHAR(100) NOT NULL,
    status VARCHAR(20) DEFAULT 'PENDING'
);

INSERT INTO q_students VALUES
(1, 'Asha', 'SQL Basics', 75),
(2, 'Bala', 'SQL Basics', 82),
(3, 'Chitra', 'SQL Advanced', 58);

INSERT INTO q_products VALUES
(101, 'Notebook', 45.00, 20),
(102, 'Pen', 12.50, 50),
(103, 'Marker', 89.00, 10);

INSERT INTO q_orders VALUES
(1001, 101, 2, '2026-04-01'),
(1002, 103, 1, '2026-04-03');

INSERT INTO q_bank VALUES
(201, 'Raj', 5000.00),
(202, 'Priya', 7200.00);

INSERT INTO q_tasks (task_name) VALUES
('Submit assignment'),
('Review notes');

-- ==========================================================
-- Q1 SOLUTION
-- ==========================================================

INSERT INTO q_students VALUES (4, 'Deepa', 'SQL Basics', 90);

SELECT * FROM q_students WHERE student_id = 4;

-- Expected Output:
-- 4 | Deepa | SQL Basics | 90

-- ==========================================================
-- Q2 SOLUTION
-- ==========================================================

UPDATE q_products
SET stock = 45
WHERE product_id = 102;

SELECT product_id, stock FROM q_products WHERE product_id = 102;

-- Expected Output:
-- 102 | 45

-- ==========================================================
-- Q3 SOLUTION
-- ==========================================================

DELETE FROM q_orders WHERE order_id = 1002;

SELECT * FROM q_orders WHERE order_id = 1002;

-- Expected Output:
-- no rows returned

-- ==========================================================
-- Q4 SOLUTION
-- ==========================================================

INSERT INTO q_products (product_id, product_name, price, stock) VALUES
(104, 'Eraser', 5.00, 100),
(105, 'Sharpener', 8.00, 60);

SELECT * FROM q_products WHERE product_id IN (104, 105);

-- Expected Output:
-- 104 | Eraser | 5.00 | 100
-- 105 | Sharpener | 8.00 | 60

-- ==========================================================
-- Q5 SOLUTION
-- ==========================================================

UPDATE q_students
SET score = 88
WHERE student_name = 'Bala';

SELECT student_name, score FROM q_students WHERE student_name = 'Bala';

-- Expected Output:
-- Bala | 88

-- ==========================================================
-- Q6 SOLUTION
-- ==========================================================

TRUNCATE TABLE q_orders;

SELECT COUNT(*) FROM q_orders;

-- Expected Output:
-- 0

-- ==========================================================
-- Q7 SOLUTION
-- ==========================================================

INSERT INTO q_tasks (task_name) VALUES ('Submit quiz');

SELECT task_name, status FROM q_tasks WHERE task_name = 'Submit quiz';

-- Expected Output:
-- Submit quiz | PENDING

-- ==========================================================
-- Q8 SOLUTION
-- ==========================================================

UPDATE q_bank
SET balance = balance + 500.00
WHERE account_id = 201;

SELECT account_id, balance FROM q_bank WHERE account_id = 201;

-- Expected Output:
-- 201 | 5500.00

-- ==========================================================
-- Q9 SOLUTION
-- ==========================================================

DELETE FROM q_students WHERE score < 60;

SELECT * FROM q_students WHERE score < 60;

-- Expected Output:
-- no rows returned

-- ==========================================================
-- Q10 SOLUTION
-- ==========================================================

DROP TABLE IF EXISTS q_attendance;

CREATE TABLE q_attendance (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    attendance_date DATE,
    status VARCHAR(10)
);

SHOW CREATE TABLE q_attendance;

-- Expected Output:
-- q_attendance created with id, student_id, attendance_date, status

-- ==========================================================
-- Q11 SOLUTION
-- ==========================================================

INSERT IGNORE INTO q_products (product_id, product_name, price, stock)
VALUES (101, 'Notebook', 45.00, 20);

SELECT * FROM q_products WHERE product_id = 101;

-- Expected Output:
-- Product remains without duplicate error

-- ==========================================================
-- Q12 SOLUTION
-- ==========================================================

UPDATE q_products
SET price = 50.00
WHERE product_id = 103;

SELECT product_id, price FROM q_products WHERE product_id = 103;

-- Expected Output:
-- 103 | 50.00

-- ==========================================================
-- Q13 SOLUTION
-- ==========================================================

INSERT INTO q_bank (account_id, account_name, balance)
VALUES (202, 'Priya', 7200.00)
ON DUPLICATE KEY UPDATE
    balance = VALUES(balance);

SELECT * FROM q_bank WHERE account_id = 202;

-- Expected Output:
-- Existing row remains and is updated if duplicate key occurs

-- ==========================================================
-- Q14 SOLUTION
-- ==========================================================

ALTER TABLE q_tasks
ADD UNIQUE KEY uq_task_name (task_name);

INSERT IGNORE INTO q_tasks (task_name)
VALUES ('Review code');

SELECT * FROM q_tasks WHERE task_name = 'Review code';

-- Expected Output:
-- One row with task_name = Review code

-- ==========================================================
-- Q15 SOLUTION
-- ==========================================================

DROP TABLE IF EXISTS q_students_backup;
CREATE TABLE q_students_backup AS SELECT * FROM q_students;

SELECT * FROM q_students_backup;

-- Expected Output:
-- Same rows as q_students

-- ==========================================================
-- Q16 SOLUTION
-- ==========================================================

UPDATE q_products
SET stock = 0
ORDER BY product_id
LIMIT 2;

SELECT product_id, stock FROM q_products ORDER BY product_id LIMIT 2;

-- Expected Output:
-- Two rows should have stock = 0

-- ==========================================================
-- Q17 SOLUTION
-- ==========================================================

DELETE FROM q_orders
ORDER BY order_date
LIMIT 1;

SELECT * FROM q_orders;

-- Expected Output:
-- The row with the earliest order_date is deleted

-- ==========================================================
-- Q18 SOLUTION
-- ==========================================================

UPDATE q_tasks
SET status = 'DONE'
WHERE task_id = 1;

SELECT task_id, status FROM q_tasks WHERE task_id = 1;

-- Expected Output:
-- 1 | DONE

-- ==========================================================
-- Q19 SOLUTION
-- ==========================================================

START TRANSACTION;

UPDATE q_bank
SET balance = balance - 100.00
WHERE account_id = 202;

UPDATE q_bank
SET balance = balance + 100.00
WHERE account_id = 201;

COMMIT;

SELECT * FROM q_bank WHERE account_id IN (201, 202);

-- Expected Output:
-- 202 balance reduced by 100.00, 201 balance increased by 100.00

-- ==========================================================
-- Q20 SOLUTION
-- ==========================================================

DROP TABLE IF EXISTS q_session;
CREATE TABLE q_session (
    session_id INT PRIMARY KEY AUTO_INCREMENT,
    session_name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO q_session (session_name) VALUES ('Morning study');

SELECT session_name, created_at FROM q_session;

-- Expected Output:
-- created_at is automatically generated

-- ==========================================================
-- Q21 SOLUTION
-- ==========================================================

INSERT INTO q_products (product_id, product_name, price, stock)
VALUES (103, 'Marker', 89.00, 15)
ON DUPLICATE KEY UPDATE
    stock = VALUES(stock);

SELECT * FROM q_products WHERE product_id = 103;

-- Expected Output:
-- q_products row for 103 is updated using alias

-- ==========================================================
-- Q22 SOLUTION
-- ==========================================================

REPLACE INTO q_products (product_id, product_name, price, stock)
VALUES (102, 'Pen', 12.50, 30);

SELECT * FROM q_products WHERE product_id = 102;

-- Expected Output:
-- Existing row is replaced with new values

-- ==========================================================
-- Q23 SOLUTION
-- ==========================================================

DROP TABLE IF EXISTS q_inventory;
CREATE TABLE q_inventory (
    inventory_id INT PRIMARY KEY AUTO_INCREMENT,
    item_name VARCHAR(100),
    quantity INT
);

INSERT INTO q_inventory (item_name, quantity) VALUES
('A4 Paper', 200),
('Stapler', 15);

DELETE FROM q_inventory
ORDER BY inventory_id
LIMIT 1;

SELECT * FROM q_inventory;

-- Expected Output:
-- One row deleted, one row remains

-- ==========================================================
-- Q24 SOLUTION
-- ==========================================================

UPDATE q_students
SET score = score + 5
WHERE score < 80
ORDER BY student_id
LIMIT 1;

SELECT * FROM q_students WHERE score < 85;

-- Expected Output:
-- Only one below-80 row is updated

-- ==========================================================
-- Q25 SOLUTION
-- ==========================================================

-- TRUNCATE TABLE removes all rows quickly and resets storage.
-- It is DDL, so it cannot be rolled back in most engines.
-- DELETE removes rows one by one and can be rolled back if inside a transaction.

-- Use TRUNCATE when you want to empty a table fast and do not need rollback.
-- Use DELETE when you need finer control, WHERE filtering, or rollback support.
