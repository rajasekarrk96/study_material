/*
============================================================
  MySQL Scalar_Functions - Full Answers
  File: _05_02_Scalar_Functions_Answers.sql
============================================================
  Note: Attempt all questions yourself before reading answers.
  Each answer includes:
    - Full working SQL
    - Step-by-step explanation
    - Dry run through sample data
    - Alternative approach (where applicable)
    - Complexity notes (for advanced queries)
============================================================
*/

-- ============================================================
-- SETUP: Same tables as Questions file
-- ============================================================
DROP DATABASE IF EXISTS mysql_answers;
CREATE DATABASE mysql_answers;
USE mysql_answers;

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dept_id INT NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    bonus DECIMAL(10,2) NULL,
    hire_date DATE NOT NULL,
    manager_id INT NULL,
    email VARCHAR(150) NULL,
    city VARCHAR(50) NULL
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    discount DECIMAL(10,2) NULL,
    stock INT NOT NULL
);

CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    budget DECIMAL(12,2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NULL
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    city VARCHAR(50),
    join_date DATE NOT NULL
);

INSERT INTO employees (emp_id, name, dept_id, salary, bonus, hire_date, manager_id, email, city) VALUES
(101, 'Asha Menon', 40, 52000.75, 2500.00, '2024-01-15', 108, 'asha.menon@gmail.com', ' Mumbai '),
(102, 'Balan Iyer', 10, 78000.40, NULL, '2023-07-10', 109, 'balan.iyer@yahoo.com', 'Chennai'),
(103, 'Meera Joshi', 20, 61000.90, 4000.00, '2022-11-05', 110, 'meera.joshi@gmail.com', 'Bangalore'),
(104, 'Manoj Das', 10, 67000.25, 3500.00, '2021-03-20', 109, 'manoj.das@gmail.com', 'Delhi'),
(105, 'Ravi Shah', 30, 35000.10, NULL, '2025-02-01', 111, 'ravi.shah@company.com', 'Mumbai'),
(106, 'Anita Rao', 40, 49500.55, 1800.00, '2020-09-25', 108, 'anita.rao@company.com', ' Pune '),
(107, 'Kiran Bose', 50, 61500.00, NULL, '2019-04-12', 112, 'kiran.bose@outlook.com', 'Kolkata'),
(108, 'Nisha Kapoor', 40, 90000.00, 7000.00, '2017-09-17', NULL, 'nisha.kapoor@company.com', 'Chennai'),
(109, 'Arjun Sethi', 10, 98000.35, 9000.00, '2016-05-30', NULL, 'arjun.sethi@company.com', 'Bangalore'),
(110, 'Pooja Nair', 20, 93000.10, 8500.00, '2018-12-21', NULL, 'pooja.nair@gmail.com', 'Delhi'),
(111, 'Tarun Malhotra', 30, 88000.65, 6200.00, '2019-06-11', NULL, 'tarun.malhotra@gmail.com', 'Mumbai'),
(112, 'Dev Roy', 50, 91000.50, 5000.00, '2017-01-05', NULL, 'dev.roy@company.com', NULL);

INSERT INTO products (product_id, name, category, price, discount, stock) VALUES
(501, 'Notebook', 'Stationery', 45.75, 5.00, 120),
(502, 'Pen', 'Stationery', 12.40, NULL, 300),
(503, 'Marker', 'Stationery', 35.95, 2.00, 90),
(504, 'Monitor', 'Electronics', 11500.80, 500.00, 10),
(505, 'Keyboard', 'Electronics', 1700.55, 100.00, 40),
(506, 'Water Bottle', 'Kitchen', 250.15, NULL, 0),
(507, 'Printer', 'Electronics', 8900.45, 250.00, 8),
(508, 'Folder', 'Office', 75.60, 3.00, 60),
(509, 'Mouse Pad', 'Accessories', 399.35, 20.00, 150),
(510, 'Desk Organizer', 'Office', 649.95, 15.00, 35),
(511, 'Cable Manager', 'Accessories', 299.45, NULL, 70),
(512, 'Laptop Stand', 'Electronics', 1999.95, 150.00, 25);

