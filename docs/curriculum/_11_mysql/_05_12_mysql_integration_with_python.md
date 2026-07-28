---
id: "05_12"
title: "MySQL Integration with Python"
course: "MySQL"
module: 5
module_title: "Administration"
lesson: 12
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["mysql-connector-python", "PyMySQL", "SQLAlchemy", "connection-pool", "cursor", "execute", "fetchone", "fetchall", "parameterized-query", "ORM", "transaction"]
prerequisites: []
lab_required: true
---

## Topics Covered

### 1. mysql-connector-python
```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost", port=3306,
    user="app_user", password="pass",
    database="mydb"
)
cursor = conn.cursor(dictionary=True)

# Parameterized query (prevents SQL injection)
cursor.execute("SELECT * FROM products WHERE category_id = %s AND price > %s", (2, 10.0))
rows = cursor.fetchall()

# Insert
cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", ("Widget", 9.99))
conn.commit()
product_id = cursor.lastrowid

cursor.close()
conn.close()
```

### 2. Connection Pooling
```python
from mysql.connector import pooling

pool = pooling.MySQLConnectionPool(
    pool_name="mypool", pool_size=5,
    host="localhost", user="user", password="pass", database="mydb"
)

conn = pool.get_connection()
cursor = conn.cursor()
...
conn.close()  # Returns to pool
```

### 3. SQLAlchemy ORM (MySQL)
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

engine = create_engine("mysql+pymysql://user:pass@localhost/mydb", pool_size=10)

class Base(DeclarativeBase): pass

class Product(Base):
    __tablename__ = "products"
    id    = mapped_column(Integer, primary_key=True)
    name  = mapped_column(String(200))
    price = mapped_column(Numeric(10, 2))

with Session(engine) as session:
    product = session.get(Product, 1)
    products = session.scalars(select(Product).where(Product.price > 10)).all()
    session.add(Product(name="New", price=9.99))
    session.commit()
```

### 4. Async MySQL (aiomysql)
```python
import aiomysql, asyncio

async def main():
    pool = await aiomysql.create_pool(host='localhost', user='u', password='p', db='mydb')
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM products LIMIT 10")
            rows = await cur.fetchall()
    pool.close()
    await pool.wait_closed()
```

## Lab
Build a Python product catalog CLI using: raw mysql-connector for CRUD, connection pooling, and SQLAlchemy ORM for complex queries. Include transaction handling for bulk inserts.
