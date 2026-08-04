---
id: "20_07_01"
title: "Capstone Enterprise Database Architecture"
course: "SQL Server"
module: 7
module_title: "Enterprise Architecture"
lesson: 1
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["capstone", "enterprise-db", "tsql-project", "schema-design"]
prerequisites: []
lab_required: true
---

# Capstone Enterprise Database Architecture

## Overview of Capstone Enterprise Database Architecture

In this lesson, you will master **Capstone Enterprise Database Architecture** as part of Module 7: Enterprise Architecture in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Capstone Enterprise Database Architecture
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
