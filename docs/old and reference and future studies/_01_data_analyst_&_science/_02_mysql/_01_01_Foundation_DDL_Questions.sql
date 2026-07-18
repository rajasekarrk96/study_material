-- ==========================================================
-- TITLE: MYSQL FOUNDATION DDL QUESTIONS
-- ==========================================================

DROP DATABASE IF EXISTS mysql_01_foundation_ddl_questions;
CREATE DATABASE mysql_01_foundation_ddl_questions;
USE mysql_01_foundation_ddl_questions;

CREATE TABLE q_departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    location VARCHAR(100)
);

CREATE TABLE q_employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    salary DECIMAL(10,2),
    department_id INT,
    join_date DATE
);

INSERT INTO q_departments VALUES
(1, 'Engineering', 'Bangalore'),
(2, 'Sales', 'Mumbai'),
(3, 'Finance', 'Delhi');

INSERT INTO q_employees VALUES
(101, 'Aarav Sharma', 'aarav@corp.com', 75000.00, 1, '2023-01-15'),
(102, 'Diya Mehta', 'diya@corp.com', 68000.00, 2, '2022-11-21'),
(103, 'Kabir Nair', 'kabir@corp.com', 82000.00, 1, '2021-06-10');

SELECT * FROM q_departments;
SELECT * FROM q_employees;

-- ==========================================================
-- SECTION 1: BASIC (10 QUESTIONS)
-- ==========================================================

-- Q1:
-- Problem:
-- Create a database named company_lab.
-- Table Schema:
-- Database only.
-- Sample Data:
-- Not required.
-- Expected Output:
-- Database company_lab should exist.
-- Constraints:
-- Use IF NOT EXISTS.

-- Q2:
-- Problem:
-- Create a table named students with columns student_id, student_name, and course_name.
-- Table Schema:
-- student_id INT PRIMARY KEY
-- student_name VARCHAR(100) NOT NULL
-- course_name VARCHAR(100) NOT NULL
-- Sample Data:
-- Not required.
-- Expected Output:
-- Table should be created successfully.
-- Constraints:
-- student_id must be the primary key.

-- Q3:
-- Problem:
-- Create a table named products with an AUTO_INCREMENT primary key.
-- Table Schema:
-- product_id INT PRIMARY KEY AUTO_INCREMENT
-- product_name VARCHAR(100) NOT NULL
-- price DECIMAL(8,2) NOT NULL
-- Sample Data:
-- Insert two rows after creation.
-- Expected Output:
-- product_id values should auto-generate.
-- Constraints:
-- price must not be NULL.

-- Q4:
-- Problem:
-- Create a table named users where email must be unique.
-- Table Schema:
-- user_id INT PRIMARY KEY
-- user_name VARCHAR(100) NOT NULL
-- email VARCHAR(150) UNIQUE
-- Sample Data:
-- Add two valid rows.
-- Expected Output:
-- Duplicate email values should not be allowed.
-- Constraints:
-- Keep email nullable.

-- Q5:
-- Problem:
-- Create a table named tasks with a default status value of OPEN.
-- Table Schema:
-- task_id INT PRIMARY KEY
-- task_name VARCHAR(100) NOT NULL
-- status VARCHAR(20) DEFAULT 'OPEN'
-- Sample Data:
-- Insert one row without status.
-- Expected Output:
-- status should become OPEN automatically.
-- Constraints:
-- Use DEFAULT.

-- Q6:
-- Problem:
-- Create a table named departments_basic and inspect its structure.
-- Table Schema:
-- department_id INT PRIMARY KEY
-- department_name VARCHAR(100) NOT NULL
-- Sample Data:
-- Not required.
-- Expected Output:
-- DESCRIBE should show both columns.
-- Constraints:
-- Use DESCRIBE after creation.

-- Q7:
-- Problem:
-- Add a phone_number column to the existing q_employees table.
-- Table Schema:
-- phone_number VARCHAR(15)
-- Sample Data:
-- Not required.
-- Expected Output:
-- q_employees should contain the new column.
-- Constraints:
-- Use ALTER TABLE ... ADD.

