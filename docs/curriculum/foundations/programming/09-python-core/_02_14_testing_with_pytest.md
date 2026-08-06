---
id: "02_14_02"
title: "Testing with Pytest"
course: "Python"
module: 14
module_title: "Debugging and Testing"
lesson: 2
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["pytest", "assert", "fixture", "parametrize", "mock", "monkeypatch", "conftest", "coverage", "TDD", "hypothesis"]
prerequisites: []
lab_required: true
---

# Testing with Pytest


## Pytest Basics

```python
# test_calculator.py
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3

def test_add_negative():
    assert add(-1, -2) == -3

def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)
```

```bash
pytest                    # run all tests
pytest test_calculator.py # specific file
pytest -v                 # verbose
pytest -k "add"           # run tests matching pattern
pytest --tb=short         # shorter traceback
pytest -x                 # stop on first failure
```

## Fixtures

```python
import pytest

@pytest.fixture
def sample_user():
    return {"id": 1, "name": "Raja", "email": "raja@test.com"}

@pytest.fixture
def db_connection():
    conn = create_test_db()
    yield conn          # test runs here
    conn.close()        # teardown

def test_user_name(sample_user):
    assert sample_user["name"] == "Raja"

def test_user_in_db(db_connection, sample_user):
    db_connection.insert(sample_user)
    result = db_connection.find(1)
    assert result["email"] == sample_user["email"]
```

## Parametrize

```python
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (100, -50, 50),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
```

## Mocking

```python
from unittest.mock import Mock, patch, MagicMock

def test_send_email(monkeypatch):
    called_with = []

    def fake_send(to, subject, body):
        called_with.append((to, subject, body))
        return True

    monkeypatch.setattr("myapp.email.send", fake_send)
    result = register_user("user@test.com")

    assert result.success
    assert len(called_with) == 1
    assert called_with[0][0] == "user@test.com"

# patch as decorator
@patch("requests.get")
def test_api_call(mock_get):
    mock_get.return_value.json.return_value = {"data": [1, 2, 3]}
    result = my_api_client.fetch()
    assert result == [1, 2, 3]
    mock_get.assert_called_once_with("https://api.example.com/data")
```

## Coverage

```bash
pip install pytest-cov

pytest --cov=myapp --cov-report=html tests/
# Opens htmlcov/index.html with per-line coverage
```

## Property-Based Testing with Hypothesis

```python
from hypothesis import given, strategies as st

@given(st.integers(), st.integers())
def test_add_commutative(a, b):
    assert add(a, b) == add(b, a)   # tests 100 random pairs

@given(st.lists(st.integers(), min_size=1))
def test_max_in_list(lst):
    result = max(lst)
    assert result in lst
    assert all(result >= x for x in lst)
```

## Lab Exercise
1. Write unit tests for a `BankAccount` class with 100% coverage
2. Use `pytest.fixture` with database setup/teardown and test CRUD operations
3. Write property-based tests for a `sort()` function using Hypothesis
