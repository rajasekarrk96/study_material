---
id: "20_05_02"
title: "User-Defined Functions (Scalar and Table-Valued)"
course: "SQL Server"
module: 5
module_title: "Programmability and Transactions"
lesson: 2
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["udf", "scalar-function", "table-valued-function"]
prerequisites: []
lab_required: true
---

# User-Defined Functions (Scalar and Table-Valued)

## Overview of User-Defined Functions (Scalar and Table-Valued)

In this lesson, you will master **User-Defined Functions (Scalar and Table-Valued)** as part of Module 5: Programmability and Transactions in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for User-Defined Functions (Scalar and Table-Valued)
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
