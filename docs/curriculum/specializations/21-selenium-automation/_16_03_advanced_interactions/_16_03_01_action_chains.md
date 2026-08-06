---
id: "16_03_01"
title: "Action Chains"
course: "Selenium"
module: 3
module_title: "Advanced Interactions"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["ActionChains", "click_and_hold", "drag_and_drop", "move_to_element", "hover", "context_click", "double_click", "key_down", "perform"]
prerequisites: []
lab_required: true
---

# Action Chains


## ActionChains Overview

`ActionChains` build a sequence of low-level browser actions (mouse movements, clicks, key presses) that are performed in order.

```python
from selenium.webdriver.common.action_chains import ActionChains

action = ActionChains(driver)
```

## Mouse Actions

```python
element = driver.find_element(By.ID, "target")

# Hover (mouse over)
action.move_to_element(element).perform()

# Click types
action.click(element).perform()
action.double_click(element).perform()
action.context_click(element).perform()   # right-click

# Click and hold (drag start)
action.click_and_hold(element).perform()
action.release().perform()

# Move by offset from element
action.move_to_element_with_offset(element, 10, 20).perform()

# Move by offset from current position
action.move_by_offset(100, 0).perform()
```

## Drag and Drop

```python
source = driver.find_element(By.ID, "drag-item")
target = driver.find_element(By.ID, "drop-zone")

# Method 1: drag_and_drop
action.drag_and_drop(source, target).perform()

# Method 2: manual (more reliable for some apps)
action.click_and_hold(source)       .move_to_element(target)       .release()       .perform()
```

## Keyboard Actions

```python
from selenium.webdriver.common.keys import Keys

# Key combinations
action.key_down(Keys.CONTROL)       .send_keys("a")       .key_up(Keys.CONTROL)       .perform()   # Ctrl+A

# Type in focused element
action.send_keys("Hello World").perform()

# Tab through form fields
action.send_keys(Keys.TAB).perform()
```

## Chaining Actions

```python
# Hover over menu, wait for submenu, click submenu item
menu = driver.find_element(By.ID, "nav-products")
submenu_item = driver.find_element(By.ID, "nav-laptops")

ActionChains(driver)     .move_to_element(menu)     .pause(0.5)     .move_to_element(submenu_item)     .click()     .perform()
```

## Lab Exercise
1. Automate a drag-and-drop kanban board (move card from "To Do" to "In Progress")
2. Open a dropdown navigation menu by hovering, then click a submenu link
3. Select all text in an input field using keyboard shortcut and replace it
