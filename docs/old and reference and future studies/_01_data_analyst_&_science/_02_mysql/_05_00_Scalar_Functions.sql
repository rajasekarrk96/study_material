/*
============================================================
  MySQL Scalar_Functions - Complete Study Notes
  File: _05_00_Scalar_Functions.sql
============================================================
  WHAT YOU WILL LEARN:
  - What scalar functions are and how they differ from aggregate functions
  - String functions such as UPPER, LOWER, LENGTH, CHAR_LENGTH, TRIM,
    CONCAT, CONCAT_WS, SUBSTRING, LEFT, RIGHT, INSTR, LOCATE, and REPLACE
  - Numeric functions such as ROUND, TRUNCATE, CEIL, FLOOR, ABS, MOD,
    POWER, SQRT, GREATEST, and LEAST
  - Date and time functions such as NOW, CURDATE, CURTIME, YEAR, MONTH,
    DATE_FORMAT, DATEDIFF, TIMESTAMPDIFF, DATE_ADD, and DATE_SUB
  - NULL handling with IFNULL, COALESCE, and NULLIF
  - Conditional logic with IF and CASE
  - Real-world reporting use cases, edge cases, and common mistakes
============================================================
*/

-- ============================================================
-- SECTION 1: INTRODUCTION
-- ============================================================
/*
  What is Scalar_Functions?
  -------------------------
  Scalar functions take one input value for a row and return one output value
  for that same row. They do not summarize multiple rows together. Instead,
  they transform, clean, calculate, format, or inspect row-level values.

  Why is it used?
  ---------------
  Real applications and reports rarely display raw data exactly as stored.
  We often need to:
  - show names in uppercase or lowercase
  - round prices for display
  - format dates for reports
  - extract the year from a date
  - replace NULL with fallback values
  - derive a new value such as total pay or price after discount

  Real-world use cases:
  ---------------------
  - Payroll reports: salary + bonus, with NULL bonus treated as 0
  - E-commerce: price after discount and rounded display price
  - CRM: extract email username before @
  - HR: years of service using hire_date
  - Operations: trim bad text input and normalize labels

  Where does it fit in SQL?
  -------------------------
  Scalar functions are mainly used in DQL because they often appear in:
  - SELECT
  - WHERE
  - ORDER BY
  - GROUP BY expressions
  They are also useful in DML statements such as UPDATE.
*/

-- ============================================================
-- SECTION 2: SAMPLE DATABASE SETUP
-- ============================================================
DROP DATABASE IF EXISTS mysql_learning;
CREATE DATABASE mysql_learning;
USE mysql_learning;

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,                    -- Unique department identifier
    dept_name VARCHAR(50) NOT NULL,            -- Department name
    location VARCHAR(50) NOT NULL              -- Department location
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,                    -- Unique employee identifier
    name VARCHAR(100) NOT NULL,                -- Employee full name
    dept_id INT NOT NULL,                      -- Department reference
    salary DECIMAL(10,2) NOT NULL,             -- Base salary
    bonus DECIMAL(10,2) NULL,                  -- Bonus, may be missing
    hire_date DATE NOT NULL,                   -- Hiring date
    manager_id INT NULL,                       -- Manager reference if known
    email VARCHAR(150) NULL,                   -- Employee email
    city VARCHAR(50) NULL,                     -- City, sometimes messy or missing
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

CREATE TABLE projects (
    project_id INT PRIMARY KEY,                -- Unique project identifier
    project_name VARCHAR(100) NOT NULL,        -- Project name
    budget DECIMAL(12,2) NOT NULL,             -- Project budget
    start_date DATE NOT NULL,                  -- Start date
    end_date DATE NULL                         -- End date if closed
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,               -- Unique customer identifier
    name VARCHAR(100) NOT NULL,                -- Customer name
    email VARCHAR(150) UNIQUE,                 -- Customer email
    city VARCHAR(50),                          -- Customer city
    join_date DATE NOT NULL                    -- Join date
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,                  -- Unique order identifier
    customer_id INT NOT NULL,                  -- Customer who placed the order
    order_date DATETIME NOT NULL,              -- Order timestamp
    total_amount DECIMAL(10,2) NOT NULL,       -- Order total
    status VARCHAR(20) NOT NULL,               -- Order status
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,                -- Unique product identifier
    name VARCHAR(100) NOT NULL,                -- Product name
    category VARCHAR(50) NOT NULL,             -- Product category
    price DECIMAL(10,2) NOT NULL,              -- Selling price
    discount DECIMAL(10,2) NULL,               -- Discount amount
    stock INT NOT NULL                         -- Current stock quantity
);

