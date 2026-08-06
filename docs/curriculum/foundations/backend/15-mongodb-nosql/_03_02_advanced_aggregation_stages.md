# Advanced Aggregation Stages

> **Course**: Mongodb | **Module**: Aggregation Framework | **Difficulty**: advanced

---

```javascript
// $lookup (Left Outer Join)
db.orders.aggregate([
  {
    $lookup: {
      from: "users",
      localField: "userId",
      foreignField: "_id",
      as: "userDetails"
    }
  },
  { $unwind: "$userDetails" } // Deconstructs array
]);
```

---

1. Perform a `$lookup` joining `orders` with `products` to calculate order item names and prices.

---
