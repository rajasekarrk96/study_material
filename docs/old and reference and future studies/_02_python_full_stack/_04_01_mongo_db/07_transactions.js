// ==============================================================================
// 07: MongoDB ACID Transactions
// ==============================================================================

// HOW TO RUN THIS FILE:
// mongosh < 07_transactions.js

use interview_prep;
db.accounts.drop();
db.accounts.insertMany([
    { account_id: "A", balance: 1000 },
    { account_id: "B", balance: 500 }
]);

// ------------------------------------------------------------------------------
// MULTI-DOCUMENT TRANSACTIONS CONCEPTS
// ------------------------------------------------------------------------------
// MongoDB supports ACID transactions across multiple documents and collections.
// Requires: 
// 1. A Replica Set (Does generally NOT work on standalone instances)
// 2. A Session to bind operations together.

// NOTE ABOUT LOCAL TESTING:
// If you installed MongoDB as a standard standalone service, the following code
// might throw an error: "Transaction numbers are only allowed on a replica set"
// In an interview, it is the *concepts* and *syntax* that matter. 
// Standard production MongoDB environments are always Replica Sets.

print("\n--- Starting a Session and Transaction ---");

try {
    // 1. Start a Client Session
    const session = db.getMongo().startSession();
    
    // 2. Start the Transaction
    session.startTransaction();
    
    // Get collecton references tied to the session
    const accountsCol = session.getDatabase("interview_prep").accounts;

    print("Attempting to transfer 200 from A to B...");
    
    // Deduct from A
    accountsCol.updateOne({ account_id: "A" }, { $inc: { balance: -200 } });
    
    // Add to B
    accountsCol.updateOne({ account_id: "B" }, { $inc: { balance: 200 } });

    // 3. Commit the Transaction
    session.commitTransaction();
    print("Transaction Committed successfully.");

    // End session
    session.endSession();
} catch (error) {
    print("Transaction failed or not supported on this topology:", error.message);
    // session.abortTransaction();
}

print("\n--- Final Balances ---");
printjson(db.accounts.find().toArray());


// ==============================================================================
// PRACTICE QUESTIONS (LeetCode Style)
// ==============================================================================
/*
Q1 (Easy Concept): What does ACID stand for in database transactions?
Solution:
Atomicity, Consistency, Isolation, Durability.

Q2 (Easy): In MongoDB, what topology is strictly required to run multi-document transactions?
Solution:
Replica Sets (or Sharded Clusters depending on version, though 4.2+ supports distributed transactions). It cannot be run on a standalone instance.

Q3 (Medium): Why are multi-document transactions generally avoided in NoSQL databases if possible? How does good data modeling mitigate the need for them?
Solution:
Multi-document transactions impact performance due to locks and coordination overhead. 
In MongoDB, a single-document update is always atomic. By modeling data with embedding (denormalization), you can often update related data in a single document atomically without needing a multi-document transaction.

Q4 (Medium): Write the command to abort/rollback a transaction if an error occurs.
Solution:
session.abortTransaction();

Q5 (Hard - Code Scenario): You are transferring funds. You deducted $50 from Account A, but the database crashed right before you added $50 to Account B inside a transaction context. What happens when the database recovers?
Solution:
Atomicity ensures "all or nothing". Because `session.commitTransaction()` was not invoked and successfully written to the journal (oplog), the transaction will be rolled back upon recovery. Account A's balance will revert to its original state, and the $50 is not lost in limbo.
*/
