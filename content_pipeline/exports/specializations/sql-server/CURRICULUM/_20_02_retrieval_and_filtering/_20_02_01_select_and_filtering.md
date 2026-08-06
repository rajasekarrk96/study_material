---
id: "20_02_01"
title: "SELECT and Filtering with WHERE"
course: "SQL Server"
module: 2
module_title: "Retrieval and Filtering"
lesson: 1
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["select", "where", "like", "in", "between"]
prerequisites: []
lab_required: true
---

# SELECT and Filtering with WHERE

## Overview of SELECT and Filtering with WHERE

In this lesson, you will master **SELECT and Filtering with WHERE** as part of Module 2: Retrieval and Filtering in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for SELECT and Filtering with WHERE
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
