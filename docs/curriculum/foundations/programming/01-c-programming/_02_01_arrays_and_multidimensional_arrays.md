# Arrays and Multidimensional Arrays

> **Course**: C Programming | **Module**: Memory and Data Structures | **Difficulty**: beginner

---

```c
#include <stdio.h>
#include <string.h>

/* Declaration and initialisation */
int nums[5] = {10, 20, 30, 40, 50};
int zeros[100] = {0};       /* all elements initialised to 0 */
int auto_size[] = {1,2,3};  /* compiler counts: size = 3 */

int len = sizeof(nums) / sizeof(nums[0]);   /* 5 */

/* Access (0-indexed) */
printf("%d\n", nums[0]);    /* 10 */
printf("%d\n", nums[4]);    /* 50 */

/* Traverse */
for (int i = 0; i < len; i++) {
    printf("%d ", nums[i]);
}
```

---

```c
int matrix[3][4] = {
    {1,  2,  3,  4},
    {5,  6,  7,  8},
    {9, 10, 11, 12}
};

printf("%d\n", matrix[1][2]);  /* 7 */

/* Row-major storage (row by row in memory) */
int rows = 3, cols = 4;
for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
        printf("%3d", matrix[i][j]);
    }
    printf("\n");
}
```

---

```c
/* Arrays decay to pointer when passed to functions */
void print_array(int arr[], int len) {   /* same as int *arr */
    for (int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }
}

/* CANNOT get size from pointer inside function */
/* Must pass length explicitly */
void sort(int *arr, int len) {
    /* bubblesort */
    for (int i = 0; i < len-1; i++)
        for (int j = 0; j < len-1-i; j++)
            if (arr[j] > arr[j+1]) {
                int tmp = arr[j]; arr[j] = arr[j+1]; arr[j+1] = tmp;
            }
}
```

---

1. Find maximum, minimum, and average of a 10-element array
2. Implement matrix multiplication for two 3×3 matrices
3. Search an element in a sorted array using binary search

---
