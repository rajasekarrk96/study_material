# C Introduction and Toolchain

> **Course**: C Programming | **Module**: C Fundamentals | **Difficulty**: beginner

---

C is a **procedural, statically-typed, compiled** systems programming language developed by Dennis Ritchie at Bell Labs (1972). It remains the foundation of operating systems, embedded systems, and high-performance software.

---

- Deep understanding of memory management
- Foundation for C++, Java, Rust, Go
- Required for embedded/systems programming
- Close-to-hardware control

---

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

---

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

---

```c
#include <stdio.h>   /* standard I/O */
#include <stdlib.h>  /* EXIT_SUCCESS, EXIT_FAILURE */

int main(void) {
    printf("Hello, World!\n");
    return EXIT_SUCCESS;   /* 0 */
}
```

---

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

---

1. Install GCC, compile `hello.c`, run it
2. Break compilation into stages: `-E` (preprocess), `-S` (compile), `-c` (assemble)
3. Write a `Makefile` for a two-file C project

---
