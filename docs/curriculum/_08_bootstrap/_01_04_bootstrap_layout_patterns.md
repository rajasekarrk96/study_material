# Bootstrap Layout Patterns

> **Course**: Bootstrap | **Module**: Grid System and Layout | **Difficulty**: intermediate

---

### Holy Grail / Dashboard Layout

```html
<div class="container-fluid">
  <div class="row min-vh-100">
    <nav class="col-md-3 col-lg-2 d-md-block bg-dark sidebar collapse p-3 text-white">
      <h5>Dashboard</h5>
    </nav>
    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 py-4">
      <h1>Main Content Area</h1>
    </main>
  </div>
</div>
```

---

1. Assemble a complete admin dashboard shell with a fixed top navbar, a responsive left sidebar, and a main content grid.

---
