---
id: "21_02_01"
title: "Logical and Array Operators"
course: "MongoDB"
module: 2
module_title: "Advanced Querying"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["$and", "$or", "$nor", "$not", "$elemMatch", "$all", "$size"]
prerequisites: []
lab_required: true
---

# Logical and Array Operators


## Logical and Array Searching

```javascript
// Logical Operators
db.orders.find({
  $or: [
    { status: "pending" },
    { totalAmount: { $gt: 500 } }
  ]
});

// Array Operators
db.users.find({ tags: { $all: ["mongodb", "python"] } });
db.users.find({ scores: { $elemMatch: { $gte: 80, $lt: 90 } } });
```

## Lab Exercise
1. Query a blog collection for posts that contain both "Node.js" and "Express" in their tags list and have at least 10 likes.
