---
id: "20_02_03"
title: "JOINS: INNER, LEFT, RIGHT, FULL, CROSS"
course: "SQL Server"
module: 2
module_title: "Retrieval and Filtering"
lesson: 3
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["joins", "inner-join", "left-join", "cross-join"]
prerequisites: []
lab_required: true
---

# JOINS: INNER, LEFT, RIGHT, FULL, CROSS

## Overview of JOINS: INNER, LEFT, RIGHT, FULL, CROSS

In this lesson, you will master **JOINS: INNER, LEFT, RIGHT, FULL, CROSS** as part of Module 2: Retrieval and Filtering in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for JOINS: INNER, LEFT, RIGHT, FULL, CROSS
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
