/*
================================================================================
PART 1: CORE DEFINITIONS (DBMS / RDBMS / SQL)
================================================================================

🔹 DBMS (Database Management System)
A DBMS is software used to store, manage, and retrieve data.

Characteristics:
- Stores data in files or non-relational formats
- No strict relationships
- Less normalization
- Used for small-scale applications

Examples:
- Microsoft Access
- dBase
- FileMaker


🔹 RDBMS (Relational Database Management System)
An RDBMS is a type of DBMS where data is stored in tables 
(rows and columns) and relationships are maintained using keys.

Characteristics:
- Structured tables
- Primary Key & Foreign Key
- Supports SQL
- High data integrity
- Used in large systems

Examples:
- MySQL
- Oracle
- SQL Server
- IBM DB2

👉 Key Point:
All RDBMS are DBMS, but not all DBMS are RDBMS.


🔹 SQL (Structured Query Language)
Language used to interact with databases.

- Used to create, modify, and retrieve data
- Works mainly with RDBMS


================================================================================
PART 2: SQL SUB-LANGUAGES
================================================================================

DDL → Data Definition Language (Structure)
    CREATE, ALTER, DROP, TRUNCATE, RENAME

DML → Data Manipulation Language (Data)
    INSERT, UPDATE, DELETE

DQL → Data Query Language
    SELECT

TCL → Transaction Control
    COMMIT, ROLLBACK

DCL → Data Control
    GRANT, REVOKE


================================================================================
PART 3: DATABASE LEVEL DDL
================================================================================
*/
-- Create Database (Basic)
CREATE DATABASE student;

-- Safe Create (Recommended)
CREATE DATABASE IF NOT EXISTS student;

-- Select Database
USE student;

-- Drop Database (Dangerous)
-- Deletes entire database permanently
DROP DATABASE student;

-- Safe Drop
DROP DATABASE IF EXISTS student;


================================================================================
PART 4: TABLE CREATION (DDL)
================================================================================

/*
WHAT:
Tables store actual data in rows and columns.

WHY:
Database is empty until tables are created.
*/

-- Create Table
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY AUTO_INCREMENT,      -- Unique ID
    name VARCHAR(100) NOT NULL,             -- Name (cannot be NULL)
    age INT,                                -- Age
    department VARCHAR(100),                -- Department
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- View Table Structure
DESCRIBE students;

/*
================================================================================
PART 12: CONSTRAINTS & DATA INTEGRITY
================================================================================

WHAT:
Constraints are rules applied on table columns to restrict invalid data entry.

WHY:
- Ensures data accuracy
- Maintains consistency
- Prevents invalid or duplicate data
- Enforces business logic

IF VIOLATED:
→ INSERT / UPDATE will FAIL with an ERROR

================================================================================
TYPES OF CONSTRAINTS
================================================================================

1. NOT NULL
2. UNIQUE
3. PRIMARY KEY
4. FOREIGN KEY
5. CHECK
6. DEFAULT
7. AUTO_INCREMENT

================================================================================
1️⃣ NOT NULL CONSTRAINT
================================================================================

WHAT:
Prevents NULL (empty) values in a column

WHY:
Important fields must always have values

Example:
*/

CREATE TABLE student_notnull (
    id INT NOT NULL,
    name VARCHAR(50) NOT NULL
);

-- ❌ ERROR (NULL not allowed)
-- INSERT INTO student_notnull VALUES(NULL, 'Raj');

-- ✅ VALID
INSERT INTO student_notnull VALUES(1, 'Raj');


================================================================================
2️⃣ UNIQUE CONSTRAINT
================================================================================

WHAT:
Ensures all values in a column are unique (no duplicates)

NOTE:
- Allows ONE NULL (MySQL behavior)

Example:
*/

CREATE TABLE student_unique (
    email VARCHAR(100) UNIQUE
);

-- ❌ Duplicate error
-- INSERT INTO student_unique VALUES('a@gmail.com');
-- INSERT INTO student_unique VALUES('a@gmail.com');

-- ✅ VALID
INSERT INTO student_unique VALUES('b@gmail.com');


/*
COMPOSITE UNIQUE:
Combination of columns must be unique
*/

