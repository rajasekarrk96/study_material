-- ============================================================================
-- TITLE: MYSQL QUERYING, FILTERING, SORTING, AND LIMITING QUESTIONS
-- ============================================================================

DROP DATABASE IF EXISTS mysql_03_querying_filtering_questions;
CREATE DATABASE mysql_03_querying_filtering_questions;
USE mysql_03_querying_filtering_questions;

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL
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
    status VARCHAR(20) NOT NULL
);

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

-- ============================================================================
-- SECTION 1: BASIC QUESTIONS
-- ============================================================================

-- Q1:
-- Select product_id, name, and price from products.

-- Q2:
-- Select name AS product_name and price AS selling_price from products.

-- Q3:
-- Select all products where price is greater than 3000.

-- Q4:
-- Select all products where stock is equal to 0.

-- Q5:
-- Select all customers whose city is 'Mumbai'.

-- Q6:
-- Select distinct category values from products.

-- Q7:
-- Select all products ordered by price in descending order.

-- Q8:
-- Select customers whose email contains '@gmail.com'.

-- Q9:
-- Select customers whose city is NULL.

-- Q10:
-- Select product name, price, and price * stock AS inventory_value.

-- ============================================================================
-- SECTION 2: INTERMEDIATE QUESTIONS
-- ============================================================================

-- Q11:
-- Select the first 3 products when ordered by product_id.

-- Q12:
-- Select products 4 through 6 when ordered by product_id.

-- Q13:
-- Select products whose category is either 'Stationery' or 'Electronics'.

-- Q14:
-- Select products where price is between 500 and 3000.

-- Q15:
-- Select customers who do not live in Chennai.

-- Q16:
-- Select orders placed after '2024-04-04'.

-- Q17:
-- Select customers whose names start with 'M'.

-- Q18:
-- Select product name and stock for products where stock is greater than 50,
-- then order the result by stock descending.

-- Q19:
-- Select orders whose status is either 'Pending' or 'Shipped'.

-- Q20:
-- Select customers whose city is either 'Mumbai' or 'Bangalore',
-- ordered by city and then by name.

-- ============================================================================
-- SECTION 3: ADVANCED QUESTIONS
-- ============================================================================

-- Q21:
-- Select the top 5 most expensive in-stock products from Electronics or Furniture.

-- Q22:
-- Select delivered orders where total_amount is greater than 3000,
-- ordered by order_date descending.

-- Q23:
-- Select customers whose city is NOT NULL and whose email ends with gmail.com.

-- Q24:
-- Select products whose price is between 500 and 5000 and stock is above 20.

-- Q25:
-- Select the 3rd, 4th, and 5th highest-value orders using ORDER BY and LIMIT/OFFSET.

-- Q26:
-- Select all customers except those from Mumbai or Delhi.

-- Q27:
-- Select products where category is Electronics and price is below 10000.

-- Q28:
-- Select customers whose city is NULL or whose email ends with outlook.com.

-- Q29:
-- Select products ordered first by category ascending and then by price descending.

-- Q30:
-- Select customers who joined on or after '2024-01-01', ordered by join_date.

-- ============================================================================
-- SECTION 4: REAL-WORLD SCENARIO QUESTIONS
-- ============================================================================

-- Q31:
-- Create an e-commerce home page query that returns the 5 most expensive
-- in-stock products from Electronics and Furniture.

-- Q32:
-- Create a customer support query that returns all customers with missing city.

-- Q33:
-- Create a finance query that returns all high-value delivered or shipped orders
-- above 4000, ordered by total_amount descending.

-- Q34:
-- Create a merchandiser query that returns all low-stock products
-- where stock is below 10, ordered by stock ascending.

-- Q35:
-- Create a CRM query that returns all unique customer cities in alphabetical order.