INSERT INTO projects (project_id, project_name, budget, start_date, end_date) VALUES
(201, 'Warehouse Automation', 450000.00, '2024-01-01', '2024-12-31'),
(202, 'Mobile Commerce App', 800000.00, '2024-03-15', NULL),
(203, 'Payroll Upgrade', 220000.00, '2023-10-01', '2024-04-30'),
(204, 'Cloud Migration', 1200000.00, '2024-02-10', NULL),
(205, 'Sales Forecasting', 310000.00, '2024-05-01', NULL);

INSERT INTO customers (customer_id, name, email, city, join_date) VALUES
(301, 'Asha Patel', 'asha.patel@gmail.com', 'Mumbai', '2023-01-05'),
(302, 'Rohan Singh', 'rohan.singh@yahoo.com', 'Delhi', '2023-02-17'),
(303, 'Meera Kulkarni', 'meera.kulkarni@gmail.com', 'Bangalore', '2023-03-09'),
(304, 'David Kumar', 'david.kumar@outlook.com', 'Chennai', '2023-05-21'),
(305, 'Priya Menon', 'priya.menon@gmail.com', 'Pune', '2023-06-14'),
(306, 'Aman Batra', 'aman.batra@live.com', 'Delhi', '2023-07-19'),
(307, 'Neha Arora', 'neha.arora@gmail.com', 'Jaipur', '2023-08-11'),
(308, 'Tarun Sethi', 'tarun.sethi@gmail.com', 'Mumbai', '2023-10-03'),
(309, 'Ritika Pal', 'ritika.pal@yahoo.com', 'Kolkata', '2024-01-24'),
(310, 'Manav Kulkarni', 'manav.kulkarni@gmail.com', NULL, '2024-02-16');

-- ============================================================
-- SECTION 1: BASIC ANSWERS
-- ============================================================

/*
  ANS 1. Uppercase Employee Names
  -------------------------------
  Approach:
    Step 1 - Read employee rows.
    Step 2 - Apply UPPER to the name column.
*/
SELECT
    UPPER(name) AS upper_name      -- Convert employee names to uppercase
FROM employees;                    -- Read rows from employees
-- Verify Result:
-- Expected Output:
-- ASHA MENON
-- BALAN IYER

/*
  ANS 2. Lowercase Product Names
  ------------------------------
*/
SELECT
    LOWER(name) AS lower_product_name -- Convert product names to lowercase
FROM products;                        -- Read rows from products
-- Verify Result:
-- Expected Output:
-- notebook
-- pen

/*
  ANS 3. Name Lengths
  -------------------
*/
SELECT
    name,                             -- Show employee name
    LENGTH(name) AS name_length       -- Count byte length of the name
FROM employees;                       -- Read rows from employees
-- Verify Result:
-- Expected Output:
-- Asha Menon, 10

/*
  ANS 4. First Three Characters
  -----------------------------
*/
SELECT
    name,                             -- Show product name
    LEFT(name, 3) AS first_three_chars -- Extract first three characters
FROM products;                        -- Read rows from products
-- Verify Result:
-- Expected Output:
-- Notebook, Not

/*
  ANS 5. Rounded Price
  --------------------
*/
SELECT
    name,                             -- Show product name
    ROUND(price, 1) AS rounded_price  -- Round to 1 decimal place
FROM products;                        -- Read rows from products
-- Verify Result:
-- Expected Output:
-- Notebook, 45.8

/*
  ANS 6. Truncated Price
  ----------------------
*/
SELECT
    name,                                -- Show product name
    TRUNCATE(price, 1) AS truncated_price -- Cut off after 1 decimal place
FROM products;                           -- Read rows from products
-- Verify Result:
-- Expected Output:
-- Notebook, 45.7

/*
  ANS 7. Absolute Value
  ---------------------
*/
SELECT
    ABS(-250) AS absolute_value;      -- Remove the sign from -250
-- Verify Result:
-- Expected Output:
-- 250

/*
  ANS 8. Square Root
  ------------------
*/
SELECT
    SQRT(81) AS square_root_value;    -- Return the square root
