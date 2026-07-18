/*
=============================================================================
SQL SERVER INTERVIEW PREPARATION - MODULE 11: PIVOT, UNPIVOT & MERGE
=============================================================================
NOTES:
------
1. PIVOT:
   - Transforms a dataset by turning unique values from one column into MULTIPLE columns in the output, performing aggregations along the way.
   - Typically used for reporting (e.g., turning "Month" rows into "Jan", "Feb", "Mar" columns).

2. UNPIVOT:
   - The exact opposite of PIVOT. Transforms columns back into rows.
   - Useful when dealing with poorly designed schemas (like having SalesQ1, SalesQ2, SalesQ3 columns instead of a 'Quarter' column and a 'Sales' column).

3. MERGE (The "UPSERT"):
   - Performs INSERT, UPDATE, or DELETE operations on a target table based on the results of a join with a source table.
   - Extremely powerful for data warehousing (ETL) and synchronizing tables.
   - WHEN MATCHED -> UPDATE
   - WHEN NOT MATCHED BY TARGET -> INSERT
   - WHEN NOT MATCHED BY SOURCE -> DELETE (Optional)

Interview Tips:
- PIVOT syntax is famously clunky. Interviewers often look for your logic here or whether you know the alternative: using conditional aggregation (SUM(CASE WHEN Month='Jan' THEN Sales END)).
- MERGE requires a semicolon at the very end. Omitting it causes a syntax error!
=============================================================================
*/

USE InterviewPrepDB;
GO

/*
=============================================================================
PRACTICE QUESTIONS (Difficulty: Hard)
=============================================================================
*/

-- Setup: Let's create a quick temp table for Sales data to practice Pivoting
CREATE TABLE #SalesData (Year INT, Department VARCHAR(50), Revenue INT);
INSERT INTO #SalesData VALUES (2022, 'IT', 100), (2022, 'HR', 50), (2023, 'IT', 150), (2023, 'HR', 75);

-- Q1 (Hard): Use the PIVOT operator to transpose #SalesData so that 'IT' and 'HR' become columns, and the rows represent the Year.
-- [Write your query below]



-- Q2 (Hard): Achieve the exact same result as Q1 WITHOUT using the PIVOT operator. Use Conditional Aggregation (SUM with CASE). Highly recommended approach!
-- [Write your query below]



-- Setup: Let's create tables to practice MERGE
CREATE TABLE #TargetTable (ID INT PRIMARY KEY, Val VARCHAR(50));
INSERT INTO #TargetTable VALUES (1, 'Old A'), (2, 'Old B');

CREATE TABLE #SourceTable (ID INT PRIMARY KEY, Val VARCHAR(50));
INSERT INTO #SourceTable VALUES (1, 'New A'), (3, 'New C');

-- Q3 (Hard): Write a MERGE statement to synchronize #TargetTable with #SourceTable. 
-- If an ID matches, UPDATE the Val. If an ID exists in Source but not Target, INSERT it.
-- Don't forget the semicolon at the end!
-- [Write your query below]



-- Q4 (Hard): Explain what UNPIVOT does and write a conceptual query to Unpivot the result of Q1 back into rows.
-- [Write your explanation below]



-- Q5 (Hard): What are the performance implications of the MERGE statement compared to separate UPDATE and INSERT statements?
-- [Write your explanation below]



/* 
ANSWERS:
Q1:
SELECT Year, [IT], [HR]
FROM (
    SELECT Year, Department, Revenue FROM #SalesData
) AS SourceTable
PIVOT (
    SUM(Revenue) FOR Department IN ([IT], [HR])
) AS PivotTable;

Q2 (Conditional Aggregation - often faster and more flexible than PIVOT):
SELECT 
    Year,
    SUM(CASE WHEN Department = 'IT' THEN Revenue ELSE 0 END) AS IT,
    SUM(CASE WHEN Department = 'HR' THEN Revenue ELSE 0 END) AS HR
FROM #SalesData
GROUP BY Year;

Q3:
MERGE INTO #TargetTable AS tgt
USING #SourceTable AS src
ON tgt.ID = src.ID
WHEN MATCHED THEN
    UPDATE SET tgt.Val = src.Val
WHEN NOT MATCHED BY TARGET THEN
    INSERT (ID, Val) VALUES (src.ID, src.Val);
-- (Optional: WHEN NOT MATCHED BY SOURCE THEN DELETE;)

Q4:
UNPIVOT rotates columns of a table-valued expression into column values.
Example:
SELECT Year, Department, Revenue 
FROM (
    SELECT Year, [IT], [HR] FROM #PivotedResult -- assuming the table above was saved
) p
UNPIVOT (
    Revenue FOR Department IN ([IT], [HR])
) AS UnpivotTable;

Q5:
MERGE can be more efficient because it only scans the source and target tables once to calculate the joins, whereas separate INSERT, UPDATE, and DELETE statements might require multiple scans. However, MERGE can have complex locking behaviors and bugs in certain SQL Server versions (optimizing MERGE can be tricky), so some DBAs prefer separate statements for highly concurrent OLTP systems.
*/

-- Cleanup
DROP TABLE #SalesData;
DROP TABLE #TargetTable;
DROP TABLE #SourceTable;
