# Logical and Array Operators

> **Course**: Mongodb | **Module**: Advanced Querying | **Difficulty**: intermediate

---

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

---

1. Query a blog collection for posts that contain both "Node.js" and "Express" in their tags list and have at least 10 likes.

---
