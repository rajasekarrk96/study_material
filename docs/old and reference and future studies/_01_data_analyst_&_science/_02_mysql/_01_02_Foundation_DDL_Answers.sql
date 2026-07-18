-- ==========================================================
-- TITLE: MYSQL FOUNDATION DDL ANSWERS
-- ==========================================================

DROP DATABASE IF EXISTS mysql_01_foundation_ddl_answers;
CREATE DATABASE mysql_01_foundation_ddl_answers;
USE mysql_01_foundation_ddl_answers;

-- ==========================================================
-- Q1 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- Create the database only if it does not already exist.

CREATE DATABASE IF NOT EXISTS company_lab;

-- Query:
SELECT schema_name
FROM information_schema.schemata
WHERE schema_name = 'company_lab';

-- Expected Output:
-- company_lab

-- Test Case:
SELECT schema_name
FROM information_schema.schemata
WHERE schema_name = 'company_lab';

-- ==========================================================
-- Q2 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- Create the students table and define student_id as the primary key.

DROP TABLE IF EXISTS students_q2;

CREATE TABLE students_q2 (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    course_name VARCHAR(100) NOT NULL
);

-- Query:
DESCRIBE students_q2;

-- Expected Output:
-- student_id
-- student_name
-- course_name

-- Test Case:
SHOW CREATE TABLE students_q2;

-- ==========================================================
-- Q3 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- AUTO_INCREMENT generates sequential primary key values automatically.

DROP TABLE IF EXISTS products_q3;

CREATE TABLE products_q3 (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(8,2) NOT NULL
);

INSERT INTO products_q3 (product_name, price) VALUES
('Keyboard', 1499.00),
('Mouse', 799.00);

-- Query:
SELECT * FROM products_q3;

-- Expected Output:
-- 1 | Keyboard | 1499.00
-- 2 | Mouse    | 799.00

-- Test Case:
DESCRIBE products_q3;

-- ==========================================================
-- Q4 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- UNIQUE prevents duplicate email values while the nullable column can still remain optional.

DROP TABLE IF EXISTS users_q4;

CREATE TABLE users_q4 (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE
);

INSERT INTO users_q4 VALUES
(1, 'Riya', 'riya@example.com'),
(2, 'Dev', 'dev@example.com');

-- Query:
SELECT * FROM users_q4;

-- Expected Output:
-- 1 | Riya | riya@example.com
-- 2 | Dev  | dev@example.com

-- Test Case:
SHOW INDEX FROM users_q4;

-- ==========================================================
-- Q5 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- DEFAULT automatically fills a value when the column is omitted.

DROP TABLE IF EXISTS tasks_q5;

CREATE TABLE tasks_q5 (
    task_id INT PRIMARY KEY,
    task_name VARCHAR(100) NOT NULL,
    status VARCHAR(20) DEFAULT 'OPEN'
);

INSERT INTO tasks_q5 (task_id, task_name) VALUES
(1, 'Prepare report');

-- Query:
SELECT * FROM tasks_q5;

-- Expected Output:
-- 1 | Prepare report | OPEN

-- Test Case:
DESCRIBE tasks_q5;

-- ==========================================================
-- Q6 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- Create the table and inspect it with DESCRIBE.

DROP TABLE IF EXISTS departments_basic_q6;

CREATE TABLE departments_basic_q6 (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);

-- Query:
DESCRIBE departments_basic_q6;

-- Expected Output:
-- department_id
-- department_name

-- Test Case:
SHOW CREATE TABLE departments_basic_q6;

-- ==========================================================
-- Q7 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- Add a new nullable phone_number column to an existing table.

DROP TABLE IF EXISTS q_employees_q7;

CREATE TABLE q_employees_q7 (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    salary DECIMAL(10,2),
    department_id INT,
    join_date DATE
);

ALTER TABLE q_employees_q7
ADD phone_number VARCHAR(15);

-- Query:
DESCRIBE q_employees_q7;

-- Expected Output:
-- Column list should include phone_number.

-- Test Case:
SHOW CREATE TABLE q_employees_q7;

-- ==========================================================
-- Q8 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- MODIFY changes the type or attributes of an existing column.

DROP TABLE IF EXISTS q_employees_q8;

CREATE TABLE q_employees_q8 (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL
);

ALTER TABLE q_employees_q8
MODIFY employee_name VARCHAR(150) NOT NULL;

-- Query:
DESCRIBE q_employees_q8;

-- Expected Output:
-- employee_name should be VARCHAR(150) NOT NULL.

