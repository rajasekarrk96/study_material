/*
================================================================================
STEP 10: SYSTEM MAINTENANCE, LOCKS, TEMP TABLES, AND TABLE COPYING
================================================================================
GOAL:
Learn core administrative and maintenance commands used to manage sessions,
temporary storage, and structural copies of tables.
================================================================================
*/

USE student;

/*
--------------------------------------------------------------------------------
1. REPAIR TABLE
--------------------------------------------------------------------------------
- Used mainly for MyISAM tables
- Helps fix corruption issues
- Always keep backups before repair operations
--------------------------------------------------------------------------------
*/

/*
Example:
REPAIR TABLE memberships QUICK;
*/

/*
--------------------------------------------------------------------------------
2. LOCK TABLES
--------------------------------------------------------------------------------
- READ lock allows reads, blocks writes
- WRITE lock allows current session write access and blocks others
- Used carefully in maintenance workflows
--------------------------------------------------------------------------------
*/

LOCK TABLES det READ;
UNLOCK TABLES;

/*
--------------------------------------------------------------------------------
3. CONNECTION_ID
--------------------------------------------------------------------------------
- Shows current session id
--------------------------------------------------------------------------------
*/

SELECT CONNECTION_ID();

/*
--------------------------------------------------------------------------------
4. TEMPORARY TABLES
--------------------------------------------------------------------------------
- Exist only in current session
- Useful for intermediate query results
- Automatically removed when session ends
--------------------------------------------------------------------------------
*/

CREATE TEMPORARY TABLE temp_demo (
    id INT,
    name VARCHAR(50)
);

INSERT INTO temp_demo VALUES (1, 'demo');
SELECT * FROM temp_demo;
DROP TEMPORARY TABLE IF EXISTS temp_demo;

/*
--------------------------------------------------------------------------------
5. COPYING TABLE STRUCTURE
--------------------------------------------------------------------------------
- CREATE TABLE new_table LIKE old_table
- copies structure including indexes in normal cases
--------------------------------------------------------------------------------
*/

/*
Example:
CREATE TABLE det_copy LIKE det;
*/

/*
--------------------------------------------------------------------------------
6. COPYING STRUCTURE AND DATA
--------------------------------------------------------------------------------
- CREATE TABLE ... AS SELECT ...
- copies result data
- may not fully copy constraints and indexes
--------------------------------------------------------------------------------
*/

/*
Example:
CREATE TABLE det_data_copy AS
SELECT * FROM det;
*/

/*
--------------------------------------------------------------------------------
7. SHOW PROCESSLIST
--------------------------------------------------------------------------------
- Shows running sessions and queries
- useful for diagnostics
--------------------------------------------------------------------------------
*/

SHOW PROCESSLIST;

/*
--------------------------------------------------------------------------------
8. SHOW STATUS AND VARIABLES
--------------------------------------------------------------------------------
- Server metadata and runtime information
--------------------------------------------------------------------------------
*/

SHOW VARIABLES;
SHOW STATUS;

/*
--------------------------------------------------------------------------------
9. COMMON MISTAKES
--------------------------------------------------------------------------------
1. Using REPAIR TABLE assuming it works for every engine
2. Forgetting to UNLOCK TABLES
3. Expecting temporary tables to remain across sessions
4. Assuming CREATE TABLE AS SELECT copies every constraint
--------------------------------------------------------------------------------
*/

/*
================================================================================
SUMMARY
================================================================================
- REPAIR TABLE is mainly for MyISAM repair scenarios
- Locks control concurrent access
- Temporary tables are session-scoped
- Table cloning can copy structure only or structure plus data
================================================================================
*/
