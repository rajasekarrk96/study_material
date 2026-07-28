---
id: "19_01_04"
title: "DOM Traversal and Manipulation"
course: "jQuery"
module: 1
module_title: "Core and DOM Selection"
lesson: 4
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["parent", "children", "find", "siblings", "append", "prepend", "html", "text", "attr", "val"]
prerequisites: []
lab_required: true
---

# DOM Traversal and Manipulation


## Traversal & Content Manipulation

```javascript
// Traversal
$('#child').parent();
$('.item').siblings();
$('#menu').find('.active');

// Content Manipulation
$('#output').text('Plain Text');
$('#container').html('<strong>HTML Content</strong>');
$('input#username').val('john_doe');

// Insertion
$('#list').append('<li>Last Item</li>');
$('#list').prepend('<li>First Item</li>');
```

## Lab Exercise
1. Build a dynamic list builder where users type text into an input and click a button to append `<li>` elements.
