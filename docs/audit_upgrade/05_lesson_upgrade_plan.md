# 05 Lesson Upgrade Plan Report — Enterprise Learning OS

**Plan Date**: July 28, 2026  
**Auditor & Architect**: Chief Curriculum Architect  

---

## 1. Executive Overview

This report provides the exact, file-by-file **Lesson Upgrade Plan** for all 7 legacy existing courses. 

> [!IMPORTANT]
> **NO LESSON REWRITES**: Existing prose, working code snippets, and diagrams MUST NOT be rewritten or deleted. Upgrades are strictly **additive**—injecting YAML metadata headers, missing `[id:]` section anchors, modern code deltas, interview Q&A, and interactive quiz blocks.

---

## 2. Granular Lesson Upgrade Action Matrix

### 2.1 Git Course Upgrade Plan (`_01_git`)

- **Files `_01_01_...md` to `_01_23_...md` (19 Files)**:
  - **Status**: 🟢 Complete Core Structure.
  - **Action**: **KEEP** existing content.
  - **Inject**: Add SSH/GPG commit signing snippet to `_01_22`.
  - **New File**: Create `_01_24_monorepos_and_git_scalar_lfs.md` (`[NEW]`).

---

### 2.2 Python Course Upgrade Plan (`_02_python`)

- **Existing 65 Files in `_02_python/`**:
  - **Status**: 🟡 Unindexed Legacy Drafts.
  - **Action**: **UPDATE METADATA** & **EXPAND**.
  - **Missing Sections to Inject**:
    1. YAML frontmatter header (Schema v2.0).
    2. 14 Standard `[id:]` section anchors (`[id: overview]`, `[id: prerequisites]`, `[id: theory]`, `[id: diagram]`, `[id: syntax]`, `[id: examples]`, `[id: exercises]`, `[id: common_mistakes]`, `[id: best_practices]`, `[id: interview_qa]`, `[id: quiz]`, `[id: lab]`, `[id: flashcards]`, `[id: summary]`).
    3. F-string string formatting updates.
  - **New Files to Create**:
    1. `_02_66_pattern_matching_match_case.md` (`[NEW]`)
    2. `_02_67_static_type_hinting_and_mypy.md` (`[NEW]`)
    3. `_02_68_asyncio_event_loop_and_async_await.md` (`[NEW]`)
    4. `_02_69_modern_packaging_pyproject_and_uv.md` (`[NEW]`)

---

### 2.3 Java Course Upgrade Plan (`_03_java`)

- **Existing 52 Files in `_03_java/`**:
  - **Status**: 🔴 Legacy Java 8/11 Drafts.
  - **Action**: **UPDATE METADATA** & **EXPAND**.
  - **Missing Sections to Inject**:
    1. YAML frontmatter header (Schema v2.0).
    2. 14 Standard `[id:]` section anchors.
    3. Java 21 syntax examples alongside traditional OOP examples.
  - **New Files to Create**:
    1. `_03_53_java21_record_classes_and_dtop.md` (`[NEW]`)
    2. `_03_54_java21_sealed_classes_and_interfaces.md` (`[NEW]`)
    3. `_03_55_java21_virtual_threads_project_loom.md` (`[NEW]`)
    4. `_03_56_java21_sequenced_collections.md` (`[NEW]`)

---

### 2.4 Selenium Course Upgrade Plan (`_04_selenium`)

- **Existing 48 Files in `_04_selenium/`**:
  - **Status**: 🔴 Legacy Selenium 3.x Drafts.
  - **Action**: **UPDATE METADATA** & **EXPAND**.
  - **Missing Sections to Inject**:
    1. YAML frontmatter header (Schema v2.0).
    2. Selenium Manager automatic binary driver management (eliminating `System.setProperty`).
    3. Relative Locators code snippets (`above`, `below`, `near`).
  - **New Files to Create**:
    1. `_04_49_selenium4_relative_locators.md` (`[NEW]`)
    2. `_04_50_chrome_devtools_protocol_cdp_interception.md` (`[NEW]`)
    3. `_04_51_bidi_websocket_realtime_automation.md` (`[NEW]`)

---

### 2.5 MySQL Course Upgrade Plan (`_05_mysql`)

- **Existing 42 Files in `_05_mysql/`**:
  - **Status**: 🟡 Solid Relational Core.
  - **Action**: **UPDATE METADATA** & **EXPAND**.
  - **Missing Sections to Inject**:
    1. YAML frontmatter header (Schema v2.0).
    2. 14 Standard `[id:]` section anchors.
  - **New Files to Create**:
    1. `_05_43_mysql8_analytical_window_functions.md` (`[NEW]`)
    2. `_05_44_mysql8_common_table_expressions_ctes.md` (`[NEW]`)
    3. `_05_45_mysql8_native_json_datatype_and_functions.md` (`[NEW]`)

---

### 2.6 C Systems Programming Upgrade Plan (`_06_c`)

- **Existing 25 Files in `_06_c/`**:
  - **Status**: 🟢 Strong Low-Level Foundation.
  - **Action**: **UPDATE METADATA** & **EXPAND**.
  - **Missing Sections to Inject**:
    1. YAML frontmatter header (Schema v2.0) across 23 remaining files.
    2. Modern C23 features (`constexpr`, `auto`, `typeof`).

---

### 2.7 C++ Course Upgrade Plan (`_07_cpp`)

- **Existing 30 Files in `_07_cpp/`**:
  - **Status**: 🟢 Strong OOP & Template Core.
  - **Action**: **UPDATE METADATA** & **EXPAND**.
  - **Missing Sections to Inject**:
    1. YAML frontmatter header (Schema v2.0) across 28 remaining files.
    2. 14 Standard `[id:]` section anchors.
  - **New Files to Create**:
    1. `_07_31_cpp20_smart_pointers_memory_safety.md` (`[NEW]`)
    2. `_07_32_cpp20_concepts_and_constraints.md` (`[NEW]`)
    3. `_07_33_cpp20_ranges_and_views.md` (`[NEW]`)

---

## 3. Upgrade Execution Standard Operating Procedure (SOP)

When upgrading an existing file:
1. Read target markdown file.
2. Verify YAML frontmatter block at the beginning of the file. If missing, insert standard Schema v2.0 frontmatter.
3. Verify section anchors `## N. Title [id: section_type]`. If missing, wrap existing headings into the 14 standard anchors.
4. Append modern technology delta snippets under `[id: syntax]` and `[id: examples]`.
5. Append interactive quiz JSON block under `[id: quiz]` and flashcard block under `[id: flashcards]`.
6. Save file and run `python scripts/migrate_markdown.py` to verify automated database ingestion.
