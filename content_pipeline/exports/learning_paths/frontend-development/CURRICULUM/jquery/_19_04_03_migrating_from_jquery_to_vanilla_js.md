---
id: "19_04_03"
title: "Migrating from jQuery to Vanilla JS"
course: "jQuery"
module: 4
module_title: "Plugins and Modern Usage"
lesson: 3
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["vanilla-js", "migration", "fetch", "querySelectorAll", "addEventListener"]
prerequisites: []
lab_required: true
---

# Migrating from jQuery to Vanilla JS


## Modern Alternatives to jQuery

| jQuery Syntax | Modern Vanilla JS Equivalent |
|---|---|
| `$('#el')` | `document.querySelector('#el')` |
| `$('.el')` | `document.querySelectorAll('.el')` |
| `$(el).on('click', fn)` | `el.addEventListener('click', fn)` |
| `$.ajax({url})` | `fetch(url).then(res => res.json())` |
| `$(el).hide()` | `el.style.display = 'none'` |

## Lab Exercise
1. Refactor a 20-line jQuery DOM script into clean modern Vanilla JS using `fetch` and ES6 syntax.
