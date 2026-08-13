# Error Handling with TRY...CATCH

> **Course**: Sql Server | **Module**: Programmability and Transactions | **Difficulty**: intermediate

---

In this lesson, you will master **Error Handling with TRY...CATCH** as part of Module 5: Programmability and Transactions in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for Error Handling with TRY...CATCH
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
