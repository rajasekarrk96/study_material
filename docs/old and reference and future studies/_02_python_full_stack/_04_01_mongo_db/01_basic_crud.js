// ==============================================================================
// 01: MongoDB Basic CRUD Operations (Create, Read, Update, Delete)
// ==============================================================================

// HOW TO RUN THIS FILE:
// Open your terminal and run:
// mongosh < 01_basic_crud.js
// OR
// Open mongosh, copy and paste the code below in chunks to see the output.

// ------------------------------------------------------------------------------
// DATABASE & COLLECTION CREATION
// ------------------------------------------------------------------------------
// In MongoDB, databases and collections are created lazily. 
// They are actually created when the first document is inserted.

// Switch to a new database called 'interview_prep'
use interview_prep;

// Drop the collection if it exists to start fresh
db.employees.drop();

// Note: A collection is like a Table in SQL. A document is like a Row.

// ------------------------------------------------------------------------------
// 1. CREATE (Insert)
// ------------------------------------------------------------------------------
// db.collection.insertOne()  - inserts a single document
// db.collection.insertMany() - inserts multiple documents

print("\n--- Inserting Documents ---");

db.employees.insertOne({
    emp_id: 101,
    name: "Alice Johnson",
    department: "Engineering",
    role: "Software Engineer",
    salary: 85000,
    skills: ["Java", "Spring Boot", "MongoDB"],
    join_date: new Date("2021-03-15")
});

let bulkData = [
    { emp_id: 102, name: "Bob Smith", department: "HR", role: "Manager", salary: 75000, skills: ["Communication", "Excel"], join_date: new Date("2019-06-20") },
    { emp_id: 103, name: "Charlie Davis", department: "Engineering", role: "Senior Developer", salary: 115000, skills: ["Python", "AWS", "MongoDB"], join_date: new Date("2018-11-01") },
    { emp_id: 104, name: "Diana Prince", department: "Marketing", role: "Director", salary: 130000, skills: ["Strategy", "SEO"], join_date: new Date("2017-02-14") },
    { emp_id: 105, name: "Evan Wright", department: "Engineering", role: "Junior Developer", salary: 65000, skills: ["Java", "Spring Boot"], join_date: new Date("2023-01-10") }
];

db.employees.insertMany(bulkData);
print("Inserted 5 employees.");

// ------------------------------------------------------------------------------
// 2. READ (Find)
// ------------------------------------------------------------------------------
// db.collection.find(query, projection) - finds documents matching the query

print("\n--- Finding Documents ---");

// Find ALL documents
// The .toArray() is used in scripts to print the cursor output, otherwise in mongosh just db.employees.find() is enough.
print("All employees:");
printjson(db.employees.find().toArray());

// Find ONE document matching a condition
print("Find one employee in HR:");
printjson(db.employees.findOne({ department: "HR" }));

// ------------------------------------------------------------------------------
// 3. UPDATE
// ------------------------------------------------------------------------------
// db.collection.updateOne(filter, update, options)
// db.collection.updateMany(filter, update, options)
// Operators: $set (update field), $unset (remove field), $inc (increment)

print("\n--- Updating Documents ---");

// Update Alice's salary
db.employees.updateOne(
    { name: "Alice Johnson" }, // Filter
    { $set: { salary: 90000, role: "Senior Software Engineer" } } // Update operation
);

// Give everyone in Engineering a $5000 bonus/raise
db.employees.updateMany(
    { department: "Engineering" },
    { $inc: { salary: 5000 } }
);

print("Alice's updated document:");
printjson(db.employees.findOne({ name: "Alice Johnson" }));

// ------------------------------------------------------------------------------
// 4. DELETE
// ------------------------------------------------------------------------------
// db.collection.deleteOne(filter)
// db.collection.deleteMany(filter)

print("\n--- Deleting Documents ---");

// Delete Evan
db.employees.deleteOne({ name: "Evan Wright" });

// Delete all unassigned employees (just an example, none exist here currently)
db.employees.deleteMany({ department: { $exists: false } });

print("Remaining employees count:", db.employees.countDocuments());


// ==============================================================================
// PRACTICE QUESTIONS (LeetCode Style mapping easy -> difficult)
// ==============================================================================
/*
Q1 (Easy): Insert a new employee named "Frank Castle" into the "Marketing" department with a salary of 80000.
Solution:
db.employees.insertOne({ name: "Frank Castle", department: "Marketing", salary: 80000 });

Q2 (Easy): Find the document for the employee with emp_id 103.
Solution:
db.employees.find({ emp_id: 103 });

Q3 (Medium): Bob Smith got promoted. Update his department to "Management" and increment his salary by 15000.
Solution:
db.employees.updateOne({ name: "Bob Smith" }, { $set: { department: "Management" }, $inc: { salary: 15000 } });

Q4 (Medium): Remove all employees who are in the "Marketing" department.
Solution:
db.employees.deleteMany({ department: "Marketing" });

Q5 (Hard - Tricky Concept): Try to update Diana Prince's document to completely replace it (not using $set), changing only her name and salary, effectively removing her skills and department.
Solution:
// Note: replaceOne completely drops the old document and replaces it with the new one (except _id).
db.employees.replaceOne(
    { emp_id: 104 },
    { name: "Diana Prince", salary: 135000 }
);
*/
