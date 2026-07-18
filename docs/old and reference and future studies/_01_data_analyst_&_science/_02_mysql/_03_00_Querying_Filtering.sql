/*
================================================================================
STEP 03: QUERYING, FILTERING, SORTING, AND LIMITING DATA
================================================================================
GOAL:
Learn how to read data from tables, choose required columns, filter rows,
remove duplicates, sort results, and return only the rows we actually need.

THIS FILE IS SELF-CONTAINED:
- Creates a practice database
- Creates realistic tables
- Inserts sample data
- Demonstrates query concepts from beginner to interview level
================================================================================
*/

-- Create a dedicated practice database for this step
DROP DATABASE IF EXISTS mysql_03_querying_filtering_notes;

-- Create the database so all examples are isolated and repeatable
CREATE DATABASE mysql_03_querying_filtering_notes;

-- Switch into the new database
USE mysql_03_querying_filtering_notes;

/*
--------------------------------------------------------------------------------
1. SAMPLE SCHEMA USED THROUGHOUT THIS FILE
--------------------------------------------------------------------------------
We will use a realistic mini business schema with:
- departments
- employees
- projects
- emp_projects
- customers
- orders
- products
- order_items
--------------------------------------------------------------------------------
*/

-- Departments table for employee examples
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(50) NOT NULL
);

-- Employees table for HR-style querying examples
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dept_id INT,
    salary DECIMAL(10,2) NOT NULL,
    hire_date DATE NOT NULL,
    manager_id INT NULL,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- Projects table for later business filtering examples
CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    budget DECIMAL(12,2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NULL
);

-- Bridge table between employees and projects
CREATE TABLE emp_projects (
    emp_id INT NOT NULL,
    project_id INT NOT NULL,
    role VARCHAR(50) NOT NULL,
    PRIMARY KEY (emp_id, project_id),
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Customers table for e-commerce style queries
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    city VARCHAR(50),
    join_date DATE NOT NULL
);

-- Orders table for date, amount, and status filtering
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Products table for straightforward row filtering
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL
);

-- Order items table for richer transactional examples
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert department rows
INSERT INTO departments (dept_id, dept_name, location) VALUES
(10, 'Engineering', 'Bangalore'),
(20, 'Human Resources', 'Mumbai'),
(30, 'Finance', 'Delhi'),
(40, 'Sales', 'Chennai'),
(50, 'Operations', 'Hyderabad');

-- Insert employee rows
INSERT INTO employees (emp_id, name, dept_id, salary, hire_date, manager_id) VALUES
(101, 'Aarav Mehta', 10, 95000.00, '2020-01-15', NULL),
(102, 'Diya Sharma', 10, 72000.00, '2021-03-22', 101),
(103, 'Kabir Verma', 20, 54000.00, '2022-07-01', 108),
(104, 'Meera Iyer', 30, 68000.00, '2019-11-10', 109),
(105, 'Rohan Patel', 40, 61000.00, '2023-02-18', 110),
(106, 'Sana Khan', 40, 59000.00, '2024-05-06', 110),
(107, 'Vikram Das', 50, 64000.00, '2021-09-14', 111),
(108, 'Nisha Rao', 20, 88000.00, '2018-06-03', NULL),
(109, 'Arjun Sen', 30, 99000.00, '2017-04-27', NULL),
(110, 'Pooja Nair', 40, 91000.00, '2019-08-19', NULL),
(111, 'Karan Gill', 50, 87000.00, '2018-12-11', NULL),
(112, 'Ishita Bose', 10, 78000.00, '2022-10-30', 101);

-- Insert project rows
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

-- Insert employee-project assignments
INSERT INTO emp_projects (emp_id, project_id, role) VALUES
(101, 202, 'Architect'),
(102, 202, 'Backend Developer'),
(112, 202, 'Frontend Developer'),
(104, 210, 'Business Analyst'),
(109, 210, 'Finance Lead'),
(105, 205, 'Sales Analyst'),
(106, 208, 'Account Executive'),
(107, 201, 'Operations Coordinator'),
(111, 201, 'Program Manager'),
(103, 207, 'Recruiter'),
(108, 207, 'HR Lead'),
(107, 209, 'Process Owner');

