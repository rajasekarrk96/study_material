---
id: "19_03_01"
title: "Ajax Fundamentals"
course: "jQuery"
module: 3
module_title: "Ajax and Data Exchange"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["ajax", "$.get", "$.post", "json", "xhr"]
prerequisites: []
lab_required: true
---

# Ajax Fundamentals


## Asynchronous Requests with $.ajax

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

## Lab Exercise
1. Fetch a random user profile from an open REST API using `$.ajax()` and render their info into a card container.
