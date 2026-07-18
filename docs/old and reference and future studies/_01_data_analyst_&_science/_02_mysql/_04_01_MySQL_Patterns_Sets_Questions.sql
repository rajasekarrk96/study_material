-- ############################################################
-- FILE: 04_MySQL_Patterns_Sets_Questions.sql
-- ############################################################

/*
============================================================
  MySQL Patterns_Sets - Practice Questions
  File: 04_MySQL_Patterns_Sets_Questions.sql
============================================================
  Instructions:
  - Run the SETUP section first before attempting questions
  - Write your answer below each question comment block
  - Do NOT look at the Answers file until you have tried
============================================================
*/

-- ============================================================
-- SETUP: Create and populate tables for questions
-- ============================================================
DROP DATABASE IF EXISTS mysql_questions;
CREATE DATABASE mysql_questions;
USE mysql_questions;

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(50) NOT NULL
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dept_id INT NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    hire_date DATE NOT NULL,
    manager_id INT NULL,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    budget DECIMAL(12,2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NULL
);

CREATE TABLE emp_projects (
    emp_id INT NOT NULL,
    project_id INT NOT NULL,
    role VARCHAR(50) NOT NULL,
    PRIMARY KEY (emp_id, project_id),
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    city VARCHAR(50),
    join_date DATE NOT NULL
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL
);

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE current_customers (
    customer_name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL
);

CREATE TABLE archived_customers (
    customer_name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL
);

INSERT INTO departments (dept_id, dept_name, location) VALUES
(10, 'Engineering', 'Bangalore'),
(20, 'Finance', 'Delhi'),
(30, 'Sales', 'Mumbai'),
(40, 'Human Resources', 'Chennai'),
(50, 'Operations', 'Hyderabad');

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

INSERT INTO current_customers (customer_name, city) VALUES
('Asha Patel', 'Mumbai'),
('Rohan Singh', 'Delhi'),
('Meera Joshi', 'Bangalore'),
('David Kumar', 'Chennai'),
('Priya Menon', 'Pune'),
('Tarun Sethi', 'Mumbai');

INSERT INTO archived_customers (customer_name, city) VALUES
('Rohan Singh', 'Delhi'),
('Kiran Das', 'Kolkata'),
('David Kumar', 'Chennai'),
('Latha R', 'Madurai'),
('Asha Patel', 'Mumbai'),
('Sonia Verma', 'Bhopal');

-- ============================================================
-- SECTION 1: BASIC QUESTIONS (10 Questions)
-- ============================================================

/*
  Q1. Salary Range Filter
  -----------------------
  Problem : Return employees whose salary is between 50000 and 90000 inclusive.
  Table(s) : employees
  Expected Output:
    emp_id, name, salary
    101, Asha Menon, 52000.00
    108, Nisha Kapoor, 90000.00
  Hint: Use BETWEEN.
*/
-- Write your answer here:

/*
  Q2. Products Outside Band
  -------------------------
  Problem : Return products whose price is not between 50 and 500.
  Table(s) : products
  Expected Output:
    product_id, name, price
    504, Monitor, 11500.00
    502, Pen, 12.00
  Hint: Use NOT BETWEEN.
*/
-- Write your answer here:

/*
  Q3. Department List Filter
  --------------------------
  Problem : Return employees who belong to department 10 or department 40.
  Table(s) : employees
  Expected Output:
    emp_id, name, dept_id
    102, Balan Iyer, 10
    106, Anita Rao, 40
  Hint: Use IN.
*/
-- Write your answer here:

/*
  Q4. Excluding Cities
  --------------------
  Problem : Return customers whose city is not Mumbai and not Delhi.
  Table(s) : customers
  Expected Output:
    customer_id, name, city
    303, Meera Joshi, Bangalore
    305, Priya Menon, Pune
  Hint: Use NOT IN.
*/
-- Write your answer here:

/*
  Q5. Prefix Search
  -----------------
  Problem : Return employees whose names start with A.
  Table(s) : employees
  Expected Output:
    emp_id, name
    101, Asha Menon
    109, Arjun Sethi
  Hint: Use LIKE with a prefix wildcard.
*/
-- Write your answer here:

