# Update Operators

> **Course**: Mongodb | **Module**: Advanced Querying | **Difficulty**: intermediate

---

```javascript
// Increment & Field Modification
db.users.updateOne(
  { _id: ObjectId("...") },
  { 
    $inc: { loginCount: 1 },
    $set: { lastLogin: new Date() }
  }
);

// Array Push & Pull
db.users.updateOne(
  { name: "Alice" },
  { $addToSet: { roles: "manager" } } // prevents duplicates
);
```

---

1. Append a new comment object to an article's `comments` array field using `$push`.

---
