---
id: "22_05_02"
title: "Jailbreaking Techniques and Defenses"
course: "Prompt Engineering"
module: 5
module_title: "Security and Vulnerabilities"
lesson: 2
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["jailbreak", "dan-prompt", "defense-in-depth"]
prerequisites: []
lab_required: true
---

# Jailbreaking Techniques and Defenses

## Overview of Jailbreaking Techniques and Defenses

In this lesson, you will master **Jailbreaking Techniques and Defenses** as part of Module 5: Security and Vulnerabilities in Prompt Engineering.

### Core Concepts & Strategy

1. **Theory & Rationale**: Understand why language models respond to specific structural framing, context placement, and constraint specifications.
2. **Technique Breakdown**:
   - System instruction vs User prompt separation.
   - Using explicit formatting markers (e.g., Markdown headers, XML tags `<context>`).
   - Controlling model behavior via few-shot examples and chain-of-thought step triggers.

```markdown
### Example Prompt Template for Jailbreaking Techniques and Defenses

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
