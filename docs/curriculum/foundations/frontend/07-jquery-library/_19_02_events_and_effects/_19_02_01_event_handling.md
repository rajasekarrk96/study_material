---
id: "19_02_01"
title: "Event Handling"
course: "jQuery"
module: 2
module_title: "Events and Effects"
lesson: 1
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["on", "click", "hover", "submit", "keyup", "event-delegation"]
prerequisites: []
lab_required: true
---

# Event Handling


## Event Listeners in jQuery

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

## Lab Exercise
1. Create a To-Do list application utilizing event delegation so newly added tasks can be clicked to toggle completion.
