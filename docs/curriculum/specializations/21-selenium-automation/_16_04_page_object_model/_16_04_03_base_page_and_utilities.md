---
id: "16_04_03"
title: "Base Page and Utilities"
course: "Selenium"
module: 4
module_title: "Test Architecture"
lesson: 3
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["BasePage", "utility", "screenshot-on-failure", "scroll", "highlight", "config", "DriverFactory", "conftest"]
prerequisites: []
lab_required: true
---

# Base Page and Utilities


## Enhanced Base Page

```python
# pages/base_page.py
import time, os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    def open(self, url: str = None):
        target = url or getattr(self, "URL", "")
        self.driver.get(target)
        return self

    # ── Finding ──────────────────────────────────────────────
    def find(self, locator, timeout=None):
        w = WebDriverWait(self.driver, timeout or self.DEFAULT_TIMEOUT)
        return w.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def is_present(self, locator, timeout=3) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    # ── Interacting ───────────────────────────────────────────
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text: str):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    def select_option(self, locator, text: str):
        from selenium.webdriver.support.ui import Select
        Select(self.find(locator)).select_by_visible_text(text)

    # ── Reading ───────────────────────────────────────────────
    def get_text(self, locator) -> str:
        return self.find(locator).text

    def get_attr(self, locator, attribute: str) -> str:
        return self.find(locator).get_attribute(attribute)

    # ── Utilities ─────────────────────────────────────────────
    def scroll_to(self, locator):
        el = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", el)

    def scroll_by(self, px: int):
        self.driver.execute_script(f"window.scrollBy(0, {px});")

    def highlight(self, locator, color="yellow"):
        el = self.find(locator)
        self.driver.execute_script(
            f"arguments[0].style.backgroundColor='{color}'; "
            f"arguments[0].style.border='2px solid red';", el
        )

    def screenshot(self, name: str = None):
        fname = name or f"screenshot_{int(time.time())}.png"
        self.driver.save_screenshot(fname)
        return fname
```

## conftest.py — Pytest Fixtures

```python
# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def driver():
    opts = Options()
    opts.add_argument("--start-maximized")
    # opts.add_argument("--headless")
    drv = webdriver.Chrome(options=opts)
    drv.implicitly_wait(0)   # use explicit waits only
    yield drv
    drv.quit()

@pytest.fixture(autouse=True)
def screenshot_on_failure(driver, request):
    yield
    if request.node.rep_call.failed:
        test_name = request.node.name
        driver.save_screenshot(f"failures/{test_name}.png")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
```

## Lab Exercise
1. Add `wait_for_url_contains(partial_url)` and `wait_for_title_contains(text)` to BasePage
2. Configure `conftest.py` to take a screenshot on EVERY failure automatically
3. Add `DriverFactory.create(browser: str, headless: bool)` that supports Chrome, Firefox, Edge
