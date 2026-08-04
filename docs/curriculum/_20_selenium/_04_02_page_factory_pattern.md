# Page Factory Pattern

> **Course**: Selenium | **Module**: Test Architecture | **Difficulty**: intermediate

---

Rather than one monolithic page object, break pages into reusable **components** (header, footer, nav bar, modal, etc.).

```python
# components/header.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Header:
    LOGO        = (By.CSS_SELECTOR, ".logo")
    SEARCH_BOX  = (By.ID, "global-search")
    CART_ICON   = (By.CSS_SELECTOR, ".cart-count")
    USER_MENU   = (By.ID, "user-dropdown")

    def __init__(self, driver):
        self.driver = driver
        self._base = BasePage(driver)

    def search(self, query: str):
        self._base.type(self.SEARCH_BOX, query)
        from selenium.webdriver.common.keys import Keys
        self._base.find(self.SEARCH_BOX).send_keys(Keys.RETURN)

    def get_cart_count(self) -> int:
        text = self._base.get_text(self.CART_ICON)
        return int(text) if text.isdigit() else 0

    def open_user_menu(self):
        self._base.click(self.USER_MENU)
```

---

```python
# pages/product_listing_page.py
from .base_page import BasePage
from components.header import Header
from components.product_card import ProductCard
from selenium.webdriver.common.by import By

class ProductListingPage(BasePage):
    URL = "https://myapp.com/products"
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".product-card")
    SORT_SELECT   = (By.ID, "sort-by")

    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(driver)        # composition

    def get_products(self) -> list:
        cards = self.driver.find_elements(*self.PRODUCT_CARDS)
        return [ProductCard(card) for card in cards]

    def sort_by(self, option: str):
        from selenium.webdriver.support.ui import Select
        Select(self.find(self.SORT_SELECT)).select_by_visible_text(option)
```

---

```python
# components/product_card.py
from selenium.webdriver.common.by import By

class ProductCard:
    def __init__(self, element):
        self._el = element

    def get_name(self) -> str:
        return self._el.find_element(By.CSS_SELECTOR, ".product-name").text

    def get_price(self) -> float:
        text = self._el.find_element(By.CSS_SELECTOR, ".price").text
        return float(text.replace("$", "").replace(",", ""))

    def add_to_cart(self):
        self._el.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
```

---

1. Create Header, Footer, and Modal components shared across 3 page objects
2. Write a test that uses Header.search() and verifies product listing updates
3. Implement a `DataTable` component that wraps `<table>` and provides `get_row_by_column(col, val)`

---
