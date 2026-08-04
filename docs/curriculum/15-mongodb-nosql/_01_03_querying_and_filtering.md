# Querying and Filtering

> **Course**: Mongodb | **Module**: Core Concepts and CRUD | **Difficulty**: beginner

---

```javascript
// Greater than / Less than
db.products.find({ price: { $gt: 20, $lte: 100 } });

// In Array
db.users.find({ role: { $in: ["admin", "editor"] } });

// Not Equal
db.products.find({ category: { $ne: "Electronics" } });
```

---

1. Find all employees with salaries between 50,000 and 90,000 who belong to IT or Finance departments.

---
