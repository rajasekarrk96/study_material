# Capstone E-Commerce Automation

> **Course**: Selenium | **Module**: Advanced and CI | **Difficulty**: advanced

---

Build a complete automated test suite for an e-commerce website (e.g., `https://automationexercise.com`) covering:

1. User registration and login
2. Product search and filtering
3. Add to cart and checkout
4. Order history verification

---

```
ecommerce_tests/
    pages/
        base_page.py
        login_page.py
        register_page.py
        product_listing_page.py
        product_detail_page.py
        cart_page.py
        checkout_page.py
        order_confirmation_page.py
    components/
        header.py
        footer.py
        product_card.py
    tests/
        test_auth.py
        test_search.py
        test_cart.py
        test_checkout.py
    test_data/
        users.csv
        products.json
    conftest.py
    pytest.ini
    requirements.txt
```

---

```python
# tests/test_checkout.py
import pytest
from faker import Faker
from pages.login_page import LoginPage
from pages.product_listing_page import ProductListingPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

fake = Faker()

class TestCheckout:
    @pytest.mark.smoke
    def test_guest_checkout(self, driver):
        """Guest user can complete checkout with valid details"""
        # 1. Add product to cart
        ProductListingPage(driver).open()             .search("blue dress")             .get_first_product().add_to_cart()

        # 2. Go to cart
        cart = CartPage(driver).open()
        assert cart.item_count() == 1

        # 3. Proceed to checkout
        checkout = cart.proceed_to_checkout()
        checkout.fill_shipping(
            name=fake.name(), email=fake.email(),
            address=fake.address(), zip=fake.zipcode()
        )
        checkout.pay_with_card(
            number="4111111111111111", expiry="12/26", cvv="123"
        )

        # 4. Verify confirmation
        confirmation = checkout.place_order()
        assert confirmation.order_placed()
        assert confirmation.get_order_id() is not None

    @pytest.mark.regression
    @pytest.mark.parametrize("product", ["t-shirt", "jeans", "jacket"])
    def test_add_multiple_products(self, driver, authenticated_user, product):
        page = ProductListingPage(driver).open()
        page.search(product).get_first_product().add_to_cart()
        assert CartPage(driver).open().item_count() >= 1
```

---

| Artifact | Description |
|---|---|
| `conftest.py` | Session driver, authenticated fixture, screenshot on fail |
| `pytest.ini` | Markers, options, HTML report config |
| `pages/` | Full POM with BasePage, 8 page classes |
| `components/` | Header, Cart icon, Product card |
| `tests/` | 20+ test cases across 4 modules |
| `reports/` | HTML + Allure report |
| `.github/workflows/` | CI pipeline on push |

---

1. Implement all 8 page objects with proper locators and action methods
2. Write 20 test cases with data-driven login, search, and checkout tests
3. Set up CI pipeline to run on push, upload report, and notify on failure

---
