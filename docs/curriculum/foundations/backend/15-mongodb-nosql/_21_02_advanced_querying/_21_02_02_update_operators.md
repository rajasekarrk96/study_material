---
id: "21_02_02"
title: "Update Operators"
course: "MongoDB"
module: 2
module_title: "Advanced Querying"
lesson: 2
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["$set", "$unset", "$inc", "$push", "$pull", "$addToSet"]
prerequisites: []
lab_required: true
---

# Update Operators


## Modifying Documents with Update Operators

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

## Lab Exercise
1. Append a new comment object to an article's `comments` array field using `$push`.
