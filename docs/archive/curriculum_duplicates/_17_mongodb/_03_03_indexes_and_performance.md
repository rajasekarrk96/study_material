# Indexes and Performance

> **Course**: Mongodb | **Module**: Aggregation Framework | **Difficulty**: advanced

---

```javascript
// Single Field Index
db.users.createIndex({ email: 1 }, { unique: true });

// Compound Index
db.orders.createIndex({ customerId: 1, orderDate: -1 });

// Query Execution Plan Check
db.users.find({ email: "user@test.com" }).explain("executionStats");
```

---

1. Create a compound index on `{ category: 1, price: -1 }` and verify index usage using `.explain()`.

---
