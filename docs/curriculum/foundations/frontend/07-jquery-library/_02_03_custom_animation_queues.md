# Custom Animation Queues

> **Course**: Jquery | **Module**: Events and Effects | **Difficulty**: intermediate

---

```javascript
$('#box')
  .slideDown(500)
  .delay(1000)
  .animate({ width: '300px' }, 500)
  .fadeOut(500);

// Stop running animations immediately
$('#box').stop(true, true);
```

---

1. Create a multi-stage notification banner animation that slides down, pauses, turns green, and fades out.

---