INSERT INTO departments (dept_id, dept_name, location) VALUES
(10, 'Engineering', 'Bangalore'),
(20, 'Finance', 'Delhi'),
(30, 'Sales', 'Mumbai'),
(40, 'Human Resources', 'Chennai'),
(50, 'Operations', 'Hyderabad');

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

INSERT INTO projects (project_id, project_name, budget, start_date, end_date) VALUES
(201, 'Warehouse Automation', 450000.00, '2024-01-01', '2024-12-31'),
(202, 'Mobile Commerce App', 800000.00, '2024-03-15', NULL),
(203, 'Payroll Upgrade', 220000.00, '2023-10-01', '2024-04-30'),
(204, 'Cloud Migration', 1200000.00, '2024-02-10', NULL),
(205, 'Sales Forecasting', 310000.00, '2024-05-01', NULL),
(206, 'Data Governance', 275000.00, '2024-06-01', NULL),
(207, 'Campus Hiring Drive', 90000.00, '2024-07-01', '2024-09-15'),
(208, 'Regional Expansion', 650000.00, '2024-08-01', NULL),
(209, 'Inventory Cleanup', 145000.00, '2024-01-20', '2024-06-30'),
(210, 'Finance Dashboard', 260000.00, '2024-04-05', NULL);

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
(310, 'Manav Kulkarni', 'manav.kulkarni@gmail.com', NULL, '2024-02-16'),
(311, 'Ira Bansal', 'ira.bansal@gmail.com', 'Noida', '2024-03-10'),
(312, 'Kunal Roy', 'kunal.roy@outlook.com', 'Bangalore', '2024-04-12');

INSERT INTO orders (order_id, customer_id, order_date, total_amount, status) VALUES
(401, 301, '2024-04-01 09:15:00', 3499.00, 'Delivered'),
(402, 302, '2024-04-02 10:45:00', 899.00, 'Pending'),
(403, 303, '2024-04-03 14:30:00', 15999.00, 'Delivered'),
(404, 304, '2024-04-04 17:05:00', 2299.00, 'Cancelled'),
(405, 305, '2024-04-05 11:20:00', 4999.00, 'Shipped'),
(406, 306, '2024-04-06 13:50:00', 1249.00, 'Delivered'),
(407, 307, '2024-04-07 16:10:00', 799.00, 'Pending'),
(408, 308, '2024-04-08 18:40:00', 18999.00, 'Delivered'),
(409, 309, '2024-04-09 12:05:00', 999.00, 'Returned'),
(410, 310, '2024-04-10 08:55:00', 2750.00, 'Delivered'),
(411, 311, '2024-04-11 15:35:00', 6499.00, 'Shipped'),
(412, 312, '2024-04-12 19:25:00', 1599.00, 'Pending');

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

-- ============================================================
-- CONCEPT: WHAT MAKES A FUNCTION SCALAR
-- ============================================================
/*
  Explanation:
  ------------
  A scalar function works on one input row value at a time and returns one
  output value for that row. It does not collapse many rows into one summary.

  Syntax:
  -------
  SELECT function_name(column_name)
  FROM table_name;

  Common Mistake:
  ---------------
  Confusing scalar functions like UPPER() or ROUND() with aggregate functions
  like SUM() or AVG().
*/

-- Example: Scalar function returns one transformed value per employee
SELECT
    emp_id,                         -- Show employee id
    name,                           -- Show original employee name
    UPPER(name) AS upper_name       -- Convert the same row value to uppercase
FROM employees;                     -- Read rows from employees
-- Expected Output: One output row per employee with upper_name added

-- Edge Case: Aggregate function reduces many rows to one result
SELECT
    AVG(salary) AS average_salary   -- Summarize many salary rows into one value
FROM employees;                     -- Read rows from employees
-- Expected Output: A single average_salary row

-- ============================================================
-- CONCEPT: STRING FUNCTIONS - UPPER AND LOWER
-- ============================================================
/*
  Explanation:
  ------------
  UPPER converts text to uppercase and LOWER converts text to lowercase.
  These are useful for display normalization and consistent comparisons.

  Syntax:
  -------
  UPPER(text_expression)
  LOWER(text_expression)

  Common Mistake:
  ---------------
  Assuming these functions change stored data permanently. They only change
  query output unless used inside UPDATE.
*/

