# Set Operators: UNION, UNION ALL, INTERSECT, EXCEPT

> **Course**: Sql Server | **Module**: Retrieval and Filtering | **Difficulty**: beginner

---

In this lesson, you will master **Set Operators: UNION, UNION ALL, INTERSECT, EXCEPT** as part of Module 2: Retrieval and Filtering in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Set Operators: UNION, UNION ALL, INTERSECT, EXCEPT
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
