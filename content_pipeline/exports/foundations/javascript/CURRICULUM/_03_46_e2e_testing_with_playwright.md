```yaml
schema_version: "2.0"
metadata:
  lesson_id: "JS-MOD12-LES05"
  course_slug: "course-03-javascript"
  course_title: "Course 3: JavaScript & ES6+"
  module_slug: "mod-12-advanced-patterns-testing-capstone"
  module_title: "Module 12 - Advanced Patterns, Meta-Programming, & Testing"
  lesson_slug: "e2e-testing-with-playwright"
  lesson_title: "Lesson 12.5 Integration & E2E Testing with Playwright"
  sort_order: 1205

pedagogy:
  difficulty: "intermediate"
  estimated_time:
    reading_minutes: 20
    practice_minutes: 25
    quiz_minutes: 10
    total_minutes: 55
  bloom_taxonomy_level: "Apply"
  xp_reward: 60

prerequisites:
  required_lesson_ids:
    - "JS-MOD12-LES04"
  required_skills:
    - "JavaScript Unit Testing & Vitest"

skills_acquired:
  - "End-to-End (E2E) Browser Automation Architecture"
  - "Playwright Test Runner Setup (`@playwright/test`)"
  - "User Interaction Simulation (`page.goto()`, `page.click()`, `page.fill()`)"
  - "Visual Regression & Network Mocking"

dependencies:
  software:
    - "VS Code"
    - "Node.js 18+ with Playwright"
  hardware: []

seo_and_social:
  meta_title: "End-to-End Testing: Playwright Browser Automation & UI Assertions"
  meta_description: "Master E2E Browser Automation: Playwright setup, simulating user clicks/forms, page object models, visual assertions, and network request mocking."
  keywords: ["Playwright", "E2E Testing", "Browser Automation", "UI Testing", "Integration Testing", "Headless Browser"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 12.5 Integration & E2E Testing with Playwright

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 12.4 Vitest](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_03_javascript/_03_45_javascript_unit_testing_with_vitest.md)
- **XP Reward**: +60 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Understand **End-to-End (E2E)** browser automation testing.
2. Configure **Playwright** test runners across Chrome, Firefox, and Safari engines.
3. Simulate user interactions (`page.goto()`, `page.click()`, `page.fill()`).
4. Perform web UI assertions using `expect(page.locator()).toBeVisible()`.

---

## 2. Environment & Prerequisites [id: prerequisites]

Open terminal with Node.js 18+.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 Unit Testing vs End-to-End (E2E) Testing
While Unit Tests (Vitest) test isolated JavaScript functions in memory, **End-to-End (E2E) Testing** controls real headless browser engines to verify that the entire web application (UI, DOM, routing, APIs) works seamlessly from the end user's perspective.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      UNIT TESTING VS E2E TESTING MATRIX                     │
├─────────────────┬──────────────────────────────────┬────────────────────────┤
│ Feature         │ Unit Testing (Vitest)            │ E2E Testing (Playwright)│
├─────────────────┼──────────────────────────────────┼────────────────────────┤
│ Scope           │ Single function / component      │ Full user workflow     │
│ Execution Speed │ Milliseconds                     │ Seconds                │
│ Browser Context │ Node.js / jsdom                  │ Chromium, Firefox, WebKit│
└─────────────────┴──────────────────────────────────┴────────────────────────┘
```

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    Runner[Playwright Runner] -->|Controls Headless Chromium| Browser[Headless Browser Engine]
    Browser --> Nav[page.goto '/login']
    Nav --> Fill[page.fill '#email', 'user@test.com']
    Fill --> Click[page.click '#submit']
    Click --> Assert[expect page.locator '.dashboard' .toBeVisible]
```

---

## 5. Code & Hardware Implementation [id: syntax]

### Playwright Test Suite: `dashboard.spec.js`

```javascript
import { test, expect } from "@playwright/test";

test.describe("IoT Telemetry Dashboard E2E Tests", () => {
  test("should allow user to filter active sensor cards", async ({ page }) => {
    // 1. Navigate to Web Application
    await page.goto("http://localhost:3000");

    // 2. Interact with DOM Elements
    await page.fill("#search-input", "ESP32");
    await page.click("#btn-filter");

    // 3. Assert Visual & DOM State
    const card = page.locator(".sensor-card").first();
    await expect(card).toBeVisible();
    await expect(card).toContainText("ESP32");
  });
});
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **E-Commerce Checkout Testing**: Retailers run Playwright E2E suites before deployments to verify that users can add items to carts, enter shipping info, and process credit card payments without UI errors.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Run `npm init playwright@latest` in project directory.
2. Execute `npx playwright test --headed` $\to$ Watch Playwright automate browser clicks live!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **Flaky Tests (Timing Issues)** | Using hardcoded `setTimeout()` waiting for async DOM elements to load. | Rely on Playwright auto-waiting locators (`expect(locator).toBeVisible()`). |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Use User-Facing Locators**: Prefer `page.getByRole()` and `page.getByText()` over fragile CSS selectors.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: Why is Playwright preferred over older Selenium or Puppeteer testing frameworks?
**Answer**: Playwright supports all major browser engines (Chromium, Firefox, WebKit) out of the box with zero external drivers, features native auto-waiting (eliminating artificial sleep calls), runs tests in parallel using isolated browser contexts, and includes network request mocking.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 12.5 Playwright Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which Playwright method simulates typing input into a form text field?",
      "options": ["page.type()", "page.fill()", "page.write()", "page.input()"],
      "correct_answer_index": 1,
      "explanation": "page.fill() inputs text into form fields."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Build an E2E Playwright test verifying form validation and dynamic card creation.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: Does Playwright automatically wait for elements to be visible before clicking?
**Back**: Yes. Playwright features built-in auto-waiting for element visibility and stability.
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```javascript
await page.goto(url);
await page.click("#btn");
await expect(page.locator(".card")).toBeVisible();
```