-- Example: Show names in multiple text forms
SELECT
    name,                           -- Show original name
    UPPER(name) AS upper_name,      -- Convert to uppercase
    LOWER(name) AS lower_name       -- Convert to lowercase
FROM employees;                     -- Read rows from employees
-- Expected Output: Original, uppercase, and lowercase versions of each name

-- Edge Case: Apply LOWER to email for case-normalized reporting
SELECT
    email,                          -- Show original email
    LOWER(email) AS lower_email     -- Convert email to lowercase
FROM customers;                     -- Read rows from customers
-- Expected Output: Email addresses displayed in lowercase

-- ============================================================
-- CONCEPT: STRING FUNCTIONS - LENGTH AND CHAR_LENGTH
-- ============================================================
/*
  Explanation:
  ------------
  LENGTH returns byte length, while CHAR_LENGTH returns character count.
  For plain English text they often look the same, but they are not identical.

  Syntax:
  -------
  LENGTH(text_expression)
  CHAR_LENGTH(text_expression)

  Common Mistake:
  ---------------
  Using LENGTH when you really want number of characters rather than bytes.
*/

-- Example: Show string length information for product names
SELECT
    name,                                      -- Show product name
    LENGTH(name) AS byte_length,               -- Show byte length
    CHAR_LENGTH(name) AS character_count       -- Show character count
FROM products;                                 -- Read rows from products
-- Expected Output: One row per product with both length measurements

-- Edge Case: Use LENGTH inside WHERE
SELECT
    name                                       -- Return product name only
FROM products                                  -- Read rows from products
WHERE LENGTH(name) = 3;                        -- Keep names that are exactly 3 bytes long
-- Expected Output: Pen

-- ============================================================
-- CONCEPT: STRING FUNCTIONS - TRIM, LTRIM, RTRIM
-- ============================================================
/*
  Explanation:
  ------------
  TRIM removes spaces from both ends, LTRIM removes left spaces, and RTRIM
  removes right spaces. This is important when imported data contains extra
  whitespace.

  Syntax:
  -------
  TRIM(text_expression)
  LTRIM(text_expression)
  RTRIM(text_expression)

  Common Mistake:
  ---------------
  Forgetting that extra spaces can break comparisons and display quality.
*/

-- Example: Clean employee city values
SELECT
    name,                               -- Show employee name
    city,                               -- Show original city text
    TRIM(city) AS cleaned_city,         -- Remove spaces from both ends
    LTRIM(city) AS left_trimmed_city,   -- Remove spaces from the left
    RTRIM(city) AS right_trimmed_city   -- Remove spaces from the right
FROM employees;                         -- Read rows from employees
-- Expected Output: Messy city values become cleaner display values

-- Edge Case: TRIM a custom character
SELECT
    TRIM('_' FROM '_mysql_') AS custom_trimmed_text; -- Remove underscore from both ends
-- Expected Output: mysql

-- ============================================================
-- CONCEPT: STRING FUNCTIONS - CONCAT AND CONCAT_WS
-- ============================================================
/*
  Explanation:
  ------------
  CONCAT joins expressions directly, while CONCAT_WS joins them using a chosen
  separator. These are useful for labels and formatted report output.

  Syntax:
  -------
  CONCAT(value1, value2, ...)
  CONCAT_WS(separator, value1, value2, ...)

  Common Mistake:
  ---------------
  Forgetting that CONCAT can become NULL if any argument is NULL in some SQL
  dialects. In MySQL, CONCAT returns NULL if any argument is NULL.
*/

-- Example: Create readable employee labels
SELECT
    name,                                                -- Show employee name
    CONCAT(name, ' - ', dept_id) AS simple_label,        -- Build a simple label
    CONCAT_WS(' | ', name, TRIM(city), email) AS rich_label -- Build a separator-based label
FROM employees;                                          -- Read rows from employees
-- Expected Output: One label-oriented row per employee

-- Edge Case: CONCAT with a NULL expression
SELECT
    name,                                           -- Show employee name
    CONCAT(name, ' / ', city) AS risky_concat       -- CONCAT returns NULL if city is NULL
