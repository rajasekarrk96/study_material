# Cards and Accordions

> **Course**: Bootstrap | **Module**: Core Components | **Difficulty**: beginner

---

```html
<!-- Card Component -->
<div class="card" style="width: 18rem;">
  <img src="https://via.placeholder.com/150" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>

<!-- Accordion Component -->
<div class="accordion" id="faqAccordion">
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne">
        Question #1
      </button>
    </h2>
    <div id="collapseOne" class="accordion-collapse collapse show">
      <div class="accordion-body">Answer text goes here...</div>
    </div>
  </div>
</div>
```

---

1. Build an interactive FAQ section using the Bootstrap Accordion component.

---
