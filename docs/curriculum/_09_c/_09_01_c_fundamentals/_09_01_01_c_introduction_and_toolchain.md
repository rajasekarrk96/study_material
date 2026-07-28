---
id: "09_01_01"
title: "C Introduction and Toolchain"
course: "C"
module: 1
module_title: "C Fundamentals"
lesson: 1
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["C", "gcc", "clang", "compilation", "linking", "preprocessor", "make", "CMake", "valgrind"]
prerequisites: []
lab_required: true
---

# C Introduction and Toolchain

## What is C?

C is a **procedural, statically-typed, compiled** systems programming language developed by Dennis Ritchie at Bell Labs (1972). It remains the foundation of operating systems, embedded systems, and high-performance software.

## Why Learn C?

- Deep understanding of memory management
- Foundation for C++, Java, Rust, Go
- Required for embedded/systems programming
- Close-to-hardware control

## Toolchain

```bash
# Install GCC (Linux)
sudo apt install gcc build-essential

# Compile and run
gcc -o hello hello.c
./hello

# With warnings (always use!)
gcc -Wall -Wextra -Werror -o hello hello.c

# Clang (alternative)
clang -o hello hello.c
```

## Compilation Stages

```
hello.c (source)
  ↓ Preprocessor (cpp)   → expands #include, #define
hello.i (preprocessed)
  ↓ Compiler (cc1)       → generates assembly
hello.s (assembly)
  ↓ Assembler (as)       → generates object code
hello.o (object file)
  ↓ Linker (ld)          → links libraries
hello (executable)
```

## Hello World

```c
#include <stdio.h>   /* standard I/O */
#include <stdlib.h>  /* EXIT_SUCCESS, EXIT_FAILURE */

int main(void) {
    printf("Hello, World!\n");
    return EXIT_SUCCESS;   /* 0 */
}
```

## Makefile

```makefile
CC = gcc
CFLAGS = -Wall -Wextra -std=c11

all: myprogram

myprogram: main.o utils.o
	$(CC) $(CFLAGS) -o $@ $^

main.o: main.c main.h
	$(CC) $(CFLAGS) -c $<

clean:
	rm -f *.o myprogram
```

## Lab Exercise
1. Install GCC, compile `hello.c`, run it
2. Break compilation into stages: `-E` (preprocess), `-S` (compile), `-c` (assemble)
3. Write a `Makefile` for a two-file C project