CREATE TABLE student_unique_combo (
    name VARCHAR(50),
    dept VARCHAR(50),
    UNIQUE(name, dept)
);
-- can have one value of null(because it is also a unique value)

================================================================================
3️⃣ PRIMARY KEY
================================================================================

WHAT:
- Combination of NOT NULL + UNIQUE
- Identifies each row uniquely

RULES:
- Only ONE per table
- Cannot be NULL
- No duplicates

Example:
*/

CREATE TABLE student_pk (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

/*
COMPOSITE PRIMARY KEY:
Multiple columns form primary key
*/

CREATE TABLE student_pk_combo (
    id INT,
    dept_id INT,
    name VARCHAR(50),
    PRIMARY KEY(id, dept_id)
);

/*
================================================================================
PART 13: INDEXES (DATABASE PERFORMANCE OPTIMIZATION)
================================================================================

WHAT:
An INDEX is a data structure that improves the speed of data retrieval 
operations on a table.

WHY:
- Faster SELECT queries
- Efficient searching, sorting, filtering
- Reduces full table scans

HOW IT WORKS:
- Works like a "book index"
- Instead of scanning entire table, DB jumps directly to data

NOTE:
- Improves READ performance
- Slightly slows INSERT, UPDATE, DELETE

================================================================================
1️⃣ TYPES OF INDEXES
================================================================================

1. PRIMARY INDEX (PRIMARY KEY)
2. UNIQUE INDEX
3. SIMPLE INDEX
4. COMPOSITE INDEX
5. FULLTEXT INDEX
6. SPATIAL INDEX (advanced)

================================================================================
2️⃣ PRIMARY INDEX
================================================================================

WHAT:
Automatically created when PRIMARY KEY is defined

FEATURES:
- Unique values
- No NULL allowed
- Only ONE per table

Example:
*/

CREATE TABLE student_pk_index (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

/*
👉 id column is automatically indexed
*/


================================================================================
3️⃣ UNIQUE INDEX
================================================================================

WHAT:
Ensures all values are unique

Example:
*/

CREATE TABLE student_unique_index (
    email VARCHAR(100) UNIQUE
);

/*
OR explicitly:
*/

CREATE UNIQUE INDEX idx_email
ON student_unique_index(email);


================================================================================
4️⃣ SIMPLE INDEX (NORMAL INDEX)
================================================================================

WHAT:
Index on a single column for faster search

Example:
*/

CREATE INDEX idx_name
ON student_unique_index(name);


/*
USE CASE:
- Searching names frequently
- WHERE name = 'Raj'
*/


================================================================================
5️⃣ COMPOSITE INDEX (MULTI-COLUMN)
================================================================================

WHAT:
Index on multiple columns

IMPORTANT:
Order matters!

Example:
*/

CREATE INDEX idx_name_dept
ON student_unique_index(name, department);

/*
Used when:
SELECT * FROM table WHERE name='Raj' AND department='AI';

NOTE:
- Works best if query uses columns in same order
*/


================================================================================
6️⃣ FULLTEXT INDEX
================================================================================

WHAT:
Used for searching large text data (full content)

Example:
*/

CREATE FULLTEXT INDEX idx_text
ON articles(content);

/*
Used for:
- Search engines
- Text search ("like Google")
*/

================================================================================
8️⃣ DROP INDEX
================================================================================

DROP INDEX idx_name ON student_unique_index;

-- OR (MySQL alternative)
ALTER TABLE student_unique_index DROP INDEX idx_name;


================================================================================
9️⃣ SHOW INDEX
================================================================================

SHOW INDEX FROM student_unique_index;


================================================================================
🔟 WHEN TO USE INDEX
================================================================================

✔ Columns used in WHERE
✔ Columns used in JOIN
✔ Columns used in ORDER BY
✔ Columns used in GROUP BY

Example:
SELECT * FROM students WHERE email='abc@gmail.com';


================================================================================
11️⃣ WHEN NOT TO USE INDEX
================================================================================

❌ Small tables
❌ Columns with frequent updates
❌ Columns with low uniqueness (e.g., gender)

================================================================================
12️⃣ PERFORMANCE IMPACT
================================================================================

ADVANTAGES:
✔ Faster SELECT queries
✔ Efficient searching

DISADVANTAGES:
❌ Slower INSERT/UPDATE/DELETE
❌ Extra storage required

================================================================================
13️⃣ REAL-WORLD EXAMPLE
================================================================================

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50)
);

