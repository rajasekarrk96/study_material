# Ajax Fundamentals

> **Course**: Jquery | **Module**: Ajax and Data Exchange | **Difficulty**: intermediate

---

```javascript
$.ajax({
  url: 'https://jsonplaceholder.typicode.com/posts/1',
  method: 'GET',
  dataType: 'json',
  success: function(data) {
    console.log(data);
    $('#title').text(data.title);
  },
  error: function(xhr, status, error) {
    console.error('Request failed:', error);
  }
});
```

---

1. Fetch a random user profile from an open REST API using `$.ajax()` and render their info into a card container.

---
