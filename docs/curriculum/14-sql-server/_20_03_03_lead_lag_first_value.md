---
id: "20_03_03"
title: "Analytic Functions: LEAD, LAG, FIRST_VALUE"
course: "SQL Server"
module: 3
module_title: "Aggregations and Window Functions"
lesson: 3
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["lead", "lag", "first_value", "last_value"]
prerequisites: []
lab_required: true
---

# Analytic Functions: LEAD, LAG, FIRST_VALUE

## Overview of Analytic Functions: LEAD, LAG, FIRST_VALUE

In this lesson, you will master **Analytic Functions: LEAD, LAG, FIRST_VALUE** as part of Module 3: Aggregations and Window Functions in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Analytic Functions: LEAD, LAG, FIRST_VALUE
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
