---
id: "19_03_02"
title: "Ajax Shorthand Methods"
course: "jQuery"
module: 3
module_title: "Ajax and Data Exchange"
lesson: 2
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["get", "post", "getJSON", "load"]
prerequisites: []
lab_required: true
---

# Ajax Shorthand Methods


## Shorthand AJAX Helper Functions

```javascript
// $.get()
$.get('/api/users', function(users) {
  console.log(users);
});

// $.post()
$.post('/api/users', { name: 'Raja', age: 28 }, function(response) {
  console.log('User created:', response);
});

// $.getJSON()
$.getJSON('/api/data.json', function(data) {
  // process JSON directly
});
```

## Lab Exercise
1. Load external HTML snippet content directly into a `<div>` using `$('#content').load('snippet.html')`.
