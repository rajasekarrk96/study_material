/*
=============================================================================
SQL SERVER INTERVIEW PREPARATION - MODULE 04: JOINS & SET OPERATIONS
=============================================================================
NOTES:
------
1. JOIN Types:
   - INNER JOIN: Returns rows when there's a match in BOTH tables.
   - LEFT (OUTER) JOIN: Returns all rows from the left table, and matched rows from the right. Unmatched left rows get NULL for right table columns.
   - RIGHT (OUTER) JOIN: Opposite of LEFT JOIN.
   - FULL (OUTER) JOIN: Returns all rows when there's a match in either left or right table. Unmatched rows get NULLs.
   - CROSS JOIN: Cartesian product (every row in table 1 pairs with every row in table 2).
   - SELF JOIN: A regular join where a table is joined with itself (useful for hierarchies, e.g., Employee to Manager).

2. SET Operations:
   - UNION: Combines the result of two SELECTs, removing duplicates. Both result sets must have the same number of columns and compatible types.
   - UNION ALL: Like UNION, but keeps duplicates. (Much faster than UNION!).
   - INTERSECT: Returns only rows that appear in BOTH queries.
   - EXCEPT: Returns rows from the first query that are NOT present in the second query.

Interview Tips:
- JOIN logically combines columns side-by-side. SET operations combine rows vertically.
- "What happens if there are NULLs in the join key?" -> Standard JOIN condition (A.key = B.key) will discard them because NULL = NULL evaluates to false/unknown.
- Always prefer UNION ALL over UNION unless you explicitly need to deduplicate.
=============================================================================
*/

USE InterviewPrepDB;
GO

/*
=============================================================================
PRACTICE QUESTIONS (Difficulty: Easy to Hard)
=============================================================================
*/

-- Q1 (Easy): Retrieve a list of all Employees (FirstName, LastName) and their corresponding DepartmentName. Use an INNER JOIN.
-- [Write your query below]



-- Q2 (Easy): Retrieve ALL Departments and any Employees in them. If a Department has no employees, it should still appear in the result with NULL employee details.
-- [Write your query below]



-- Q3 (Medium): Write a query to find all pairs of employees who work in the exact same department. (Hint: Self Join). Ensure you do not match the employee with themselves, and prevent duplicate pairs (A-B and B-A).
-- [Write your query below]



-- Q4 (Medium-Hard): You want to find employees who do NOT have any projects assigned. Write this query twice: once using a LEFT JOIN, and once using EXCEPT.
-- [Write your query below]



-- Q5 (Hard): Your task is to list Employee names alongside their Manager's name. Specifically, format the output as "EmployeeName works for ManagerName". If they have no manager, print "CEO/Top Executive".
-- [Write your query below]



/* 
ANSWERS:
Q1: SELECT e.FirstName, e.LastName, d.DepartmentName FROM Employees e INNER JOIN Departments d ON e.DepartmentID = d.DepartmentID;
Q2: SELECT d.DepartmentName, e.FirstName, e.LastName FROM Departments d LEFT JOIN Employees e ON d.DepartmentID = e.DepartmentID;
Q3: SELECT e1.FirstName AS Emp1, e2.FirstName AS Emp2, e1.DepartmentID FROM Employees e1 INNER JOIN Employees e2 ON e1.DepartmentID = e2.DepartmentID AND e1.EmployeeID < e2.EmployeeID;
Q4 Solution 1 (LEFT JOIN): SELECT e.EmployeeID, e.FirstName FROM Employees e LEFT JOIN EmployeeProjects ep ON e.EmployeeID = ep.EmployeeID WHERE ep.ProjectID IS NULL;
Q4 Solution 2 (EXCEPT): SELECT EmployeeID, FirstName FROM Employees EXCEPT SELECT e.EmployeeID, e.FirstName FROM Employees e INNER JOIN EmployeeProjects ep ON e.EmployeeID = ep.EmployeeID;
Q5: SELECT e.FirstName + ' ' + e.LastName + ' works for ' + ISNULL(m.FirstName + ' ' + m.LastName, 'CEO/Top Executive') AS Hierarchy FROM Employees e LEFT JOIN Employees m ON e.ManagerID = m.EmployeeID;
*/
