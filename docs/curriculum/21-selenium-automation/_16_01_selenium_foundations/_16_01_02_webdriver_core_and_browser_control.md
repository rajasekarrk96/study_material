---
id: "16_01_02"
title: "WebDriver Core and Browser Control"
course: "Selenium"
module: 1
module_title: "Selenium Fundamentals"
lesson: 2
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["get", "back", "forward", "refresh", "title", "current-url", "window-size", "maximize", "screenshot", "quit", "close"]
prerequisites: []
lab_required: true
---

# WebDriver Core and Browser Control


## WebDriver Navigation

```python
driver.get("https://example.com")    # open URL (blocks until loaded)
driver.back()                         # browser Back button
driver.forward()                      # browser Forward button
driver.refresh()                      # reload page
```

## Browser Properties

```python
driver.title           # page title string
driver.current_url     # current URL string
driver.page_source     # full HTML source
```

## Window Management

```python
driver.maximize_window()
driver.minimize_window()
driver.set_window_size(1920, 1080)
driver.set_window_position(0, 0)
driver.get_window_size()    # {'width': 1920, 'height': 1080}
```

## Screenshots

```python
# Capture full page screenshot
driver.save_screenshot("screenshot.png")

# Get as bytes (for embedding in reports)
png_bytes = driver.get_screenshot_as_png()

# Screenshot of specific element
element = driver.find_element(By.ID, "header")
element.screenshot("header.png")
```

## Cookies

```python
driver.get_cookies()                          # list of all cookies
driver.get_cookie("session_id")              # specific cookie
driver.add_cookie({"name": "token", "value": "abc123"})
driver.delete_cookie("session_id")
driver.delete_all_cookies()
```

## Execute Script

```python
# Scroll to bottom of page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Get value not accessible via Selenium
inner_text = driver.execute_script("return arguments[0].innerText;", element)
```

## Quit vs Close

```python
driver.close()   # closes current window/tab only
driver.quit()    # quits entire browser + kills WebDriver process
# Always use quit() at end of test!
```

## Lab Exercise
1. Script that navigates back and forward through 3 pages, verifying the URL each time
2. Save a screenshot before and after clicking a button
3. Set a custom cookie and verify it persists on page reload
