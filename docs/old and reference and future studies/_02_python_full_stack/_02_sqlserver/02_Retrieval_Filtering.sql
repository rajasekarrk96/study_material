/*
=============================================================================
SQL SERVER INTERVIEW PREPARATION - MODULE 02: RETRIEVAL & FILTERING
=============================================================================
NOTES:
------
1. SELECT Structure:
   SELECT column1, column2 FROM TableName WHERE condition ORDER BY column1;

2. Filtering (WHERE clause):
   - AND, OR, NOT
   - IN (val1, val2) - checks if a value matches any in a list.
   - BETWEEN val1 AND val2 - inclusive range check.
   - LIKE - for pattern matching. 
     '%' matches 0 or more characters. 
     '_' matches exactly one character.
   - IS NULL / IS NOT NULL - strict check for missing data. (= NULL does NOT work natively without ANSI_NULLS OFF).

3. Sorting (ORDER BY):
   - ASC (default) / DESC
   - Multiple columns supported: ORDER BY col1 DESC, col2 ASC

4. Limiting Rows:
   - TOP N: SELECT TOP 5 * FROM ...
   - OFFSET/FETCH: Used for pagination. 
     ORDER BY column OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY;

Interview Tips:
- Understand the logical processing order: FROM -> WHERE -> SELECT -> ORDER BY.
- Filtering with NULLs is a very common trap. NULL is unknown, so mathematically anything compared to NULL is still NULL (unknown).
=============================================================================
*/

USE InterviewPrepDB;
GO

/*
=============================================================================
PRACTICE QUESTIONS (Difficulty: Easy to Medium-Hard)
=============================================================================
*/

-- Q1 (Easy): Select all columns from the Employees table where the Salary is greater than 80,000.
-- [Write your query below]



-- Q2 (Easy): Find the details of all Employees whose LastName starts with 'S' or 'B'.
-- [Write your query below]



-- Q3 (Medium): Retrieve a list of Employee Emails who do not have a Manager assigned.
-- [Write your query below]



-- Q4 (Medium): Retrieve the top 3 highest paid Employees, ordering the results by Salary descending.
-- [Write your query below]



-- Q5 (Medium-Hard): Write a query to implement pagination. Fetch the 2nd page of Employees, assuming 2 results per page, ordered by HireDate ascending.
-- [Write your query below]



/* 
ANSWERS:
Q1: SELECT * FROM Employees WHERE Salary > 80000;
Q2: SELECT * FROM Employees WHERE LastName LIKE 'S%' OR LastName LIKE 'B%';
Q3: SELECT Email FROM Employees WHERE ManagerID IS NULL;
Q4: SELECT TOP 3 * FROM Employees ORDER BY Salary DESC;
Q5: SELECT * FROM Employees ORDER BY HireDate ASC OFFSET 2 ROWS FETCH NEXT 2 ROWS ONLY;
*/
