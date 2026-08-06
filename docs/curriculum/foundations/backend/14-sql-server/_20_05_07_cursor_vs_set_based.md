---
id: "20_05_07"
title: "Cursors vs Set-Based Operations"
course: "SQL Server"
module: 5
module_title: "Programmability and Transactions"
lesson: 7
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["cursor", "fetch-next", "set-based"]
prerequisites: []
lab_required: true
---

# Cursors vs Set-Based Operations

## Overview of Cursors vs Set-Based Operations

In this lesson, you will master **Cursors vs Set-Based Operations** as part of Module 5: Programmability and Transactions in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Cursors vs Set-Based Operations
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
