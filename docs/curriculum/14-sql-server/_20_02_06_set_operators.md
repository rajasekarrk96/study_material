---
id: "20_02_06"
title: "Set Operators: UNION, UNION ALL, INTERSECT, EXCEPT"
course: "SQL Server"
module: 2
module_title: "Retrieval and Filtering"
lesson: 6
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["union", "union-all", "intersect", "except"]
prerequisites: []
lab_required: true
---

# Set Operators: UNION, UNION ALL, INTERSECT, EXCEPT

## Overview of Set Operators: UNION, UNION ALL, INTERSECT, EXCEPT

In this lesson, you will master **Set Operators: UNION, UNION ALL, INTERSECT, EXCEPT** as part of Module 2: Retrieval and Filtering in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Set Operators: UNION, UNION ALL, INTERSECT, EXCEPT
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
