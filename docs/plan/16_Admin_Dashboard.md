# 16 — Admin Dashboard

> The Admin Dashboard manages content review pipelines, platform settings, media files, and SEO configs.

---

## 16.1 Layout & Visual Mockup

```
┌────────────────────────────────────────────────────────────────────────┐
│ [Logo] Learning OS Admin Panel               [Admin Settings] [Profile]│
├────────────────────────────────────────────────────────────────────────┤
│  Sidebar          │ Dashboard Metrics Overview                         │
│  ────────        │ ──────────────────────────                         │
│  [CMS Home]       │ Total Users: 12,422 (▲12%)  Total Courses: 45      │
│  [Lessons Drafts] │ Live Quizzes: 243           Job Status: Healthy    │
│  [Reviews Queue]  │                                                    │
│  [Quiz Bank]      │ Review Pipeline Queue                              │
│  [User Roles]     │ ─────────────────────                              │
│  [Analytics]      │ 1. "Java Multithreading" - Author: Alice [Review]  │
│  [SEO/Sitemap]    │ 2. "SQL Indexes" - Author: Bob         [Review]  │
│  [Media Manager]  │                                                    │
│  [Job Monitor]    │ Background Workers Status                          │
│                   │ ─────────────────────────                          │
│                   │ FTS Rebuild Job: COMPLETED   Backup: Pending       │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 16.2 Core Modules

### 1. CMS Management Portal
Allows administrators and editors to organize courses, manage modules, configure lessons, and track editing versions.

### 2. Peer Review Portal
Enables reviewers to examine lesson drafts submitted by authors, approve/reject them, and write feedback comments.

### 3. User & Role Management (RBAC Dashboard)
Super admins can create system roles, assign permissions, verify student accounts, or lock accounts to prevent access.

### 4. Search and Indexing Controls
Provides manual triggers to rebuild full-text search indexes or synchronize indexing clusters.

### 5. Media & Assets Management
Stores, compresses, and links media files (images, diagrams, downloads) to lesson sections.
