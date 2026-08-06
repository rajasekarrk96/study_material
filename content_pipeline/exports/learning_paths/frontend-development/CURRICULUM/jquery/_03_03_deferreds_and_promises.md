# Deferreds and Promises

> **Course**: Jquery | **Module**: Ajax and Data Exchange | **Difficulty**: advanced

---

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

---

1. Execute 2 simultaneous API calls using `$.when()` and update the UI only when both responses return successfully.

---
