# PyMongo Integration

> **Course**: Mongodb | **Module**: Data Modeling and Administration | **Difficulty**: intermediate

---

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["school_db"]
students = db["students"]

# Insert
students.insert_one({"name": "Raja", "grade": "A"})

# Find
for student in students.find({"grade": "A"}):
    print(student["name"])
```

---

1. Build a Python script that connects to MongoDB, parses a JSON data file, and uploads documents in batches using `insert_many()`.

---
