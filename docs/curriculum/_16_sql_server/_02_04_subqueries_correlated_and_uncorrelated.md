# Subqueries: Correlated and Uncorrelated

> **Course**: Sql Server | **Module**: Retrieval and Filtering | **Difficulty**: intermediate

---

In this lesson, you will master **Subqueries: Correlated and Uncorrelated** as part of Module 2: Retrieval and Filtering in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Subqueries: Correlated and Uncorrelated
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
