// ==============================================================================
// 03: MongoDB Advanced Querying (Arrays & Nested Documents)
// ==============================================================================

// HOW TO RUN THIS FILE:
// mongosh < 03_advanced_querying.js

use interview_prep;
db.students.drop(); // Cleanup

// ------------------------------------------------------------------------------
// Sample Data Creation
// ------------------------------------------------------------------------------
db.students.insertMany([
    { 
        _id: 1, name: "John", 
        courses: ["Math", "Physics", "Chemistry"], 
        scores: [85, 92, 78],
        address: { city: "New York", zip: "10001", state: "NY" }
    },
    { 
        _id: 2, name: "Jane", 
        courses: ["Biology", "Chemistry"], 
        scores: [95, 88],
        address: { city: "Boston", zip: "02108", state: "MA" }
    },
    { 
        _id: 3, name: "Sam", 
        courses: ["Math", "Computer Science"], 
        scores: [70, 65, 80],
        address: { city: "New York", zip: "10012", state: "NY" },
        // Array of embedded documents
        projects: [
            { title: "AI Bot", grade: "A", hours: 120 },
            { title: "Web App", grade: "B", hours: 80 }
        ]
    },
    { 
        _id: 4, name: "Lisa", 
        courses: ["Computer Science", "Physics"], 
        scores: [90, 95, 100],
        address: { city: "Seattle", zip: "98101", state: "WA" },
        projects: [
            { title: "Data Analysis", grade: "A", hours: 90 }
        ]
    }
]);

// ------------------------------------------------------------------------------
// 1. QUERYING NESTED DOCUMENTS
// ------------------------------------------------------------------------------
// Use Dot Notation. ALWAYS enclose the field path in quotes!

print("\n--- Students living in NY State ---");
printjson(db.students.find({ "address.state": "NY" }).toArray());

// ------------------------------------------------------------------------------
// 2. QUERYING ARRAYS
// ------------------------------------------------------------------------------

// Equality match on an element (Array contains 'Math')
print("\n--- Students taking Math ---");
printjson(db.students.find({ courses: "Math" }).toArray());

// Exact array match (Must have exactly these elements in this exact order)
// This will match John but not Sam or Jane
print("\n--- Students taking exactly [Math, Physics, Chemistry] ---");
printjson(db.students.find({ courses: ["Math", "Physics", "Chemistry"] }).toArray());

// $all - Array contains all specified elements (order doesn't matter)
print("\n--- Students taking both Math and Chemistry ---");
printjson(db.students.find({ courses: { $all: ["Math", "Chemistry"] } }).toArray());

// $size - Array has exact size
print("\n--- Students taking exactly 2 courses ---");
printjson(db.students.find({ courses: { $size: 2 } }).toArray());

// ------------------------------------------------------------------------------
// 3. THE $elemMatch OPERATOR
// ------------------------------------------------------------------------------
// Crucial for Array of Documents! Ensures that the conditions are met by the SAME element in the array.

// Incorrect way: This matches if ANY project has grade A AND ANY project has hours > 100.
// It could be two different projects satisfying each condition!
print("\n--- $elemMatch (Array of Embedded Docs) ---");
print("Matching specific project criteria:");
printjson(db.students.find({
    projects: { $elemMatch: { grade: "A", hours: { $gt: 100 } } }
}).toArray());


// ==============================================================================
// PRACTICE QUESTIONS (LeetCode Style)
// ==============================================================================
/*
Q1 (Easy): Find students who live in the city "Boston".
Solution:
db.students.find({ "address.city": "Boston" });

Q2 (Easy): Find students who have scored exactly 100 in ANY subject.
Solution:
db.students.find({ scores: 100 });

Q3 (Medium): Find students who are taking 3 courses (using array size).
Solution:
db.students.find({ courses: { $size: 3 } });

Q4 (Medium): Find students whose scores array contains AT LEAST one score greater than 90.
Solution:
db.students.find({ scores: { $gt: 90 } });

Q5 (Hard): Find students who have completed a project titled "Web App" with a grade of "B". Ensure that both conditions are met by the SAME project using $elemMatch.
Solution:
db.students.find({
    projects: { $elemMatch: { title: "Web App", grade: "B" } }
});
*/
