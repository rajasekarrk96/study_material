# Page Load Strategies

> **Course**: Selenium | **Module**: Waits and Synchronisation | **Difficulty**: intermediate

---

```python
from selenium.webdriver.chrome.options import Options

options = Options()

# NORMAL (default) — waits for full page load (document.readyState == "complete")
options.page_load_strategy = "normal"

# EAGER — waits for interactive (DOM ready, resources may still load)
options.page_load_strategy = "eager"

# NONE — returns immediately after initial request
options.page_load_strategy = "none"

driver = webdriver.Chrome(options=options)
```

---

```python
driver.set_page_load_timeout(30)     # max seconds to wait for page to load
driver.set_script_timeout(10)        # max seconds for execute_async_script
driver.implicitly_wait(5)            # implicit wait for element presence

# Via options (Selenium 4 preferred)
from selenium.webdriver.chrome.options import Options
options = Options()
options.set_capability("timeouts", {
    "pageLoad": 30000,   # milliseconds
    "script": 10000,
    "implicit": 0,
})
```

---

```python
def wait_for_ajax(driver, timeout=30):
    """Wait until jQuery AJAX requests complete"""
    from selenium.webdriver.support.wait import WebDriverWait
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script("return jQuery.active == 0")
    )

def wait_for_network_idle(driver, timeout=30):
    """Wait for React/Vue single-page apps to finish rendering"""
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script(
            "return document.readyState === 'complete'"
        )
    )
```

---

1. Compare page load times for `normal`, `eager`, `none` strategies on a heavy website
2. Write a `navigate_and_wait(driver, url)` that uses `none` strategy then polls for readiness
3. Handle a page that loads content via AJAX 2 seconds after initial DOM load

---
