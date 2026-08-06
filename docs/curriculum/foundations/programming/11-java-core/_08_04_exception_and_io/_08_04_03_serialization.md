---
id: "08_04_03"
title: "Serialization"
course: "Java"
module: 4
module_title: "Exceptions and I/O"
lesson: 3
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["Serializable", "ObjectOutputStream", "ObjectInputStream", "transient", "serialVersionUID", "JSON", "Gson", "Jackson"]
prerequisites: []
lab_required: true
---

# Serialization

## Java Object Serialization

```java
import java.io.*;

// Must implement Serializable
public class User implements Serializable {
    private static final long serialVersionUID = 1L;  // version control
    private String name;
    private String email;
    private transient String password;  // NOT serialized

    // constructor, getters...
}

// Serialize (write)
User user = new User("Raja", "raja@example.com");
try (ObjectOutputStream oos = new ObjectOutputStream(
        new FileOutputStream("user.ser"))) {
    oos.writeObject(user);
}

// Deserialize (read)
try (ObjectInputStream ois = new ObjectInputStream(
        new FileInputStream("user.ser"))) {
    User loaded = (User) ois.readObject();
    System.out.println(loaded.getName());
}
```

## JSON with Gson

```java
// pom.xml: com.google.code.gson:gson:2.10.1
import com.google.gson.*;

Gson gson = new GsonBuilder()
    .setPrettyPrinting()
    .setDateFormat("yyyy-MM-dd")
    .create();

// Object → JSON string
String json = gson.toJson(user);

// JSON string → Object
User parsed = gson.fromJson(json, User.class);

// List of objects
Type listType = new TypeToken<List<User>>(){}.getType();
List<User> users = gson.fromJson(jsonArray, listType);
```

## JSON with Jackson

```java
// pom.xml: com.fasterxml.jackson.core:jackson-databind:2.17
import com.fasterxml.jackson.databind.*;

ObjectMapper mapper = new ObjectMapper();
mapper.configure(SerializationFeature.INDENT_OUTPUT, true);

// Write
String json = mapper.writeValueAsString(user);
mapper.writeValue(new File("user.json"), user);

// Read
User user = mapper.readValue(json, User.class);
User user = mapper.readValue(new File("user.json"), User.class);

// Tree model (dynamic)
JsonNode root = mapper.readTree(json);
String name = root.get("name").asText();
```

## Lab Exercise
1. Serialize a `Product` list to binary with Java serialization, then JSON with Jackson
2. Show what happens when `serialVersionUID` changes — demonstrate `InvalidClassException`
3. Build a JSON config reader that loads app settings from `config.json`