-- Insert customer rows
INSERT INTO customers (customer_id, name, email, city, join_date) VALUES
(301, 'Ananya Gupta', 'ananya.gupta@gmail.com', 'Mumbai', '2023-01-05'),
(302, 'Rahul Joshi', 'rahul.joshi@yahoo.com', 'Delhi', '2023-02-17'),
(303, 'Sneha Kapoor', 'sneha.kapoor@outlook.com', 'Bangalore', '2023-03-09'),
(304, 'Dev Malhotra', 'dev.malhotra@gmail.com', 'Pune', '2023-05-21'),
(305, 'Priya Menon', 'priya.menon@gmail.com', 'Chennai', '2023-06-14'),
(306, 'Aman Batra', 'aman.batra@live.com', 'Delhi', '2023-07-19'),
(307, 'Neha Arora', 'neha.arora@gmail.com', 'Jaipur', '2023-08-11'),
(308, 'Tarun Sethi', 'tarun.sethi@gmail.com', 'Mumbai', '2023-10-03'),
(309, 'Ritika Pal', 'ritika.pal@yahoo.com', 'Kolkata', '2024-01-24'),
(310, 'Manav Kulkarni', 'manav.kulkarni@gmail.com', NULL, '2024-02-16'),
(311, 'Ira Bansal', 'ira.bansal@gmail.com', 'Noida', '2024-03-10'),
(312, 'Kunal Roy', 'kunal.roy@outlook.com', 'Bangalore', '2024-04-12');

-- Insert order rows
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

-- Insert product rows
INSERT INTO products (product_id, name, category, price, stock) VALUES
(501, 'Wireless Mouse', 'Electronics', 799.00, 55),
(502, 'Mechanical Keyboard', 'Electronics', 3499.00, 18),
(503, 'USB-C Hub', 'Electronics', 2299.00, 32),
(504, 'Office Chair', 'Furniture', 8999.00, 7),
(505, 'Standing Desk', 'Furniture', 18999.00, 4),
(506, 'Notebook Pack', 'Stationery', 299.00, 120),
(507, 'Gel Pen Set', 'Stationery', 199.00, 200),
(508, 'Water Bottle', 'Lifestyle', 499.00, 85),
(509, 'Laptop Sleeve', 'Accessories', 999.00, 40),
(510, 'Noise Cancelling Headphones', 'Electronics', 15999.00, 9),
(511, 'Desk Lamp', 'Furniture', 1499.00, 25),
(512, 'Planner 2026', 'Stationery', 349.00, 0);

-- Insert order item rows
INSERT INTO order_items (order_item_id, order_id, product_id, quantity, unit_price) VALUES
(601, 401, 502, 1, 3499.00),
(602, 402, 507, 3, 199.00),
(603, 403, 510, 1, 15999.00),
(604, 404, 509, 2, 999.00),
(605, 405, 503, 1, 2299.00),
(606, 405, 508, 2, 499.00),
(607, 406, 506, 2, 299.00),
(608, 407, 508, 1, 499.00),
(609, 408, 505, 1, 18999.00),
(610, 409, 509, 1, 999.00),
(611, 410, 511, 1, 1499.00),
(612, 410, 506, 3, 299.00),
(613, 411, 504, 1, 8999.00),
(614, 412, 503, 1, 2299.00);

-- Verify setup
SELECT COUNT(*) AS employee_rows FROM employees;
-- Expected output: 12

SELECT COUNT(*) AS customer_rows FROM customers;
-- Expected output: 12

SELECT COUNT(*) AS order_rows FROM orders;
-- Expected output: 12

/*
--------------------------------------------------------------------------------
2. WHAT IS DQL?
--------------------------------------------------------------------------------
DQL = Data Query Language

Main command:
- SELECT

WHY WE USE IT:
- To read data from tables
- To display only required columns
- To filter unwanted rows
- To sort results
- To return only the rows we actually need

IMPORTANT:
- SELECT does not modify stored table data
- SELECT returns result sets only
--------------------------------------------------------------------------------
*/

