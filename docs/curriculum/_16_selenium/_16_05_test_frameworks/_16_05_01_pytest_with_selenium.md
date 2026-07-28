---
id: "16_05_01"
title: "Pytest with Selenium"
course: "Selenium"
module: 5
module_title: "Testing Framework Integration"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["pytest", "fixture", "conftest", "mark", "parametrize", "assert", "setup", "teardown", "allure", "scope"]
prerequisites: []
lab_required: true
---

# Pytest with Selenium


## Test Structure

```python
# tests/test_login.py
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

class TestLogin:
    def test_valid_credentials(self, driver, base_url):
        page = LoginPage(driver)
        page.open(base_url + "/login")
        page.login("admin@test.com", "password123")
        assert HomePage(driver).is_logged_in()

    def test_empty_username(self, driver, base_url):
        page = LoginPage(driver)
        page.open(base_url + "/login")
        page.login("", "password123")
        assert page.has_error()
        assert "Username is required" in page.get_error()

    @pytest.mark.skip(reason="Feature in development")
    def test_sso_login(self, driver):
        ...
```

## Fixtures Hierarchy

```python
# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture(scope="session")           # once per session
def driver():
    drv = webdriver.Chrome()
    yield drv
    drv.quit()

@pytest.fixture(scope="module")            # once per module
def authenticated_driver(driver, base_url):
    from pages.login_page import LoginPage
    LoginPage(driver).open(base_url + "/login").login("user", "pass")
    yield driver
    driver.delete_all_cookies()

@pytest.fixture(scope="function")          # default — before each test
def fresh_page(driver):
    driver.delete_all_cookies()
    driver.get("about:blank")
    yield

@pytest.fixture
def base_url():
    return "https://staging.myapp.com"
```

## Markers

```python
# pytest.ini or pyproject.toml
[pytest]
markers =
    smoke: Quick sanity check tests
    regression: Full regression suite
    slow: Tests taking >30 seconds

# Usage
@pytest.mark.smoke
def test_homepage_loads(driver): ...

@pytest.mark.regression
@pytest.mark.slow
def test_full_checkout(driver): ...

# Run only smoke tests
# pytest -m smoke
```

## Allure Reporting

```bash
pip install allure-pytest

pytest --alluredir=allure-results tests/
allure serve allure-results
```

```python
import allure

@allure.title("User can login with valid credentials")
@allure.description("Validates the happy path for user authentication")
@allure.feature("Authentication")
@allure.severity(allure.severity_level.CRITICAL)
def test_login(driver):
    with allure.step("Open login page"):
        driver.get("https://myapp.com/login")
    with allure.step("Enter credentials"):
        driver.find_element(By.ID, "username").send_keys("user@test.com")
    with allure.step("Submit form"):
        driver.find_element(By.ID, "submit").click()
    allure.attach(driver.get_screenshot_as_png(),
                  name="screenshot", attachment_type=allure.attachment_type.PNG)
```

## Lab Exercise
1. Create a full test suite for a registration flow with 5 test cases using class-based tests
2. Set up `scope="session"` driver with login in `autouse` fixture
3. Add Allure report generation with screenshots on each test step
