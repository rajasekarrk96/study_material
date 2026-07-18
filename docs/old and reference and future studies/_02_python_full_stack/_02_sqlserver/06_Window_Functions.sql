/*
=============================================================================
SQL SERVER INTERVIEW PREPARATION - MODULE 06: WINDOW FUNCTIONS
=============================================================================
NOTES:
------
1. Concept:
   - Window functions perform calculations across a set of table rows related to the current row. 
   - Unlike GROUP BY, window functions do not cause rows to be grouped into a single output row - the rows retain their separate identities.

2. Syntax Structure:
   - FunctionName() OVER (
        PARTITION BY column1 (Optional - acts like GROUP BY, resetting calculation per partition)
        ORDER BY column2     (Required for Ranking/Analytic, Optional for Aggregate)
        ROWS/RANGE clause    (Optional - fine-tunes the framing of the window)
     )

3. Core Functions:
   - Aggregates as Window: SUM(Col) OVER (...), AVG(Col) OVER(...), COUNT() OVER(...)
   - Ranking:
     - ROW_NUMBER(): Unique sequential number (1, 2, 3, 4). No ties.
     - RANK(): Leaves gaps on ties (1, 2, 2, 4).
     - DENSE_RANK(): No gaps on ties (1, 2, 2, 3).
     - NTILE(N): Distributes rows evenly into N buckets.
   - Analytic:
     - LEAD(col, offset): Gets a value from a subsequent row within the partition.
     - LAG(col, offset): Gets a value from a preceding row within the partition.
     - FIRST_VALUE() / LAST_VALUE()

Interview Tips:
- A classic question: "How do you find the 2nd highest salary per department?" -> Use DENSE_RANK() or ROW_NUMBER() in a CTE, then filter WHERE Rank = 2. You CANNOT use Window Functions directly in a WHERE clause.
- Know the subtle difference between RANK and DENSE_RANK perfectly.
=============================================================================
*/

USE InterviewPrepDB;
GO

/*
=============================================================================
PRACTICE QUESTIONS (Difficulty: Medium to Hard)
=============================================================================
*/

-- Q1 (Medium): Assign a unique sequential number to every employee based on their HireDate (oldest first).
-- [Write your query below]



-- Q2 (Medium): Write a query to find the 'Running Total' of Salaries across all employees, ordered by their HireDate.
-- [Write your query below]



-- Q3 (Medium-Hard): Retrieve the 2nd highest salary from the *entire company*. Do not use TOP or OFFSET.
-- [Write your query below]



-- Q4 (Hard): Rank the employees WITHIN their respective Departments by Salary DESC. Then use a CTE to filter and ONLY return the highest-paid employee per department.
-- [Write your query below]



-- Q5 (Hard): Use LEAD/LAG to write a query showing each Employee's Salary, and in the next column, show the Salary of the employee hired immediately AFTER them (ordered by HireDate). If they are the newest employee, show NULL.
-- [Write your query below]



/* 
ANSWERS:
Q1: SELECT FirstName, LastName, HireDate, ROW_NUMBER() OVER (ORDER BY HireDate ASC) AS EmployeeNum FROM Employees;
Q2: SELECT FirstName, Salary, HireDate, SUM(Salary) OVER (ORDER BY HireDate ASC) AS RunningTotalSalary FROM Employees;
Q3: 
WITH RankedSalaries AS (
    SELECT Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) as Rnk FROM Employees
)
SELECT DISTINCT Salary FROM RankedSalaries WHERE Rnk = 2;
Q4: 
WITH DeptRanks AS (
    SELECT FirstName, DepartmentID, Salary, DENSE_RANK() OVER (PARTITION BY DepartmentID ORDER BY Salary DESC) AS Rnk FROM Employees
)
SELECT * FROM DeptRanks WHERE Rnk = 1;

Q5: SELECT FirstName, HireDate, Salary, LEAD(Salary, 1, NULL) OVER (ORDER BY HireDate ASC) AS NextHiredPersonSalary FROM Employees;
*/