-- Add indexes
CREATE INDEX idx_name ON users(name);
CREATE UNIQUE INDEX idx_email ON users(email);


================================================================================
14️⃣ INTERVIEW KEY POINTS
================================================================================

✔ Index improves READ performance
✔ Primary key automatically creates index
✔ Composite index order matters
✔ Too many indexes reduce performance
✔ Use EXPLAIN to analyze query performance

/*
================================================================================
PART 14: SHOW COMMANDS (METADATA / INFORMATION QUERIES)
================================================================================

WHAT:
SHOW commands are used to display database metadata (information about DB objects).

WHY:
- To inspect databases, tables, columns, indexes
- To debug schema issues
- To understand structure before writing queries

NOTE:
- These are READ-ONLY commands
- Mostly used in MySQL

================================================================================
1️⃣ SHOW DATABASES
================================================================================

WHAT:
Displays all databases in the server

Example:
*/

SHOW DATABASES;

/*
================================================================================
2️⃣ SHOW TABLES
================================================================================

WHAT:
Displays all tables in current database

IMPORTANT:
Use USE database_name first
*/

USE student;
SHOW TABLES;


================================================================================
3️⃣ SHOW COLUMNS / DESCRIBE
================================================================================

WHAT:
Displays structure of a table

SYNTAX:
*/

SHOW COLUMNS FROM students;

-- OR
DESCRIBE students;

/*
OUTPUT:
- Column name
- Data type
- NULL / NOT NULL
- Key (PRI, UNI, etc.)
- Default value
*/


================================================================================
4️⃣ SHOW CREATE TABLE
================================================================================

WHAT:
Displays exact SQL used to create the table

Example:
*/

SHOW CREATE TABLE students;

/*
VERY IMPORTANT:
- Used for backup
- Used to understand constraints/indexes
*/


================================================================================
5️⃣ SHOW INDEX
================================================================================

WHAT:
Displays indexes of a table

Example:
*/

SHOW INDEX FROM students;

/*
Shows:
- Index name
- Column name
- Unique / Non-unique
*/

================================================================================
6️⃣ SHOW TABLE STATUS
================================================================================

WHAT:
Displays detailed information about tables

Example:
*/

SHOW TABLE STATUS;

/*
Shows:
- Engine (InnoDB)
- Rows count
- Size
- Creation time
*/


================================================================================
7️⃣ SHOW VARIABLES
================================================================================

WHAT:
Displays system variables

Example:
*/

SHOW VARIABLES;

-- Specific variable
SHOW VARIABLES LIKE 'max_connections';


================================================================================
8️⃣ SHOW STATUS
================================================================================

WHAT:
Displays server status information

Example:
*/

SHOW STATUS;

-- Filter
SHOW STATUS LIKE 'Threads_connected';


================================================================================
9️⃣ SHOW ENGINES
================================================================================

WHAT:
Displays storage engines available

Example:
*/

SHOW ENGINES;

/*
Common engines:
- InnoDB (default)
- MyISAM
*/


================================================================================
🔟 SHOW GRANTS
================================================================================

WHAT:
Displays user permissions

Example:
*/

SHOW GRANTS FOR CURRENT_USER;


================================================================================
11️⃣ SHOW PROCESSLIST
================================================================================

WHAT:
Displays currently running queries

Example:
*/

SHOW PROCESSLIST;

/*
Useful for:
- Debugging slow queries
- Monitoring DB activity
*/


================================================================================
12️⃣ SHOW WARNINGS / ERRORS
================================================================================

WHAT:
Displays warnings or errors from last query

Example:
*/

SHOW WARNINGS;
SHOW ERRORS;


================================================================================
13️⃣ SHOW TRIGGERS / EVENTS / PROCEDURE STATUS
================================================================================

-- Triggers
SHOW TRIGGERS;

