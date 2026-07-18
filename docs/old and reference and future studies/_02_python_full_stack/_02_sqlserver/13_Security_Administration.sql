/*
=============================================================================
SQL SERVER INTERVIEW PREPARATION - MODULE 13: SECURITY & ADMINISTRATION
=============================================================================
NOTES:
------
1. Authentication vs Authorization:
   - Authentication (Logins): Identifying WHO the user is at the Server level. 
     (e.g., Windows Authentication vs SQL Server Authentication).
   - Authorization (Users/Roles): Determining WHAT the authenticated user can do at the Database level.
   
2. Core Security Hierarchy:
   - Server Level: Server Roles (sysadmin, serveradmin, securityadmin).
   - Database Level: Database Roles (db_owner, db_datareader, db_datawriter).
   - Object Level: Tables, Views, Stored Procedures permissions.

3. DCL (Data Control Language) Commands:
   - GRANT: Gives a permission.
   - REVOKE: Removes a previously granted or denied permission.
   - DENY: Explicitly prevents a user from performing an action (Overrides any GRANTs from other roles).

4. Row-Level Security (RLS) & Dynamic Data Masking (DDM):
   - RLS: Restricts read/write access to certain rows based on user execution context. Uses Security Predicate functions.
   - DDM: Hides sensitive data (like credit cards, emails) from non-privileged users without changing the actual data on disk.

Interview Tips:
- Understand the difference between a LOGIN and a USER. (Login maps to the Server; User maps to a Database. A Login can map to multiple Users across different DBs).
- "A user belongs to Role A which has GRANT SELECT, and Role B which has DENY SELECT. Can they select?" -> NO. DENY always wins.
- Principle of Least Privilege: Always grant only the permissions absolutely necessary for a job.
=============================================================================
*/

USE InterviewPrepDB;
GO

/*
=============================================================================
PRACTICE QUESTIONS (Difficulty: Medium to Hard)
=============================================================================
*/

-- Q1 (Medium): Write a command to create a SQL Server Login named 'ReportUser' with the password 'P@ssw0rd123'. 
-- (Note: Do not actually run this on a production system without permission).
-- [Write your query below]



-- Q2 (Medium): Map the 'ReportUser' login to a Database User inside 'InterviewPrepDB' named 'ReportUser'.
-- [Write your query below]



-- Q3 (Medium-Hard): You want 'ReportUser' to be able to read all tables in the database, but NEVER be able to insert, update, or delete. 
-- How do you assign them to the appropriate built-in database role?
-- [Write your query below]



-- Q4 (Hard): Explain what happens when you run REVOKE SELECT on a table for a user, versus DENY SELECT.
-- [Write your explanation below]



-- Q5 (Hard): Write a query to apply Dynamic Data Masking to the 'Email' column of the Employees table so that it appears as 'aXXX@XXXX.com' to unprivileged users. 
-- What permission must you grant a user so they can bypass the mask and see the real email?
-- [Write your query below]



/* 
ANSWERS:
Q1: CREATE LOGIN ReportUser WITH PASSWORD = 'P@ssw0rd123';
Q2: CREATE USER ReportUser FOR LOGIN ReportUser;
Q3: ALTER ROLE db_datareader ADD MEMBER ReportUser;

Q4:
REVOKE simply removes a previously granted permission. If the user still has SELECT access via another role (like db_datareader), they can still select. 
DENY explicitly blocks the permission. Even if the user belongs to `db_datareader` or `db_owner`, a direct DENY on their account or a sub-role will prevent them from selecting. (Note: DENY does not override sysadmin privileges).

Q5:
ALTER TABLE Employees ALTER COLUMN Email ADD MASKED WITH (FUNCTION = 'email()');
-- To allow a specific user to see the unmasked data:
-- GRANT UNMASK TO ReportUser;
*/
