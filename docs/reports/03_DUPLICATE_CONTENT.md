# 03 -- Duplicate Content Report

**Generated:** 2026-08-04  
**Audit Version:** 4.1 (Corrected — False Positive Resolved)  
**Status:** OK -- No Structural Duplicates

---

## Duplicate Subject Folders

**NONE DETECTED.**

### Note: Python Folders Are NOT Duplicates

The audit script previously flagged Python-related folders as duplicates. This is a **false positive**.
The following 4 folders all contain the keyword `python` but are **distinct, non-overlapping subjects**:

| Folder | Subject | Content |
| :--- | :--- | :--- |
| `09-python-core` | Python Language Fundamentals | Syntax, OOP, built-ins, decorators, async |
| `10-advanced-python` | Advanced Python Patterns | Metaclasses, descriptors, C extensions, packaging |
| `39-python-data-science` | Python Data Science Stack | NumPy, Pandas, Matplotlib, SciPy |
| `50-python-dsa` | Python Algorithms & Data Structures | Big-O, sorting, trees, graphs, dynamic programming |

These are **canonical, non-duplicate folders** and must remain separate.

---

## Duplicate Files (Same Filename in Multiple Folders)

**2 duplicate filenames found across multiple curriculum folders:**

| Filename | Appears In | Recommended Action |
| :--- | :--- | :--- |
| `_01_03_control_flow.md` | `01-c-programming`, `11-java-core` | Keep in canonical folder, archive others |
| `README.md` | `09-python-core`, `11-java-core` | Keep in canonical folder, archive others |

---

## Summary

| Type | Count | Action Required |
| :--- | :---: | :---: |
| Duplicate Subject Folders | 0 | None |
| Duplicate Files | 2 | Review manually |
| Overall Duplicate Rate | 0% | OK |
| **Status** | | **CLEAN** |
