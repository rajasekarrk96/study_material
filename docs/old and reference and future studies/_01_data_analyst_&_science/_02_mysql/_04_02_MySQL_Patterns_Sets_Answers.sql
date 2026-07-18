-- ############################################################
-- FILE: 04_MySQL_Patterns_Sets_Answers.sql
-- ############################################################

/*
============================================================
  MySQL Patterns_Sets - Full Answers
  File: 04_MySQL_Patterns_Sets_Answers.sql
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
-- SECTION 1: BASIC ANSWERS
-- ============================================================

/*
  ANS 1. Salary Range Filter
  --------------------------
  Approach:
    Step 1 - Read rows from employees.
    Step 2 - Use BETWEEN to keep salaries from 50000 through 90000.
    Step 3 - Return the requested columns.

  Dry Run:
    Asha Menon has salary 52000.00.
    52000.00 is between 50000 and 90000.
    Therefore the row is included.

  Alternative:
    salary >= 50000 AND salary <= 90000
*/
SELECT
    emp_id,                          -- Return employee id
    name,                            -- Return employee name
    salary                           -- Return salary being filtered
FROM employees                       -- Read rows from employees
WHERE salary BETWEEN 50000 AND 90000 -- Keep the inclusive salary band
ORDER BY salary;                     -- Sort from lowest qualifying salary upward
-- Verify Result:
-- Expected Output:
-- | emp_id | name         | salary   |
-- | 101    | Asha Menon   | 52000.00 |

/*
  ANS 2. Products Outside Band
  ----------------------------
  Approach:
    Step 1 - Read rows from products.
    Step 2 - Use NOT BETWEEN to exclude the 50 to 500 range.

  Dry Run:
    Pen has price 12.00.
    12.00 is outside the 50-500 range.
    Therefore Pen is included.
*/
SELECT
    product_id,                           -- Return product id
    name,                                 -- Return product name
    price                                 -- Return product price
FROM products                             -- Read rows from products
WHERE price NOT BETWEEN 50 AND 500        -- Keep prices outside the inclusive band
ORDER BY price;                           -- Sort from lowest price upward
-- Verify Result:
-- Expected Output:
-- | product_id | name    | price    |
-- | 502        | Pen     | 12.00    |

/*
  ANS 3. Department List Filter
  -----------------------------
  Approach:
    Step 1 - Read employees.
    Step 2 - Use IN to match two department ids.

  Dry Run:
    Balan Iyer has dept_id 10.
    10 appears in the IN list.
    Therefore the row is included.
*/
SELECT
    emp_id,                     -- Return employee id
    name,                       -- Return employee name
    dept_id                     -- Return department id
FROM employees                  -- Read rows from employees
WHERE dept_id IN (10, 40)       -- Keep department 10 and 40 rows
ORDER BY dept_id, name;         -- Sort by department then name
-- Verify Result:
-- Expected Output:
-- | emp_id | name        | dept_id |
-- | 102    | Balan Iyer  | 10      |

/*
  ANS 4. Excluding Cities
  -----------------------
  Approach:
    Step 1 - Read customers.
    Step 2 - Use NOT IN to remove Mumbai and Delhi.

  Dry Run:
    Meera Joshi has city Bangalore.
    Bangalore is not in the excluded list.
    Therefore the row is included.
*/
SELECT
    customer_id,                         -- Return customer id
    name,                                -- Return customer name
    city                                 -- Return city
FROM customers                           -- Read rows from customers
WHERE city NOT IN ('Mumbai', 'Delhi')    -- Exclude two cities
ORDER BY city, name;                     -- Sort alphabetically by city and name
-- Verify Result:
-- Expected Output:
-- | customer_id | name         | city      |
-- | 303         | Meera Joshi  | Bangalore |

/*
  ANS 5. Prefix Search
  --------------------
  Approach:
    Step 1 - Read employee names.
    Step 2 - Use LIKE 'A%' to match names beginning with A.

  Dry Run:
    Anita Rao begins with A.
    Therefore it matches the prefix condition.
*/
SELECT
    emp_id,                -- Return employee id
    name                   -- Return employee name
FROM employees             -- Read rows from employees
WHERE name LIKE 'A%'       -- Match names starting with A
ORDER BY name;             -- Sort alphabetically
-- Verify Result:
-- Expected Output:
-- | emp_id | name         |
-- | 101    | Asha Menon   |

