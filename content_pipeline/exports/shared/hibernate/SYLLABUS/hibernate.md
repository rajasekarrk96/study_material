# Hibernate & JPA -- Syllabus

> Source: `_source_java_full_stack.md`



#### 2.7.1. Module 1 — ORM and JPA Foundations

1. **Persistence Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Object-relational impedance mismatch and ORM responsibilities
    2. JPA specification, provider, persistence context, and entity lifecycle
    3. Hibernate roles in standalone and Spring applications
2. **Project Configuration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Dependencies, datasource, dialect, and schema settings
    2. EntityManagerFactory, EntityManager, and Spring-managed configuration
    3. Logging generated SQL and binding parameters
3. **First Entity and CRUD**
    - **Course Coverage:** 🟢 Covered in Class
    1. Entity, table, identifier, generated value, and column mapping
    2. persist, find, merge/update tracking, and remove
    3. Lab: implement CRUD for a Product entity

#### 2.7.2. Module 2 — Entity Mapping and Relationships

1. **Value and Type Mapping**
    - **Course Coverage:** 🟢 Covered in Class
    1. Basic fields, enums, temporal values, converters, and embedded types
    2. Identity, sequence, table, and application-assigned identifiers
    3. Validation constraints versus database constraints
2. **Associations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Many-to-one, one-to-many, one-to-one, and many-to-many
    2. Owning side, mappedBy, join columns, and join tables
    3. Cascade operations and orphan removal
3. **Inheritance and Mapping Lab**
    - **Course Coverage:** 🟢 Covered in Class
    1. Single-table, joined, and table-per-class strategies
    2. Map Product and Category with bidirectional navigation
    3. Verify schema, inserts, updates, and deletes

#### 2.7.3. Module 3 — Queries and Data Access

1. **JPQL and HQL**
    - **Course Coverage:** 🟢 Covered in Class
    1. Entity-oriented select, joins, filtering, grouping, and ordering
    2. Named and positional parameters
    3. DTO projections and constructor expressions
2. **Criteria and Native Queries**
    - **Course Coverage:** 🟢 Covered in Class
    1. Type-safe dynamic queries with Criteria API
    2. Native SQL and result mapping
    3. Pagination, sorting, bulk update, and bulk delete
3. **Spring Data JPA**
    - **Course Coverage:** 🟢 Covered in Class
    1. Repository interfaces and derived query methods
    2. Custom @Query methods and specifications
    3. Lab: implement search and price filters in ProductRepository

#### 2.7.4. Module 4 — Transactions and Performance

1. **Transaction Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Transaction boundaries, propagation, isolation, and rollback
    2. Dirty checking, flush modes, and write-behind
    3. Optimistic and pessimistic locking
2. **Fetching and N+1**
    - **Course Coverage:** 🟢 Covered in Class
    1. Lazy versus eager loading
    2. N+1 diagnosis with SQL logs
    3. Fetch joins, entity graphs, batch fetching, and projections
3. **Caching and Tuning**
    - **Course Coverage:** 🟢 Covered in Class
    1. First-level and second-level cache concepts
    2. JDBC batching and ordered writes
    3. Lab: profile and optimize a relationship-heavy query

#### 2.7.5. Module 5 — Testing, Reliability, and Capstone

1. **Persistence Testing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Repository slice and integration tests
    2. Test data setup, rollback, and database containers
    3. Verify mappings, constraints, queries, and concurrency
2. **Production Practices**
    - **Course Coverage:** 🟢 Covered in Class
    1. Schema migrations instead of automatic production DDL
    2. Connection pooling, timeouts, observability, and slow-query analysis
    3. Avoid Open Session in View and uncontrolled serialization
3. **Capstone: Transactional Data Service**
    - **Course Coverage:** 🟢 Covered in Class
    1. Model a multi-entity business domain
    2. Implement repositories, queries, validation, and transactional services
    3. Demonstrate N+1 remediation, locking, migrations, and automated tests
