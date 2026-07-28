---
id: "21_01_02"
title: "Basic CRUD Operations"
course: "MongoDB"
module: 1
module_title: "Core Concepts and CRUD"
lesson: 2
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["insertOne", "insertMany", "find", "updateOne", "deleteOne", "crud"]
prerequisites: []
lab_required: true
---

# Basic CRUD Operations


## Fundamentals of CRUD in MongoDB

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

## Lab Exercise
1. Insert 5 product records into a `products` collection, query all products under $50, and update the stock count of one product.
