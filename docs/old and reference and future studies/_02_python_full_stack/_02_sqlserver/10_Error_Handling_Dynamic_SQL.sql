/*
=============================================================================
SQL SERVER INTERVIEW PREPARATION - MODULE 10: ERROR HANDLING & DYNAMIC SQL
=============================================================================
NOTES:
------
1. Error Handling (TRY...CATCH):
   - Put risky code inside a BEGIN TRY ... END TRY block.
   - If an error occurs (severity > 10 and < 20), execution jumps to BEGIN CATCH ... END CATCH.
   - Built-in functions available only in the CATCH block:
     ERROR_NUMBER(), ERROR_MESSAGE(), ERROR_SEVERITY(), ERROR_STATE(), ERROR_LINE(), ERROR_PROCEDURE().
   
2. Throwing Errors:
   - RAISERROR: The older way to generate custom errors. Allows substituting variables (like printf).
   - THROW: The modern way (SQL Server 2012+). Syntax: THROW [error_number, message, state]. Must be preceded by a semicolon if in a batch. Re-throws the exact original error if used without parameters inside a CATCH block.

3. Dynamic SQL:
   - Building SQL statements as strings and executing them at runtime.
   - Useful when table names, column names, or database names need to be parameterized (which standard variables don't allow).
   - Executing options:
     1. EXEC(@SqlString) - Simple, but highly vulnerable to SQL Injection and cannot easily output parameters.
     2. sp_executesql - Highly recommended! Allows safe parameterization, prevents SQL injection, and promotes query plan reuse.

Interview Tips:
- Security risk: NEVER concatenate user input directly into a dynamic SQL string -> SQL INJECTION! Always use `sp_executesql` with explicit parameters.
- Mention `THROW` over `RAISERROR` when asked how to bubble up errors in modern SQL Server.
=============================================================================
*/

USE InterviewPrepDB;
GO

/*
=============================================================================
PRACTICE QUESTIONS (Difficulty: Medium to Hard)
=============================================================================
*/

-- Q1 (Medium): Write a TRY...CATCH block that attempts to insert a duplicate Primary Key or Unique Email into the Employees table. In the CATCH block, select the ERROR_NUMBER() and ERROR_MESSAGE().
-- [Write your query below]



-- Q2 (Medium-Hard): Show how to use the THROW statement manually to raise a custom error: Error Number 50001, Message 'Salary cannot be negative', State 1.
-- [Write your query below]



-- Q3 (Medium-Hard): Write a script that uses sp_executesql to perform a dynamic SELECT from the Employees table where the DepartmentID is passed as a parameter.
-- [Write your query below]



-- Q4 (Hard): Explain why Dynamic SQL is vulnerable to SQL Injection and demonstrate a "bad" example of Dynamic SQL that concatenates a parameter directly.
-- [Write your explanation below]



-- Q5 (Hard): Create a Stored Procedure that takes a TABLE NAME as a parameter and returns the count of rows in that table dynamically using sp_executesql. (Hint: Output parameters in sp_executesql).
-- [Write your query below]



/* 
ANSWERS:
Q1:
BEGIN TRY
    INSERT INTO Employees (FirstName, LastName, Email, Salary) 
    VALUES ('Duplicate', 'User', 'alice.smith@example.com', 50000); -- email already exists
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS ErrNum, ERROR_MESSAGE() AS ErrMsg;
END CATCH;

Q2:
DECLARE @Salary DECIMAL(10,2) = -500;
IF @Salary < 0
BEGIN
    ;THROW 50001, 'Salary cannot be negative.', 1;
END

Q3:
DECLARE @SQL NVARCHAR(MAX) = N'SELECT * FROM Employees WHERE DepartmentID = @DeptID';
DECLARE @FilterDept INT = 2;
EXEC sp_executesql @stmt = @SQL, @params = N'@DeptID INT', @DeptID = @FilterDept;

Q4:
Dynamic SQL is vulnerable when user input is concatenated directly. If a user inputs something like "2; DROP TABLE Employees", the executing string becomes mischievous. 
Bad Example: 
DECLARE @UserInput VARCHAR(100) = '2; DROP TABLE Employees'; -- Hacker input
DECLARE @BadSQL VARCHAR(MAX) = 'SELECT * FROM Employees WHERE EmployeeID = ' + @UserInput;
EXEC(@BadSQL); -- Executes the select, then drops the table!

Q5:
CREATE PROCEDURE usp_GetTableRowCount 
    @TableName NVARCHAR(128),
    @RowCount INT OUTPUT
AS
BEGIN
    -- Basic protection against injection: ensure table exists
    IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = @TableName)
    BEGIN
        ;THROW 50002, 'Table does not exist.', 1;
    END

    DECLARE @SQL NVARCHAR(MAX);
    -- We can safely concatenate @TableName here because we verified it's a real table above, 
    -- and we use QUOTENAME to add brackets safely [TableName].
    SET @SQL = N'SELECT @Cnt = COUNT(*) FROM ' + QUOTENAME(@TableName);
    
    EXEC sp_executesql 
        @stmt = @SQL, 
        @params = N'@Cnt INT OUTPUT', 
        @Cnt = @RowCount OUTPUT;
END;
-- Use: DECLARE @Res INT; EXEC usp_GetTableRowCount 'Employees', @Res OUTPUT; SELECT @Res;
*/
