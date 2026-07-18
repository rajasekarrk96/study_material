/*
================================================================================
STEP 07: JOINS AND TABLE RELATIONSHIPS
================================================================================
GOAL:
Learn how to combine data from multiple related tables using join operations.
================================================================================
*/

USE world;

/*
--------------------------------------------------------------------------------
1. WHY JOINS ARE NEEDED
--------------------------------------------------------------------------------
- Real databases store related data in separate tables
- Joins combine related rows through matching columns
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
2. INNER JOIN
--------------------------------------------------------------------------------
- Returns only matching rows from both tables
--------------------------------------------------------------------------------
*/

SELECT c.name, ci.name
FROM country AS c
INNER JOIN city AS ci
    ON c.code = ci.countrycode;

/*
--------------------------------------------------------------------------------
3. LEFT JOIN
--------------------------------------------------------------------------------
- Returns all rows from left table
- Matching rows from right table
- If no match, right side becomes NULL
--------------------------------------------------------------------------------
*/

SELECT c.name, ci.name
FROM country AS c
LEFT JOIN city AS ci
    ON c.code = ci.countrycode;

/*
--------------------------------------------------------------------------------
4. RIGHT JOIN
--------------------------------------------------------------------------------
- Returns all rows from right table and matching rows from left table
--------------------------------------------------------------------------------
*/

SELECT c.name, ci.name
FROM country AS c
RIGHT JOIN city AS ci
    ON c.code = ci.countrycode;

/*
--------------------------------------------------------------------------------
5. CROSS JOIN
--------------------------------------------------------------------------------
- Returns cartesian product
- Every row from first table combines with every row from second table
--------------------------------------------------------------------------------
*/

SELECT c.code, ci.id
FROM country AS c
CROSS JOIN city AS ci
LIMIT 5;

/*
--------------------------------------------------------------------------------
6. SELF JOIN
--------------------------------------------------------------------------------
- A table joined with itself
- Requires aliases
--------------------------------------------------------------------------------
*/

/*
Example pattern:
SELECT e.emp_name, m.emp_name AS manager_name
FROM employees e
LEFT JOIN employees m
  ON e.manager_id = m.emp_id;
*/

/*
--------------------------------------------------------------------------------
7. JOIN CONDITIONS
--------------------------------------------------------------------------------
- Most joins use primary key to foreign key relationships
- Wrong join condition can create duplicate or incorrect results
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
8. IMPLICIT JOIN VS EXPLICIT JOIN
--------------------------------------------------------------------------------
Explicit join:
- uses JOIN ... ON ...
- recommended

Implicit join:
- uses commas and WHERE
- older style
--------------------------------------------------------------------------------
*/

SELECT c.name, ci.name
FROM country c, city ci
WHERE c.code = ci.countrycode;

/*
--------------------------------------------------------------------------------
9. FULL OUTER JOIN IN MYSQL
--------------------------------------------------------------------------------
- MySQL does not support FULL OUTER JOIN directly
- Can simulate using LEFT JOIN UNION RIGHT JOIN
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
10. JOIN WITH FILTERING
--------------------------------------------------------------------------------
- Joins are often combined with WHERE, ORDER BY, GROUP BY
--------------------------------------------------------------------------------
*/

SELECT c.name AS country_name, ci.name AS city_name, ci.population
FROM country AS c
INNER JOIN city AS ci
    ON c.code = ci.countrycode
WHERE ci.population > 1000000
ORDER BY ci.population DESC;

/*
--------------------------------------------------------------------------------
11. COMMON MISTAKES
--------------------------------------------------------------------------------
1. Missing ON condition
2. Joining wrong columns
3. Confusing LEFT JOIN with INNER JOIN
4. Forgetting NULL behavior in outer joins
--------------------------------------------------------------------------------
*/

/*
================================================================================
SUMMARY
================================================================================
- INNER JOIN keeps matches only
- LEFT JOIN keeps all left rows
- RIGHT JOIN keeps all right rows
- CROSS JOIN creates all combinations
- SELF JOIN joins one table to itself
================================================================================
*/
