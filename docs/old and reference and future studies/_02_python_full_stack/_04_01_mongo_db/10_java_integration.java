// ==============================================================================
// 10: MongoDB Java Integration (MongoDB Java Driver)
// ==============================================================================

// Prerequisites:
// Add this to your Maven pom.xml:
/*
<dependency>
    <groupId>org.mongodb</groupId>
    <artifactId>mongodb-driver-sync</artifactId>
    <version>5.0.0</version> 
</dependency>
*/

// Note: To run this as a standalone file, you need a project setup with the driver on your classpath.
// This file serves as your interview prep reference.

import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.model.Filters;
import com.mongodb.client.model.Updates;
import org.bson.Document;
import java.util.Arrays;

public class MongoJavaExample {

    public static void main(String[] args) {
        
        // ------------------------------------------------------------------------------
        // 1. CONNECTION
        // ------------------------------------------------------------------------------
        // Connect to MongoDB
        String uri = "mongodb://localhost:27017";
        System.out.println("Connecting to MongoDB...");
        
        // Try-with-resources handles closing the client automatically
        try (MongoClient mongoClient = MongoClients.create(uri)) {
            
            // Access Database
            MongoDatabase database = mongoClient.getDatabase("interview_prep_java");
            
            // Access Collection (Uses Document class by default)
            MongoCollection<Document> collection = database.getCollection("users");
            
            // Clean up
            collection.drop();

            // ------------------------------------------------------------------------------
            // 2. CREATE (Insert)
            // ------------------------------------------------------------------------------
            System.out.println("\n--- Inserting Document ---");
            Document doc = new Document("name", "Alice")
                            .append("age", 30)
                            .append("city", "London");
            collection.insertOne(doc);
            System.out.println("Inserted Alice.");

            Document doc2 = new Document("name", "Bob").append("age", 25).append("city", "Paris");
            Document doc3 = new Document("name", "Charlie").append("age", 40).append("city", "London");
            collection.insertMany(Arrays.asList(doc2, doc3));
            System.out.println("Inserted Bob and Charlie.");

            // ------------------------------------------------------------------------------
            // 3. READ (Find)
            // ------------------------------------------------------------------------------
            // Using com.mongodb.client.model.Filters helper is highly recommended
            System.out.println("\n--- Finding London Residents ---");
            
            // Using standard find() returns a FindIterable.
            // Using Filters.eq() creates the BSON query cleanly.
            for (Document user : collection.find(Filters.eq("city", "London"))) {
                System.out.println(user.toJson());
            }

            // ------------------------------------------------------------------------------
            // 4. UPDATE
            // ------------------------------------------------------------------------------
            System.out.println("\n--- Updating Bob's Age ---");
            // Using Updates.set() helper
            collection.updateOne(
                Filters.eq("name", "Bob"), 
                Updates.set("age", 26)
            );
            
            Document updatedBob = collection.find(Filters.eq("name", "Bob")).first();
            System.out.println("Updated Bob: " + updatedBob.toJson());

            // ------------------------------------------------------------------------------
            // 5. DELETE
            // ------------------------------------------------------------------------------
            System.out.println("\n--- Deleting Charlie ---");
            collection.deleteOne(Filters.eq("name", "Charlie"));
            System.out.println("Total documents left: " + collection.countDocuments());
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}


// ==============================================================================
// PRACTICE QUESTIONS (LeetCode Style for Java Driver)
// ==============================================================================
/*
Q1 (Easy): In Java, what class represents a single BSON document? How do you add key-value pairs to it?
Solution:
The `org.bson.Document` class. You use the `.append("key", value)` method.

Q2 (Easy): Write the Java code snippet to find all documents in `collection` where "age" is greater than 18.
Solution:
import static com.mongodb.client.model.Filters.*;
// ...
collection.find(gt("age", 18)); // returns FindIterable<Document>

Q3 (Medium): Write a multi-update in Java to set "status" to "active" for all documents where "city" is "New York".
Solution:
collection.updateMany(
    Filters.eq("city", "New York"),
    Updates.set("status", "active")
);

Q4 (Medium): How do you project (select only specific fields) in the Java driver so you only return the "name" field and exclude "_id"?
Solution:
import static com.mongodb.client.model.Projections.*;

collection.find()
          .projection(fields(include("name"), excludeId()));

Q5 (Hard - Advanced Drivers): Working with raw `Document` maps can be prone to typos. What alternative object-mapping feature does the official Java driver provide out-of-the-box using Codecs, allowing you to map directly to a custom `Employee` Java class?
Solution:
The Java Driver natively supports POJO (Plain Old Java Object) mappings. 
You can construct a `PojoCodecProvider` added to the `CodecRegistry`, and then request a collection parametrized to your class:
`MongoCollection<Employee> collection = database.getCollection("employees", Employee.class);`
Then `collection.find()` returns an iterable of fully hydrated `Employee` objects rather than `Document` maps!
*/
