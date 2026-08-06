---
id: "18_02_03"
title: "Spacing Utilities"
course: "Bootstrap"
module: 2
module_title: "Typography and Utilities"
lesson: 3
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["m-3", "p-4", "margin", "padding", "spacing", "gap", "auto"]
prerequisites: []
lab_required: true
---

# Spacing Utilities


## Spacing Notation
Format: `{property}{sides}-{size}` or `{property}{sides}-{breakpoint}-{size}`

- **property**: `m` (margin), `p` (padding)
- **sides**: `t` (top), `b` (bottom), `s` (start/left), `e` (end/right), `x` (left & right), `y` (top & bottom), blank (all 4 sides)
- **size**: `0` to `5` (0rem to 3rem), `auto`

```html
<div class="mt-4 mb-2 px-3 py-5 bg-light border">
  Custom spaced box
</div>
```

## Lab Exercise
1. Use spacing utilities to build a clean card layout without writing a single line of custom CSS.
