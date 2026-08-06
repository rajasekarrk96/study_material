---
id: "19_02_02"
title: "Effects and Animations"
course: "jQuery"
module: 2
module_title: "Events and Effects"
lesson: 2
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["fadeIn", "fadeOut", "slideDown", "slideUp", "animate", "toggle"]
prerequisites: []
lab_required: true
---

# Effects and Animations


## Built-in Animation Effects

```javascript
// Fading
$('#box').fadeIn(400);
$('#box').fadeOut('slow');

// Sliding
$('#panel').slideDown();
$('#panel').slideUp();
$('#panel').slideToggle();

// Custom Animations
$('#box').animate({
  left: '250px',
  opacity: '0.5',
  height: '150px'
}, 1000);
```

## Lab Exercise
1. Implement a collapsible accordion panel using `.slideToggle()`.
