---
id: "09_03_01"
title: "Dynamic Memory Allocation"
course: "C"
module: 3
module_title: "Advanced C"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["malloc", "calloc", "realloc", "free", "heap", "valgrind", "memory-leak", "dangling-pointer", "double-free"]
prerequisites: []
lab_required: true
---

# Dynamic Memory Allocation

## Heap vs Stack

```
Stack: automatic, fast, limited size (~1-8 MB)
       local variables, function frames, freed on return

Heap:  manual, slower, large (limited by RAM)
       malloc/calloc/realloc, must free() manually
```

## Allocation Functions

```c
#include <stdlib.h>

/* malloc — allocate n bytes (uninitialized) */
int *arr = malloc(10 * sizeof(int));
if (arr == NULL) {
    fprintf(stderr, "malloc failed\n");
    exit(EXIT_FAILURE);
}

/* calloc — allocate n*size bytes (zero-initialized) */
int *zeroed = calloc(10, sizeof(int));

/* realloc — resize existing allocation */
arr = realloc(arr, 20 * sizeof(int));
if (arr == NULL) { /* original freed on failure! store backup */ }

/* free — release memory */
free(arr);
arr = NULL;   /* prevent dangling pointer */
```

## Common Mistakes

```c
/* Memory leak — allocated but never freed */
for (int i = 0; i < 1000; i++) {
    char *s = malloc(100);
    strcpy(s, "leaked string");
    /* forgot free(s)! */
}

/* Double free — undefined behaviour */
free(p);
free(p);    /* CRASH */

/* Dangling pointer — accessing freed memory */
free(p);
printf("%d\n", *p);  /* undefined behaviour */

/* Buffer overflow — writing past allocation */
int *arr = malloc(5 * sizeof(int));
arr[5] = 99;   /* off by one — undefined behaviour */
```

## Valgrind (Memory Debugger)

```bash
gcc -g -o program program.c
valgrind --leak-check=full --track-origins=yes ./program
```

## Dynamic Array Implementation

```c
typedef struct {
    int *data;
    int size;
    int capacity;
} DynArray;

DynArray *dynarray_create(int initial) {
    DynArray *a = malloc(sizeof(DynArray));
    a->data = malloc(initial * sizeof(int));
    a->size = 0;
    a->capacity = initial;
    return a;
}

void dynarray_push(DynArray *a, int val) {
    if (a->size == a->capacity) {
        a->capacity *= 2;
        a->data = realloc(a->data, a->capacity * sizeof(int));
    }
    a->data[a->size++] = val;
}

void dynarray_free(DynArray *a) {
    free(a->data);
    free(a);
}
```

## Lab Exercise
1. Implement a dynamic string builder with `realloc` (grow by 2x when full)
2. Find all memory leaks in a provided buggy program using Valgrind
3. Build a `stack_t` using dynamic allocation with push/pop/peek
