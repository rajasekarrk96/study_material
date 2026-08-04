# Lesson 4.1 SQLAlchemy 2.0 Async Engine & `asyncpg`

> **Course**: Fastapi | **Module**: Module 1 | **Difficulty**: beginner

---

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐⭐ Advanced
- **Prerequisites**: [Lesson 3.2 Sub-Dependencies](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_05_fastapi/_05_06_sub_dependencies_security_and_yield_cleanups.md)
- **XP Reward**: +70 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Explain why traditional synchronous database drivers block FastAPI's async event loop.
2. Configure **SQLAlchemy 2.0** with **`create_async_engine()`**.
3. Use asynchronous database drivers (**`asyncpg`** for PostgreSQL, **`aiosqlite`** for SQLite).
4. Create an **`async_sessionmaker`** and inject **`AsyncSession`** instances using FastAPI yield dependencies.

---

---

Install `sqlalchemy`, `asyncpg`, and `aiosqlite`:

```bash
pip install "sqlalchemy>=2.0" asyncpg aiosqlite
```

---

---

### 3.1 Synchronous vs Asynchronous Database Drivers
FastAPI's high performance relies on its non-blocking event loop. If an `async def` endpoint uses a synchronous database driver (like standard `psycopg2` or `sqlite3`), database queries block the event loop thread—completely defeating the purpose of async I/O!

**SQLAlchemy 2.0** introduces native async support. Combined with async drivers like **`asyncpg`** (PostgreSQL) or **`aiosqlite`** (SQLite), database queries execute non-blockingly:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ASYNC DATABASE CONNECTION MATRIX                         │
├─────────────────┬──────────────────────────────────┬────────────────────────┤
│ Database        │ Async Driver Package             │ Async Connection URI   │
├─────────────────┼──────────────────────────────────┼────────────────────────┤
│ SQLite          │ `aiosqlite`                      │ `sqlite+aiosqlite:///` │
│ PostgreSQL      │ `asyncpg`                        │ `postgresql+asyncpg://`│
│ MySQL           │ `asyncmy`                        │ `mysql+asyncmy://`     │
└─────────────────┴──────────────────────────────────┴────────────────────────┘
```

---

---

```mermaid
flowchart TD
    Req[Async HTTP Request] --> Dep["FastAPI Yield Dependency: get_db()"]
    Dep --> Session["async_sessionmaker Creates AsyncSession"]
    Session --> Query["await session.execute(select(Model))"]
    Query --> AsyncDriver[Async Driver: asyncpg / aiosqlite]
    AsyncDriver --> NonBlock[Database I/O non-blocking to Event Loop!]
```

---

---

### File 1: `database.py` (SQLAlchemy 2.0 Async Engine & Dependency)

```python
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

# Async Database URI (sqlite+aiosqlite for local testing; postgresql+asyncpg for prod!)
DATABASE_URL = "sqlite+aiosqlite:///./async_telemetry.db"

# 1. Instantiate SQLAlchemy 2.0 Async Engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True, # Logs SQL queries during development
    future=True
)

# 2. Configure Async Session Maker Factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False # Prevents lazy-loading errors after commit!
)

# 3. Base Declarative Class
class Base(DeclarativeBase):
    pass

# 4. FastAPI Yield Dependency for Injecting AsyncSession
async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
```

### File 2: `main.py` (Using AsyncSession in Route)

```python
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from database import get_async_db

app = FastAPI(title="Async DB API")

@app.get("/api/v1/db-health")
async def check_db_health(db: AsyncSession = Depends(get_async_db)):
    # Execute non-blocking SQL query using await!
    result = await db.execute(text("SELECT 1"))
    value = result.scalar()
    return {"status": "HEALTHY", "result": value}
```

---

---

- **High-Concurrency Telemetry Services**: Production FastAPI microservices connect to PostgreSQL database clusters using `postgresql+asyncpg://`, enabling hundreds of concurrent web requests to execute non-blocking database queries simultaneously.

---

---

1. Save `database.py` and `main.py`.
2. Run `uvicorn main:app --reload`.
3. Navigate to `/api/v1/db-health` $\to$ Inspect terminal logs for non-blocking async SQL execution!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`MissingGreenlet: Missing greenlet context`** | Attempting to access lazy-loaded relational attributes synchronously on an AsyncSession model. | Use explicit `selectinload()` or `joinedload()` eager loading strategies in async queries. |

---

---

- **Set `expire_on_commit=False`**: Prevents SQLAlchemy from expiring model attribute instances after `commit()`, avoiding `MissingGreenlet` errors in async code.

---

---

### Q1: Why is `asyncpg` significantly faster than `psycopg2` when used with FastAPI?
**Answer**: `psycopg2` is a synchronous C-extension driver that blocks Python's thread during database network I/O. `asyncpg` is built specifically for `asyncio` from the ground up, utilizing PostgreSQL's binary protocol directly without intermediate abstractions, enabling fast non-blocking I/O and handling massive concurrent connection loads efficiently.

---

---

