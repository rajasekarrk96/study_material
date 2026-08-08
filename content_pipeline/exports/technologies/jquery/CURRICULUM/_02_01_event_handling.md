# Event Handling

> **Course**: Jquery | **Module**: Events and Effects | **Difficulty**: beginner

---

```javascript
// Basic Event Listeners
$('#btn').on('click', function(e) {
  e.preventDefault();
  alert('Button clicked!');
});

// Event Delegation (for dynamically added elements)
$('#todo-list').on('click', 'li', function() {
  $(this).toggleClass('completed');
});
```

---

1. Create a To-Do list application utilizing event delegation so newly added tasks can be clicked to toggle completion.

---
