# Validation Rules

Enforced automatically by `scripts/validate_import.py` and during human review.

---

## File Naming

- Lowercase with underscores only
- Module and lesson number prefix required
- Extension must be `.md`
- No renames of existing files
- No new files outside MISSING_NOTES.md

## Required Sections

All 16 sections in NOTE_TEMPLATE.md must be present.

## Code Blocks

- Language identifier required
- No pseudocode in examples
- Lines ≤ 100 characters

## Interview Questions

- Minimum 3 per lesson

## References

- Minimum 2 per lesson
- All must be markdown links (no bare URLs)

## Rejection Criteria

- Missing sections > 5% of lessons
- Pseudocode in code blocks > 10% of lessons
- Renamed files
- Added unauthorized files
- Modified existing complete notes
- Fewer than 3 interview questions per lesson
- References missing or bare URLs
