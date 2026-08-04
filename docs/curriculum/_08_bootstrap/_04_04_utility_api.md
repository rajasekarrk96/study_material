# Utility API

> **Course**: Bootstrap | **Module**: Advanced Layout and Customization | **Difficulty**: advanced

---

Add, change, or remove Bootstrap utilities by modifying the `$utilities` map in Sass.

```scss
$utilities: map-merge(
  $utilities,
  (
    "cursor": (
      property: cursor,
      class: cursor,
      values: pointer grab progress,
    )
  )
);
```

---

1. Generate custom `.cursor-pointer` and `.opacity-80` classes using the Utility API.

---
