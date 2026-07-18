-- ============================================================================
-- TITLE: MYSQL QUERYING, FILTERING, SORTING, AND LIMITING ANSWERS
-- ============================================================================

DROP DATABASE IF EXISTS mysql_03_querying_filtering_answers;
CREATE DATABASE mysql_03_querying_filtering_answers;
USE mysql_03_querying_filtering_answers;

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

-- Q1
-- Return only the selected columns from products.
SELECT product_id, name, price
FROM products;
-- Expected: 12 rows with product_id, name, and price

-- Q2
-- Use aliases to produce clearer output headers.
SELECT name AS product_name, price AS selling_price
FROM products;
-- Expected: same values with aliased column names

-- Q3
-- Filter products priced above 3000.
SELECT *
FROM products
WHERE price > 3000;
-- Expected: Mechanical Keyboard, Office Chair, Standing Desk, Noise Cancelling Headphones

-- Q4
-- Filter out-of-stock products.
SELECT *
FROM products
WHERE stock = 0;
-- Expected: Planner 2026 only

-- Q5
-- Return customers from Mumbai.
SELECT *
FROM customers
WHERE city = 'Mumbai';
-- Expected: Ananya Gupta and Tarun Sethi

-- Q6
-- Return unique product categories.
SELECT DISTINCT category
FROM products;
-- Expected: Electronics, Furniture, Stationery, Lifestyle, Accessories

-- Q7
-- Sort products by price descending.
SELECT *
FROM products
ORDER BY price DESC;
-- Expected: most expensive product first

-- Q8
-- Find Gmail customers using LIKE.
SELECT *
FROM customers
WHERE email LIKE '%@gmail.com';
-- Expected: only Gmail-address customers

-- Q9
-- Correctly match NULL with IS NULL.
SELECT *
FROM customers
WHERE city IS NULL;
-- Expected: Manav Kulkarni

-- Q10
-- Build a calculated column with an expression.
SELECT name, price, price * stock AS inventory_value
FROM products;
-- Expected: each product row includes inventory_value

-- Q11
-- Return the first three products by product_id.
SELECT *
FROM products
ORDER BY product_id
LIMIT 3;
-- Expected: product_id 501, 502, 503

-- Q12
-- Skip the first three rows and return the next three.
SELECT *
FROM products
ORDER BY product_id
LIMIT 3 OFFSET 3;
-- Expected: product_id 504, 505, 506

-- Q13
-- Filter products using IN.
SELECT *
FROM products
WHERE category IN ('Stationery', 'Electronics');
-- Expected: all Stationery and Electronics rows

-- Q14
-- Filter products using an inclusive range.
SELECT *
FROM products
WHERE price BETWEEN 500 AND 3000;
-- Expected: Wireless Mouse, USB-C Hub, Desk Lamp, Laptop Stand

-- Q15
-- Exclude Chennai rows.
SELECT *
FROM customers
WHERE city <> 'Chennai';
-- Expected: all non-Chennai rows where city is not NULL

-- Q16
-- Return orders after April 4, 2024.
SELECT *
FROM orders
WHERE order_date > '2024-04-04';
-- Expected: orders 405 through 412 except earlier ones

-- Q17
-- Match customer names starting with M.
SELECT *
FROM customers
WHERE name LIKE 'M%';
-- Expected: Manav Kulkarni

-- Q18
-- Sort high-stock items from highest stock to lowest stock.
SELECT name, stock
FROM products
WHERE stock > 50
ORDER BY stock DESC;
-- Expected: Gel Pen Set, Notebook Pack, Water Bottle, Cable Manager, Folder, Wireless Mouse

-- Q19
-- Match two order statuses with OR-style logic through IN.
SELECT *
FROM orders
WHERE status IN ('Pending', 'Shipped');
-- Expected: Pending and Shipped orders

-- Q20
-- Filter and sort by multiple columns.
SELECT *
FROM customers
WHERE city IN ('Mumbai', 'Bangalore')
ORDER BY city, name;
-- Expected: Bangalore and Mumbai customers in sorted order

-- Q21
-- Top 5 most expensive in-stock Electronics or Furniture products.
SELECT product_id, name, category, price, stock
FROM products
WHERE category IN ('Electronics', 'Furniture')
  AND stock > 0
ORDER BY price DESC, name ASC
LIMIT 5;
-- Expected: 5 highest-priced in-stock rows from those categories

-- Q22
-- Delivered orders above 3000, newest first.
SELECT order_id, customer_id, order_date, total_amount
FROM orders
WHERE status = 'Delivered'
  AND total_amount > 3000
ORDER BY order_date DESC;
-- Expected: orders 408, 403, 401

-- Q23
-- Gmail customers with known city.
SELECT *
FROM customers
WHERE city IS NOT NULL
  AND email LIKE '%@gmail.com';
-- Expected: Gmail customers except Manav Kulkarni if city is NULL

-- Q24
-- Mid-range products with good stock.
SELECT *
FROM products
WHERE price BETWEEN 500 AND 5000
  AND stock > 20;
-- Expected: Wireless Mouse, USB-C Hub, Desk Lamp, Laptop Stand

-- Q25
-- Return the 3rd, 4th, and 5th highest-value orders.
SELECT order_id, total_amount, status
FROM orders
ORDER BY total_amount DESC
LIMIT 3 OFFSET 2;
-- Expected: the third through fifth rows from the descending amount sort

-- Q26
-- Exclude Mumbai and Delhi.
SELECT *
FROM customers
WHERE city NOT IN ('Mumbai', 'Delhi');
-- Expected: all customers outside Mumbai and Delhi, excluding NULL city

-- Q27
-- Electronics under 10000.
SELECT *
FROM products
WHERE category = 'Electronics'
  AND price < 10000;
-- Expected: Wireless Mouse, Mechanical Keyboard, USB-C Hub

-- Q28
-- Match missing city or outlook domain.
SELECT *
FROM customers
WHERE city IS NULL
   OR email LIKE '%@outlook.com';
-- Expected: Manav Kulkarni plus Outlook customers

-- Q29
-- Sort by category then by price descending.
SELECT *
FROM products
ORDER BY category ASC, price DESC;
-- Expected: rows grouped alphabetically by category and sorted by price inside each category

-- Q30
-- Customers who joined in 2024 or later.
SELECT *
FROM customers
WHERE join_date >= '2024-01-01'
ORDER BY join_date;
-- Expected: 2024 joiners sorted by date

-- Q31
-- Home page product query.
SELECT product_id, name, category, price, stock
FROM products
WHERE category IN ('Electronics', 'Furniture')
  AND stock > 0
ORDER BY price DESC
LIMIT 5;
-- Expected: premium in-stock display products

-- Q32
-- Support query for missing city.
SELECT customer_id, name, email, city
FROM customers
WHERE city IS NULL;
-- Expected: customers missing city information

-- Q33
-- High-value delivered or shipped orders above 4000.
SELECT *
FROM orders
WHERE status IN ('Delivered', 'Shipped')
  AND total_amount > 4000
ORDER BY total_amount DESC;
-- Expected: high-value delivered or shipped rows

-- Q34
-- Low-stock products.
SELECT product_id, name, stock
FROM products
WHERE stock < 10
ORDER BY stock ASC, name ASC;
-- Expected: zero-stock and very-low-stock products first

-- Q35
-- Unique city list for CRM dropdown.
SELECT DISTINCT city
FROM customers
WHERE city IS NOT NULL
ORDER BY city ASC;
-- Expected: alphabetical unique non-NULL city values
