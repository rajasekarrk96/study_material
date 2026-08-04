# DML: INSERT, UPDATE, DELETE, MERGE

> **Course**: Sql Server | **Module**: Setup and TSQL Fundamentals | **Difficulty**: beginner

---

In this lesson, you will master **DML: INSERT, UPDATE, DELETE, MERGE** as part of Module 1: Setup and TSQL Fundamentals in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for DML: INSERT, UPDATE, DELETE, MERGE
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
