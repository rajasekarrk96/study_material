---
id: "20_01_05"
title: "Built-in System Functions (Date, String, Math)"
course: "SQL Server"
module: 1
module_title: "Setup and TSQL Fundamentals"
lesson: 5
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["functions", "getdate", "string_split", "cast", "convert"]
prerequisites: []
lab_required: true
---

# Built-in System Functions (Date, String, Math)

## Overview of Built-in System Functions (Date, String, Math)

In this lesson, you will master **Built-in System Functions (Date, String, Math)** as part of Module 1: Setup and TSQL Fundamentals in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Built-in System Functions (Date, String, Math)
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
