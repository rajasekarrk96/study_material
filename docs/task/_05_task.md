# Task 05 — Enterprise CMS Dashboard & RBAC Rules

> **Goal**: Deploy role-based permission check decorators (RBAC), build the administrative CMS dashboard, structure edit workflows, and define SEO tags.

---

## 5.1 RBAC Authentication Decorators & Permissions
- [ ] Middleware security:
  - Code `@require_role` and `@require_min_role` check hooks parsing roles profiles.
- [ ] User and Role database keys:
  - Seed baseline parameters into tables: `roles` and `permissions`.
  - Wire checks within route controllers restricting administrative pages.

---

## 5.2 Content Review Pipelines & Ingestion Dashboards
- [ ] Draft workspace templates:
  - Create admin templates showing upload dropzones, link inputs, chunk monitors, and edit boards.
- [ ] Quality assurance pipelines:
  - Integrate readability checks (Flesch metrics checks) and plagiarism validation triggers.
  - Create the `content_quality_scores` database table.

---

## 5.3 Automated SEO Strategy
- [ ] Schema.org markup generation:
  - Setup Jinja layout macros formatting dynamic JSON-LD metadata for Courses and Lessons.
- [ ] Sitemaps background job:
  - Create background schedule updating `sitemap.xml` entries nightly.

---

## 🛑 CHECKPOINT & BREAK POINT
- Test administrative dashboard access restrictions using a mock Student profile (verifying they receive `403 Forbidden` errors).
- Verify published lessons contain valid structured schema.org markdown metadata tags by testing them against validator standards.
- **Action**: Pause and request approval before executing deployment steps.
