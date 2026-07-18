/*
================================================================================
STEP 02: DATA MANAGEMENT (DML & TCL – COMPLETE GUIDE)
================================================================================
GOAL:
Learn how to insert, update, delete, and safely manage data using transactions.

--------------------------------------------------------------------------------
1. CORE DEFINITIONS (WHAT & WHY)
--------------------------------------------------------------------------------

🔹 DML (Data Manipulation Language)
- Used to manipulate data inside tables
- Commands: INSERT, UPDATE, DELETE

🔹 TCL (Transaction Control Language)
- Used to control transactions (data changes)
- Commands: COMMIT, ROLLBACK, SAVEPOINT

================================================================================
*/

USE student;

-- ---------------------------------------------------------
-- PART A: INSERT INTO (ADDING DATA)
-- ---------------------------------------------------------
/*
WHAT:
Insert new records into a table

WHY:
To store new data (students, users, sensor data, etc.)
*/

-- Method 1: Insert all columns
INSERT INTO det VALUES (1, 'rajasekar');

-- Method 2: Insert specific columns (recommended)
INSERT INTO det (sno, name) VALUES (2, 'sekar');
INSERT INTO det (sno) VALUES (2,);

-- Insert NULL
INSERT INTO det (sno, name) VALUES (3, NULL);

-- Insert multiple rows
INSERT INTO det (sno, name) VALUES
(4, 'arun'),
(5, 'kumar');

-- Insert from another table
INSERT INTO det_copy (sno, name) SELECT sno, name FROM det;

/*
================================================================================
PART B: UPDATE (MODIFY DATA)
================================================================================

WHAT:
Modify existing records

IMPORTANT:
Always use WHERE condition (to avoid full update)
*/

-- Disable safe mode (only if needed)
SET sql_safe_updates = 0;

-- Update single column
UPDATE country
SET surfacearea = 345.56 -- new value
WHERE name = 'aruba'; -- ??

-- Update multiple columns
UPDATE country
SET surfacearea = 193.00, indepyear = 1996
WHERE name = 'aruba';

-- Update to NULL
UPDATE country
SET indepyear = NULL
WHERE name = 'aruba';

-- Update using condition
UPDATE det
SET name = 'updated_name'
WHERE sno > 3;


/*
================================================================================
PART C: DELETE (REMOVE DATA)
================================================================================

WHAT:
Deletes specific rows

IMPORTANT:
DELETE supports ROLLBACK
*/
-- Delete specific row
DELETE FROM det WHERE sno = 2;

-- Delete multiple rows
DELETE FROM det WHERE sno > 3;

set autocommit=0;

-- Delete all rows (slow but rollback possible)
DELETE FROM det;
rollback;
commit;

/*
================================================================================
PART D: TRUNCATE (FAST DELETE)
================================================================================

WHAT:
Deletes ALL data instantly

DIFFERENCE:
- TRUNCATE → DDL
- DELETE → DML

IMPORTANT:
❌ Cannot rollback TRUNCATE
*/

-- TRUNCATE TABLE det;


/*
================================================================================
PART E: TCL (TRANSACTION CONTROL)
================================================================================

WHAT:
Control saving or undoing changes

CONCEPT:
Transaction = Group of SQL operations

STEPS:
1. Start transaction
2. Perform operations
3. COMMIT or ROLLBACK
*/

-- Disable auto-commit
SET autocommit = 0;

-- Example transaction
DELETE FROM country;

-- Undo changes
ROLLBACK;

-- Confirm changes
COMMIT;


/*
================================================================================
PART F: SAVEPOINT (ADVANCED TCL)
================================================================================

WHAT:
Create checkpoints inside transaction

WHY:
Partial rollback possible
*/

SET autocommit = 0;

DELETE FROM det WHERE sno = 1;

SAVEPOINT sp1;

DELETE FROM det WHERE sno = 2;

-- Rollback to savepoint
ROLLBACK TO sp1;

-- Final commit
COMMIT;




================================================================================
PART G: UPSERT (INSERT OR UPDATE)
================================================================================

WHAT:
UPSERT = Insert + Update

- If record DOES NOT exist → INSERT
- If record EXISTS (duplicate key) → UPDATE

WHY:
- Avoid duplicate errors
- Handle real-time data (IoT, user updates, logs)
- Reduce multiple queries (INSERT + UPDATE separately)

IMPORTANT:
UPSERT works based on:
✔ PRIMARY KEY
✔ UNIQUE KEY

