# Encapsulation and Access Control

> **Course**: Java | **Module**: Object-Oriented Programming | **Difficulty**: intermediate

---

| Modifier | Same Class | Same Package | Subclass | Any |
|---|---|---|---|---|
| `private` | ✅ | ❌ | ❌ | ❌ |
| (package) | ✅ | ✅ | ❌ | ❌ |
| `protected` | ✅ | ✅ | ✅ | ❌ |
| `public` | ✅ | ✅ | ✅ | ✅ |

---

```java
public class Temperature {
    private double celsius;

    public Temperature(double celsius) {
        setCelsius(celsius);
    }

    public double getCelsius()    { return celsius; }
    public double getFahrenheit() { return celsius * 9/5 + 32; }
    public double getKelvin()     { return celsius + 273.15; }

    public void setCelsius(double celsius) {
        if (celsius < -273.15)
            throw new IllegalArgumentException("Below absolute zero!");
        this.celsius = celsius;
    }
}
```

---

```java
// All fields final, no setters, defensive copies
public final class Money {
    private final double amount;
    private final String currency;

    public Money(double amount, String currency) {
        if (amount < 0) throw new IllegalArgumentException();
        this.amount = amount;
        this.currency = currency;
    }

    public double getAmount()   { return amount; }
    public String getCurrency() { return currency; }

    public Money add(Money other) {
        if (!currency.equals(other.currency)) throw new IllegalStateException();
        return new Money(amount + other.amount, currency);  // new object
    }
}
```

---

```java
public class User {
    private final String name;
    private final String email;
    private final int age;

    private User(Builder b) {
        this.name  = b.name;
        this.email = b.email;
        this.age   = b.age;
    }

    public static class Builder {
        private String name;
        private String email;
        private int age = 0;

        public Builder name(String name)   { this.name = name; return this; }
        public Builder email(String email) { this.email = email; return this; }
        public Builder age(int age)        { this.age = age; return this; }
        public User build()                { return new User(this); }
    }
}

User user = new User.Builder()
    .name("Raja")
    .email("raja@example.com")
    .age(28)
    .build();
```

---

1. Build an immutable `ImmutableList<T>` wrapper that throws on modification attempts
2. Implement `Address` using Builder pattern with required and optional fields
3. Show how `final` prevents subclassing and why `String` is final

---
