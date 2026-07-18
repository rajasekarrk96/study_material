-- ############################################################
-- FILE: 04_MySQL_Patterns_Sets_Notes.sql
-- ############################################################

/*
============================================================
  MySQL Patterns_Sets - Complete Study Notes
  File: 04_MySQL_Patterns_Sets_Notes.sql
============================================================
  WHAT YOU WILL LEARN:
  - Pattern matching with LIKE, NOT LIKE, wildcards, and ESCAPE
  - Advanced pattern matching with REGEXP and MySQL regex behavior
  - Range filtering with BETWEEN and NOT BETWEEN
  - List filtering with IN and NOT IN
  - NULL behavior in pattern and set filters
  - Combining filters with comparison and logical operators
  - DISTINCT versus GROUP BY for uniqueness
  - Set operations with UNION, UNION ALL, INTERSECT, and EXCEPT
  - MySQL version notes for INTERSECT and EXCEPT
  - Ordering and limiting filtered result sets
  - Grouped filtering with HAVING where relevant
  - Joins and subqueries used with pattern and set filters
  - Edge cases, common mistakes, performance notes, and interview tips
============================================================
*/

-- ============================================================
-- SECTION 1: INTRODUCTION
-- ============================================================
/*
  What is Patterns_Sets?
  ----------------------
  This topic covers how to search for rows when the match is not a simple
  exact equality. In real SQL work, users do not always search for a full
  value. They may search for:
  - names that start with A
  - emails that end with gmail.com
  - prices inside a specific range
  - rows whose values belong to a small list
  - rows that come from combining two result sets

  Why is it used?
  ---------------
  Exact matching with = is important, but not sufficient for practical work.
  We often need to:
  - filter by bands such as salary, price, or date range
  - filter by a list of statuses, categories, or cities
  - search partial text values
  - merge result sets from multiple tables or queries

  Real-world use cases:
  ---------------------
  - E-commerce: find products priced between 500 and 5000
  - HR: find employees in Mumbai, Delhi, or Bangalore
  - CRM: find customers whose email contains gmail
  - Reporting: merge current and archived customer lists
  - Audit: exclude rows from blocked cities or statuses

  Where does it fit in SQL?
  -------------------------
  This topic belongs mainly to DQL because it focuses on querying data with
  SELECT. It especially uses:
  - WHERE
  - HAVING
  - ORDER BY
  - LIMIT
  - UNION / UNION ALL / INTERSECT / EXCEPT
*/

-- ============================================================
-- SECTION 2: SAMPLE DATABASE SETUP
-- ============================================================
-- Recreate the learning database from scratch for a clean run.
DROP DATABASE IF EXISTS mysql_learning;

-- Create the database used throughout this notes file.
CREATE DATABASE mysql_learning;

-- Switch to the learning database.
USE mysql_learning;

-- Create the departments table for employee-based examples.
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,                    -- Unique department identifier
    dept_name VARCHAR(50) NOT NULL,            -- Department name
    location VARCHAR(50) NOT NULL              -- Main department location
);

-- Create the employees table for filtering and text-search examples.
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,                    -- Unique employee identifier
    name VARCHAR(100) NOT NULL,                -- Employee full name
    dept_id INT NOT NULL,                      -- Department reference
    salary DECIMAL(10,2) NOT NULL,             -- Current salary
    hire_date DATE NOT NULL,                   -- Hiring date
    manager_id INT NULL,                       -- Reporting manager if available
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- Create the projects table for list and range filters.
CREATE TABLE projects (
    project_id INT PRIMARY KEY,                -- Unique project identifier
    project_name VARCHAR(100) NOT NULL,        -- Project name
    budget DECIMAL(12,2) NOT NULL,             -- Approved budget
    start_date DATE NOT NULL,                  -- Project start date
    end_date DATE NULL                         -- Project end date if completed
);

-- Create the employee-project mapping table.
CREATE TABLE emp_projects (
    emp_id INT NOT NULL,                       -- Employee participating in project
    project_id INT NOT NULL,                   -- Project worked on
    role VARCHAR(50) NOT NULL,                 -- Employee role on project
    PRIMARY KEY (emp_id, project_id),          -- Prevent duplicate assignments
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Create the customers table for email and city pattern searches.
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,               -- Unique customer identifier
    name VARCHAR(100) NOT NULL,                -- Customer full name
    email VARCHAR(150) UNIQUE,                 -- Email address
    city VARCHAR(50),                          -- Customer city, may be NULL
    join_date DATE NOT NULL                    -- Registration date
);