-- Read every column from the products table
SELECT *
FROM products;
-- Expected output: 12 product rows with all columns

/*
--------------------------------------------------------------------------------
3. BASIC SELECT
--------------------------------------------------------------------------------
SYNTAX:
SELECT column1, column2, ...
FROM table_name;

SELECT * means:
- return all columns

BEST PRACTICE:
- avoid SELECT * in production queries when only a few columns are needed
- selecting only required columns improves readability and often performance
--------------------------------------------------------------------------------
*/

-- Select only the columns needed for a product list
SELECT product_id, name, price
FROM products;
-- Expected output: 12 rows with product_id, name, and price only

-- Select a single column
SELECT name
FROM customers;
-- Expected output: 12 customer names

/*
--------------------------------------------------------------------------------
4. FROM CLAUSE
--------------------------------------------------------------------------------
WHAT:
- FROM tells MySQL which table to read from

WITHOUT FROM:
- expressions can be selected directly
- table data requires FROM
--------------------------------------------------------------------------------
*/

SELECT 10 + 20 AS quick_math_example;
-- Expected output: 30

SELECT name, category
FROM products;
-- Expected output: product names and categories

/*
--------------------------------------------------------------------------------
5. COLUMN ALIAS
--------------------------------------------------------------------------------
WHAT:
- alias gives a temporary output name to a column or expression

WHY:
- makes reports more readable
- helps with calculated values

NOTES:
- AS is optional in MySQL
- alias does not rename the real column in the table
--------------------------------------------------------------------------------
*/

SELECT name AS product_name, price AS selling_price
FROM products;
-- Expected output: same data with report-friendly headers

SELECT total_amount AS order_value
FROM orders;
-- Expected output: order values under the alias order_value

/*
--------------------------------------------------------------------------------
6. TABLE ALIAS
--------------------------------------------------------------------------------
WHAT:
- gives a short temporary name to a table inside the query

WHY:
- useful for long names
- very useful in joins and subqueries
--------------------------------------------------------------------------------
*/

SELECT p.name, p.category, p.price
FROM products AS p;
-- Expected output: product details using p as a short alias

/*
--------------------------------------------------------------------------------
7. EXPRESSIONS IN SELECT
--------------------------------------------------------------------------------
WHAT:
- we can calculate new values while reading data

COMMON USES:
- arithmetic
- pricing analysis
- reporting values

IMPORTANT:
- the calculated output is not permanently stored unless you run UPDATE
--------------------------------------------------------------------------------
*/

SELECT
    name,
    price,
    stock,
    price * stock AS inventory_value
FROM products;
-- Expected output: each row includes calculated inventory_value

SELECT
    order_id,
    total_amount,
    total_amount * 0.18 AS estimated_tax
FROM orders;
-- Expected output: each order includes an estimated tax value

/*
--------------------------------------------------------------------------------
8. ARITHMETIC OPERATORS
--------------------------------------------------------------------------------
+   addition
-   subtraction
*   multiplication
/   division
%   remainder
--------------------------------------------------------------------------------
*/

SELECT 5 + 2 AS add_value;
SELECT 5 - 2 AS subtract_value;
SELECT 5 * 2 AS multiply_value;
SELECT 5 / 2 AS divide_value;
SELECT 5 % 2 AS remainder_value;
-- Expected output:
-- add_value = 7
-- subtract_value = 3
-- multiply_value = 10
-- divide_value = 2.5000
-- remainder_value = 1

/*
--------------------------------------------------------------------------------
9. COMPARISON OPERATORS
--------------------------------------------------------------------------------
=    equal to
>    greater than
<    less than
>=   greater than or equal to
<=   less than or equal to
<>   not equal to
!=   not equal to
--------------------------------------------------------------------------------
*/

SELECT *
FROM products
WHERE price > 3000;
-- Expected output: products priced above 3000

SELECT *
FROM employees
WHERE salary >= 90000;
-- Expected output: employees earning 90000 or more

SELECT *
FROM customers
WHERE city <> 'Mumbai';
-- Expected output: non-Mumbai customers, but NULL city will not match this comparison

