---
id: "05_11"
title: "Database Security Administration and Replication"
course: "MySQL"
module: 5
module_title: "Administration"
lesson: 11
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["CREATE-USER", "GRANT", "REVOKE", "privileges", "SSL", "roles", "backup", "mysqldump", "mysqlpump", "binary-log", "replication", "master-slave"]
prerequisites: []
lab_required: true
---

## Topics Covered

### 1. User Management
```sql
CREATE USER 'app_user'@'%' IDENTIFIED BY 'StrongPass123!';
CREATE USER 'read_only'@'192.168.1.%' IDENTIFIED WITH caching_sha2_password BY 'Pass!';

GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'app_user'@'%';
GRANT SELECT ON mydb.* TO 'read_only'@'%';
GRANT ALL PRIVILEGES ON mydb.* TO 'admin'@'localhost';

REVOKE INSERT ON mydb.orders FROM 'app_user'@'%';
DROP USER 'old_user'@'%';
FLUSH PRIVILEGES;
```

### 2. MySQL Roles (8.0+)
```sql
CREATE ROLE 'app_read', 'app_write', 'admin';
GRANT SELECT ON mydb.* TO 'app_read';
GRANT INSERT, UPDATE, DELETE ON mydb.* TO 'app_write';
GRANT ALL ON *.* TO 'admin';

GRANT 'app_read', 'app_write' TO 'dev_user'@'%';
SET DEFAULT ROLE ALL TO 'dev_user'@'%';
```

### 3. Backup and Restore
```bash
# Full dump
mysqldump -u root -p --all-databases --single-transaction > backup.sql

# Restore
mysql -u root -p < backup.sql

# Binary log backup (point-in-time recovery)
mysqlbinlog /var/log/mysql/mysql-bin.000001 | mysql -u root -p
```

### 4. Replication Overview
```
Primary (writes) → binary log → Replica (reads)
```
```sql
-- On primary
CREATE USER 'repl'@'%' IDENTIFIED BY 'ReplPass!';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';

-- On replica
CHANGE MASTER TO MASTER_HOST='primary_ip', MASTER_USER='repl', ...;
START SLAVE;
SHOW SLAVE STATUS\G;
```

## Lab
Set up a read-only reporting user with table-level restrictions, back up a database, simulate point-in-time recovery using binary logs.
