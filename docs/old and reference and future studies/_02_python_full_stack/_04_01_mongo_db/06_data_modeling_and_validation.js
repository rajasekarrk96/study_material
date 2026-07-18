// ==============================================================================
// 06: MongoDB Data Modeling and Validation
// ==============================================================================

// HOW TO RUN THIS FILE:
// mongosh < 06_data_modeling_and_validation.js

use interview_prep;
// Clean up in case collections exist
db.authors.drop();
db.books.drop();
db.users_validated.drop();

// ------------------------------------------------------------------------------
// DATA MODELING CONCEPTS
// ------------------------------------------------------------------------------
// Two primary ways to model relationships: References vs. Embedded Documents.
// Rule of Thumb: 
// - Favor embedding for "contains" relationships where data is queried together.
// - Favor references when embedding would result in unbound document growth (16MB limit).

print("\n--- 1. Embedded Relationship (One-to-Few) ---");
// A user has a few addresses.
db.authors.insertOne({
    name: "J.K. Rowling",
    addresses: [
        { city: "London", country: "UK" },
        { city: "Edinburgh", country: "UK", type: "Home" }
    ] // Embedded: Fast read, but shouldn't grow infinitely.
});

print("\n--- 2. Referenced Relationship (One-to-Many) ---");
// A publisher has potentially thousands of books.
let authorRef = db.authors.findOne({ name: "J.K. Rowling" });

db.books.insertMany([
    { title: "Harry Potter and the Sorcerer's Stone", author_id: authorRef._id }, // Reference to author document
    { title: "Harry Potter and the Chamber of Secrets", author_id: authorRef._id }
]);


// ------------------------------------------------------------------------------
// SCHEMA VALIDATION (JSON Schema)
// ------------------------------------------------------------------------------
// MongoDB is schemaless by default, but you can enforce validation rules!

print("\n--- Creating Collection with Schema Validation ---");
db.createCollection("users_validated", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["username", "email", "age"], // These fields MUST exist
            properties: {
                username: {
                    bsonType: "string",
                    description: "must be a string and is required"
                },
                email: {
                    bsonType: "string",
                    pattern: "^.+@.+\\..+$",
                    description: "must be a valid email string and is required"
                },
                age: {
                    bsonType: "int",
                    minimum: 18, // Must be 18 or older
                    description: "must be an integer >= 18 and is required"
                }
            }
        }
    },
    validationAction: "error" // "error" rejects write, "warn" logs it but writes.
});

print("\n--- Inserting Valid Document ---");
// This will succeed
db.users_validated.insertOne({
    username: "john_doe",
    email: "john@example.com",
    age: NumberInt(25) // Note: Need to specify integer explicitly in mongosh sometimes
});
print("Insert successful.");

print("\n--- Attempting Invalid Insert (Will Throw Error) ---");
// This will FAIL because age is < 18
try {
    db.users_validated.insertOne({
        username: "jane_doe",
        email: "jane@example.com",
        age: NumberInt(16)
    });
} catch(e) {
    print("Caught Exception as expected: Document failed validation.");
}


// ==============================================================================
// PRACTICE QUESTIONS (LeetCode Style)
// ==============================================================================
/*
Q1 (Easy Concept): Explain when you should use Embedding vs. Referencing in MongoDB.
Solution:
Embed data when items are queried together frequently, items are dependent, and the array won't grow infinitely (One-to-Few, 1:1). 
Reference data when items are queried independently, array could grow large causing >16MB documents (One-to-Many/Millions, N:M).

Q2 (Easy): In the "Referenced Relationship" example above, how do you perform a "join"? Which pipeline operator is used?
Solution:
Using the Aggregation Framework, specifically the `$lookup` operator.

Q3 (Medium): Write a `$lookup` aggregation on the `books` collection to pull in the author data from `authors`.
Solution:
db.books.aggregate([
    {
        $lookup: {
            from: "authors",          // the collection to join
            localField: "author_id",  // the reference field in 'books'
            foreignField: "_id",      // the matching field in 'authors'
            as: "author_details"      // output array name
        }
    }
]);

Q4 (Medium): Add a new required field "status" to a schema validation rule that only accepts the string values "active" or "inactive". (Write the property object).
Solution:
status: {
    bsonType: "string",
    enum: ["active", "inactive"],
    description: "must be either active or inactive"
}

Q5 (Hard - Conceptual Array Limits): An IoT platform stores sensor data in a MongoDB document. The document looks like: { sensorId: "S1", readings: [...] }. They append a new reading to the array every second. Why is this a very bad data modeling practice in MongoDB, and what pattern should be used instead?
Solution:
This is bad because of the Unbounded Array Anti-Pattern. MongoDB documents have a hard 16MB limit. Appending every second will eventually hit this limit. Also, constantly reallocating the document on disk as the array grows causes performance fragmentation.
Better Pattern: The "Bucket Pattern". Group readings by chunks of time (e.g., one document per day, per sensor).
{ sensorId: "S1", day: "2023-10-01", readingsCount: 86400, readings: [ ... ] }
*/
