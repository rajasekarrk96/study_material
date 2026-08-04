---
id: "16_03_05"
title: "File Upload and Download"
course: "Selenium"
module: 3
module_title: "Advanced Interactions"
lesson: 5
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["file-upload", "input-type-file", "send_keys", "download", "chrome-prefs", "robot", "pyautogui", "wait-for-download"]
prerequisites: []
lab_required: true
---

# File Upload and Download


## File Upload

```python
# Standard <input type="file"> — just send_keys the absolute path
file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(r"C:/path/to/my/document.pdf")

# Multiple files
file_input.send_keys(
    r"C:/files/file1.pdf" + "
" + r"C:/files/file2.pdf"
)
# OR send separately
file_input.send_keys(r"C:/files/file1.pdf")
```

## File Download Configuration

```python
import os

download_dir = os.path.abspath("downloads")
os.makedirs(download_dir, exist_ok=True)

# Chrome — set download directory
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
}
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)
```

## Wait for Download to Complete

```python
import time
import glob

def wait_for_download(directory, filename_pattern="*.pdf", timeout=30):
    """Wait until a file matching pattern appears and is complete"""
    deadline = time.time() + timeout
    while time.time() < deadline:
        files = glob.glob(os.path.join(directory, filename_pattern))
        # Filter out .crdownload (Chrome temp files)
        complete = [f for f in files if not f.endswith(".crdownload")]
        if complete:
            return complete[-1]   # return latest matching file
        time.sleep(0.5)
    raise TimeoutError(f"Download not completed in {timeout}s")

# Usage
driver.find_element(By.ID, "download-report").click()
downloaded = wait_for_download(download_dir, "report_*.xlsx")
print(f"Downloaded: {downloaded}")
```

## Handling Native OS Dialogs

```python
# For systems without hidden file inputs (uses pyautogui)
import pyautogui, time

driver.find_element(By.ID, "upload-button").click()
time.sleep(1)   # wait for native dialog to open

pyautogui.typewrite(r"C:iles\document.pdf", interval=0.05)
pyautogui.press("enter")
```

## Lab Exercise
1. Upload a PDF to a file-upload form and verify the file name appears in the UI
2. Configure Chrome to auto-download CSVs to a temp directory, trigger download, verify file
3. Handle a chunked upload form that shows a progress bar — wait until 100% complete
