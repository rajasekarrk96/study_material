# Classes and Constructors

> **Course**: Cpp | **Module**: Object-Oriented C++ | **Difficulty**: intermediate

---

```cpp
class BankAccount {
private:
    std::string owner_;
    double balance_;

public:
    // Constructor with initializer list (preferred)
    explicit BankAccount(std::string owner, double initial = 0.0)
        : owner_(std::move(owner)), balance_(initial) {
        if (initial < 0) throw std::invalid_argument("Negative balance");
    }

    // Copy constructor
    BankAccount(const BankAccount &other)
        : owner_(other.owner_), balance_(other.balance_) {}

    // Move constructor
    BankAccount(BankAccount &&other) noexcept
        : owner_(std::move(other.owner_)), balance_(other.balance_) {
        other.balance_ = 0;
    }

    // Destructor
    ~BankAccount() { /* clean up if needed */ }

    // Member functions
    void deposit(double amount) {
        if (amount <= 0) throw std::invalid_argument("Amount must be positive");
        balance_ += amount;
    }

    double balance() const { return balance_; }  // const: doesn't modify object

    // Friend function
    friend std::ostream &operator<<(std::ostream &os, const BankAccount &acc);
};

std::ostream &operator<<(std::ostream &os, const BankAccount &acc) {
    return os << "Account[" << acc.owner_ << ": $" << acc.balance_ << "]";
}
```

---

```cpp
// Rule of Zero: if no custom destructor needed, use defaults
class Simple {
    std::string name;  // std::string manages its own memory
    int value = 0;
    // No custom destructor, copy, move needed!
};

// Rule of Five: if you define any of these, define all 5:
// destructor, copy constructor, copy assignment,
// move constructor, move assignment

// Delete to prevent copying
class NonCopyable {
public:
    NonCopyable() = default;
    NonCopyable(const NonCopyable &) = delete;
    NonCopyable &operator=(const NonCopyable &) = delete;
    NonCopyable(NonCopyable &&) = default;
    NonCopyable &operator=(NonCopyable &&) = default;
};
```

---

1. Implement a `Matrix` class with constructor, copy/move, and `operator*`
2. Create a `RAII` file handle class that auto-closes on destruction
3. Demonstrate the difference between `explicit` and non-explicit constructors

---