/*
  ANS 6. Suffix Search
  --------------------
  Approach:
    Step 1 - Read product names.
    Step 2 - Use LIKE '%er' to match names ending in er.
*/
SELECT
    product_id,            -- Return product id
    name                   -- Return product name
FROM products              -- Read rows from products
WHERE name LIKE '%er'      -- Match names ending with er
ORDER BY name;             -- Sort alphabetically
-- Verify Result:
-- Expected Output:
-- | product_id | name    |
-- | 503        | Marker  |

/*
  ANS 7. Contains Search
  ----------------------
  Approach:
    Step 1 - Read customer rows.
    Step 2 - Use LIKE '%gmail%' for contains search.
*/
SELECT
    customer_id,             -- Return customer id
    name,                    -- Return customer name
    email                    -- Return email
FROM customers               -- Read rows from customers
WHERE email LIKE '%gmail%'   -- Match the gmail substring
ORDER BY customer_id;        -- Sort by customer id
-- Verify Result:
-- Expected Output:
-- | customer_id | name        | email                    |
-- | 301         | Asha Patel  | asha.patel@gmail.com     |

/*
  ANS 8. One-Character Wildcard
  -----------------------------
  Approach:
    Step 1 - Read product names.
    Step 2 - Use _ to enforce one character before o.
*/
SELECT
    name                 -- Return the product name only
FROM products            -- Read rows from products
WHERE name LIKE '_o%';   -- Match names with o in the second position
-- Verify Result:
-- Expected Output:
-- | name   |
-- | Folder |

/*
  ANS 9. Missing City
  -------------------
  Approach:
    Step 1 - Read customers.
    Step 2 - Use IS NULL because = NULL never works.
*/
SELECT
    customer_id,         -- Return customer id
    name,                -- Return customer name
    city                 -- Return city to prove it is NULL
FROM customers           -- Read rows from customers
WHERE city IS NULL;      -- Keep rows with missing city
-- Verify Result:
-- Expected Output:
-- | customer_id | name             | city |
-- | 310         | Manav Kulkarni   | NULL |

/*
  ANS 10. Sorted Premium Product Slice
  ------------------------------------
  Approach:
    Step 1 - Filter Electronics rows.
    Step 2 - Sort by price descending.
    Step 3 - Limit to three rows.
*/
SELECT
    product_id,                     -- Return product id
    name,                           -- Return product name
    price                           -- Return price for ranking
FROM products                       -- Read rows from products
WHERE category = 'Electronics'      -- Keep Electronics rows only
ORDER BY price DESC                 -- Highest price first
LIMIT 3;                            -- Return the top three rows
-- Verify Result:
-- Expected Output:
-- | product_id | name         | price    |
-- | 504        | Monitor      | 11500.00 |

-- ============================================================
-- SECTION 2: INTERMEDIATE ANSWERS
-- ============================================================

/*
  ANS 11. Date Range Orders
  -------------------------
  Approach:
    Step 1 - Read orders.
    Step 2 - Use BETWEEN with dates.
*/
SELECT
    order_id,                                        -- Return order id
    order_date,                                      -- Return order date
    total_amount                                     -- Return order amount
FROM orders                                          -- Read rows from orders
WHERE order_date BETWEEN '2024-04-03' AND '2024-04-09' -- Keep inclusive date range
ORDER BY order_date;                                -- Sort chronologically
-- Verify Result:
-- Expected Output:
-- Orders 403 through 409

/*
  ANS 12. Category and Price Band
  -------------------------------
  Approach:
    Step 1 - Filter Electronics category.
    Step 2 - Apply BETWEEN for price band.
*/
SELECT
    product_id,                                   -- Return product id
    name,                                         -- Return product name
    price                                         -- Return product price
FROM products                                     -- Read rows from products
WHERE category = 'Electronics'                    -- Keep Electronics rows
  AND price BETWEEN 1000 AND 10000               -- Keep the target price band
ORDER BY price;                                   -- Sort from lowest to highest price
-- Verify Result:
-- Expected Output:
-- Keyboard, Printer, Laptop Stand

/*
  ANS 13. REGEXP City Search
  --------------------------
  Approach:
    Step 1 - Read customer rows.
    Step 2 - Use REGEXP with ^ for start and alternation with |.
*/
SELECT
    customer_id,                    -- Return customer id
    name,                           -- Return customer name
    city                            -- Return city
