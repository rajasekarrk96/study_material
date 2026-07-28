---
id: "18_03_03"
title: "Navbars and Navigation"
course: "Bootstrap"
module: 3
module_title: "Core Components"
lesson: 3
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["navbar", "navbar-expand-lg", "navbar-brand", "nav-link", "dropdown"]
prerequisites: []
lab_required: true
---

# Navbars and Navigation


## Navbar Component

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">BrandLogo</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item"><a class="nav-link active" href="#">Home</a></li>
        <li class="nav-item"><a class="nav-link" href="#">Features</a></li>
        <li class="nav-item"><a class="nav-link" href="#">Pricing</a></li>
      </ul>
    </div>
  </div>
</nav>
```

## Lab Exercise
1. Build a dark-themed responsive navbar with a dropdown menu and a search form.
