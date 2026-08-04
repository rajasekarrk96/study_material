# Page Object Model Pattern

> **Course**: Selenium | **Module**: Test Architecture | **Difficulty**: intermediate

---

POM separates **test logic** from **page interaction code**:

- **Without POM**: Locators scattered throughout tests → fragile
- **With POM**: Each page has one class → change locator in one place

---

```
tests/
    test_login.py
    test_checkout.py
pages/
    base_page.py
    login_page.py
    home_page.py
    checkout_page.py
conftest.py
```

---

```python
# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    URL = ""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        return self

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def is_displayed(self, locator):
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False
```

---

```python
# pages/login_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    URL = "https://myapp.com/login"

    # Locators (as class attributes)
    USERNAME_INPUT  = (By.ID, "username")
    PASSWORD_INPUT  = (By.ID, "password")
    SUBMIT_BUTTON   = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE   = (By.CLASS_NAME, "error-alert")
    FORGOT_PASSWORD = (By.LINK_TEXT, "Forgot Password?")

    # Actions
    def login(self, username: str, password: str):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)
        return self   # fluent interface

    def get_error(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def has_error(self) -> bool:
        return self.is_displayed(self.ERROR_MESSAGE)
```

---

```python
# tests/test_login.py
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_valid_login(driver):
    login = LoginPage(driver).open()
    login.login("user@test.com", "password123")

    home = HomePage(driver)
    assert home.is_logged_in()
    assert home.get_username() == "user@test.com"

def test_invalid_login(driver):
    login = LoginPage(driver).open()
    login.login("wrong@test.com", "wrongpass")

    assert login.has_error()
    assert "Invalid credentials" in login.get_error()
```

---

1. Build POM for a 3-page e-commerce flow: Home → Product → Cart
2. Add a `navigate_to()` method to BasePage that waits for the URL to change
3. Implement a `DriverFactory` that creates Chrome/Firefox/Edge drivers by config

---