-- Test Case:
SHOW CREATE TABLE q_employees_q8;

-- ==========================================================
-- Q9 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- Rename the email column while preserving its type definition.

DROP TABLE IF EXISTS q_employees_q9;

CREATE TABLE q_employees_q9 (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    email VARCHAR(100)
);

INSERT INTO q_employees_q9 VALUES
(101, 'Aarav Sharma', 'aarav@corp.com');

ALTER TABLE q_employees_q9
CHANGE email work_email VARCHAR(100);

-- Query:
SELECT * FROM q_employees_q9;

-- Expected Output:
-- 101 | Aarav Sharma | aarav@corp.com

-- Test Case:
DESCRIBE q_employees_q9;

-- ==========================================================
-- Q10 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- Drop an unnecessary column while keeping the rest of the table.

DROP TABLE IF EXISTS q_employees_q10;

CREATE TABLE q_employees_q10 (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15)
);

ALTER TABLE q_employees_q10
DROP COLUMN phone_number;

-- Query:
DESCRIBE q_employees_q10;

-- Expected Output:
-- Only employee_id and employee_name should remain.

-- Test Case:
SHOW CREATE TABLE q_employees_q10;

-- ==========================================================
-- Q11 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- Create the parent table first, then the child table with a foreign key.

DROP TABLE IF EXISTS items_q11;
DROP TABLE IF EXISTS categories_q11;

CREATE TABLE categories_q11 (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL
);

CREATE TABLE items_q11 (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    category_id INT,
    CONSTRAINT fk_items_q11_category
        FOREIGN KEY (category_id) REFERENCES categories_q11(category_id)
);

INSERT INTO categories_q11 VALUES
(1, 'Hardware'),
(2, 'Software');

INSERT INTO items_q11 VALUES
(101, 'Keyboard', 1),
(102, 'License Pack', 2);

-- Query:
SELECT * FROM items_q11;

-- Expected Output:
-- 101 | Keyboard     | 1
-- 102 | License Pack | 2

-- Test Case:
SHOW CREATE TABLE items_q11;

-- ==========================================================
-- Q12 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- A composite primary key makes the employee-date combination unique.

DROP TABLE IF EXISTS attendance_q12;

CREATE TABLE attendance_q12 (
    employee_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    attendance_status VARCHAR(10) NOT NULL,
    PRIMARY KEY (employee_id, attendance_date)
);

INSERT INTO attendance_q12 VALUES
(1, '2024-06-01', 'PRESENT'),
(1, '2024-06-02', 'ABSENT'),
(2, '2024-06-01', 'PRESENT');

-- Query:
SELECT * FROM attendance_q12;

-- Expected Output:
-- 1 | 2024-06-01 | PRESENT
-- 1 | 2024-06-02 | ABSENT
-- 2 | 2024-06-01 | PRESENT

-- Test Case:
SHOW CREATE TABLE attendance_q12;

-- ==========================================================
-- Q13 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- CHECK ensures salary values stay positive.

DROP TABLE IF EXISTS payroll_q13;

CREATE TABLE payroll_q13 (
    payroll_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    salary DECIMAL(10,2),
    CONSTRAINT chk_payroll_q13_salary CHECK (salary > 0)
);

INSERT INTO payroll_q13 VALUES
(1, 'Aarav Sharma', 45000.00),
(2, 'Diya Mehta', 52000.00);

-- Query:
SELECT * FROM payroll_q13;

-- Expected Output:
-- Two rows with positive salary values.

-- Test Case:
SHOW CREATE TABLE payroll_q13;

-- ==========================================================
-- Q14 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- CURRENT_TIMESTAMP fills the creation time automatically.

DROP TABLE IF EXISTS orders_mid_q14;