FROM customers                      -- Read rows from customers
WHERE city REGEXP '^(M|B)'          -- Match city names beginning with M or B
ORDER BY city, name;                -- Sort by city then name
-- Verify Result:
-- Expected Output:
-- Mumbai and Bangalore customer rows

/*
  ANS 14. NOT LIKE Exclusion
  --------------------------
  Approach:
    Step 1 - Read products.
    Step 2 - Use NOT LIKE 'M%' to exclude names beginning with M.
*/
SELECT
    product_id,                 -- Return product id
    name                        -- Return product name
FROM products                   -- Read rows from products
WHERE name NOT LIKE 'M%'        -- Exclude names starting with M
ORDER BY name;                  -- Sort alphabetically
-- Verify Result:
-- Expected Output:
-- All product rows except Marker, Monitor, and Mouse Pad

/*
  ANS 15. Grouped Gmail Cities
  ----------------------------
  Approach:
    Step 1 - Filter to Gmail rows in WHERE.
    Step 2 - Group by city.
    Step 3 - Use HAVING for the group count rule.
*/
SELECT
    city,                               -- Grouping column
    COUNT(*) AS gmail_customer_count    -- Count Gmail customers in each city
FROM customers                          -- Read rows from customers
WHERE email LIKE '%@gmail.com'          -- Keep Gmail users only
  AND city IS NOT NULL                  -- Exclude NULL city values
GROUP BY city                           -- Build one group per city
HAVING COUNT(*) >= 2;                   -- Keep cities with at least two Gmail users
-- Verify Result:
-- Expected Output:
-- Mumbai = 2

/*
  ANS 16. Customers With Delivered Orders
  ---------------------------------------
  Approach:
    Step 1 - Read customers.
    Step 2 - Use EXISTS to check delivered-order presence.

  Alternative:
    customer_id IN (SELECT customer_id FROM orders WHERE status = 'Delivered')
*/
SELECT
    c.customer_id,                             -- Return customer id
    c.name                                     -- Return customer name
FROM customers AS c                            -- Read rows from customers
WHERE EXISTS (                                 -- Keep customers with at least one delivered order
    SELECT 1                                   -- EXISTS only checks whether a row exists
    FROM orders AS o                           -- Read rows from orders
    WHERE o.customer_id = c.customer_id        -- Match the outer customer
      AND o.status = 'Delivered'               -- Keep delivered orders only
)
ORDER BY c.customer_id;                        -- Sort by customer id
-- Verify Result:
-- Expected Output:
-- Customers tied to delivered orders

/*
  ANS 17. Products Sold In Active Orders
  --------------------------------------
  Approach:
    Step 1 - Join products to order_items.
    Step 2 - Join order_items to orders.
    Step 3 - Filter by Delivered or Shipped statuses.
    Step 4 - Use DISTINCT so repeated products appear once.
*/
SELECT DISTINCT
    p.product_id,                              -- Return product id
    p.name                                     -- Return product name
FROM products AS p                             -- Start from products
INNER JOIN order_items AS oi                   -- Join order_items to see sales
    ON p.product_id = oi.product_id            -- Match products to sold items
INNER JOIN orders AS o                         -- Join orders to inspect order status
    ON oi.order_id = o.order_id                -- Match order items to parent orders
WHERE o.status IN ('Delivered', 'Shipped')     -- Keep active-completion statuses
ORDER BY p.product_id;                         -- Sort by product id
-- Verify Result:
-- Expected Output:
-- Unique products sold in delivered or shipped orders

/*
  ANS 18. Deduplicated Customer Merge
  -----------------------------------
  Approach:
    Step 1 - Select customer rows from current_customers.
    Step 2 - UNION with archived_customers to remove duplicates.
*/
SELECT
    customer_name,                   -- Return customer name
    city                             -- Return city
FROM current_customers               -- Read current snapshot
UNION                                -- Deduplicate matching rows
SELECT
    customer_name,                   -- Return archived customer name
    city                             -- Return archived customer city
FROM archived_customers              -- Read archived snapshot
ORDER BY customer_name;              -- Sort the final merged result
-- Verify Result:
-- Expected Output:
-- Unique combined customer rows

/*
  ANS 19. Duplicate-Preserving Customer Merge
  -------------------------------------------
  Approach:
    Step 1 - Select current snapshot.
    Step 2 - UNION ALL with archived snapshot to keep duplicates.
*/
SELECT
    customer_name,                   -- Return customer name
    city                             -- Return city
