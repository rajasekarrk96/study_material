/*
=============================================================================
SQL SERVER INTERVIEW PREPARATION - MODULE 09: TEMP TABLES & TABLE VARIABLES
=============================================================================
NOTES:
------
1. Local Temporary Tables (#TempTable):
   - Scope is limited to the connection/session that created it.
   - Dropped automatically when the connection is closed, or can be dropped manually.
   - Physical table stored in the `tempdb` system database.
   - Can have indexes, constraints, and statistics generated (which helps performance on larger datasets).

2. Global Temporary Tables (##GlobalTempTable):
   - Visible to ALL connections/sessions.
   - Dropped automatically when the last connection referencing it closes.
   - Seldom used due to potential naming conflicts and security concerns.

3. Table Variables (@TableVar):
   - Defined like a variable: DECLARE @MyTable TABLE (ID INT, Name VARCHAR(50)).
   - Stored in memory AND `tempdb` (contrary to the myth that they are memory-only).
   - Scope is limited to the specific batch, stored procedure, or function where declared.
   - NO statistics are maintained (the query optimizer assumes it has 1 row), which can lead to poor performance for large datasets.
   - Cannot create non-clustered indexes on them after creation (only via PRIMARY KEY or UNIQUE constraints during declaration in older versions, though newer versions allow inline index syntax).
   - Unaffected by transaction rollbacks (if you roll back a transaction, data in a table variable is NOT reverted).

Interview Tips:
- "When would you use a Temp Table vs a Table Variable vs a CTE?"
  - CTE: For simple recursion or avoiding repeating a subquery in a single statement. No physical storage.
  - Table Variable: For very small amounts of data (usually < 100 rows) within a stored procedure.
  - Temp Table: For larger datasets, complex operations needing indexes, or when statistics are required for the query optimizer to make good choices.
=============================================================================
*/

USE InterviewPrepDB;
GO

/*
=============================================================================
PRACTICE QUESTIONS (Difficulty: Medium to Hard)
=============================================================================
*/

-- Q1 (Medium): Create a local Temporary Table named #HighEarners containing EmployeeID, FirstName, and Salary. Insert all employees earning over 80,000 into it.
-- [Write your query below]



-- Q2 (Medium): Create a Table Variable named @DeptCounts to hold DepartmentID and EmployeeCount. Populate it using an INSERT INTO...SELECT query from the Employees table.
-- [Write your query below]



-- Q3 (Medium-Hard): Demonstrate that Table Variables are NOT affected by a transaction rollback. 
-- (Hint: Declare a table var, BEGIN TRAN, insert a row, ROLLBACK TRAN, then select from the table var).
-- [Write your query below]



-- Q4 (Hard): Write a query that generates a comma-separated list of all employee Email addresses from the IT department. 
-- (Hint: You can use a Table Variable or rely on the FOR XML PATH('') trick to concatenate rows into a single string).
-- [Write your query below]



-- Q5 (Hard): Explain why performance might degrade significantly if you join a very large table (e.g., 1 million rows) with a Table Variable containing 50,000 rows, compared to joining with a Temp Table.
-- [Write your explanation below]



/* 
ANSWERS:
Q1: 
CREATE TABLE #HighEarners (EmployeeID INT, FirstName NVARCHAR(50), Salary DECIMAL(10,2));
INSERT INTO #HighEarners (EmployeeID, FirstName, Salary)
SELECT EmployeeID, FirstName, Salary FROM Employees WHERE Salary > 80000;
-- SELECT * FROM #HighEarners;
-- DROP TABLE #HighEarners;

Q2:
DECLARE @DeptCounts TABLE (DepartmentID INT, EmployeeCount INT);
INSERT INTO @DeptCounts (DepartmentID, EmployeeCount)
SELECT DepartmentID, COUNT(EmployeeID) FROM Employees GROUP BY DepartmentID;
-- SELECT * FROM @DeptCounts;

Q3:
DECLARE @TestVar TABLE (ID INT);
BEGIN TRAN;
INSERT INTO @TestVar (ID) VALUES (1);
ROLLBACK TRAN;
SELECT * FROM @TestVar; -- Returns 1 row! If it were a temp table, it would be empty.

Q4:
SELECT STUFF(
    (SELECT ', ' + Email 
     FROM Employees e 
     INNER JOIN Departments d ON e.DepartmentID = d.DepartmentID 
     WHERE d.DepartmentName = 'IT' 
     FOR XML PATH('')), 
1, 2, '') AS EmailList;

Q5:
Table variables do not maintain distribution statistics (row counts/data distribution). The Query Optimizer generally assumes a Table Variable contains exactly 1 row. When joining to a 1-million-row table, it might choose a nested loop join expecting 1 iteration, which is catastrophic if the variable actually has 50,000 rows. A Temp Table maintains statistics, so the optimizer knows it has 50,000 rows and will choose a more efficient Hash Match or Merge join.
*/
