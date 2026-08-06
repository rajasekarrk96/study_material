---
id: "20_03_01"
title: "GROUP BY and HAVING Clause"
course: "SQL Server"
module: 3
module_title: "Aggregations and Window Functions"
lesson: 1
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["group-by", "having", "sum", "avg", "count"]
prerequisites: []
lab_required: true
---

# GROUP BY and HAVING Clause

## Overview of GROUP BY and HAVING Clause

In this lesson, you will master **GROUP BY and HAVING Clause** as part of Module 3: Aggregations and Window Functions in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for GROUP BY and HAVING Clause
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
