---
id: "09_02_04"
title: "Pointers and Arrays"
course: "C"
module: 2
module_title: "Memory and Data Structures"
lesson: 4
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["pointer-array-equivalence", "array-decay", "double-pointer", "pointer-to-pointer", "string-array", "argv"]
prerequisites: []
lab_required: true
---

# Pointers and Arrays

## Array-Pointer Equivalence

```c
int arr[] = {1, 2, 3, 4, 5};
int *p = arr;    /* arr decays to &arr[0] */

arr[2]   == *(arr + 2)   /* true */
arr[i]   == *(arr + i)   /* true */
p[i]     == *(p + i)     /* true */

/* But arr itself is NOT a pointer — it's an array */
sizeof(arr)  /* 20 (5 * 4) */
sizeof(p)    /* 8 (pointer size) */
/* arr = p; */  /* ERROR: arr is not assignable */
```

## Function Pointers

```c
/* Pointer to function returning int, taking two ints */
int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }

int (*op)(int, int) = add;
printf("%d\n", op(3, 4));   /* 7 */
op = sub;
printf("%d\n", op(3, 4));   /* -1 */

/* Array of function pointers (dispatch table) */
int (*operations[])(int,int) = {add, sub, mul, div};
printf("%d\n", operations[2](3, 4));   /* 12 */

/* Callback pattern */
void apply(int *arr, int len, int (*transform)(int)) {
    for (int i = 0; i < len; i++)
        arr[i] = transform(arr[i]);
}
int square(int x) { return x * x; }
apply(arr, 5, square);
```

## Pointer to Pointer (double pointer)

```c
int x = 42;
int *p = &x;
int **pp = &p;

**pp         /* 42 */
*pp          /* p (address of x) */

/* Common use: modify pointer in function */
void allocate(int **ptr, int size) {
    *ptr = malloc(size * sizeof(int));
}

int *data = NULL;
allocate(&data, 100);
```

## Array of Strings

```c
/* Array of string literals */
const char *days[] = {"Mon","Tue","Wed","Thu","Fri","Sat","Sun"};
printf("%s\n", days[0]);   /* Mon */

/* main argc/argv */
int main(int argc, char *argv[]) {
    for (int i = 0; i < argc; i++) {
        printf("arg[%d] = %s\n", i, argv[i]);
    }
}
```

## Lab Exercise
1. Implement `qsort` using a function pointer comparator for an array of structs
2. Write `strdup` equivalent that allocates and returns a copy of a string
3. Build a command dispatch table mapping command strings to functions
