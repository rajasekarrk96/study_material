---
id: "20_04_04"
title: "Statistics, Index Maintenance, and Fragmentation"
course: "SQL Server"
module: 4
module_title: "Indexes and Optimization"
lesson: 4
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["statistics", "fragmentation", "rebuild-index"]
prerequisites: []
lab_required: true
---

# Statistics, Index Maintenance, and Fragmentation

## Overview of Statistics, Index Maintenance, and Fragmentation

In this lesson, you will master **Statistics, Index Maintenance, and Fragmentation** as part of Module 4: Indexes and Optimization in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Statistics, Index Maintenance, and Fragmentation
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
