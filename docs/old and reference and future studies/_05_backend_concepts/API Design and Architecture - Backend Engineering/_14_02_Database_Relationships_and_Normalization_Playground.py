# %% [markdown]
# # Topic 14: Database Relationships & SQLAlchemy Playground
# In this playground, you will learn how to define and query relationships in SQLAlchemy.
# We will use an in-memory SQLite database (`sqlite:///:memory:`).
# We will cover:
# 1. Defining a One-to-Many relationship (Category -> Products).
# 2. Creating tables and inserting records.
# 3. Querying relationships.
# 4. Preventing the **N+1 Query Problem** using eager loading (`joinedload`).
#
# **How to use this:**
# 1. Open this file in VS Code.
# 2. Click **"Run Cell"** above each code block.

# %%
# 1. INSTALL DEPENDENCIES
# We install sqlalchemy.
%pip install sqlalchemy

# %%
# 2. IMPORT LIBRARIES
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, joinedload
import json

# %%
# 3. DATABASE SETUP
# Create an in-memory SQLite database
engine = create_engine("sqlite:///:memory:", echo=True) # echo=True prints raw SQL queries in stdout!
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

Base = declarative_base()

# %%
# 4. DEFINE MODELS

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    
    # 1:N relationship. back_populates links it to the 'category' attribute in Product.
    products = relationship("Product", back_populates="category", cascade="all, delete-orphan")

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False) # Store price in cents (best practice to avoid floating point issues!)
    category_id = Column(Integer, ForeignKey("categories.id"))
    
    category = relationship("Category", back_populates="products")

# Create all tables in our database
Base.metadata.create_all(engine)

# %% [markdown]
# ## Inserting Data
# Let's create a category and add products to it.

# %%
# 5. INSERT RECORDS
electronics = Category(name="Electronics")

# We can append products directly to the relationship list
phone = Product(name="iPhone 14", price=99900, category=electronics)
laptop = Product(name="MacBook Pro", price=199900, category=electronics)

session.add(electronics)
session.commit()

print("\n--- Data successfully committed ---")

# %% [markdown]
# ## Querying Relationships
# Notice that when we access `electronics.products`, SQLAlchemy automatically queries the
# products table behind the scenes. This is called **Lazy Loading**.

# %%
# 6. LAZY LOADING DEMO
session.expire_all() # Clear session cache to force DB queries

# Let's fetch the category
cat = session.query(Category).filter_by(name="Electronics").first()
print(f"\nFetched Category: {cat.name}")

# Now we access the products. Watch the console logs!
# You will see a second SELECT query fired automatically to fetch the products.
print("\n--- Accessing products (Lazy Load) ---")
for prod in cat.products:
    print(f"Product: {prod.name} | Price: ${prod.price / 100}")

# %% [markdown]
# ## Eager Loading: Fixing the N+1 Query Problem
# If you query 100 categories and loop through each to print their products,
# lazy loading will fire 1 query to get categories, and then 100 separate queries to get products.
# This is the **N+1 Query Problem** and it slows down APIs drastically.
# We fix this by using **`joinedload`** to fetch categories and products in a single SQL JOIN query.

# %%
# 7. EAGER LOADING DEMO
session.expire_all()

print("\n--- Querying with Eager Loading (joinedload) ---")
# This fires a single SELECT query with a LEFT OUTER JOIN
categories_with_products = session.query(Category).options(joinedload(Category.products)).all()

for c in categories_with_products:
    print(f"\nCategory: {c.name}")
    for p in c.products:
        print(f"  -> Product: {p.name}")
