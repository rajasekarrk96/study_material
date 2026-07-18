# Module 6: Validation, Error Handling, Exceptions, Best Practices
## Topic 13: Advanced Pydantic Validation & Error Formatting

---

### 1. The Big Picture

#### What is Advanced Validation?
While basic types (like `str`, `int`, `EmailStr`) catch simple errors, real-world applications require complex business validation rules. E.g.,:
* "The discount price cannot be greater than the original price."
* "The password must contain at least one uppercase letter, one number, and one special character."
* "A phone number must match a specific international format."

Pydantic v2 provides powerful decorators—**`@field_validator`** and **`@model_validator`**—to implement these rules cleanly in your data layer.

---

### 2. Field Validators vs. Model Validators

#### 1. Field Validators (`@field_validator`)
Used to validate a single, specific field.
* *Example:* Checking if a username contains only alphanumeric characters.
```python
from pydantic import BaseModel, field_validator

class UserRegister(BaseModel):
    username: str

    @field_validator("username")
    @classmethod
    def validate_username(cls, value: str) -> str:
        if not value.isalnum():
            raise ValueError("Username must be alphanumeric")
        return value
```

#### 2. Model Validators (`@model_validator`)
Used to validate relationships between multiple fields (cross-field validation).
* *Example:* Verifying that `password` and `confirm_password` match, or checking that `discount_price` is less than `price`.
```python
from pydantic import BaseModel, model_validator

class ProductCreate(BaseModel):
    price: float
    discount_price: float

    @model_validator(mode="after")
    def check_discount(self) -> "ProductCreate":
        if self.discount_price >= self.price:
            raise ValueError("Discount price must be less than the regular price")
        return self
```

---

### 3. Customizing FastAPI Validation Error Format
By default, when validation fails, FastAPI returns a detailed but sometimes verbose `422 Unprocessable Entity` response. 
In production, you often want to simplify this format or match your team's standard error envelope (like RFC 7807). We can achieve this by overriding the default **`RequestValidationError`** handler.

```python
from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        errors.append({
            "field": ".".join(map(str, error["loc"][1:])), # Extract field name
            "message": error["msg"]
        })
        
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, # Change from 422 to 400
        content={
            "title": "Validation Failed",
            "status": 400,
            "errors": errors
        }
    )
```

---

### 4. Hands-on Workout & Assessment

#### Part A: API Design Challenge (Complex Validation)
You are building an API for a **Hotel Booking System**. The request body contains `room_id`, `check_in_date`, and `check_out_date`.
- Write a Pydantic model `BookingRequest`.
- Write a model validator to ensure that `check_out_date` is at least one day after `check_in_date`.
- Write a field validator to ensure `check_in_date` is not in the past.

#### Part B: Quiz
1. Which Pydantic decorator is used to validate relationships between multiple fields?
   A. `@field_validator`
   B. `@model_validator`
   C. `@validator`
   D. `@check_fields`
2. What status code does FastAPI return by default when a Pydantic validation fails?
   A. 400 Bad Request
   B. 401 Unauthorized
   C. 422 Unprocessable Entity
   D. 500 Internal Server Error
3. Why is it a best practice to write class methods for `@field_validator` in Pydantic?
   A. It makes the code execute faster.
   B. Pydantic v2 requires `@field_validator` to be a `@classmethod`.
   C. It connects to the database.
   D. It allows the validator to modify the database.

---

### 5. Progress Tracker

* **Module 6: Validation, Error Handling, Exceptions:** 0%
* **Topics Completed:** 0/1
* **Coding Exercises:** 0/0
* **Quiz Score:** N/A
* **API Design Challenge Score:** N/A
* **Backend Score:** 0 / 100

---
