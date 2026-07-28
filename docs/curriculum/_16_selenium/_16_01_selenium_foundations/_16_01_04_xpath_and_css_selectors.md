---
id: "16_01_04"
title: "XPath and CSS Selectors"
course: "Selenium"
module: 1
module_title: "Selenium Fundamentals"
lesson: 4
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["xpath", "css-selector", "axes", "predicates", "contains", "text()", "attribute", "parent", "sibling", "nth-child"]
prerequisites: []
lab_required: true
---

# XPath and CSS Selectors


## CSS Selector Syntax

```css
/* By element type */
input
button

/* By ID */
#username
input#username

/* By class */
.btn-primary
button.btn.btn-primary    /* multiple classes */

/* By attribute */
input[type="email"]
input[placeholder="Enter email"]
[data-testid="submit-btn"]

/* Child selectors */
form > input           /* direct child */
.container input       /* any descendant */

/* Nth child */
li:nth-child(2)        /* second li */
li:first-child
li:last-child
li:nth-of-type(3)

/* Chaining */
#login-form input[type="password"]
.product-list > .product-card > .price
```

## XPath Syntax

```xpath
/* Basic */
//input                          all input elements
//input[@id="username"]          input with id=username
//input[@type="email"]           input with type=email

/* Text content */
//button[text()="Submit"]
//a[contains(text(), "Login")]
//h1[normalize-space()="Home"]

/* Contains */
//input[contains(@class, "form-control")]
//div[contains(@id, "product-")]

/* Starts-with */
//input[starts-with(@name, "user")]

/* Axes */
//label[@for="email"]/following-sibling::input
//td[text()="Price"]/following-sibling::td
//input[@id="email"]/parent::div
//tr/td[1]                      first column of each row

/* Index (1-based!) */
(//li[@class="item"])[1]
(//tr)[last()]

/* AND / OR */
//input[@type="text" and @required]
//button[@type="submit" or @type="button"]
```

## Practical Examples

```python
# Find table cell containing "Active" in same row as specific name
driver.find_element(By.XPATH,
    "//tr[td[text()='John Doe']]/td[contains(@class,'status')]")

# Find button that comes after a specific heading
driver.find_element(By.XPATH,
    "//h2[text()='Payment Details']/following::button[@type='submit']")

# Dynamic ID that starts with known prefix
driver.find_element(By.CSS_SELECTOR, "[id^='react-select-']")
```

## CSS vs XPath — When to Use

| Feature | CSS | XPath |
|---|---|---|
| Speed | Faster | Slightly slower |
| Readability | More readable | Complex |
| Parent traversal | Not supported | Supported |
| Text matching | Not supported | Supported |
| Browser support | Universal | Universal |

## Lab Exercise
1. Extract all product names from a table using XPath axes
2. Write CSS selector for: input with class containing "form" inside a div with id "checkout"
3. Use XPath to find a button that follows a specific label text
