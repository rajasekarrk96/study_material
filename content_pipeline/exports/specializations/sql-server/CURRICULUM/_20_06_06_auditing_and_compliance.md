---
id: "20_06_06"
title: "Auditing and Compliance Features"
course: "SQL Server"
module: 6
module_title: "Administration and Security"
lesson: 6
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["auditing", "cdc", "temporal-tables"]
prerequisites: []
lab_required: true
---

# Auditing and Compliance Features

## Overview of Auditing and Compliance Features

In this lesson, you will master **Auditing and Compliance Features** as part of Module 6: Administration and Security in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Auditing and Compliance Features
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
