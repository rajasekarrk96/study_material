# Validation Rules

Rules enforced during Learning OS audit before merging.

---

## File Naming

- All lowercase with underscores: _01_01_what_is_ml.md
- Module and lesson prefix required: _03_05_...
- Extension: .md only
- Do NOT rename existing files
- Do NOT add files not in MISSING_NOTES.md

---

## Heading Rules

- Exactly ONE H1 per file (lesson title)
- H2 for required template sections
- No heading level skipping (H2 → H4 without H3)
- Metadata blockquote on line 3

## Required Sections (16)

H1 Title | Metadata | Overview | Learning Objectives | Prerequisites | Theory | Internal Working | Code Examples | Hands-on Practice | Real-world Example | Best Practices | Common Mistakes | Interview Questions | Summary | Cheat Sheet | References

---

## Code Block Rules

- Language identifier required on every block
- No pseudocode — all examples must be runnable
- Allowed: python, sql, bash, yaml, json, javascript, dockerfile, text, mermaid

---

## Rejection Criteria

A note is rejected if:
- Missing any required section
- Code block has no language identifier
- Fewer than 3 interview questions
- References section missing or has bare URLs
- File was renamed or added outside MISSING_NOTES.md
- Existing note content was modified
