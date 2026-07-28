---
id: "10_02_03"
title: "Inheritance and Polymorphism"
course: "C++"
module: 2
module_title: "Object-Oriented C++"
lesson: 3
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["virtual", "override", "final", "pure-virtual", "abstract", "vtable", "dynamic_cast", "RTTI"]
prerequisites: []
lab_required: true
---

# Inheritance and Polymorphism

## Virtual Functions and Polymorphism

```cpp
class Shape {
public:
    virtual double area() const = 0;       // pure virtual
    virtual double perimeter() const = 0;  // pure virtual
    virtual std::string name() const { return "Shape"; }
    virtual ~Shape() = default;            // virtual destructor!
};

class Circle : public Shape {
    double radius_;
public:
    explicit Circle(double r) : radius_(r) {}
    double area()      const override { return M_PI * radius_ * radius_; }
    double perimeter() const override { return 2 * M_PI * radius_; }
    std::string name() const override { return "Circle"; }
};

// Polymorphism via pointer/reference
std::vector<std::unique_ptr<Shape>> shapes;
shapes.push_back(std::make_unique<Circle>(5));
shapes.push_back(std::make_unique<Rectangle>(4, 6));

for (const auto &s : shapes) {
    std::cout << s->name() << ": area=" << s->area() << "\n";
}
```

## dynamic_cast and RTTI

```cpp
Shape *ptr = get_some_shape();

// Safe downcast — returns nullptr on failure
if (auto *c = dynamic_cast<Circle *>(ptr)) {
    std::cout << "It's a circle with r=" << c->radius() << "\n";
}

// typeid
std::cout << typeid(*ptr).name() << "\n";
```

## final and override

```cpp
class Animal {
    virtual void speak() const {}
};

class Dog final : public Animal {   // cannot be subclassed
    void speak() const override final { std::cout << "Woof!\n"; }
};
```

## Lab Exercise
1. Build a `Shape` hierarchy, compute total area polymorphically
2. Demonstrate why `virtual ~Shape()` is essential — show double-free bug without it
3. Use `dynamic_cast` to safely downcast a base pointer to derived