================================================================================
1️⃣ METHOD 1: INSERT IGNORE
================================================================================

WHAT:
- Ignores duplicate key errors
- Skips insertion if duplicate exists

SYNTAX:
*/

INSERT IGNORE INTO det (sno, name)
VALUES (1, 'duplicate');

/*
BEHAVIOR:

CASE 1: sno = 1 NOT EXISTS
→ INSERT happens

CASE 2: sno = 1 EXISTS
→ IGNORE (no error, no update)

IMPORTANT:
❌ Does NOT update existing data
✔ Only prevents error

USE CASE:
- Avoid crashing application
- Bulk insert where duplicates may exist

================================================================================
2️⃣ METHOD 2: ON DUPLICATE KEY UPDATE (REAL UPSERT)
================================================================================

WHAT:
- Inserts new row OR updates existing row

SYNTAX:
*/

INSERT INTO det (sno, name)
VALUES (1, 'raj')
ON DUPLICATE KEY UPDATE name = 'updated_raj';

/*
BEHAVIOR:

CASE 1: sno = 1 NOT EXISTS
→ INSERT (1, 'raj')

CASE 2: sno = 1 EXISTS
→ UPDATE name = 'updated_raj'

IMPORTANT:
✔ True UPSERT
✔ Updates existing records

================================================================================
3️⃣ INTERNAL WORKING
================================================================================

STEP 1:
Try INSERT

STEP 2:
If duplicate key error occurs →
→ Execute UPDATE instead

================================================================================
4️⃣ REQUIREMENTS
================================================================================

UPSERT works only if:

✔ PRIMARY KEY exists
OR
✔ UNIQUE constraint exists

Example:
*/

CREATE TABLE det (
    sno INT PRIMARY KEY,
    name VARCHAR(50)
);

/*
================================================================================
5️⃣ MULTIPLE COLUMN UPDATE
================================================================================

INSERT INTO det (sno, name)
VALUES (1, 'raj')
ON DUPLICATE KEY UPDATE 
    name = 'updated_raj';

-- Example with multiple columns:
-- col1 = VALUES(col1), col2 = VALUES(col2)

================================================================================
6️⃣ UPSERT WITH VALUES() FUNCTION
================================================================================

WHAT:
Reuse inserted values in update

Example:
*/

INSERT INTO det (sno, name)
VALUES (1, 'raj')
ON DUPLICATE KEY UPDATE name = VALUES(name);

/*
NOTE:
VALUES() is deprecated in MySQL 8.0.20+
Use alias instead:

INSERT INTO det AS new
VALUES (1, 'raj')
ON DUPLICATE KEY UPDATE name = new.name;

================================================================================
7️⃣ DIFFERENCE: IGNORE vs DUPLICATE UPDATE
================================================================================

Feature              INSERT IGNORE        ON DUPLICATE KEY UPDATE
------------------------------------------------------------------
Duplicate handling   Skips row            Updates row
Error                No error             No error
Data change          No change            Updates existing data
Use case             Avoid crash          Real UPSERT

================================================================================
8️⃣ REAL-WORLD EXAMPLE (YOUR PROJECT)
================================================================================

-- Example: Sensor data update

INSERT INTO sensor_data (id, temp)
VALUES (1, 30)
ON DUPLICATE KEY UPDATE temp = 30;

/*
Scenario:
- If sensor ID exists → update temp
- If not → insert new record
*/

================================================================================
9️⃣ COMMON MISTAKES
================================================================================

❌ No PRIMARY KEY → UPSERT won't work
❌ Expecting INSERT IGNORE to update → it won't
❌ Wrong column mapping

================================================================================
🔟 BEST PRACTICES
================================================================================

✔ Use ON DUPLICATE KEY UPDATE for real applications
✔ Use INSERT IGNORE only for bulk safe inserts
✔ Always define PRIMARY KEY
✔ Use UPSERT for APIs and IoT data

================================================================================
11️⃣ INTERVIEW QUESTIONS
================================================================================

Q1: What is UPSERT?
→ Insert or update if record exists

Q2: Difference between INSERT IGNORE and UPSERT?
→ IGNORE skips, UPSERT updates

Q3: What constraint is required?
→ PRIMARY KEY or UNIQUE

Q4: Can UPSERT work without key?
→ NO

================================================================================
END OF UPSERT NOTES
================================================================================
*/


/*
================================================================================
PART H: REPLACE (ALTERNATIVE TO UPSERT)
================================================================================

WHAT:
Deletes existing row and inserts new row

IMPORTANT:
Acts like DELETE + INSERT
*/

