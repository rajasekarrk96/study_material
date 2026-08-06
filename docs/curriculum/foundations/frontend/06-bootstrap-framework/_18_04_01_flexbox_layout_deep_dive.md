---
id: "18_04_01"
title: "Flexbox Layout Deep Dive"
course: "Bootstrap"
module: 4
module_title: "Advanced Layout and Customization"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["flexbox", "align-self", "order", "flex-grow", "flex-shrink"]
prerequisites: []
lab_required: true
---

# Flexbox Layout Deep Dive


## Deep Dive into Flexbox Helpers

```html
<!-- Reordering Elements Across Breakpoints -->
<div class="d-flex flex-column flex-md-row">
  <div class="order-2 order-md-1">Column 1 (Appears 2nd on mobile, 1st on desktop)</div>
  <div class="order-1 order-md-2">Column 2 (Appears 1st on mobile, 2nd on desktop)</div>
</div>
```

## Lab Exercise
1. Build a responsive media object layout with image order flipping on mobile.
