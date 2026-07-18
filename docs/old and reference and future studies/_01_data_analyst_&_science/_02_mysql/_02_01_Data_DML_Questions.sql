-- ==========================================================
-- TITLE: MYSQL DATA DML BASICS QUESTIONS
-- ==========================================================

DROP DATABASE IF EXISTS mysql_02_data_dml_questions;
CREATE DATABASE mysql_02_data_dml_questions;
USE mysql_02_data_dml_questions;

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
-- SECTION 1: BASIC (10 QUESTIONS)
-- ==========================================================

-- Q1:
-- Problem:
-- Insert a new student record into q_students.
-- Table Schema:
-- q_students(student_id PK, student_name, course_name, score)
-- Sample Data:
-- Add student_id 4, name 'Deepa', course 'SQL Basics', score 90.
-- Expected Output:
-- New row should appear in q_students.
-- Constraints:
-- Use INSERT INTO.

-- Q2:
-- Problem:
-- Update q_products stock for product_id 102 to 45.
-- Table Schema:
-- q_products(product_id PK, product_name, price, stock)
-- Sample Data:
-- Existing product 102 has stock 50.
-- Expected Output:
-- q_products.stock should become 45.
-- Constraints:
-- Use UPDATE with WHERE.

-- Q3:
-- Problem:
-- Delete the order with order_id 1002 from q_orders.
-- Table Schema:
-- q_orders(order_id PK, product_id, quantity, order_date)
-- Sample Data:
-- Order 1002 exists.
-- Expected Output:
-- q_orders should not contain order_id 1002.
-- Constraints:
-- Use DELETE FROM.

-- Q4:
-- Problem:
-- Insert two new products in q_products with product_id 104 and 105.
-- Table Schema:
-- q_products(product_id PK, product_name, price, stock)
-- Sample Data:
-- 104 -> 'Eraser', 5.00, 100
-- 105 -> 'Sharpener', 8.00, 60
-- Expected Output:
-- Both rows should be added.
-- Constraints:
-- Use a single INSERT statement.

-- Q5:
-- Problem:
-- Change q_students.score for Bala to 88.
-- Table Schema:
-- q_students(student_id PK, student_name, course_name, score)
-- Sample Data:
-- Bala currently has score 82.
-- Expected Output:
-- Bala's score should update to 88.
-- Constraints:
-- Use UPDATE and WHERE.

-- Q6:
-- Problem:
-- Delete all rows from q_orders without dropping the table.
-- Table Schema:
-- q_orders(order_id PK, product_id, quantity, order_date)
-- Sample Data:
-- q_orders currently has rows.
-- Expected Output:
-- q_orders should be empty after the command.
-- Constraints:
-- Use TRUNCATE TABLE.

-- Q7:
-- Problem:
-- Add a new task called 'Submit quiz' to q_tasks and keep default status.
-- Table Schema:
-- q_tasks(task_id PK AUTO_INCREMENT, task_name, status DEFAULT 'PENDING')
-- Sample Data:
-- New row should use default status.
-- Expected Output:
-- Newly inserted row should have status 'PENDING'.
-- Constraints:
-- Do not specify status in INSERT.

-- Q8:
-- Problem:
-- Update q_bank.balance for account_id 201 by adding 500.
-- Table Schema:
-- q_bank(account_id PK, account_name, balance)
-- Sample Data:
-- Raj's current balance is 5000.00.
-- Expected Output:
-- New balance should be 5500.00.
-- Constraints:
-- Use arithmetic in UPDATE.

-- Q9:
-- Problem:
-- Delete q_students rows where score is less than 60.
-- Table Schema:
-- q_students(student_id PK, student_name, course_name, score)
-- Sample Data:
-- Chitra has score 58.
-- Expected Output:
-- Chitra's row should be removed.
-- Constraints:
-- Use WHERE with comparison.

-- Q10:
-- Problem:
-- Create q_attendance table with id, student_id, attendance_date, and status.
-- Table Schema:
-- q_attendance(id PK AUTO_INCREMENT, student_id INT, attendance_date DATE, status VARCHAR(10))
-- Sample Data:
-- Not required.
-- Expected Output:
-- Table should be created successfully.
-- Constraints:
-- Use CREATE TABLE.

-- ==========================================================
-- SECTION 2: INTERMEDIATE (10 QUESTIONS)
-- ==========================================================

-- Q11:
-- Problem:
-- Insert a row into q_products and avoid duplicate key error if product_id exists.
-- Table Schema:
-- q_products(product_id PK, product_name, price, stock)
-- Sample Data:
-- product_id 101 already exists.
-- Expected Output:
-- No error should occur if duplicate exists.
-- Constraints:
-- Use INSERT IGNORE.

-- Q12:
-- Problem:
-- Update q_products.price to 50.00 for product_id 103, but only one row.
-- Table Schema:
-- q_products(product_id PK, product_name, price, stock)
-- Sample Data:
-- product_id 103 exists.
-- Expected Output:
-- Only product 103 should change.
-- Constraints:
-- Use UPDATE with WHERE.