-- Q8:
-- Problem:
-- Modify q_employees.employee_name so it allows 150 characters.
-- Table Schema:
-- employee_name VARCHAR(150) NOT NULL
-- Sample Data:
-- Existing rows should remain valid.
-- Expected Output:
-- Column size should be updated.
-- Constraints:
-- Use MODIFY.

-- Q9:
-- Problem:
-- Rename q_employees.email to work_email.
-- Table Schema:
-- work_email VARCHAR(100)
-- Sample Data:
-- Existing email data should remain.
-- Expected Output:
-- Column name should change.
-- Constraints:
-- Use CHANGE or RENAME COLUMN.

-- Q10:
-- Problem:
-- Drop the phone_number column from q_employees.
-- Table Schema:
-- Remove phone_number only.
-- Sample Data:
-- Existing employee rows should remain.
-- Expected Output:
-- q_employees should no longer have phone_number.
-- Constraints:
-- Use ALTER TABLE ... DROP COLUMN.

-- ==========================================================
-- SECTION 2: INTERMEDIATE (10 QUESTIONS)
-- ==========================================================

-- Q11:
-- Problem:
-- Create parent and child tables for categories and items using a foreign key.
-- Table Schema:
-- categories(category_id PK, category_name)
-- items(item_id PK, item_name, category_id FK)
-- Sample Data:
-- Insert two categories and two items.
-- Expected Output:
-- Items should reference valid categories.
-- Constraints:
-- Foreign key must reference categories(category_id).

-- Q12:
-- Problem:
-- Create a table named attendance with a composite primary key.
-- Table Schema:
-- employee_id INT
-- attendance_date DATE
-- attendance_status VARCHAR(10)
-- Sample Data:
-- Insert three unique combinations.
-- Expected Output:
-- Duplicate employee_id + attendance_date should not be allowed.
-- Constraints:
-- Composite key on employee_id and attendance_date.

-- Q13:
-- Problem:
-- Create a table named payroll with a CHECK constraint that salary must be greater than 0.
-- Table Schema:
-- payroll_id INT PRIMARY KEY
-- employee_name VARCHAR(100)
-- salary DECIMAL(10,2)
-- Sample Data:
-- Insert valid rows only.
-- Expected Output:
-- Table should enforce positive salary values.
-- Constraints:
-- Use a named CHECK constraint.

-- Q14:
-- Problem:
-- Create a table named orders_mid with created_at defaulting to the current timestamp.
-- Table Schema:
-- order_id INT PRIMARY KEY AUTO_INCREMENT
-- customer_name VARCHAR(100) NOT NULL
-- created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- Sample Data:
-- Insert two rows.
-- Expected Output:
-- created_at should auto-fill.
-- Constraints:
-- Use CURRENT_TIMESTAMP.

-- Q15:
-- Problem:
-- Rename q_departments to q_department_master.
-- Table Schema:
-- Same columns as q_departments.
-- Sample Data:
-- Existing rows should remain.
-- Expected Output:
-- Table should exist under the new name.
-- Constraints:
-- Use RENAME TABLE.

-- Q16:
-- Problem:
-- Create a table temp_sales, insert three rows, then remove all rows quickly without removing the structure.
-- Table Schema:
-- sale_id INT PRIMARY KEY AUTO_INCREMENT
-- sale_amount DECIMAL(10,2) NOT NULL
-- Sample Data:
-- Insert three rows.
-- Expected Output:
-- Table should remain, but row count should become 0.
-- Constraints:
-- Use TRUNCATE TABLE.

-- Q17:
-- Problem:
-- Create an index on q_employees(department_id).
-- Table Schema:
-- Existing q_employees table.
-- Sample Data:
-- Existing data may be used.
-- Expected Output:
-- SHOW INDEX should display the new index.
-- Constraints:
-- Use CREATE INDEX.

-- Q18:
-- Problem:
-- Create a unique index on q_employees(work_email) after renaming the column.
-- Table Schema:
-- Existing q_employees table.
-- Sample Data:
-- Existing work_email data may be used.
-- Expected Output:
-- SHOW INDEX should display a unique index.
-- Constraints:
-- Use CREATE UNIQUE INDEX.

