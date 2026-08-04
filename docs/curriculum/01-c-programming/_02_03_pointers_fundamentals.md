# Pointers Fundamentals

> **Course**: C Programming | **Module**: Memory and Data Structures | **Difficulty**: intermediate

---

A pointer is a variable that stores the **memory address** of another variable.

```c
#include <stdio.h>

int x = 42;
int *p = &x;      /* p holds the address of x */

printf("x     = %d\n", x);     /* 42 */
printf("&x    = %p\n", (void*)&x);   /* address, e.g. 0x7ffee */
printf("p     = %p\n", (void*)p);    /* same address */
printf("*p    = %d\n", *p);    /* 42 (dereference) */

*p = 100;          /* modify x through pointer */
printf("x now = %d\n", x);     /* 100 */
```

---

```c
sizeof(int *)    /* 8 bytes on 64-bit system (all pointers same size) */
sizeof(char *)   /* 8 bytes */
sizeof(double *) /* 8 bytes */

/* void pointer — generic pointer */
void *generic = &x;
int *back = (int *)generic;   /* must cast back before use */
```

---

```c
int *p = NULL;    /* explicitly null — safe to check */
if (p != NULL) {
    *p = 42;      /* safe */
}

/* NEVER do this */
int *bad;         /* uninitialized — undefined behaviour! */
*bad = 42;        /* may crash or corrupt memory */
```

---

```c
const int x = 10;
const int *p = &x;   /* pointer to const int — can't change *p */
int * const q = &y;  /* const pointer — can't change q itself */
const int * const r = &x;  /* both const */

/* Practical: protect function parameters */
void print_string(const char *str) {
    /* str cannot be modified here */
    printf("%s\n", str);
}
```

---

```c
int arr[] = {10, 20, 30, 40, 50};
int *p = arr;        /* points to arr[0] */

p + 1;               /* points to arr[1] (adds sizeof(int)) */
*(p + 2);            /* arr[2] = 30 */

p++;                 /* advance to next element */
printf("%d\n", *p); /* 20 */

/* Difference between pointers */
int *start = arr;
int *end   = &arr[4];
ptrdiff_t count = end - start;   /* 4 */
```

---

1. Write `swap(int *a, int *b)` — verify it actually swaps the caller's variables
2. Traverse an array using pointer arithmetic (no `[]` subscript)
3. Explain the difference between `const int *p` and `int * const p`

---
