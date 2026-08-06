# Folder Structure Reference

**Updated:** 2026-08-06

---

## Complete Directory Tree

```
content_pipeline/
│
├── README.md                    ← System overview
├── PIPELINE_OVERVIEW.md         ← Architecture diagrams
├── EXPORT_WORKFLOW.md           ← Export process
├── IMPORT_WORKFLOW.md           ← Import process
├── REVIEW_WORKFLOW.md           ← Review process
├── MERGE_WORKFLOW.md            ← Merge process
├── ARCHIVE_WORKFLOW.md          ← Archive process
├── FOLDER_STRUCTURE.md          ← This file
├── VERSIONING.md                ← Version and ID system
├── CONTRIBUTOR_DOCS.md          ← For contributors
├── REVIEWER_DOCS.md             ← For reviewers
├── ADMIN_DOCS.md                ← For administrators
│
├── exports/                     ← Active export packages
│   │
│   ├── shared/                  ← Individual reusable course packages
│   │   ├── _01_c_programming/
│   │   ├── _02_cpp_programming/
│   │   ├── _03_git_version_control/
│   │   ├── _04_html5/
│   │   ├── _05_css3/
│   │   ├── _06_bootstrap/
│   │   ├── _07_javascript/
│   │   ├── _08_jquery/
│   │   ├── _09_python_core/
│   │   ├── _10_advanced_python/
│   │   ├── _11_java_core/
│   │   ├── _12_spring_boot/
│   │   ├── _13_mysql/
│   │   ├── _14_sql_server/
│   │   ├── _15_mongodb/
│   │   ├── _16_flask/
│   │   ├── _17_fastapi/
│   │   ├── _18_rest_api/
│   │   ├── _19_auth_jwt/
│   │   ├── _20_react/
│   │   ├── _21_selenium/
│   │   ├── _22_linux/
│   │   ├── _23_docker/
│   │   └── ...
│   │
│   ├── learning_paths/          ← Full learning path packages
│   │   ├── python_full_stack/
│   │   ├── java_full_stack/
│   │   ├── frontend_engineering/
│   │   ├── backend_engineering/
│   │   ├── data_science/
│   │   ├── ai_engineering/
│   │   ├── devops/
│   │   ├── cloud_engineering/
│   │   ├── iot_full_stack/
│   │   └── dotnet_full_stack/
│   │
│   └── specializations/         ← Specialization packages
│       ├── machine_learning/
│       ├── deep_learning/
│       ├── computer_vision/
│       ├── nlp/
│       ├── mlops/
│       ├── powerbi/
│       ├── tableau/
│       ├── excel/
│       ├── mongodb/
│       ├── big_data/
│       ├── hadoop/
│       ├── spark/
│       ├── airflow/
│       ├── kubeflow/
│       ├── mlflow/
│       ├── pcb_design/
│       ├── esp32/
│       └── arduino/
│
├── imports/                     ← Returned packages in various states
│   ├── pending_review/          ← Just returned, not yet audited
│   ├── under_review/            ← Being reviewed right now
│   ├── approved/                ← Passed review, ready to merge
│   └── rejected/                ← Needs corrections
│
├── completed/                   ← Permanently archived packages
│   ├── shared/
│   ├── learning_paths/
│   └── specializations/
│
├── reports/                     ← System-wide reports
│   ├── AUDIT_REPORT_*.md
│   ├── CURRICULUM_HEALTH_*.md
│   ├── SYLLABUS_COVERAGE_*.md
│   ├── DUPLICATE_REPORT_*.md
│   ├── QUALITY_REPORT_*.md
│   ├── MERGE_REPORT_*.md
│   └── CONFLICT_REPORT_*.md
│
├── templates/                   ← Reusable document templates
│   ├── PACKAGE_MANIFEST.md
│   ├── README_template.md
│   ├── COURSE_METADATA_template.md
│   ├── STYLE_GUIDE.md
│   ├── NOTE_TEMPLATE.md
│   ├── CHECKLIST_template.md
│   ├── VALIDATION_RULES.md
│   ├── CONTRIBUTOR_GUIDE_template.md
│   ├── REPORT_template.md
│   ├── REVIEW_COMMENTS.md
│   ├── REJECTION_NOTICE.md
│   └── MERGE_REQUEST.md
│
├── scripts/                     ← Automation scripts
│   ├── export_shared.py
│   ├── export_learning_path.py
│   ├── export_specialization.py
│   ├── validate_import.py
│   ├── audit_package.py
│   ├── move_to_review.py
│   ├── approve_package.py
│   ├── reject_package.py
│   ├── merge_package.py
│   ├── verify_merge.py
│   ├── archive_package.py
│   ├── list_packages.py
│   └── search_archive.py
│
└── registry/                    ← Package tracking
    ├── PACKAGE_REGISTRY.md
    ├── ACTIVE_EXPORTS.md
    └── ARCHIVE_INDEX.md
```

---

## Naming Conventions

### Export Packages

| Type | Convention | Example |
|---|---|---|
| Shared course | `_NN_<slug>/` | `_06_javascript/` |
| Learning path | `<slug>/` | `frontend_engineering/` |
| Specialization | `<slug>/` | `machine_learning/` |

### Import Packages

All imports use the `package_id` as the folder name:
```
imports/pending_review/PKG-20260806-JS-001/
```

### Archive Packages

```
completed/<type>/PKG-<id>_v<version>_<merged_date>/
```

### Reports

```
reports/AUDIT_REPORT_<package_id>_<date>.md
reports/MERGE_REPORT_<package_id>_<date>.md
```
