---
id: "19_03_03"
title: "Deferreds and Promises"
course: "jQuery"
module: 3
module_title: "Ajax and Data Exchange"
lesson: 3
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["$.Deferred", "then", "done", "fail", "always", "$.when"]
prerequisites: []
lab_required: true
---

# Deferreds and Promises


## Deferreds & Promises

```javascript
$.when(
  $.get('/api/users'),
  $.get('/api/posts')
).done(function(userRes, postRes) {
  console.log('Both requests completed successfully!');
}).fail(function() {
  console.error('One or more requests failed.');
});
```

## Lab Exercise
1. Execute 2 simultaneous API calls using `$.when()` and update the UI only when both responses return successfully.
