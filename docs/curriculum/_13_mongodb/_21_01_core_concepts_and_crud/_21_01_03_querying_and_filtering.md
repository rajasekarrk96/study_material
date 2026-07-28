---
id: "21_01_03"
title: "Querying and Filtering"
course: "MongoDB"
module: 1
module_title: "Core Concepts and CRUD"
lesson: 3
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["$eq", "$gt", "$gte", "$lt", "$lte", "$in", "$nin", "comparison"]
prerequisites: []
lab_required: true
---

# Querying and Filtering


## Comparison Query Operators

```javascript
// Greater than / Less than
db.products.find({ price: { $gt: 20, $lte: 100 } });

// In Array
db.users.find({ role: { $in: ["admin", "editor"] } });

// Not Equal
db.products.find({ category: { $ne: "Electronics" } });
```

## Lab Exercise
1. Find all employees with salaries between 50,000 and 90,000 who belong to IT or Finance departments.
