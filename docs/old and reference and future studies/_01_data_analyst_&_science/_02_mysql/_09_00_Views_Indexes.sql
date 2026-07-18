/*
================================================================================
STEP 09: VIEWS, INDEXES, EXPLAIN, AND METADATA
================================================================================
GOAL:
Learn how to save query logic using views, improve lookup speed using indexes,
inspect execution plans, and read database metadata.
================================================================================
*/

USE world;

/*
--------------------------------------------------------------------------------
1. VIEW
--------------------------------------------------------------------------------
- A view is a virtual table based on a SELECT query
- It stores query definition, not data itself in normal cases
--------------------------------------------------------------------------------
*/

CREATE OR REPLACE VIEW v_country_basic AS
SELECT code, name, continent, population
FROM country;

SELECT * FROM v_country_basic;

/*
--------------------------------------------------------------------------------
2. WHY USE VIEWS
--------------------------------------------------------------------------------
1. Simplify repeated queries
2. Hide complex joins
3. Limit direct access to sensitive columns
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
3. DROP VIEW
--------------------------------------------------------------------------------
*/

DROP VIEW IF EXISTS v_country_basic;

/*
--------------------------------------------------------------------------------
4. INDEX
--------------------------------------------------------------------------------
- Index speeds up data lookup
- Often useful on WHERE, JOIN, ORDER BY, GROUP BY columns
- Too many indexes slow INSERT, UPDATE, DELETE
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
5. CREATE INDEX
--------------------------------------------------------------------------------
*/

CREATE INDEX idx_country_name
ON country(name);

/*
--------------------------------------------------------------------------------
6. UNIQUE INDEX
--------------------------------------------------------------------------------
- Ensures uniqueness and speeds lookup
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
7. DROP INDEX
--------------------------------------------------------------------------------
*/

DROP INDEX idx_country_name ON country;

/*
--------------------------------------------------------------------------------
8. EXPLAIN
--------------------------------------------------------------------------------
- EXPLAIN shows how MySQL plans to execute a query
- Helps detect full scans and index usage
--------------------------------------------------------------------------------
*/

EXPLAIN SELECT * FROM country WHERE name LIKE 'A%';

/*
--------------------------------------------------------------------------------
9. SHOW AND DESCRIBE
--------------------------------------------------------------------------------
- SHOW DATABASES
- SHOW TABLES
- SHOW COLUMNS
- SHOW CREATE TABLE
- SHOW INDEX
- DESCRIBE
--------------------------------------------------------------------------------
*/

SHOW DATABASES;
SHOW TABLES;
DESCRIBE country;
SHOW COLUMNS FROM country;
SHOW CREATE TABLE country;
SHOW INDEX FROM country;

/*
--------------------------------------------------------------------------------
10. COMMON MISTAKES
--------------------------------------------------------------------------------
1. Creating indexes on everything
2. Expecting index use with leading wildcard searches
3. Assuming view stores copied data
--------------------------------------------------------------------------------
*/

/*
================================================================================
SUMMARY
================================================================================
- Views simplify query reuse
- Indexes improve read performance
- EXPLAIN helps analyze queries
- SHOW and DESCRIBE reveal metadata
================================================================================
*/
