---
id: "20_04_05"
title: "Columnstore Indexes for Data Warehousing"
course: "SQL Server"
module: 4
module_title: "Indexes and Optimization"
lesson: 5
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["columnstore", "dw", "data-warehouse", "batch-mode"]
prerequisites: []
lab_required: true
---

# Columnstore Indexes for Data Warehousing

## Overview of Columnstore Indexes for Data Warehousing

In this lesson, you will master **Columnstore Indexes for Data Warehousing** as part of Module 4: Indexes and Optimization in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Columnstore Indexes for Data Warehousing
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
