---
id: "05_02"
title: "Database Design ER Modeling and Normalization"
course: "MySQL"
module: 1
module_title: "MySQL Foundations"
lesson: 2
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["er-diagram", "entity", "relationship", "cardinality", "1NF", "2NF", "3NF", "BCNF", "denormalization", "crow-foot"]
prerequisites: []
lab_required: true
---

## Topics Covered

### 1. Entity-Relationship Modeling
- **Entities** vs **Attributes** vs **Relationships**
- Cardinality: 1:1, 1:N, M:N
- Crow's foot notation
- Identifying vs non-identifying relationships
- Weak entities and partial keys

### 2. ER to Schema Mapping
```
Student(id PK, name, email)
Course(id PK, title, credits)
Enrollment(student_id FK, course_id FK, grade)  -- M:N resolved
```

### 3. Normal Forms
| Form | Rule | Fix |
|---|---|---|
| 1NF | No repeating groups; atomic values | Split multi-value cols |
| 2NF | No partial dependencies on composite PK | Move partial deps to new table |
| 3NF | No transitive dependencies | Remove transitive cols |
| BCNF | Every determinant is a candidate key | Decompose further |

### 4. Normalization Example
```sql
-- Unnormalized
Orders(order_id, customer_name, customer_city, product1, product2)

-- After 1NF
OrderItems(order_id, line, product)
Orders(order_id, customer_name, customer_city)

-- After 3NF
Customers(customer_id, name, city)
Orders(order_id, customer_id FK)
OrderItems(order_id FK, line, product_id FK)
```

## Lab
Design an ER diagram for a Library Management System (Books, Authors, Members, Loans) and implement it in MySQL with proper FK constraints.
