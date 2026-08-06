---
id: "20_05_06"
title: "Dynamic SQL and sp_executesql"
course: "SQL Server"
module: 5
module_title: "Programmability and Transactions"
lesson: 6
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["dynamic-sql", "sp_executesql", "sql-injection"]
prerequisites: []
lab_required: true
---

# Dynamic SQL and sp_executesql

## Overview of Dynamic SQL and sp_executesql

In this lesson, you will master **Dynamic SQL and sp_executesql** as part of Module 5: Programmability and Transactions in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Dynamic SQL and sp_executesql
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
