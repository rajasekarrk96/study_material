---
id: "20_05_03"
title: "Triggers: AFTER and INSTEAD OF"
course: "SQL Server"
module: 5
module_title: "Programmability and Transactions"
lesson: 3
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["triggers", "after-trigger", "instead-of-trigger", "inserted", "deleted"]
prerequisites: []
lab_required: true
---

# Triggers: AFTER and INSTEAD OF

## Overview of Triggers: AFTER and INSTEAD OF

In this lesson, you will master **Triggers: AFTER and INSTEAD OF** as part of Module 5: Programmability and Transactions in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Triggers: AFTER and INSTEAD OF
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
