---
id: "16_01_03"
title: "Locator Strategies"
course: "Selenium"
module: 1
module_title: "Selenium Fundamentals"
lesson: 3
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["By", "find_element", "find_elements", "ID", "NAME", "CLASS_NAME", "TAG_NAME", "LINK_TEXT", "PARTIAL_LINK_TEXT", "CSS_SELECTOR", "XPATH"]
prerequisites: []
lab_required: true
---

# Locator Strategies


## By Locator Types

```python
from selenium.webdriver.common.by import By

# By ID — fastest, most reliable
element = driver.find_element(By.ID, "username")

# By NAME
element = driver.find_element(By.NAME, "q")

# By CLASS_NAME (only first class)
elements = driver.find_elements(By.CLASS_NAME, "product-card")

# By TAG NAME
all_links = driver.find_elements(By.TAG_NAME, "a")

# By LINK TEXT (exact text of <a>)
driver.find_element(By.LINK_TEXT, "Sign In")

# By PARTIAL LINK TEXT
driver.find_element(By.PARTIAL_LINK_TEXT, "Sign")

# By CSS SELECTOR — flexible, fast
driver.find_element(By.CSS_SELECTOR, "#login-form input[type='email']")
driver.find_elements(By.CSS_SELECTOR, ".product-card > .price")

# By XPATH — most powerful, slowest
driver.find_element(By.XPATH, "//input[@id='username']")
driver.find_elements(By.XPATH, "//table[@class='data']//tr")
```

## find_element vs find_elements

```python
# find_element — returns ONE element; NoSuchElementException if not found
element = driver.find_element(By.ID, "header")

# find_elements — returns LIST; empty list if none found (no exception)
elements = driver.find_elements(By.CLASS_NAME, "item")
print(len(elements))    # 0 if not found
```

## Choosing the Right Locator

| Priority | Strategy | Why |
|---|---|---|
| 1 | `ID` | Unique, fast, semantic |
| 2 | `NAME` | Common on form fields |
| 3 | `CSS_SELECTOR` | Fast, readable, powerful |
| 4 | `XPATH` | When CSS can't reach it |
| 5 | `CLASS_NAME` | When unique enough |
| ✗ | `TAG_NAME` | Too broad |
| ✗ | `LINK_TEXT` | Breaks on text changes |

## Relative Locators (Selenium 4)

```python
from selenium.webdriver.support.relative_locator import locate_with

email = driver.find_element(By.ID, "email")

# Find password field BELOW email field
password = driver.find_element(
    locate_with(By.TAG_NAME, "input").below(email)
)

# More relative locators
.above(element)
.to_left_of(element)
.to_right_of(element)
.near(element)
```

## Lab Exercise
1. Locate 5 elements on a login page using 5 different By strategies
2. Use `find_elements` to count all links on a Wikipedia page
3. Demonstrate relative locators by finding a label next to an input
