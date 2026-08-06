---
id: "19_01_01"
title: "jQuery Setup and Core"
course: "jQuery"
module: 1
module_title: "Core and DOM Selection"
lesson: 1
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["jquery", "setup", "cdn", "ready", "dollar-sign"]
prerequisites: []
lab_required: true
---

# jQuery Setup and Core


## What is jQuery?

jQuery is a fast, small, and feature-rich JavaScript library. It makes HTML document traversal, event handling, animation, and Ajax much simpler with an easy-to-use API that works across a multitude of browsers.

```html
<!-- CDN Import -->
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<script>
  $(document).ready(function() {
    console.log("DOM fully loaded and ready!");
  });
  
  // Shorthand:
  $(function() {
    $('#title').text("Updated with jQuery!");
  });
</script>
```

## Lab Exercise
1. Add jQuery via CDN to a basic HTML page and log a success message when the DOM is ready.
