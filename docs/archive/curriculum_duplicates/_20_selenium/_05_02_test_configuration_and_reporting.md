# Test Configuration and Reporting

> **Course**: Selenium | **Module**: Testing Framework Integration | **Difficulty**: intermediate

---

```ini
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts =
    -v
    --tb=short
    --screenshot=on
    --html=reports/report.html
    --self-contained-html
markers =
    smoke: Smoke tests
    regression: Full regression
    slow: > 30 seconds
```

---

```bash
pip install pytest-html

pytest --html=reports/report.html --self-contained-html tests/
```

---

```bash
pip install pytest-xdist

pytest -n 4 tests/          # 4 parallel workers
pytest -n auto tests/       # auto-detect CPU count
```

```python
# conftest.py — unique driver per worker
@pytest.fixture(scope="function")
def driver(tmp_path):
    import uuid
    opts = webdriver.ChromeOptions()
    opts.add_argument(f"--user-data-dir=/tmp/chrome_{uuid.uuid4()}")
    drv = webdriver.Chrome(options=opts)
    yield drv
    drv.quit()
```

---

```python
# config.py
import os

class Config:
    BASE_URL     = os.getenv("BASE_URL", "https://staging.myapp.com")
    USERNAME     = os.getenv("TEST_USER", "testuser@example.com")
    PASSWORD     = os.getenv("TEST_PASS", "Test@1234")
    BROWSER      = os.getenv("BROWSER", "chrome")
    HEADLESS     = os.getenv("HEADLESS", "false").lower() == "true"
    TIMEOUT      = int(os.getenv("TIMEOUT", "10"))

config = Config()
```

---

1. Set up pytest.ini with custom markers, test discovery, and default HTML report generation
2. Run the same test suite in parallel with `-n 4` and verify isolation
3. Read base URL and credentials from environment variables using `os.getenv`

---
