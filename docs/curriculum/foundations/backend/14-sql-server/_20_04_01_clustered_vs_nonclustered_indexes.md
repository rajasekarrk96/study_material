---
id: "20_04_01"
title: "Clustered vs Nonclustered Indexes"
course: "SQL Server"
module: 4
module_title: "Indexes and Optimization"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["indexes", "clustered-index", "nonclustered-index", "b-tree"]
prerequisites: []
lab_required: true
---

# Clustered vs Nonclustered Indexes

## Overview of Clustered vs Nonclustered Indexes

In this lesson, you will master **Clustered vs Nonclustered Indexes** as part of Module 4: Indexes and Optimization in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Clustered vs Nonclustered Indexes
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
