# Introduction to SSIS (SQL Server Integration Services)

> **Course**: Sql Server | **Module**: Enterprise Architecture | **Difficulty**: intermediate

---

In this lesson, you will master **Introduction to SSIS (SQL Server Integration Services)** as part of Module 7: Enterprise Architecture in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Introduction to SSIS (SQL Server Integration Services)
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
