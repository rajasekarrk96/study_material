---
id: "20_03_05"
title: "PIVOT and UNPIVOT Operators"
course: "SQL Server"
module: 3
module_title: "Aggregations and Window Functions"
lesson: 5
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["pivot", "unpivot", "crosstab"]
prerequisites: []
lab_required: true
---

# PIVOT and UNPIVOT Operators

## Overview of PIVOT and UNPIVOT Operators

In this lesson, you will master **PIVOT and UNPIVOT Operators** as part of Module 3: Aggregations and Window Functions in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for PIVOT and UNPIVOT Operators
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
