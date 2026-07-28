---
id: "20_04_03"
title: "Execution Plans and Query Tuning"
course: "SQL Server"
module: 4
module_title: "Indexes and Optimization"
lesson: 3
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["execution-plan", "seek-vs-scan", "index-tuning"]
prerequisites: []
lab_required: true
---

# Execution Plans and Query Tuning

## Overview of Execution Plans and Query Tuning

In this lesson, you will master **Execution Plans and Query Tuning** as part of Module 4: Indexes and Optimization in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Execution Plans and Query Tuning
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
