# Data Driven Testing

> **Course**: Selenium | **Module**: Testing Framework Integration | **Difficulty**: intermediate

---

```python
import pytest

LOGIN_DATA = [
    ("admin@test.com",   "Admin@123",    True,  "Dashboard"),
    ("editor@test.com",  "Editor@123",   True,  "Editor Panel"),
    ("wrong@test.com",   "wrongpass",    False, ""),
    ("admin@test.com",   "",             False, ""),
]

@pytest.mark.parametrize("username,password,expected_success,expected_title",
                         LOGIN_DATA, ids=["admin","editor","wrong-creds","empty-pass"])
def test_login_scenarios(driver, username, password, expected_success, expected_title):
    page = LoginPage(driver).open()
    page.login(username, password)

    if expected_success:
        assert HomePage(driver).get_title() == expected_title
    else:
        assert page.has_error()
```

---

```python
import csv

def load_csv(filepath):
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

test_data = load_csv("test_data/login_data.csv")

@pytest.mark.parametrize("data", test_data,
    ids=[d["test_id"] for d in test_data])
def test_login_csv(driver, data):
    page = LoginPage(driver).open()
    page.login(data["username"], data["password"])
    if data["expected"] == "success":
        assert HomePage(driver).is_logged_in()
    else:
        assert page.has_error()
```

---

```python
import openpyxl

def load_excel(filepath, sheet_name="Sheet1"):
    wb = openpyxl.load_workbook(filepath)
    ws = wb[sheet_name]
    headers = [cell.value for cell in ws[1]]
    return [
        dict(zip(headers, [cell.value for cell in row]))
        for row in ws.iter_rows(min_row=2)
    ]
```

---

```python
from faker import Faker
fake = Faker()

def generate_user():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "address": fake.address(),
    }

@pytest.mark.parametrize("user", [generate_user() for _ in range(5)])
def test_register_new_user(driver, user):
    page = RegistrationPage(driver).open()
    page.fill_form(**user)
    page.submit()
    assert page.success_message_displayed()
```

---

1. Load 20 product searches from a CSV and verify each search returns results
2. Parametrize a checkout test with different shipping addresses from an Excel file
3. Use Faker to generate and test 10 unique user registrations

---
