/*
============================================================
  MySQL Scalar_Functions - Practice Questions
  File: _05_01_Scalar_Functions_Questions.sql
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
-- SECTION 1: BASIC QUESTIONS (10 Questions)
-- ============================================================

/*
  Q1. Uppercase Employee Names
  ----------------------------
  Problem : Show employee names in uppercase.
  Table(s) : employees
  Expected Output:
    upper_name
    ASHA MENON
    BALAN IYER
  Hint: Use UPPER.
*/
-- Write your answer here:

/*
  Q2. Lowercase Product Names
  ---------------------------
  Problem : Show product names in lowercase.
  Table(s) : products
  Expected Output:
    lower_product_name
    notebook
    pen
  Hint: Use LOWER.
*/
-- Write your answer here:

/*
  Q3. Name Lengths
  ----------------
  Problem : Show each employee name and the length of the name.
  Table(s) : employees
  Expected Output:
    name, name_length
    Asha Menon, 10
    Dev Roy, 7
  Hint: Use LENGTH or CHAR_LENGTH.
*/
-- Write your answer here:

/*
  Q4. First Three Characters
  --------------------------
  Problem : Show the first 3 characters of each product name.
  Table(s) : products
  Expected Output:
    name, first_three_chars
    Notebook, Not
    Monitor, Mon
  Hint: Use LEFT or SUBSTRING.
*/
-- Write your answer here:

/*
  Q5. Rounded Price
  -----------------
  Problem : Show product name and price rounded to 1 decimal place.
  Table(s) : products
  Expected Output:
    name, rounded_price
    Notebook, 45.8
    Pen, 12.4
  Hint: Use ROUND.
*/
-- Write your answer here:

/*
  Q6. Truncated Price
  -------------------
  Problem : Show product name and price truncated to 1 decimal place.
  Table(s) : products
  Expected Output:
    name, truncated_price
    Notebook, 45.7
    Pen, 12.4
  Hint: Use TRUNCATE.
*/
-- Write your answer here:

/*
  Q7. Absolute Value
  ------------------
  Problem : Show the absolute value of -250.
  Table(s) : none
  Expected Output:
    absolute_value
    250
  Hint: Use ABS.
*/
-- Write your answer here:

/*
  Q8. Square Root
  ---------------
  Problem : Show the square root of 81.
  Table(s) : none
  Expected Output:
    square_root_value
    9
  Hint: Use SQRT.
*/
-- Write your answer here:

/*
  Q9. Hire Year
  -------------
  Problem : Show employee name and hire year only.
  Table(s) : employees
  Expected Output:
    name, hire_year
    Asha Menon, 2024
    Arjun Sethi, 2016
  Hint: Use YEAR.
*/
-- Write your answer here:

/*
  Q10. Current Date and Time
  --------------------------
  Problem : Show current system date and time.
  Table(s) : none
  Expected Output:
    current_datetime
    <current timestamp>
  Hint: Use NOW.
*/
-- Write your answer here:

-- ============================================================
-- SECTION 2: INTERMEDIATE QUESTIONS (10 Questions)
-- ============================================================

/*
  Q11. Employee Label
  -------------------
  Problem : Show employee name and a new column full_label as "name - dept_id".
  Table(s) : employees
  Expected Output:
    name, full_label
    Asha Menon, Asha Menon - 40
  Hint: Use CONCAT.
*/
-- Write your answer here:

/*
  Q12. Exact-Length Names
  -----------------------
  Problem : Show employee names whose length is exactly 9 characters.
  Table(s) : employees
  Expected Output:
    name
    Anita Rao
  Hint: Use LENGTH in WHERE.
*/
-- Write your answer here:

/*
  Q13. Price Remainder
  --------------------
  Problem : Show product name and the remainder when price is divided by 10.
  Table(s) : products
  Expected Output:
    name, remainder_value
    Notebook, 5.75
  Hint: Use MOD.
*/
-- Write your answer here:

/*
  Q14. Rounded Salaries
  ---------------------
  Problem : Show employee name and salary rounded to the nearest whole number.
  Table(s) : employees
  Expected Output:
    name, rounded_salary
    Asha Menon, 52001
  Hint: Use ROUND with 0 decimals.
*/
-- Write your answer here:

/*
  Q15. Greater of Price and Discount
  ----------------------------------
  Problem : Show product name and the greater value between price and discount.
  Table(s) : products
  Expected Output:
    name, greater_value
    Notebook, 45.75
  Hint: Use GREATEST and protect NULL discount.
*/
-- Write your answer here:

/*
  Q16. Smaller of Price and Discount
  ----------------------------------
  Problem : Show product name and the smaller value between price and discount.
  Table(s) : products
  Expected Output:
    name, smaller_value
    Notebook, 5.00
  Hint: Use LEAST and protect NULL discount.
*/
-- Write your answer here:

/*
  Q17. Safe Bonus
  ---------------
  Problem : Show employee name and bonus, replacing NULL bonus with 0.
  Table(s) : employees
  Expected Output:
    name, bonus_value
    Balan Iyer, 0
  Hint: Use IFNULL.
*/
-- Write your answer here:

/*
  Q18. Total Pay
  --------------
  Problem : Show employee name and total_pay as salary + bonus, treating NULL bonus as 0.
  Table(s) : employees
  Expected Output:
    name, total_pay
    Balan Iyer, 78000.40
  Hint: Use IFNULL or COALESCE.
*/
-- Write your answer here:

/*
  Q19. Formatted Join Date
  ------------------------
  Problem : Show employee name and formatted hire_date as dd-mm-yyyy.
  Table(s) : employees
  Expected Output:
    name, formatted_hire_date
    Asha Menon, 15-01-2024
  Hint: Use DATE_FORMAT.
*/
-- Write your answer here:

/*
  Q20. Days Since Hire
  --------------------
  Problem : Show employee name and number of days from hire_date to today.
  Table(s) : employees
  Expected Output:
    name, days_since_hire
    <non-negative integers>
  Hint: Use DATEDIFF.
*/
-- Write your answer here:

-- ============================================================
-- SECTION 3: ADVANCED QUESTIONS (10 Questions)
-- ============================================================

/*
  Q21. Salary Status
  ------------------
  Problem : Show employee name and a status column:
            if salary >= 60000 then 'HIGH', otherwise 'NORMAL'.
  Table(s) : employees
  Expected Output:
    name, salary_status
    Ravi Shah, NORMAL
    Arjun Sethi, HIGH
  Hint: Use IF or CASE.
*/
-- Write your answer here:

/*
  Q22. Price After Discount
  -------------------------
  Problem : Show product name and price_after_discount as price - discount,
            treating NULL discount as 0.
  Table(s) : products
  Expected Output:
    name, price_after_discount
    Pen, 12.40
    Monitor, 11000.80
  Hint: Use IFNULL or COALESCE.
*/
-- Write your answer here:

/*
  Q23. Email Username
  -------------------
  Problem : Show employee name and the first_email_part before the @ symbol.
  Table(s) : employees
  Expected Output:
    name, first_email_part
    Asha Menon, asha.menon
  Hint: Use SUBSTRING and INSTR or LOCATE.
*/
-- Write your answer here:

/*
  Q24. Cleaned City
  -----------------
  Problem : Show employee name and a cleaned version of city where extra spaces are removed.
  Table(s) : employees
  Expected Output:
    name, cleaned_city
    Asha Menon, Mumbai
    Anita Rao, Pune
  Hint: Use TRIM.
*/
-- Write your answer here:

/*
  Q25. Longest Names First
  ------------------------
  Problem : Show employee names ordered by the length of the name in descending order.
  Table(s) : employees
  Expected Output:
    name
    Tarun Malhotra
    Asha Menon
  Hint: Use LENGTH in ORDER BY.
*/
-- Write your answer here:

/*
  Q26. Project Start Year
  -----------------------
  Problem : Show each project name and the project start year.
  Table(s) : projects
  Expected Output:
    project_name, project_start_year
    Warehouse Automation, 2024
  Hint: Use YEAR.
*/
-- Write your answer here:

/*
  Q27. Years of Service
  ---------------------
  Problem : Show each employee name and completed years of service.
  Table(s) : employees
  Expected Output:
    name, years_of_service
    Asha Menon, <depends on current date>
  Hint: Use TIMESTAMPDIFF.
*/
-- Write your answer here:

/*
  Q28. City Fallback
  ------------------
  Problem : Show each customer name and a city fallback of 'Unknown' when city is NULL.
  Table(s) : customers
  Expected Output:
    name, city_fallback
    Manav Kulkarni, Unknown
  Hint: Use COALESCE.
*/
-- Write your answer here:

/*
  Q29. Price Band
  ---------------
  Problem : Show each product name and a CASE-based price band of
            BUDGET, MID, or PREMIUM.
  Table(s) : products
  Expected Output:
    name, price_band
    Pen, BUDGET
    Monitor, PREMIUM
  Hint: Use CASE.
*/
-- Write your answer here:

/*
  Q30. Probation End Date
  -----------------------
  Problem : Show each employee name, hire_date, and probation_end_date
            calculated as hire_date + 90 days.
  Table(s) : employees
  Expected Output:
    name, hire_date, probation_end_date
    Asha Menon, 2024-01-15, 2024-04-14
  Hint: Use DATE_ADD.
*/
-- Write your answer here:
