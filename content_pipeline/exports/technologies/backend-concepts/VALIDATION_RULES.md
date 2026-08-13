# Validation Rules

> These rules can be checked manually or by an automated script.  
> Every rule must pass before the package is returned.

---

## Rule Category 1 — Folder Naming

| Rule ID | Rule | Valid | Invalid |
|---|---|---|---|
| FOLDER-01 | Folder names must be all lowercase | `01-http-protocol` | `01-HTTP-Protocol` |
| FOLDER-02 | Folder names must use hyphens as separators | `04-auth` | `04_auth` |
| FOLDER-03 | Folder names must start with a two-digit number | `09-observability` | `9-observability` |
| FOLDER-04 | No spaces in folder names | `01-http-protocol` | `01-http protocol` |
| FOLDER-05 | No special characters in folder names (only `a-z`, `0-9`, `-`) | `10-infrastructure` | `10-infra&prod` |

---

## Rule Category 2 — File Naming

| Rule ID | Rule | Valid | Invalid |
|---|---|---|---|
| FILE-01 | File names must be all lowercase | `01_http_fundamentals.md` | `01_HTTP_Fundamentals.md` |
| FILE-02 | File names must use underscores as separators | `03_request_response.md` | `03-request-response.md` |
| FILE-03 | File names must start with a two-digit number | `05_caching.md` | `5_caching.md` |
| FILE-04 | File extension must be `.md` | `01_http.md` | `01_http.txt` |
| FILE-05 | No spaces in file names | `01_http_fundamentals.md` | `01 http fundamentals.md` |
| FILE-06 | No special characters (only `a-z`, `0-9`, `_`) | `04_jwt_token_auth.md` | `04_jwt-token-auth.md` |

---

## Rule Category 3 — Heading Format

| Rule ID | Rule |
|---|---|
| HEADING-01 | The file must have exactly one H1 (`#`) heading |
| HEADING-02 | The H1 must be the very first line of the file |
| HEADING-03 | Heading levels must not be skipped (H2 → H3, never H2 → H4) |
| HEADING-04 | All headings must use sentence case (only first word capitalized, plus proper nouns) |
| HEADING-05 | No trailing punctuation in headings |
| HEADING-06 | There must be exactly one blank line before each heading |
| HEADING-07 | There must be exactly one blank line after each heading |

---

## Rule Category 4 — Required Sections

Every lesson file must contain all of the following sections as H2 (`##`) headings, in this order:

| Order | Section Heading | Required |
|---|---|---|
| 1 | `## Overview` | ✅ Mandatory |
| 2 | `## Learning Objectives` | ✅ Mandatory |
| 3 | `## Prerequisites` | ✅ Mandatory |
| 4 | `## Theory` | ✅ Mandatory |
| 5 | `## Architecture` | ✅ Mandatory |
| 6 | `## Internal Working` | ✅ Mandatory |
| 7 | `## Examples` | ✅ Mandatory |
| 8 | `## Real World Example` | ✅ Mandatory |
| 9 | `## Hands-on Practice` | ✅ Mandatory |
| 10 | `## Best Practices` | ✅ Mandatory |
| 11 | `## Common Mistakes` | ✅ Mandatory |
| 12 | `## Summary` | ✅ Mandatory |
| 13 | `## Cheat Sheet` | ✅ Mandatory |
| 14 | `## References` | ✅ Mandatory |

Validation failure: Any file missing one of these sections is invalid.

---

## Rule Category 5 — Content Minimums

| Rule ID | Rule | Minimum |
|---|---|---|
| CONTENT-01 | Learning Objectives must have bullet points | 3 |
| CONTENT-02 | Examples section must have code blocks | 2 |
| CONTENT-03 | Best Practices must have bullet items | 4 |
| CONTENT-04 | Common Mistakes table must have rows | 3 |
| CONTENT-05 | References must have external links | 2 |
| CONTENT-06 | Architecture section must have a Mermaid diagram | 1 |
| CONTENT-07 | Hands-on Practice must have exercises | 1 |

---

## Rule Category 6 — Markdown Validation

| Rule ID | Rule |
|---|---|
| MD-01 | All code blocks must have a language identifier |
| MD-02 | All code blocks must be closed (triple backtick) |
| MD-03 | All tables must have a header row separated by `|---|` |
| MD-04 | No placeholder text (`[PLACEHOLDER]`) may remain |
| MD-05 | All Mermaid blocks must be syntactically valid |
| MD-06 | No trailing spaces at end of lines |
| MD-07 | File must end with exactly one newline |
| MD-08 | All external links must use `https://` |
| MD-09 | No broken anchor links within the same file |

---

## Rule Category 7 — Package Integrity

| Rule ID | Rule |
|---|---|
| PKG-01 | No files outside `OUTPUT/curriculum/` have been created |
| PKG-02 | No files outside `OUTPUT/curriculum/` have been modified |
| PKG-03 | `SYLLABUS.md` content is unchanged from original |
| PKG-04 | `NOTE_TEMPLATE.md` content is unchanged from original |
| PKG-05 | `STYLE_GUIDE.md` content is unchanged from original |
| PKG-06 | `VALIDATION_RULES.md` content is unchanged from original |
| PKG-07 | `AUDIT_TEMPLATE.md` has been completed (not blank) |
| PKG-08 | `CHECKLIST.md` has been checked off |
| PKG-09 | All placeholder `.md` files in `OUTPUT/curriculum/` are filled |
| PKG-10 | No new folders have been added inside `OUTPUT/curriculum/` |
