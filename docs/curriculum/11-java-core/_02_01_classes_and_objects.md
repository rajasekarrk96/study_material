# Classes and Objects

> **Course**: Java | **Module**: Object-Oriented Programming | **Difficulty**: intermediate

---

```java
public class BankAccount {
    // Fields (instance variables)
    private final String accountId;
    private String owner;
    private double balance;
    private static int accountCount = 0;  // class variable

    // Constructor
    public BankAccount(String owner, double initialBalance) {
        this.accountId = "ACC" + (++accountCount);
        this.owner = owner;
        this.balance = initialBalance;
    }

    // Methods
    public void deposit(double amount) {
        if (amount <= 0) throw new IllegalArgumentException("Amount must be positive");
        this.balance += amount;
    }

    public double withdraw(double amount) {
        if (amount > balance) throw new IllegalStateException("Insufficient funds");
        this.balance -= amount;
        return amount;
    }

    // Getters / Setters
    public double getBalance() { return balance; }
    public String getOwner()   { return owner; }
    public void setOwner(String owner) { this.owner = owner; }

    // toString, equals, hashCode
    @Override
    public String toString() {
        return String.format("BankAccount[id=%s, owner=%s, balance=%.2f]",
                             accountId, owner, balance);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof BankAccount other)) return false;
        return accountId.equals(other.accountId);
    }

    @Override
    public int hashCode() { return accountId.hashCode(); }
}
```

---

```java
BankAccount acc = new BankAccount("Raja", 1000.0);
acc.deposit(500.0);
System.out.println(acc.getBalance());   // 1500.0
System.out.println(acc);               // BankAccount[id=ACC1, owner=Raja, balance=1500.00]

// Static members
System.out.println(BankAccount.accountCount);
```

---

```java
public record Point(double x, double y) {
    // Compact constructor (validation)
    public Point {
        if (Double.isNaN(x) || Double.isNaN(y))
            throw new IllegalArgumentException("Coordinates cannot be NaN");
    }

    // Custom method
    public double distanceTo(Point other) {
        return Math.hypot(other.x - x, other.y - y);
    }
}

var p = new Point(3, 4);
p.x()              // 3.0
p.distanceTo(new Point(0, 0))  // 5.0
```

---

1. Build a `Student` class with name, id, grades[] — compute average, min, max
2. Create a `Point` record and implement `distance()`, `midpoint()`, `translate()`
3. Override `equals()` and `hashCode()` and verify two equal objects in a `HashSet`

---