FROM employees;                                     -- Read rows from employees
-- Expected Output: Dev Roy may show NULL in risky_concat because city is NULL

-- ============================================================
-- CONCEPT: STRING FUNCTIONS - SUBSTRING, LEFT, RIGHT
-- ============================================================
/*
  Explanation:
  ------------
  SUBSTRING extracts a portion of text. LEFT takes the first N characters.
  RIGHT takes the last N characters. MySQL positions begin at 1, not 0.

  Syntax:
  -------
  SUBSTRING(text_expression, start_position, length)
  LEFT(text_expression, number_of_characters)
  RIGHT(text_expression, number_of_characters)

  Common Mistake:
  ---------------
  Assuming string positions start at 0 as they do in many programming languages.
*/

-- Example: Extract pieces of product names
SELECT
    name,                                     -- Show original product name
    SUBSTRING(name, 1, 4) AS first_four,      -- Extract first four characters
    LEFT(name, 3) AS left_three,              -- Take first three characters
    RIGHT(name, 3) AS right_three             -- Take last three characters
FROM products;                                -- Read rows from products
-- Expected Output: Product names split into several useful fragments

-- Edge Case: Extract exact email username before @
SELECT
    name,                                     -- Show employee name
    email,                                    -- Show original email
    SUBSTRING(email, 1, INSTR(email, '@') - 1) AS email_user_name -- Extract username
FROM employees                                -- Read rows from employees
WHERE email IS NOT NULL;                      -- Skip rows without email
-- Expected Output: Employee email prefixes before the @ symbol

-- ============================================================
-- CONCEPT: STRING FUNCTIONS - INSTR, LOCATE, POSITION, REPLACE
-- ============================================================
/*
  Explanation:
  ------------
  INSTR and LOCATE return the position of a substring. REPLACE swaps one text
  sequence for another throughout the string.

  Syntax:
  -------
  INSTR(string, substring)
  LOCATE(substring, string)
  POSITION(substring IN string)
  REPLACE(string, search_text, replacement_text)

  Common Mistake:
  ---------------
  Forgetting that these position functions return 0 when the substring is not found.
*/

-- Example: Inspect and modify text
SELECT
    email,                                         -- Show original email
    INSTR(email, '@') AS at_sign_position,         -- Position of @
    LOCATE('.', email) AS first_dot_position,      -- Position of first dot
    REPLACE(email, '.', '_') AS underscored_email  -- Replace dots with underscores
FROM employees                                     -- Read rows from employees
WHERE email IS NOT NULL;                           -- Skip missing email values
-- Expected Output: Email position metadata and transformed text

-- Edge Case: Direct position calls on literals
SELECT
    INSTR('rajasekar', 'se') AS instr_pos,         -- Find substring position using INSTR
    LOCATE('ase', 'database') AS locate_pos,       -- Find substring position using LOCATE
    POSITION('ta' IN 'database') AS position_pos;  -- Find substring position using POSITION
-- Expected Output: Position numbers for each search

-- ============================================================
-- CONCEPT: NUMERIC FUNCTIONS - ROUND AND TRUNCATE
-- ============================================================
/*
  Explanation:
  ------------
  ROUND changes the last retained digit based on the next digit.
  TRUNCATE simply cuts off digits beyond the chosen precision.

  Syntax:
  -------
  ROUND(number_expression, decimal_places)
  TRUNCATE(number_expression, decimal_places)

  Common Mistake:
  ---------------
  Thinking TRUNCATE rounds values. It does not.
*/

-- Example: Show rounded and truncated product prices
SELECT
    name,                                      -- Show product name
    price,                                     -- Show original price
    ROUND(price, 1) AS rounded_price,          -- Round to 1 decimal place
    TRUNCATE(price, 1) AS truncated_price      -- Cut off after 1 decimal place
FROM products;                                 -- Read rows from products
-- Expected Output: One row per product showing different numeric handling

-- Edge Case: Round salary to a whole number
SELECT
    name,                                      -- Show employee name
    salary,                                    -- Show original salary
    ROUND(salary, 0) AS rounded_salary         -- Round to nearest integer
FROM employees;                                -- Read rows from employees
-- Expected Output: Rounded salary values with no decimal digits