-- Stored Procedures
SHOW PROCEDURE STATUS;

-- Events
SHOW EVENTS;


================================================================================
14️⃣ BEST PRACTICES
================================================================================

✔ Use SHOW CREATE TABLE before modifying schema
✔ Use SHOW INDEX to optimize queries
✔ Use SHOW PROCESSLIST for debugging
✔ Use DESCRIBE for quick table structure
✔ Use SHOW VARIABLES to tune DB performance


================================================================================
PART 15: EXPLAIN SELECT (QUERY ANALYSIS / OPTIMIZATION)
================================================================================

WHAT:
EXPLAIN is used to analyze how MySQL executes a SELECT query.

WHY:
- Understand query performance
- Check if indexes are used
- Identify slow queries
- Optimize database queries

IMPORTANT:
EXPLAIN does NOT execute the query
→ It only shows execution plan

================================================================================
1️⃣ BASIC SYNTAX
================================================================================

EXPLAIN SELECT * FROM table_name;

-- Example:
EXPLAIN SELECT * FROM country;

================================================================================
2️⃣ YOUR EXAMPLE
================================================================================

EXPLAIN SELECT * 
FROM country 
WHERE name LIKE '%a%';


/*
WHAT THIS QUERY DOES:
- Fetch all rows from 'country'
- Filters rows where name contains letter 'a'

IMPORTANT:
LIKE '%a%' → leading wildcard
→ Index will NOT be used (full table scan)
*/


================================================================================
3️⃣ EXPLAIN OUTPUT COLUMNS
================================================================================

Column Name     Meaning
--------------------------------------------------------------

id              Query ID (execution order)

select_type     Type of query
                (SIMPLE, PRIMARY, SUBQUERY, etc.)

table           Table being accessed

type            Access type (VERY IMPORTANT)

possible_keys   Indexes that can be used

key             Index actually used

key_len         Length of index used

rows            Number of rows MySQL expects to scan

Extra           Additional info (Using where, Using index, etc.)


================================================================================
4️⃣ ACCESS TYPES (type column)
================================================================================

BEST → WORST PERFORMANCE

system          → Fastest (single row)
const           → Single row using index
eq_ref          → Unique index lookup
ref             → Non-unique index lookup
range           → Range scan (>, <, BETWEEN)
index           → Full index scan
ALL             → Full table scan (slowest)

IMPORTANT:
type = ALL → BAD (no index used)


================================================================================
5️⃣ ANALYSIS OF YOUR QUERY
================================================================================

EXPLAIN SELECT * FROM country WHERE name LIKE '%a%';

EXPECTED RESULT:

type: ALL
key: NULL
rows: large number
Extra: Using where

WHY?
- '%a%' starts with wildcard
- Index cannot be used
- Full table scan happens


================================================================================
6️⃣ OPTIMIZED VERSION
================================================================================

-- Better query (can use index)
SELECT * FROM country WHERE name LIKE 'a%';

WHY?
- Starts with fixed character
- Index can be used

================================================================================
4️⃣ FOREIGN KEY
================================================================================

WHAT:
Links one table to another

TERMS:
- Parent Table → has PRIMARY KEY
- Child Table → has FOREIGN KEY

RULE:
Cannot insert value in child table if not present in parent

Example:
*/

CREATE TABLE department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE student_fk (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    dept_id_ch INT,
    FOREIGN KEY(dept_id_ch) REFERENCES department(dept_id)
);

/*
IMPORTANT RULE:
❌ Cannot delete parent row if child exists
*/

-- DELETE FROM department WHERE dept_id = 1; -- ERROR


================================================================================
🔁 ON DELETE CASCADE
================================================================================

WHAT:
Automatically deletes child records when parent is deleted

Example:
*/

