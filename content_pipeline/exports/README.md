# Learning OS — Authoritative Content Exports (`content_pipeline/exports/`)

_Authoritative Staging & Curriculum Management Area_  
_Architecture Version: 2.0.0_

---

## 1. Directory Structure

```
exports/
├── ARCHITECTURE_V2.md               # Learning OS v2 Core Standard & Rules
├── COURSE_CLASSIFICATION_REPORT.md  # Master Audit & Course Classification Matrix
├── MIGRATION_PLAN.md                # Structural Migration & Transformation Plan
├── MISSING_CANONICAL_COURSES.md     # Technology Justification & Analysis Report
├── AUDIT_BEFORE_MIGRATION.md        # Pre-Migration Baseline Snapshot
├── FINAL_EXPORT_AUDIT.md            # Post-Migration Verification & Completeness Audit
├── course_index.md                  # Master Index of All Canonical Courses
│
├── foundations/                     # Tier 1: 22 Zero-Prerequisite Baselines
├── technologies/                    # Tier 2: 55 Standalone Tool & Framework Courses
├── specializations/                 # Tier 3: 12 Professional Domain Integrations
├── learning_paths/                  # Tier 4: 9 Career Roadmaps (References Only)
│
└── archive/                         # Non-Destructive Historical Preservation
    ├── duplicate_courses/           # Preserved duplicate packages
    ├── legacy_bundles/              # Preserved monolithic multi-course dumps
    └── ARCHIVE_REGISTRY.md          # Comprehensive archive log & provenance
```

---

## 2. The Four Tiers at a Glance

1. **Foundations (`exports/foundations/` — 22 Courses):**
   - Pure, first-principles baseline languages, operating systems, mathematics, and electronics.
   - Zero prerequisite knowledge required; zero framework dependencies.

2. **Technologies (`exports/technologies/` — 55 Courses):**
   - Standalone tools, frameworks, libraries, platforms, databases, and protocols.
   - Teaches ONE technology completely from setup to production.

3. **Specializations (`exports/specializations/` — 12 Courses):**
   - Professional domain capabilities that integrate multiple prerequisite Foundations and Technologies.
   - Focuses strictly on cross-technology workflows, system architecture, and capstones.

4. **Learning Paths (`exports/learning_paths/` — 9 Paths):**
   - Career roadmaps defining milestones and course progression.
   - Contains NO syllabuses, NO lesson notes, and NO duplicated curriculum.

---

## 3. Core Axiom

> **"Teach Once. Reuse Everywhere."**