-- Q19:
-- Problem:
-- Create a table named course_enrollments with foreign keys to students and courses tables.
-- Table Schema:
-- students_q19(student_id PK, student_name)
-- courses_q19(course_id PK, course_name)
-- course_enrollments(student_id, course_id, enrolled_on)
-- Sample Data:
-- Insert valid rows in all tables.
-- Expected Output:
-- Enrollment table should represent a many-to-many relationship.
-- Constraints:
-- Use a composite primary key in course_enrollments.

-- Q20:
-- Problem:
-- Show the complete CREATE TABLE definition for q_employees.
-- Table Schema:
-- Existing q_employees table.
-- Sample Data:
-- Existing rows may remain.
-- Expected Output:
-- MySQL should return the full CREATE TABLE statement.
-- Constraints:
-- Use SHOW CREATE TABLE.

-- ==========================================================
-- SECTION 3: ADVANCED (10 QUESTIONS)
-- ==========================================================

-- Q21:
-- Problem:
-- Create a table named subscriptions with checks on monthly_fee and date range.
-- Table Schema:
-- subscription_id INT PK AUTO_INCREMENT
-- customer_email VARCHAR(150) UNIQUE NOT NULL
-- monthly_fee DECIMAL(8,2) NOT NULL
-- start_date DATE NOT NULL
-- end_date DATE NULL
-- Sample Data:
-- Insert valid sample rows.
-- Expected Output:
-- Table should reject negative fee and invalid date order.
-- Constraints:
-- Use two CHECK constraints.

-- Q22:
-- Problem:
-- Create a table named shipment_tracking and add a column named last_updated after creation.
-- Table Schema:
-- tracking_id INT PK
-- shipment_code VARCHAR(30) NOT NULL
-- current_status VARCHAR(30) NOT NULL
-- last_updated DATETIME
-- Sample Data:
-- Insert one row after altering the table.
-- Expected Output:
-- Table should include last_updated.
-- Constraints:
-- Use ALTER TABLE ... ADD.

-- Q23:
-- Problem:
-- Create a table named account_audit and position a new column audit_note as the first column.
-- Table Schema:
-- audit_id INT PK
-- account_id INT NOT NULL
-- action_name VARCHAR(50) NOT NULL
-- Sample Data:
-- Not required.
-- Expected Output:
-- audit_note should appear first in DESCRIBE output.
-- Constraints:
-- Use ALTER TABLE ... ADD COLUMN ... FIRST.

-- Q24:
-- Problem:
-- Create a table named inventory_levels and add a composite unique constraint on warehouse_id and sku_code.
-- Table Schema:
-- inventory_id INT PK
-- warehouse_id INT NOT NULL
-- sku_code VARCHAR(30) NOT NULL
-- quantity INT NOT NULL
-- Sample Data:
-- Insert valid unique combinations.
-- Expected Output:
-- Duplicate warehouse_id + sku_code combinations should not be allowed.
-- Constraints:
-- Use UNIQUE(warehouse_id, sku_code).

-- Q25:
-- Problem:
-- Create a table named login_sessions and reset its AUTO_INCREMENT start value to 1000.
-- Table Schema:
-- session_id INT PK AUTO_INCREMENT
-- user_name VARCHAR(100) NOT NULL
-- Sample Data:
-- Insert one row after reset.
-- Expected Output:
-- First inserted row should start at 1000.
-- Constraints:
-- Use ALTER TABLE ... AUTO_INCREMENT.

-- Q26:
-- Problem:
-- Create a table named archived_orders and then drop it safely.
-- Table Schema:
-- order_id INT PRIMARY KEY
-- order_total DECIMAL(10,2)
-- Sample Data:
-- Not required.
-- Expected Output:
-- Table should be removed without error even if rerun.
-- Constraints:
-- Use DROP TABLE IF EXISTS.

-- Q27:
-- Problem:
-- Query INFORMATION_SCHEMA.COLUMNS to list all columns of q_employees in order.
-- Table Schema:
-- Existing q_employees table.
-- Sample Data:
-- Existing data may remain.
-- Expected Output:
-- Ordered metadata rows for q_employees.
-- Constraints:
-- Use table_schema and table_name filters.