-- Create the orders table for date and status filters.
CREATE TABLE orders (
    order_id INT PRIMARY KEY,                  -- Unique order identifier
    customer_id INT NOT NULL,                  -- Customer who placed the order
    order_date DATE NOT NULL,                  -- Order date
    total_amount DECIMAL(10,2) NOT NULL,       -- Full order amount
    status VARCHAR(20) NOT NULL,               -- Current order status
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create the products table for price bands and product-name searches.
CREATE TABLE products (
    product_id INT PRIMARY KEY,                -- Unique product identifier
    name VARCHAR(100) NOT NULL,                -- Product name
    category VARCHAR(50) NOT NULL,             -- Product category
    price DECIMAL(10,2) NOT NULL,              -- Current selling price
    stock INT NOT NULL                         -- Quantity available
);

-- Create the order_items table for combined query examples.
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,             -- Unique order item identifier
    order_id INT NOT NULL,                     -- Parent order
    product_id INT NOT NULL,                   -- Product sold
    quantity INT NOT NULL,                     -- Quantity sold
    unit_price DECIMAL(10,2) NOT NULL,         -- Price at time of order
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create helper tables for set operation demonstrations.
CREATE TABLE current_customers (
    customer_name VARCHAR(100) NOT NULL,       -- Current customer name snapshot
    city VARCHAR(50) NOT NULL                  -- Current customer city snapshot
);

-- Create helper archive table for set operation demonstrations.
CREATE TABLE archived_customers (
    customer_name VARCHAR(100) NOT NULL,       -- Historical customer name snapshot
    city VARCHAR(50) NOT NULL                  -- Historical customer city snapshot
);

-- Insert department seed data.
INSERT INTO departments (dept_id, dept_name, location) VALUES
(10, 'Engineering', 'Bangalore'),
(20, 'Finance', 'Delhi'),
(30, 'Sales', 'Mumbai'),
(40, 'Human Resources', 'Chennai'),
(50, 'Operations', 'Hyderabad');

-- Insert employee seed data.
INSERT INTO employees (emp_id, name, dept_id, salary, hire_date, manager_id) VALUES
(101, 'Asha Menon', 40, 52000.00, '2021-02-10', 108),
(102, 'Balan Iyer', 10, 78000.00, '2020-08-14', 109),
(103, 'Meera Joshi', 20, 68000.00, '2019-11-03', 110),
(104, 'Manoj Das', 10, 84500.00, '2022-01-19', 109),
(105, 'Ravi Shah', 30, 47000.00, '2023-03-12', 111),
(106, 'Anita Rao', 40, 49500.00, '2021-07-08', 108),
(107, 'Kiran Bose', 50, 61500.00, '2018-04-26', 112),
(108, 'Nisha Kapoor', 40, 90000.00, '2017-09-17', NULL),
(109, 'Arjun Sethi', 10, 98000.00, '2016-05-30', NULL),
(110, 'Pooja Nair', 20, 93000.00, '2018-12-21', NULL),
(111, 'Tarun Malhotra', 30, 88000.00, '2019-06-11', NULL),
(112, 'Dev Roy', 50, 91000.00, '2017-01-05', NULL);

-- Insert project seed data.
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

-- Insert employee-project seed data.
INSERT INTO emp_projects (emp_id, project_id, role) VALUES
(101, 202, 'Architect'),
(102, 202, 'Backend Developer'),
(103, 207, 'Recruiter'),
(104, 210, 'Business Analyst'),
(105, 205, 'Sales Analyst'),
(106, 208, 'Account Executive'),
(107, 201, 'Operations Coordinator'),
(108, 207, 'HR Lead'),
(109, 210, 'Finance Lead'),
(110, 205, 'Sales Director'),
(111, 201, 'Program Manager'),
(112, 202, 'Frontend Developer');

-- Insert customer seed data.
INSERT INTO customers (customer_id, name, email, city, join_date) VALUES
(301, 'Asha Patel', 'asha.patel@gmail.com', 'Mumbai', '2023-01-05'),
(302, 'Rohan Singh', 'rohan.singh@yahoo.com', 'Delhi', '2023-02-17'),
(303, 'Meera Joshi', 'meera.joshi@gmail.com', 'Bangalore', '2023-03-09'),
(304, 'David Kumar', 'david.kumar@outlook.com', 'Chennai', '2023-05-21'),
(305, 'Priya Menon', 'priya.menon@gmail.com', 'Pune', '2023-06-14'),
(306, 'Aman Batra', 'aman.batra@live.com', 'Delhi', '2023-07-19'),
(307, 'Neha Arora', 'neha.arora@gmail.com', 'Jaipur', '2023-08-11'),
(308, 'Tarun Sethi', 'tarun.sethi@gmail.com', 'Mumbai', '2023-10-03'),
(309, 'Ritika Pal', 'ritika.pal@yahoo.com', 'Kolkata', '2024-01-24'),
(310, 'Manav Kulkarni', 'manav.kulkarni@gmail.com', NULL, '2024-02-16'),
(311, 'Ira Bansal', 'ira.bansal@gmail.com', 'Noida', '2024-03-10'),
(312, 'Kunal Roy', 'kunal.roy@outlook.com', 'Bangalore', '2024-04-12');

-- Insert order seed data.
INSERT INTO orders (order_id, customer_id, order_date, total_amount, status) VALUES
(401, 301, '2024-04-01', 3499.00, 'Delivered'),
(402, 302, '2024-04-02', 899.00, 'Pending'),
(403, 303, '2024-04-03', 15999.00, 'Delivered'),
(404, 304, '2024-04-04', 2299.00, 'Cancelled'),
(405, 305, '2024-04-05', 4999.00, 'Shipped'),
(406, 306, '2024-04-06', 1249.00, 'Delivered'),
(407, 307, '2024-04-07', 799.00, 'Pending'),
(408, 308, '2024-04-08', 18999.00, 'Delivered'),
(409, 309, '2024-04-09', 999.00, 'Returned'),
(410, 310, '2024-04-10', 2750.00, 'Delivered'),
(411, 311, '2024-04-11', 6499.00, 'Shipped'),
(412, 312, '2024-04-12', 1599.00, 'Pending');

-- Insert product seed data.
INSERT INTO products (product_id, name, category, price, stock) VALUES
(501, 'Notebook', 'Stationery', 45.00, 120),
(502, 'Pen', 'Stationery', 12.00, 300),
(503, 'Marker', 'Stationery', 35.00, 90),
(504, 'Monitor', 'Electronics', 11500.00, 10),
(505, 'Keyboard', 'Electronics', 1700.00, 40),
(506, 'Water Bottle', 'Kitchen', 250.00, 0),
(507, 'Printer', 'Electronics', 8900.00, 8),
(508, 'Folder', 'Office', 75.00, 60),
(509, 'Mouse Pad', 'Accessories', 399.00, 150),
(510, 'Desk Organizer', 'Office', 649.00, 35),
(511, 'Cable Manager', 'Accessories', 299.00, 70),
(512, 'Laptop Stand', 'Electronics', 1999.00, 25);

-- Insert order item seed data.
INSERT INTO order_items (order_item_id, order_id, product_id, quantity, unit_price) VALUES
(601, 401, 505, 1, 1700.00),
(602, 401, 509, 2, 399.00),
(603, 402, 502, 3, 12.00),
(604, 403, 504, 1, 11500.00),
(605, 403, 512, 2, 1999.00),
(606, 404, 508, 4, 75.00),
(607, 405, 507, 1, 8900.00),
(608, 406, 506, 2, 250.00),
(609, 407, 511, 1, 299.00),
(610, 408, 504, 1, 11500.00),
(611, 409, 503, 5, 35.00),
(612, 410, 510, 2, 649.00),
(613, 411, 507, 1, 8900.00),
(614, 412, 502, 4, 12.00);

-- Insert current customer snapshot data.
INSERT INTO current_customers (customer_name, city) VALUES
('Asha Patel', 'Mumbai'),
('Rohan Singh', 'Delhi'),
('Meera Joshi', 'Bangalore'),
('David Kumar', 'Chennai'),
('Priya Menon', 'Pune'),
('Tarun Sethi', 'Mumbai');

-- Insert archived customer snapshot data.
INSERT INTO archived_customers (customer_name, city) VALUES
('Rohan Singh', 'Delhi'),
('Kiran Das', 'Kolkata'),
('David Kumar', 'Chennai'),
('Latha R', 'Madurai'),
('Asha Patel', 'Mumbai'),
('Sonia Verma', 'Bhopal');

-- ============================================================
-- CONCEPT: BASIC SYNTAX & FILTER STRUCTURE
-- ============================================================
/*
  Explanation:
  ------------
  Pattern and set filtering mostly starts inside the WHERE clause.
  The main structure is:
  - SELECT the columns you need
  - FROM the table you need
  - WHERE the rows must match a pattern, list, or range

  Syntax:
  -------
  SELECT column_list
  FROM table_name
  WHERE condition;

  Common Mistake:
  ---------------
  Beginners often try to write a text search using = when they really need
  LIKE or REGEXP.
*/

-- Example: Basic range filter on product price
SELECT
    product_id,                  -- Show the product identifier
    name,                        -- Show the product name
    price                        -- Show the product price
FROM products                    -- Read rows from products
WHERE price BETWEEN 100 AND 500; -- Keep only rows within the inclusive range
-- Expected Output: Products priced from 100 through 500 inclusive

-- Edge Case: Exact equality is not partial matching
SELECT
    customer_id,                 -- Show the customer identifier
    name,                        -- Show the customer name
    email                        -- Show the email being checked
FROM customers                   -- Read rows from customers
WHERE email = 'gmail.com';       -- This checks exact equality only
-- Expected Output: No rows, because email values are full addresses, not just gmail.com

-- ============================================================
-- CONCEPT: COMPARISON AND LOGICAL OPERATORS USED WITH PATTERNS/SETS
-- ============================================================
/*
  Explanation:
  ------------
  Pattern and set filters are often combined with comparison and logical
  operators. BETWEEN, IN, LIKE, and REGEXP rarely appear alone in real work.
  We combine them with AND, OR, and NOT.

  Syntax:
  -------
  WHERE condition_1
    AND condition_2

  Common Mistake:
  ---------------
  Forgetting parentheses when mixing AND and OR can change the result.
*/

-- Example: Combine category and price conditions
SELECT
    product_id,                                 -- Show the product identifier
    name,                                       -- Show the product name
    category,                                   -- Show the product category
    price                                       -- Show the product price
FROM products                                   -- Read rows from products
WHERE category IN ('Electronics', 'Office')     -- Keep two categories
  AND price BETWEEN 500 AND 10000;              -- Then keep only the target price band
-- Expected Output: Keyboard, Printer, Desk Organizer, Laptop Stand

-- Edge Case: Parentheses make logical intention explicit
SELECT
    order_id,                                   -- Show the order identifier
    status,                                     -- Show the order status
    total_amount                                -- Show the order amount
FROM orders                                     -- Read rows from orders
WHERE (status = 'Delivered' OR status = 'Shipped') -- Keep two status groups
  AND total_amount > 4000;                      -- Then require high value
-- Expected Output: Delivered or Shipped orders above 4000 only

-- ============================================================
-- CONCEPT: BETWEEN
-- ============================================================
/*
  Explanation:
  ------------
  BETWEEN checks whether a value falls inside a range. In MySQL, BETWEEN is
  inclusive. That means the start value and the end value both count.

  Syntax:
  -------
  expression BETWEEN low_value AND high_value

  Common Mistake:
  ---------------
  Beginners often think BETWEEN excludes the boundaries. It does not.
*/

-- Example: Salary range filter
SELECT
    emp_id,                                   -- Show employee id
    name,                                     -- Show employee name
    salary                                    -- Show salary being tested
FROM employees                                -- Read rows from employees
WHERE salary BETWEEN 50000 AND 90000;         -- Keep salaries inside the inclusive band
-- Expected Output: Employees whose salary is at least 50000 and at most 90000

-- Edge Case: Boundary values are included
SELECT
    product_id,                               -- Show product id
    name,                                     -- Show product name
    price                                     -- Show price
FROM products                                 -- Read rows from products
WHERE price BETWEEN 299 AND 299;              -- Keep rows exactly equal to 299
-- Expected Output: Cable Manager only

-- ============================================================
-- CONCEPT: NOT BETWEEN
-- ============================================================
/*
  Explanation:
  ------------
  NOT BETWEEN returns rows outside the specified range. It is equivalent to
  checking less than the lower bound OR greater than the upper bound.

  Syntax:
  -------
  expression NOT BETWEEN low_value AND high_value

  Common Mistake:
  ---------------
  Some learners assume NOT BETWEEN is exclusive in a different way. It simply
  means "outside the inclusive range."
*/

-- Example: Products outside a mid-price range
SELECT
    product_id,                               -- Show product id
    name,                                     -- Show product name
    price                                     -- Show price
FROM products                                 -- Read rows from products
WHERE price NOT BETWEEN 50 AND 500;           -- Keep rows outside the band
-- Expected Output: Products priced below 50 or above 500

-- Edge Case: NOT BETWEEN with equal boundary
SELECT
    product_id,                               -- Show product id
    name,                                     -- Show product name
    price                                     -- Show price
FROM products                                 -- Read rows from products
WHERE price NOT BETWEEN 250 AND 250;          -- Exclude only the exact value 250
-- Expected Output: All products except Water Bottle

-- ============================================================
-- CONCEPT: BETWEEN WITH DATES
-- ============================================================
/*
  Explanation:
  ------------
  BETWEEN works with dates as well as numbers. This is extremely common in
  reporting, monthly summaries, and operational checks.

  Syntax:
  -------
  date_column BETWEEN 'YYYY-MM-DD' AND 'YYYY-MM-DD'

  Common Mistake:
  ---------------
  Forgetting that the start and end date both count.
*/

-- Example: Orders placed in the first week of April 2024
SELECT
    order_id,                                         -- Show order id
    order_date,                                       -- Show order date
    total_amount                                      -- Show order amount
FROM orders                                           -- Read rows from orders
WHERE order_date BETWEEN '2024-04-01' AND '2024-04-07'; -- Keep orders inside the date band
-- Expected Output: Orders 401 through 407

-- Edge Case: Single-day date range
SELECT
    order_id,                                         -- Show order id
    order_date,                                       -- Show order date
    status                                            -- Show order status
FROM orders                                           -- Read rows from orders
WHERE order_date BETWEEN '2024-04-08' AND '2024-04-08'; -- Keep one exact date
-- Expected Output: Order 408 only

-- ============================================================
-- CONCEPT: IN
-- ============================================================
/*
  Explanation:
  ------------
  IN checks whether a value matches one of several listed values. It is cleaner
  and more maintainable than many OR conditions.

  Syntax:
  -------
  expression IN (value1, value2, value3, ...)

  Common Mistake:
  ---------------
  Repeating OR endlessly when IN would be simpler and less error-prone.
*/

-- Example: Employees from selected cities
SELECT
    emp_id,                                      -- Show employee id
    name,                                        -- Show employee name
    dept_id                                      -- Show department id
FROM employees                                   -- Read rows from employees
WHERE dept_id IN (10, 40);                       -- Keep Engineering and HR department members
-- Expected Output: Employees from departments 10 and 40

-- Edge Case: IN with text values
SELECT
    customer_id,                                 -- Show customer id
    name,                                        -- Show customer name
    city                                         -- Show city
FROM customers                                   -- Read rows from customers
WHERE city IN ('Mumbai', 'Bangalore', 'Delhi');  -- Keep three city groups
-- Expected Output: Customers from Mumbai, Bangalore, or Delhi

-- ============================================================
-- CONCEPT: NOT IN
-- ============================================================
/*
  Explanation:
  ------------
  NOT IN excludes listed values. It is the opposite of IN.

  Syntax:
  -------
  expression NOT IN (value1, value2, value3, ...)

  Common Mistake:
  ---------------
  NOT IN becomes tricky when NULL appears inside the list or subquery result.
*/

-- Example: Exclude two cities
SELECT
    customer_id,                              -- Show customer id
    name,                                     -- Show customer name
    city                                      -- Show city
FROM customers                                -- Read rows from customers
WHERE city NOT IN ('Mumbai', 'Delhi');        -- Exclude two cities
-- Expected Output: Customers whose city is not Mumbai or Delhi, excluding NULL city

-- Edge Case: NULL row is not matched by NOT IN
SELECT
    customer_id,                              -- Show customer id
    name,                                     -- Show customer name
    city                                      -- Show city
FROM customers                                -- Read rows from customers
WHERE city NOT IN ('Mumbai', 'Delhi', 'Chennai'); -- Exclude three city values
-- Expected Output: Non-listed city rows only, but NULL city still does not appear

-- ============================================================
-- CONCEPT: NOT IN WITH NULL WARNING
-- ============================================================
/*
  Explanation:
  ------------
  If NULL appears inside a NOT IN list or subquery result, the logical outcome
  can become UNKNOWN, causing unexpected missing rows.

  Syntax:
  -------
  WHERE key_column NOT IN (subquery_or_list)

  Common Mistake:
  ---------------
  Assuming NOT IN always behaves like "not equal to every item." NULL changes
  the logic and can invalidate the comparison.
*/

-- Example: Dangerous NOT IN pattern using a literal NULL
SELECT
    customer_id,                               -- Show customer id
    name                                       -- Show customer name
FROM customers                                 -- Read rows from customers
WHERE customer_id NOT IN (301, 302, NULL);     -- Include NULL inside the NOT IN list
-- Expected Output: No rows in standard three-valued SQL logic, because NULL poisons the comparison

-- Edge Case: Safer comparison without NULL
SELECT
    customer_id,                               -- Show customer id
    name                                       -- Show customer name
FROM customers                                 -- Read rows from customers
WHERE customer_id NOT IN (301, 302);           -- Exclude only two known ids
-- Expected Output: All customer rows except 301 and 302

-- ============================================================
-- CONCEPT: IN WITH SUBQUERY
-- ============================================================
/*
  Explanation:
  ------------
  IN can compare a value against the result of another SELECT statement.
  This is useful when one table must be filtered using values discovered
  in another table.

  Syntax:
  -------
  WHERE expression IN (SELECT single_column FROM ...)

  Common Mistake:
  ---------------
  Returning multiple columns from the subquery. IN expects one comparable column.
*/

-- Example: Customers who have placed at least one delivered order
SELECT
    customer_id,                               -- Show customer id
    name                                       -- Show customer name
FROM customers                                 -- Read rows from customers
WHERE customer_id IN (                         -- Keep customers whose ids appear in the subquery
    SELECT customer_id                         -- Return only the customer id column
    FROM orders                                -- Read rows from orders
    WHERE status = 'Delivered'                 -- Keep delivered orders only
);
-- Expected Output: Customers tied to at least one delivered order

-- Edge Case: Product categories appearing in order items through a subquery
SELECT
    product_id,                                -- Show product id
    name,                                      -- Show product name
    category                                   -- Show category
FROM products                                  -- Read rows from products
WHERE product_id IN (                          -- Keep products that appear in order items
    SELECT product_id                          -- Return sold product ids
    FROM order_items                           -- Read rows from order_items
);
-- Expected Output: Products that have appeared in at least one order

-- ============================================================
-- CONCEPT: LIKE
-- ============================================================
/*
  Explanation:
  ------------
  LIKE performs simple pattern matching on text values. It uses wildcards:
  - % for zero or more characters
  - _ for exactly one character

  Syntax:
  -------
  expression LIKE 'pattern'

  Common Mistake:
  ---------------
  Using = for partial text matching. = only checks complete equality.
*/

-- Example: Customer emails ending with gmail.com
SELECT
    customer_id,                               -- Show customer id
    name,                                      -- Show customer name
    email                                      -- Show email
FROM customers                                 -- Read rows from customers
WHERE email LIKE '%@gmail.com';                -- Match addresses ending in @gmail.com
-- Expected Output: Gmail customer rows

-- Edge Case: Product names starting with M
SELECT
    product_id,                                -- Show product id
    name                                       -- Show product name
FROM products                                  -- Read rows from products
WHERE name LIKE 'M%';                          -- Match names starting with M
-- Expected Output: Marker and Monitor and Mouse Pad

-- ============================================================
-- CONCEPT: LIKE WITH PREFIX, SUFFIX, AND CONTAINS SEARCH
-- ============================================================
/*
  Explanation:
  ------------
  LIKE patterns are often used in three common forms:
  - 'A%' for prefix search
  - '%land' for suffix search
  - '%sql%' for contains search

  Syntax:
  -------
  LIKE 'text%'
  LIKE '%text'
  LIKE '%text%'

  Common Mistake:
  ---------------
  Using leading % everywhere. It is flexible but usually weaker for index use.
*/

-- Example: Names starting with A
SELECT
    emp_id,                                    -- Show employee id
    name                                       -- Show employee name
FROM employees                                 -- Read rows from employees
WHERE name LIKE 'A%';                          -- Match names that begin with A
-- Expected Output: Asha Menon, Anita Rao, Arjun Sethi

-- Edge Case: Names containing 'an'
SELECT
    emp_id,                                    -- Show employee id
    name                                       -- Show employee name
FROM employees                                 -- Read rows from employees
WHERE name LIKE '%an%';                        -- Match names containing the sequence an
-- Expected Output: Balan Iyer, Anita Rao, Tarun Malhotra

-- ============================================================
-- CONCEPT: UNDERSCORE WILDCARD
-- ============================================================
/*
  Explanation:
  ------------
  The underscore wildcard matches exactly one character. It is useful when
  pattern position matters.

  Syntax:
  -------
  LIKE '_a%'

  Common Mistake:
  ---------------
  Using % when an exact single-character position matters.
*/

-- Example: Product names whose second letter is o
SELECT
    product_id,                                -- Show product id
    name                                       -- Show product name
FROM products                                  -- Read rows from products
WHERE name LIKE '_o%';                         -- Match names with o as the second character
-- Expected Output: Folder

-- Edge Case: Names with exactly three letters
SELECT
    name                                       -- Show product name
FROM products                                  -- Read rows from products
WHERE name LIKE '___';                         -- Match exactly three characters
-- Expected Output: Pen

-- ============================================================
-- CONCEPT: NOT LIKE
-- ============================================================
/*
  Explanation:
  ------------
  NOT LIKE excludes rows that match a pattern.

  Syntax:
  -------
  expression NOT LIKE 'pattern'

  Common Mistake:
  ---------------
  Forgetting that NOT LIKE still follows three-valued logic for NULL values.
*/

-- Example: Exclude product names starting with M
SELECT
    product_id,                                -- Show product id
    name                                       -- Show product name
FROM products                                  -- Read rows from products
WHERE name NOT LIKE 'M%';                      -- Exclude names beginning with M
-- Expected Output: All product rows except Marker, Monitor, and Mouse Pad

-- Edge Case: NOT LIKE does not include NULL values
SELECT
    customer_id,                               -- Show customer id
    name,                                      -- Show customer name
    city                                       -- Show city
FROM customers                                 -- Read rows from customers
WHERE city NOT LIKE 'M%';                      -- Exclude city values starting with M
-- Expected Output: Non-M cities only, but NULL city does not appear

-- ============================================================
-- CONCEPT: ESCAPE WITH LIKE
-- ============================================================
/*
  Explanation:
  ------------
  If the actual stored text contains % or _, you can use ESCAPE to treat the
  wildcard as a literal character.

  Syntax:
  -------
  expression LIKE 'item\\_%' ESCAPE '\\'

  Common Mistake:
  ---------------
  Forgetting that _ and % are wildcard symbols by default.
*/

-- Create a helper table for literal wildcard examples.
CREATE TABLE pattern_demo (
    label_text VARCHAR(50) NOT NULL            -- Demo text values for LIKE ESCAPE
);

-- Insert helper rows that include literal underscores and percent signs.
INSERT INTO pattern_demo (label_text) VALUES
('item_01'),
('itemA01'),
('discount_20%'),
('discountX20%');

-- Example: Match a literal underscore
SELECT
    label_text                                 -- Show the demo text
FROM pattern_demo                              -- Read rows from the helper table
WHERE label_text LIKE 'item\\_01' ESCAPE '\\'; -- Treat _ as a literal underscore
-- Expected Output: item_01 only

-- Edge Case: Match a literal underscore before a percent text segment
SELECT
    label_text                                 -- Show the demo text
FROM pattern_demo                              -- Read rows from the helper table
WHERE label_text LIKE 'discount\\_20%' ESCAPE '\\'; -- Match the literal underscore
-- Expected Output: discount_20% only

-- ============================================================
-- CONCEPT: REGEXP
-- ============================================================
/*
  Explanation:
  ------------
  REGEXP allows more flexible pattern matching than LIKE. It supports anchors,
  alternation, and richer expressions.

  Syntax:
  -------
  expression REGEXP 'regular_expression'

  Common Mistake:
  ---------------
  Treating REGEXP exactly like LIKE. They are different pattern systems.
*/

-- Example: Customers in cities starting with M or B
SELECT
    customer_id,                               -- Show customer id
    name,                                      -- Show customer name
    city                                       -- Show city
FROM customers                                 -- Read rows from customers
WHERE city REGEXP '^(M|B)';                    -- Match city values beginning with M or B
-- Expected Output: Mumbai and Bangalore customers

-- Edge Case: Product names ending with er
SELECT
    product_id,                                -- Show product id
    name                                       -- Show product name
FROM products                                  -- Read rows from products
WHERE name REGEXP 'er$';                       -- Match names ending in er
-- Expected Output: Marker, Folder, Printer, Cable Manager

-- ============================================================
-- CONCEPT: NULL HANDLING WITH PATTERN FILTERS
-- ============================================================
/*
  Explanation:
  ------------
  NULL means unknown or missing. Pattern operators like LIKE and REGEXP do not
  match NULL. You must use IS NULL or COALESCE/IFNULL deliberately when needed.

  Syntax:
  -------
  column IS NULL
  column IS NOT NULL
  COALESCE(column, 'fallback')

  Common Mistake:
  ---------------
  Writing column = NULL instead of column IS NULL.
*/

-- Example: Find customers with missing city
SELECT
    customer_id,                               -- Show customer id
    name,                                      -- Show customer name
    city                                       -- Show city
FROM customers                                 -- Read rows from customers
WHERE city IS NULL;                            -- Keep rows with missing city
-- Expected Output: Manav Kulkarni

-- Edge Case: Convert NULL to text for search testing
SELECT
    customer_id,                               -- Show customer id
    name,                                      -- Show customer name
    COALESCE(city, 'Unknown') AS city_label    -- Replace NULL city with Unknown
FROM customers                                 -- Read rows from customers
WHERE COALESCE(city, 'Unknown') LIKE 'U%';     -- Match the replacement value
-- Expected Output: Customer rows whose missing city becomes Unknown

-- ============================================================
-- CONCEPT: DISTINCT WITH PATTERN AND LIST RESULTS
-- ============================================================
/*
  Explanation:
  ------------
  DISTINCT removes duplicate rows from the selected output. It is useful when
  pattern or set filters return repeated category or city values.

  Syntax:
  -------
  SELECT DISTINCT column_name
  FROM table_name
  WHERE condition;

  Common Mistake:
  ---------------
  Confusing DISTINCT with GROUP BY. DISTINCT removes duplicates but does not
  calculate aggregates by itself.
*/

-- Example: Unique cities among Gmail customers
SELECT DISTINCT
    city                                       -- Return one row per city
FROM customers                                 -- Read rows from customers
WHERE email LIKE '%@gmail.com'                 -- Keep Gmail rows only
  AND city IS NOT NULL;                        -- Exclude NULL for cleaner output
-- Expected Output: Unique city values for Gmail customers

-- Edge Case: Unique categories among products in a price range
SELECT DISTINCT
    category                                   -- Return one row per category
FROM products                                  -- Read rows from products
WHERE price BETWEEN 100 AND 2000;              -- Keep mid-range products
-- Expected Output: Categories represented by products in the 100-2000 range

-- ============================================================
-- CONCEPT: ORDER BY AND LIMIT WITH FILTERS
-- ============================================================
/*
  Explanation:
  ------------
  After filtering rows with patterns or sets, we often sort and trim the final
  result. This is how we produce ranked shortlists and paginated search results.

  Syntax:
  -------
  SELECT ...
  FROM ...
  WHERE ...
  ORDER BY column_name DESC
  LIMIT n OFFSET m;

  Common Mistake:
  ---------------
  Using LIMIT without ORDER BY for a "top" result. Without ordering, the slice
  is not meaningfully ranked.
*/

-- Example: Top three most expensive electronics or office products
SELECT
    product_id,                                -- Show product id
    name,                                      -- Show product name
    category,                                  -- Show product category
    price                                      -- Show product price
FROM products                                  -- Read rows from products
WHERE category IN ('Electronics', 'Office')    -- Keep target categories
ORDER BY price DESC                            -- Sort highest price first
LIMIT 3;                                       -- Return only the top three rows
-- Expected Output: The three most expensive rows among Electronics and Office

-- Edge Case: Pagination style query
SELECT
    customer_id,                               -- Show customer id
    name,                                      -- Show customer name
    city                                       -- Show city
FROM customers                                 -- Read rows from customers
WHERE city IS NOT NULL                         -- Exclude NULL city
ORDER BY city ASC, name ASC                    -- Sort deterministically
LIMIT 3 OFFSET 2;                              -- Skip two rows and return the next three
-- Expected Output: The third, fourth, and fifth rows from the sorted result

-- ============================================================
-- CONCEPT: GROUP BY AND HAVING WITH SET-STYLE FILTERS
-- ============================================================
/*
  Explanation:
  ------------
  This topic mainly focuses on row filtering, but grouped filtering is still
  relevant when we want category-level or city-level pattern results.

  Syntax:
  -------
  SELECT grouped_column, COUNT(*)
  FROM table_name
  WHERE row_filter
  GROUP BY grouped_column
  HAVING aggregate_filter;

  Common Mistake:
  ---------------
  Trying to use aggregate conditions like COUNT(*) > 1 inside WHERE.
*/

-- Example: Cities with at least two customers among Gmail users
SELECT
    city,                                      -- Group by city
    COUNT(*) AS gmail_customer_count           -- Count Gmail customers in each city
FROM customers                                 -- Read rows from customers
WHERE email LIKE '%@gmail.com'                 -- Keep Gmail rows only
  AND city IS NOT NULL                         -- Exclude NULL city
GROUP BY city                                  -- Form one group per city
HAVING COUNT(*) >= 2;                          -- Keep only cities with at least two matches
-- Expected Output: Cities that have two or more Gmail customers

-- Edge Case: Categories with average price above 1000 among office/electronics
SELECT
    category,                                  -- Group by category
    AVG(price) AS average_price                -- Compute average price in each group
FROM products                                  -- Read rows from products
WHERE category IN ('Electronics', 'Office')    -- Keep two categories only
GROUP BY category                              -- Form groups by category
HAVING AVG(price) > 1000;                      -- Keep expensive average groups
-- Expected Output: Categories whose average price exceeds 1000

-- ============================================================
-- CONCEPT: JOINS USED WITH PATTERN AND SET FILTERS
-- ============================================================
/*
  Explanation:
  ------------
  Pattern and set filters become much more powerful when applied after joining
  related tables. This lets us filter customer rows using order information,
  or product rows using sales activity.

  Syntax:
  -------
  SELECT ...
  FROM table_a
  JOIN table_b
    ON ...
  WHERE pattern_or_set_filter;

  Common Mistake:
  ---------------
  Filtering the wrong table's column because the join logic is not understood.
*/

-- Example: Delivered orders placed by customers from Mumbai or Bangalore
SELECT
    o.order_id,                                -- Show order id
    c.name AS customer_name,                   -- Show customer name from the joined table
    c.city,                                    -- Show customer city
    o.status,                                  -- Show order status
    o.total_amount                             -- Show order amount
FROM orders AS o                               -- Start from the orders table
INNER JOIN customers AS c                      -- Join customers to enrich order rows
    ON o.customer_id = c.customer_id           -- Match each order to its customer
WHERE c.city IN ('Mumbai', 'Bangalore')        -- Filter by the customer city
  AND o.status = 'Delivered';                  -- Filter by the order status
-- Expected Output: Delivered orders from Mumbai or Bangalore customers

-- Edge Case: Products sold in orders whose status is Delivered or Shipped
SELECT DISTINCT
    p.product_id,                              -- Show product id
    p.name,                                    -- Show product name
    p.category                                 -- Show category
FROM products AS p                             -- Start from products
INNER JOIN order_items AS oi                   -- Join order items to see what sold
    ON p.product_id = oi.product_id            -- Match products to order item rows
INNER JOIN orders AS o                         -- Join orders to inspect order status
    ON oi.order_id = o.order_id                -- Match order items to parent orders
WHERE o.status IN ('Delivered', 'Shipped');    -- Keep sold products from active completion states
-- Expected Output: Unique products that appeared in delivered or shipped orders

-- ============================================================
-- CONCEPT: SUBQUERIES WITH IN, EXISTS, AND NOT EXISTS
-- ============================================================
/*
  Explanation:
  ------------
  Subqueries let one query depend on the result of another. In this topic,
  they are commonly used with IN, EXISTS, and NOT EXISTS.

  Syntax:
  -------
  WHERE key IN (SELECT ...)
  WHERE EXISTS (SELECT ...)
  WHERE NOT EXISTS (SELECT ...)

  Common Mistake:
  ---------------
  Using NOT IN with a subquery that may return NULL. NOT EXISTS is often safer.
*/

-- Example: Customers who have at least one shipped order
SELECT
    customer_id,                               -- Show customer id
    name                                       -- Show customer name
FROM customers AS c                            -- Read rows from customers
WHERE EXISTS (                                 -- Keep rows for which the subquery finds a match
    SELECT 1                                   -- The actual returned value is irrelevant for EXISTS
    FROM orders AS o                           -- Read rows from orders
    WHERE o.customer_id = c.customer_id        -- Correlate subquery to outer customer row
      AND o.status = 'Shipped'                 -- Keep shipped orders only
);
-- Expected Output: Customers who have placed at least one shipped order

-- Edge Case: Customers with no orders at all
SELECT
    customer_id,                               -- Show customer id
    name                                       -- Show customer name
FROM customers AS c                            -- Read rows from customers
WHERE NOT EXISTS (                             -- Keep rows for which no order exists
    SELECT 1                                   -- Value is irrelevant for NOT EXISTS
    FROM orders AS o                           -- Read rows from orders
    WHERE o.customer_id = c.customer_id        -- Check whether the customer has any order
);
-- Expected Output: Customers with zero orders

-- ============================================================
-- CONCEPT: UNION
-- ============================================================
/*
  Explanation:
  ------------
  UNION combines result sets from two SELECT statements and removes duplicates.

  Syntax:
  -------
  SELECT ...
  UNION
  SELECT ...

  Common Mistake:
  ---------------
  Forgetting that UNION removes duplicate rows, which may hide repeated values.
*/

-- Example: Combine current and archived customer names without duplicates
SELECT
    customer_name,                             -- Return customer name
    city                                       -- Return customer city
FROM current_customers                         -- Read current snapshot
UNION                                          -- Combine and remove duplicates
SELECT
    customer_name,                             -- Return archived customer name
    city                                       -- Return archived customer city
FROM archived_customers;                       -- Read archived snapshot
-- Expected Output: One combined deduplicated list of customer_name and city pairs

-- Edge Case: UNION result sorted at the very end
SELECT
    customer_name                              -- Return customer name only
FROM current_customers                         -- Read current snapshot
UNION                                          -- Combine and remove duplicates
SELECT
    customer_name                              -- Return archived customer name only
FROM archived_customers                        -- Read archived snapshot
ORDER BY customer_name;                        -- Sort the final combined result
-- Expected Output: Alphabetically sorted unique customer names

-- ============================================================
-- CONCEPT: UNION ALL
-- ============================================================
/*
  Explanation:
  ------------
  UNION ALL also combines result sets, but it keeps duplicates. This is useful
  when duplicate rows are meaningful or when performance matters.

  Syntax:
  -------
  SELECT ...
  UNION ALL
  SELECT ...

  Common Mistake:
  ---------------
  Using UNION when the task needs duplicate-preserving output.
*/

-- Example: Combine current and archived customer names with duplicates preserved
SELECT
    customer_name,                             -- Return customer name
    city                                       -- Return customer city
FROM current_customers                         -- Read current snapshot
UNION ALL                                      -- Combine and keep duplicates
SELECT
    customer_name,                             -- Return archived customer name
    city                                       -- Return archived customer city
FROM archived_customers;                       -- Read archived snapshot
-- Expected Output: Combined list with repeated rows still visible

-- Edge Case: Duplicate-sensitive audit count
SELECT
    COUNT(*) AS combined_row_count             -- Count all rows after combining
FROM (                                         -- Build a derived table for counting
    SELECT customer_name, city                 -- Select current rows
    FROM current_customers                     -- Read current snapshot
    UNION ALL                                  -- Combine and keep duplicates
    SELECT customer_name, city                 -- Select archived rows
    FROM archived_customers                    -- Read archived snapshot
) AS combined_rows;                            -- Name the derived table
-- Expected Output: Total number of combined rows including duplicates

-- ============================================================
-- CONCEPT: INTERSECT
-- ============================================================
/*
  Explanation:
  ------------
  INTERSECT returns only rows common to both result sets.

  Syntax:
  -------
  SELECT ...
  INTERSECT
  SELECT ...

  Common Mistake:
  ---------------
  Assuming every MySQL installation supports INTERSECT. It is available in
  newer MySQL versions. In older versions, you emulate it with INNER JOIN or
  EXISTS logic.
*/

-- Example: Customers present in both current and archived snapshots
SELECT
    customer_name,                             -- Return customer name
    city                                       -- Return city
FROM current_customers                         -- Read current snapshot
INTERSECT                                      -- Keep only common rows
SELECT
    customer_name,                             -- Return archived customer name
    city                                       -- Return archived customer city
FROM archived_customers;                       -- Read archived snapshot
-- Expected Output: Rows that appear in both tables, such as Rohan Singh and Asha Patel

-- Edge Case: Compatible fallback using INNER JOIN for older MySQL versions
SELECT DISTINCT
    c.customer_name,                           -- Return customer name
    c.city                                     -- Return city
FROM current_customers AS c                    -- Read current snapshot
INNER JOIN archived_customers AS a             -- Join to archived snapshot
    ON c.customer_name = a.customer_name       -- Match by name
   AND c.city = a.city;                        -- Match by city too
-- Expected Output: Same logical result as INTERSECT

-- ============================================================
-- CONCEPT: EXCEPT
-- ============================================================
/*
  Explanation:
  ------------
  EXCEPT returns rows from the first query that do not appear in the second.

  Syntax:
  -------
  SELECT ...
  EXCEPT
  SELECT ...

  Common Mistake:
  ---------------
  Assuming EXCEPT is universal across all MySQL environments. As with INTERSECT,
  older versions need an alternative pattern.
*/

-- Example: Current customers not found in the archive snapshot
SELECT
    customer_name,                             -- Return customer name
    city                                       -- Return city
FROM current_customers                         -- Read current snapshot
EXCEPT                                         -- Remove rows also present in archive
SELECT
    customer_name,                             -- Return archived customer name
    city                                       -- Return archived customer city
FROM archived_customers;                       -- Read archived snapshot
-- Expected Output: Rows found only in current_customers

-- Edge Case: Fallback using NOT EXISTS for older MySQL versions
SELECT
    c.customer_name,                           -- Return customer name
    c.city                                     -- Return city
FROM current_customers AS c                    -- Read current snapshot
WHERE NOT EXISTS (                             -- Keep rows absent from archive
    SELECT 1                                   -- Value is irrelevant
    FROM archived_customers AS a               -- Read archived snapshot
    WHERE a.customer_name = c.customer_name    -- Match on customer name
      AND a.city = c.city                      -- Match on city
);
-- Expected Output: Same logical result as EXCEPT

-- ============================================================
-- CONCEPT: PERFORMANCE AND EXPLAIN
-- ============================================================
/*
  Explanation:
  ------------
  Pattern and set filters can affect performance significantly.
  - Prefix LIKE patterns may use indexes more easily.
  - Leading wildcard LIKE patterns are usually harder to optimize.
  - IN with a small list is often efficient.
  - UNION ALL is usually cheaper than UNION because there is no deduplication.

  Syntax:
  -------
  EXPLAIN SELECT ...

  Common Mistake:
  ---------------
  Ignoring how a pattern shape changes index usage.
*/

-- Create an index that can help city lookups.
CREATE INDEX idx_customers_city
ON customers (city);

-- Example: Explain a prefix search
EXPLAIN
SELECT
    customer_id,                               -- Show customer id
    name,                                      -- Show customer name
    city                                       -- Show city
FROM customers                                 -- Read rows from customers
WHERE city LIKE 'M%';                          -- Prefix search on city
-- Expected Output: Execution plan showing how MySQL intends to access the table

-- Edge Case: Explain a leading wildcard search
EXPLAIN
SELECT
    customer_id,                               -- Show customer id
    name,                                      -- Show customer name
    email                                      -- Show email
FROM customers                                 -- Read rows from customers
WHERE email LIKE '%gmail.com';                 -- Leading wildcard pattern
-- Expected Output: Execution plan that often shows weaker index use than a prefix pattern

-- ============================================================
-- CONCEPT: SECURITY NOTES FOR QUERYING
-- ============================================================
/*
  Explanation:
  ------------
  This topic is mainly about querying, but in real environments you still need
  the correct permissions to read data.

  Syntax:
  -------
  CREATE USER ...
  GRANT SELECT ...
  SHOW GRANTS ...

  Common Mistake:
  ---------------
  Attempting to query a database without SELECT privilege.
*/

-- Example: Create a read-only user for reporting
CREATE USER IF NOT EXISTS 'report_user'@'localhost'
IDENTIFIED BY 'ReportUser#2026';
-- Expected Output: A MySQL user account is created if it does not already exist

-- Example: Grant SELECT access on the learning database
GRANT SELECT
ON mysql_learning.*
TO 'report_user'@'localhost';
-- Expected Output: The user receives read-only access on this schema

-- Edge Case: Inspect granted privileges
SHOW GRANTS
FOR 'report_user'@'localhost';
-- Expected Output: The privilege statements granted to report_user

-- ============================================================
-- CONCEPT: EDGE CASES & COMMON MISTAKES
-- ============================================================
/*
  Explanation:
  ------------
  This topic has many beginner traps:
  - BETWEEN is inclusive
  - NOT IN behaves badly with NULL
  - LIKE and REGEXP are different tools
  - NULL is never matched by = NULL
  - UNION removes duplicates, UNION ALL does not

  Syntax:
  -------
  No single syntax here; this is a caution section.

  Common Mistake:
  ---------------
  Using city = NULL instead of city IS NULL.
*/

-- Example: Incorrect NULL comparison
SELECT
    customer_id,                               -- Show customer id
    name,                                      -- Show customer name
    city                                       -- Show city
FROM customers                                 -- Read rows from customers
WHERE city = NULL;                             -- Incorrect NULL comparison
-- Expected Output: No rows because = NULL is never true

-- Edge Case: Correct NULL comparison
SELECT
    customer_id,                               -- Show customer id
    name,                                      -- Show customer name
    city                                       -- Show city
FROM customers                                 -- Read rows from customers
WHERE city IS NULL;                            -- Correct NULL comparison
-- Expected Output: Manav Kulkarni

-- ============================================================
-- CONCEPT: INTERVIEW TIPS & TRICKY MYSQL BEHAVIORS
-- ============================================================
/*
  Explanation:
  ------------
  Interviewers often ask:
  - Is BETWEEN inclusive?
  - What is the difference between UNION and UNION ALL?
  - Why is NOT IN risky with NULL?
  - What is the difference between LIKE and REGEXP?
  - Can INTERSECT and EXCEPT be used in MySQL?

  Syntax:
  -------
  These are concept checks rather than new syntax.

  Common Mistake:
  ---------------
  Answering from generic SQL memory without noting MySQL-specific version behavior.
*/

-- Example: Quick reminder query for UNION versus UNION ALL
SELECT 'UNION removes duplicates' AS interview_tip_1
UNION
SELECT 'UNION ALL keeps duplicates' AS interview_tip_1;
-- Expected Output: Two distinct reminder rows

-- Edge Case: Version-sensitive note for INTERSECT and EXCEPT
SELECT VERSION() AS mysql_version;
-- Expected Output: The running MySQL version, which helps you judge feature availability

-- ============================================================
-- CONCEPT: REAL-WORLD SCHEMA EXAMPLES
-- ============================================================
/*
  Explanation:
  ------------
  Pattern and set filters appear in almost every domain:
  - E-commerce: products in price bands and categories
  - HR: employees from selected departments or cities
  - CRM: customer email domain searches
  - Hospital: patients with names matching a prefix or insurance in a list
  - Library: books whose title matches a pattern or category list

  Syntax:
  -------
  Standard SELECT / WHERE / ORDER BY / UNION patterns

  Common Mistake:
  ---------------
  Forgetting to match the filter style to the business rule.
*/

-- Example: E-commerce shortlist of premium electronics and office products
SELECT
    product_id,                                -- Show product id
    name,                                      -- Show product name
    category,                                  -- Show category
    price                                      -- Show price
FROM products                                  -- Read rows from products
WHERE category IN ('Electronics', 'Office')    -- Keep the requested categories
  AND price BETWEEN 500 AND 10000              -- Keep the requested price band
ORDER BY price DESC;                           -- Rank most expensive first
-- Expected Output: Premium shortlist for merchandising review

-- Edge Case: CRM query for Gmail or Outlook users
SELECT
    customer_id,                               -- Show customer id
    name,                                      -- Show customer name
    email                                      -- Show email
FROM customers                                 -- Read rows from customers
WHERE email REGEXP '@gmail\\.com$|@outlook\\.com$'; -- Match two email domains
-- Expected Output: Gmail and Outlook users only

-- ############################################################
-- END OF FILE: 04_MySQL_Patterns_Sets_Notes.sql
-- ############################################################
