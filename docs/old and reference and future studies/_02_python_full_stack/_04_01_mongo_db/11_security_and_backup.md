# MongoDB Security & Maintenance

## 1. Security & RBAC (Role-Based Access Control)
MongoDB uses RBAC to govern access to a MongoDB system. A user is granted one or more **roles** that determine the user’s access to database resources and operations.

### Key Concepts
- **Authentication**: Verifying the identity of a user (e.g., via SCRAM, LDAP, Kerberos, or x.509 certificates).
- **Authorization**: Determining what an authenticated user can do (via Roles).
- **Encryption at Rest**: Encrypting data on disk to prevent unauthorized access to the underlying storage files.
- **Auditing**: Recording a trail of administrative and data access actions.

### Common Built-in Roles
- `read`: Read-only access to a specific database.
- `readWrite`: Full access to read and modify data in a specific database.
- `dbAdmin`: Administrative tasks for a database (indexing, stats).
- `root`: Absolute control over the entire system (admin database only).

---

## 2. Backup & Restore (Maintenance)
Regular backups are critical for disaster recovery.

### Tool 1: mongodump & mongorestore (Binary BSON)
Used for small to medium databases. It reads data from the database and creates BSON files.
- **Backup**:
  ```bash
  mongodump --db=interview_prep --out=/backups/backup_01
  ```
- **Restore**:
  ```bash
  mongorestore --db=interview_prep_restored /backups/backup_01/interview_prep
  ```

### Tool 2: mongoexport & mongoimport (JSON/CSV)
Utility for exporting/importing data in human-readable formats. Not recommended for full backups as it doesn't preserve BSON data types perfectly (e.g., Dates).
- **Export to JSON**:
  ```bash
  mongoexport --db=interview_prep --collection=users --out=users.json
  ```

---

## Practice Questions (Interview Style)

**Q1 (Easy): What is the difference between Authentication and Authorization?**
*Solution:* 
Authentication is "Who are you?" (proving identity). Authorization is "What are you allowed to do?" (applying permissions/roles).

**Q2 (Easy): Which command would you use to create a binary backup of a specific MongoDB database named `prod_db`?**
*Solution:* 
`mongodump --db=prod_db`

**Q3 (Medium): Why is `mongoexport` generally considered inferior to `mongodump` for database backups intended for disaster recovery?**
*Solution:* 
`mongoexport` exports to JSON/CSV, which are not type-aware in the same way BSON is. When you re-import JSON, certain specific MongoDB types (like `ISODate` or `Long`) might be interpreted as strings or other generic types, leading to data fidelity loss. `mongodump` preserves the raw BSON binary format exactly as it exists in the database.

**Q4 (Medium): You want a user to be able to read and write to the `app_db` database but not perform administrative tasks like dropping the database or creating users. Which built-in role should you assign?**
*Solution:* 
The `readWrite` role on the `app_db` database.

**Q5 (Hard - Scenario): Your organization requires "Encryption at Rest". How does this affect the mongodump utility? Do you need to do anything special during restore?**
*Solution:* 
Encryption at Rest (WiredTiger encryption) happens at the storage engine layer. When you run `mongodump`, the `mongod` process decrypts the data in memory before streaming it to the utility as BSON. Therefore, the resulting dump files are **NOT encrypted** by default. You must secure the backup files yourself (e.g., by placing them on an encrypted volume or using external encryption tools). During `mongorestore`, you simply restore them to another encrypted `mongod` instance.
