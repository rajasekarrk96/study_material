# Transactions and ACID

> **Course**: Mongodb | **Module**: Data Modeling and Administration | **Difficulty**: advanced

---

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

---

1. Implement a balance transfer script between two accounts wrapped in a session transaction.

---
