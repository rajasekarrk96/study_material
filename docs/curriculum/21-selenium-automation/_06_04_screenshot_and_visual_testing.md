# Screenshot and Visual Testing

> **Course**: Selenium | **Module**: Advanced and CI | **Difficulty**: intermediate

---

```python
import os, time

def take_screenshot(driver, name, folder="screenshots"):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{name}_{int(time.time())}.png")
    driver.save_screenshot(path)
    return path

# Element-level screenshot
element = driver.find_element(By.ID, "product-card")
element.screenshot("product_card.png")

# Full-page screenshot (Selenium 4.15+)
from selenium.webdriver.common.print_page_options import PrintOptions
print_opts = PrintOptions()
print_opts.orientation = "portrait"
pdf = driver.print_page(print_opts)   # returns base64 PDF
```

---

```python
from PIL import Image, ImageChops
import math, operator, functools

def images_are_equal(img1_path, img2_path, threshold=0.01):
    img1 = Image.open(img1_path).convert("RGB")
    img2 = Image.open(img2_path).convert("RGB")

    if img1.size != img2.size:
        return False

    diff = ImageChops.difference(img1, img2)
    pixels = list(diff.getdata())
    total_diff = sum(sum(p) for p in pixels)
    max_diff = 255 * 3 * img1.size[0] * img1.size[1]
    diff_ratio = total_diff / max_diff

    return diff_ratio <= threshold

# Baseline comparison
baseline = "baselines/home_page.png"
current = take_screenshot(driver, "home_page_current")

if os.path.exists(baseline):
    if not images_are_equal(baseline, current):
        print("VISUAL REGRESSION DETECTED!")
else:
    import shutil
    shutil.copy(current, baseline)
    print("Baseline created")
```

---

1. Build a visual regression framework: capture baselines on first run, compare on subsequent runs
2. Highlight pixel differences between two screenshots by drawing red borders around diff areas
3. Integrate Percy.io visual testing into a pytest test (using Percy SDK)

---
