---
id: "20_05_05"
title: "Error Handling with TRY...CATCH"
course: "SQL Server"
module: 5
module_title: "Programmability and Transactions"
lesson: 5
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["try-catch", "raiserror", "throw", "error_message"]
prerequisites: []
lab_required: true
---

# Error Handling with TRY...CATCH

## Overview of Error Handling with TRY...CATCH

In this lesson, you will master **Error Handling with TRY...CATCH** as part of Module 5: Programmability and Transactions in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Error Handling with TRY...CATCH
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
