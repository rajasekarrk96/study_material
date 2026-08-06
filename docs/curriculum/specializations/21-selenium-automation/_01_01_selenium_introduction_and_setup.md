# Selenium Introduction and Setup

> **Course**: Selenium | **Module**: Selenium Fundamentals | **Difficulty**: beginner

---

**Selenium** is an open-source browser automation framework that allows you to programmatically control web browsers — click buttons, fill forms, extract data, and validate UI behaviour.

### Selenium Suite Components

| Tool | Purpose |
|---|---|
| **Selenium WebDriver** | Core API to control browsers |
| **Selenium Grid** | Distributed test execution across machines/browsers |
| **Selenium IDE** | Record & playback browser extension (no-code) |

---

```bash
# Install Selenium
pip install selenium

# Selenium 4.6+ includes Selenium Manager (auto-downloads drivers!)
# No manual chromedriver install needed for Chrome/Firefox/Edge
```

---

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Chrome (headless option)
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # uncomment for headless

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.google.com")
    print(driver.title)   # Google

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.submit()
    time.sleep(2)
    print(driver.title)
finally:
    driver.quit()   # always quit to free resources
```

---

```python
# Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
opts = ChromeOptions()
opts.add_argument("--start-maximized")
opts.add_argument("--disable-notifications")
opts.add_experimental_option("detach", True)   # keep browser open after script
driver = webdriver.Chrome(options=opts)

# Firefox
from selenium.webdriver.firefox.options import Options as FirefoxOptions
opts = FirefoxOptions()
driver = webdriver.Firefox(options=opts)

# Edge
driver = webdriver.Edge()
```

---

1. Set up a virtual environment, install selenium, verify `selenium.__version__`
2. Write a script that opens `https://example.com`, prints the title and current URL
3. Navigate to Wikipedia, search for "Python programming", print the first paragraph

---
