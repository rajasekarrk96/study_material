---
id: "20_01_03"
title: "DML: INSERT, UPDATE, DELETE, MERGE"
course: "SQL Server"
module: 1
module_title: "Setup and TSQL Fundamentals"
lesson: 3
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["dml", "insert", "update", "delete", "merge"]
prerequisites: []
lab_required: true
---

# DML: INSERT, UPDATE, DELETE, MERGE

## Overview of DML: INSERT, UPDATE, DELETE, MERGE

In this lesson, you will master **DML: INSERT, UPDATE, DELETE, MERGE** as part of Module 1: Setup and TSQL Fundamentals in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for DML: INSERT, UPDATE, DELETE, MERGE
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
