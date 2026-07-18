/*
=============================================================================
SQL SERVER INTERVIEW PREPARATION - MODULE 07: ADVANCED DB OBJECTS
=============================================================================
NOTES:
------
1. Views:
   - A virtual table based on the result-set of an SQL statement.
   - Used for security (restricting columns/rows) and simplifying complex queries.
   - Indexed Views (Materialized views) store data physically but have strict requirements.

2. Stored Procedures (SPs):
   - Prepared SQL code that you can save and reuse.
   - Accepts IN and OUT parameters.
   - Pre-compiled execution plan (faster repeated execution).
   - Can execute complex logic, loops, IF/ELSE statements, and modify data (INSERT/UPDATE/DELETE).

3. User-Defined Functions (UDFs):
   - Scalar Function: Returns a single value.
   - Table-Valued Function (TVF): Returns a Table.
   - Differences from SPs: UDFs must return a value, can be used inline in a SELECT statement. UDFs CANNOT alter database state (no INSERT/UPDATE/DELETE to physical tables).

4. Triggers:
   - Special SPs that run automatically when an event occurs (DML triggers: AFTER INSERT, UPDATE, DELETE or INSTEAD OF).
   - Utilizes inserted & deleted virtual tables.

5. Indexes:
   - Clustered Index: Sorts and stores the data rows in the table physically. (Only ONE per table. Often the PK).
   - Non-Clustered Index: A separate structure with pointers back to the data rows. (Can have multiple).

Interview Tips:
- SP vs Function: SP can have output parameters, handle transactions, change data; Functions cannot. Functions can be placed inside SELECT/WHERE; SPs cannot.
- Clustered vs Non-Clustered Index: Physical sort order vs Phone Book Index (pointers).
- "Inserted" and "Deleted" tables are available inside DML triggers to see the before/after state.
=============================================================================
*/

USE InterviewPrepDB;
GO

/*
=============================================================================
PRACTICE QUESTIONS (Difficulty: Medium to Hard)
=============================================================================
*/

-- Q1 (Medium): Create a VIEW named 'vw_ActiveITEmployees' that selects only Employees who belong to the 'IT' department.
-- [Write your query below]



-- Q2 (Medium): Create a Stored Procedure named 'usp_GetEmployeesByDept' that takes an input parameter @DeptName (NVARCHAR(100)) and returns all employees in that department.
-- [Write your query below]



-- Q3 (Medium-Hard): Create a Scalar UDF named 'fn_CalculateAnnualBonus' that takes an EmployeeID, calculates 10% of their Salary, and returns the numeric value.
-- [Write your query below]
-- Remember to test it using: SELECT EmployeeID, dbo.fn_CalculateAnnualBonus(EmployeeID) FROM Employees;



-- Q4 (Hard): Create an AFTER UPDATE Trigger on the Employees table named 'trg_AuditSalaryUpdate'. 
-- Whenever a salary is updated, simply print the old salary from the 'deleted' table and the new salary from the 'inserted' table. (Note: A real-world trigger would insert this into an Audit table).
-- [Write your query below]



-- Q5 (Hard): Write the SQL statement to create a Non-Clustered Index on the 'Email' column in the Employees table to speed up searches where Email is used in the WHERE clause.
-- [Write your query below]



/* 
ANSWERS:
Q1: 
CREATE VIEW vw_ActiveITEmployees AS
SELECT e.FirstName, e.LastName, e.Email FROM Employees e INNER JOIN Departments d ON e.DepartmentID = d.DepartmentID WHERE d.DepartmentName = 'IT';

Q2:
CREATE PROCEDURE usp_GetEmployeesByDept (@DeptName NVARCHAR(100))
AS
BEGIN
    SELECT e.* FROM Employees e INNER JOIN Departments d ON e.DepartmentID = d.DepartmentID WHERE d.DepartmentName = @DeptName;
END;

Q3:
CREATE FUNCTION fn_CalculateAnnualBonus (@EmpID INT)
RETURNS DECIMAL(10,2)
AS
BEGIN
    DECLARE @Bonus DECIMAL(10,2);
    SELECT @Bonus = (Salary * 0.10) FROM Employees WHERE EmployeeID = @EmpID;
    RETURN @Bonus;
END;

Q4:
CREATE TRIGGER trg_AuditSalaryUpdate 
ON Employees 
AFTER UPDATE 
AS 
BEGIN
    IF UPDATE(Salary)
    BEGIN
        DECLARE @OldSal DECIMAL(10,2), @NewSal DECIMAL(10,2);
        SELECT @OldSal = Salary FROM deleted;
        SELECT @NewSal = Salary FROM inserted;
        PRINT 'Salary change detected. Old: ' + CAST(@OldSal AS VARCHAR) + ' New: ' + CAST(@NewSal AS VARCHAR);
    END
END;

Q5: CREATE NONCLUSTERED INDEX IX_Employees_Email ON Employees(Email);
*/
