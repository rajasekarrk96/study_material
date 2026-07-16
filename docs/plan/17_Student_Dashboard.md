# 17 — Student Dashboard

> The Student Dashboard offers personalized insights into learning streaks, active courses, quiz scores, and achievements.

---

## 17.1 UI Mockup

```
┌────────────────────────────────────────────────────────────────────────┐
│ [Logo] Learning OS Dashboard              [Notifications] [My Profile] │
├────────────────────────────────────────────────────────────────────────┤
│  Sidebar          │ Welcome Back, Student!                             │
│  ────────        │ ──────────────────────                             │
│  [Catalog]        │ Level: 4    XP: 920/1600   Daily Streak: 🔥 5 Days  │
│  [My Courses]     │ [====== Progress Bar 58% =======]                  │
│  [Quiz Analytics] │                                                    │
│  [Exercise Log]   │ Active Learning Paths                              │
│  [Spaced Rep]     │ ──────────────────────                             │
│  [Flashcards]     │ - Core Python Roadmap [Resume Lesson: Functions]   │
│  [Bookmarks]      │ - MySQL Basics [Next Up: Joins]                    │
│  [My Notes]       │                                                    │
│                   │ Spaced Repetition Revision Schedule                │
│                   │ ───────────────────────────────────                │
│                   │ - Loop Syntax: Overdue (Review Now)                │
│                   │ - Class Polymorphism: Due tomorrow                 │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 17.2 Core Experience Features

### 1. Streaks Tracker & Weekly Heatmap
A calendar grid showing the days the student was active. Helps maintain daily engagement.

### 2. Spaced Repetition & Revision Pipeline
Pulls review alerts from the Spaced Repetition tables to notify users when topic summaries or flashcards require study.

### 3. Bookmarks & Personal Notes Layer
Aggregates student-created study cards, personal annotations, and bookmarked lesson files into a single, searchable notebook dashboard.

### 4. Dynamic Recommendation Panel
Suggests lessons based on completed prerequisites and cosine similarity calculations.
