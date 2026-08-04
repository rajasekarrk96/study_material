# Alerts Frames and Windows

> **Course**: Selenium | **Module**: Advanced Interactions | **Difficulty**: intermediate

---

```python
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Wait for alert to appear
wait = WebDriverWait(driver, 10)
wait.until(EC.alert_is_present())

alert = driver.switch_to.alert

# Alert types
alert.accept()    # OK button
alert.dismiss()   # Cancel button
print(alert.text) # alert message text

# Prompt (alert with input)
alert.send_keys("My answer")
alert.accept()
```

---

```python
# Switch to frame by index (0-based)
driver.switch_to.frame(0)

# Switch to frame by name or ID attribute
driver.switch_to.frame("iframe-name")

# Switch to frame by WebElement
iframe = driver.find_element(By.CSS_SELECTOR, "iframe.content-frame")
driver.switch_to.frame(iframe)

# Interact with content inside frame
driver.find_element(By.ID, "submit").click()

# Return to main page
driver.switch_to.default_content()

# Switch to parent frame (from nested frame)
driver.switch_to.parent_frame()
```

---

```python
# Open new tab
driver.execute_script("window.open('https://example.com', '_blank');")

# Get all window handles
handles = driver.window_handles
print(handles)   # ['handle1', 'handle2']

main_window = driver.current_window_handle

# Switch to new window
driver.switch_to.window(handles[-1])
print(driver.title)   # Title of new window

# Switch back
driver.switch_to.window(main_window)

# Close current window/tab
driver.close()
driver.switch_to.window(main_window)
```

---

1. Automate a scenario: click button → alert appears → type in prompt → verify result
2. Switch to an iframe, fill a form inside it, submit, switch back to main content
3. Open a link in a new tab, verify the URL, close it, and return to the original tab

---
