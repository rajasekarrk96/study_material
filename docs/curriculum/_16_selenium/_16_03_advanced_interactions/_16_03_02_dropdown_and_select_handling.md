---
id: "16_03_02"
title: "Dropdown and Select Handling"
course: "Selenium"
module: 3
module_title: "Advanced Interactions"
lesson: 2
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["Select", "select_by_value", "select_by_visible_text", "select_by_index", "deselect", "options", "all_selected_options", "multi-select"]
prerequisites: []
lab_required: true
---

# Dropdown and Select Handling


## HTML Select Dropdown

```python
from selenium.webdriver.support.ui import Select

dropdown = driver.find_element(By.ID, "country-select")
select = Select(dropdown)

# Select by visible text
select.select_by_visible_text("India")

# Select by value attribute
select.select_by_value("IN")

# Select by index (0-based)
select.select_by_index(2)

# Get all options
for option in select.options:
    print(option.text, option.get_attribute("value"))

# Get currently selected option
print(select.first_selected_option.text)
print(select.all_selected_options)   # list (for multi-select)
```

## Multi-Select Dropdown

```python
select = Select(driver.find_element(By.ID, "languages"))

select.select_by_visible_text("Python")
select.select_by_visible_text("Java")
select.select_by_visible_text("JavaScript")

# Deselect
select.deselect_by_visible_text("Java")
select.deselect_all()

print([opt.text for opt in select.all_selected_options])
```

## Custom Dropdown (not `<select>`)

Many modern UI frameworks use `<div>` or `<ul>` based dropdowns.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Click to open
driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle").click()

# Wait for options to appear
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".dropdown-menu")))

# Click specific option
options = driver.find_elements(By.CSS_SELECTOR, ".dropdown-menu li a")
for option in options:
    if option.text == "Settings":
        option.click()
        break
```

## Lab Exercise
1. Select a date from three separate dropdowns (day, month, year)
2. Verify all options are present in a dropdown and select each one in sequence
3. Handle a Bootstrap dropdown (custom div-based) and select a value
