/*
=============================================================================
SQL SERVER INTERVIEW PREPARATION - MODULE 03: FUNCTIONS & AGGREGATION
=============================================================================
NOTES:
------
1. Built-in Functions:
   - String: LEN(), SUBSTRING(), CHARINDEX(), REPLACE(), UPPER(), LOWER(), TRIM()
   - Math: ROUND(), CEILING(), FLOOR(), ABS()
   - Date: GETDATE(), DATEADD(), DATEDIFF(), DATEPART(), FORMAT()
   - Null-handling: ISNULL(col, default_val), COALESCE(val1, val2, ...), NULLIF(val1, val2)

2. Aggregate Functions:
   - COUNT(), SUM(), AVG(), MIN(), MAX()
   - COUNT(*) counts rows. COUNT(col) counts NON-NULL values in that column.

3. GROUP BY and HAVING:
   - GROUP BY rolls up data into buckets based on specified columns.
   - HAVING filters data AFTER aggregation (unlike WHERE, which filters before).

Interview Tips:
- Know the difference between WHERE and HAVING perfectly.
- ISNULL vs COALESCE: ISNULL is SQL Server specific, takes 2 args. COALESCE is ANSI standard, takes N args, returns the first non-null.
- DATEDIFF is often tested (e.g., calculate age, find records created in last 7 days).
=============================================================================
*/

USE InterviewPrepDB;
GO

/*
=============================================================================
PRACTICE QUESTIONS (Difficulty: Easy to Hard)
=============================================================================
*/

-- Q1 (Easy): Write a query to find the total number of employees in the Employees table.
-- [Write your query below]



-- Q2 (Easy): Find the average Salary of all employees. Use ISNULL to handle potential NULLs by treating them as 0, then average it (assuming Salary could safely be null).
-- [Write your query below]



-- Q3 (Medium): Group employees by DepartmentID. Find the total Salary (SUM) and employee count in each department.
-- [Write your query below]



-- Q4 (Medium): From the query above, filter the results to only show groups (DepartmentIDs) that have more than 1 employee.
-- [Write your query below]



-- Q5 (Hard): Extract the domain name from the employee's Email address (everything after the '@'). Group by the domain and count how many employees use each domain.
-- [Write your query below]



/* 
ANSWERS:
Q1: SELECT COUNT(*) AS TotalEmployees FROM Employees;
Q2: SELECT AVG(ISNULL(Salary, 0)) AS AvgSalary FROM Employees;
Q3: SELECT DepartmentID, SUM(Salary) AS TotalSalary, COUNT(EmployeeID) AS EmpCount FROM Employees GROUP BY DepartmentID;
Q4: SELECT DepartmentID, SUM(Salary) AS TotalSalary, COUNT(EmployeeID) AS EmpCount FROM Employees GROUP BY DepartmentID HAVING COUNT(EmployeeID) > 1;
Q5: 
SELECT 
    SUBSTRING(Email, CHARINDEX('@', Email) + 1, LEN(Email) - CHARINDEX('@', Email)) AS DomainName,
    COUNT(*) AS DomainCount
FROM Employees
GROUP BY SUBSTRING(Email, CHARINDEX('@', Email) + 1, LEN(Email) - CHARINDEX('@', Email));
*/
