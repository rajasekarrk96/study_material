---
id: "20_06_05"
title: "Always On Availability Groups Overview"
course: "SQL Server"
module: 6
module_title: "Administration and Security"
lesson: 5
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["always-on", "ha-dr", "availability-group", "failover"]
prerequisites: []
lab_required: true
---

# Always On Availability Groups Overview

## Overview of Always On Availability Groups Overview

In this lesson, you will master **Always On Availability Groups Overview** as part of Module 6: Administration and Security in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Always On Availability Groups Overview
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
