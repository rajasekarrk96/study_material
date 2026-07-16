# 09 — Exercise Engine

> The Exercise Engine manages practice problems, assignments, projects, and execution evaluations.

---

## 9.1 Exercise vs. Assignment vs. Project

```
              ┌────────────────────────────────────────────────────────┐
              │                   EXERCISE TYPES                       │
              └────────────────────────────────────────────────────────┘
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         ▼                         ▼                         ▼
 ┌───────────────┐         ┌───────────────┐         ┌───────────────┐
 │   Exercise    │         │  Assignment   │         │    Project    │
 ├───────────────┤         ├───────────────┤         ├───────────────┤
 │ Short coding  │         │ Take-home program       │ Real-world app│
 │ problems      │         │ with structured         │ folder/repo   │
 │ (1-10 lines)  │         │ criteria templates      │ submission    │
 ├───────────────┤         ├───────────────┤         ├───────────────┤
 │ Auto-graded   │         │ Semi-auto     │         │ Manual rubric │
 │ test-suites   │         │ (Linter + AI) │         │ peer/instructor│
 └───────────────┘         └───────────────┘         └───────────────┘
```

---

## 9.2 Execution Frameworks

### 1. In-Browser / Safe Auto-Grading (Judge0 Plugin)
For python, javascript, sql, and java code validation, the system integrates with Judge0/Piston sandboxed sandboxes.

```
[Student Submit] ──► [OS Service] ──► [Judge0 Sandbox] ──► [Run against Test Cases] ──► [Score]
```

### 2. Sandbox Security Architecture (Key Rules)
- Network access is disabled during execution.
- File system access is restricted to `/tmp` with absolute disk quotas (10MB).
- Process fork limit is set to 2.
- Time limit is capped at 3.0 seconds.

---

## 9.3 Coding Test Case Model

```python
# app/domains/exercise/models.py

class ExerciseTestCase(db.Model):
    __tablename__ = 'exercise_test_cases'

    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    input_data = db.Column(db.Text)          # Standard input
    expected_output = db.Column(db.Text)     # Expected standard output
    is_hidden = db.Column(db.Boolean, default=False)  # Hidden from students
    weight = db.Column(db.Integer, default=1)
```

---

## 9.4 Auto-Grading Flow

```python
# app/domains/exercise/service.py

import requests
from app.domains.exercise.models import ExerciseSubmission

class AutoGradingService:
    def __init__(self, judge0_api_url: str, judge0_key: str):
        self.api_url = judge0_api_url
        self.headers = {"X-Auth-Token": judge0_key} if judge0_key else {}

    def submit_solution(self, submission: ExerciseSubmission) -> dict:
        """
        Submits code to Judge0 sandbox, compares outputs, and returns test outcomes.
        """
        exercise = submission.exercise
        test_cases = exercise.test_cases

        passed = 0
        total = len(test_cases)
        results = []

        for case in test_cases:
            payload = {
                "source_code": submission.solution_text,
                "language_id": self._map_language_to_id(submission.language),
                "stdin": case.input_data,
                "expected_output": case.expected_output,
                "cpu_time_limit": 2.0
            }
            
            # Post compilation & execution request
            response = requests.post(f"{self.api_url}/submissions?wait=true", json=payload, headers=self.headers)
            res_data = response.json()

            status = res_data.get("status", {}).get("description", "Failed")
            is_correct = status == "Accepted"
            
            if is_correct:
                passed += 1

            results.append({
                "test_case_id": case.id,
                "is_hidden": case.is_hidden,
                "status": status,
                "is_correct": is_correct,
                "stderr": res_data.get("stderr"),
                "compile_output": res_data.get("compile_output")
            })

        submission.status = "PASSED" if passed == total else "FAILED"
        submission.points_earned = int((passed / total) * exercise.points)
        
        return {
            "status": submission.status,
            "score": submission.points_earned,
            "results": results
        }

    def _map_language_to_id(self, language: str) -> int:
        # Judge0 language ids
        mapping = {"python": 71, "java": 62, "javascript": 63, "cpp": 75}
        return mapping.get(language.lower(), 71)
```