FROM current_customers               -- Read current snapshot
UNION ALL                            -- Keep duplicate rows
SELECT
    customer_name,                   -- Return archived customer name
    city                             -- Return archived customer city
FROM archived_customers              -- Read archived snapshot
ORDER BY customer_name;              -- Sort the final merged result
-- Verify Result:
-- Expected Output:
-- Combined customer rows with duplicates still present

/*
  ANS 20. Paginated City Search
  -----------------------------
  Approach:
    Step 1 - Exclude NULL city values.
    Step 2 - Sort by city and then name.
    Step 3 - Skip two rows and take the next three.
*/
SELECT
    customer_id,                      -- Return customer id
    name,                             -- Return customer name
    city                              -- Return city
FROM customers                        -- Read rows from customers
WHERE city IS NOT NULL                -- Remove NULL city row
ORDER BY city ASC, name ASC           -- Create stable result order
LIMIT 3 OFFSET 2;                     -- Return rows 3, 4, and 5 from the sorted result
-- Verify Result:
-- Expected Output:
-- The third, fourth, and fifth rows in sorted city-name order

-- ============================================================
-- SECTION 3: ADVANCED ANSWERS
-- ============================================================

/*
  ANS 21. Project Budget Exclusion
  --------------------------------
  Approach:
    Step 1 - Read projects.
    Step 2 - Use NOT BETWEEN to exclude the 200000-700000 budget band.
*/
SELECT
    project_id,                                  -- Return project id
    project_name,                                -- Return project name
    budget                                       -- Return budget
FROM projects                                    -- Read rows from projects
WHERE budget NOT BETWEEN 200000 AND 700000       -- Keep projects outside the band
ORDER BY budget;                                 -- Sort by budget
-- Verify Result:
-- Expected Output:
-- Projects below 200000 or above 700000

/*
  ANS 22. Customers With No Orders
  --------------------------------
  Approach:
    Step 1 - Read customers.
    Step 2 - Use NOT EXISTS against orders.

  Complexity Note:
    With supporting indexes on orders.customer_id, this is usually efficient.
*/
SELECT
    c.customer_id,                               -- Return customer id
    c.name                                       -- Return customer name
FROM customers AS c                              -- Read rows from customers
WHERE NOT EXISTS (                               -- Keep customers with no related order row
    SELECT 1                                     -- EXISTS checks presence only
    FROM orders AS o                             -- Read rows from orders
    WHERE o.customer_id = c.customer_id          -- Match outer customer to orders
)
ORDER BY c.customer_id;                          -- Sort by customer id
-- Verify Result:
-- Expected Output:
-- Any customers absent from orders

/*
  ANS 23. Current Snapshot Only
  -----------------------------
  Approach:
    Step 1 - Return rows from current_customers.
    Step 2 - Exclude rows that also exist in archived_customers.

  Alternative:
    Use EXCEPT in newer MySQL environments if supported.
*/
SELECT
    c.customer_name,                             -- Return current customer name
    c.city                                       -- Return current city
FROM current_customers AS c                      -- Read current snapshot
WHERE NOT EXISTS (                               -- Keep rows absent from archive
    SELECT 1                                     -- Value is irrelevant
    FROM archived_customers AS a                 -- Read archived snapshot
    WHERE a.customer_name = c.customer_name      -- Match on customer name
      AND a.city = c.city                        -- Match on city
)
ORDER BY c.customer_name;                        -- Sort alphabetically
-- Verify Result:
-- Expected Output:
-- Current-only snapshot rows

/*
  ANS 24. Common Snapshot Rows
  ----------------------------
  Approach:
    Step 1 - Join the current and archived snapshots.
    Step 2 - Match on both customer_name and city.
    Step 3 - Use DISTINCT to avoid duplicate output if needed.

  Alternative:
    Use INTERSECT in supported MySQL versions.
*/
SELECT DISTINCT
    c.customer_name,                             -- Return shared customer name
    c.city                                       -- Return shared city
FROM current_customers AS c                      -- Read current snapshot
INNER JOIN archived_customers AS a               -- Join archived snapshot
    ON c.customer_name = a.customer_name         -- Match by name
   AND c.city = a.city                           -- Match by city
ORDER BY c.customer_name;                        -- Sort alphabetically
-- Verify Result:
-- Expected Output:
-- Asha Patel, Mumbai
-- David Kumar, Chennai
-- Rohan Singh, Delhi