CREATE TABLE orders_mid_q14 (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO orders_mid_q14 (customer_name) VALUES
('Nina'),
('Arjun');

-- Query:
SELECT * FROM orders_mid_q14;

-- Expected Output:
-- created_at should contain timestamps for both rows.

-- Test Case:
DESCRIBE orders_mid_q14;

-- ==========================================================
-- Q15 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- Rename the table without changing its rows.

DROP TABLE IF EXISTS q_department_master_q15;
DROP TABLE IF EXISTS q_departments_q15;

CREATE TABLE q_departments_q15 (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);

INSERT INTO q_departments_q15 VALUES
(1, 'Engineering'),
(2, 'Sales');

RENAME TABLE q_departments_q15 TO q_department_master_q15;

-- Query:
SHOW TABLES LIKE 'q_department_master_q15';

-- Expected Output:
-- q_department_master_q15

-- Test Case:
SELECT * FROM q_department_master_q15;

-- ==========================================================
-- Q16 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- TRUNCATE removes all rows while keeping the table structure.

DROP TABLE IF EXISTS temp_sales_q16;

CREATE TABLE temp_sales_q16 (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    sale_amount DECIMAL(10,2) NOT NULL
);

INSERT INTO temp_sales_q16 (sale_amount) VALUES
(500.00),
(750.00),
(900.00);

TRUNCATE TABLE temp_sales_q16;

-- Query:
SELECT COUNT(*) AS row_count FROM temp_sales_q16;

-- Expected Output:
-- 0

-- Test Case:
DESCRIBE temp_sales_q16;

-- ==========================================================
-- Q17 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- Create a normal index on department_id to support filtering and joins.

DROP TABLE IF EXISTS q_employees_q17;

CREATE TABLE q_employees_q17 (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    department_id INT
);

CREATE INDEX idx_q17_department
ON q_employees_q17 (department_id);

-- Query:
SHOW INDEX FROM q_employees_q17;

-- Expected Output:
-- PRIMARY and idx_q17_department should be shown.

-- Test Case:
SHOW CREATE TABLE q_employees_q17;

-- ==========================================================
-- Q18 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- A unique index enforces distinct values and also supports search operations.

DROP TABLE IF EXISTS q_employees_q18;

CREATE TABLE q_employees_q18 (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    work_email VARCHAR(100)
);

CREATE UNIQUE INDEX idx_q18_work_email
ON q_employees_q18 (work_email);

-- Query:
SHOW INDEX FROM q_employees_q18;

-- Expected Output:
-- PRIMARY and unique idx_q18_work_email should be shown.

-- Test Case:
SHOW CREATE TABLE q_employees_q18;

-- ==========================================================
-- Q19 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- Build the two parent tables first, then the many-to-many enrollment table.

DROP TABLE IF EXISTS course_enrollments_q19;
DROP TABLE IF EXISTS courses_q19;
DROP TABLE IF EXISTS students_q19;

CREATE TABLE students_q19 (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL
);

CREATE TABLE courses_q19 (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL
);

CREATE TABLE course_enrollments_q19 (
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrolled_on DATE NOT NULL,
    PRIMARY KEY (student_id, course_id),
    CONSTRAINT fk_ce_q19_student
        FOREIGN KEY (student_id) REFERENCES students_q19(student_id),
    CONSTRAINT fk_ce_q19_course
        FOREIGN KEY (course_id) REFERENCES courses_q19(course_id)
);

INSERT INTO students_q19 VALUES
(1, 'Ravi'),
(2, 'Mira');

INSERT INTO courses_q19 VALUES
(10, 'MySQL Basics'),
(20, 'Advanced SQL');

INSERT INTO course_enrollments_q19 VALUES
(1, 10, '2024-07-01'),
(1, 20, '2024-07-02'),
(2, 10, '2024-07-03');

-- Query:
SELECT * FROM course_enrollments_q19;

-- Expected Output:
-- Three valid enrollment rows.

-- Test Case:
SHOW CREATE TABLE course_enrollments_q19;

-- ==========================================================
-- Q20 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- SHOW CREATE TABLE returns the exact stored definition.

DROP TABLE IF EXISTS q_employees_q20;

CREATE TABLE q_employees_q20 (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    work_email VARCHAR(100) UNIQUE
);

-- Query:
SHOW CREATE TABLE q_employees_q20;

-- Expected Output:
-- MySQL should return the full CREATE TABLE statement.

-- Test Case:
DESCRIBE q_employees_q20;

-- ==========================================================
-- Q21 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- Use one CHECK for fee validation and one for date ordering.

DROP TABLE IF EXISTS subscriptions_q21;

CREATE TABLE subscriptions_q21 (
    subscription_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_email VARCHAR(150) UNIQUE NOT NULL,
    monthly_fee DECIMAL(8,2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NULL,
    CONSTRAINT chk_q21_monthly_fee CHECK (monthly_fee > 0),
    CONSTRAINT chk_q21_date_range CHECK (end_date IS NULL OR end_date >= start_date)
);

INSERT INTO subscriptions_q21
(customer_email, monthly_fee, start_date, end_date)
VALUES
('alpha@saas.com', 299.00, '2024-01-01', NULL),
('beta@saas.com', 499.00, '2024-02-01', '2024-12-31');

-- Query:
SELECT * FROM subscriptions_q21;

-- Expected Output:
-- Two valid subscription rows.

-- Test Case:
SHOW CREATE TABLE subscriptions_q21;

-- ==========================================================
-- Q22 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- Create the base table first, then add the new column through ALTER TABLE.

DROP TABLE IF EXISTS shipment_tracking_q22;

CREATE TABLE shipment_tracking_q22 (
    tracking_id INT PRIMARY KEY,
    shipment_code VARCHAR(30) NOT NULL,
    current_status VARCHAR(30) NOT NULL
);

ALTER TABLE shipment_tracking_q22
ADD last_updated DATETIME;

INSERT INTO shipment_tracking_q22 VALUES
(1, 'SHIP-1001', 'IN_TRANSIT', '2024-08-01 10:00:00');

-- Query:
SELECT * FROM shipment_tracking_q22;

-- Expected Output:
-- 1 | SHIP-1001 | IN_TRANSIT | 2024-08-01 10:00:00

-- Test Case:
DESCRIBE shipment_tracking_q22;

-- ==========================================================
-- Q23 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- FIRST places a new column at the beginning of the table definition.

DROP TABLE IF EXISTS account_audit_q23;

CREATE TABLE account_audit_q23 (
    audit_id INT PRIMARY KEY,
    account_id INT NOT NULL,
    action_name VARCHAR(50) NOT NULL
);

ALTER TABLE account_audit_q23
ADD COLUMN audit_note VARCHAR(100) FIRST;

-- Query:
DESCRIBE account_audit_q23;

-- Expected Output:
-- audit_note should be the first listed column.

-- Test Case:
SHOW CREATE TABLE account_audit_q23;

-- ==========================================================
-- Q24 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- A composite unique constraint prevents duplicate warehouse-SKU pairs.

DROP TABLE IF EXISTS inventory_levels_q24;

CREATE TABLE inventory_levels_q24 (
    inventory_id INT PRIMARY KEY,
    warehouse_id INT NOT NULL,
    sku_code VARCHAR(30) NOT NULL,
    quantity INT NOT NULL,
    UNIQUE (warehouse_id, sku_code)
);

INSERT INTO inventory_levels_q24 VALUES
(1, 10, 'SKU-001', 25),
(2, 10, 'SKU-002', 40),
(3, 20, 'SKU-001', 60);

-- Query:
SELECT * FROM inventory_levels_q24;

-- Expected Output:
-- Three unique warehouse-SKU combinations.

-- Test Case:
SHOW CREATE TABLE inventory_levels_q24;

-- ==========================================================
-- Q25 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- Reset the AUTO_INCREMENT starting point before inserting data.

DROP TABLE IF EXISTS login_sessions_q25;

CREATE TABLE login_sessions_q25 (
    session_id INT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(100) NOT NULL
);

ALTER TABLE login_sessions_q25 AUTO_INCREMENT = 1000;

INSERT INTO login_sessions_q25 (user_name) VALUES
('session_user');

-- Query:
SELECT * FROM login_sessions_q25;

-- Expected Output:
-- 1000 | session_user

-- Test Case:
SHOW CREATE TABLE login_sessions_q25;

-- ==========================================================
-- Q26 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- IF EXISTS makes repeated drops safe.

DROP TABLE IF EXISTS archived_orders_q26;

CREATE TABLE archived_orders_q26 (
    order_id INT PRIMARY KEY,
    order_total DECIMAL(10,2)
);

DROP TABLE IF EXISTS archived_orders_q26;

-- Query:
SHOW TABLES LIKE 'archived_orders_q26';

-- Expected Output:
-- Empty result

-- Test Case:
SELECT COUNT(*) AS object_count
FROM information_schema.tables
WHERE table_schema = 'mysql_01_foundation_ddl_answers'
  AND table_name = 'archived_orders_q26';

-- ==========================================================
-- Q27 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- INFORMATION_SCHEMA stores metadata for databases, tables, and columns.

DROP TABLE IF EXISTS q_employees_q27;

CREATE TABLE q_employees_q27 (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    work_email VARCHAR(100),
    salary DECIMAL(10,2)
);

-- Query:
SELECT
    ordinal_position,
    column_name,
    data_type,
    is_nullable
FROM information_schema.columns
WHERE table_schema = 'mysql_01_foundation_ddl_answers'
  AND table_name = 'q_employees_q27'
ORDER BY ordinal_position;

-- Expected Output:
-- Ordered metadata rows for q_employees_q27.

-- Test Case:
SHOW CREATE TABLE q_employees_q27;

-- ==========================================================
-- Q28 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- Explicit constraint names make later maintenance easier.

DROP TABLE IF EXISTS project_allocations_q28;
DROP TABLE IF EXISTS projects_q28;
DROP TABLE IF EXISTS employees_q28;

CREATE TABLE employees_q28 (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL
);

CREATE TABLE projects_q28 (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL
);

CREATE TABLE project_allocations_q28 (
    employee_id INT NOT NULL,
    project_id INT NOT NULL,
    role_name VARCHAR(50) NOT NULL,
    CONSTRAINT fk_pa_q28_employee
        FOREIGN KEY (employee_id) REFERENCES employees_q28(employee_id),
    CONSTRAINT fk_pa_q28_project
        FOREIGN KEY (project_id) REFERENCES projects_q28(project_id)
);

INSERT INTO employees_q28 VALUES
(1, 'Aarav'),
(2, 'Diya');

INSERT INTO projects_q28 VALUES
(101, 'ERP Upgrade'),
(102, 'CRM Rollout');

INSERT INTO project_allocations_q28 VALUES
(1, 101, 'Developer'),
(2, 102, 'Coordinator');

-- Query:
SHOW CREATE TABLE project_allocations_q28;

-- Expected Output:
-- CREATE TABLE output should include fk_pa_q28_employee and fk_pa_q28_project.

-- Test Case:
SELECT * FROM project_allocations_q28;

-- ==========================================================
-- Q29 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- Repeatable scripts begin with safe cleanup and then recreate objects.

DROP TABLE IF EXISTS branch_offices_q29;

CREATE TABLE branch_offices_q29 (
    branch_id INT PRIMARY KEY AUTO_INCREMENT,
    branch_name VARCHAR(100) NOT NULL UNIQUE,
    city VARCHAR(100) NOT NULL
);

INSERT INTO branch_offices_q29 (branch_name, city) VALUES
('North Hub', 'Delhi'),
('West Hub', 'Mumbai');

-- Query:
SELECT * FROM branch_offices_q29;

-- Expected Output:
-- Two branch rows.

-- Test Case:
SHOW CREATE TABLE branch_offices_q29;

-- ==========================================================
-- Q30 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- A bridge table stores many-to-many relationships between two entities.

DROP TABLE IF EXISTS employee_skills_q30;
DROP TABLE IF EXISTS skills_q30;
DROP TABLE IF EXISTS employees_q30;

CREATE TABLE employees_q30 (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL
);

CREATE TABLE skills_q30 (
    skill_id INT PRIMARY KEY,
    skill_name VARCHAR(100) NOT NULL
);

CREATE TABLE employee_skills_q30 (
    employee_id INT NOT NULL,
    skill_id INT NOT NULL,
    skill_level VARCHAR(20) NOT NULL,
    PRIMARY KEY (employee_id, skill_id),
    CONSTRAINT fk_es_q30_employee
        FOREIGN KEY (employee_id) REFERENCES employees_q30(employee_id),
    CONSTRAINT fk_es_q30_skill
        FOREIGN KEY (skill_id) REFERENCES skills_q30(skill_id)
);

INSERT INTO employees_q30 VALUES
(1, 'Aarav'),
(2, 'Kabir');

INSERT INTO skills_q30 VALUES
(10, 'MySQL'),
(20, 'Python');

INSERT INTO employee_skills_q30 VALUES
(1, 10, 'ADVANCED'),
(1, 20, 'INTERMEDIATE'),
(2, 10, 'INTERMEDIATE');

-- Query:
SELECT * FROM employee_skills_q30;

-- Expected Output:
-- Three bridge-table rows.

-- Test Case:
SHOW CREATE TABLE employee_skills_q30;

-- ==========================================================
-- Q31 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- This helpdesk table uses defaults for priority, opened time, and status.

DROP TABLE IF EXISTS customer_support_tickets_q31;

CREATE TABLE customer_support_tickets_q31 (
    ticket_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_email VARCHAR(150) NOT NULL,
    subject_line VARCHAR(150) NOT NULL,
    priority_level VARCHAR(20) DEFAULT 'MEDIUM',
    opened_on DATETIME DEFAULT CURRENT_TIMESTAMP,
    ticket_status VARCHAR(20) DEFAULT 'OPEN'
);

INSERT INTO customer_support_tickets_q31
(customer_email, subject_line)
VALUES
('help1@client.com', 'Cannot log in'),
('help2@client.com', 'Invoice missing'),
('help3@client.com', 'Feature request');

-- Query:
SELECT ticket_id, customer_email, priority_level, ticket_status
FROM customer_support_tickets_q31;

-- Expected Output:
-- Three rows with MEDIUM and OPEN defaults.

-- Test Case:
SHOW CREATE TABLE customer_support_tickets_q31;

-- ==========================================================
-- Q32 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- This design combines a unique SKU with a positive price rule.

DROP TABLE IF EXISTS retail_products_q32;

CREATE TABLE retail_products_q32 (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    sku_code VARCHAR(30) UNIQUE NOT NULL,
    product_name VARCHAR(150) NOT NULL,
    selling_price DECIMAL(10,2) NOT NULL,
    CONSTRAINT chk_q32_positive_price CHECK (selling_price > 0)
);

INSERT INTO retail_products_q32
(sku_code, product_name, selling_price)
VALUES
('SKU-A1', 'Wireless Keyboard', 2199.00),
('SKU-B2', 'USB Hub', 899.00);

-- Query:
SELECT * FROM retail_products_q32;

-- Expected Output:
-- Two valid product rows.

-- Test Case:
SHOW CREATE TABLE retail_products_q32;

-- ==========================================================
-- Q33 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- Hospitals act as parents and doctors reference them through a foreign key.

DROP TABLE IF EXISTS doctors_q33;
DROP TABLE IF EXISTS hospitals_q33;

CREATE TABLE hospitals_q33 (
    hospital_id INT PRIMARY KEY,
    hospital_name VARCHAR(150) NOT NULL
);

CREATE TABLE doctors_q33 (
    doctor_id INT PRIMARY KEY,
    doctor_name VARCHAR(150) NOT NULL,
    hospital_id INT NOT NULL,
    CONSTRAINT fk_doctors_q33_hospital
        FOREIGN KEY (hospital_id) REFERENCES hospitals_q33(hospital_id)
);

INSERT INTO hospitals_q33 VALUES
(1, 'City Care'),
(2, 'Metro Health');

INSERT INTO doctors_q33 VALUES
(101, 'Dr. Neha', 1),
(102, 'Dr. Arjun', 2);

-- Query:
SELECT * FROM doctors_q33;

-- Expected Output:
-- Two doctor rows linked to hospitals.

-- Test Case:
SHOW CREATE TABLE doctors_q33;

-- ==========================================================
-- Q34 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- Rename the payment column first, then insert data using the new name.

DROP TABLE IF EXISTS subscription_payments_q34;

CREATE TABLE subscription_payments_q34 (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    subscriber_email VARCHAR(150) NOT NULL,
    payment_mode VARCHAR(30) NOT NULL,
    paid_amount DECIMAL(10,2) NOT NULL,
    paid_on DATE NOT NULL
);

ALTER TABLE subscription_payments_q34
CHANGE payment_mode payment_method VARCHAR(30) NOT NULL;

INSERT INTO subscription_payments_q34
(subscriber_email, payment_method, paid_amount, paid_on)
VALUES
('member1@saas.com', 'CARD', 999.00, '2024-07-01'),
('member2@saas.com', 'UPI', 499.00, '2024-07-02');

-- Query:
SELECT * FROM subscription_payments_q34;

-- Expected Output:
-- Two rows using payment_method.

-- Test Case:
DESCRIBE subscription_payments_q34;

-- ==========================================================
-- Q35 SOLUTION
-- ==========================================================

-- Step-by-step explanation:
-- A composite index on attendance_date and employee_id supports date-first lookup patterns.

DROP TABLE IF EXISTS employee_attendance_log_q35;

CREATE TABLE employee_attendance_log_q35 (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    attendance_status VARCHAR(20) NOT NULL
);

INSERT INTO employee_attendance_log_q35
(employee_id, attendance_date, attendance_status)
VALUES
(1, '2024-07-01', 'PRESENT'),
(2, '2024-07-01', 'ABSENT'),
(1, '2024-07-02', 'PRESENT');

CREATE INDEX idx_q35_attendance_date_employee
ON employee_attendance_log_q35 (attendance_date, employee_id);

-- Query:
SHOW INDEX FROM employee_attendance_log_q35;

-- Expected Output:
-- PRIMARY and idx_q35_attendance_date_employee should be shown.

-- Test Case:
SELECT * FROM employee_attendance_log_q35;
