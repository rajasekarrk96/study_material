// ==============================================================================
// 04: MongoDB Indexing & Performance Optimization
// ==============================================================================

// HOW TO RUN THIS FILE:
// mongosh < 04_indexing.js

use interview_prep;
db.users.drop();

// Seed generic data
for(let i = 1; i <= 500; i++) {
    db.users.insertOne({
        user_id: i,
        username: "user" + i,
        age: 18 + (i % 50), // Randomish age 18-67
        status: (i % 2 === 0) ? "active" : "inactive",
        skills: ["js", "mongodb", i % 3 === 0 ? "python" : "java"]
    });
}

// ------------------------------------------------------------------------------
// INDEXING CONCEPTS (Crucial for Interviews)
// ------------------------------------------------------------------------------
// Indexes support the efficient execution of queries. 
// Without indexes, MongoDB must perform a "Collection Scan" (COLLSCAN), scanning every document.
// With indexes, it does an "Index Scan" (IXSCAN).

// 1. VIEW CURRENT INDEXES
print("\n--- Current Indexes (Only _id by default) ---");
printjson(db.users.getIndexes());

// ------------------------------------------------------------------------------
// 2. SINGLE FIELD INDEX
// ------------------------------------------------------------------------------
// 1 = Ascending, -1 = Descending

print("\n--- Creating Single Field Index on 'username' ---");
db.users.createIndex({ username: 1 });

// EXPLAIN PLAN (How to prove it works)
// The "explain" method shows the query execution plan
print("\n--- Execution Plan (Should be IXSCAN) ---");
let explainSingle = db.users.find({ username: "user50" }).explain("executionStats");
print("Winning Plan Stage:", explainSingle.queryPlanner.winningPlan.stage);
print("Docs Examined:", explainSingle.executionStats.totalDocsExamined); // Should be exactly 1, not 500

// ------------------------------------------------------------------------------
// 3. COMPOUND INDEX
// ------------------------------------------------------------------------------
// Indexing on multiple fields.
// IMPORTANT RULE: ESR Rule (Equality, Sort, Range)
// 1. Fields for Equality matches
// 2. Fields for Sorting
// 3. Fields for Range filtering ($gt, $lt)

print("\n--- Creating Compound Index for (status, age) ---");
db.users.createIndex({ status: 1, age: -1 });

// This query is fully supported by the compound index
let compoundPlan = db.users.find({ status: "active", age: { $gt: 30 } }).sort({ age: -1 }).explain();
print("Compound query stage:", compoundPlan.queryPlanner.winningPlan.stage);

// ------------------------------------------------------------------------------
// 4. MULTIKEY INDEX & TEXT INDEX
// ------------------------------------------------------------------------------
// Multikey Index: Created automatically when indexing an array field (e.g., 'skills')
db.users.createIndex({ skills: 1 });

// Text Index: Used for text search (words, phrases)
db.users.createIndex({ username: "text" }); 

// Using the text index
print("\n--- Using Text Index ---");
printjson(db.users.find({ $text: { $search: "user100" } }).toArray());

// ------------------------------------------------------------------------------
// 5. DROPPING INDEXES
// ------------------------------------------------------------------------------
// db.users.dropIndex("username_1"); // Drop by name
// db.users.dropIndexes(); // Drops all except _id


// ==============================================================================
// PRACTICE QUESTIONS (LeetCode Style)
// ==============================================================================
/*
Q1 (Easy): Create a single-field index on the "age" field in descending order.
Solution:
db.users.createIndex({ age: -1 });

Q2 (Easy): View all indexes that currently exist on the "users" collection.
Solution:
db.users.getIndexes();

Q3 (Medium): You frequently query for active users and sort them by their user_id. Create a compound index that optimally supports this query using the ESR rule.
Solution:
// Equality on 'status', Sort on 'user_id'
db.users.createIndex({ status: 1, user_id: 1 });

Q4 (Medium): Drop the single-field index you created on the "username" field.
Solution:
db.users.dropIndex("username_1");

Q5 (Hard - Conceptual): You have a compound index on { A: 1, B: 1, C: 1 }. 
Will this index be used efficiently if the user queries: db.collection.find({ B: "foo", C: "bar" })?
Explain why or why not.
Solution:
No, it will NOT be used efficiently. This relies on the "Index Prefix" rule. 
MongoDB can only use the index prefix to support a query. Since 'A' is the first field in the index, queries must include 'A' to leverage the index structure properly. 
Querying just { B, C } will result in a Collection Scan or a very inefficient full Index Scan depending on the MongoDB version.
*/
