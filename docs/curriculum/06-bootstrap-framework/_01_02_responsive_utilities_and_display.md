# Responsive Utilities and Display

> **Course**: Bootstrap | **Module**: Grid System and Layout | **Difficulty**: beginner

---

Bootstrap provides display classes to toggle visibility and display types dynamically across breakpoints.

### Classes Format
`.d-{value}` and `.d-{breakpoint}-{value}`

### Common Display Values
`none`, `inline`, `inline-block`, `block`, `grid`, `table`, `flex`, `inline-flex`

---

```html
<!-- Hide on screens smaller than md, show on md and larger -->
<div class="d-none d-md-block">Desktop Sidebar</div>

<!-- Show on mobile only (<576px), hide on sm and larger -->
<div class="d-block d-sm-none">Mobile Warning Banner</div>
```

---

1. Create a navigation element that displays a full horizontal bar on desktop (`d-none d-lg-flex`) and a mobile menu button on small screens (`d-lg-none`).

---
