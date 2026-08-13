# Cursors vs Set-Based Operations

> **Course**: Sql Server | **Module**: Programmability and Transactions | **Difficulty**: intermediate

---

In this lesson, you will master **Cursors vs Set-Based Operations** as part of Module 5: Programmability and Transactions in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Cursors vs Set-Based Operations
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
