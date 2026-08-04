# Basic CRUD Operations

> **Course**: Mongodb | **Module**: Core Concepts and CRUD | **Difficulty**: beginner

---

```javascript
// CREATE
db.users.insertOne({ name: "Alice", role: "admin", score: 95 });
db.users.insertMany([
  { name: "Bob", role: "user", score: 80 },
  { name: "Charlie", role: "user", score: 88 }
]);

// READ
db.users.find({ role: "user" });
db.users.findOne({ name: "Alice" });

// UPDATE
db.users.updateOne(
  { name: "Bob" },
  { $set: { score: 85 } }
);

// DELETE
db.users.deleteOne({ name: "Charlie" });
```

---

1. Insert 5 product records into a `products` collection, query all products under $50, and update the stock count of one product.

---
