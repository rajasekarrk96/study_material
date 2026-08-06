---
id: "20_05_01"
title: "Stored Procedures and Parameters"
course: "SQL Server"
module: 5
module_title: "Programmability and Transactions"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["stored-procedure", "parameters", "output-params"]
prerequisites: []
lab_required: true
---

# Stored Procedures and Parameters

## Overview of Stored Procedures and Parameters

In this lesson, you will master **Stored Procedures and Parameters** as part of Module 5: Programmability and Transactions in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Stored Procedures and Parameters
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