-- ============================================================
-- CONCEPT: NUMERIC FUNCTIONS - CEIL, FLOOR, ABS, MOD
-- ============================================================
/*
  Explanation:
  ------------
  CEIL goes upward to the nearest integer.
  FLOOR goes downward to the nearest integer.
  ABS removes the sign from a number.
  MOD returns the remainder after division.

  Syntax:
  -------
  CEIL(number_expression)
  FLOOR(number_expression)
  ABS(number_expression)
  MOD(number_expression, divisor)

  Common Mistake:
  ---------------
  Confusing remainder logic with decimal truncation.
*/

-- Example: Numeric behavior on product prices
SELECT
    name,                                  -- Show product name
    price,                                 -- Show original price
    CEIL(price) AS ceiling_price,          -- Round upward to next integer
    FLOOR(price) AS floor_price,           -- Round downward to previous integer
    MOD(price, 10) AS remainder_value      -- Remainder after dividing by 10
FROM products;                             -- Read rows from products
-- Expected Output: Numeric function values per product

-- Edge Case: ABS on a negative literal
SELECT
    ABS(-250) AS absolute_value;           -- Remove the negative sign
-- Expected Output: 250

-- ============================================================
-- CONCEPT: NUMERIC FUNCTIONS - POWER, SQRT, GREATEST, LEAST
-- ============================================================
/*
  Explanation:
  ------------
  POWER raises a number to a power. SQRT returns the square root.
  GREATEST returns the largest value among arguments.
  LEAST returns the smallest value among arguments.

  Syntax:
  -------
  POWER(base, exponent)
  SQRT(number_expression)
  GREATEST(value1, value2, ...)
  LEAST(value1, value2, ...)

  Common Mistake:
  ---------------
  Forgetting to protect nullable arguments before GREATEST or LEAST comparisons.
*/

-- Example: Compare price and discount
SELECT
    name,                                               -- Show product name
    price,                                              -- Show price
    discount,                                           -- Show discount
    GREATEST(price, IFNULL(discount, 0)) AS greater_value, -- Largest value
    LEAST(price, IFNULL(discount, 0)) AS smaller_value     -- Smallest value
FROM products;                                          -- Read rows from products
-- Expected Output: One row per product comparing price and discount

-- Edge Case: Direct mathematical expressions
SELECT
    POWER(3, 4) AS three_to_the_power_of_four,          -- Raise 3 to the power of 4
    SQRT(81) AS square_root_of_81;                      -- Take square root of 81
-- Expected Output: 81 and 9

-- ============================================================
-- CONCEPT: DATE AND TIME FUNCTIONS - NOW, CURDATE, CURTIME
-- ============================================================
/*
  Explanation:
  ------------
  NOW returns the current date and time.
  CURDATE returns the current date only.
  CURTIME returns the current time only.

  Syntax:
  -------
  NOW()
  CURDATE()
  CURTIME()

  Common Mistake:
  ---------------
  Mixing DATE, DATETIME, and TIME expectations in the same output.
*/

-- Example: Show current time-related values
SELECT
    NOW() AS current_timestamp_value,   -- Current system date and time
    CURDATE() AS current_date_value,    -- Current date only
    CURTIME() AS current_time_value;    -- Current time only
-- Expected Output: One row showing timestamp, date, and time

-- ============================================================
-- CONCEPT: DATE AND TIME FUNCTIONS - YEAR, MONTH, DATE_FORMAT
-- ============================================================
/*
  Explanation:
  ------------
  YEAR extracts the year number from a date. MONTH extracts the month number.
  DATE_FORMAT displays a date in a chosen textual format.

  Syntax:
  -------
  YEAR(date_expression)
  MONTH(date_expression)
  DATE_FORMAT(date_expression, format_mask)

  Common Mistake:
  ---------------
  Assuming DATE_FORMAT changes stored data. It changes only the displayed result.
*/

-- Example: Break hire_date into useful reporting pieces
SELECT
    name,                                                 -- Show employee name
    hire_date,                                            -- Show original hire date
    YEAR(hire_date) AS hire_year,                         -- Extract hire year
    MONTH(hire_date) AS hire_month,                       -- Extract hire month number
    DATE_FORMAT(hire_date, '%d-%m-%Y') AS formatted_hire_date -- Show a readable date format
FROM employees;                                           -- Read rows from employees
-- Expected Output: Date parts and formatted date per employee