```json
{
  "quiz_title": "Lesson 4.1 Async Database Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which SQLAlchemy 2.0 function instantiates an asynchronous database engine?",
      "options": ["create_engine()", "create_async_engine()", "init_async_db()", "AsyncEngine()"],
      "correct_answer_index": 1,
      "explanation": "create_async_engine() creates async SQLAlchemy engines."
    }
  ]
}
```

---

---

Configure an async engine with `aiosqlite` and a yield dependency providing `AsyncSession`.

---

---

**Front**: What parameter on `async_sessionmaker` prevents `MissingGreenlet` errors after committing an async session?
**Back**: `expire_on_commit=False`.
<!-- flashcard:end -->

---

---

```python
engine = create_async_engine("sqlite+aiosqlite:///app.db")
async_session = async_sessionmaker(engine, class_=AsyncSession)
```


---

---

> **Source**: `_14_01_Database_Relationships_and_Normalization_Notes.md` (from backend concepts archive)
> This content was migrated from existing study notes. Review and merge with topics above.

# Module 7: Database Design

---

---

### 1. The Big Picture

#### What is Database Design?
Database design is the organization of data according to a database model. In relational databases (like PostgreSQL), we structure data into tables with columns and establish relationships between them using **Foreign Keys**.

#### Database Normalization
Normalization is the process of structuring a relational database to reduce data redundancy and improve data integrity. 
* **1NF (First Normal Form):** Every cell contains a single (atomic) value, and there are no repeating groups.
* **2NF (Second Normal Form):** Must be in 1NF, and all non-key attributes must be fully dependent on the primary key (no partial dependencies).
* **3NF (Third Normal Form):** Must be in 2NF, and there must be no transitive dependencies (non-key fields shouldn't depend on other non-key fields).

---

### 2. Entity Relationships

```
  ONE-TO-ONE (1:1)          ONE-TO-MANY (1:N)          MANY-TO-MANY (N:M)
 ┌────────┐ ┌────────┐     ┌────────┐ ┌────────┐     ┌───────┐ ┌─────────┐ ┌───────┐
 │  User  │ │ Profile│     │Category│ │ Product│     │ Order │ │OrderItem│ │Product│
 │ (id)   │ │ (id)   │     │ (id)   │ │ (id)   │     │ (id)  │ │ (order) │ │ (id)  │
 └───┬────┘ └───┬────┘     └───┬────┘ └───┬────┘     └───┬───┘ │ (prod)  │ └───┬───┘
     │ 1        │ 1            │ 1        │ N            │ 1   └────┬────┘     │ 1
     └──────────┘              └──────────┘              └──────────┴──────────┘
```

1. **One-to-One (1:1):** A user has exactly one profile. The `Profile` table has a foreign key `user_id` marked as `UNIQUE`.
2. **One-to-Many (1:N):** A category has many products, but a product belongs to only one category. The `Product` table has a foreign key `category_id`.
3. **Many-to-Many (N:M):** An order can contain many products, and a product can belong to many orders. We **must** use an intermediate table (Association/Junction Table) like `OrderItem` to store this relationship.

---

### 3. Implementing Relationships in SQLAlchemy
In Python, we use **SQLAlchemy** (an Object-Relational Mapper) to map database tables to Python classes.

```python
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# Many-to-Many Junction Table (Order <-> Product)
order_product_association = Table(
    "order_item",
    Base.metadata,
    Column("order_id", Integer, ForeignKey("orders.id"), primary_key=True),
    Column("product_id", Integer, ForeignKey("products.id"), primary_key=True),
    Column("quantity", Integer, default=1)
)

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    
    # 1:N relationship (Category has many products)
    products = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    
    category = relationship("Category", back_populates="products")
    
    # N:M relationship (Product belongs to many orders)
    orders = relationship(
        "Order", 
        secondary=order_product_association, 
        back_populates="products"
    )

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    
    products = relationship(
        "Product", 
        secondary=order_product_association, 
        back_populates="orders"
    )
```

---

### 4. Hands-on Workout & Assessment

#### Part A: Database Design Challenge (N:M Relationship)
You are designing a database for a **Student Course Enrollment** system. 
- A student can enroll in multiple courses.
- A course has multiple students enrolled.
- We need to track the date the student enrolled in the course and the grade they received.

Write down:
- The names of the three tables required.
- The columns for each table, highlighting Primary Keys (PK) and Foreign Keys (FK).

#### Part B: Quiz
1. Which normal form requires that there are no transitive dependencies?
   A. 1NF
   B. 2NF
   C. 3NF
   D. BCNF
2. In a One-to-Many relationship (Category -> Products), where does the Foreign Key reside?
   A. In the Category table.
   B. In the Product table.
   C. In a separate junction table.
   D. Both tables have foreign keys pointing to each other.
3. What is the purpose of the `secondary` argument in SQLAlchemy's `relationship()` function?
   A. It defines a backup database connection.
   B. It specifies the junction table used to resolve a Many-to-Many relationship.
   C. It marks a column as a secondary index.
   D. It allows lazy-loading of data.

---

### 5. Progress Tracker

* **Module 7: Database Design:** 0%
* **Topics Completed:** 0/1
* **Coding Exercises:** 0/0
* **Quiz Score:** N/A
* **API Design Challenge Score:** N/A
* **Backend Score:** 0 / 100

---

---
