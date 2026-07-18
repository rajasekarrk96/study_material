# ==============================================================================
# 09: MongoDB Python Integration (PyMongo)
# ==============================================================================

# Prerequisites:
# 1. Have Python installed.
# 2. Run: pip install pymongo

import pymongo
from pymongo import MongoClient

def run_mongodb_operations():
    # ------------------------------------------------------------------------------
    # 1. CONNECTION
    # ------------------------------------------------------------------------------
    # Connect to local MongoDB instance
    # If remote, it looks like: "mongodb+srv://user:pass@cluster0.abcde.mongodb.net/"
    print("Connecting to MongoDB...")
    try:
        client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
        # Attempt to ping the server to ensure connection is valid
        client.admin.command('ping')
        print("Connected successfully!")
    except Exception as e:
        print(f"Connection failed. Make sure MongoDB is running. Error: {e}")
        return

    # Select Database
    db = client["interview_prep_python"]
    
    # Select Collection
    users_col = db["users"]
    
    # Clean slate
    users_col.drop()

    # ------------------------------------------------------------------------------
    # 2. CREATE (Insert)
    # ------------------------------------------------------------------------------
    # In PyMongo, use insert_one() and insert_many()
    
    # Insert One
    person = {"name": "Alice", "age": 28, "city": "New York"}
    result_one = users_col.insert_one(person)
    print(f"\nInserted one document with _id: {result_one.inserted_id}")

    # Insert Many
    people = [
        {"name": "Bob", "age": 35, "city": "Chicago"},
        {"name": "Charlie", "age": 22, "city": "Boston"},
        {"name": "Diana", "age": 40, "city": "New York"}
    ]
    result_many = users_col.insert_many(people)
    print(f"Inserted multiple documents. Inserted IDs list length: {len(result_many.inserted_ids)}")

    # ------------------------------------------------------------------------------
    # 3. READ (Find)
    # ------------------------------------------------------------------------------
    # find_one() returns a dictionary. find() returns a Cursor (iterator).
    
    print("\n--- Find One ---")
    alice_doc = users_col.find_one({"name": "Alice"})
    print(alice_doc)

    print("\n--- Find Many (New York residents) ---")
    ny_cursor = users_col.find({"city": "New York"})
    for doc in ny_cursor:
        print(doc)

    # ------------------------------------------------------------------------------
    # 4. UPDATE
    # ------------------------------------------------------------------------------
    # update_one() and update_many()
    
    print("\n--- Update Bob's age ---")
    # Always remember the $set parameter! If you omit $set, Python won't let you just pass a raw dict since PyMongo 4+ enforces update modifier syntax.
    update_result = users_col.update_one({"name": "Bob"}, {"$set": {"age": 36}})
    print(f"Matched count: {update_result.matched_count}, Modified count: {update_result.modified_count}")

    # ------------------------------------------------------------------------------
    # 5. DELETE
    # ------------------------------------------------------------------------------
    # delete_one() and delete_many()
    
    print("\n--- Delete Charlie ---")
    del_result = users_col.delete_one({"name": "Charlie"})
    print(f"Deleted count: {del_result.deleted_count}")

    # Close connection
    client.close()


if __name__ == "__main__":
    run_mongodb_operations()



# ==============================================================================
# PRACTICE QUESTIONS (LeetCode Style for PyMongo)
# ==============================================================================
'''
Q1 (Easy): Write the PyMongo code to connect to "mongodb://localhost:27017/", access the "company" database, and the "employees" collection.
Solution:
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["company"]
collection = db["employees"]

Q2 (Easy): Using the collection object from Q1, write the PyMongo code to find all employees where the "department" is "Engineering", and print their names.
Solution:
cursor = collection.find({"department": "Engineering"})
for emp in cursor:
    print(emp["name"])

Q3 (Medium): Update all documents where "status" is "pending" to "approved". Print the number of documents modified.
Solution:
result = collection.update_many(
    {"status": "pending"},
    {"$set": {"status": "approved"}}
)
print(result.modified_count)

Q4 (Medium): You want to fetch the TOP 5 highest paid employees. Write the query. 
Hint: PyMongo cursors have .sort() and .limit() methods!
Solution:
# Note: In PyMongo, sorting requires a tuple of (field, direction) or list of tuples
cursor = collection.find().sort("salary", pymongo.DESCENDING).limit(5)
for emp in cursor:
    print(emp)

Q5 (Hard - Error Handling): When inserting a document that violates a Unique Index constraint, PyMongo throws a specific exception. How would you wrap an insert statement to catch a duplicate key error specifically?
Solution:
from pymongo.errors import DuplicateKeyError

try:
    collection.insert_one({"_id": 1, "name": "Test"}) # Assuming _id 1 exists
except DuplicateKeyError:
    print("A document with that ID already exists!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
'''