-- Q13:
-- Problem:
-- Insert a bank row or update balance if account_id 202 exists.
-- Table Schema:
-- q_bank(account_id PK, account_name, balance)
-- Sample Data:
-- 202 exists with balance 7200.00.
-- Expected Output:
-- Existing row should update, not insert a duplicate.
-- Constraints:
-- Use ON DUPLICATE KEY UPDATE.

-- Q14:
-- Problem:
-- Insert a task into q_tasks with task_name 'Review code'. If duplicate task_name exists, do not create a second one.
-- Table Schema:
-- q_tasks(task_id PK AUTO_INCREMENT, task_name, status)
-- Sample Data:
-- 'Review code' may or may not exist.
-- Expected Output:
-- No duplicate task names after command.
-- Constraints:
-- Use a UNIQUE constraint on task_name and INSERT IGNORE or UPSERT.

-- Q15:
-- Problem:
-- Create a temporary copy of q_students named q_students_backup and insert all rows from q_students.
-- Table Schema:
-- q_students_backup has same columns as q_students.
-- Sample Data:
-- Copy current data.
-- Expected Output:
-- q_students_backup should contain the same rows.
-- Constraints:
-- Use CREATE TABLE ... SELECT.

-- Q16:
-- Problem:
-- Set q_products.stock to 0 for the first 2 products ordered by product_id.
-- Table Schema:
-- q_products(product_id PK, product_name, price, stock)
-- Sample Data:
-- At least 3 rows exist.
-- Expected Output:
-- Exactly 2 rows updated.
-- Constraints:
-- Use UPDATE ... ORDER BY ... LIMIT.

-- Q17:
-- Problem:
-- Delete the oldest order from q_orders when there are multiple orders.
-- Table Schema:
-- q_orders(order_id PK, product_id, quantity, order_date)
-- Sample Data:
-- Multiple rows may exist.
-- Expected Output:
-- One row should be removed based on earliest order_date.
-- Constraints:
-- Use DELETE ... ORDER BY ... LIMIT.

-- Q18:
-- Problem:
-- Change q_tasks.status from 'PENDING' to 'DONE' for task_id 1.
-- Table Schema:
-- q_tasks(task_id PK AUTO_INCREMENT, task_name, status)
-- Sample Data:
-- task_id 1 exists.
-- Expected Output:
-- status should become 'DONE'.
-- Constraints:
-- Use UPDATE with WHERE.

-- Q19:
-- Problem:
-- Use a transaction to transfer 100.00 from account_id 202 to account_id 201.
-- Table Schema:
-- q_bank(account_id PK, account_name, balance)
-- Sample Data:
-- Balances exist for both accounts.
-- Expected Output:
-- One balance decreases and the other increases.
-- Constraints:
-- Use START TRANSACTION, COMMIT or ROLLBACK.

-- Q20:
-- Problem:
-- Create q_session table with a default timestamp column called created_at.
-- Table Schema:
-- q_session(session_id PK AUTO_INCREMENT, session_name VARCHAR(100), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
-- Sample Data:
-- Insert one row.
-- Expected Output:
-- created_at should fill automatically.
-- Constraints:
-- Use DEFAULT CURRENT_TIMESTAMP.

-- ==========================================================
-- SECTION 3: ADVANCED (5 QUESTIONS)
-- ==========================================================

-- Q21:
-- Problem:
-- Insert into q_products using VALUES alias and update stock if product_id 103 exists.
-- Table Schema:
-- q_products(product_id PK, product_name, price, stock)
-- Sample Data:
-- product_id 103 exists.
-- Expected Output:
-- Existing row should update stock using alias.
-- Constraints:
-- Use ON DUPLICATE KEY UPDATE with alias.

-- Q22:
-- Problem:
-- Insert into q_products and replace row when product_id 102 exists.
-- Table Schema:
-- q_products(product_id PK, product_name, price, stock)
-- Sample Data:
-- 102 exists.
-- Expected Output:
-- The existing row should be replaced.
-- Constraints:
-- Use REPLACE INTO.

-- Q23:
-- Problem:
-- Create q_inventory table and insert rows, then use DELETE LIMIT 1 to remove one row safely.
-- Table Schema:
-- q_inventory(inventory_id PK AUTO_INCREMENT, item_name VARCHAR(100), quantity INT)
-- Sample Data:
-- Insert at least two rows.
-- Expected Output:
-- Only one row should be deleted.
-- Constraints:
-- Use ORDER BY with DELETE LIMIT.

-- Q24:
-- Problem:
-- Update only one row in q_students where score is below 80.
-- Table Schema:
-- q_students(student_id PK, student_name, course_name, score)
-- Sample Data:
-- More than one row may have score below 80.
-- Expected Output:
-- A single matching row should update.
-- Constraints:
-- Use UPDATE ... ORDER BY ... LIMIT.

-- Q25:
-- Problem:
-- Explain when to use TRUNCATE versus DELETE.
-- Table Schema:
-- Words only.
-- Sample Data:
-- Not applicable.
-- Expected Output:
-- Clear rule-based explanation for both commands.
-- Constraints:
-- Answer should mention rollback support.