-- Verify Result:
-- Expected Output:
-- 9

/*
  ANS 9. Hire Year
  ----------------
*/
SELECT
    name,                             -- Show employee name
    YEAR(hire_date) AS hire_year      -- Extract the year from hire_date
FROM employees;                       -- Read rows from employees
-- Verify Result:
-- Expected Output:
-- Asha Menon, 2024

/*
  ANS 10. Current Date and Time
  -----------------------------
*/
SELECT
    NOW() AS current_datetime;        -- Return current system timestamp
-- Verify Result:
-- Expected Output:
-- Current date and time at execution

-- ============================================================
-- SECTION 2: INTERMEDIATE ANSWERS
-- ============================================================

/*
  ANS 11. Employee Label
  ----------------------
*/
SELECT
    name,                                        -- Show employee name
    CONCAT(name, ' - ', dept_id) AS full_label   -- Build a display label
FROM employees;                                  -- Read rows from employees
-- Verify Result:
-- Expected Output:
-- Asha Menon - 40

/*
  ANS 12. Exact-Length Names
  --------------------------
*/
SELECT
    name                              -- Return employee name
FROM employees                        -- Read rows from employees
WHERE LENGTH(name) = 9;               -- Keep names with exact length 9
-- Verify Result:
-- Expected Output:
-- Anita Rao

/*
  ANS 13. Price Remainder
  -----------------------
*/
SELECT
    name,                             -- Show product name
    MOD(price, 10) AS remainder_value -- Return remainder after division by 10
FROM products;                        -- Read rows from products
-- Verify Result:
-- Expected Output:
-- Notebook, 5.75

/*
  ANS 14. Rounded Salaries
  ------------------------
*/
SELECT
    name,                             -- Show employee name
    ROUND(salary, 0) AS rounded_salary -- Round salary to nearest whole number
FROM employees;                       -- Read rows from employees
-- Verify Result:
-- Expected Output:
-- Asha Menon, 52001

/*
  ANS 15. Greater of Price and Discount
  -------------------------------------
*/
SELECT
    name,                                              -- Show product name
    GREATEST(price, IFNULL(discount, 0)) AS greater_value -- Compare price with safe discount
FROM products;                                         -- Read rows from products
-- Verify Result:
-- Expected Output:
-- Notebook, 45.75

/*
  ANS 16. Smaller of Price and Discount
  -------------------------------------
*/
SELECT
    name,                                           -- Show product name
    LEAST(price, IFNULL(discount, 0)) AS smaller_value -- Compare price with safe discount
FROM products;                                      -- Read rows from products
-- Verify Result:
-- Expected Output:
-- Notebook, 5.00

/*
  ANS 17. Safe Bonus
  ------------------
*/
SELECT
    name,                             -- Show employee name
    IFNULL(bonus, 0) AS bonus_value   -- Replace NULL bonus with 0
FROM employees;                       -- Read rows from employees
-- Verify Result:
-- Expected Output:
-- Balan Iyer, 0

/*
  ANS 18. Total Pay
  -----------------
*/
SELECT
    name,                                      -- Show employee name
    salary + IFNULL(bonus, 0) AS total_pay     -- Safely add salary and bonus
FROM employees;                                -- Read rows from employees
-- Verify Result:
-- Expected Output:
-- Balan Iyer, 78000.40

/*
  ANS 19. Formatted Join Date
  ---------------------------
*/
SELECT
    name,                                                  -- Show employee name
    DATE_FORMAT(hire_date, '%d-%m-%Y') AS formatted_hire_date -- Format hire_date
FROM employees;                                            -- Read rows from employees
-- Verify Result:
-- Expected Output:
-- Asha Menon, 15-01-2024

/*
  ANS 20. Days Since Hire
  -----------------------
  Complexity Note:
    This is row-by-row scalar computation over the scanned rows.
*/
SELECT
    name,                                       -- Show employee name
    DATEDIFF(CURDATE(), hire_date) AS days_since_hire -- Count days from hire date to today
