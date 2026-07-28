---
id: "21_03_03"
title: "Indexes and Performance"
course: "MongoDB"
module: 3
module_title: "Aggregation Framework"
lesson: 3
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["index", "createIndex", "explain", "single-field", "compound-index", "text-index"]
prerequisites: []
lab_required: true
---

# Indexes and Performance


## Indexing for Query Performance

```javascript
// Single Field Index
db.users.createIndex({ email: 1 }, { unique: true });

// Compound Index
db.orders.createIndex({ customerId: 1, orderDate: -1 });

// Query Execution Plan Check
db.users.find({ email: "user@test.com" }).explain("executionStats");
```

## Lab Exercise
1. Create a compound index on `{ category: 1, price: -1 }` and verify index usage using `.explain()`.
