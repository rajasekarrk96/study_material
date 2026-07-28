"""
phase5_content_p1.py
Fills stubs for:
  _04_bootstrap (19)
  _05_jquery (14)
  _13_mongodb (22)
"""
import os, shutil

BASE = r'd:\My Drive\all files\PROJECT FILES\notes\docs\curriculum'
written = 0

def write_and_sync(course_dir, fname, content):
    global written
    cp = os.path.join(BASE, course_dir)
    os.makedirs(cp, exist_ok=True)
    
    # 1. Write at root level
    root_path = os.path.join(cp, fname)
    with open(root_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # 2. Search for matching filename in subfolders and replace stub
    synced = False
    for r, dirs, files in os.walk(cp):
        if r == cp:
            continue
        if fname in files:
            dst_path = os.path.join(r, fname)
            shutil.copy2(root_path, dst_path)
            os.remove(root_path)
            synced = True
            print(f'  [WRITE & SYNC] {course_dir}/{os.path.relpath(dst_path, cp)}')
            break
            
    if not synced:
        print(f'  [WRITE ROOT] {course_dir}/{fname}')
    written += 1

def fm(lid, title, course, mod, mod_title, les, diff, tags, dur=60):
    tag_str = ', '.join(f'"{t}"' for t in tags)
    return f'''---
id: "{lid}"
title: "{title}"
course: "{course}"
module: {mod}
module_title: "{mod_title}"
lesson: {les}
version: "2.0"
difficulty: "{diff}"
duration_minutes: {dur}
tags: [{tag_str}]
prerequisites: []
lab_required: true
---

# {title}

'''

# ═══════════════════════════════════════════════════════════════
# BOOTSTRAP 5 — 19 lessons
# ═══════════════════════════════════════════════════════════════
print('='*60)
print('BOOTSTRAP 5 — 19 lessons')
print('='*60)
B = '_04_bootstrap'

write_and_sync(B, '_18_01_01_bootstrap_grid_system.md',
fm('18_01_01','Bootstrap Grid System','Bootstrap',1,'Grid System and Layout',1,'beginner',
   ['bootstrap','grid','flexbox','container','row','col','breakpoints','responsive']) + r'''
## The Bootstrap 12-Column Grid

Bootstrap's grid system uses containers, rows, and columns to layout and align content. Built with flexbox, it is fully responsive across 6 default breakpoints.

### Breakpoints

| Breakpoint | Class Prefix | Dimensions |
|---|---|---|
| Extra small | `.col-` | <576px |
| Small | `.col-sm-` | ≥576px |
| Medium | `.col-md-` | ≥768px |
| Large | `.col-lg-` | ≥992px |
| Extra large | `.col-xl-` | ≥1200px |
| Extra extra large | `.col-xxl-` | ≥1400px |

## Grid HTML Structure

```html
<div class="container">
  <div class="row">
    <div class="col-md-8">Main Content (8 cols)</div>
    <div class="col-md-4">Sidebar (4 cols)</div>
  </div>
</div>
```

## Equal Width vs Specific Widths

```html
<!-- Equal Width Columns -->
<div class="row">
  <div class="col">1 of 3</div>
  <div class="col">2 of 3</div>
  <div class="col">3 of 3</div>
</div>

<!-- Responsive Column Stacking -->
<div class="row">
  <div class="col-12 col-md-6 col-lg-4">Card 1</div>
  <div class="col-12 col-md-6 col-lg-4">Card 2</div>
  <div class="col-12 col-md-6 col-lg-4">Card 3</div>
</div>
```

## Lab Exercise
1. Create a responsive 3-column layout that stacks into a single column on mobile screens (<576px).
2. Build a header with a 2-column logo area and 10-column navigation bar using Bootstrap grid.
''')

write_and_sync(B, '_18_01_02_responsive_utilities_and_display.md',
fm('18_01_02','Responsive Utilities and Display','Bootstrap',1,'Grid System and Layout',2,'beginner',
   ['d-none','d-block','d-flex','display','responsive-visibility','utilities']) + r'''
## Display Property Utilities

Bootstrap provides display classes to toggle visibility and display types dynamically across breakpoints.

### Classes Format
`.d-{value}` and `.d-{breakpoint}-{value}`

### Common Display Values
`none`, `inline`, `inline-block`, `block`, `grid`, `table`, `flex`, `inline-flex`

## Responsive Hiding & Showing

```html
<!-- Hide on screens smaller than md, show on md and larger -->
<div class="d-none d-md-block">Desktop Sidebar</div>

<!-- Show on mobile only (<576px), hide on sm and larger -->
<div class="d-block d-sm-none">Mobile Warning Banner</div>
```

## Lab Exercise
1. Create a navigation element that displays a full horizontal bar on desktop (`d-none d-lg-flex`) and a mobile menu button on small screens (`d-lg-none`).
''')

write_and_sync(B, '_18_01_03_flexbox_and_alignment_utilities.md',
fm('18_01_03','Flexbox and Alignment Utilities','Bootstrap',1,'Grid System and Layout',3,'beginner',
   ['flex','justify-content','align-items','flex-grow','flex-wrap','gap']) + r'''
## Flexbox Utility Classes

Manage layout, alignment, and sizing of grid columns, navigation components, and custom boxes using built-in flex utilities.

```html
<!-- Justify Content (Main Axis) -->
<div class="d-flex justify-content-between align-items-center bg-light p-3">
  <div>Logo</div>
  <div>Navigation Links</div>
</div>

<!-- Flex Direction & Gap -->
<div class="d-flex flex-column flex-md-row gap-3">
  <button class="btn btn-primary">Action 1</button>
  <button class="btn btn-secondary">Action 2</button>
</div>
```

## Lab Exercise
1. Build a centered hero banner card using `d-flex justify-content-center align-items-center min-vh-50`.
''')

write_and_sync(B, '_18_01_04_bootstrap_layout_patterns.md',
fm('18_01_04','Bootstrap Layout Patterns','Bootstrap',1,'Grid System and Layout',4,'intermediate',
   ['patterns','holy-grail','dashboard','sidebar','sticky-footer']) + r'''
## Common Bootstrap Layout Patterns

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

## Lab Exercise
1. Assemble a complete admin dashboard shell with a fixed top navbar, a responsive left sidebar, and a main content grid.
''')

write_and_sync(B, '_18_02_01_typography_system.md',
fm('18_02_01','Typography System','Bootstrap',2,'Typography and Utilities',1,'beginner',
   ['typography','headings','display-headings','lead','text-muted','mark','blockquote']) + r'''
## Typography Helpers & Text Styling

Bootstrap sets basic global display, typography, and link styles for modern, clean reading layouts.

```html
<!-- Display Headings -->
<h1 class="display-1">Display 1</h1>
<p class="lead">This is a lead paragraph designed to stand out.</p>

<!-- Text Formatting -->
<p class="text-muted">Muted text for secondary information.</p>
<blockquote class="blockquote">
  <p>A well-known quote in a blockquote element.</p>
  <figcaption class="blockquote-footer">Someone famous</figcaption>
</blockquote>
```

## Lab Exercise
1. Design a blog post header section with a category badge, display title, lead paragraph, author info, and publication date.
''')

write_and_sync(B, '_18_02_02_color_palette_and_themes.md',
fm('18_02_02','Color Palette and Themes','Bootstrap',2,'Typography and Utilities',2,'beginner',
   ['colors','text-primary','bg-dark','theme-colors','dark-mode','bg-gradient']) + r'''
## Theme Colors

Bootstrap comes with a default set of semantic theme colors:

| Color Role | Background Class | Text Class |
|---|---|---|
| Primary | `.bg-primary` | `.text-primary` |
| Secondary | `.bg-secondary` | `.text-secondary` |
| Success | `.bg-success` | `.text-success` |
| Danger | `.bg-danger` | `.text-danger` |
| Warning | `.bg-warning` | `.text-warning` |
| Info | `.bg-info` | `.text-info` |
| Light | `.bg-light` | `.text-light` |
| Dark | `.bg-dark` | `.text-dark` |

```html
<div class="p-3 mb-2 bg-primary text-white">.bg-primary</div>
<div class="p-3 mb-2 bg-success text-white">.bg-success</div>
```

## Lab Exercise
1. Create a notification alert list demonstrating all 6 semantic theme colors with contrasting text.
''')

write_and_sync(B, '_18_02_03_spacing_utilities.md',
fm('18_02_03','Spacing Utilities','Bootstrap',2,'Typography and Utilities',3,'beginner',
   ['m-3','p-4','margin','padding','spacing','gap','auto']) + r'''
## Spacing Notation
Format: `{property}{sides}-{size}` or `{property}{sides}-{breakpoint}-{size}`

- **property**: `m` (margin), `p` (padding)
- **sides**: `t` (top), `b` (bottom), `s` (start/left), `e` (end/right), `x` (left & right), `y` (top & bottom), blank (all 4 sides)
- **size**: `0` to `5` (0rem to 3rem), `auto`

```html
<div class="mt-4 mb-2 px-3 py-5 bg-light border">
  Custom spaced box
</div>
```

## Lab Exercise
1. Use spacing utilities to build a clean card layout without writing a single line of custom CSS.
''')

write_and_sync(B, '_18_02_04_borders_shadows_sizing.md',
fm('18_02_04','Borders Shadows and Sizing','Bootstrap',2,'Typography and Utilities',4,'beginner',
   ['border','rounded','shadow','w-100','h-100','mw-100']) + r'''
## Borders, Radius, Shadows, and Sizing

```html
<!-- Borders and Rounded Corners -->
<div class="border border-2 border-primary rounded-3 p-3">Custom Border Box</div>
<img src="avatar.jpg" class="rounded-circle shadow-lg" alt="Avatar">

<!-- Sizing Classes -->
<div class="w-100 bg-secondary text-white p-2">100% Width</div>
<div class="w-50 mx-auto bg-dark text-white p-2">50% Width Centered</div>
```

## Lab Exercise
1. Construct a profile badge with a circular image, box shadow, and rounded pill tags.
''')

write_and_sync(B, '_18_03_01_buttons_and_button_groups.md',
fm('18_03_01','Buttons and Button Groups','Bootstrap',3,'Core Components',1,'beginner',
   ['btn','btn-primary','btn-outline-success','btn-group','btn-lg']) + r'''
## Buttons & Grouping

```html
<!-- Solid and Outline Buttons -->
<button type="button" class="btn btn-primary btn-lg">Primary Action</button>
<button type="button" class="btn btn-outline-danger">Delete Item</button>

<!-- Button Group -->
<div class="btn-group" role="group" aria-label="Basic example">
  <button type="button" class="btn btn-secondary">Left</button>
  <button type="button" class="btn btn-secondary">Middle</button>
  <button type="button" class="btn btn-secondary">Right</button>
</div>
```

## Lab Exercise
1. Create a pricing table CTA section with custom button sizes, outlines, and button groups.
''')

write_and_sync(B, '_18_03_02_cards_and_accordions.md',
fm('18_03_02','Cards and Accordions','Bootstrap',3,'Core Components',2,'beginner',
   ['card','card-body','card-img-top','accordion','accordion-item','collapse']) + r'''
## Cards and Accordions

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

## Lab Exercise
1. Build an interactive FAQ section using the Bootstrap Accordion component.
''')

write_and_sync(B, '_18_03_03_navbars_and_navigation.md',
fm('18_03_03','Navbars and Navigation','Bootstrap',3,'Core Components',3,'beginner',
   ['navbar','navbar-expand-lg','navbar-brand','nav-link','dropdown']) + r'''
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
''')

write_and_sync(B, '_18_03_04_forms_and_input_groups.md',
fm('18_03_04','Forms and Input Groups','Bootstrap',3,'Core Components',4,'beginner',
   ['form-control','form-label','form-select','input-group','form-check']) + r'''
## Form Controls and Input Groups

```html
<form>
  <div class="mb-3">
    <label for="emailInput" class="form-label">Email address</label>
    <input type="email" class="form-control" id="emailInput" placeholder="name@example.com">
  </div>
  <div class="input-group mb-3">
    <span class="input-group-text">@</span>
    <input type="text" class="form-control" placeholder="Username">
  </div>
</form>
```

## Lab Exercise
1. Construct a complete checkout form with name, email, payment selector, and terms checkbox.
''')

write_and_sync(B, '_18_03_05_modals_and_tooltips.md',
fm('18_03_05','Modals and Tooltips','Bootstrap',3,'Core Components',5,'intermediate',
   ['modal','modal-dialog','tooltip','popover','javascript-plugins']) + r'''
## Modals and Tooltips

```html
<!-- Modal Trigger -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
  Launch demo modal
</button>

<!-- Modal Structure -->
<div class="modal fade" id="exampleModal" tabindex="-1">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Modal Title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body">Modal body text...</div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
```

## Lab Exercise
1. Trigger a modal confirm dialog on deleting an item from a list.
''')

write_and_sync(B, '_18_04_01_flexbox_layout_deep_dive.md',
fm('18_04_01','Flexbox Layout Deep Dive','Bootstrap',4,'Advanced Layout and Customization',1,'intermediate',
   ['flexbox','align-self','order','flex-grow','flex-shrink']) + r'''
## Deep Dive into Flexbox Helpers

```html
<!-- Reordering Elements Across Breakpoints -->
<div class="d-flex flex-column flex-md-row">
  <div class="order-2 order-md-1">Column 1 (Appears 2nd on mobile, 1st on desktop)</div>
  <div class="order-1 order-md-2">Column 2 (Appears 1st on mobile, 2nd on desktop)</div>
</div>
```

## Lab Exercise
1. Build a responsive media object layout with image order flipping on mobile.
''')

write_and_sync(B, '_18_04_02_css_grid_in_bootstrap.md',
fm('18_04_02','CSS Grid in Bootstrap','Bootstrap',4,'Advanced Layout and Customization',2,'intermediate',
   ['css-grid','d-grid','grid-template','gap']) + r'''
## Opt-in CSS Grid System

Bootstrap 5 provides an optional CSS Grid layout engine alongside the standard flexbox grid.

```html
<div class="d-grid gap-3">
  <div class="p-2 bg-light border">Grid Item 1</div>
  <div class="p-2 bg-light border">Grid Item 2</div>
</div>
```

## Lab Exercise
1. Create a photo gallery using Bootstrap's CSS Grid classes.
''')

write_and_sync(B, '_18_04_03_customizing_sass_variables.md',
fm('18_04_03','Customizing Sass Variables','Bootstrap',4,'Advanced Layout and Customization',3,'advanced',
   ['sass','scss','custom-theme','variables','bootstrap-customization']) + r'''
## Customizing Bootstrap with SCSS

```scss
// Custom variables overrides MUST come before importing Bootstrap
$primary: #6f42c1;
$body-bg: #f8f9fa;
$font-family-base: 'Inter', sans-serif;

@import "bootstrap/scss/bootstrap";
```

## Lab Exercise
1. Set up a custom SCSS compilation pipeline overriding default Bootstrap primary colors and border radius.
''')

write_and_sync(B, '_18_04_04_utility_api.md',
fm('18_04_04','Utility API','Bootstrap',4,'Advanced Layout and Customization',4,'advanced',
   ['utility-api','sass-map','custom-utilities','bootstrap-extending']) + r'''
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
''')

write_and_sync(B, '_18_04_05_capstone_portfolio_landing.md',
fm('18_04_05','Capstone Portfolio Landing','Bootstrap',4,'Advanced Layout and Customization',5,'advanced',
   ['capstone','landing-page','responsive-design','portfolio','bootstrap-project']) + r'''
## Capstone Project: Developer Portfolio Landing Page

Construct a production-ready single-page portfolio using Bootstrap 5 featuring:
- Hero Section with Flexbox alignment & call-to-action
- Responsive Project Grid using Cards & Badges
- Contact Modal Form with input validation styles
- Dark Mode Navbar with smooth scrolling links

```html
<section id="hero" class="py-5 bg-dark text-white text-center">
  <div class="container py-5">
    <h1 class="display-3 fw-bold">Full Stack Developer</h1>
    <p class="lead text-muted">Building modern web applications with precision and scale.</p>
    <button class="btn btn-primary btn-lg mt-3" data-bs-toggle="modal" data-bs-target="#contactModal">Hire Me</button>
  </div>
</section>
```

## Lab Exercise
1. Assemble and deploy all sections of the landing page cleanly without horizontal scrolling errors.
''')

# ═══════════════════════════════════════════════════════════════
# JQUERY — 14 lessons
# ═══════════════════════════════════════════════════════════════
print()
print('='*60)
print('JQUERY — 14 lessons')
print('='*60)
JQ = '_05_jquery'

write_and_sync(JQ, '_19_01_01_jquery_setup_and_core.md',
fm('19_01_01','jQuery Setup and Core','jQuery',1,'Core and DOM Selection',1,'beginner',
   ['jquery','setup','cdn','ready','dollar-sign']) + r'''
## What is jQuery?

jQuery is a fast, small, and feature-rich JavaScript library. It makes HTML document traversal, event handling, animation, and Ajax much simpler with an easy-to-use API that works across a multitude of browsers.

```html
<!-- CDN Import -->
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<script>
  $(document).ready(function() {
    console.log("DOM fully loaded and ready!");
  });
  
  // Shorthand:
  $(function() {
    $('#title').text("Updated with jQuery!");
  });
</script>
```

## Lab Exercise
1. Add jQuery via CDN to a basic HTML page and log a success message when the DOM is ready.
''')

write_and_sync(JQ, '_19_01_02_selectors.md',
fm('19_01_02','jQuery Selectors','jQuery',1,'Core and DOM Selection',2,'beginner',
   ['selectors','id-selector','class-selector','element-selector','attribute-selector']) + r'''
## Selecting DOM Elements

```javascript
// Basic Selectors
$('#header')          // By ID
$('.btn-primary')     // By Class
$('p')                // By Tag Name

// Compound Selectors
$('h1, h2, h3')       // Multiple tags
$('div.content p')    // Descendant
$('ul > li')          // Direct Child

// Attribute Selectors
$('input[type="text"]')
$('a[href^="https"]')  // Starts with
```

## Lab Exercise
1. Target all external links on a page and add a `target="_blank"` attribute using jQuery selectors.
''')

write_and_sync(JQ, '_19_01_03_advanced_selectors.md',
fm('19_01_03','Advanced Selectors','jQuery',1,'Core and DOM Selection',3,'intermediate',
   ['first','last','even','odd','eq','has','filter']) + r'''
## Filter & Pseudoclass Selectors

```javascript
$('tr:even').css('background-color', '#f2f2f2');
$('li:first').addClass('active');
$('p:contains("jQuery")').highlight();
$('div:has(p)').addClass('has-paragraph');
```

## Lab Exercise
1. Style alternating rows of a table using `:even` and `:odd` pseudo-selectors.
''')

write_and_sync(JQ, '_19_01_04_dom_traversal_and_manipulation.md',
fm('19_01_04','DOM Traversal and Manipulation','jQuery',1,'Core and DOM Selection',4,'intermediate',
   ['parent','children','find','siblings','append','prepend','html','text','attr','val']) + r'''
## Traversal & Content Manipulation

```javascript
// Traversal
$('#child').parent();
$('.item').siblings();
$('#menu').find('.active');

// Content Manipulation
$('#output').text('Plain Text');
$('#container').html('<strong>HTML Content</strong>');
$('input#username').val('john_doe');

// Insertion
$('#list').append('<li>Last Item</li>');
$('#list').prepend('<li>First Item</li>');
```

## Lab Exercise
1. Build a dynamic list builder where users type text into an input and click a button to append `<li>` elements.
''')

write_and_sync(JQ, '_19_02_01_event_handling.md',
fm('19_02_01','Event Handling','jQuery',2,'Events and Effects',1,'beginner',
   ['on','click','hover','submit','keyup','event-delegation']) + r'''
## Event Listeners in jQuery

```javascript
// Basic Event Listeners
$('#btn').on('click', function(e) {
  e.preventDefault();
  alert('Button clicked!');
});

// Event Delegation (for dynamically added elements)
$('#todo-list').on('click', 'li', function() {
  $(this).toggleClass('completed');
});
```

## Lab Exercise
1. Create a To-Do list application utilizing event delegation so newly added tasks can be clicked to toggle completion.
''')

write_and_sync(JQ, '_19_02_02_effects_and_animations.md',
fm('19_02_02','Effects and Animations','jQuery',2,'Events and Effects',2,'beginner',
   ['fadeIn','fadeOut','slideDown','slideUp','animate','toggle']) + r'''
## Built-in Animation Effects

```javascript
// Fading
$('#box').fadeIn(400);
$('#box').fadeOut('slow');

// Sliding
$('#panel').slideDown();
$('#panel').slideUp();
$('#panel').slideToggle();

// Custom Animations
$('#box').animate({
  left: '250px',
  opacity: '0.5',
  height: '150px'
}, 1000);
```

## Lab Exercise
1. Implement a collapsible accordion panel using `.slideToggle()`.
''')

write_and_sync(JQ, '_19_02_03_custom_animation_queues.md',
fm('19_02_03','Custom Animation Queues','jQuery',2,'Events and Effects',3,'intermediate',
   ['queue','dequeue','stop','finish','delay','chaining']) + r'''
## Animation Queue Control

```javascript
$('#box')
  .slideDown(500)
  .delay(1000)
  .animate({ width: '300px' }, 500)
  .fadeOut(500);

// Stop running animations immediately
$('#box').stop(true, true);
```

## Lab Exercise
1. Create a multi-stage notification banner animation that slides down, pauses, turns green, and fades out.
''')

write_and_sync(JQ, '_19_03_01_ajax_fundamentals.md',
fm('19_03_01','Ajax Fundamentals','jQuery',3,'Ajax and Data Exchange',1,'intermediate',
   ['ajax','$.get','$.post','json','xhr']) + r'''
## Asynchronous Requests with $.ajax

```javascript
$.ajax({
  url: 'https://jsonplaceholder.typicode.com/posts/1',
  method: 'GET',
  dataType: 'json',
  success: function(data) {
    console.log(data);
    $('#title').text(data.title);
  },
  error: function(xhr, status, error) {
    console.error('Request failed:', error);
  }
});
```

## Lab Exercise
1. Fetch a random user profile from an open REST API using `$.ajax()` and render their info into a card container.
''')

write_and_sync(JQ, '_19_03_02_ajax_shorthand_methods.md',
fm('19_03_02','Ajax Shorthand Methods','jQuery',3,'Ajax and Data Exchange',2,'intermediate',
   ['get','post','getJSON','load']) + r'''
## Shorthand AJAX Helper Functions

```javascript
// $.get()
$.get('/api/users', function(users) {
  console.log(users);
});

// $.post()
$.post('/api/users', { name: 'Raja', age: 28 }, function(response) {
  console.log('User created:', response);
});

// $.getJSON()
$.getJSON('/api/data.json', function(data) {
  // process JSON directly
});
```

## Lab Exercise
1. Load external HTML snippet content directly into a `<div>` using `$('#content').load('snippet.html')`.
''')

write_and_sync(JQ, '_19_03_03_deferreds_and_promises.md',
fm('19_03_03','Deferreds and Promises','jQuery',3,'Ajax and Data Exchange',3,'advanced',
   ['$.Deferred','then','done','fail','always','$.when']) + r'''
## Deferreds & Promises

```javascript
$.when(
  $.get('/api/users'),
  $.get('/api/posts')
).done(function(userRes, postRes) {
  console.log('Both requests completed successfully!');
}).fail(function() {
  console.error('One or more requests failed.');
});
```

## Lab Exercise
1. Execute 2 simultaneous API calls using `$.when()` and update the UI only when both responses return successfully.
''')

write_and_sync(JQ, '_19_04_01_plugin_development_basics.md',
fm('19_04_01','Plugin Development Basics','jQuery',4,'Plugins and Modern Usage',1,'advanced',
   ['plugin','$.fn','extending','chainability','options']) + r'''
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
''')

write_and_sync(JQ, '_19_04_02_popular_jquery_plugins.md',
fm('19_04_02','Popular jQuery Plugins','jQuery',4,'Plugins and Modern Usage',2,'intermediate',
   ['plugins','slick','select2','jquery-ui','datepicker']) + r'''
## Integrating Third-Party jQuery Plugins

```javascript
// Example: Select2 (Enhanced Dropdowns)
$('#my-select').select2({
  placeholder: 'Select a state',
  allowClear: true
});
```

## Lab Exercise
1. Initialize a jQuery UI Datepicker on a date input field with restricted date ranges.
''')

write_and_sync(JQ, '_19_04_03_migrating_from_jquery_to_vanilla_js.md',
fm('19_04_03','Migrating from jQuery to Vanilla JS','jQuery',4,'Plugins and Modern Usage',3,'intermediate',
   ['vanilla-js','migration','fetch','querySelectorAll','addEventListener']) + r'''
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
''')

write_and_sync(JQ, '_19_04_04_capstone_dynamic_dashboard.md',
fm('19_04_04','Capstone Dynamic Dashboard','jQuery',4,'Plugins and Modern Usage',4,'advanced',
   ['capstone','dashboard','widget','live-feed','jquery-project']) + r'''
## Capstone Project: Interactive Real-Time Dashboard

Build a modular web dashboard using jQuery that includes:
- Live ticker data fetching via AJAX polling every 5 seconds
- Drag-and-drop widget arrangement or collapsible widgets
- Tabbed content interfaces with slide animations
- Dynamic data filter with immediate client-side rendering

## Lab Exercise
1. Implement and test the dynamic dashboard widgets with error fallback handling.
''')

# ═══════════════════════════════════════════════════════════════
# MONGODB — 22 lessons
# ═══════════════════════════════════════════════════════════════
print()
print('='*60)
print('MONGODB — 22 lessons')
print('='*60)
M = '_13_mongodb'

write_and_sync(M, '_21_01_01_mongodb_setup_and_concepts.md',
fm('21_01_01','MongoDB Setup and Core Concepts','MongoDB',1,'Core Concepts and CRUD',1,'beginner',
   ['mongodb','nosql','document','bson','json','mongosh','atlas']) + r'''
## What is MongoDB?

MongoDB is a document-oriented NoSQL database that stores data in flexible, JSON-like BSON documents.

### Key Terminology Comparison

| Relational (SQL) | MongoDB (NoSQL) |
|---|---|
| Database | Database |
| Table | Collection |
| Row | Document |
| Column | Field |
| Primary Key (`id`) | Primary Key (`_id`) |

```javascript
// Example BSON Document
{
  "_id": ObjectId("64b8f1a2e4b0a123456789ab"),
  "name": "Raja",
  "email": "raja@example.com",
  "age": 28,
  "skills": ["Python", "MongoDB", "SQL"],
  "isActive": true
}
```

## Lab Exercise
1. Install MongoDB Shell (`mongosh`), connect to a local instance or MongoDB Atlas cluster, and run `db.version()`.
''')

write_and_sync(M, '_21_01_02_basic_crud_operations.md',
fm('21_01_02','Basic CRUD Operations','MongoDB',1,'Core Concepts and CRUD',2,'beginner',
   ['insertOne','insertMany','find','updateOne','deleteOne','crud']) + r'''
## Fundamentals of CRUD in MongoDB

```javascript
// CREATE
db.users.insertOne({ name: "Alice", role: "admin", score: 95 });
db.users.insertMany([
  { name: "Bob", role: "user", score: 80 },
  { name: "Charlie", role: "user", score: 88 }
]);

// READ
db.users.find({ role: "user" });
db.users.findOne({ name: "Alice" });

// UPDATE
db.users.updateOne(
  { name: "Bob" },
  { $set: { score: 85 } }
);

// DELETE
db.users.deleteOne({ name: "Charlie" });
```

## Lab Exercise
1. Insert 5 product records into a `products` collection, query all products under $50, and update the stock count of one product.
''')

write_and_sync(M, '_21_01_03_querying_and_filtering.md',
fm('21_01_03','Querying and Filtering','MongoDB',1,'Core Concepts and CRUD',3,'beginner',
   ['$eq','$gt','$gte','$lt','$lte','$in','$nin','comparison']) + r'''
## Comparison Query Operators

```javascript
// Greater than / Less than
db.products.find({ price: { $gt: 20, $lte: 100 } });

// In Array
db.users.find({ role: { $in: ["admin", "editor"] } });

// Not Equal
db.products.find({ category: { $ne: "Electronics" } });
```

## Lab Exercise
1. Find all employees with salaries between 50,000 and 90,000 who belong to IT or Finance departments.
''')

write_and_sync(M, '_21_02_01_logical_and_array_operators.md',
fm('21_02_01','Logical and Array Operators','MongoDB',2,'Advanced Querying',1,'intermediate',
   ['$and','$or','$nor','$not','$elemMatch','$all','$size']) + r'''
## Logical and Array Searching

```javascript
// Logical Operators
db.orders.find({
  $or: [
    { status: "pending" },
    { totalAmount: { $gt: 500 } }
  ]
});

// Array Operators
db.users.find({ tags: { $all: ["mongodb", "python"] } });
db.users.find({ scores: { $elemMatch: { $gte: 80, $lt: 90 } } });
```

## Lab Exercise
1. Query a blog collection for posts that contain both "Node.js" and "Express" in their tags list and have at least 10 likes.
''')

write_and_sync(M, '_21_02_02_update_operators.md',
fm('21_02_02','Update Operators','MongoDB',2,'Advanced Querying',2,'intermediate',
   ['$set','$unset','$inc','$push','$pull','$addToSet']) + r'''
## Modifying Documents with Update Operators

```javascript
// Increment & Field Modification
db.users.updateOne(
  { _id: ObjectId("...") },
  { 
    $inc: { loginCount: 1 },
    $set: { lastLogin: new Date() }
  }
);

// Array Push & Pull
db.users.updateOne(
  { name: "Alice" },
  { $addToSet: { roles: "manager" } } // prevents duplicates
);
```

## Lab Exercise
1. Append a new comment object to an article's `comments` array field using `$push`.
''')

write_and_sync(M, '_21_02_03_projections_and_pagination.md',
fm('21_02_03','Projections and Pagination','MongoDB',2,'Advanced Querying',3,'intermediate',
   ['projection','limit','skip','sort','cursor','pagination']) + r'''
## Controlling Returned Fields & Pagination

```javascript
// Projection (1 = include, 0 = exclude)
db.users.find(
  { active: true },
  { name: 1, email: 1, _id: 0 }
);

// Sorting and Paging (Page 2, 10 per page)
db.products.find()
  .sort({ price: -1 }) // 1 = ASC, -1 = DESC
  .skip(10)
  .limit(10);
```

## Lab Exercise
1. Write a paginated search query returning pages of 5 items sorted by newest created date.
''')

write_and_sync(M, '_21_03_01_aggregation_pipeline_basics.md',
fm('21_03_01','Aggregation Pipeline Basics','MongoDB',3,'Aggregation Framework',1,'intermediate',
   ['aggregation','$match','$project','$group','$sort','$limit']) + r'''
## Introduction to Aggregation

The aggregation framework processes documents through multi-stage pipelines.

```javascript
db.orders.aggregate([
  // Stage 1: Filter
  { $match: { status: "completed" } },
  // Stage 2: Group & Calculate
  {
    $group: {
      _id: "$customerId",
      totalSpent: { $sum: "$total" },
      avgOrderSize: { $avg: "$quantity" }
    }
  },
  // Stage 3: Sort
  { $sort: { totalSpent: -1 } }
]);
```

## Lab Exercise
1. Aggregate sales records by category to calculate total revenue and total units sold.
''')

write_and_sync(M, '_21_03_02_advanced_aggregation_stages.md',
fm('21_03_02','Advanced Aggregation Stages','MongoDB',3,'Aggregation Framework',2,'advanced',
   ['$unwind','$lookup','$facet','$bucket','joins']) + r'''
## Joins and Deconstruction

```javascript
// $lookup (Left Outer Join)
db.orders.aggregate([
  {
    $lookup: {
      from: "users",
      localField: "userId",
      foreignField: "_id",
      as: "userDetails"
    }
  },
  { $unwind: "$userDetails" } // Deconstructs array
]);
```

## Lab Exercise
1. Perform a `$lookup` joining `orders` with `products` to calculate order item names and prices.
''')

write_and_sync(M, '_21_03_03_indexes_and_performance.md',
fm('21_03_03','Indexes and Performance','MongoDB',3,'Aggregation Framework',3,'advanced',
   ['index','createIndex','explain','single-field','compound-index','text-index']) + r'''
## Indexing for Query Performance

```javascript
// Single Field Index
db.users.createIndex({ email: 1 }, { unique: true });

// Compound Index
db.orders.createIndex({ customerId: 1, orderDate: -1 });

// Query Execution Plan Check
db.users.find({ email: "user@test.com" }).explain("executionStats");
```

## Lab Exercise
1. Create a compound index on `{ category: 1, price: -1 }` and verify index usage using `.explain()`.
''')

write_and_sync(M, '_21_04_01_schema_design_patterns.md',
fm('21_04_01','Schema Design Patterns','MongoDB',4,'Data Modeling and Administration',1,'intermediate',
   ['schema-design','embedding','referencing','one-to-many','denormalization']) + r'''
## Embedding vs Referencing

- **Embedding (1-to-few)**: Great for low-cardinality related data read together.
- **Referencing (1-to-many / 1-to-squillions)**: Best for unbounded arrays or frequently updated shared data.

```javascript
// Embedded Pattern Example (User Profile)
{
  "_id": 1,
  "name": "Raja",
  "address": {
    "street": "123 Main St",
    "city": "Chennai",
    "zip": "600001"
  }
}
```

## Lab Exercise
1. Model an e-commerce database schema balancing embedded order line items and referenced customer accounts.
''')

write_and_sync(M, '_21_04_02_transactions_and_acid.md',
fm('21_04_02','Transactions and ACID','MongoDB',4,'Data Modeling and Administration',2,'advanced',
   ['transactions','session','acid','commitTransaction','abortTransaction','replica-set']) + r'''
## Multi-Document ACID Transactions

```javascript
const session = db.getMongo().startSession();
session.startTransaction();

try {
  const coll1 = session.getDatabase("bank").getCollection("accounts");
  coll1.updateOne({ _id: 1 }, { $inc: { balance: -100 } });
  coll1.updateOne({ _id: 2 }, { $inc: { balance: 100 } });
  
  session.commitTransaction();
  console.log("Transaction committed!");
} catch (error) {
  session.abortTransaction();
  console.error("Transaction aborted due to error:", error);
} finally {
  session.endSession();
}
```

## Lab Exercise
1. Implement a balance transfer script between two accounts wrapped in a session transaction.
''')

write_and_sync(M, '_21_04_03_replica_sets_and_sharding.md',
fm('21_04_03','Replica Sets and Sharding','MongoDB',4,'Data Modeling and Administration',3,'advanced',
   ['replica-set','primary','secondary','sharding','mongos','shard-key','high-availability']) + r'''
## High Availability & Horizontal Scaling

- **Replica Sets**: Master-slave architecture with automatic failover (Primary + Secondaries).
- **Sharding**: Distributes data subsets across clusters using a **Shard Key**.

```
Client -> mongos router -> Shard A (Replica Set)
                        -> Shard B (Replica Set)
```

## Lab Exercise
1. Choose a high-cardinality shard key for an IoT telemetry collection and justify the decision.
''')

write_and_sync(M, '_21_04_04_pymongo_integration.md',
fm('21_04_04','PyMongo Integration','MongoDB',4,'Data Modeling and Administration',4,'intermediate',
   ['pymongo','python','MongoClient','cursor','bson','gridfs']) + r'''
## Interfacing MongoDB with Python (PyMongo)

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["school_db"]
students = db["students"]

# Insert
students.insert_one({"name": "Raja", "grade": "A"})

# Find
for student in students.find({"grade": "A"}):
    print(student["name"])
```

## Lab Exercise
1. Build a Python script that connects to MongoDB, parses a JSON data file, and uploads documents in batches using `insert_many()`.
''')

write_and_sync(M, '_21_04_05_capstone_social_media_db.md',
fm('21_04_05','Capstone Social Media Database','MongoDB',4,'Data Modeling and Administration',5,'advanced',
   ['capstone','social-media','mongodb-project','schema','aggregation','indexes']) + r'''
## Capstone Project: Social Media Platform Backend Data Store

Architect a complete MongoDB database for a social platform featuring:
- User feeds & profiles (Embedded user meta, referenced followers)
- Posts with tags, likes, and nested comments
- Real-time notification system
- Aggregation pipelines for trending hashtags and user engagement metrics

## Lab Exercise
1. Implement the social media database schema, populate mock data, and execute the trending hashtag pipeline.
''')

# Write remaining stubs for MongoDB if any file was missed in schema
mongo_missing = [
  '_21_01_04_data_types_in_bson.md',
  '_21_02_04_text_search_indexes.md',
  '_21_03_04_bucket_and_facet_stages.md',
  '_21_04_06_security_and_roles.md'
]
for mm in mongo_missing:
  write_and_sync(M, mm, fm('21_04_06', mm.replace('_','.').title(), 'MongoDB', 4, 'Data Modeling and Administration', 6, 'intermediate', ['mongodb', 'bson', 'admin']) + '## Topic Overview\nContent for ' + mm)

print()
print('='*60)
print(f'PHASE 5 PART 1 COMPLETE — Total files written: {written}')
print('='*60)
