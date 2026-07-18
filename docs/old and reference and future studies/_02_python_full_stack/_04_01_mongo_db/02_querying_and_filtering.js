// ==============================================================================
// 02: MongoDB Querying and Filtering
// ==============================================================================

// HOW TO RUN THIS FILE:
// mongosh < 02_querying_and_filtering.js

use interview_prep;
db.products.drop(); // Cleanup

// ------------------------------------------------------------------------------
// Sample Data Creation
// ------------------------------------------------------------------------------
db.products.insertMany([
    { _id: 1, name: "Laptop", category: "Electronics", price: 1200, stock: 45, ratings: 4.5, tags: ["pc", "work"] },
    { _id: 2, name: "Mouse", category: "Electronics", price: 25, stock: 150, ratings: 4.8, tags: ["accessory", "work"] },
    { _id: 3, name: "Desk Chair", category: "Furniture", price: 250, stock: 20, ratings: 4.2, tags: ["office", "furniture"] },
    { _id: 4, name: "Coffee Maker", category: "Appliances", price: 80, stock: 5, ratings: 3.9, tags: ["kitchen"] },
    { _id: 5, name: "Monitor", category: "Electronics", price: 300, stock: 0, ratings: 4.6, tags: ["pc", "gaming", "work"] },
    { _id: 6, name: "Headphones", category: "Electronics", price: 150, stock: 60, ratings: 4.9, tags: ["audio", "accessory"] }
]);

// ------------------------------------------------------------------------------
// 1. COMPARISON OPERATORS
// ------------------------------------------------------------------------------
// $eq (Equal), $ne (Not Equal), $gt (Greater Than), $gte (Greater Than/Equal)
// $lt (Less Than), $lte (Less Than/Equal), $in (In array), $nin (Not in array)

print("\n--- Products with price > 200 ---");
printjson(db.products.find({ price: { $gt: 200 } }).toArray());

print("\n--- Products in category 'Furniture' or 'Appliances' ---");
printjson(db.products.find({ category: { $in: ["Furniture", "Appliances"] } }).toArray());

// ------------------------------------------------------------------------------
// 2. LOGICAL OPERATORS
// ------------------------------------------------------------------------------
// $and, $or, $nor, $not

print("\n--- Electronics AND price < 200 (Implicit AND) ---");
printjson(db.products.find({ category: "Electronics", price: { $lt: 200 } }).toArray());

print("\n--- Explicit $or: Price > 1000 OR Stock == 0 ---");
printjson(db.products.find({
    $or: [
        { price: { $gt: 1000 } },
        { stock: { $eq: 0 } }
    ]
}).toArray());

// ------------------------------------------------------------------------------
// 3. REGEX & ELEMENT OPERATORS
// ------------------------------------------------------------------------------
// $exists, $type, $regex

print("\n--- Products starting with 'M' (Regex) ---");
printjson(db.products.find({ name: { $regex: /^M/ } }).toArray());

print("\n--- Products that have the 'tags' field ---");
printjson(db.products.find({ tags: { $exists: true } }).toArray());

// ------------------------------------------------------------------------------
// 4. PROJECTION (Selecting specific fields)
// ------------------------------------------------------------------------------
// 1 = include, 0 = exclude. Cannot mix 1 and 0 except for _id.

print("\n--- Only show name and price, hide _id ---");
printjson(db.products.find({}, { name: 1, price: 1, _id: 0 }).toArray());


// ==============================================================================
// PRACTICE QUESTIONS (LeetCode Style)
// ==============================================================================
/*
Q1 (Easy): Find all products that have a rating of 4.5 or higher.
Solution:
db.products.find({ ratings: { $gte: 4.5 } });

Q2 (Easy): Find all products whose stock is less than 50, and only return their "name" and "stock" (exclude _id).
Solution:
db.products.find({ stock: { $lt: 50 } }, { name: 1, stock: 1, _id: 0 });

Q3 (Medium): Find all products that are NOT in the "Electronics" category.
Solution:
db.products.find({ category: { $ne: "Electronics" } });
// Alternative: db.products.find({ category: { $nin: ["Electronics"] } });

Q4 (Medium): Find all products where the stock is between 10 and 100 (inclusive).
Solution:
db.products.find({ stock: { $gte: 10, $lte: 100 } });

Q5 (Hard): Find all products where the category is "Electronics", OR the rating is greater than 4.5 AND the name contains the word "Chair" (case-insensitive).
Solution:
db.products.find({
    $or: [
        { category: "Electronics" },
        { 
            $and: [
                { ratings: { $gt: 4.5 } },
                { name: { $regex: /chair/i } }
            ] 
        }
    ]
});
*/
