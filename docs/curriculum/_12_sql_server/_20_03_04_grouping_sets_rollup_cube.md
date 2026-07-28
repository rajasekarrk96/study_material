---
id: "20_03_04"
title: "GROUPING SETS, ROLLUP, and CUBE"
course: "SQL Server"
module: 3
module_title: "Aggregations and Window Functions"
lesson: 4
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["grouping-sets", "rollup", "cube"]
prerequisites: []
lab_required: true
---

# GROUPING SETS, ROLLUP, and CUBE

## Overview of GROUPING SETS, ROLLUP, and CUBE

In this lesson, you will master **GROUPING SETS, ROLLUP, and CUBE** as part of Module 3: Aggregations and Window Functions in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for GROUPING SETS, ROLLUP, and CUBE
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
