---
id: "16_06_02"
title: "Selenium Grid"
course: "Selenium"
module: 6
module_title: "Advanced and CI"
lesson: 2
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["selenium-grid", "hub", "node", "capabilities", "remote-webdriver", "parallel", "docker-selenium", "browser-farm"]
prerequisites: []
lab_required: true
---

# Selenium Grid


## Selenium Grid Architecture

```
              ┌─────────────────────────┐
              │        Grid Hub          │
              │  (distributes sessions)  │
              └────────────┬────────────┘
                           │
           ┌───────────────┼───────────────┐
           │               │               │
    ┌──────┴──────┐ ┌──────┴──────┐ ┌──────┴──────┐
    │  Node: Win  │ │  Node: Mac  │ │  Node: Linux│
    │  Chrome,IE  │ │  Safari,FF  │ │  Chrome,FF  │
    └─────────────┘ └─────────────┘ └─────────────┘
```

## Standalone Grid (Single Node)

```bash
# Download selenium-server-4.x.jar from selenium.dev/downloads

# Start standalone (hub+node in one)
java -jar selenium-server-4.x.jar standalone

# Start hub
java -jar selenium-server-4.x.jar hub

# Start node
java -jar selenium-server-4.x.jar node --hub http://localhost:4444
```

## Remote WebDriver

```python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Connect to Grid hub
options = webdriver.ChromeOptions()
options.set_capability("browserVersion", "latest")
options.set_capability("platformName", "Windows 10")

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=options,
)

driver.get("https://example.com")
print(driver.title)
driver.quit()
```

## Docker Selenium Grid

```yaml
# docker-compose.yml
version: "3.8"
services:
  selenium-hub:
    image: selenium/hub:4
    ports:
      - "4444:4444"

  chrome:
    image: selenium/node-chrome:4
    depends_on: [selenium-hub]
    environment:
      - SE_EVENT_BUS_HOST=selenium-hub
    volumes:
      - /dev/shm:/dev/shm

  firefox:
    image: selenium/node-firefox:4
    depends_on: [selenium-hub]
    environment:
      - SE_EVENT_BUS_HOST=selenium-hub
```

```bash
docker-compose up -d
pytest tests/ -n 4  # parallel across grid nodes
```

## Lab Exercise
1. Start a Selenium Grid with Docker Compose (hub + Chrome node)
2. Run 5 tests simultaneously on the Grid using `webdriver.Remote`
3. Add a Firefox node and run tests cross-browser in parallel
