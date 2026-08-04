---
id: "21_04_04"
title: "PyMongo Integration"
course: "MongoDB"
module: 4
module_title: "Data Modeling and Administration"
lesson: 4
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["pymongo", "python", "MongoClient", "cursor", "bson", "gridfs"]
prerequisites: []
lab_required: true
---

# PyMongo Integration


## Interfacing MongoDB with Python (PyMongo)

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

## Lab Exercise
1. Build a Python script that connects to MongoDB, parses a JSON data file, and uploads documents in batches using `insert_many()`.
