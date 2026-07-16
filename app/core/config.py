"""
Learning OS — Core Configuration
Loads environment variables and builds typed config objects.
"""
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class DatabaseConfig:
    database_type: str
    database_uri: str
    tidb_ssl_ca: str


@dataclass
class AppConfig:
    secret_key: str
    encryption_key: str
    debug: bool
    db: DatabaseConfig


def _build_database_uri() -> str:
    db_type = os.environ.get("DATABASE_TYPE", "sqlite").lower()
    if db_type == "tidb":
        url = os.environ.get("DATABASE_URL", "")
        return url
    # SQLite fallback
    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")
    os.makedirs(data_dir, exist_ok=True)
    return f"sqlite:///{os.path.join(data_dir, 'learning_os.db')}"


def _load_config() -> AppConfig:
    return AppConfig(
        secret_key=os.environ.get("SECRET_KEY", "dev-insecure-secret-change-me"),
        encryption_key=os.environ.get("ENCRYPTION_KEY", ""),
        debug=os.environ.get("FLASK_ENV", "development") == "development",
        db=DatabaseConfig(
            database_type=os.environ.get("DATABASE_TYPE", "sqlite"),
            database_uri=_build_database_uri(),
            tidb_ssl_ca=os.environ.get("TIDB_CA_PATH", ""),
        ),
    )


config: AppConfig = _load_config()
