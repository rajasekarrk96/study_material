# Task 06 — Production Scaling & Deployment

> **Goal**: Configure container deployments matching Render cloud standards, configure PostgreSQL/PGVector configurations, set up Redis rate-limiting services, and configure automated backups.

---

## 6.1 Cloud Databases Setup & Migrations
- [x] Production Database Integration (TiDB serverless):
  - Setup connections targeting TiDB Cloud using SSL certificates keys mappings.
  - Enable Postgres PGVector or TiDB compatibility wrappers inside production config matrices.
- [x] Alembic Migration Run:
  - Verify migration chains match production schemas: `alembic upgrade head`.

---

## 6.2 Redis Rate Limiting & Performance Cache
- [x] Rate limiters setup:
  - Wire Redis connection setups tracking requests limits across auth controllers and AI generation pathways.
- [x] Memory caching:
  - Cache heavy database queries (e.g. course catalogs, topic nodes lists).

---

## 6.3 Render deployment configuration
- [x] Deployment blueprints:
  - Create standard `render.yaml` configuration profiles mapping web server execution parameters, background worker schedules, and SSL values.
- [x] Automated Backups:
  - Schedule cron scripts compiling daily database dumps and asset directories, uploading them encrypted to external S3 buckets.

---

## 🛑 CHECKPOINT & FINAL WALKTHROUGH
- Run the full test suite (`python run_tests.py`) to verify all modules function correctly under local environment profiles.
- Confirm live database queries evaluate search items properly.
- **Action**: Compile the final `walkthrough.md` report showing screenshots and recordings of the system features.
