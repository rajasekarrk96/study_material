---
id: "20_05_04"
title: "Transactions and Isolation Levels"
course: "SQL Server"
module: 5
module_title: "Programmability and Transactions"
lesson: 4
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["transactions", "begin-tran", "commit", "isolation-level", "deadlocks"]
prerequisites: []
lab_required: true
---

# Transactions and Isolation Levels

## Overview of Transactions and Isolation Levels

In this lesson, you will master **Transactions and Isolation Levels** as part of Module 5: Programmability and Transactions in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Transactions and Isolation Levels
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
