/*
=============================================================================
SQL SERVER INTERVIEW PREPARATION - MODULE 05: SUBQUERIES & CTEs
=============================================================================
NOTES:
------
1. Subquery Basics (A query inside another query):
   - Scalar Subquery: Returns exactly one row and one column. Can be used anywhere a single value is expected (SELECT list, WHERE clause A = (subquery)).
   - Multi-row Subquery: Returns multiple rows. Used with operators IN, ANY, ALL, EXISTS.
   - Correlated Subquery: References a column from the outer query. It executes once for EVERY row in the outer query. Usually slow.
   - Derived Table (Inline View): A subquery in the FROM clause. MUST be given an alias.

2. EXISTS vs IN:
   - EXISTS logic checks if ANY row is returned. Generally faster than IN when the subquery returns many rows.
   - IN evaluates values to check if they match a list. Performs poorly if list is huge or contains NULLs.
   - NOT EXISTS is highly preferred over NOT IN due to NULL-handling gotchas in NOT IN.

3. Complete Table Expression (CTE):
   - Defined using the WITH clause.
   - Easier to read than derived tables.
   - Can reference itself, which makes it a "Recursive CTE" (great for tree structures like Employee/Manager hierarchy).
   - Only exists during the execution scope of the immediate next statement.

Interview Tips:
- "Why does NOT IN sometimes return no records when it logically should?" -> If the subquery list contains a single NULL value, NOT IN evaluates to UNKNOWN for everything, returning nothing. Use NOT EXISTS.
- Always use a CTE if you find yourself writing the same subquery multiple times.
=============================================================================
*/

USE InterviewPrepDB;
GO

/*
=============================================================================
PRACTICE QUESTIONS (Difficulty: Medium to Hard)
=============================================================================
*/

-- Q1 (Medium): Use a Subquery in the WHERE clause to find employees who make MORE than the average salary of the entire company.
-- [Write your query below]



-- Q2 (Medium): Use a CTE to achieve the exact same result as Q1 (employees earning above average salary).
-- [Write your query below]



-- Q3 (Medium-Hard): Write a Correlated Subquery that finds the employees whose salary is ABOVE the average salary OF THEIR OWN DEPARTMENT.
-- [Write your query below]



-- Q4 (Medium-Hard): Write a query using NOT EXISTS to find all Departments that currently have NO employees.
-- [Write your query below]



-- Q5 (Hard): Use a Recursive CTE to build an Employee Hierarchy showing Level. The top manager (ManagerID IS NULL) is Level 1, their direct reports are Level 2, etc. (Requires EmployeeID, FirstName, ManagerID, and a new column 'HierarchyLevel').
-- [Write your query below]



/* 
ANSWERS:
Q1: SELECT * FROM Employees WHERE Salary > (SELECT AVG(Salary) FROM Employees);
Q2: 
WITH AvgSalCTE AS (SELECT AVG(Salary) AS AvgSal FROM Employees)
SELECT e.* FROM Employees e CROSS JOIN AvgSalCTE cte WHERE e.Salary > cte.AvgSal;
Q3: 
SELECT e1.FirstName, e1.Salary, e1.DepartmentID 
FROM Employees e1 
WHERE Salary > (SELECT AVG(Salary) FROM Employees e2 WHERE e2.DepartmentID = e1.DepartmentID);
Q4: SELECT * FROM Departments d WHERE NOT EXISTS (SELECT 1 FROM Employees e WHERE e.DepartmentID = d.DepartmentID);
Q5:
WITH EmployeeOrg AS (
    -- Anchor member
    SELECT EmployeeID, FirstName, ManagerID, 1 AS HierarchyLevel 
    FROM Employees WHERE ManagerID IS NULL
    UNION ALL
    -- Recursive member
    SELECT e.EmployeeID, e.FirstName, e.ManagerID, o.HierarchyLevel + 1
    FROM Employees e 
    INNER JOIN EmployeeOrg o ON e.ManagerID = o.EmployeeID
)
SELECT * FROM EmployeeOrg ORDER BY HierarchyLevel;
*/
