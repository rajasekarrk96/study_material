---
id: "20_03_02"
title: "Window Functions: ROW_NUMBER, RANK, DENSE_RANK"
course: "SQL Server"
module: 3
module_title: "Aggregations and Window Functions"
lesson: 2
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["window-functions", "row_number", "rank", "dense_rank", "over"]
prerequisites: []
lab_required: true
---

# Window Functions: ROW_NUMBER, RANK, DENSE_RANK

## Overview of Window Functions: ROW_NUMBER, RANK, DENSE_RANK

In this lesson, you will master **Window Functions: ROW_NUMBER, RANK, DENSE_RANK** as part of Module 3: Aggregations and Window Functions in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Window Functions: ROW_NUMBER, RANK, DENSE_RANK
USE EnterpriseDB;
GO

SELECT 
    e.EmployeeID,
    e.FirstName,
    e.LastName,
    e.DepartmentID,
    e.Salary,
    AVG(e.Salary) OVER (PARTITION BY e.DepartmentID) AS DeptAvgSalary
FROM dbo.Employees AS e
WHERE e.IsActive = 1
ORDER BY e.DepartmentID, e.Salary DESC;
GO
```

## Lab Exercise
1. Execute the query above in SSMS, analyze the execution plan, and verify index usage.
