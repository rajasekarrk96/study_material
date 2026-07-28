---
id: "19_02_03"
title: "Custom Animation Queues"
course: "jQuery"
module: 2
module_title: "Events and Effects"
lesson: 3
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["queue", "dequeue", "stop", "finish", "delay", "chaining"]
prerequisites: []
lab_required: true
---

# Custom Animation Queues


## Animation Queue Control

```javascript
$('#box')
  .slideDown(500)
  .delay(1000)
  .animate({ width: '300px' }, 500)
  .fadeOut(500);

// Stop running animations immediately
$('#box').stop(true, true);
```

## Lab Exercise
1. Create a multi-stage notification banner animation that slides down, pauses, turns green, and fades out.