REPLACE INTO det (sno, name)
VALUES (1, 'new_name');


================================================================================
PART I: LIMIT WITH DELETE / UPDATE
================================================================================

WHAT:
Restrict number of rows affected

WHAT:
LIMIT is used to restrict the number of rows returned or affected.

WHY:
- Improve performance
- Fetch only required rows
- Control updates/deletes safely

================================================================================
1️⃣ LIMIT WITH SELECT
================================================================================

QUERY:
SELECT * FROM det LIMIT 5;

WHAT:
- Returns first 5 rows from table

IMPORTANT:
- Order is NOT guaranteed unless ORDER BY is used

BETTER PRACTICE:
*/

SELECT * FROM det
ORDER BY sno
LIMIT 5;

/*
================================================================================
2️⃣ LIMIT WITH OFFSET (PAGINATION)
================================================================================

WHAT:
Skip rows and fetch next set

SYNTAX:
LIMIT offset, count

Example:
*/

SELECT * FROM det
LIMIT 5, 5;

/*
Meaning:
- Skip first 5 rows
- Fetch next 5 rows

USED IN:
✔ Pagination (page 1, page 2, etc.)

================================================================================
3️⃣ LIMIT WITH DELETE
================================================================================

QUERY:
DELETE FROM det LIMIT 2;

WHAT:
- Deletes first 2 rows

IMPORTANT:
❌ Without ORDER BY → random rows deleted
✔ Always use ORDER BY

SAFE VERSION:
*/

DELETE FROM det
ORDER BY sno
LIMIT 2;

/*
================================================================================
4️⃣ LIMIT WITH UPDATE
================================================================================

QUERY:
UPDATE det SET name = 'test' LIMIT 1;

WHAT:
- Updates only 1 row

IMPORTANT:
❌ Without ORDER BY → unpredictable row
✔ Always use ORDER BY

SAFE VERSION:
*/

UPDATE det
SET name = 'test'
ORDER BY sno
LIMIT 1;


================================================================================
5️⃣ LIMIT WITH WHERE
================================================================================

SELECT * FROM det
WHERE sno > 2
LIMIT 3;


================================================================================
6️⃣ LIMIT WITH ORDER BY (BEST PRACTICE)
================================================================================

SELECT * FROM det
ORDER BY sno DESC
LIMIT 3;


Returns:
Top 3 highest sno values

================================================================================
7️⃣ LIMIT vs TOP (INTERVIEW)
================================================================================

MySQL:
    LIMIT 5

SQL Server:
    SELECT TOP 5 *

================================================================================
8️⃣ IMPORTANT RULES
================================================================================

✔ Always use ORDER BY with LIMIT
✔ LIMIT is MySQL-specific
✔ Used in SELECT, UPDATE, DELETE

================================================================================
9️⃣ REAL-WORLD USE CASES
================================================================================

✔ Pagination (web apps)
✔ Top records (top 10 students)
✔ Controlled updates/deletes
✔ Testing queries safely

================================================================================
🔟 COMMON MISTAKES
================================================================================

❌ Using LIMIT without ORDER BY
❌ Assuming fixed row order
❌ Using LIMIT in unsupported DBs



