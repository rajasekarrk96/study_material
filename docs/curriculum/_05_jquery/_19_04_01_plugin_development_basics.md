---
id: "19_04_01"
title: "Plugin Development Basics"
course: "jQuery"
module: 4
module_title: "Plugins and Modern Usage"
lesson: 1
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["plugin", "$.fn", "extending", "chainability", "options"]
prerequisites: []
lab_required: true
---

# Plugin Development Basics


## Writing Custom jQuery Plugins

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

## Lab Exercise
1. Develop a reusable `$.fn.tooltip()` plugin that displays custom hover popups for marked elements.
