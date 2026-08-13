---
id: "22_02_01"
title: "Zero-Shot Prompting"
course: "Prompt Engineering"
module: 2
module_title: "Core Prompting Techniques"
lesson: 1
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["zero-shot", "direct-prompting"]
prerequisites: []
lab_required: true
---

# Zero-Shot Prompting

## Overview of Zero-Shot Prompting

In this lesson, you will master **Zero-Shot Prompting** as part of Module 2: Core Prompting Techniques in Prompt Engineering.

### Core Concepts & Strategy

1. **Theory & Rationale**: Understand why language models respond to specific structural framing, context placement, and constraint specifications.
2. **Technique Breakdown**:
   - System instruction vs User prompt separation.
   - Using explicit formatting markers (e.g., Markdown headers, XML tags `<context>`).
   - Controlling model behavior via few-shot examples and chain-of-thought step triggers.

```markdown
### Example Prompt Template for Zero-Shot Prompting

System: You are an expert AI assistant specializing in software architecture.

Context:
<context>
The user is designing a microservices-based e-commerce platform.
</context>

Task:
Provide a step-by-step breakdown for handling distributed transactions.

Constraints:
- Output valid JSON only.
- Include failure recovery steps.
```

## Lab Exercise
1. Test the prompt template above on an LLM playground, compare zero-shot vs few-shot completions, and measure output consistency.