================================================================================
PART J: ORDER BY WITH UPDATE / DELETE
================================================================================
-- select __ from ____ where->group by->having->order by
/*
================================================================================
PART X: COMPLETE SQL QUERY FLOW (SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY)
================================================================================

GOAL:
Understand how to write, execute, and optimize SQL queries from basic to advanced.

================================================================================
1️⃣ STANDARD SYNTAX (HOW WE WRITE)
================================================================================

SELECT column_list
FROM table_name
WHERE condition
GROUP BY column_list
HAVING condition
ORDER BY column_list;

================================================================================
2️⃣ ACTUAL EXECUTION ORDER (HOW DATABASE RUNS)
================================================================================

1. FROM
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY

👉 IMPORTANT:
SQL does NOT execute in the order you write

================================================================================
3️⃣ STEP-BY-STEP CONCEPT
================================================================================

🔹 FROM
- Selects table
- Loads data into memory

Example:
FROM students

--------------------------------------------------

🔹 WHERE
- Filters rows BEFORE grouping
- Works on individual rows

Example:
WHERE age > 18

--------------------------------------------------

🔹 GROUP BY
- Groups rows with same values
- Used with aggregate functions

Example:
GROUP BY department

--------------------------------------------------

🔹 HAVING
- Filters groups AFTER grouping
- Works with aggregate values

Example:
HAVING COUNT(*) > 2

--------------------------------------------------

🔹 SELECT
- Chooses columns to display

Example:
SELECT department, COUNT(*)

--------------------------------------------------

🔹 ORDER BY
- Sorts final result

Example:
ORDER BY department ASC

================================================================================
4️⃣ COMPLETE EXAMPLE (IMPORTANT)
================================================================================

SELECT department, COUNT(*) AS total_students
FROM students
WHERE age > 18
GROUP BY department
HAVING COUNT(*) > 2
ORDER BY total_students DESC;

================================================================================
5️⃣ EXECUTION FLOW (DETAILED)
================================================================================

Step 1 → FROM students
Step 2 → WHERE age > 18
Step 3 → GROUP BY department
Step 4 → HAVING COUNT(*) > 2
Step 5 → SELECT department, COUNT(*)
Step 6 → ORDER BY total_students DESC

================================================================================
6️⃣ WHERE vs HAVING (VERY IMPORTANT)
================================================================================

WHERE:
✔ Filters rows
✔ Cannot use aggregate functions
✔ Runs BEFORE grouping

HAVING:
✔ Filters grouped data
✔ Can use aggregate functions
✔ Runs AFTER grouping

Example:

-- ❌ WRONG
SELECT department FROM students WHERE COUNT(*) > 2;

-- ✅ CORRECT
SELECT department FROM students
GROUP BY department
HAVING COUNT(*) > 2;

================================================================================
7️⃣ AGGREGATE FUNCTIONS
================================================================================

COUNT()  → number of rows
SUM()    → total
AVG()    → average
MIN()    → smallest value
MAX()    → largest value

Example:
SELECT department, AVG(age)
FROM students
GROUP BY department;

================================================================================
8️⃣ ORDER BY DETAILS
================================================================================

ASC  → ascending (default)
DESC → descending

Multiple columns:
ORDER BY dept ASC, age DESC

================================================================================
9️⃣ GROUP BY RULES (IMPORTANT)
================================================================================

✔ All non-aggregated columns must be in GROUP BY

Example:

-- ❌ ERROR
SELECT name, COUNT(*) FROM students;

-- ✅ CORRECT
SELECT name, COUNT(*)
FROM students
GROUP BY name;

================================================================================
🔟 DISTINCT vs GROUP BY
================================================================================

DISTINCT:
Removes duplicates

GROUP BY:
Groups data + supports aggregates

Example:
SELECT DISTINCT department FROM students;

================================================================================
11️⃣ LIMIT (OPTIONAL – MYSQL)
================================================================================

Used to restrict rows

Example:
SELECT * FROM students
ORDER BY age DESC
LIMIT 5;

================================================================================
12️⃣ ALIAS (AS)
================================================================================

Rename column

Example:
SELECT COUNT(*) AS total FROM students;

================================================================================
13️⃣ ADVANCED EXAMPLE
================================================================================

SELECT department, AVG(age) AS avg_age
FROM students
WHERE age > 18
GROUP BY department
HAVING AVG(age) > 20
ORDER BY avg_age DESC
LIMIT 3;

================================================================================
14️⃣ COMMON MISTAKES
================================================================================

❌ Using aggregate in WHERE
❌ Missing GROUP BY columns
❌ Not using ORDER BY with LIMIT
❌ Confusing WHERE and HAVING

================================================================================
15️⃣ PERFORMANCE TIPS
================================================================================

✔ Filter early using WHERE
✔ Use indexes on WHERE columns
✔ Avoid unnecessary GROUP BY
✔ Use LIMIT for large datasets

================================================================================
16️⃣ INTERVIEW QUESTIONS
================================================================================

Q1: SQL execution order?
→ FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY

Q2: WHERE vs HAVING?
→ WHERE filters rows, HAVING filters groups

Q3: Can we use COUNT in WHERE?
→ NO

Q4: Why SELECT is after GROUP BY?
→ Because grouping must be completed first

================================================================================
17️⃣ REAL-WORLD EXAMPLE
================================================================================

-- Top 3 departments with highest average marks

SELECT department, AVG(marks) AS avg_marks
FROM students
WHERE marks > 50
GROUP BY department
HAVING AVG(marks) > 60
ORDER BY avg_marks DESC
LIMIT 3;

================================================================================
END OF COMPLETE SQL FLOW NOTES
================================================================================
*/

