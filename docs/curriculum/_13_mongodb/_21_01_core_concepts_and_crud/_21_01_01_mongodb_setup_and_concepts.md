---
id: "21_01_01"
title: "MongoDB Setup and Core Concepts"
course: "MongoDB"
module: 1
module_title: "Core Concepts and CRUD"
lesson: 1
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["mongodb", "nosql", "document", "bson", "json", "mongosh", "atlas"]
prerequisites: []
lab_required: true
---

# MongoDB Setup and Core Concepts


## What is MongoDB?

MongoDB is a document-oriented NoSQL database that stores data in flexible, JSON-like BSON documents.

### Key Terminology Comparison

| Relational (SQL) | MongoDB (NoSQL) |
|---|---|
| Database | Database |
| Table | Collection |
| Row | Document |
| Column | Field |
| Primary Key (`id`) | Primary Key (`_id`) |

```javascript
// Example BSON Document
{
  "_id": ObjectId("64b8f1a2e4b0a123456789ab"),
  "name": "Raja",
  "email": "raja@example.com",
  "age": 28,
  "skills": ["Python", "MongoDB", "SQL"],
  "isActive": true
}
```

## Lab Exercise
1. Install MongoDB Shell (`mongosh`), connect to a local instance or MongoDB Atlas cluster, and run `db.version()`.
