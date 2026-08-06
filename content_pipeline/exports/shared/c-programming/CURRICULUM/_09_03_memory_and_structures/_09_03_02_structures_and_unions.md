---
id: "09_03_02"
title: "Structures and Unions"
course: "C"
module: 3
module_title: "Advanced C"
lesson: 2
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["struct", "union", "typedef", "padding", "bit-fields", "enum", "nested-struct"]
prerequisites: []
lab_required: true
---

# Structures and Unions

## Structures

```c
#include <stdio.h>

/* Define structure */
typedef struct {
    char name[50];
    int  age;
    float salary;
} Employee;

/* Declaration and initialization */
Employee emp = {"Raja", 28, 75000.0f};
Employee emp2 = {.name = "Alice", .age = 30};   /* designated initialiser */

/* Access members */
printf("%s earns %.2f\n", emp.name, emp.salary);

/* Pointer to struct */
Employee *ptr = &emp;
printf("%s\n", ptr->name);     /* arrow operator */
printf("%d\n", (*ptr).age);    /* same as ptr->age */
```

## Memory Layout and Padding

```c
struct Padded {
    char  a;       /* 1 byte */
    /* 3 bytes padding */
    int   b;       /* 4 bytes */
    char  c;       /* 1 byte */
    /* 3 bytes padding */
};  /* total: 12 bytes (not 6!) */

struct Packed {
    char  a;
    char  c;
    int   b;
};  /* total: 8 bytes (better packing) */

printf("%zu\n", sizeof(struct Padded));  /* 12 */
printf("%zu\n", sizeof(struct Packed));  /* 8 */
```

## Unions

```c
/* All members share the SAME memory */
typedef union {
    int   i;
    float f;
    char  bytes[4];
} Value;

Value v;
v.i = 0x3F800000;
printf("float: %f\n", v.f);  /* 1.0 (IEEE 754 representation) */
printf("int:   %d\n", v.i);  /* same bytes, different interpretation */
```

## Enumerations

```c
typedef enum {
    STATUS_PENDING  = 0,
    STATUS_ACTIVE   = 1,
    STATUS_CLOSED   = 2,
    STATUS_ARCHIVED = 3,
} Status;

Status s = STATUS_ACTIVE;
if (s == STATUS_ACTIVE) printf("Active\n");
```

## Lab Exercise
1. Define a `struct Date` and write functions to compare and format dates
2. Measure struct padding: create optimally packed vs default struct, compare sizes
3. Implement a tagged union for a dynamic type system (int, float, string)