/*
  Q6. Suffix Search
  -----------------
  Problem : Return products whose names end with er.
  Table(s) : products
  Expected Output:
    product_id, name
    503, Marker
    507, Printer
  Hint: Use LIKE with a suffix wildcard.
*/
-- Write your answer here:

/*
  Q7. Contains Search
  -------------------
  Problem : Return customers whose email contains gmail.
  Table(s) : customers
  Expected Output:
    customer_id, name, email
    301, Asha Patel, asha.patel@gmail.com
    311, Ira Bansal, ira.bansal@gmail.com
  Hint: Use LIKE with % on both sides.
*/
-- Write your answer here:

/*
  Q8. One-Character Wildcard
  --------------------------
  Problem : Return product names whose second letter is o.
  Table(s) : products
  Expected Output:
    name
    Folder
  Hint: Use the underscore wildcard.
*/
-- Write your answer here:

/*
  Q9. Missing City
  ----------------
  Problem : Return customers whose city is missing.
  Table(s) : customers
  Expected Output:
    customer_id, name, city
    310, Manav Kulkarni, NULL
  Hint: Use IS NULL.
*/
-- Write your answer here:

/*
  Q10. Sorted Premium Product Slice
  ---------------------------------
  Problem : Return the 3 most expensive products from the Electronics category.
  Table(s) : products
  Expected Output:
    product_id, name, price
    504, Monitor, 11500.00
    512, Laptop Stand, 1999.00
  Hint: Use WHERE, ORDER BY, and LIMIT.
*/
-- Write your answer here:

-- ============================================================
-- SECTION 2: INTERMEDIATE QUESTIONS (10 Questions)
-- ============================================================

/*
  Q11. Date Range Orders
  ----------------------
  Problem : Return orders placed between 2024-04-03 and 2024-04-09 inclusive.
  Table(s) : orders
  Expected Output:
    order_id, order_date, total_amount
    403, 2024-04-03, 15999.00
    409, 2024-04-09, 999.00
  Hint: Use BETWEEN with dates.
*/
-- Write your answer here:

/*
  Q12. Category and Price Band
  ----------------------------
  Problem : Return products from Electronics where price is between 1000 and 10000.
  Table(s) : products
  Expected Output:
    product_id, name, price
    505, Keyboard, 1700.00
    507, Printer, 8900.00
  Hint: Combine = with BETWEEN.
*/
-- Write your answer here:

/*
  Q13. REGEXP City Search
  -----------------------
  Problem : Return customers whose city starts with M or B.
  Table(s) : customers
  Expected Output:
    customer_id, name, city
    301, Asha Patel, Mumbai
    303, Meera Joshi, Bangalore
  Hint: Use REGEXP with alternation.
*/
-- Write your answer here:

/*
  Q14. NOT LIKE Exclusion
  -----------------------
  Problem : Return products whose names do not start with M.
  Table(s) : products
  Expected Output:
    product_id, name
    501, Notebook
    507, Printer
  Hint: Use NOT LIKE.
*/
-- Write your answer here:

/*
  Q15. Grouped Gmail Cities
  -------------------------
  Problem : Return city and count of Gmail customers for cities having at least 2 Gmail customers.
  Table(s) : customers
  Expected Output:
    city, gmail_customer_count
    Mumbai, 2
  Hint: Use WHERE, GROUP BY, and HAVING.
*/
-- Write your answer here:

/*
  Q16. Customers With Delivered Orders
  ------------------------------------
  Problem : Return customers who have at least one delivered order.
  Table(s) : customers, orders
  Expected Output:
    customer_id, name
    301, Asha Patel
    303, Meera Joshi
  Hint: Use IN or EXISTS.
*/
-- Write your answer here:

/*
  Q17. Products Sold In Active Orders
  -----------------------------------
  Problem : Return unique product names that appeared in Delivered or Shipped orders.
  Table(s) : products, order_items, orders
  Expected Output:
    product_id, name
    504, Monitor
    507, Printer
  Hint: Use JOIN plus DISTINCT.
*/
-- Write your answer here:

/*
  Q18. Deduplicated Customer Merge
  --------------------------------
  Problem : Combine current_customers and archived_customers into one unique result set.
  Table(s) : current_customers, archived_customers
  Expected Output:
    customer_name, city
    Asha Patel, Mumbai
    Sonia Verma, Bhopal
  Hint: Use UNION.
*/
-- Write your answer here:

/*
  Q19. Duplicate-Preserving Customer Merge
  ----------------------------------------
  Problem : Combine current_customers and archived_customers while preserving duplicates.
  Table(s) : current_customers, archived_customers
  Expected Output:
    customer_name, city
    Rohan Singh, Delhi
    Rohan Singh, Delhi
  Hint: Use UNION ALL.
*/
-- Write your answer here:

/*
  Q20. Paginated City Search
  --------------------------
  Problem : Return the 3rd, 4th, and 5th non-NULL customer-city rows after sorting by city and then name.
  Table(s) : customers
  Expected Output:
    customer_id, name, city
    ...depends on sorted order...
  Hint: Use ORDER BY with LIMIT and OFFSET.
*/
-- Write your answer here:

-- ============================================================
-- SECTION 3: ADVANCED QUESTIONS (10 Questions)
-- ============================================================

/*
  Q21. Project Budget Exclusion
  -----------------------------
  Problem : Return projects whose budget is not between 200000 and 700000.
  Table(s) : projects
  Expected Output:
    project_id, project_name, budget
    202, Mobile Commerce App, 800000.00
    207, Campus Hiring Drive, 90000.00
  Hint: Use NOT BETWEEN.
*/
-- Write your answer here:

/*
  Q22. Customers With No Orders
  -----------------------------
  Problem : Return customers who have never placed an order.
  Table(s) : customers, orders
  Expected Output:
    customer_id, name
    ...any customer ids absent from orders...
  Hint: Use NOT EXISTS.
*/
-- Write your answer here:

/*
  Q23. Current Snapshot Only
  --------------------------
  Problem : Return rows that exist in current_customers but not in archived_customers.
  Table(s) : current_customers, archived_customers
  Expected Output:
    customer_name, city
    Priya Menon, Pune
    Tarun Sethi, Mumbai
  Hint: Use EXCEPT if supported, otherwise use NOT EXISTS logic.
*/
-- Write your answer here:

/*
  Q24. Common Snapshot Rows
  -------------------------
  Problem : Return rows that exist in both current_customers and archived_customers.
  Table(s) : current_customers, archived_customers
  Expected Output:
    customer_name, city
    Asha Patel, Mumbai
    Rohan Singh, Delhi
  Hint: Use INTERSECT if supported, otherwise use INNER JOIN logic.
*/
-- Write your answer here:

/*
  Q25. Customer Domain Regex
  --------------------------
  Problem : Return customers whose email domain is gmail.com or outlook.com.
  Table(s) : customers
  Expected Output:
    customer_id, name, email
    301, Asha Patel, asha.patel@gmail.com
    304, David Kumar, david.kumar@outlook.com
  Hint: Use REGEXP with escaped dots.
*/
-- Write your answer here:

/*
  Q26. Literal Underscore Search
  ------------------------------
  Problem : Create a small helper table with values such as item_01 and itemA01,
            then return only the row with the literal underscore.
  Table(s) : create your own helper table
  Expected Output:
    label_text
    item_01
  Hint: Use LIKE ... ESCAPE.
*/
-- Write your answer here:

/*
  Q27. Delivered/High-Value Customer Join
  ---------------------------------------
  Problem : Return delivered orders above 3000 for customers in Mumbai or Bangalore.
  Table(s) : customers, orders
  Expected Output:
    order_id, customer_name, city, total_amount
    401, Asha Patel, Mumbai, 3499.00
    403, Meera Joshi, Bangalore, 15999.00
  Hint: Use JOIN, IN, and AND.
*/
-- Write your answer here:

/*
  Q28. Category Coverage by Sales
  -------------------------------
  Problem : Return distinct product categories that appear in order_items.
  Table(s) : products, order_items
  Expected Output:
    category
    Electronics
    Office
  Hint: Use JOIN and DISTINCT.
*/
-- Write your answer here:

/*
  Q29. Name Pattern With Multiple Conditions
  ------------------------------------------
  Problem : Return employees whose names start with A or end with r, and whose salary is above 50000.
  Table(s) : employees
  Expected Output:
    emp_id, name, salary
    101, Asha Menon, 52000.00
    109, Arjun Sethi, 98000.00
  Hint: Use REGEXP or combine LIKE patterns with parentheses.
*/
-- Write your answer here:

/*
  Q30. Ordered Multi-Category Shortlist
  -------------------------------------
  Problem : Return products from Electronics, Office, or Accessories with stock above 20,
            ordered by category and then price descending.
  Table(s) : products
  Expected Output:
    product_id, name, category, price, stock
    509, Mouse Pad, Accessories, 399.00, 150
    510, Desk Organizer, Office, 649.00, 35
  Hint: Use IN, AND, and ORDER BY.
*/
-- Write your answer here:

-- ============================================================
-- SECTION 4: REAL-WORLD SCENARIO PROBLEMS (5 Problems)
-- ============================================================

/*
  SCENARIO 1: E-commerce Merchandising Filter
  -------------------------------------------
  Background : A merchandising analyst needs a shortlist of products from
               Electronics and Office categories that are mid-priced and in stock.
  Task        : Return products in Electronics or Office with price between
               500 and 10000 and stock greater than 0, sorted by price descending.
  Table(s)    : products
  Expected Output:
    product_id, name, category, price, stock
    507, Printer, Electronics, 8900.00, 8
    512, Laptop Stand, Electronics, 1999.00, 25
  Constraints : Make sure your final logic truly respects the price band.
*/
-- Write your answer here:

/*
  SCENARIO 2: CRM Outreach List
  -----------------------------
  Background : The CRM team wants Gmail and Outlook users from metro cities.
  Task        : Return customers whose email domain is gmail.com or outlook.com
               and whose city is Mumbai, Delhi, Bangalore, or Chennai.
  Table(s)    : customers
  Expected Output:
    customer_id, name, email, city
    301, Asha Patel, asha.patel@gmail.com, Mumbai
    303, Meera Joshi, meera.joshi@gmail.com, Bangalore
  Constraints : Use REGEXP for the domain check.
*/
-- Write your answer here:

/*
  SCENARIO 3: Order Monitoring
  ----------------------------
  Background : Operations wants a list of non-cancelled orders in a date window.
  Task        : Return orders placed between 2024-04-03 and 2024-04-10
               excluding Cancelled and Returned statuses.
  Table(s)    : orders
  Expected Output:
    order_id, order_date, total_amount, status
    403, 2024-04-03, 15999.00, Delivered
    405, 2024-04-05, 4999.00, Shipped
  Constraints : Use BETWEEN and NOT IN.
*/
-- Write your answer here:

/*
  SCENARIO 4: Snapshot Reconciliation
  -----------------------------------
  Background : The data team wants to know who appears in both the current
               and archived customer snapshots.
  Task        : Return common rows across current_customers and archived_customers.
  Table(s)    : current_customers, archived_customers
  Expected Output:
    customer_name, city
    Asha Patel, Mumbai
    Rohan Singh, Delhi
  Constraints : Use INTERSECT if supported, otherwise solve using a join.
*/
-- Write your answer here:

/*
  SCENARIO 5: Recruitment Project Search
  --------------------------------------
  Background : HR wants projects related to hiring or payroll, or projects
               whose budget is under 250000.
  Task        : Return projects whose name contains 'Hiring' or 'Payroll'
               or whose budget is below 250000.
  Table(s)    : projects
  Expected Output:
    project_id, project_name, budget
    203, Payroll Upgrade, 220000.00
    207, Campus Hiring Drive, 90000.00
  Constraints : Use LIKE or REGEXP plus OR logic.
*/
-- Write your answer here:

-- ############################################################
-- END OF FILE: 04_MySQL_Patterns_Sets_Questions.sql
-- ############################################################
