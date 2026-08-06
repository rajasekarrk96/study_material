# Implementation Plan — RBAC & Content Proposal Workflow (v2.3 — Approved & Frozen)

This document is the approved and frozen architecture specification and implementation roadmap for the Learning Content Management System (LCMS) v2.3. No database, model, or directory structures may be redesigned from this point forward.

---

## STATUS: FROZEN
**Effective Date**: 2026-08-06
**Version**: v2.3

---

## 1. Bounded Context Separation

- **Knowledge Layer**: Isolated from user authentication and progress. Contains markdown content, media libraries, search indexing chunks, and taxonomy tags.
- **Curriculum Layer**: Governs courses, modules, lessons, topic coverage, and roadmaps.
- **Platform/Delivery Layer**: Enforces RBAC permissions, enrollments, billing states, and handles authentication.

---

## 2. Authentication Gateway & Future JWT SSO Addendum

To support both **Standalone Mode** and **External Authentication Mode** without changing application routes or business logic:

### Login Modes
1. **LOCAL Mode (`AUTH_MODE=LOCAL`)**: Users log in directly using the local `LocalAuthProvider`.
2. **JWT Mode (`AUTH_MODE=JWT`)**: Users are authenticated via a JWT token issued by Bytes & Boards. Validated by `ExternalAuthProvider`.
3. **AUTO Mode (`AUTH_MODE=AUTO`)**: If a valid JWT is present (in headers, cookies, or query parameters), use `ExternalAuthProvider`; otherwise, fall back to `LocalAuthProvider`.

### User Synchronization & Enrollments
- Validated external users are synchronized into the local `User` table, with status set to `External Account` and source `Bytes & Boards`.
- Course entitlements provided in the JWT are synchronized with the local `UserCourse` (enrollments) table.
- A Flask session is created upon successful token validation so that subsequent requests use local sessions without validating the JWT on every request.

---

## 3. Detailed Implementation Phases

- **Phase 1: Foundation**: Bounded Context project structures, SQLAlchemy models, relationships, and database schema migrations (Completed).
- **Phase 2: Authentication & Authorization**: `BaseAuthProvider`, `LocalAuthProvider`, `ExternalAuthProvider` interface, permission matrix, enrollments (`UserCourse`), and Flask-Login integration (Completed).
- **Phase 3: Knowledge Layer**: Media libraries (`Media`, `MediaFolder`), search indexes (`SearchDocument`, `SearchChunk`), tags, and slugs (Completed).
- **Phase 4: Curriculum Layer**: Course categories, topics, coverage metrics, and roadmap graphs (Completed).
- **Phase 5: Editorial Workflow**: Draft layers, proposals lifecycle, AI checks, versions rollback systems, and releases (Completed).
- **Phase 6: Content Pipeline**: Import/export packages and automated proposal generators (Completed).
- **Phase 7: Admin Panel**: CMS dashboard modules (Completed).
- **Phase 8: Staff Workflow**: suggestion triggers and drafts workspace (Completed).
- **Phase 9: Admin Workflow**: review console, diff checks, and merges (Completed).
- **Phase 10: Student Experience**: enrolled course validation and public previews (Completed).
- **Phase 11: API & Future Readiness**: service layers preparing for mobile and platform integrations (Completed).
