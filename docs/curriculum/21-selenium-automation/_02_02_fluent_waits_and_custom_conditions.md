# Fluent Waits and Custom Conditions

> **Course**: Selenium | **Module**: Waits and Synchronisation | **Difficulty**: advanced

---

`FluentWait` gives fine-grained control over polling frequency and which exceptions to ignore.

```python
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from datetime import timedelta

# FluentWait via WebDriverWait parameters
wait = WebDriverWait(
    driver,
    timeout=30,
    poll_frequency=0.5,                  # check every 500ms (default: 500ms)
    ignored_exceptions=[
        NoSuchElementException,
        StaleElementReferenceException,  # ignore stale elements during polling
    ]
)

element = wait.until(
    EC.visibility_of_element_located((By.ID, "dynamic-content"))
)
```

---

```python
# Wait for element count to be at least N
wait.until(lambda d: len(d.find_elements(By.CLASS_NAME, "result-item")) >= 5)

# Wait for element's text to contain expected value
wait.until(lambda d:
    "success" in d.find_element(By.ID, "status").text.lower()
)

# Wait for a specific attribute value
wait.until(lambda d:
    d.find_element(By.ID, "progress").get_attribute("aria-valuenow") == "100"
)

# Wait for URL to change
original_url = driver.current_url
driver.find_element(By.ID, "navigate-btn").click()
wait.until(lambda d: d.current_url != original_url)
```

---

```python
import time
from functools import wraps
from selenium.common.exceptions import StaleElementReferenceException

def retry_on_stale(retries=3, delay=0.5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except StaleElementReferenceException:
                    if attempt == retries - 1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@retry_on_stale(retries=3)
def click_element(driver, locator):
    driver.find_element(*locator).click()
```

---

```python
def wait_for_page_load(driver, timeout=30):
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

def wait_for_angular(driver, timeout=30):
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script(
            "return window.getAllAngularTestabilities && "
            "window.getAllAngularTestabilities().every(t => t.isStable())"
        )
    )
```

---

1. Implement a `wait_for_ajax(driver)` function that polls until no jQuery AJAX requests are pending
2. Use FluentWait to ignore `StaleElementReferenceException` while waiting for a result table
3. Build a `wait_for_text_change(element, original_text)` custom condition

---