FROM employees;                                 -- Read rows from employees
-- Verify Result:
-- Expected Output:
-- Non-negative day counts

-- ============================================================
-- SECTION 3: ADVANCED ANSWERS
-- ============================================================

/*
  ANS 21. Salary Status
  ---------------------
*/
SELECT
    name,                                               -- Show employee name
    IF(salary >= 60000, 'HIGH', 'NORMAL') AS salary_status -- Two-way status label
FROM employees;                                         -- Read rows from employees
-- Verify Result:
-- Expected Output:
-- Ravi Shah, NORMAL
-- Arjun Sethi, HIGH

/*
  ANS 22. Price After Discount
  ----------------------------
*/
SELECT
    name,                                       -- Show product name
    price - IFNULL(discount, 0) AS price_after_discount -- Subtract safe discount
FROM products;                                  -- Read rows from products
-- Verify Result:
-- Expected Output:
-- Pen, 12.40

/*
  ANS 23. Email Username
  ----------------------
*/
SELECT
    name,                                                   -- Show employee name
    SUBSTRING(email, 1, INSTR(email, '@') - 1) AS first_email_part -- Extract username
FROM employees                                              -- Read rows from employees
WHERE email IS NOT NULL;                                    -- Skip missing emails
-- Verify Result:
-- Expected Output:
-- Asha Menon, asha.menon

/*
  ANS 24. Cleaned City
  --------------------
*/
SELECT
    name,                              -- Show employee name
    TRIM(city) AS cleaned_city         -- Remove surrounding spaces
FROM employees;                        -- Read rows from employees
-- Verify Result:
-- Expected Output:
-- Asha Menon, Mumbai
-- Anita Rao, Pune

/*
  ANS 25. Longest Names First
  ---------------------------
*/
SELECT
    name                               -- Return employee name
FROM employees                         -- Read rows from employees
ORDER BY LENGTH(name) DESC, name ASC;  -- Sort by derived length then by name
-- Verify Result:
-- Expected Output:
-- Longest names first

/*
  ANS 26. Project Start Year
  --------------------------
*/
SELECT
    project_name,                      -- Show project name
    YEAR(start_date) AS project_start_year -- Extract project start year
FROM projects;                         -- Read rows from projects
-- Verify Result:
-- Expected Output:
-- Warehouse Automation, 2024

/*
  ANS 27. Years of Service
  ------------------------
  Dry Run:
    If hire_date is 2016-05-30 and today is later in 2026,
    TIMESTAMPDIFF(YEAR, hire_date, CURDATE()) counts completed years only.
*/
SELECT
    name,                                               -- Show employee name
    TIMESTAMPDIFF(YEAR, hire_date, CURDATE()) AS years_of_service -- Count completed years
FROM employees;                                         -- Read rows from employees
-- Verify Result:
-- Expected Output:
-- One years_of_service value per employee

/*
  ANS 28. City Fallback
  ---------------------
*/
SELECT
    name,                               -- Show customer name
    COALESCE(city, 'Unknown') AS city_fallback -- Replace NULL city with Unknown
FROM customers;                         -- Read rows from customers
-- Verify Result:
-- Expected Output:
-- Manav Kulkarni, Unknown

/*
  ANS 29. Price Band
  ------------------
*/
SELECT
    name,                               -- Show product name
    CASE
        WHEN price < 100 THEN 'BUDGET'  -- Lowest price band
        WHEN price <= 2000 THEN 'MID'   -- Middle price band
        ELSE 'PREMIUM'                  -- Highest price band
    END AS price_band
FROM products;                          -- Read rows from products
-- Verify Result:
-- Expected Output:
-- Pen, BUDGET
-- Monitor, PREMIUM

/*
  ANS 30. Probation End Date
  --------------------------
*/
SELECT
    name,                                                -- Show employee name
    hire_date,                                           -- Show hire date
    DATE_ADD(hire_date, INTERVAL 90 DAY) AS probation_end_date -- Add 90 days
FROM employees;                                          -- Read rows from employees
-- Verify Result:
-- Expected Output:
-- Asha Menon, 2024-01-15, 2024-04-14
