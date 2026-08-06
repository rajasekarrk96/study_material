# DOM Traversal and Manipulation

> **Course**: Jquery | **Module**: Core and DOM Selection | **Difficulty**: intermediate

---

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

---

1. Build a dynamic list builder where users type text into an input and click a button to append `<li>` elements.

---
