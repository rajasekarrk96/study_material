# Headless Browser Testing

> **Course**: Selenium | **Module**: Advanced and CI | **Difficulty**: intermediate

---

Headless mode runs the browser **without a visible window**. Essential for:
- CI/CD pipelines (no display available)
- Faster test execution
- Server-side scraping

---

```python
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument("--headless=new")          # new headless mode (Chrome 112+)
opts.add_argument("--window-size=1920,1080") # set viewport
opts.add_argument("--disable-gpu")           # needed on some systems
opts.add_argument("--no-sandbox")            # required in Docker
opts.add_argument("--disable-dev-shm-usage") # prevent /dev/shm issues in Docker

driver = webdriver.Chrome(options=opts)
driver.get("https://example.com")
driver.save_screenshot("headless_screenshot.png")
driver.quit()
```

---

```python
from selenium.webdriver.firefox.options import Options as FirefoxOptions

opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(options=opts)
```

---

```bash
# Install Xvfb (virtual frame buffer)
sudo apt-get install xvfb
Xvfb :99 -screen 0 1920x1080x24 &
export DISPLAY=:99

# OR use pyvirtualdisplay in Python
pip install pyvirtualdisplay
```

```python
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1920, 1080))
display.start()

driver = webdriver.Chrome()   # now uses virtual display
# run tests...
driver.quit()
display.stop()
```

---

1. Configure headless Chrome with 1920x1080 viewport and run 5 tests
2. Set up GitHub Actions workflow that runs headless Selenium tests on push
3. Compare execution time: headed vs headless for a 10-test suite

---