-- Edge Case: Format order timestamp for business display
SELECT
    order_id,                                             -- Show order id
    order_date,                                           -- Show original timestamp
    DATE_FORMAT(order_date, '%d-%m-%Y %H:%i') AS order_label -- Format timestamp
FROM orders;                                              -- Read rows from orders
-- Expected Output: Order timestamps in readable report form

-- ============================================================
-- CONCEPT: DATE FUNCTIONS - DATEDIFF, TIMESTAMPDIFF, DATE_ADD, DATE_SUB
-- ============================================================
/*
  Explanation:
  ------------
  DATEDIFF returns day difference between two dates.
  TIMESTAMPDIFF returns differences in a chosen unit such as YEAR or MONTH.
  DATE_ADD and DATE_SUB shift dates forward or backward.

  Syntax:
  -------
  DATEDIFF(date1, date2)
  TIMESTAMPDIFF(unit, start_date, end_date)
  DATE_ADD(date_expression, INTERVAL n unit)
  DATE_SUB(date_expression, INTERVAL n unit)

  Common Mistake:
  ---------------
  Reversing argument order in DATEDIFF and getting negative results unexpectedly.
*/

-- Example: Tenure and date shifting for employees
SELECT
    name,                                                       -- Show employee name
    hire_date,                                                  -- Show original hire date
    DATEDIFF(CURDATE(), hire_date) AS days_since_hire,          -- Count days from hire_date to today
    TIMESTAMPDIFF(YEAR, hire_date, CURDATE()) AS years_of_service, -- Count completed years
    DATE_ADD(hire_date, INTERVAL 90 DAY) AS probation_end_date, -- Add 90 days
    DATE_SUB(hire_date, INTERVAL 1 MONTH) AS one_month_before_hire -- Subtract one month
FROM employees;                                                 -- Read rows from employees
-- Expected Output: Several date calculations per employee

-- Edge Case: Compare two fixed dates
SELECT
    DATEDIFF('2024-04-10', '2024-04-01') AS day_difference;     -- Difference in days
-- Expected Output: 9

-- ============================================================
-- CONCEPT: NULL HANDLING - IFNULL, COALESCE, NULLIF
-- ============================================================
/*
  Explanation:
  ------------
  IFNULL replaces NULL with a fallback value.
  COALESCE returns the first non-NULL value from a list.
  NULLIF returns NULL if two expressions are equal, otherwise it returns the first one.

  Syntax:
  -------
  IFNULL(value, fallback)
  COALESCE(value1, value2, ...)
  NULLIF(expression1, expression2)

  Common Mistake:
  ---------------
  Forgetting that arithmetic with NULL usually returns NULL unless you handle it.
*/

-- Example: Bonus handling and safe total pay
SELECT
    name,                                                  -- Show employee name
    salary,                                                -- Show salary
    bonus,                                                 -- Show original bonus
    IFNULL(bonus, 0) AS bonus_with_zero,                   -- Replace NULL bonus with 0
    COALESCE(bonus, 0) AS bonus_with_zero_via_coalesce,    -- Do the same through COALESCE
    salary + IFNULL(bonus, 0) AS total_pay                 -- Safely add salary and bonus
FROM employees;                                            -- Read rows from employees
-- Expected Output: No NULL total_pay values even when bonus is missing

-- Edge Case: NULLIF to suppress a repeated value
SELECT
    name,                                                  -- Show employee name
    city,                                                  -- Show city
    NULLIF(TRIM(city), 'Mumbai') AS null_if_mumbai         -- Return NULL when city is Mumbai
FROM employees;                                            -- Read rows from employees
-- Expected Output: Mumbai becomes NULL in the derived column; other cities remain unchanged

-- ============================================================
-- CONCEPT: CONDITIONAL LOGIC - IF AND CASE
-- ============================================================
/*
  Explanation:
  ------------
  IF is MySQL-specific shorthand for a simple condition.
  CASE is standard SQL and is better when many branches exist.

  Syntax:
  -------
  IF(condition, true_result, false_result)

  CASE
      WHEN condition THEN result
      WHEN condition THEN result
      ELSE result
  END

  Common Mistake:
  ---------------
  Using nested IF repeatedly when CASE would be clearer.
*/

-- Example: Salary band and stock band labels
SELECT
    name,                                                   -- Show employee name
    salary,                                                 -- Show salary
    IF(salary >= 60000, 'HIGH', 'NORMAL') AS salary_status  -- Build a simple two-way status