/*
--------------------------------------------------------------------------------
10. LOGICAL OPERATORS
--------------------------------------------------------------------------------
AND:
- both conditions must be true

OR:
- at least one condition must be true

NOT:
- reverses a condition
--------------------------------------------------------------------------------
*/

SELECT *
FROM products
WHERE category = 'Electronics'
  AND stock > 0;
-- Expected output: electronics products that are in stock

SELECT *
FROM orders
WHERE status = 'Pending'
   OR status = 'Shipped';
-- Expected output: pending and shipped orders

SELECT *
FROM products
WHERE NOT stock = 0;
-- Expected output: all products except Planner 2026

/*
--------------------------------------------------------------------------------
11. WHERE CLAUSE
--------------------------------------------------------------------------------
WHAT:
- WHERE filters rows before they are returned

WHY:
- real queries rarely need every row

IMPORTANT:
- WHERE filters rows, not groups
--------------------------------------------------------------------------------
*/

SELECT customer_id, name, city
FROM customers
WHERE city = 'Delhi';
-- Expected output: Delhi customers only

/*
--------------------------------------------------------------------------------
12. DISTINCT
--------------------------------------------------------------------------------
WHAT:
- DISTINCT removes duplicate rows from the selected output

IMPORTANT:
- DISTINCT applies to the full selected row
- if you select multiple columns, the full combination is checked
--------------------------------------------------------------------------------
*/

SELECT DISTINCT category
FROM products;
-- Expected output: one row per product category

SELECT DISTINCT city
FROM customers;
-- Expected output: one row per city value, including one NULL if present

/*
--------------------------------------------------------------------------------
13. IN AND BETWEEN
--------------------------------------------------------------------------------
IN:
- checks membership in a list

BETWEEN:
- checks whether a value lies inside an inclusive range
--------------------------------------------------------------------------------
*/

SELECT name, city
FROM customers
WHERE city IN ('Mumbai', 'Bangalore');
-- Expected output: customers from Mumbai or Bangalore

SELECT name, price
FROM products
WHERE price BETWEEN 500 AND 3000;
-- Expected output: products priced between 500 and 3000 inclusive

/*
--------------------------------------------------------------------------------
14. LIKE AND NULL FILTERS
--------------------------------------------------------------------------------
LIKE:
- searches text patterns

IS NULL:
- checks missing values correctly

IS NOT NULL:
- checks present values correctly
--------------------------------------------------------------------------------
*/

SELECT customer_id, name, email
FROM customers
WHERE email LIKE '%@gmail.com';
-- Expected output: customers with Gmail addresses

SELECT customer_id, name, city
FROM customers
WHERE city IS NULL;
-- Expected output: customers with missing city

SELECT customer_id, name, city
FROM customers
WHERE city IS NOT NULL;
-- Expected output: customers with present city values

/*
--------------------------------------------------------------------------------
15. ORDER BY
--------------------------------------------------------------------------------
WHAT:
- ORDER BY sorts the final result set

NOTES:
- ASC is default
- DESC reverses sort order
- multiple sort columns are allowed
--------------------------------------------------------------------------------
*/

SELECT name, price
FROM products
ORDER BY price DESC;
-- Expected output: most expensive product first

SELECT emp_id, name, dept_id, salary
FROM employees
ORDER BY dept_id ASC, salary DESC;
-- Expected output: employees grouped by dept_id, highest salary first inside each department

/*
--------------------------------------------------------------------------------
16. LIMIT AND OFFSET
--------------------------------------------------------------------------------
WHAT:
- LIMIT restricts the number of returned rows
- OFFSET skips rows before returning them

WHY:
- useful for pagination and top-N reports
--------------------------------------------------------------------------------
*/

SELECT order_id, total_amount
FROM orders
ORDER BY total_amount DESC
LIMIT 3;
-- Expected output: top 3 highest-value orders

SELECT order_id, total_amount
FROM orders
ORDER BY total_amount DESC
LIMIT 3 OFFSET 2;
-- Expected output: 3rd, 4th, and 5th highest-value orders

/*
--------------------------------------------------------------------------------
17. COMBINING CLAUSES
--------------------------------------------------------------------------------
Most useful SQL queries combine:
- SELECT
- FROM
- WHERE
- ORDER BY
- LIMIT
--------------------------------------------------------------------------------
*/

