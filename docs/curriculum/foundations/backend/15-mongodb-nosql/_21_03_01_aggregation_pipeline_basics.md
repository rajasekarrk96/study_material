---
id: "21_03_01"
title: "Aggregation Pipeline Basics"
course: "MongoDB"
module: 3
module_title: "Aggregation Framework"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["aggregation", "$match", "$project", "$group", "$sort", "$limit"]
prerequisites: []
lab_required: true
---

# Aggregation Pipeline Basics


## Introduction to Aggregation

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

## Lab Exercise
1. Aggregate sales records by category to calculate total revenue and total units sold.
