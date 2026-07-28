---
id: "09_04_02"
title: "Preprocessor and Macros"
course: "C"
module: 4
module_title: "Systems Programming"
lesson: 2
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["#define", "#include", "#ifdef", "#ifndef", "macro", "function-macro", "guard", "#pragma", "conditional-compilation"]
prerequisites: []
lab_required: true
---

# Preprocessor and Macros

## Preprocessor Directives

```c
/* File inclusion */
#include <stdio.h>          /* system header */
#include "my_header.h"      /* local header */

/* Constants (macro) */
#define PI        3.14159265
#define MAX_SIZE  100
#define COMPANY   "TechCorp"

/* Function-like macros */
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define SQUARE(x) ((x) * (x))
#define ABS(x)    ((x) < 0 ? -(x) : (x))

/* Parentheses are essential! */
/* SQUARE(1+2) -> ((1+2)*(1+2)) = 9  (correct) */
/* without parens: (1+2*1+2) = 5  (wrong!) */
```

## Include Guards

```c
/* my_header.h */
#ifndef MY_HEADER_H
#define MY_HEADER_H

typedef struct { int x, y; } Point;
void point_print(Point p);

#endif /* MY_HEADER_H */

/* Or use #pragma once (non-standard but widely supported) */
#pragma once
```

## Conditional Compilation

```c
#define DEBUG 1

#if DEBUG
    #define LOG(msg) fprintf(stderr, "[DEBUG] %s:%d: %s\n", __FILE__, __LINE__, msg)
#else
    #define LOG(msg) /* nothing */
#endif

/* Platform detection */
#ifdef _WIN32
    #define PATH_SEP "\"
#else
    #define PATH_SEP "/"
#endif

/* gcc -DDEBUG=1 */
```

## Predefined Macros

```c
__FILE__    /* "main.c" */
__LINE__    /* 42 */
__func__    /* "main" */
__DATE__    /* "Jul 28 2024" */
__TIME__    /* "13:45:00" */
```

## Variadic Macros

```c
#define DEBUG_PRINT(fmt, ...) \
    fprintf(stderr, "[%s:%d] " fmt "\n", __FILE__, __LINE__, ##__VA_ARGS__)

DEBUG_PRINT("Value: %d", 42);
DEBUG_PRINT("Hello World");
```

## Lab Exercise
1. Write a `ASSERT(cond)` macro that prints file, line, and expression on failure
2. Create a debug logging system: DEBUG level off in release build via `-DNDEBUG`
3. Write a generic `SWAP(type, a, b)` macro and test for int, float, char
