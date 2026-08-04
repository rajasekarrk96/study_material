# Operator Overloading

> **Course**: Cpp | **Module**: Object-Oriented C++ | **Difficulty**: intermediate

---

```cpp
struct Vector2D {
    double x, y;

    Vector2D(double x = 0, double y = 0) : x(x), y(y) {}

    // Member operator
    Vector2D operator+(const Vector2D &rhs) const {
        return {x + rhs.x, y + rhs.y};
    }

    Vector2D &operator+=(const Vector2D &rhs) {
        x += rhs.x; y += rhs.y; return *this;
    }

    // Scalar multiplication
    Vector2D operator*(double scalar) const { return {x*scalar, y*scalar}; }

    // Unary minus
    Vector2D operator-() const { return {-x, -y}; }

    // Length
    double length() const { return std::sqrt(x*x + y*y); }

    // Comparison (C++20 spaceship operator)
    auto operator<=>(const Vector2D &) const = default;  // lexicographic
    bool operator==(const Vector2D &) const = default;
};

// Non-member: double * Vector2D
Vector2D operator*(double scalar, const Vector2D &v) { return v * scalar; }

// Stream output
std::ostream &operator<<(std::ostream &os, const Vector2D &v) {
    return os << "(" << v.x << ", " << v.y << ")";
}

Vector2D a{1, 2}, b{3, 4};
auto c = a + b;           // (4, 6)
std::cout << c;
auto d = 2.0 * a;         // (2, 4)
bool eq = (a == a);       // true
```

---

```cpp
class Matrix {
    std::vector<std::vector<double>> data_;
    int rows_, cols_;
public:
    // operator[] for row access
    std::vector<double> &operator[](int i) { return data_[i]; }
    const std::vector<double> &operator[](int i) const { return data_[i]; }

    // operator() for element access
    double &operator()(int r, int c) { return data_[r][c]; }
};

Matrix m(3, 3);
m[0][0] = 1.0;
m(1, 2) = 3.14;
```

---

1. Implement a `Fraction` class with `+`, `-`, `*`, `/`, `<<`, `==` operators
2. Add `<=>` spaceship operator to `Fraction` and verify sorting works
3. Create a `JSON` class with `operator[]` for string keys and integer indices

---