FROM employees;                                             -- Read rows from employees
-- Expected Output: Employees labelled HIGH or NORMAL

-- Edge Case: Multi-branch stock logic with CASE
SELECT
    name,                                                   -- Show product name
    stock,                                                  -- Show stock quantity
    CASE
        WHEN stock = 0 THEN 'OUT OF STOCK'                  -- Exact zero stock case
        WHEN stock < 20 THEN 'LOW STOCK'                    -- Low stock warning
        ELSE 'AVAILABLE'                                    -- Default category
    END AS stock_status
FROM products;                                              -- Read rows from products
-- Expected Output: Each product labelled by stock condition

-- ============================================================
-- CONCEPT: USING FUNCTIONS IN WHERE AND ORDER BY
-- ============================================================
/*
  Explanation:
  ------------
  Scalar functions can appear in WHERE and ORDER BY as well as SELECT.
  This lets us filter or sort using derived logic.

  Syntax:
  -------
  WHERE function_name(column_name) = value
  ORDER BY function_name(column_name)

  Common Mistake:
  ---------------
  Forgetting that function-wrapped columns may affect index usage.
*/

-- Example: Filter names by their length
SELECT
    name                                           -- Return employee name
FROM employees                                     -- Read rows from employees
WHERE LENGTH(name) = 9;                            -- Keep names with exact length 9
-- Expected Output: Names having length 9

-- Edge Case: Sort by name length descending
SELECT
    name                                           -- Return employee name
FROM employees                                     -- Read rows from employees
ORDER BY LENGTH(name) DESC, name ASC;              -- Sort by derived length first
-- Expected Output: Longest employee names first

-- ============================================================
-- CONCEPT: COMMON MISTAKES AND EDGE CASES
-- ============================================================
/*
  Explanation:
  ------------
  Scalar functions are powerful, but several beginner errors appear often:
  - forgetting NULL handling in arithmetic
  - confusing ROUND and TRUNCATE
  - using LENGTH instead of CHAR_LENGTH without thinking
  - forgetting string positions start at 1 in MySQL
  - assuming display formatting changes stored values

  Syntax:
  -------
  No single syntax; this section demonstrates caution cases.

  Common Mistake:
  ---------------
  Writing salary + bonus and expecting a number even when bonus is NULL.
*/

-- Example: Broken arithmetic because NULL propagates
SELECT
    name,                                -- Show employee name
    salary,                              -- Show salary
    bonus,                               -- Show bonus
    salary + bonus AS broken_total_pay   -- NULL bonus makes the total NULL
FROM employees;                          -- Read rows from employees
-- Expected Output: Rows with NULL bonus show NULL broken_total_pay

-- Edge Case: Corrected arithmetic with IFNULL
SELECT
    name,                                           -- Show employee name
    salary,                                         -- Show salary
    bonus,                                          -- Show bonus
    salary + IFNULL(bonus, 0) AS corrected_total_pay -- Replace NULL bonus before addition
FROM employees;                                     -- Read rows from employees
-- Expected Output: Every row shows a usable corrected_total_pay

-- ============================================================
-- CONCEPT: REAL-WORLD EXAMPLES AND INTERVIEW TIPS
-- ============================================================
/*
  Explanation:
  ------------
  Interview questions often ask:
  - What is the difference between scalar and aggregate functions?
  - Why does salary + bonus become NULL?
  - What is the difference between ROUND and TRUNCATE?
  - What is the difference between IF and CASE?

  Real-world examples:
  --------------------
  - Payroll report with total pay
  - Product display with discount-adjusted price
  - Employee tenure report with years of service
  - Email parsing for CRM exports
*/

-- Example: Payroll-style report
SELECT
    UPPER(name) AS employee_name,                      -- Normalize name for report display
    TRIM(city) AS cleaned_city,                        -- Clean spacing in city text
    salary,                                            -- Show original salary
    IFNULL(bonus, 0) AS safe_bonus,                    -- Replace missing bonus with 0
    ROUND(salary + IFNULL(bonus, 0), 2) AS total_pay, -- Compute final pay safely
    DATE_FORMAT(hire_date, '%b %d, %Y') AS hire_label  -- Build a friendly hire date label
FROM employees                                         -- Read rows from employees
ORDER BY LENGTH(name) DESC;                            -- Show longest names first
-- Expected Output: A report-friendly payroll result set
