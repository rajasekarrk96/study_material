---
id: "22_04_04"
title: "Creative Writing and Brainstorming Prompts"
course: "Prompt Engineering"
module: 4
module_title: "Domain Specific Applications"
lesson: 4
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["creative-writing", "ideation", "copywriting"]
prerequisites: []
lab_required: true
---

# Creative Writing and Brainstorming Prompts

## Overview of Creative Writing and Brainstorming Prompts

In this lesson, you will master **Creative Writing and Brainstorming Prompts** as part of Module 4: Domain Specific Applications in Prompt Engineering.

### Core Concepts & Strategy

1. **Theory & Rationale**: Understand why language models respond to specific structural framing, context placement, and constraint specifications.
2. **Technique Breakdown**:
   - System instruction vs User prompt separation.
   - Using explicit formatting markers (e.g., Markdown headers, XML tags `<context>`).
   - Controlling model behavior via few-shot examples and chain-of-thought step triggers.

```markdown
### Example Prompt Template for Creative Writing and Brainstorming Prompts

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
