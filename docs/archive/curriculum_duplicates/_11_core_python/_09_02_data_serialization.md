# Data Serialization

> **Course**: Core Python | **Module**: File I/O and Serialisation | **Difficulty**: intermediate

---

```python
import json

# Serialise Python → JSON string
data = {"name": "Raja", "scores": [90, 85, 92], "active": True}
text = json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False)

# Custom encoder for non-serialisable types
from datetime import datetime
from dataclasses import dataclass, asdict

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

json.dumps({"ts": datetime.now()}, cls=DateTimeEncoder)
```

---

```python
import pickle

# Serialize any Python object
data = {"model": trained_sklearn_model, "params": {...}}

with open("model.pkl", "wb") as f:
    pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

with open("model.pkl", "rb") as f:
    loaded = pickle.load(f)

# ⚠️ NEVER unpickle untrusted data — arbitrary code execution risk!
```

---

```python
import yaml

config = yaml.safe_load('''
database:
  host: localhost
  port: 5432
  name: mydb
debug: false
''')

config["database"]["host"]   # "localhost"

with open("config.yaml") as f:
    config = yaml.safe_load(f)

yaml.dump(config, default_flow_style=False)
```

---

```python
import tomllib   # read only in 3.11+
# pip install tomli for older Python

with open("pyproject.toml", "rb") as f:
    config = tomllib.load(f)

# Write: use tomli-w
import tomli_w
with open("config.toml", "wb") as f:
    tomli_w.dump({"key": "value"}, f)
```

---

```python
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    created_at: datetime = datetime.now()

# From dict / JSON
user = User(id=1, name="Raja")
user = User.model_validate({"id": 1, "name": "Raja"})
user = User.model_validate_json('{"id": 1, "name": "Raja"}')

# To dict / JSON
user.model_dump()              # dict
user.model_dump_json()         # JSON string
user.model_dump(exclude={"created_at"})
```

---

```python
import orjson

# 5-10x faster than stdlib json
data = {"name": "Raja", "scores": [1,2,3]}
encoded = orjson.dumps(data)          # bytes
decoded = orjson.loads(encoded)       # dict

# Handles datetime, UUID, numpy arrays natively
orjson.dumps(datetime.now())          # works!
```

---

1. Serialize a list of dataclass objects to JSON and back
2. Build a config system supporting YAML, TOML, and JSON with unified API
3. Benchmark `json` vs `orjson` vs `ujson` for 10,000 serializations

---
