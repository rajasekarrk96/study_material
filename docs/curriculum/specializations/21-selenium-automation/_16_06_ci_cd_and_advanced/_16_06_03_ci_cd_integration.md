---
id: "16_06_03"
title: "CI/CD Integration"
course: "Selenium"
module: 6
module_title: "Advanced and CI"
lesson: 3
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["github-actions", "jenkins", "CI", "CD", "headless", "artifacts", "allure", "docker", "environment-variables", "test-report"]
prerequisites: []
lab_required: true
---

# CI/CD Integration


## GitHub Actions Workflow

```yaml
# .github/workflows/selenium-tests.yml
name: Selenium UI Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  ui-tests:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run Selenium Tests
        env:
          BASE_URL: ${{ secrets.STAGING_URL }}
          TEST_USER: ${{ secrets.TEST_USER }}
          TEST_PASS: ${{ secrets.TEST_PASS }}
        run: |
          pytest tests/             --headless             --html=reports/report.html             --self-contained-html             -v

      - name: Upload test report
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: test-report
          path: reports/

      - name: Upload failure screenshots
        if: failure()
        uses: actions/upload-artifact@v4
        with:
          name: failure-screenshots
          path: failures/
```

## Jenkins Pipeline (Declarative)

```groovy
pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh """
                    pytest tests/                       --html=report.html                       --self-contained-html                       -n 4
                """
            }
        }
    }

    post {
        always {
            publishHTML(target: [
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Selenium Test Report'
            ])
        }
    }
}
```

## Lab Exercise
1. Create a GitHub Actions workflow that runs tests on every PR targeting `main`
2. Archive screenshots from failed tests as workflow artifacts
3. Add a Slack notification step that posts the pass/fail summary on completion
