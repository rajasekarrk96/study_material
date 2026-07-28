---
id: "02_09_01"
title: "File I/O and Paths"
course: "Python"
module: 9
module_title: "File I/O and Serialisation"
lesson: 1
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["open", "read", "write", "readline", "pathlib", "Path", "glob", "shutil", "os.path", "context-manager", "text-vs-binary"]
prerequisites: []
lab_required: true
---

# File I/O and Paths


## File Operations

```python
# Reading
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()          # entire file as string
    lines   = f.readlines()     # list of lines (with \n)
    line    = f.readline()      # one line

# Writing
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")

# Appending
with open("log.txt", "a") as f:
    f.write(f"Entry: {entry}\n")

# Binary mode
with open("image.png", "rb") as f:
    data = f.read()

with open("copy.png", "wb") as f:
    f.write(data)
```

## File Modes

| Mode | Description |
|---|---|
| `r` | Read (default) |
| `w` | Write (create/truncate) |
| `a` | Append |
| `x` | Exclusive create (fails if exists) |
| `b` | Binary (append to mode: `rb`, `wb`) |
| `+` | Read+Write (`r+`, `w+`) |

## pathlib — Modern Path Handling

```python
from pathlib import Path

# Build paths (cross-platform)
base = Path("/var/www/myapp")
config = base / "config" / "settings.json"

config.exists()        # True/False
config.is_file()       # True
config.is_dir()        # False
config.suffix          # ".json"
config.stem            # "settings"
config.name            # "settings.json"
config.parent          # Path('/var/www/myapp/config')

# Read/Write directly
config.read_text(encoding="utf-8")
config.write_text('{"debug": false}')
config.read_bytes()
config.write_bytes(data)

# Glob patterns
list(base.glob("**/*.py"))       # all Python files recursively
list(base.glob("*.json"))        # JSON files in base only

# Create directories
(base / "new_dir").mkdir(parents=True, exist_ok=True)

# Rename / move
old = Path("old.txt")
old.rename("new.txt")           # rename in-place

# Delete
config.unlink()                 # delete file
(base / "empty_dir").rmdir()   # delete empty dir
import shutil
shutil.rmtree(base / "full_dir")  # delete dir with contents
```

## CSV and JSON Files

```python
import csv, json

# CSV read
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])

# CSV write
with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows([{"name": "Raja", "age": 28}])

# JSON
data = {"users": [{"id": 1, "name": "Raja"}]}
text = json.dumps(data, indent=2, ensure_ascii=False)
parsed = json.loads(text)

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

with open("data.json") as f:
    data = json.load(f)
```

## Lab Exercise
1. Build a log parser that reads a log file and counts errors per hour
2. Recursively find all `.py` files in a directory using `pathlib.glob`
3. Write a config manager that reads/writes JSON and handles missing keys gracefully
