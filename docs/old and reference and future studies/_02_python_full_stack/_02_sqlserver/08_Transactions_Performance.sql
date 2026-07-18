/*
=============================================================================
SQL SERVER INTERVIEW PREPARATION - MODULE 08: TRANSACTIONS & PERFORMANCE
=============================================================================
NOTES:
------
1. Transactions & ACID:
   - A sequence of operations performed as a single logical unit of work.
   - ACID Properties:
     - Atomicity: "All or nothing".
     - Consistency: DB remains structurally sound throughout.
     - Isolation: Concurrent transactions don't interfere with each other.
     - Durability: Once committed, it's permanent (even if power fails).
   - BEGIN TRAN, COMMIT TRAN, ROLLBACK TRAN.
   - Typically wrapped in TRY...CATCH blocks for error handling.

2. Isolation Levels (Locking behaviors):
   - READ UNCOMMITTED (Lowest): Allows "Dirty Reads" (reading uncommitted data).
   - READ COMMITTED (Default in SQL Server): Prevents dirty reads.
   - REPEATABLE READ: Prevents dirty reads + "Non-repeatable reads" (data changing between two reads in same tran).
   - SERIALIZABLE (Highest/Most Restrictive): Prevents all above + "Phantom reads" (new rows appearing during the tran).
   - SNAPSHOT: Uses row-versioning (tempdb) rather than locking.

3. Performance Tuning Concepts:
   - Index Seek vs Index Scan: Seek is direct lookup (good). Scan reads every row (bad).
   - SARGable (Search ARGument ABLE) Queries: Queries that CAN use indexes. 
     - BAD (Non-SARGable): WHERE YEAR(OrderDate) = 2023 -> Cannot use index on OrderDate.
     - GOOD (SARGable): WHERE OrderDate >= '2023-01-01' AND OrderDate < '2024-01-01'
   - Avoid Cursors: Relational databases are optimized for "Set-Based" operations. Loops (cursors/while) are extremely slow because of row-by-row processing.

Interview Tips:
- Be prepared to explain ACID.
- Be prepared to explain the difference between a Dirty Read and a Phantom Read.
- "How do you optimize a slow query?" -> 1. Check Execution Plan. 2. Look for Scans instead of Seeks. 3. Check for missing indexes. 4. Ensure SARGability. 5. Update Statistics.
=============================================================================
*/

USE InterviewPrepDB;
GO

/*
=============================================================================
PRACTICE QUESTIONS (Difficulty: Medium to Hard)
=============================================================================
*/

-- Q1 (Medium): Write a template for a robust Transaction using TRY...CATCH. In the TRY block, explicitly divide 1 by 0 to cause an error, and ensure the Catch block rolls back the transaction.
-- [Write your query below]



-- Q2 (Medium): How can you write a SELECT query to read data from the Employees table WITHOUT putting shared locks on the data, intentionally allowing Dirty Reads?
-- [Write your query below]



-- Q3 (Medium-Hard): You need to find all Employees hired in the year 2021. 
-- Write a Non-SARGable version (using the YEAR() function), and then rewrite it to be SARGable.
-- [Write your query below]



-- Q4 (Hard): Explain what happens in a "Non-Repeatable Read" anomaly. Give a quick scenario.
-- [Write your explanation below]



-- Q5 (Hard): Explain "Phantom Read" and how the SERIALIZABLE isolation level prevents it.
-- [Write your explanation below]



/* 
ANSWERS:
Q1:
BEGIN TRY
    BEGIN TRAN;
       SELECT 1/0; -- Causes divide by zero error
    COMMIT TRAN;
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0
        ROLLBACK TRAN;
    PRINT 'Error occurred: ' + ERROR_MESSAGE();
END CATCH;

Q2: SELECT * FROM Employees WITH (NOLOCK);  -- OR: SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;

Q3 Non-SARGable: SELECT * FROM Employees WHERE YEAR(HireDate) = 2021;
Q3 SARGable:     SELECT * FROM Employees WHERE HireDate >= '2021-01-01' AND HireDate < '2022-01-01';

Q4: A non-repeatable read occurs when Transaction A reads a row, then Transaction B modifies or deletes that row and commits. If Transaction A reads that same row again, it gets different data. REPEATABLE READ isolation level prevents this by keeping shared locks until the transaction completes.

Q5: A phantom read occurs when Transaction A reads a set of rows matching a WHERE clause. Then Transaction B inserts NEW rows that match that WHERE clause. If Transaction A runs the exact same query again, "phantom" new rows appear in the result. SERIALIZABLE prevents this by placing a range lock on the entire dataset satisfying the search condition, preventing inserts into that range.
*/
