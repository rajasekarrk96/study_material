# Ajax Shorthand Methods

> **Course**: Jquery | **Module**: Ajax and Data Exchange | **Difficulty**: intermediate

---

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

---

1. Load external HTML snippet content directly into a `<div>` using `$('#content').load('snippet.html')`.

---