SELECT product_id, name, category, price, stock
FROM products
WHERE category IN ('Electronics', 'Furniture')
  AND stock > 0
ORDER BY price DESC, name ASC
LIMIT 5;
-- Expected output: the 5 most expensive in-stock Electronics and Furniture products

/*
--------------------------------------------------------------------------------
18. COMMON MISTAKES
--------------------------------------------------------------------------------
1. Using = NULL instead of IS NULL
2. Using LIMIT without ORDER BY for top-N logic
3. Forgetting parentheses when mixing AND and OR
4. Overusing SELECT *
--------------------------------------------------------------------------------
*/

SELECT customer_id, name, city
FROM customers
WHERE city = NULL;
-- Expected output: no rows, because = NULL is not valid NULL comparison logic

SELECT customer_id, name, city
FROM customers
WHERE city IS NULL;
-- Expected output: correct NULL matches

/*
--------------------------------------------------------------------------------
19. INTERVIEW TIPS
--------------------------------------------------------------------------------
- LIMIT without ORDER BY is not a true "top" result
- NULL is never matched with = NULL
- DISTINCT removes duplicates, but does not summarize data
- WHERE filters rows before output
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
20. REAL-WORLD PRACTICE QUERIES
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
*/

-- E-commerce style query
SELECT order_id, customer_id, order_date, total_amount
FROM orders
WHERE status = 'Delivered'
  AND total_amount > 3000
ORDER BY order_date DESC;
-- Expected output: delivered orders above 3000 sorted from newest to oldest

-- HR style query
SELECT emp_id, name, hire_date, salary
FROM employees
WHERE hire_date >= '2022-01-01'
ORDER BY salary DESC;
-- Expected output: employees hired in 2022 or later, highest salary first

/*
--------------------------------------------------------------------------------
21. LEARNING CHECKLIST FOR THIS TOPIC
--------------------------------------------------------------------------------
After completing this topic, you should be able to:

1. Read all rows from a table.
2. Select only required columns.
3. Give readable aliases to columns and expressions.
4. Filter rows using WHERE.
5. Compare text, numbers, and dates.
6. Combine conditions using AND, OR, and NOT.
7. Use IN for multiple allowed values.
8. Use BETWEEN for inclusive ranges.
9. Use LIKE for text pattern matching.
10. Handle NULL values using IS NULL and IS NOT NULL.
11. Remove duplicate output rows using DISTINCT.
12. Sort results using ORDER BY.
13. Return top-N rows using LIMIT.
14. Write clean business-style reporting queries.
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
22. SQL CLAUSE WRITING ORDER VS EXECUTION ORDER
--------------------------------------------------------------------------------
WRITING ORDER:

SELECT
FROM
WHERE
ORDER BY
LIMIT

LOGICAL EXECUTION IDEA:

1. FROM      -> choose the table
2. WHERE     -> filter rows
3. SELECT    -> choose output columns or expressions
4. DISTINCT  -> remove duplicates from selected output
5. ORDER BY  -> sort final output
6. LIMIT     -> return limited rows

WHY THIS MATTERS:
- WHERE cannot use a SELECT alias in many SQL situations because WHERE is
  logically evaluated before SELECT.
- ORDER BY can usually use a SELECT alias because sorting happens after SELECT.
--------------------------------------------------------------------------------
*/

SELECT
    name,
    price * stock AS inventory_value
FROM products
WHERE price * stock > 20000
ORDER BY inventory_value DESC;
-- Expected output: products whose calculated inventory value is above 20000

/*
--------------------------------------------------------------------------------
23. TEXT FILTERING DETAILS WITH LIKE
--------------------------------------------------------------------------------
WILDCARDS:

%  -> zero or more characters
_  -> exactly one character

COMMON PATTERNS:

'A%'      -> starts with A
'%a'      -> ends with a
'%pen%'   -> contains pen
'_a%'     -> second character is a

NOTE:
- LIKE is very useful for beginner text search.
- For large production tables, leading wildcard searches like '%text' can be slow.
--------------------------------------------------------------------------------
*/

