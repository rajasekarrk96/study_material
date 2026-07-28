---
id: "02_08_03"
title: "Logging Module"
course: "Python"
module: 8
module_title: "Exceptions and File I/O"
lesson: 3
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["logging", "Logger", "Handler", "Formatter", "basicConfig", "FileHandler", "RotatingFileHandler", "levels", "structlog", "rich-logging"]
prerequisites: []
lab_required: true
---

# Logging Module


## Python Logging Overview

```python
import logging

# Basic setup
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

logger.debug("Debug message — detailed diagnostic")
logger.info("Info message — general events")
logger.warning("Warning — unexpected but handled")
logger.error("Error — operation failed")
logger.critical("Critical — program may not recover")
```

## Log Levels

| Level | Value | When to Use |
|---|---|---|
| DEBUG | 10 | Detailed diagnostic information |
| INFO | 20 | Confirmation things are working |
| WARNING | 30 | Unexpected, but recoverable |
| ERROR | 40 | Serious problem, function failed |
| CRITICAL | 50 | Program may crash |

## Production Logger Setup

```python
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name: str, log_file: str, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Console handler
    console = logging.StreamHandler()
    console.setLevel(logging.WARNING)

    # File handler with rotation (5MB, keep 3 backups)
    file_handler = RotatingFileHandler(
        log_file, maxBytes=5*1024*1024, backupCount=3
    )
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(funcName)s:%(lineno)d | %(message)s"
    )
    console.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file_handler)
    return logger

logger = setup_logger("myapp", "app.log")
```

## Logging Exceptions

```python
try:
    result = 1 / 0
except ZeroDivisionError:
    logger.exception("Division failed")   # logs full traceback
    # OR
    logger.error("Division failed", exc_info=True)
```

## Structured Logging with structlog

```python
import structlog

log = structlog.get_logger()
log.info("user.login", user_id=42, ip="192.168.1.1")
# {"event": "user.login", "user_id": 42, "ip": "192.168.1.1", "timestamp": "..."}
```

## Lab Exercise
1. Configure separate DEBUG file log and WARNING console log for a module
2. Add request ID to all log messages in a FastAPI app using `logging.LoggerAdapter`
3. Set up JSON-formatted logs using `structlog` for production