/*
  ANS 25. Customer Domain Regex
  -----------------------------
  Approach:
    Step 1 - Read customer rows.
    Step 2 - Use REGEXP with two explicit domains.
*/
SELECT
    customer_id,                                 -- Return customer id
    name,                                        -- Return customer name
    email                                        -- Return email
FROM customers                                   -- Read rows from customers
WHERE email REGEXP '@gmail\\.com$|@outlook\\.com$' -- Match gmail.com or outlook.com domains
ORDER BY customer_id;                            -- Sort by customer id
-- Verify Result:
-- Expected Output:
-- Gmail and Outlook customer rows only

/*
  ANS 26. Literal Underscore Search
  ---------------------------------
  Approach:
    Step 1 - Create a helper table.
    Step 2 - Insert sample values.
    Step 3 - Use LIKE with ESCAPE so the underscore is treated literally.
*/
CREATE TABLE pattern_demo (
    label_text VARCHAR(50) NOT NULL              -- Store demo values
);

INSERT INTO pattern_demo (label_text) VALUES
('item_01'),
('itemA01'),
('item_02'),
('itemB02');

SELECT
    label_text                                   -- Return matching demo text
FROM pattern_demo                                -- Read rows from helper table
WHERE label_text LIKE 'item\\_%' ESCAPE '\\'     -- Treat underscore literally
ORDER BY label_text;                             -- Sort alphabetically
-- Verify Result:
-- Expected Output:
-- item_01
-- item_02

/*
  ANS 27. Delivered/High-Value Customer Join
  ------------------------------------------
  Approach:
    Step 1 - Join orders with customers.
    Step 2 - Filter by city list.
    Step 3 - Filter by delivered status and amount > 3000.
*/
SELECT
    o.order_id,                                  -- Return order id
    c.name AS customer_name,                     -- Return customer name
    c.city,                                      -- Return city
    o.total_amount                               -- Return order amount
FROM orders AS o                                 -- Start from orders
INNER JOIN customers AS c                        -- Join customers
    ON o.customer_id = c.customer_id             -- Match order to customer
WHERE c.city IN ('Mumbai', 'Bangalore')          -- Keep target cities
  AND o.status = 'Delivered'                     -- Keep delivered orders
  AND o.total_amount > 3000                      -- Keep high-value orders
ORDER BY o.total_amount DESC;                    -- Rank by amount
-- Verify Result:
-- Expected Output:
-- 408, Tarun Sethi, Mumbai, 18999.00
-- 403, Meera Joshi, Bangalore, 15999.00
-- 401, Asha Patel, Mumbai, 3499.00

/*
  ANS 28. Category Coverage by Sales
  ----------------------------------
  Approach:
    Step 1 - Join products with order_items.
    Step 2 - Use DISTINCT on category.
*/
SELECT DISTINCT
    p.category                                   -- Return category once
FROM products AS p                               -- Read rows from products
INNER JOIN order_items AS oi                     -- Join sold item rows
    ON p.product_id = oi.product_id              -- Match sold item to product
ORDER BY p.category;                             -- Sort alphabetically
-- Verify Result:
-- Expected Output:
-- Categories that appeared in order_items

/*
  ANS 29. Name Pattern With Multiple Conditions
  ---------------------------------------------
  Approach:
    Step 1 - Filter salary first conceptually.
    Step 2 - Match names that start with A or end with r.
    Step 3 - Use parentheses to preserve logic.

  Alternative:
    Use REGEXP '(^A|r$)' instead of two LIKE clauses.
*/
SELECT
    emp_id,                                      -- Return employee id
    name,                                        -- Return employee name
    salary                                       -- Return salary
FROM employees                                   -- Read rows from employees
WHERE (name LIKE 'A%' OR name LIKE '%r')         -- Match prefix A or suffix r
  AND salary > 50000                             -- Keep higher-salary rows
ORDER BY salary DESC;                            -- Sort highest salary first
-- Verify Result:
-- Expected Output:
-- Employees matching the name pattern and salary threshold

/*
  ANS 30. Ordered Multi-Category Shortlist
  ----------------------------------------
  Approach:
    Step 1 - Keep three categories using IN.
    Step 2 - Keep rows with stock above 20.
    Step 3 - Sort by category then price descending.
*/
SELECT
    product_id,                                  -- Return product id
    name,                                        -- Return product name
    category,                                    -- Return category
    price,                                       -- Return price
    stock                                        -- Return stock
FROM products                                    -- Read rows from products
WHERE category IN ('Electronics', 'Office', 'Accessories') -- Keep three categories
  AND stock > 20                                 -- Keep available products
