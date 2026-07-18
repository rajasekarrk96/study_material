# %% [markdown]
# # Topic 17: Testing with Pytest & Mocking Playground
# In this playground, you will learn how to write unit tests and mock dependencies.
# We will test an `OrderService` that has two external dependencies:
# 1. `InventoryRepository` (Database access)
# 2. `PaymentGateway` (Third-party API, e.g., Stripe)
#
# We will use `pytest` to write the tests and `unittest.mock.Mock` to mock the dependencies,
# ensuring our tests run in milliseconds and never make real API or database calls.
#
# **How to use this:**
# 1. Open this file in VS Code.
# 2. Click **"Run Cell"** above each code block.

# %%
# 1. INSTALL DEPENDENCIES
# We install pytest.
%pip install pytest

# %%
# 2. IMPORT LIBRARIES
from unittest.mock import Mock
import pytest

# %%
# 3. DEFINE CLASSES TO TEST

class InventoryRepository:
    def get_stock(self, product_id: int) -> int:
        # Pretend this queries a real PostgreSQL database
        raise NotImplementedError("Database connection not configured")

    def deduct_stock(self, product_id: int, quantity: int):
        raise NotImplementedError("Database connection not configured")

class PaymentGateway:
    def charge(self, amount: int, card_token: str) -> bool:
        # Pretend this makes an HTTPS call to Stripe
        raise NotImplementedError("Stripe API credentials missing")

class OrderService:
    def __init__(self, inventory_repo: InventoryRepository, payment_gateway: PaymentGateway):
        self.inventory_repo = inventory_repo
        self.payment_gateway = payment_gateway

    def place_order(self, product_id: int, quantity: int, price: int, card_token: str) -> dict:
        # 1. Check stock
        stock = self.inventory_repo.get_stock(product_id)
        if stock < quantity:
            raise ValueError("Insufficient stock")
            
        # 2. Charge card
        total_amount = price * quantity
        charge_success = self.payment_gateway.charge(total_amount, card_token)
        if not charge_success:
            raise ValueError("Payment failed")
            
        # 3. Deduct stock
        self.inventory_repo.deduct_stock(product_id, quantity)
        
        return {"status": "success", "product_id": product_id, "quantity": quantity}

# %% [markdown]
# ## Writing the Unit Tests
# We mock `InventoryRepository` and `PaymentGateway` using `Mock()`.
# We configure these mocks to return specific values (e.g., stock levels, payment success).

# %%
# 4. TEST DEFINITIONS

def test_place_order_success():
    # Arrange: Create mocks
    mock_inventory = Mock(spec=InventoryRepository)
    mock_payment = Mock(spec=PaymentGateway)
    
    # Configure mock behaviors
    mock_inventory.get_stock.return_value = 10  # Pretend we have 10 items in stock
    mock_payment.charge.return_value = True     # Pretend payment succeeds
    
    # Instantiate service with injected mocks
    service = OrderService(inventory_repo=mock_inventory, payment_gateway=mock_payment)
    
    # Act
    result = service.place_order(product_id=101, quantity=2, price=1000, card_token="tok_visa")
    
    # Assert
    assert result["status"] == "success"
    assert result["quantity"] == 2
    
    # Verify that our code actually called the dependencies correctly!
    mock_inventory.get_stock.assert_called_once_with(101)
    mock_payment.charge.assert_called_once_with(2000, "tok_visa")
    mock_inventory.deduct_stock.assert_called_once_with(101, 2)

def test_place_order_insufficient_stock():
    # Arrange: Create mocks
    mock_inventory = Mock(spec=InventoryRepository)
    mock_payment = Mock(spec=PaymentGateway)
    
    # Configure mock: only 1 item in stock, but client wants 5
    mock_inventory.get_stock.return_value = 1
    
    service = OrderService(inventory_repo=mock_inventory, payment_gateway=mock_payment)
    
    # Act & Assert: Expect a ValueError to be raised
    with pytest.raises(ValueError, match="Insufficient stock"):
        service.place_order(product_id=101, quantity=5, price=1000, card_token="tok_visa")
        
    # Verify that we NEVER charged the card because stock check failed
    mock_payment.charge.assert_not_called()
    mock_inventory.deduct_stock.assert_not_called()

# %% [markdown]
# ## Running Pytest Programmatically
# Normally, you run `pytest` in the terminal. In this playground, we can run it programmatically
# using `pytest.main()` and see the test results output directly below!

# %%
# 5. RUN THE TESTS
# We pass the name of this file (or run it inline by passing the test functions)
# For simplicity, we run pytest on our defined test functions.
import sys

class TestSuite:
    def run_tests(self):
        # Run pytest programmatically on the current module
        print("--- Running Pytest Suite ---")
        pytest.main(["-v", "-p", "no:cacheprovider", __file__])

TestSuite().run_tests()
