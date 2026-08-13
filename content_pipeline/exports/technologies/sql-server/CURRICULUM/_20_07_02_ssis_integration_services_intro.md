---
id: "20_07_02"
title: "Introduction to SSIS (SQL Server Integration Services)"
course: "SQL Server"
module: 7
module_title: "Enterprise Architecture"
lesson: 2
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["ssis", "etl", "integration-services"]
prerequisites: []
lab_required: true
---

# Introduction to SSIS (SQL Server Integration Services)

## Overview of Introduction to SSIS (SQL Server Integration Services)

In this lesson, you will master **Introduction to SSIS (SQL Server Integration Services)** as part of Module 7: Enterprise Architecture in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Introduction to SSIS (SQL Server Integration Services)
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
