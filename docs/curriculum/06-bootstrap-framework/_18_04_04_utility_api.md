---
id: "18_04_04"
title: "Utility API"
course: "Bootstrap"
module: 4
module_title: "Advanced Layout and Customization"
lesson: 4
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["utility-api", "sass-map", "custom-utilities", "bootstrap-extending"]
prerequisites: []
lab_required: true
---

# Utility API


## Bootstrap Utility API

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

## Lab Exercise
1. Generate custom `.cursor-pointer` and `.opacity-80` classes using the Utility API.
