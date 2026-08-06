---
id: "05_05"
title: "Aggregation Grouping and Functions"
course: "MySQL"
module: 2
module_title: "SQL Fundamentals"
lesson: 5
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["COUNT", "SUM", "AVG", "MIN", "MAX", "GROUP-BY", "HAVING", "ROLLUP", "string-functions", "date-functions", "COALESCE", "NULLIF", "CASE"]
prerequisites: []
lab_required: true
---

## Topics Covered

### 1. Aggregate Functions
```sql
SELECT
    dept_id,
    COUNT(*)           AS total_employees,
    COUNT(DISTINCT job) AS unique_jobs,
    AVG(salary)        AS avg_salary,
    MIN(salary)        AS min_salary,
    MAX(salary)        AS max_salary,
    SUM(salary)        AS total_payroll
FROM employees
WHERE is_active = 1
GROUP BY dept_id
HAVING avg_salary > 50000
ORDER BY total_payroll DESC;
```

### 2. WITH ROLLUP
```sql
SELECT dept_id, job, SUM(salary)
FROM employees
GROUP BY dept_id, job WITH ROLLUP;
-- Adds subtotal rows per dept and grand total
```

### 3. String Functions
```sql
CONCAT(first_name, ' ', last_name)
SUBSTRING(email, 1, LOCATE('@', email) - 1)  -- username
UPPER(country), LOWER(email)
TRIM(LEADING '0' FROM phone)
LENGTH(description)
REPLACE(text, 'old', 'new')
FORMAT(salary, 2)                             -- 55,000.00
```

### 4. Date Functions
```sql
NOW(), CURDATE(), CURTIME()
DATE_FORMAT(hire_date, '%d %M %Y')           -- 15 July 2023
DATEDIFF(CURDATE(), hire_date)               -- days since hire
DATE_ADD(order_date, INTERVAL 30 DAY)        -- due date
YEAR(hire_date), MONTH(hire_date), DAY(hire_date)
```

### 5. CASE Expression
```sql
SELECT name, salary,
    CASE
        WHEN salary < 30000 THEN 'Junior'
        WHEN salary < 60000 THEN 'Mid'
        ELSE 'Senior'
    END AS grade
FROM employees;
```

## Lab
Write queries to: monthly sales totals with ROLLUP, format customer names, calculate age from DOB, grade products by price bracket.
