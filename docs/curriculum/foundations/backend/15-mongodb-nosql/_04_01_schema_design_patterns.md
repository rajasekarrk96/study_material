# Schema Design Patterns

> **Course**: Mongodb | **Module**: Data Modeling and Administration | **Difficulty**: intermediate

---

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

---

1. Model an e-commerce database schema balancing embedded order line items and referenced customer accounts.

---
