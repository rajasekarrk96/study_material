---
id: "22_04_06"
title: "Synthetic Data Generation via Prompts"
course: "Prompt Engineering"
module: 4
module_title: "Domain Specific Applications"
lesson: 6
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["synthetic-data", "dataset-generation", "bootstrap"]
prerequisites: []
lab_required: true
---

# Synthetic Data Generation via Prompts

## Overview of Synthetic Data Generation via Prompts

In this lesson, you will master **Synthetic Data Generation via Prompts** as part of Module 4: Domain Specific Applications in Prompt Engineering.

### Core Concepts & Strategy

1. **Theory & Rationale**: Understand why language models respond to specific structural framing, context placement, and constraint specifications.
2. **Technique Breakdown**:
   - System instruction vs User prompt separation.
   - Using explicit formatting markers (e.g., Markdown headers, XML tags `<context>`).
   - Controlling model behavior via few-shot examples and chain-of-thought step triggers.

```markdown
### Example Prompt Template for Synthetic Data Generation via Prompts

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
