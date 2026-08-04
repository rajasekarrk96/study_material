# Migrating from jQuery to Vanilla JS

> **Course**: Jquery | **Module**: Plugins and Modern Usage | **Difficulty**: intermediate

---

| jQuery Syntax | Modern Vanilla JS Equivalent |
|---|---|
| `$('#el')` | `document.querySelector('#el')` |
| `$('.el')` | `document.querySelectorAll('.el')` |
| `$(el).on('click', fn)` | `el.addEventListener('click', fn)` |
| `$.ajax({url})` | `fetch(url).then(res => res.json())` |
| `$(el).hide()` | `el.style.display = 'none'` |

---

1. Refactor a 20-line jQuery DOM script into clean modern Vanilla JS using `fetch` and ES6 syntax.

---
