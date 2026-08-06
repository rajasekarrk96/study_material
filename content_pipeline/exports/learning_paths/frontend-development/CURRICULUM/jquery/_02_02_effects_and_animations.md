# Effects and Animations

> **Course**: Jquery | **Module**: Events and Effects | **Difficulty**: beginner

---

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

---

1. Implement a collapsible accordion panel using `.slideToggle()`.

---