-- Customers whose names start with A
SELECT customer_id, name
FROM customers
WHERE name LIKE 'A%';
-- Expected output: customer names beginning with A

-- Products that contain the word Desk anywhere in the product name
SELECT product_id, name, category
FROM products
WHERE name LIKE '%Desk%';
-- Expected output: Standing Desk and Desk Lamp

-- Customers whose email is a Gmail address
SELECT customer_id, name, email
FROM customers
WHERE email LIKE '%@gmail.com';
-- Expected output: customers using Gmail addresses

-- Products where the second character in the name is the letter e
SELECT product_id, name
FROM products
WHERE name LIKE '_e%';
-- Expected output: names where the second character is e

/*
--------------------------------------------------------------------------------
24. NUMBER, TEXT, AND DATE FILTERING
--------------------------------------------------------------------------------
NUMBERS:
- Do not put numeric values in quotes unless there is a reason.

TEXT:
- Put text values inside single quotes.
- Text comparison can depend on collation settings.

DATES:
- Use the standard format 'YYYY-MM-DD'.
- BETWEEN includes both start and end values.
--------------------------------------------------------------------------------
*/

-- Number filtering
SELECT product_id, name, price
FROM products
WHERE price >= 1000
ORDER BY price ASC;
-- Expected output: products priced 1000 or above

-- Text filtering
SELECT order_id, status, total_amount
FROM orders
WHERE status = 'Delivered';
-- Expected output: delivered orders only

-- Date filtering
SELECT order_id, order_date, total_amount
FROM orders
WHERE order_date BETWEEN '2024-04-01' AND '2024-04-07'
ORDER BY order_date ASC;
-- Expected output: orders from 1 Apr 2024 through 7 Apr 2024

/*
--------------------------------------------------------------------------------
25. AND / OR PRECEDENCE AND PARENTHESES
--------------------------------------------------------------------------------
IMPORTANT:
- AND is evaluated before OR.
- Use parentheses whenever mixed AND and OR logic appears in a query.

BAD HABIT:
Writing mixed logic without parentheses and hoping the database understands
the business meaning.

GOOD HABIT:
Use parentheses to make the business rule clear.
--------------------------------------------------------------------------------
*/

-- Business rule:
-- Find in-stock Electronics or in-stock Furniture products.
SELECT product_id, name, category, stock
FROM products
WHERE (category = 'Electronics' OR category = 'Furniture')
  AND stock > 0
ORDER BY category, name;
-- Expected output: in-stock products from either Electronics or Furniture

-- Business rule:
-- Find high-value delivered or high-value shipped orders.
SELECT order_id, status, total_amount
FROM orders
WHERE (status = 'Delivered' OR status = 'Shipped')
  AND total_amount >= 5000
ORDER BY total_amount DESC;
-- Expected output: delivered or shipped orders with amount at least 5000

/*
--------------------------------------------------------------------------------
26. NULL FILTERING RULES
--------------------------------------------------------------------------------
IMPORTANT:
- NULL means missing or unknown.
- NULL is not equal to anything, not even another NULL.
- Use IS NULL and IS NOT NULL.

INCORRECT:
WHERE city = NULL

CORRECT:
WHERE city IS NULL
--------------------------------------------------------------------------------
*/

-- Customers where city is missing
SELECT customer_id, name, city
FROM customers
WHERE city IS NULL;
-- Expected output: customers with missing city values

-- Customers where city is available
SELECT customer_id, name, city
FROM customers
WHERE city IS NOT NULL
ORDER BY city ASC;
-- Expected output: customers with city values sorted by city

-- Projects that are still active because end_date is missing
SELECT project_id, project_name, start_date, end_date
FROM projects
WHERE end_date IS NULL
ORDER BY start_date ASC;
-- Expected output: active projects with no end date

/*
--------------------------------------------------------------------------------
27. DISTINCT PRACTICE
--------------------------------------------------------------------------------
DISTINCT removes duplicate rows after SELECT chooses the output columns.

If one column is selected:
- duplicate values from that column are removed.

If multiple columns are selected:
- duplicate combinations are removed.
--------------------------------------------------------------------------------
*/

