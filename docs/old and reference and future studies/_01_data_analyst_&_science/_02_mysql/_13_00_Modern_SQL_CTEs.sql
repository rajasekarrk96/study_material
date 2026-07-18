/*
================================================================================
STEP 13: CTEs AND WINDOW FUNCTIONS
================================================================================
GOAL:
Learn modern SQL patterns for writing readable multi-step queries and advanced
analytics without collapsing rows.
================================================================================
*/

USE student;

/*
--------------------------------------------------------------------------------
1. CTE
--------------------------------------------------------------------------------
- CTE means Common Table Expression
- Written with WITH
- Gives a temporary name to a query result
- Improves readability over deeply nested subqueries
--------------------------------------------------------------------------------
*/

WITH passing_students AS (
    SELECT student_name, mark
    FROM stud3
    WHERE mark >= 50
)
SELECT * FROM passing_students;

/*
--------------------------------------------------------------------------------
2. WHY USE CTEs
--------------------------------------------------------------------------------
1. Better readability
2. Reuse derived result in same query
3. Easier debugging
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
3. RECURSIVE CTE
--------------------------------------------------------------------------------
- Used for hierarchical or repeated sequence logic
- MySQL supports recursive CTEs in modern versions
--------------------------------------------------------------------------------
*/

/*
Example:
WITH RECURSIVE nums AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1 FROM nums WHERE n < 5
)
SELECT * FROM nums;
*/

/*
--------------------------------------------------------------------------------
4. WINDOW FUNCTIONS
--------------------------------------------------------------------------------
- Perform calculations across related rows
- Unlike GROUP BY, window functions do not collapse rows
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
5. ROW_NUMBER, RANK, DENSE_RANK
--------------------------------------------------------------------------------
ROW_NUMBER:
- unique sequence

RANK:
- same rank for ties, gaps appear

DENSE_RANK:
- same rank for ties, no gaps
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
6. OVER CLAUSE
--------------------------------------------------------------------------------
- Window functions use OVER(...)
- Can include ORDER BY and PARTITION BY
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
7. PARTITION BY
--------------------------------------------------------------------------------
- Divides rows into groups for window calculation
- Similar idea to grouping, but rows still remain visible
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
8. RUNNING TOTALS AND WINDOW AGGREGATES
--------------------------------------------------------------------------------
- SUM() OVER(...)
- AVG() OVER(...)
- MAX() OVER(...)
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
9. COMMON MISTAKES
--------------------------------------------------------------------------------
1. Confusing GROUP BY with window functions
2. Forgetting ORDER BY inside ranking logic
3. Expecting CTE to persist like a table
--------------------------------------------------------------------------------
*/

/*
================================================================================
SUMMARY
================================================================================
- CTEs make complex queries readable
- Recursive CTEs solve hierarchical and sequence problems
- Window functions rank, compare, and summarize while keeping every row visible
================================================================================
*/
