/*
=============================================================================
SQL SERVER INTERVIEW PREPARATION - MODULE 01: DDL & DML BASICS
=============================================================================
NOTES:
------
1. DDL (Data Definition Language):
   - CREATE: Generates a new database object (Table, View, Index, etc.)
   - ALTER: Modifies the structure of an existing object.
   - DROP: Deletes an object entirely from the database.
   - TRUNCATE: Quickly removes all rows from a table, resetting IDENTITY. 
     (Cannot be rolled back in some older databases, but in SQL Server it can be if inside a TRY/CATCH transaction). It doesn't fire delete triggers.

2. DML (Data Manipulation Language):
   - INSERT: Adds new rows.
   - UPDATE: Modifies existing data. Always use WHERE, or it updates ALL rows.
   - DELETE: Removes rows. Fires delete triggers. Slower than TRUNCATE.

Interview Tips:
- Be clear on TRUNCATE vs DELETE. (TRUNCATE is DDL, resets identity, faster. DELETE is DML, row-by-row logging, doesn't reset identity).
- Know what happens to constraints when you drop a table.
- Be cautious of updates/deletes without WHERE clauses.
=============================================================================
*/

USE InterviewPrepDB;
GO

/*
=============================================================================
PRACTICE QUESTIONS (Difficulty: Easy to Medium-Hard)
=============================================================================
*/

-- Q1 (Easy): Create a new table named 'Vendors' with columns VendorID (Primary Key), VendorName (Not Null), and ContactEmail.
-- [Write your query below]



-- Q2 (Easy): Insert two new rows into the 'Vendors' table.
-- [Write your query below]



-- Q3 (Medium): Add a new column 'IsActive' (BIT data type, default 1) to the 'Vendors' table using ALTER TABLE.
-- [Write your query below]



-- Q4 (Medium): Update the 'Vendors' table to set IsActive = 0 for the Vendor with VendorID = 1.
-- [Write your query below]



-- Q5 (Medium-Hard): You want to completely clear the 'Vendors' table and reset its primary key identity to 1 seamlessly. Write the statement. What happens if this table is referenced by a Foreign Key?
-- [Write your query below]



/* 
ANSWERS (Don't peek until you try!):
Q1: CREATE TABLE Vendors (VendorID INT IDENTITY(1,1) PRIMARY KEY, VendorName NVARCHAR(100) NOT NULL, ContactEmail NVARCHAR(100));
Q2: INSERT INTO Vendors (VendorName, ContactEmail) VALUES ('TechCorp', 'info@techcorp.com'), ('OfficeSupplies', 'sales@officesupplies.com');
Q3: ALTER TABLE Vendors ADD IsActive BIT DEFAULT 1;
Q4: UPDATE Vendors SET IsActive = 0 WHERE VendorID = 1;
Q5: TRUNCATE TABLE Vendors; -- Note: If it is referenced by an active Foreign Key, TRUNCATE will fail. You must drop the FK first, or use DELETE without WHERE (which won't reset identity).
*/
