# Python Selenium Test Automation — Master Syllabus

**Target Role:** QA Automation Engineer / SDET (Python) / Test Automation Architect  
**Difficulty Level:** Intermediate  
**Estimated Duration:** 120 Hours  
**Prerequisites:** core-python  
**Required Courses:** core-python  
**Optional Courses:** devops, postman  

---

## Study Flow

### 1. Python QA & Selenium Automation

#### 1.1. Module 1 — Python QA Foundations & Selenium 4 Setup
1. **Python Testing Ecosystem & PyTest Setup**
    - **Course Coverage:** 🟢 Covered in Class
    - PyTest Test Runner, Naming Conventions, and Test Discovery
    - Virtual Environments, `pip`, and Dependency Management (`requirements.txt`)
    - PyTest Execution Flags (`-v`, `-s`, `-k`, `-m`, `--maxfail`)
    - Command Line Arguments & Custom PyTest Markers
2. **Selenium 4 Architecture & WebDriver Setup**
    - **Course Coverage:** 🟢 Covered in Class
    - W3C WebDriver Protocol Architecture vs Legacy JSON Wire Protocol
    - Selenium Manager & Automatic Driver Binary Management (ChromeDriver, GeckoDriver)
    - Browser Options, Capabilities, Headless Execution, and Incognito Mode
    - Initializing and Teardown of `webdriver.Chrome()` and `webdriver.Firefox()`

#### 1.2. Module 2 — Element Locators & WebDriver Operations
1. **Advanced Locator Strategies**
    - **Course Coverage:** 🟢 Covered in Class
    - Locating by ID, Name, Class Name, Tag Name, Link Text, Partial Link Text
    - XPath Strategies: Absolute vs Relative, Axes (`parent`, `following-sibling`, `ancestor`), Text Matching, Indexing
    - CSS Selectors: Attributes, Pseudo-classes, Wildcards (`^=`, `$=`, `*=`), Child/Sibling Combinators
    - Selenium 4 Relative Locators (`above`, `below`, `to_left_of`, `to_right_of`, `near`)
2. **Dynamic Synchronization & Waits**
    - **Course Coverage:** 🟢 Covered in Class
    - Implicit Waits vs Explicit Waits vs Fluent Waits
    - `WebDriverWait` and `expected_conditions` (`element_to_be_clickable`, `visibility_of_element_located`, `presence_of_element_located`)
    - Custom Wait Conditions & Handling `StaleElementReferenceException`
    - Auto-Healing & Retry Mechanics for Flaky Elements

#### 1.3. Module 3 — Advanced Interactions, Frames & Chrome DevTools Protocol
1. **Complex Web Controls & ActionChains**
    - **Course Coverage:** 🟢 Covered in Class
    - Handling JavaScript Alerts, Confirmations, and Prompt Dialogs
    - iFrames & Nested Frames Traversal (`switch_to.frame`, `switch_to.default_content`)
    - Multiple Windows & Tab Handling (`current_window_handle`, `window_handles`, `switch_to.window`)
    - ActionChains: Mouse Hover, Drag-and-Drop, Double Click, Context Click, Key Combinations
2. **Chrome DevTools Protocol (CDP) & Low-Level API**
    - **Course Coverage:** 🟢 Covered in Class
    - Intercepting & Modifying Network Requests (CDP Network Domain)
    - Emulating Geo-Location, Device Mode, and Network Throttling
    - Capture Performance Metrics & Browser Console Logs
    - Handling Shadow DOM (Open vs Closed Shadow Root Navigation)

#### 1.4. Module 4 — Page Object Model (POM) & Framework Architecture
1. **Page Object Model (POM) Design Pattern**
    - **Course Coverage:** 🟢 Covered in Class
    - Class-Based Page Objects and Page Element Encapsulation
    - Base Page Abstraction: Reusable Wait, Click, Type, and Assert Wrapper Methods
    - Component Object Model for Reusable UI Components (Header, Navbar, Table, Modal)
    - Page Factory vs Pure Class POM Design Comparison
2. **PyTest Fixtures & Test Lifecycle**
    - **Course Coverage:** 🟢 Covered in Class
    - Fixture Scopes (`function`, `class`, `module`, `session`)
    - Conftest.py Architecture: Global Fixtures, Browser Fixture, Hooks
    - Teardown & Yield Statements for Clean State Management
    - Parallel Execution with `pytest-xdist` & Thread-Safe Driver Instances

#### 1.5. Module 5 — Enterprise Automation Frameworks (Data-Driven, Hybrid)
1. **Data-Driven Automation Framework**
    - **Course Coverage:** 🟢 Covered in Class
    - Excel Integration using `openpyxl` & Pandas for Parameterized Test Data
    - Reading & Writing JSON, YAML, and CSV Configuration Files
    - PyTest `@pytest.mark.parametrize` for Multi-Data Set Execution
2. **Keyword-Driven & Hybrid Framework Design**
    - **Course Coverage:** 🟢 Covered in Class
    - Architecture of Keyword-Driven Frameworks (Action Engine, Keyword Sheet)
    - Building a Hybrid Framework combining POM, Data-Driven & Keyword Engines
    - Externalizing Locators to Configuration Files (YAML / Properties)

#### 1.6. Module 6 — Enterprise Reporting, Logging & Fail-Safe Mechanisms
1. **Structured Logging & Capture on Failure**
    - **Course Coverage:** 🟢 Covered in Class
    - Python `logging` Framework Integration (FileAppender, ConsoleAppender, Formatter)
    - Automatically Capturing Screenshots & Video Recordings on Test Failure
    - Attaching Screenshots & Browser Logs to Reports via PyTest Hooks
2. **Enterprise Test Reporting (Allure & HTML)**
    - **Course Coverage:** 🟢 Covered in Class
    - PyTest HTML Report Generation & Customization
    - Allure Reports Setup: `@allure.feature`, `@allure.story`, `@allure.step`, `@allure.severity`
    - Generating Interactive Allure Dashboards and History Trends

#### 1.7. Module 7 — Selenium Grid 4, Docker & Cloud Execution
1. **Selenium Grid 4 Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    - Standalone Mode, Hub-and-Node Mode, and Fully Distributed Mode
    - Configuring Grid Router, Distributor, Session Queue, Event Bus, and Sessions Engine
    - Executing Tests Remotely via `RemoteWebDriver`
2. **Dockerized Test Infrastructure (Selenoid)**
    - **Course Coverage:** 🟢 Covered in Class
    - Setting up Selenoid & Selenoid UI with Docker Compose
    - Running Tests in Isolated Containerized Browsers
    - Cloud Grid Execution: BrowserStack / SauceLabs Integration

#### 1.8. Module 8 — CI/CD Pipeline Integration & Quality Standards
1. **CI/CD Integration & Headless Execution**
    - **Course Coverage:** 🟢 Covered in Class
    - Headless Chrome/Firefox Execution in Linux Containers
    - GitHub Actions Workflow Configuration for Automated Test Triggers
    - Jenkins Pipeline (`Jenkinsfile`) Integration with Allure Plugin
2. **SDET Best Practices & SDLC Alignment**
    - **Course Coverage:** 🟢 Covered in Class
    - Test Suite ROI & Flaky Test Quarantine Workflow
    - Cross-Browser Matrix Testing Strategies
    - Industry SDET Interview Q&A & Capstone Portfolio Project
