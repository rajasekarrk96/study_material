# %% [markdown]
# # Topic 13: Advanced Pydantic Validation & Error Formatting Playground
# In this playground, you will learn how to write advanced validation rules.
# We will create a `ProductListing` schema that:
# 1. Uses `@field_validator` to reject names containing blacklisted words.
# 2. Uses `@model_validator` to ensure the sale price is strictly less than the original price.
# 3. Overrides the default FastAPI validation exception handler to return a clean error list.
#
# **How to use this:**
# 1. Open this file in VS Code.
# 2. Click **"Run Cell"** above each code block.

# %%
# 1. IMPORT LIBRARIES
from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field, field_validator, model_validator
import json

# %%
# 2. SCHEMAS WITH ADVANCED VALIDATION
class ProductListing(BaseModel):
    name: str = Field(..., min_length=3)
    original_price: float = Field(..., gt=0)
    sale_price: float = Field(..., gt=0)

    # 1. Field Validator: Check forbidden words
    @field_validator("name")
    @classmethod
    def check_clean_name(cls, val: str) -> str:
        blacklisted_words = ["fake", "spam", "scam"]
        for word in blacklisted_words:
            if word in val.lower():
                raise ValueError(f"Product name cannot contain forbidden word: '{word}'")
        return val

    # 2. Model Validator: Compare multiple fields
    # mode="after" ensures that field-level validations run first,
    # and we get a fully populated model instance.
    @model_validator(mode="after")
    def check_pricing(self) -> "ProductListing":
        if self.sale_price >= self.original_price:
            raise ValueError("The sale_price must be strictly less than the original_price")
        return self

# %%
# 3. APPLICATION SETUP
app = FastAPI(title="Advanced Validation Service")

# %% [markdown]
# ## Overriding the Validation Handler
# We catch `RequestValidationError` and extract only the field name and error message,
# returning a clean, custom JSON response with status code `400 Bad Request`.

# %%
# 4. CUSTOM VALIDATION EXCEPTION HANDLER
@app.exception_handler(RequestValidationError)
def custom_validation_exception_handler(request, exc: RequestValidationError):
    simplified_errors = []
    
    for error in exc.errors():
        # loc contains the path to the field, e.g., ("body", "sale_price")
        field_path = error.get("loc", [])
        field_name = "body"
        if len(field_path) > 1:
            field_name = ".".join(str(x) for x in field_path[1:])
            
        simplified_errors.append({
            "field": field_name,
            "message": error.get("msg", "Invalid value")
        })
        
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, # Changing default 422 to 400
        content={
            "title": "Validation Failure",
            "status": 400,
            "invalid_fields": simplified_errors
        }
    )

# %%
# 5. ROUTE DEFINITIONS
@app.post("/api/v1/products", status_code=status.HTTP_201_CREATED)
def add_product(product: ProductListing):
    return {
        "message": "Product listing created successfully",
        "product": product.model_dump()
    }

# %%
# 6. INITIALIZE TEST CLIENT
client = TestClient(app)

# %% [markdown]
# ### Test 1: Valid Product
# This should succeed with `201 Created`.

# %%
valid_payload = {
    "name": "Sony WH-1000XM4 Headphones",
    "original_price": 349.99,
    "sale_price": 278.00
}
response = client.post("/api/v1/products", json=valid_payload)
print(f"Status Code: {response.status_code}")
print(json.dumps(response.json(), indent=2))

# %% [markdown]
# ### Test 2: Invalid Name (Forbidden Word)
# We try to post a product named "Super Fake Watch".
# The field validator should reject it, and our handler should format the output.

# %%
invalid_name_payload = {
    "name": "Super Fake Watch",
    "original_price": 100.00,
    "sale_price": 50.00
}
response = client.post("/api/v1/products", json=invalid_name_payload)
print(f"Status Code: {response.status_code} (Should be 400)")
print(json.dumps(response.json(), indent=2))

# %% [markdown]
# ### Test 3: Invalid Pricing (Sale Price >= Original Price)
# We set the sale price higher than the original price.
# The model validator should reject it.

# %%
invalid_pricing_payload = {
    "name": "Mechanical Keyboard",
    "original_price": 100.00,
    "sale_price": 120.00 # Sale price is higher!
}
response = client.post("/api/v1/products", json=invalid_pricing_payload)
print(f"Status Code: {response.status_code} (Should be 400)")
print(json.dumps(response.json(), indent=2))