CREATE TABLE department2 (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE student_fk2 (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    dept_id INT,
    FOREIGN KEY(dept_id)
    REFERENCES department2(dept_id)
    ON DELETE CASCADE
);

-- Now deleting parent will delete child automatically


================================================================================
5️⃣ CHECK CONSTRAINT
================================================================================

WHAT:
Restricts values based on condition

Example:
*/

CREATE TABLE student_check (
    id INT,
    marks INT CHECK(marks >= 50 AND marks <= 100),
    city VARCHAR(50) CHECK(city IN ('chennai','pondy'))
);

-- ❌ ERROR
-- INSERT INTO student_check VALUES(1, 40, 'chennai');

-- ✅ VALID
INSERT INTO student_check VALUES(1, 90, 'chennai');


================================================================================
6️⃣ DEFAULT CONSTRAINT
================================================================================

WHAT:
Sets default value if not provided

Example:
*/

CREATE TABLE orders (
    id INT,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Auto fills date
INSERT INTO orders(id) VALUES(1);


================================================================================
7️⃣ AUTO_INCREMENT
================================================================================

WHAT:
Automatically generates increasing values

RULES:
- Used with PRIMARY KEY
- Starts from 1 (default)

Example:
*/

CREATE TABLE student_auto (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);

INSERT INTO student_auto(name) VALUES('Raj');
INSERT INTO student_auto(name) VALUES('Arun');

/*
To change starting value:
*/
ALTER TABLE student_auto AUTO_INCREMENT = 1001;


/*
NOTE:
- Deleted values are NOT reused
- Sequence always increases
*/

================================================================================
PART 5: ALTER TABLE (MODIFY STRUCTURE)
================================================================================

/*
WHAT:
Modify existing table structure
*/

-- Add UNIQUE
ALTER TABLE student_auto ADD UNIQUE(name);

-- Add NOT NULL
ALTER TABLE student_auto MODIFY name VARCHAR(50) NOT NULL;

-- Add FOREIGN KEY
ALTER TABLE child ADD FOREIGN KEY(col) REFERENCES parent(col);

-- Modify Column (change datatype but column data should be empty)
-- varchar(50)-> varchar(20) then data size should be less then 20 or equal to 20. 
ALTER TABLE students MODIFY age INT NOT NULL;

-- Rename Column
ALTER TABLE students RENAME COLUMN name TO student_name;

-- Change Column (rename + datatype)
ALTER TABLE students CHANGE student_name name VARCHAR(150);

-- Drop Column
ALTER TABLE students DROP COLUMN email;

-- Add Column (ervery time it will add at last)
ALTER TABLE students ADD email VARCHAR(100);

-- Add column at specific position
ALTER TABLE students ADD phone VARCHAR(15) AFTER name;

-- Add column as first
ALTER TABLE students ADD new_id INT FIRST;


================================================================================
PART 7: RENAME & DROP TABLE
================================================================================

-- Rename Table
RENAME TABLE students TO student_details;

-- Drop Table
-- Deletes table permanently
DROP TABLE student_details;

-- Safe Drop
DROP TABLE IF EXISTS student_details;


================================================================================
PART 8: TRUNCATE TABLE
================================================================================

/*
WHAT:
Deletes all records but keeps table structure
*/

TRUNCATE TABLE students;


================================================================================
PART 9: DATA TYPES (IMPORTANT FOR DDL)
================================================================================

🔹 STRING TYPES
CHAR(n)       → Fixed length
VARCHAR(n)    → Variable length
TEXT          → Large text

🔹 NUMERIC TYPES
INT           → Integer
FLOAT         → Decimal (approx)
DOUBLE        → High precision decimal
DECIMAL       → Exact value (money)

🔹 DATE TYPES
DATE          → YYYY-MM-DD
DATETIME      → Date + Time
TIMESTAMP     → Auto time tracking

🔹 BOOLEAN
BOOLEAN       → TRUE / FALSE


================================================================================
PART 10: COMPLETE DDL FLOW (REAL EXAMPLE)
================================================================================

-- Step 1: Create DB
CREATE DATABASE IF NOT EXISTS college;

-- Step 2: Use DB
USE college;

-- Step 3: Create Table
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT
);

-- Step 4: Modify Table
ALTER TABLE students ADD email VARCHAR(100);

-- Step 5: Rename Table
RENAME TABLE students TO college_students;

-- Step 6: Delete Table
-- DROP TABLE college_students;

-- Step 7: Delete Database
-- DROP DATABASE college;


================================================================================
END OF DDL NOTES
================================================================================
*/