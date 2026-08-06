---
id: "20_02_02"
title: "Sorting and Paging (OFFSET-FETCH)"
course: "SQL Server"
module: 2
module_title: "Retrieval and Filtering"
lesson: 2
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["order-by", "offset-fetch", "paging"]
prerequisites: []
lab_required: true
---

# Sorting and Paging (OFFSET-FETCH)

## Overview of Sorting and Paging (OFFSET-FETCH)

In this lesson, you will master **Sorting and Paging (OFFSET-FETCH)** as part of Module 2: Retrieval and Filtering in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Sorting and Paging (OFFSET-FETCH)
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
