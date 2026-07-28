---
id: "21_04_02"
title: "Transactions and ACID"
course: "MongoDB"
module: 4
module_title: "Data Modeling and Administration"
lesson: 2
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["transactions", "session", "acid", "commitTransaction", "abortTransaction", "replica-set"]
prerequisites: []
lab_required: true
---

# Transactions and ACID


## Multi-Document ACID Transactions

```javascript
const session = db.getMongo().startSession();
session.startTransaction();

try {
  const coll1 = session.getDatabase("bank").getCollection("accounts");
  coll1.updateOne({ _id: 1 }, { $inc: { balance: -100 } });
  coll1.updateOne({ _id: 2 }, { $inc: { balance: 100 } });
  
  session.commitTransaction();
  console.log("Transaction committed!");
} catch (error) {
  session.abortTransaction();
  console.error("Transaction aborted due to error:", error);
} finally {
  session.endSession();
}
```

## Lab Exercise
1. Implement a balance transfer script between two accounts wrapped in a session transaction.
