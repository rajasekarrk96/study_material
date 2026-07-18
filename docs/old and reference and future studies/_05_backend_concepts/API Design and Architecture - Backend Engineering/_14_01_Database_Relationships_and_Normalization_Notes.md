# Module 7: Database Design
## Topic 14: Database Relationships & Normalization

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
