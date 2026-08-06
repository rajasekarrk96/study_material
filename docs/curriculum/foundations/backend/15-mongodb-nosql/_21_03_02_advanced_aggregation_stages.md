---
id: "21_03_02"
title: "Advanced Aggregation Stages"
course: "MongoDB"
module: 3
module_title: "Aggregation Framework"
lesson: 2
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["$unwind", "$lookup", "$facet", "$bucket", "joins"]
prerequisites: []
lab_required: true
---

# Advanced Aggregation Stages


## Joins and Deconstruction

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

## Lab Exercise
1. Perform a `$lookup` joining `orders` with `products` to calculate order item names and prices.
