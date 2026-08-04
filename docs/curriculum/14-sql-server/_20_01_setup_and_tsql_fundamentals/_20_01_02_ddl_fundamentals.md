---
id: "20_01_02"
title: "DDL Fundamentals: CREATE, ALTER, DROP"
course: "SQL Server"
module: 1
module_title: "Setup and TSQL Fundamentals"
lesson: 2
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["ddl", "create-table", "alter-table", "drop-table"]
prerequisites: []
lab_required: true
---

# DDL Fundamentals: CREATE, ALTER, DROP

## Overview of DDL Fundamentals: CREATE, ALTER, DROP

In this lesson, you will master **DDL Fundamentals: CREATE, ALTER, DROP** as part of Module 1: Setup and TSQL Fundamentals in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for DDL Fundamentals: CREATE, ALTER, DROP
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
