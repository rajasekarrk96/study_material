---
id: "20_02_05"
title: "Common Table Expressions (CTEs)"
course: "SQL Server"
module: 2
module_title: "Retrieval and Filtering"
lesson: 5
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["cte", "with-clause", "recursive-cte"]
prerequisites: []
lab_required: true
---

# Common Table Expressions (CTEs)

## Overview of Common Table Expressions (CTEs)

In this lesson, you will master **Common Table Expressions (CTEs)** as part of Module 2: Retrieval and Filtering in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Common Table Expressions (CTEs)
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
