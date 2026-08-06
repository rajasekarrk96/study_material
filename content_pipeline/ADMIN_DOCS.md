# Administrator Documentation

**Learning OS Content Pipeline — Admin Guide**  
**Updated:** 2026-08-06

---

## Administrator Responsibilities

Administrators manage the full pipeline lifecycle:
- Creating and sending export packages
- Managing the contributor registry
- Overseeing merge operations
- Maintaining the package registry
- Running system-wide health checks
- Managing concurrent exports without conflicts

---

## Creating an Export

### Shared Course

```bash
python content_pipeline/scripts/export_shared.py \
    --course javascript \
    --assigned-to "contributor-name" \
    --deadline 2026-08-20 \
    --version 1.0.0
```

### Learning Path

```bash
python content_pipeline/scripts/export_learning_path.py \
    --path frontend_engineering \
    --assigned-to "team-name" \
    --deadline 2026-09-01
```

### Specialization

```bash
python content_pipeline/scripts/export_specialization.py \
    --course machine_learning \
    --assigned-to "ml-team" \
    --deadline 2026-09-15
```

---

## Managing the Registry

```bash
# View all active exports
python content_pipeline/scripts/list_packages.py --state exported

# View all pending review
python content_pipeline/scripts/list_packages.py --state pending_review

# View pipeline summary
python content_pipeline/scripts/list_packages.py --summary
```

---

## Running a Merge

```bash
# 1. Dry run
python content_pipeline/scripts/merge_package.py \
    --package imports/approved/<package_id> \
    --dry-run

# 2. Review dry run output in reports/

# 3. Execute merge
python content_pipeline/scripts/merge_package.py \
    --package imports/approved/<package_id> \
    --execute \
    --admin "your-name"

# 4. Verify
python content_pipeline/scripts/verify_merge.py \
    --package imports/approved/<package_id>

# 5. Archive
python content_pipeline/scripts/archive_package.py \
    --package imports/approved/<package_id>
```

---

## Concurrent Export Management

Rules to prevent conflicts:
1. The same course can only have ONE active export per version at a time
2. If you need a second export of the same course, bump the version
3. The registry tracks active exports — always check before creating a new one

```bash
# Check if a course is currently exported
python content_pipeline/scripts/list_packages.py --course javascript --state exported
```

---

## Conflict Detection

If a syllabus changes after a package was exported:

```bash
python content_pipeline/scripts/check_conflicts.py --package imports/pending_review/<package_id>
```

This compares the package's `syllabus_version` against the current Learning OS syllabus and reports:
- Added lessons (new stubs missing from package)
- Removed lessons (package has lessons that no longer exist)
- Renamed modules (structural changes)

---

## System Health Check

```bash
# Full pipeline health check
python content_pipeline/scripts/pipeline_health.py
```

Generates `reports/PIPELINE_HEALTH_<date>.md` with:
- Active exports count and age
- Pending review queue
- Overdue packages
- Registry integrity
- Archive completeness

---

## Registry Maintenance

`registry/PACKAGE_REGISTRY.md` — Master registry of all packages  
`registry/ACTIVE_EXPORTS.md` — Currently active (unreturned) packages only  
`registry/ARCHIVE_INDEX.md` — Index of all archived packages  

These are auto-updated by the scripts. Manual edits should only be made with great care and must be documented.
