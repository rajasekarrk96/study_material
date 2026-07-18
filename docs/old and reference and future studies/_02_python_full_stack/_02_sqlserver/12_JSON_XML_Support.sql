/*
=============================================================================
SQL SERVER INTERVIEW PREPARATION - MODULE 12: JSON & XML SUPPORT
=============================================================================
NOTES:
------
1. JSON in SQL Server (2016+):
   - FOR JSON AUTO: Automatically formats query results as JSON based on the table structure.
   - FOR JSON PATH: Allows full control over the JSON output structure using dot notation (e.g., 'Employee.Name').
   - OPENJSON(): Parses JSON text and returns rows and columns.
   - ISJSON(): Checks if a string is valid JSON.
   - JSON_VALUE(): Extracts a scalar value from a JSON string.
   - JSON_QUERY(): Extracts an object or an array from a JSON string.

2. XML in SQL Server:
   - FOR XML AUTO / FOR XML PATH: Converts relational data to XML format.
   - nodes() / value(): Methods used to shred XML data back into relational format mapping.
   - While JSON is much more prevalent in modern APIs, legacy enterprise systems still rely heavily on XML.

Interview Tips:
- Understand that SQL Server doesn't have a dedicated "JSON" data type (unlike PostgreSQL). JSON is stored simply as standard NVARCHAR.
- FOR JSON PATH is extremely useful when building API backends directly with SQL Server.
=============================================================================
*/

USE InterviewPrepDB;
GO

/*
=============================================================================
PRACTICE QUESTIONS (Difficulty: Medium to Hard)
=============================================================================
*/

-- Q1 (Medium): Select the top 2 employees and output the result as a raw JSON array using FOR JSON AUTO.
-- [Write your query below]



-- Q2 (Medium-Hard): You have a JSON string: '{"Id": 1, "User": {"Name": "Alice", "Role": "Admin"}}'. 
-- Use JSON_VALUE to extract the User's Name into a column.
-- [Write your query below]



-- Q3 (Hard): Define a variable with a JSON array: '[{"DeptID":1, "Name":"HR"}, {"DeptID":2, "Name":"IT"}]'.
-- Use OPENJSON to parse this JSON array into a relational table format with columns DeptID (INT) and Name (VARCHAR).
-- [Write your query below]



-- Q4 (Medium): Write a query to export all records from the Departments table as XML output.
-- [Write your query below]



-- Q5 (Hard): Explain why SQL Server uses NVARCHAR to store JSON instead of a specific JSON data type. What function would you use inside a CHECK constraint to ensure only valid JSON is inserted?
-- [Write your explanation below]



/* 
ANSWERS:
Q1:
SELECT TOP 2 * FROM Employees FOR JSON AUTO;

Q2:
DECLARE @json NVARCHAR(MAX) = N'{"Id": 1, "User": {"Name": "Alice", "Role": "Admin"}}';
SELECT JSON_VALUE(@json, '$.User.Name') AS UserName;

Q3:
DECLARE @jsonArray NVARCHAR(MAX) = N'[{"DeptID":1, "Name":"HR"}, {"DeptID":2, "Name":"IT"}]';
SELECT * FROM OPENJSON(@jsonArray)
WITH (
    DeptID INT '$.DeptID',
    Name VARCHAR(50) '$.Name'
);

Q4:
SELECT * FROM Departments FOR XML AUTO, ELEMENTS; 
-- or FOR XML PATH('Department'), ROOT('Departments');

Q5:
Microsoft chose to use standard NVARCHAR so that existing database architectures wouldn't need to change to support JSON, and text compression/storage works natively. To ensure column data validity, you use the ISJSON() function in a constraint:
ALTER TABLE MyTable ADD CONSTRAINT chk_ValidJson CHECK (ISJSON(JsonDataColumn) = 1);
*/
