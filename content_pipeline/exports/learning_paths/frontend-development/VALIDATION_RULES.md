# Validation Rules

> These rules are enforced during Learning OS audit before merging returned packages.  
> Violations will result in the file being rejected.

---

## 1. Folder Naming

| Rule | Example |
|---|---|
| All lowercase | `html5/` ✅ `HTML5/` ❌ |
| Use the course slug | `react/` ✅ `react-frontend/` ❌ |
| No spaces | `javascript/` ✅ `java script/` ❌ |
| Do not add new subfolders | `react/hooks/` ❌ |

---

## 2. File Naming

| Rule | Example |
|---|---|
| All lowercase | `_01_01_jsx_syntax.md` ✅ |
| Use underscores only (no hyphens, no spaces) | `_01_01_jsx_syntax.md` ✅ `01-jsx-syntax.md` ❌ |
| Module and lesson prefix required | `_03_12_scope_chain_and_closures.md` ✅ |
| Extension must be `.md` | `.md` ✅ `.txt` ❌ |
| Do NOT rename existing files | Renaming is a rejection |
| Do NOT add files not listed in `MISSING_NOTES.md` | Unauthorized additions are removed |

---

## 3. Heading Rules

| Rule | Detail |
|---|---|
| Exactly ONE H1 per file | First line must be `# Lesson Title` |
| H2 for major sections | `## Overview`, `## Theory`, etc. |
| No heading level skipping | H2 → H4 without H3 is invalid |
| Sentence case for headings | `## Internal working` ✅ `## Internal Working` ✅ (both accepted) |
| No trailing spaces after heading text | `## Overview ` ❌ |

---

## 4. Required Lesson Sections

Every note must contain ALL of the following sections in this order:

| # | Section | H-level |
|---|---|---|
| 1 | Lesson Title | H1 |
| 2 | Metadata blockquote | (no heading) |
| 3 | Overview | H2 |
| 4 | Learning Objectives | H2 |
| 5 | Prerequisites | H2 |
| 6 | Theory | H2 |
| 7 | Internal Working / How It Works | H2 |
| 8 | Code Examples | H2 |
| 9 | Hands-on Practice | H2 |
| 10 | Real-world Example | H2 |
| 11 | Best Practices | H2 |
| 12 | Common Mistakes | H2 |
| 13 | Interview Questions | H2 |
| 14 | Summary | H2 |
| 15 | Cheat Sheet | H2 |
| 16 | References | H2 |

**Architecture** section is optional (include only for architecture-heavy topics).

> A note missing any required section will be returned for revision.

---

## 5. Code Block Rules

| Rule | Detail |
|---|---|
| Language identifier required | ` ```html `, ` ```javascript `, ` ```css `, ` ```jsx ` |
| No pseudocode | Examples must be copy-pasteable and runnable |
| Comments in examples | Every non-obvious line must have a `//` or `<!-- -->` comment |
| Indentation | 4 spaces (no tabs) |
| Max line length in code | 100 characters |

Allowed identifiers: `html`, `css`, `scss`, `javascript`, `jsx`, `json`, `bash`, `text`, `mermaid`

---

## 6. Markdown Validation

| Rule | Detail |
|---|---|
| Valid GFM | Tables need separator rows `|---|---|` |
| No broken links | All markdown links must resolve |
| Escape special characters | `<`, `>` in prose must be escaped or in backticks |
| No raw HTML (except diagrams) | Use Markdown formatting instead |
| Trailing newline | File must end with a newline character |

---

## 7. Metadata Blockquote (required on line 3)

Format exactly as:

```
> **Course:** [Course Name] | **Module:** [Module Name] | **Difficulty:** [level]
```

Valid difficulty values: `beginner`, `intermediate`, `advanced`

---

## 8. References Section

| Rule | Detail |
|---|---|
| Minimum 2 references | At least MDN and one other |
| Markdown links only | No bare URLs |
| Format | `- [Description](https://url)` |

---

## 9. Audit Rejection Criteria

A note will be **automatically rejected** if:

- ❌ Missing any required section
- ❌ Contains pseudocode in code blocks
- ❌ Code block has no language identifier
- ❌ File was renamed
- ❌ File was added outside `MISSING_NOTES.md`
- ❌ Existing note content was modified
- ❌ References section is missing or has bare URLs
- ❌ Fewer than 3 interview questions
- ❌ File does not end with a newline

---

## 10. Automatic Merge Rules

A note is **approved for merge** when:

- ✅ All 36 stubs are complete
- ✅ All sections present
- ✅ All code blocks valid
- ✅ All references valid
- ✅ `CHECKLIST.md` is fully ticked
- ✅ `REPORT.md` is completed
- ✅ No existing files modified
- ✅ No unexpected files added
