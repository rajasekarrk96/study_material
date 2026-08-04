# Debugging and Best Practices

> **Course**: C Programming | **Module**: Systems Programming | **Difficulty**: intermediate

---

```bash
# Compile with debug info
gcc -g -O0 -o program program.c

# Start GDB
gdb ./program

# GDB commands
(gdb) run                # start program
(gdb) break main         # breakpoint at main
(gdb) break program.c:42 # breakpoint at line 42
(gdb) next               # next line (step over)
(gdb) step               # step into function
(gdb) continue           # continue to next breakpoint
(gdb) print x            # print variable x
(gdb) print *ptr         # dereference pointer
(gdb) info locals        # all local variables
(gdb) backtrace          # call stack
(gdb) quit
```

---

```bash
gcc -fsanitize=address -g -o program program.c
./program
# Reports: buffer overflow, heap use-after-free, stack overflow, leaks
```

---

```bash
# clang static analyzer
scan-build gcc -o program program.c

# cppcheck
cppcheck --enable=all program.c

# splint (MISRA-style)
splint program.c
```

---

```c
#include <assert.h>

/* assert — checks during DEBUG, removed in release (-DNDEBUG) */
void array_set(int *arr, int idx, int val, int len) {
    assert(arr != NULL);
    assert(idx >= 0 && idx < len);
    arr[idx] = val;
}

/* Check all return values */
FILE *fp = fopen("file.txt", "r");
if (fp == NULL) {
    fprintf(stderr, "Cannot open file: %s\n", strerror(errno));
    return -1;
}

/* Always null-check malloc */
int *buf = malloc(n * sizeof(int));
if (!buf) { perror("malloc"); exit(EXIT_FAILURE); }

/* Avoid magic numbers */
#define BUFFER_SIZE 4096
char buf[BUFFER_SIZE];
```

---

| Bug | Prevention |
|---|---|
| Memory leak | Free every malloc, use valgrind |
| Buffer overflow | Use `snprintf`, `strncpy`, bounds check |
| Null dereference | Check before dereferencing |
| Uninitialized variable | Initialize all variables |
| Integer overflow | Use `UINT_MAX` checks |
| Off-by-one | Draw diagrams, test edge cases |
| Use after free | Set pointer to NULL after free |

---

1. Find and fix 5 bugs in a provided buggy C program using GDB
2. Run the same program with ASAN — compare the errors caught
3. Write a `safe_malloc` wrapper that logs allocation size and always zero-inits

---
