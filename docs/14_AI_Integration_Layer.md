# 14 — AI Integration Layer

> The AI Integration Layer connects the platform's user interfaces with the AI Gateway service, handling requests for explanation, summarization, quiz generation, and comparison.

---

## 14.1 Architecture Topology

The AI Integration Layer leverages the existing `AIGatewayService` via a uniform plugin registry.

```
       ┌────────────────────────┐
       │   Student UI Action    │
       │   ("Explain code...")  │
       └───────────┬────────────┘
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
┌─────────────────┐ ┌─────────────────┐
│  AI REST Route  │ │   AI Gateway    │
│  Validation     │ │ Plugin Registry │
└─────────────────┘ └─────────────────┘
```

---

## 14.2 Prompt Engineering Templates

System templates ensure structural consistency and prevent LLM hallucination:

```python
# app/domains/ai/service.py

class AIPromptsRegistry:
    EXPLAIN_CONCEPT = (
        "You are a master teacher in the Learning OS.\n"
        "Explain the following concept: {concept}.\n"
        "Break it down using simple analogies, key conceptual principles, "
        "and draft one practical code example. Format output using markdown."
    )
    
    GENERATE_QUIZ = (
        "Based on the following content, generate 5 MCQ questions:\n"
        "{lesson_content}\n"
        "Ensure there are 4 options per question, only one correct option, "
        "and provide clear explanations for why the correct option is selected.\n"
        "Format the output strictly as a JSON list matching this schema:\n"
        "[{{\"question_text\": \"...\", \"options\": [{{\"text\": \"...\", \"is_correct\": true}}], \"explanation\": \"...\"}}]"
    )

    COMPARE_TECHNOLOGY = (
        "Compare {tech_a} and {tech_b}.\n"
        "Provide a markdown table illustrating: Primary Use Case, Performance, "
        "Learning Curve, Syntax verbosity, and when to use one over the other."
    )
```

---

## 14.3 Integration Service Model

```python
# app/domains/ai/service.py

import json
from app.services.ai_service import AIGatewayService

class AIIntegrationService:
    def __init__(self, ai_gateway: AIGatewayService):
        self.gateway = ai_gateway

    def explain_concept(self, concept_name: str) -> str:
        prompt = AIPromptsRegistry.EXPLAIN_CONCEPT.format(concept=concept_name)
        response = self.gateway.generate(
            task_type="chat",
            prompt=prompt,
            model="gemini-2.5-flash"  # default recommended model
        )
        return response.get("text", "Error calling AI services.")

    def generate_quiz_for_lesson(self, lesson_content: str) -> list[dict]:
        prompt = AIPromptsRegistry.GENERATE_QUIZ.format(lesson_content=lesson_content)
        response = self.gateway.generate(
            task_type="chat",
            prompt=prompt,
            model="gemini-2.5-flash",
            response_format="json"  # request JSON output mode
        )
        try:
            quiz_data = json.loads(response.get("text", "[]"))
            return quiz_data
        except Exception:
            return []
```
