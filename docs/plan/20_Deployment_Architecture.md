# 20 — Deployment Architecture

> The Deployment Architecture outlines system infrastructure, CI/CD procedures, scaling capabilities, and backup topologies.

---

## 20.1 Infrastructure Topology (Production Environment)

The production configuration runs on **Render** paired with **TiDB Serverless Cloud**.

```
                           ┌────────────────────────┐
                           │   Client Web Browser   │
                           └───────────┬────────────┘
                                       │
                                       ▼
                       ┌────────────────────────────────┐
                       │      Render Cloud (App)        │
                       │   (Flask App + Background Job)  │
                       └───────────────┬────────────────┘
                                       │
                ┌──────────────────────┴──────────────────────┐
                ▼                                             ▼
 ┌─────────────────────────────┐               ┌─────────────────────────────┐
 │       TiDB Serverless       │               │      Redis Cache Cloud      │
 ├─────────────────────────────┤               ├─────────────────────────────┤
 │ MySQL-compatible DB,        │               │ Stores rate limit metrics,  │
 │ transactional scale.        │               │ and system-wide page caches.│
 └─────────────────────────────┘               └─────────────────────────────┘
```

---

## 20.2 Scaling Strategies

1. **Horizontal App Autoscaling**: The Flask runtime container on Render spins up additional instances if CPU usage surpasses 70%. Sessions are shared via cookie cryptography keys or stored in Redis, ensuring stateless operations.
2. **Read/Write DB Decoupling**: For intense workloads, TiDB handles automatic shard scaling. Write operations hit transactional clusters, while read operations read from replicas.
3. **FTS Offloading**: The full-text search engine can be migrated from Postgres FTS/SQLite FTS to an external Meilisearch cluster, decoupling indexing load from transactional resources.

---

## 20.3 Database Backups

- Backups run nightly via an automated Cron background job.
- Generates a full SQL dump along with a ZIP file containing the media directory.
- Encrypts and uploads archives to secure S3 bucket storages.
- Retains backups using a grandfather-father-son policy: daily backups are kept for 7 days, weekly for 4 weeks, and monthly for 12 months.
