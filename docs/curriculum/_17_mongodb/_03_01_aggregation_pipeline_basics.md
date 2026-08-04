# Aggregation Pipeline Basics

> **Course**: Mongodb | **Module**: Aggregation Framework | **Difficulty**: intermediate

---

The aggregation framework processes documents through multi-stage pipelines.

```javascript
db.orders.aggregate([
  // Stage 1: Filter
  { $match: { status: "completed" } },
  // Stage 2: Group & Calculate
  {
    $group: {
      _id: "$customerId",
      totalSpent: { $sum: "$total" },
      avgOrderSize: { $avg: "$quantity" }
    }
  },
  // Stage 3: Sort
  { $sort: { totalSpent: -1 } }
]);
```

---

1. Aggregate sales records by category to calculate total revenue and total units sold.

---
