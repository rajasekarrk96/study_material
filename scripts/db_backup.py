#!/usr/bin/env python3
"""
Bytes and Boards Solutions — Database Backup Script.
Dumps every table's schema (CREATE TABLE) and rows (INSERT statements) to a
single timestamped .sql file under backups/, restorable via any MySQL client.
"""
import os
import sys
import logging
from datetime import datetime
from pathlib import Path

import pymysql
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("backup_pipeline")

BACKUP_DIR = Path(__file__).parent.parent / "backups"


def _connect():
    db_type = os.environ.get("DATABASE_TYPE", "sqlite")
    if db_type != "tidb":
        raise RuntimeError(f"db_backup.py only supports DATABASE_TYPE=tidb (got '{db_type}')")

    return pymysql.connect(
        host=os.environ["TIDB_HOST"],
        port=int(os.environ.get("TIDB_PORT", 4000)),
        user=os.environ["TIDB_USER"],
        password=os.environ["TIDB_PASSWORD"],
        database=os.environ["TIDB_DATABASE"],
        ssl_ca=os.environ.get("TIDB_CA_PATH") or None,
        connect_timeout=30,
    )


def run_database_backup() -> Path:
    """Dumps every table's schema + rows to a timestamped .sql file. Returns the file path."""
    logger.info("Connecting to TiDB Cloud...")
    conn = _connect()
    cur = conn.cursor()

    BACKUP_DIR.mkdir(exist_ok=True)
    backup_path = BACKUP_DIR / f"backup_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.sql"

    cur.execute("SHOW TABLES")
    tables = [row[0] for row in cur.fetchall()]
    logger.info("Found %d tables to back up.", len(tables))

    total_rows = 0
    with open(backup_path, "w", encoding="utf-8") as f:
        f.write(f"-- Learning OS database backup — {datetime.utcnow().isoformat()}Z\n")
        f.write("SET FOREIGN_KEY_CHECKS=0;\n\n")

        for table in tables:
            cur.execute(f"SHOW CREATE TABLE `{table}`")
            create_stmt = cur.fetchone()[1]
            f.write(f"-- Table: {table}\nDROP TABLE IF EXISTS `{table}`;\n{create_stmt};\n\n")

            cur.execute(f"SELECT * FROM `{table}`")
            rows = cur.fetchall()
            col_names = [d[0] for d in cur.description]
            if rows:
                col_list = ", ".join(f"`{c}`" for c in col_names)
                for row in rows:
                    values = ", ".join(conn.escape(v) for v in row)
                    f.write(f"INSERT INTO `{table}` ({col_list}) VALUES ({values});\n")
                total_rows += len(rows)
            f.write("\n")
            logger.info("Backed up %-32s %d rows", table, len(rows))

        f.write("SET FOREIGN_KEY_CHECKS=1;\n")

    conn.close()
    size_mb = backup_path.stat().st_size / (1024 * 1024)
    logger.info("Backup complete: %s (%d rows, %.2f MB)", backup_path, total_rows, size_mb)
    return backup_path


if __name__ == "__main__":
    run_database_backup()
