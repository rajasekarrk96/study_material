// ==============================================================================
// 05: MongoDB Aggregation Framework
// ==============================================================================

// HOW TO RUN THIS FILE:
// mongosh < 05_aggregation.js

use interview_prep;
db.orders.drop();

// ------------------------------------------------------------------------------
// Sample Data Creation
// ------------------------------------------------------------------------------
db.orders.insertMany([
    { _id: 1, customer: "Alice", item: "Laptop", price: 1000, qty: 1, date: new Date("2023-01-10"), status: "shipped" },
    { _id: 2, customer: "Bob", item: "Mouse", price: 20, qty: 2, date: new Date("2023-01-15"), status: "shipped" },
    { _id: 3, customer: "Alice", item: "Monitor", price: 300, qty: 2, date: new Date("2023-02-10"), status: "processing" },
    { _id: 4, customer: "Charlie", item: "Keyboard", price: 80, qty: 1, date: new Date("2023-02-20"), status: "shipped" },
    { _id: 5, customer: "Bob", item: "Laptop", price: 1000, qty: 1, date: new Date("2023-03-05"), status: "cancelled" },
    { _id: 6, customer: "Alice", item: "Mouse", price: 20, qty: 3, date: new Date("2023-03-15"), status: "shipped" }
]);

// ------------------------------------------------------------------------------
// AGGREGATION PIPELINE CONCEPTS (A sequence of data processing stages)
// ------------------------------------------------------------------------------
// db.collection.aggregate([ {stage1}, {stage2}, ... ])

print("\n--- Pipeline 1: Total Spent by Customer on Shipped Orders ---");
// Stages:
// 1. $match (Filter like a normal find) -> ONLY shipped orders
// 2. $group (Group by customer, calculate sum)
// 3. $sort (Sort by total spent descending)

let pipeline1 = [
    { $match: { status: "shipped" } },
    { 
        $group: { 
            _id: "$customer", // Group by 'customer' field
            totalSpent: { $sum: { $multiply: ["$price", "$qty"] } }, // Calculate cost per order line, then sum
            totalItems: { $sum: "$qty" }
        } 
    },
    { $sort: { totalSpent: -1 } }
];

printjson(db.orders.aggregate(pipeline1).toArray());

print("\n--- Pipeline 2: $project and $limit ---");
// The $project stage shapes the output (like SELECT in SQL, but allows new computed fields)

let pipeline2 = [
    { $match: { item: "Laptop" } },
    {
        $project: {
            // Include customer
            customerName: "$customer", 
            // Create a new computed field
            orderTotal: { $multiply: ["$price", "$qty"] },
            // Date formatting (extract just the month)
            orderMonth: { $month: "$date" },
            _id: 0
        }
    },
    { $limit: 2 } // Only show first 2 results
];

printjson(db.orders.aggregate(pipeline2).toArray());

print("\n--- Pipeline 3: $unwind (If we had arrays) ---");
// $unwind deconstructs an array field, outputting a document for each element.
// Example conceptually: { a: 1, b: [1,2] } -> unwinds to -> { a: 1, b: 1 }, { a: 1, b: 2 }


// ==============================================================================
// PRACTICE QUESTIONS (LeetCode Style)
// ==============================================================================
/*
Q1 (Easy): Create an aggregation pipeline with a single `$match` stage to find orders where the `status` is "processing".
Solution:
db.orders.aggregate([
    { $match: { status: "processing" } }
]);

Q2 (Easy): Use `$group` to find the total number of orders (documents) per customer.
Solution:
db.orders.aggregate([
    { $group: { _id: "$customer", totalOrders: { $sum: 1 } } }
]);

Q3 (Medium): Find the highest priced item ever ordered (single document) using $sort and $limit.
Solution:
db.orders.aggregate([
    { $sort: { price: -1 } },
    { $limit: 1 }
]);

Q4 (Medium): Use `$match` and `$group` to calculate the total quantity (`qty`) of "Mouse" items ordered across all customers.
Solution:
db.orders.aggregate([
    { $match: { item: "Mouse" } },
    { $group: { _id: null, totalMice: { $sum: "$qty" } } } // _id: null means group everything into one document
]);

Q5 (Hard): Calculate the average total cost ($price * $qty) of "shipped" orders per customer. Sort the results alphabetically by customer name. Use $project to simplify the output to only show `customer` and `averageCost`.
Solution:
db.orders.aggregate([
    { $match: { status: "shipped" } },
    { 
        $group: { 
            _id: "$customer", 
            totalLineCost: { $sum: { $multiply: ["$price", "$qty"] } },
            orderCount: { $sum: 1 }
        } 
    },
    {
        $project: {
            customer: "$_id",
            averageCost: { $divide: ["$totalLineCost", "$orderCount"] },
            _id: 0
        }
    },
    { $sort: { customer: 1 } }
]);
// Note: Alternatively, $avg accumulator can be used if we pre-calculate order cost.
*/
