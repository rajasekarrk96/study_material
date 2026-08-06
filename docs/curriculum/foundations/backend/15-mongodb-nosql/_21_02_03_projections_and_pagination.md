---
id: "21_02_03"
title: "Projections and Pagination"
course: "MongoDB"
module: 2
module_title: "Advanced Querying"
lesson: 3
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["projection", "limit", "skip", "sort", "cursor", "pagination"]
prerequisites: []
lab_required: true
---

# Projections and Pagination


## Controlling Returned Fields & Pagination

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

## Lab Exercise
1. Write a paginated search query returning pages of 5 items sorted by newest created date.