ORDER BY category ASC, price DESC;               -- Sort by category then price
-- Verify Result:
-- Expected Output:
-- Ordered shortlist across three categories

-- ============================================================
-- SECTION 4: SCENARIO ANSWERS
-- ============================================================

/*
  ANS 31. E-commerce Merchandising Filter
  ---------------------------------------
  Approach:
    Step 1 - Keep Electronics and Office categories.
    Step 2 - Keep price in the required band.
    Step 3 - Keep in-stock rows.
    Step 4 - Sort by price descending.
*/
SELECT
    product_id,                                  -- Return product id
    name,                                        -- Return product name
    category,                                    -- Return category
    price,                                       -- Return price
    stock                                        -- Return stock
FROM products                                    -- Read rows from products
WHERE category IN ('Electronics', 'Office')      -- Keep target categories
  AND price BETWEEN 500 AND 10000               -- Respect the mid-price band
  AND stock > 0                                  -- Keep in-stock rows
ORDER BY price DESC;                             -- Highest price first
-- Verify Result:
-- Expected Output:
-- Printer, Laptop Stand, Keyboard, Desk Organizer

/*
  ANS 32. CRM Outreach List
  -------------------------
  Approach:
    Step 1 - Use REGEXP for email domain filtering.
    Step 2 - Use IN for metro cities.
*/
SELECT
    customer_id,                                 -- Return customer id
    name,                                        -- Return customer name
    email,                                       -- Return email
    city                                         -- Return city
FROM customers                                   -- Read rows from customers
WHERE email REGEXP '@gmail\\.com$|@outlook\\.com$' -- Match Gmail or Outlook domains
  AND city IN ('Mumbai', 'Delhi', 'Bangalore', 'Chennai') -- Keep target metro cities
ORDER BY city, name;                             -- Sort by city then name
-- Verify Result:
-- Expected Output:
-- Metro-city Gmail and Outlook users only

/*
  ANS 33. Order Monitoring
  ------------------------
  Approach:
    Step 1 - Use BETWEEN for the date window.
    Step 2 - Use NOT IN to exclude problem statuses.
*/
SELECT
    order_id,                                    -- Return order id
    order_date,                                  -- Return order date
    total_amount,                                -- Return amount
    status                                       -- Return status
FROM orders                                      -- Read rows from orders
WHERE order_date BETWEEN '2024-04-03' AND '2024-04-10' -- Keep date window
  AND status NOT IN ('Cancelled', 'Returned')    -- Exclude two statuses
ORDER BY order_date;                             -- Sort chronologically
-- Verify Result:
-- Expected Output:
-- Valid operational orders inside the requested date window

/*
  ANS 34. Snapshot Reconciliation
  -------------------------------
  Approach:
    Step 1 - Join both snapshot tables on name and city.
    Step 2 - Return the shared rows.

  Alternative:
    INTERSECT can express this directly in supported MySQL versions.
*/
SELECT DISTINCT
    c.customer_name,                             -- Return common customer name
    c.city                                       -- Return common city
FROM current_customers AS c                      -- Read current snapshot
INNER JOIN archived_customers AS a               -- Join archive snapshot
    ON c.customer_name = a.customer_name         -- Match name
   AND c.city = a.city                           -- Match city
ORDER BY c.customer_name;                        -- Sort alphabetically
-- Verify Result:
-- Expected Output:
-- Asha Patel, Mumbai
-- David Kumar, Chennai
-- Rohan Singh, Delhi

/*
  ANS 35. Recruitment Project Search
  ----------------------------------
  Approach:
    Step 1 - Search project names for Hiring or Payroll.
    Step 2 - Also include budgets below 250000.
    Step 3 - Combine the conditions with OR.
*/
SELECT
    project_id,                                  -- Return project id
    project_name,                                -- Return project name
    budget                                       -- Return budget
FROM projects                                    -- Read rows from projects
WHERE project_name REGEXP 'Hiring|Payroll'       -- Match two keyword families
   OR budget < 250000                            -- Also include small-budget projects
ORDER BY budget, project_name;                   -- Sort by budget then name
-- Verify Result:
-- Expected Output:
-- Payroll Upgrade
-- Campus Hiring Drive
-- Inventory Cleanup

-- ############################################################
-- END OF FILE: 04_MySQL_Patterns_Sets_Answers.sql
-- ############################################################
