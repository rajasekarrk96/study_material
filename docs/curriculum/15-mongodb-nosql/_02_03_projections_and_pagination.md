# Projections and Pagination

> **Course**: Mongodb | **Module**: Advanced Querying | **Difficulty**: intermediate

---

```javascript
// Projection (1 = include, 0 = exclude)
db.users.find(
  { active: true },
  { name: 1, email: 1, _id: 0 }
);

// Sorting and Paging (Page 2, 10 per page)
db.products.find()
  .sort({ price: -1 }) // 1 = ASC, -1 = DESC
  .skip(10)
  .limit(10);
```

---

1. Write a paginated search query returning pages of 5 items sorted by newest created date.

---
