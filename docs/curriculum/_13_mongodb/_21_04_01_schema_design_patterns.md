---
id: "21_04_01"
title: "Schema Design Patterns"
course: "MongoDB"
module: 4
module_title: "Data Modeling and Administration"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["schema-design", "embedding", "referencing", "one-to-many", "denormalization"]
prerequisites: []
lab_required: true
---

# Schema Design Patterns


## Embedding vs Referencing

- **Embedding (1-to-few)**: Great for low-cardinality related data read together.
- **Referencing (1-to-many / 1-to-squillions)**: Best for unbounded arrays or frequently updated shared data.

```javascript
// Embedded Pattern Example (User Profile)
{
  "_id": 1,
  "name": "Raja",
  "address": {
    "street": "123 Main St",
    "city": "Chennai",
    "zip": "600001"
  }
}
```

## Lab Exercise
1. Model an e-commerce database schema balancing embedded order line items and referenced customer accounts.
