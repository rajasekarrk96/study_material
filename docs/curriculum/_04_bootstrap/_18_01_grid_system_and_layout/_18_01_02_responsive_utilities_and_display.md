---
id: "18_01_02"
title: "Responsive Utilities and Display"
course: "Bootstrap"
module: 1
module_title: "Grid System and Layout"
lesson: 2
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["d-none", "d-block", "d-flex", "display", "responsive-visibility", "utilities"]
prerequisites: []
lab_required: true
---

# Responsive Utilities and Display


## Display Property Utilities

Bootstrap provides display classes to toggle visibility and display types dynamically across breakpoints.

### Classes Format
`.d-{value}` and `.d-{breakpoint}-{value}`

### Common Display Values
`none`, `inline`, `inline-block`, `block`, `grid`, `table`, `flex`, `inline-flex`

## Responsive Hiding & Showing

```html
<!-- Hide on screens smaller than md, show on md and larger -->
<div class="d-none d-md-block">Desktop Sidebar</div>

<!-- Show on mobile only (<576px), hide on sm and larger -->
<div class="d-block d-sm-none">Mobile Warning Banner</div>
```

## Lab Exercise
1. Create a navigation element that displays a full horizontal bar on desktop (`d-none d-lg-flex`) and a mobile menu button on small screens (`d-lg-none`).
