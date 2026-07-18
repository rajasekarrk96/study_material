# Module 7: Database Design
## Topic 15: Database Indexes & ACID Transactions

---

### 1. Database Indexes

#### What is an Index?
A database **Index** is a data structure (typically a B-Tree) that improves the speed of data retrieval operations on a database table at the cost of additional write time and storage space.

* **The Book Metaphor:** Without an index, finding a word in a 1,000-page book requires scanning every page from page 1 to 1,000 (**Full Table Scan** - $O(N)$). With an index at the back of the book, you look up the word alphabetically, find the page number, and jump directly to it (**Index Scan** - $O(\log N)$).

#### Tradeoffs of Indexing
* **Pros:** Speeds up `SELECT` queries with `WHERE`, `JOIN`, `ORDER BY`, or `GROUP BY` clauses.
* **Cons:** 
  * **Slower Writes:** Every time you perform an `INSERT`, `UPDATE`, or `DELETE`, the database must update the index structure.
  * **Disk Space:** Indexes consume significant disk space. Large tables can have indexes that are gigabytes in size.

#### What Columns to Index
1. **Primary Keys:** Indexed automatically.
2. **Foreign Keys:** Always index foreign keys to speed up table joins.
3. **High-Cardiality Search Columns:** Columns frequently used in filters (e.g., `email`, `username`, `created_at`). Do *not* index low-cardinality columns (like `gender` or `status` with only 2-3 distinct values), as the database will still prefer a full table scan.

---

### 2. ACID Transactions
A **Transaction** is a unit of work performed against a database. To ensure data integrity, relational databases guarantee **ACID** properties:

1. **Atomicity:** "All-or-Nothing." If a transaction has 5 steps (e.g., deduct balance, record payment, create order), and step 4 fails, the entire transaction is rolled back. No partial changes are saved.
2. **Consistency:** A transaction must transition the database from one valid state to another, maintaining all constraints (e.g., foreign keys, unique fields).
3. **Isolation:** Multiple transactions executing concurrently must not interfere with each other. The database simulates running them sequentially.
4. **Durability:** Once a transaction is committed, its changes are permanently written to non-volatile storage (disk) and will survive a system crash.

---

### 3. Implementing Transactions in SQLAlchemy

To implement Atomicity, we use `try-except` blocks. If any database operation fails, we trigger a `session.rollback()`.

```python
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer

def transfer_funds(db: Session, sender_id: int, receiver_id: int, amount: int):
    try:
        # 1. Deduct from sender
        sender = db.query(Account).filter_by(id=sender_id).with_for_update().first() # Lock row
        sender.balance -= amount
        
        # 2. Add to receiver
        receiver = db.query(Account).filter_by(id=receiver_id).with_for_update().first()
        receiver.balance += amount
        
        # If both succeed, commit the transaction
        db.commit()
    except Exception as e:
        # If any step fails (e.g., connection drop, constraint violation), roll back everything!
        db.rollback()
        raise e
```

---

### 4. Hands-on Workout & Assessment

#### Part A: API Design Challenge (ACID Transactions)
You are building an **E-Commerce Checkout** API. When a user buys a product:
1. The **Order** is created.
2. The **Product Stock** is decremented.
3. The **User Loyalty Points** are incremented.

- Explain what would happen to database integrity if step 1 and 2 succeed, but step 3 fails due to a database constraint, and you are **not** using a transaction.
- Explain how a transaction solves this.

#### Part B: Quiz
1. Which ACID property ensures that all operations in a transaction either succeed completely or fail completely?
   A. Atomicity
   B. Consistency
   C. Isolation
   D. Durability
2. Why should you avoid indexing every single column in a database table?
   A. The database allows only 3 indexes per table.
   B. It will slow down `INSERT`, `UPDATE`, and `DELETE` operations because the database must rebuild the indexes on every write.
   C. It causes database memory leaks.
   D. Indexes can only be created on integer columns.
3. What does `session.rollback()` do in SQLAlchemy?
   A. It restarts the database server.
   B. It deletes the database file.
   C. It undoes all uncommitted database modifications made during the current transaction.
   D. It commits the changes.

---

### 5. Progress Tracker

* **Module 7: Database Design:** 0%
* **Topics Completed:** 0/2
* **Coding Exercises:** 0/0
* **Quiz Score:** N/A
* **API Design Challenge Score:** N/A
* **Backend Score:** 0 / 100

---
