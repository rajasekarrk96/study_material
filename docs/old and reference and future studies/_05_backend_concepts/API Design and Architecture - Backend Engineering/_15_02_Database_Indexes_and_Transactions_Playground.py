# %% [markdown]
# # Topic 15: Database Indexes & ACID Transactions Playground
# In this playground, you will learn how to implement transactions in SQLAlchemy.
# We will simulate a bank transfer between two accounts:
# 1. Deduct $100 from Alice.
# 2. Add $100 to Bob.
#
# We will deliberately trigger a failure (violating a database check constraint)
# and observe how `session.rollback()` ensures **Atomicity** (no partial transfer occurs).
#
# **How to use this:**
# 1. Open this file in VS Code.
# 2. Click **"Run Cell"** above each code block.

# %%
# 1. IMPORT LIBRARIES
from sqlalchemy import create_engine, Column, Integer, String, CheckConstraint
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError

# %%
# 2. DATABASE SETUP
engine = create_engine("sqlite:///:memory:", echo=True)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

Base = declarative_base()

# %%
# 3. DEFINE MODELS
class BankAccount(Base):
    __tablename__ = "bank_accounts"
    
    id = Column(Integer, primary_key=True)
    owner = Column(String(50), nullable=False)
    # Balance in cents. We add a CheckConstraint to ensure the balance never drops below 0.
    balance = Column(Integer, CheckConstraint("balance >= 0"), nullable=False)

# Create tables
Base.metadata.create_all(engine)

# %%
# 4. SEED ACCOUNTS
alice = BankAccount(owner="Alice", balance=15000) # $150.00
bob = BankAccount(owner="Bob", balance=5000)      # $50.00

session.add_all([alice, bob])
session.commit()
print("\n--- Seed Accounts Committed ---")

# %% [markdown]
# ## Scenario 1: Successful Money Transfer
# We transfer $50 (5000 cents) from Alice to Bob. Both steps succeed, and we commit.

# %%
# 5. SUCCESSFUL TRANSFER

def transfer_money(sender_id: int, receiver_id: int, amount: int):
    print(f"\n[Transaction] Initiating transfer of ${amount/100}...")
    try:
        # Fetch accounts
        sender = session.query(BankAccount).filter_by(id=sender_id).first()
        receiver = session.query(BankAccount).filter_by(id=receiver_id).first()
        
        # Step 1: Deduct from sender
        sender.balance -= amount
        
        # Step 2: Add to receiver
        receiver.balance += amount
        
        # Commit transaction
        session.commit()
        print("[Transaction] Transfer completed successfully!")
    except Exception as e:
        print(f"[Transaction] Error occurred: {e}. Rolling back...")
        session.rollback()

transfer_money(sender_id=1, receiver_id=2, amount=5000)

# Verify balances
a = session.query(BankAccount).filter_by(owner="Alice").first()
b = session.query(BankAccount).filter_by(owner="Bob").first()
print(f"Alice Balance: ${a.balance/100}") # Should be $100
print(f"Bob Balance: ${b.balance/100}")     # Should be $100

# %% [markdown]
# ## Scenario 2: Failed Money Transfer (Triggering Rollback)
# Now, we try to transfer $150 from Alice. Since Alice only has $100 left,
# the deduct step will violate the `CheckConstraint("balance >= 0")` when we commit.
# The transaction must fail and roll back completely, ensuring Alice does not lose money
# and Bob does not receive unbacked funds.

# %%
# 6. FAILED TRANSFER WITH ROLLBACK

try:
    # 1. Fetch accounts
    sender = session.query(BankAccount).filter_by(id=1).first()
    receiver = session.query(BankAccount).filter_by(id=2).first()
    
    # 2. Deduct $150 (Alice only has $100)
    sender.balance -= 15000
    
    # 3. Add to Bob
    receiver.balance += 15000
    
    # 4. Attempt to commit. SQLite will raise an IntegrityError here because of the constraint.
    session.commit()
except IntegrityError as e:
    print(f"\n[Transaction] Integrity constraint violated: {e}")
    print("[Transaction] Rolling back changes to ensure Atomicity...")
    session.rollback()

# %% [markdown]
# ### Verifying Atomicity
# We verify that Alice's balance was NOT changed (it remains $100),
# and Bob's balance was NOT changed (it remains $100).
# Without a transaction and rollback, Bob's balance would have increased to $250
# while Alice's write would have failed, causing $150 to appear out of nowhere!

# %%
a = session.query(BankAccount).filter_by(owner="Alice").first()
b = session.query(BankAccount).filter_by(owner="Bob").first()
print(f"\nAlice Balance: ${a.balance/100} (Should still be $100.00)")
print(f"Bob Balance: ${b.balance/100} (Should still be $100.00)")
print(f"Total system money: ${ (a.balance + b.balance) / 100 } (Should be $200.00)")