-- Unique product categories
SELECT DISTINCT category
FROM products
ORDER BY category;
-- Expected output: one row per category

-- Unique order statuses
SELECT DISTINCT status
FROM orders
ORDER BY status;
-- Expected output: one row per order status

-- Unique customer city and email domain style cannot be done cleanly yet
-- without scalar functions, so that belongs in the scalar functions topic.

/*
--------------------------------------------------------------------------------
28. TOP-N REPORTING PATTERNS
--------------------------------------------------------------------------------
Top-N reports should normally use ORDER BY with LIMIT.

QUESTION:
What are the top 5 most expensive products?

PATTERN:
ORDER BY metric DESC
LIMIT N
--------------------------------------------------------------------------------
*/

-- Top 5 expensive products
SELECT product_id, name, category, price
FROM products
ORDER BY price DESC
LIMIT 5;
-- Expected output: 5 products with highest price

-- Top 3 highest-value orders
SELECT order_id, customer_id, total_amount, status
FROM orders
ORDER BY total_amount DESC
LIMIT 3;
-- Expected output: 3 orders with highest total_amount

-- Lowest stock products that still have stock available
SELECT product_id, name, stock
FROM products
WHERE stock > 0
ORDER BY stock ASC
LIMIT 5;
-- Expected output: 5 in-stock products with lowest stock

/*
--------------------------------------------------------------------------------
29. PRACTICE QUESTIONS
--------------------------------------------------------------------------------
Try writing these queries before checking examples below:

1. Show all products in the Electronics category.
2. Show products with stock equal to 0.
3. Show customers from Mumbai or Delhi.
4. Show orders that are not Cancelled.
5. Show products priced between 500 and 5000.
6. Show employees hired before 2021.
7. Show customers with Gmail email addresses.
8. Show top 3 highest salary employees.
9. Show unique order statuses.
10. Show active projects where end_date is NULL.
--------------------------------------------------------------------------------
*/

-- 1. Products in Electronics category
SELECT product_id, name, category, price
FROM products
WHERE category = 'Electronics';

-- 2. Products with zero stock
SELECT product_id, name, stock
FROM products
WHERE stock = 0;

-- 3. Customers from Mumbai or Delhi
SELECT customer_id, name, city
FROM customers
WHERE city IN ('Mumbai', 'Delhi');

-- 4. Orders that are not Cancelled
SELECT order_id, status, total_amount
FROM orders
WHERE status <> 'Cancelled';

-- 5. Products priced between 500 and 5000
SELECT product_id, name, price
FROM products
WHERE price BETWEEN 500 AND 5000
ORDER BY price ASC;

-- 6. Employees hired before 2021
SELECT emp_id, name, hire_date
FROM employees
WHERE hire_date < '2021-01-01'
ORDER BY hire_date ASC;

-- 7. Customers with Gmail addresses
SELECT customer_id, name, email
FROM customers
WHERE email LIKE '%@gmail.com';

-- 8. Top 3 highest salary employees
SELECT emp_id, name, salary
FROM employees
ORDER BY salary DESC
LIMIT 3;

-- 9. Unique order statuses
SELECT DISTINCT status
FROM orders
ORDER BY status;

-- 10. Active projects
SELECT project_id, project_name, start_date
FROM projects
WHERE end_date IS NULL
ORDER BY start_date ASC;

