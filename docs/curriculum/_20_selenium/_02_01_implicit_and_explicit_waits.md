# Implicit and Explicit Waits

> **Course**: Selenium | **Module**: Waits and Synchronisation | **Difficulty**: intermediate

---

Modern web apps load content dynamically (AJAX, React, Vue). Without waits, Selenium may try to interact with elements that haven't appeared yet, causing `NoSuchElementException` or `ElementNotInteractableException`.

---

```python
# Set once — applies to ALL find_element calls for the session
driver.implicitly_wait(10)   # wait up to 10 seconds for element to appear

# Selenium polls the DOM at ~500ms intervals
# Use sparingly — slows down tests when elements genuinely don't exist
```

---

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, timeout=10)

# Wait for element to be visible
element = wait.until(
    EC.visibility_of_element_located((By.ID, "success-message"))
)

# Wait for element to be clickable (visible AND enabled)
btn = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#submit-btn"))
)
btn.click()

# Wait for element to disappear
wait.until(
    EC.invisibility_of_element_located((By.CLASS_NAME, "loading-spinner"))
)
```

---

```python
from selenium.webdriver.support import expected_conditions as EC

EC.title_contains("Dashboard")
EC.title_is("Home Page")
EC.url_contains("/dashboard")
EC.url_to_be("https://example.com/dashboard")

EC.presence_of_element_located(locator)   # in DOM, may not be visible
EC.visibility_of_element_located(locator)  # visible (display != none)
EC.element_to_be_clickable(locator)        # visible AND enabled
EC.invisibility_of_element_located(locator) # hidden/removed

EC.presence_of_all_elements_located(locator)  # returns list
EC.text_to_be_present_in_element(locator, "text")
EC.element_to_be_selected(element)
EC.staleness_of(element)    # element removed from DOM (after navigation)
EC.number_of_windows_to_be(2)
EC.alert_is_present()
```

---

```python
def element_has_css_class(locator, css_class):
    def condition(driver):
        element = driver.find_element(*locator)
        classes = element.get_attribute("class")
        return css_class in classes.split()
    return condition

wait.until(element_has_css_class((By.ID, "status"), "active"))
```

---

| | Implicit | Explicit |
|---|---|---|
| Scope | All find_element calls | Specific condition |
| Flexibility | Low | High |
| Timeout | Single global | Per-wait |
| Conditions | Presence only | Any condition |
| Recommendation | Avoid mixing with explicit | Preferred |

> ⚠️ Never mix implicit and explicit waits — leads to unpredictable timeouts.

---

1. Use `element_to_be_clickable` to wait for a button that appears after 3 seconds
2. Wait for a loading spinner to disappear before asserting page content
3. Write a custom condition that checks element text matches a regex

---
