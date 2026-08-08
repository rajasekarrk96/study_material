# Hibernate & JPA — Master Syllabus

---

# Course Information

**Course Name:** Hibernate & JPA

**Category:** Technology Course

**Learning Path(s):**

- Java Full Stack
- Backend Development

**Difficulty:** Intermediate

**Estimated Duration:** 2 Hours

**Prerequisites:**

- Core Java
- SQL

**Course Status:** COMING_SOON

---

# Module 1 — ORM and JPA Foundations

## Lesson 1.1 — Persistence Architecture

**Course Coverage:** 🟢 Covered in Class

### Topics

- Object-relational impedance mismatch and ORM responsibilities
- JPA specification, provider, persistence context, and entity lifecycle
- Hibernate roles in standalone and Spring applications

## Lesson 1.2 — Project Configuration

**Course Coverage:** 🟢 Covered in Class

### Topics

- Dependencies, datasource, dialect, and schema settings
- EntityManagerFactory, EntityManager, and Spring-managed configuration
- Logging generated SQL and binding parameters

## Lesson 1.3 — First Entity and CRUD

**Course Coverage:** 🟢 Covered in Class

### Topics

- Entity, table, identifier, generated value, and column mapping
- persist, find, merge/update tracking, and remove
- Lab: implement CRUD for a Product entity

---

# Module 2 — Entity Mapping and Relationships

## Lesson 2.1 — Value and Type Mapping

**Course Coverage:** 🟢 Covered in Class

### Topics

- Basic fields, enums, temporal values, converters, and embedded types
- Identity, sequence, table, and application-assigned identifiers
- Validation constraints versus database constraints

## Lesson 2.2 — Associations

**Course Coverage:** 🟢 Covered in Class

### Topics

- Many-to-one, one-to-many, one-to-one, and many-to-many
- Owning side, mappedBy, join columns, and join tables
- Cascade operations and orphan removal

## Lesson 2.3 — Inheritance and Mapping Lab

**Course Coverage:** 🟢 Covered in Class

### Topics

- Single-table, joined, and table-per-class strategies
- Map Product and Category with bidirectional navigation
- Verify schema, inserts, updates, and deletes

---

# Module 3 — Queries and Data Access

## Lesson 3.1 — JPQL and HQL

**Course Coverage:** 🟢 Covered in Class

### Topics

- Entity-oriented select, joins, filtering, grouping, and ordering
- Named and positional parameters
- DTO projections and constructor expressions

## Lesson 3.2 — Criteria and Native Queries

**Course Coverage:** 🟢 Covered in Class

### Topics

- Type-safe dynamic queries with Criteria API
- Native SQL and result mapping
- Pagination, sorting, bulk update, and bulk delete

## Lesson 3.3 — Spring Data JPA

**Course Coverage:** 🟢 Covered in Class

### Topics

- Repository interfaces and derived query methods
- Custom @Query methods and specifications
- Lab: implement search and price filters in ProductRepository

---

# Module 4 — Transactions and Performance

## Lesson 4.1 — Transaction Management

**Course Coverage:** 🟢 Covered in Class

### Topics

- Transaction boundaries, propagation, isolation, and rollback
- Dirty checking, flush modes, and write-behind
- Optimistic and pessimistic locking

## Lesson 4.2 — Fetching and N+1

**Course Coverage:** 🟢 Covered in Class

### Topics

- Lazy versus eager loading
- N+1 diagnosis with SQL logs
- Fetch joins, entity graphs, batch fetching, and projections

## Lesson 4.3 — Caching and Tuning

**Course Coverage:** 🟢 Covered in Class

### Topics

- First-level and second-level cache concepts
- JDBC batching and ordered writes
- Lab: profile and optimize a relationship-heavy query

---

# Module 5 — Testing, Reliability, and Capstone

## Lesson 5.1 — Persistence Testing

**Course Coverage:** 🟢 Covered in Class

### Topics

- Repository slice and integration tests
- Test data setup, rollback, and database containers
- Verify mappings, constraints, queries, and concurrency

## Lesson 5.2 — Production Practices

**Course Coverage:** 🟢 Covered in Class

### Topics

- Schema migrations instead of automatic production DDL
- Connection pooling, timeouts, observability, and slow-query analysis
- Avoid Open Session in View and uncontrolled serialization

## Lesson 5.3 — Capstone: Transactional Data Service

**Course Coverage:** 🟢 Covered in Class

### Topics

- Model a multi-entity business domain
- Implement repositories, queries, validation, and transactional services
- Demonstrate N+1 remediation, locking, migrations, and automated tests

---

# Software & Tools

- Hibernate
- JPA
- Maven

---

# Hardware Requirements

- A computer with the JDK and a database installed

---

# Course Completion Summary

**Estimated Hours:** 2 Hours

**Modules:** 5

**Lessons:** 15

**Topics:** 45+

**Difficulty:** Intermediate

**Course Status:** COMING_SOON
