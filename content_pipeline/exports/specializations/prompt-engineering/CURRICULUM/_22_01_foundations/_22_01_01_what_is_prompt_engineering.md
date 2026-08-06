---
id: "22_01_01"
title: "What is Prompt Engineering"
course: "Prompt Engineering"
module: 1
module_title: "Foundations"
lesson: 1
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["prompt-engineering", "llm", "ai", "generative-ai"]
prerequisites: []
lab_required: true
---

# What is Prompt Engineering

## Overview of What is Prompt Engineering

In this lesson, you will master **What is Prompt Engineering** as part of Module 1: Foundations in Prompt Engineering.

### Core Concepts & Strategy

1. **Theory & Rationale**: Understand why language models respond to specific structural framing, context placement, and constraint specifications.
2. **Technique Breakdown**:
   - System instruction vs User prompt separation.
   - Using explicit formatting markers (e.g., Markdown headers, XML tags `<context>`).
   - Controlling model behavior via few-shot examples and chain-of-thought step triggers.

```markdown
### Example Prompt Template for What is Prompt Engineering

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