-- Q28:
-- Problem:
-- Create a table named project_allocations with foreign keys and explicit constraint names.
-- Table Schema:
-- employees_q28(employee_id PK)
-- projects_q28(project_id PK)
-- project_allocations(employee_id, project_id, role_name)
-- Sample Data:
-- Insert valid rows.
-- Expected Output:
-- SHOW CREATE TABLE should show the named constraints.
-- Constraints:
-- Use named foreign keys.

-- Q29:
-- Problem:
-- Create a full repeatable DDL script for a table named branch_offices that can run multiple times.
-- Table Schema:
-- branch_id INT PK AUTO_INCREMENT
-- branch_name VARCHAR(100) NOT NULL UNIQUE
-- city VARCHAR(100) NOT NULL
-- Sample Data:
-- Insert two rows.
-- Expected Output:
-- Script should work on rerun without manual cleanup.
-- Constraints:
-- Use safe drop/create logic.

-- Q30:
-- Problem:
-- Create a bridge table named employee_skills between employees_q30 and skills_q30.
-- Table Schema:
-- employees_q30(employee_id PK, employee_name)
-- skills_q30(skill_id PK, skill_name)
-- employee_skills(employee_id, skill_id, skill_level)
-- Sample Data:
-- Insert valid rows.
-- Expected Output:
-- Bridge table should store many-to-many mappings.
-- Constraints:
-- Composite primary key and two foreign keys required.

-- ==========================================================
-- SECTION 4: REAL-WORLD (5 QUESTIONS)
-- ==========================================================

-- Q31:
-- Problem:
-- Design a customer_support_tickets table for a helpdesk system.
-- Table Schema:
-- ticket_id INT PK AUTO_INCREMENT
-- customer_email VARCHAR(150) NOT NULL
-- subject_line VARCHAR(150) NOT NULL
-- priority_level VARCHAR(20) DEFAULT 'MEDIUM'
-- opened_on DATETIME DEFAULT CURRENT_TIMESTAMP
-- ticket_status VARCHAR(20) DEFAULT 'OPEN'
-- Sample Data:
-- Insert three rows.
-- Expected Output:
-- Defaults should populate automatically.
-- Constraints:
-- customer_email and subject_line must be NOT NULL.

-- Q32:
-- Problem:
-- Design a retail_products table with a positive price rule and a unique SKU.
-- Table Schema:
-- product_id INT PK AUTO_INCREMENT
-- sku_code VARCHAR(30) UNIQUE NOT NULL
-- product_name VARCHAR(150) NOT NULL
-- selling_price DECIMAL(10,2) NOT NULL
-- Sample Data:
-- Insert valid rows.
-- Expected Output:
-- Table should enforce uniqueness and positive price.
-- Constraints:
-- Use a CHECK constraint.

-- Q33:
-- Problem:
-- Design tables for hospitals and doctors where each doctor belongs to one hospital.
-- Table Schema:
-- hospitals(hospital_id PK, hospital_name)
-- doctors(doctor_id PK, doctor_name, hospital_id FK)
-- Sample Data:
-- Insert valid rows.
-- Expected Output:
-- Doctors should reference hospitals correctly.
-- Constraints:
-- Use foreign key relationship.

-- Q34:
-- Problem:
-- Create a subscription_payments table for a SaaS system and later rename a column from payment_mode to payment_method.
-- Table Schema:
-- payment_id INT PK AUTO_INCREMENT
-- subscriber_email VARCHAR(150) NOT NULL
-- payment_mode VARCHAR(30) NOT NULL
-- paid_amount DECIMAL(10,2) NOT NULL
-- paid_on DATE NOT NULL
-- Sample Data:
-- Insert valid rows after rename.
-- Expected Output:
-- Column should be renamed while keeping intended meaning.
-- Constraints:
-- Use ALTER TABLE for the rename.

-- Q35:
-- Problem:
-- Create an employee_attendance_log table and then create an index to support frequent searches by attendance_date and employee_id.
-- Table Schema:
-- log_id INT PK AUTO_INCREMENT
-- employee_id INT NOT NULL
-- attendance_date DATE NOT NULL
-- attendance_status VARCHAR(20) NOT NULL
-- Sample Data:
-- Insert valid rows.
-- Expected Output:
-- SHOW INDEX should show the new composite index.
-- Constraints:
-- Use a composite index in the correct column order.
