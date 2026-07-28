---
id: "09_01_04"
title: "Functions and Scope"
course: "C"
module: 1
module_title: "C Fundamentals"
lesson: 4
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["function", "prototype", "return", "void", "scope", "static", "extern", "auto", "register", "recursion"]
prerequisites: []
lab_required: true
---

# Functions and Scope

## Functions

```c
#include <stdio.h>

/* Function prototype (declaration) — before main */
double calculate_bmi(double weight, double height);
void print_bmi(double bmi);

int main(void) {
    double bmi = calculate_bmi(70.0, 1.75);
    print_bmi(bmi);
    return 0;
}

/* Function definitions */
double calculate_bmi(double weight, double height) {
    if (height <= 0.0) return -1.0;  /* error sentinel */
    return weight / (height * height);
}

void print_bmi(double bmi) {
    const char *category;
    if      (bmi < 18.5) category = "Underweight";
    else if (bmi < 25.0) category = "Normal";
    else if (bmi < 30.0) category = "Overweight";
    else                  category = "Obese";
    printf("BMI: %.2f (%s)\n", bmi, category);
}
```

## Scope and Storage Classes

```c
int global_var = 10;   /* file scope, static storage */

void func(void) {
    int local = 20;    /* block scope, automatic storage */
    static int count = 0;  /* block scope, STATIC storage (persists) */
    count++;
    printf("Called %d times\n", count);
}

/* static at file level — limits visibility to this file */
static void internal_helper(void) { /* not visible outside */ }

/* extern — access global from another file */
extern int shared_counter;
```

## Recursion

```c
/* Factorial */
unsigned long long factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

/* Fibonacci with memoization */
#define MAX 100
long long memo[MAX] = {0};
long long fib(int n) {
    if (n <= 1) return n;
    if (memo[n]) return memo[n];
    memo[n] = fib(n-1) + fib(n-2);
    return memo[n];
}

/* Tower of Hanoi */
void hanoi(int n, char from, char to, char via) {
    if (n == 1) { printf("Move disk 1 from %c to %c\n", from, to); return; }
    hanoi(n-1, from, via, to);
    printf("Move disk %d from %c to %c\n", n, from, to);
    hanoi(n-1, via, to, from);
}
```

## Lab Exercise
1. Write a recursive `power(base, exp)` function without using `math.h`
2. Use `static` local variable to count function invocations
3. Split a C program into two files with a header; use `extern` for shared data
