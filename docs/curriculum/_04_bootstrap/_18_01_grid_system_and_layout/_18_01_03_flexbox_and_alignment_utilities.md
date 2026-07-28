---
id: "18_01_03"
title: "Flexbox and Alignment Utilities"
course: "Bootstrap"
module: 1
module_title: "Grid System and Layout"
lesson: 3
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["flex", "justify-content", "align-items", "flex-grow", "flex-wrap", "gap"]
prerequisites: []
lab_required: true
---

# Flexbox and Alignment Utilities


## Flexbox Utility Classes

Manage layout, alignment, and sizing of grid columns, navigation components, and custom boxes using built-in flex utilities.

```html
<!-- Justify Content (Main Axis) -->
<div class="d-flex justify-content-between align-items-center bg-light p-3">
  <div>Logo</div>
  <div>Navigation Links</div>
</div>

<!-- Flex Direction & Gap -->
<div class="d-flex flex-column flex-md-row gap-3">
  <button class="btn btn-primary">Action 1</button>
  <button class="btn btn-secondary">Action 2</button>
</div>
```

## Lab Exercise
1. Build a centered hero banner card using `d-flex justify-content-center align-items-center min-vh-50`.
