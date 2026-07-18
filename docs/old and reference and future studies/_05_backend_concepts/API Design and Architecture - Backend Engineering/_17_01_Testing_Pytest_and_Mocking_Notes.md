# Module 9: Testing
## Topic 17: Testing with Pytest & Mocking

---

### 1. The Big Picture

#### Why We Test
In an enterprise, you cannot deploy code to production based on "it works on my machine." **Automated Testing** is the safety net that ensures:
1. New features do not break existing functionality (Regression Testing).
2. Code is designed cleanly (hard-to-test code is usually poorly designed code).
3. The team can deploy changes to production multiple times a day with confidence.

#### The Testing Pyramid

```
       ▲
      / \      E2E / System Tests (Slow, expensive, covers entire flow)
     /   \
    /     \    Integration Tests (Verifies database, HTTP, and services work together)
   /       \
  /         \  Unit Tests (Fast, cheap, tests a single function/class in isolation)
 ─────────────
```

* **Unit Tests:** Test a single unit of code (e.g., a service method) in isolation. External dependencies (like databases or APIs) are **mocked**.
* **Integration Tests:** Test how multiple components work together (e.g., a route handler interacting with a real database).
* **End-to-End (E2E) Tests:** Test the entire system from the client's perspective (e.g., simulating a user clicking a button and checking the database).

---

### 2. Testing with Pytest
**Pytest** is the standard testing framework for Python. It makes it easy to write small, readable tests.

#### Core Pytest Concepts
* **Test Discovery:** Pytest automatically finds and runs files named `test_*.py` or `*_test.py`. Inside those files, it runs functions prefixed with `test_`.
* **Assertions:** Instead of complex methods, Pytest uses Python's native `assert` statement. E.g., `assert value == 42`.
* **Fixtures:** Reusable setup and teardown code. E.g., creating a clean database session before each test.

---

### 3. What is Mocking?
**Mocking** is replacing a real dependency (like a database connection or a Stripe payment client) with a simulated object that returns predetermined responses.
* **Why Mock?**
  * **Speed:** Querying a real database or sending an email takes seconds. Running 1,000 mocked tests takes milliseconds.
  * **Consistency:** Tests shouldn't fail because Google's servers are temporarily down.
  * **Safety:** You don't want to charge a real credit card during a test run!

---

### 4. Python Example: Writing a FastAPI Test with Pytest
We use Pytest's fixtures and FastAPI's `TestClient` to write clean integration tests.

```python
import pytest
from fastapi.testclient import TestClient
from main import app # Import your FastAPI app

@pytest.fixture
def client():
    # Setup: Create a TestClient instance
    with TestClient(app) as c:
        yield c
    # Teardown: Code here runs after the test finishes

def test_create_user_success(client):
    # Act: Make request
    payload = {"name": "Michael Scott", "email": "michael@dundermifflin.com"}
    response = client.post("/api/v1/users", json=payload)
    
    # Assert: Verify response
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Michael Scott"
    assert "id" in data
```

---

### 5. Hands-on Workout & Assessment

#### Part A: Testing Design Challenge
You are writing a unit test for a `PaymentService.charge_customer()` method. This method:
1. Fetches the customer's Stripe ID from the database.
2. Calls Stripe's API (`stripe.Charge.create()`) using a secret key.
3. If successful, updates the order status to "Paid" in the database.

- Which parts of this method should be **mocked** in a unit test?
- Write a short description of how you would set up the mock for the Stripe API call.

#### Part B: Quiz
1. What is a Pytest fixture?
   A. A database table constraint.
   B. A reusable function that provides setup (and optional teardown) code for tests.
   C. A tool to format code.
   D. A test case that never changes.
2. Why do we prefer unit tests over E2E tests for testing complex business logic edge cases?
   A. E2E tests are not secure.
   B. Unit tests are extremely fast, cheap to run, and allow isolating the exact logic without setting up the entire application stack.
   C. Unit tests do not require writing code.
   D. E2E tests cannot test edge cases.
3. What happens if you run a test file that is not named with a `test_` prefix or `_test` suffix in Pytest?
   A. Pytest will raise a syntax error.
   B. Pytest will ignore the file during test discovery.
   C. Pytest will delete the file.
   D. The test will run but always pass.

---

### 6. Progress Tracker

* **Module 9: Testing:** 0%
* **Topics Completed:** 0/1
* **Coding Exercises:** 0/0
* **Quiz Score:** N/A
* **API Design Challenge Score:** N/A
* **Backend Score:** 0 / 100

---
