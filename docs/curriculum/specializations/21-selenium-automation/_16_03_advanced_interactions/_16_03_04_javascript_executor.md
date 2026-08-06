---
id: "16_03_04"
title: "JavaScript Executor"
course: "Selenium"
module: 3
module_title: "Advanced Interactions"
lesson: 4
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["execute_script", "execute_async_script", "scroll", "click", "getAttribute", "DOM", "shadow-DOM", "hidden-elements"]
prerequisites: []
lab_required: true
---

# JavaScript Executor


## execute_script

```python
# Pass arguments using `arguments[0]`, `arguments[1]`, etc.

# Scroll to element
element = driver.find_element(By.ID, "footer")
driver.execute_script("arguments[0].scrollIntoView(true);", element)

# Scroll to position
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.execute_script("window.scrollTo(0, 0);")   # scroll to top

# Click element (bypasses visibility check)
driver.execute_script("arguments[0].click();", element)

# Set value (bypasses read-only or custom inputs)
driver.execute_script("arguments[0].value = arguments[1];", element, "new value")

# Get value
val = driver.execute_script("return arguments[0].value;", element)
txt = driver.execute_script("return arguments[0].innerText;", element)

# Modify style
driver.execute_script("arguments[0].style.border = '2px solid red';", element)

# Remove attribute
driver.execute_script("arguments[0].removeAttribute('readonly');", element)
```

## execute_async_script

```python
# For async operations (AJAX, setTimeout, etc.)
result = driver.execute_async_script("""
    var callback = arguments[arguments.length - 1];
    setTimeout(function() {
        callback("done after 2s");
    }, 2000);
""")
print(result)   # "done after 2s"
```

## Shadow DOM

```python
# Access shadow root (Selenium 4)
host = driver.find_element(By.CSS_SELECTOR, "my-component")
shadow_root = driver.execute_script("return arguments[0].shadowRoot", host)
inner_el = shadow_root.find_element(By.CSS_SELECTOR, ".inner-button")
inner_el.click()
```

## Common Use Cases

```python
# Highlight element (for debugging)
def highlight(driver, element):
    driver.execute_script(
        "arguments[0].style.backgroundColor = 'yellow'; "
        "arguments[0].style.border = '2px solid red';",
        element
    )

# Get page dimensions
width  = driver.execute_script("return document.body.scrollWidth;")
height = driver.execute_script("return document.body.scrollHeight;")

# Check if element is in viewport
in_view = driver.execute_script("""
    var rect = arguments[0].getBoundingClientRect();
    return rect.top >= 0 && rect.bottom <= window.innerHeight;
""", element)
```

## Lab Exercise
1. Use JS executor to interact with a date-picker hidden behind CSS `display:none`
2. Scroll through a long page in 500px increments, scraping content at each step
3. Access and interact with a Shadow DOM component (e.g., a custom web component)
