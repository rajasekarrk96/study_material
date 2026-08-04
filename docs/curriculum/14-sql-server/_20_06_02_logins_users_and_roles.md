---
id: "20_06_02"
title: "Logins, Users, Roles, and Permissions"
course: "SQL Server"
module: 6
module_title: "Administration and Security"
lesson: 2
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["security", "logins", "users", "roles", "grant", "deny"]
prerequisites: []
lab_required: true
---

# Logins, Users, Roles, and Permissions

## Overview of Logins, Users, Roles, and Permissions

In this lesson, you will master **Logins, Users, Roles, and Permissions** as part of Module 6: Administration and Security in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Logins, Users, Roles, and Permissions
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
