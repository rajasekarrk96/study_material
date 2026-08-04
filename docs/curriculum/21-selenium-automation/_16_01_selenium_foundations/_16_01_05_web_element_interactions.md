---
id: "16_01_05"
title: "Web Element Interactions"
course: "Selenium"
module: 1
module_title: "Selenium Fundamentals"
lesson: 5
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["click", "send_keys", "clear", "text", "get_attribute", "is_displayed", "is_enabled", "is_selected", "submit", "value"]
prerequisites: []
lab_required: true
---

# Web Element Interactions


## Core Element Methods

```python
element = driver.find_element(By.ID, "username")

# Clicking
element.click()

# Typing
element.send_keys("myusername")
element.clear()                         # clear existing text
element.send_keys("new text")

# Form submit
form = driver.find_element(By.ID, "login-form")
form.submit()

# Read content
print(element.text)                     # visible text
print(element.get_attribute("value"))   # input value
print(element.get_attribute("href"))    # link href
print(element.get_attribute("class"))   # class attribute
print(element.get_attribute("innerHTML"))
print(element.get_attribute("outerHTML"))

# State checks
element.is_displayed()   # True if visible
element.is_enabled()     # True if not disabled
element.is_selected()    # True if checkbox/radio checked
```

## Special Keys

```python
from selenium.webdriver.common.keys import Keys

element.send_keys(Keys.RETURN)       # Enter
element.send_keys(Keys.TAB)          # Tab
element.send_keys(Keys.ESCAPE)       # Esc
element.send_keys(Keys.BACKSPACE)    # Backspace
element.send_keys(Keys.CONTROL, "a") # Ctrl+A (select all)
element.send_keys(Keys.CONTROL, "c") # Ctrl+C
element.send_keys(Keys.HOME)
element.send_keys(Keys.END)
element.send_keys(Keys.PAGE_DOWN)
element.send_keys(Keys.ARROW_DOWN)
```

## CSS Properties and Dimensions

```python
# CSS value
color = element.value_of_css_property("color")
font_size = element.value_of_css_property("font-size")

# Location and size
location = element.location      # {'x': 100, 'y': 200}
size = element.size              # {'width': 300, 'height': 50}
rect = element.rect              # {'x', 'y', 'width', 'height'}
```

## Checkbox and Radio Buttons

```python
checkbox = driver.find_element(By.ID, "agree-terms")

if not checkbox.is_selected():
    checkbox.click()   # check it

# Verify state
assert checkbox.is_selected()

# Radio buttons
radio = driver.find_element(By.XPATH, "//input[@type='radio' and @value='monthly']")
radio.click()
```

## Lab Exercise
1. Automate a login form: clear fields, type credentials, click submit, verify redirect
2. Interact with a form that has checkboxes, radio buttons, and a text area
3. Verify a button is disabled before form validation and enabled after