/*
--------------------------------------------------------------------------------
30. INTERVIEW-STYLE QUESTIONS AND ANSWERS
--------------------------------------------------------------------------------
Q1. What is the difference between WHERE and ORDER BY?
A1. WHERE filters rows. ORDER BY sorts the final result.

Q2. What is the difference between WHERE and LIMIT?
A2. WHERE decides which rows qualify. LIMIT decides how many final rows return.

Q3. Why should LIMIT be used with ORDER BY for top-N reports?
A3. Without ORDER BY, the returned rows are not guaranteed to be the highest,
    lowest, newest, or oldest according to business logic.

Q4. Why is = NULL wrong?
A4. NULL means unknown. Use IS NULL or IS NOT NULL to test missing values.

Q5. What does DISTINCT do?
A5. DISTINCT removes duplicate rows from the selected output.

Q6. What is the difference between IN and OR?
A6. IN is cleaner when checking one column against many possible values.
    OR is more flexible for different columns or different conditions.

Q7. Is BETWEEN inclusive?
A7. Yes. BETWEEN includes both boundary values.

Q8. Why avoid SELECT * in reports?
A8. It can return unnecessary columns, reduce readability, and make output
    unstable when table structure changes.
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
31. MINI PROJECT: BASIC E-COMMERCE ANALYSIS
--------------------------------------------------------------------------------
SCENARIO:
You are a junior data analyst. The business wants a quick report from the
orders, customers, and products data using only querying and filtering skills.

TASKS:
1. Find all delivered orders.
2. Find high-value orders above 5000.
3. Find pending or shipped orders.
4. Find products that need restocking.
5. Find customers whose city is missing.
6. Find top 5 expensive products.
--------------------------------------------------------------------------------
*/

-- 1. Delivered orders
SELECT order_id, customer_id, order_date, total_amount
FROM orders
WHERE status = 'Delivered'
ORDER BY order_date ASC;

-- 2. High-value orders above 5000
SELECT order_id, customer_id, total_amount, status
FROM orders
WHERE total_amount > 5000
ORDER BY total_amount DESC;

-- 3. Pending or shipped orders
SELECT order_id, customer_id, status, order_date
FROM orders
WHERE status IN ('Pending', 'Shipped')
ORDER BY order_date ASC;

-- 4. Products that need restocking
SELECT product_id, name, category, stock
FROM products
WHERE stock <= 10
ORDER BY stock ASC, name ASC;

-- 5. Customers with missing city
SELECT customer_id, name, email, city
FROM customers
WHERE city IS NULL;

-- 6. Top 5 expensive products
SELECT product_id, name, category, price
FROM products
ORDER BY price DESC
LIMIT 5;

/*
--------------------------------------------------------------------------------
32. MINI PROJECT: BASIC HR ANALYSIS
--------------------------------------------------------------------------------
SCENARIO:
The HR team wants simple employee lists using only SELECT, WHERE, ORDER BY,
DISTINCT, and LIMIT.

TASKS:
1. Find employees earning 80000 or more.
2. Find employees hired from 2022 onward.
3. Find employees without a manager.
4. Find employees from selected departments.
5. Find top 5 salaries.
--------------------------------------------------------------------------------
*/

-- 1. Employees earning 80000 or more
SELECT emp_id, name, dept_id, salary
FROM employees
WHERE salary >= 80000
ORDER BY salary DESC;

-- 2. Employees hired from 2022 onward
SELECT emp_id, name, hire_date
FROM employees
WHERE hire_date >= '2022-01-01'
ORDER BY hire_date ASC;

-- 3. Employees without a manager
SELECT emp_id, name, manager_id
FROM employees
WHERE manager_id IS NULL;

-- 4. Employees from Engineering, Finance, or Sales department IDs
SELECT emp_id, name, dept_id, salary
FROM employees
WHERE dept_id IN (10, 30, 40)
ORDER BY dept_id ASC, salary DESC;

-- 5. Top 5 salaries
SELECT emp_id, name, salary
FROM employees
ORDER BY salary DESC
LIMIT 5;

/*
--------------------------------------------------------------------------------
33. FINAL REVISION SUMMARY
--------------------------------------------------------------------------------
Most important commands and clauses from this topic:

SELECT      -> choose output columns or expressions
FROM        -> choose the table
WHERE       -> filter rows
DISTINCT    -> remove duplicate selected rows
AND         -> both conditions must be true
OR          -> at least one condition must be true
NOT         -> reverse a condition
IN          -> match a list of values
BETWEEN     -> match an inclusive range
LIKE        -> match text patterns
IS NULL     -> find missing values
IS NOT NULL -> find present values
ORDER BY    -> sort final output
LIMIT       -> restrict returned row count
OFFSET      -> skip rows before returning results

NEXT TOPIC:
Move to MySQL patterns and set-based filtering after you are comfortable with
all queries in this file.
--------------------------------------------------------------------------------
*/
