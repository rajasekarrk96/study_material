# Plugin Development Basics

> **Course**: Jquery | **Module**: Plugins and Modern Usage | **Difficulty**: advanced

---

```javascript
(function($) {
  $.fn.highlight = function(options) {
    var settings = $.extend({
      color: 'yellow',
      fontStyle: 'normal'
    }, options);

    return this.each(function() {
      $(this).css({
        backgroundColor: settings.color,
        fontStyle: settings.fontStyle
      });
    });
  };
})(jQuery);

// Usage:
$('p').highlight({ color: '#ffecb3' });
```

---

1. Develop a reusable `$.fn.tooltip()` plugin that displays custom hover popups for marked elements.

---
