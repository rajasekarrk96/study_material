---
id: "08_04_01"
title: "Exception Handling"
course: "Java"
module: 4
module_title: "Exceptions and I/O"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["try", "catch", "finally", "throws", "throw", "checked", "unchecked", "custom-exception", "multi-catch", "try-with-resources"]
prerequisites: []
lab_required: true
---

# Exception Handling

## Exception Hierarchy

```
Throwable
├── Error          (JVM errors — don't catch)
│   ├── OutOfMemoryError
│   └── StackOverflowError
└── Exception
    ├── RuntimeException  (unchecked — no declaration needed)
    │   ├── NullPointerException
    │   ├── IllegalArgumentException
    │   ├── IndexOutOfBoundsException
    │   └── ClassCastException
    └── Checked exceptions (must declare/catch)
        ├── IOException
        ├── SQLException
        └── ParseException
```

## try / catch / finally

```java
public double divide(double a, double b) {
    try {
        return a / b;
    } catch (ArithmeticException e) {
        System.err.println("Error: " + e.getMessage());
        return 0;
    } finally {
        System.out.println("Operation attempted");  // always runs
    }
}

// Multi-catch (Java 7+)
try {
    parseAndSave(data);
} catch (NumberFormatException | NullPointerException e) {
    throw new IllegalArgumentException("Invalid data: " + e.getMessage(), e);
}
```

## try-with-resources

```java
// Auto-closes anything implementing AutoCloseable
try (
    FileReader  fr = new FileReader("file.txt");
    BufferedReader br = new BufferedReader(fr)
) {
    String line;
    while ((line = br.readLine()) != null) {
        process(line);
    }
} catch (IOException e) {
    throw new RuntimeException("Failed to read file", e);
}
// Both br and fr are automatically closed
```

## Custom Exceptions

```java
// Checked exception
public class InsufficientFundsException extends Exception {
    private final double amount;
    public InsufficientFundsException(double amount) {
        super("Insufficient funds. Needed: " + amount);
        this.amount = amount;
    }
    public double getAmount() { return amount; }
}

// Unchecked exception
public class DuplicateUserException extends RuntimeException {
    public DuplicateUserException(String username) {
        super("User already exists: " + username);
    }
}

// Declare checked exceptions
public void withdraw(double amount) throws InsufficientFundsException {
    if (amount > balance) throw new InsufficientFundsException(amount);
    balance -= amount;
}
```

## Lab Exercise
1. Write a file parser that throws custom `ParseException` with line number and message
2. Implement `retry(Callable<T>, int times)` that retries on IOException
3. Compare checked vs unchecked — when to use each in a REST API context
