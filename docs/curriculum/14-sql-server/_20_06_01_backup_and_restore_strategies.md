---
id: "20_06_01"
title: "Backup and Restore Strategies"
course: "SQL Server"
module: 6
module_title: "Administration and Security"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["backup", "full-backup", "diff-backup", "log-backup", "restore"]
prerequisites: []
lab_required: true
---

# Backup and Restore Strategies

## Overview of Backup and Restore Strategies

In this lesson, you will master **Backup and Restore Strategies** as part of Module 6: Administration and Security in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Backup and Restore Strategies
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
