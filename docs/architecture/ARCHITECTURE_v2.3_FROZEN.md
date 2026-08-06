# STATUS: FROZEN
**Effective Date**: 2026-08-06
**Version**: v2.3

> [!IMPORTANT]
> This architecture is frozen.
> New features must be implemented within this architecture.
> Schema modifications require a new architecture version (v2.4+).
> Implementation bugs do NOT justify architectural redesign.

---

# Enterprise LCMS Architecture Specification v2.3

This document specifies the Bounded Context architecture for the Learning Content Management System (LCMS). It partitions the system into three main layers: Knowledge, Curriculum, and Platform/Delivery.

## 1. Bounded Context Separation

```mermaid
graph TD
    subgraph Knowledge Layer
        Markdown[Markdown Content]
        Media[Media Assets]
        Search[Search Index]
        Tags[Taxonomy Tags]
    end

    subgraph Curriculum Layer
        Course[Courses & Categories]
        Module[Modules & Lessons]
        Topic[Topics & Sections]
        Roadmap[Prerequisite Graph]
    end

    subgraph Platform Layer
        Auth[Auth Provider Registry]
        User[Users & Roles]
        Enrollment[User Course Entitlements]
        Progress[Progress Logs]
        Workflow[Editorial proposals]
    end

    Knowledge Layer --> Curriculum Layer
    Curriculum Layer --> Platform Layer
```

### Knowledge Layer
- Focuses entirely on pure content storage, media linkage, search metadata indexing, and general tagging.
- Completely isolated from users, enrollments, billing, or progress tracking.

### Curriculum Layer
- Binds knowledge resources into reusable structured units (Courses, Modules, Lessons, Sections, Roadmaps).
- Free from auth logic, allowing offline pipeline generation or contributor exports.

### Platform Layer
- Handles delivery concerns, dynamic permissions matrices, student enrollments, progress tracking, and integration hookups (JWT authentication).

## 2. Review Workflow States
A Content Proposal progresses through these states:
`Draft` ➔ `Submitted` ➔ `AI Review` ➔ `Pending Review` ➔ `Under Review` ➔ `Changes Requested` ➔ `Approved` ➔ `Merged` ➔ `Published`
