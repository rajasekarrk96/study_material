---
id: "08_06_01"
title: "JDBC Fundamentals"
course: "Java"
module: 6
module_title: "Database Access"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["JDBC", "Connection", "Statement", "PreparedStatement", "ResultSet", "DataSource", "connection-pool", "HikariCP", "transaction"]
prerequisites: []
lab_required: true
---

# JDBC Fundamentals

## JDBC Basics

```java
import java.sql.*;

// Load driver (auto-registered in JDBC 4+)
String url = "jdbc:mysql://localhost:3306/mydb";
String user = "root", pass = "password";

try (Connection conn = DriverManager.getConnection(url, user, pass)) {
    // PreparedStatement — prevents SQL injection
    String sql = "SELECT id, name, salary FROM employees WHERE dept_id = ?";
    try (PreparedStatement ps = conn.prepareStatement(sql)) {
        ps.setInt(1, 3);
        try (ResultSet rs = ps.executeQuery()) {
            while (rs.next()) {
                int id       = rs.getInt("id");
                String name  = rs.getString("name");
                double salary = rs.getDouble("salary");
                System.out.printf("%d: %s = %.2f%n", id, name, salary);
            }
        }
    }
}
```

## CRUD Operations

```java
// INSERT with generated key
String insert = "INSERT INTO products (name, price) VALUES (?, ?)";
try (PreparedStatement ps = conn.prepareStatement(insert,
        Statement.RETURN_GENERATED_KEYS)) {
    ps.setString(1, "Widget");
    ps.setDouble(2, 9.99);
    int rows = ps.executeUpdate();   // returns affected rows
    try (ResultSet keys = ps.getGeneratedKeys()) {
        if (keys.next()) System.out.println("New ID: " + keys.getInt(1));
    }
}

// UPDATE / DELETE
String update = "UPDATE products SET price = ? WHERE id = ?";
try (PreparedStatement ps = conn.prepareStatement(update)) {
    ps.setDouble(1, 14.99);
    ps.setInt(2, 5);
    ps.executeUpdate();
}
```

## Connection Pooling with HikariCP

```java
import com.zaxxer.hikari.*;

HikariConfig config = new HikariConfig();
config.setJdbcUrl("jdbc:mysql://localhost:3306/mydb");
config.setUsername("root");
config.setPassword("password");
config.setMaximumPoolSize(10);
config.setMinimumIdle(5);
config.setConnectionTimeout(30000);

HikariDataSource ds = new HikariDataSource(config);

try (Connection conn = ds.getConnection()) {
    // use conn
}  // returned to pool automatically
```

## Transactions

```java
conn.setAutoCommit(false);
try {
    deductBalance(conn, fromId, amount);
    addBalance(conn, toId, amount);
    conn.commit();
} catch (SQLException e) {
    conn.rollback();
    throw e;
}
```

## Lab Exercise
1. Build a `ProductDAO` with CRUD methods using `PreparedStatement`
2. Configure HikariCP and benchmark single connection vs pool for 100 queries
3. Implement a bank transfer with proper transaction rollback on any failure
