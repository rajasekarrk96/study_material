---
id: "20_01_01"
title: "SQL Server Setup and SSMS"
course: "SQL Server"
module: 1
module_title: "Setup and TSQL Fundamentals"
lesson: 1
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["sql-server", "ssms", "setup", "express", "developer"]
prerequisites: []
lab_required: true
---

# SQL Server Setup and SSMS

## Overview of SQL Server Setup and SSMS

In this lesson, you will master **SQL Server Setup and SSMS** as part of Module 1: Setup and TSQL Fundamentals in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for SQL Server Setup and SSMS
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
