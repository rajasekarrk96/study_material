# Logins, Users, Roles, and Permissions

> **Course**: Sql Server | **Module**: Administration and Security | **Difficulty**: intermediate

---

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

---

1. Execute the query above in SSMS, analyze the execution plan, and verify index usage.

---
