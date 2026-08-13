# SQL Server Agent and Job Scheduling

> **Course**: Sql Server | **Module**: Administration and Security | **Difficulty**: intermediate

---

In this lesson, you will master **SQL Server Agent and Job Scheduling** as part of Module 6: Administration and Security in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for SQL Server Agent and Job Scheduling
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
