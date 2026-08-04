# GROUPING SETS, ROLLUP, and CUBE

> **Course**: Sql Server | **Module**: Aggregations and Window Functions | **Difficulty**: advanced

---

In this lesson, you will master **GROUPING SETS, ROLLUP, and CUBE** as part of Module 3: Aggregations and Window Functions in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for GROUPING SETS, ROLLUP, and CUBE
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
