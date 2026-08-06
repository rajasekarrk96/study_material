---
id: "09_01_03"
title: "Control Flow"
course: "C"
module: 1
module_title: "C Fundamentals"
lesson: 3
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["if", "else", "switch", "for", "while", "do-while", "break", "continue", "goto"]
prerequisites: []
lab_required: true
---

# Control Flow

## Conditional Statements

```c
int score = 82;

if (score >= 90) {
    printf("A\n");
} else if (score >= 75) {
    printf("B\n");
} else if (score >= 60) {
    printf("C\n");
} else {
    printf("F\n");
}

/* Ternary */
const char *result = (score >= 60) ? "Pass" : "Fail";

/* Switch */
char grade = 'B';
switch (grade) {
    case 'A': printf("Excellent\n"); break;
    case 'B': printf("Good\n");      break;
    case 'C': printf("Average\n");   break;
    default:  printf("Below\n");     break;
}
```

## Loops

```c
/* for loop */
for (int i = 0; i < 10; i++) {
    printf("%d ", i);
}

/* while loop */
int n = 1;
while (n <= 1000) {
    n *= 2;
}

/* do-while (runs at least once) */
int input;
do {
    printf("Enter positive number: ");
    scanf("%d", &input);
} while (input <= 0);

/* Nested loops — multiplication table */
for (int i = 1; i <= 9; i++) {
    for (int j = 1; j <= 9; j++) {
        printf("%3d", i * j);
    }
    printf("\n");
}
```

## Break, Continue, Goto

```c
/* break — exit current loop */
for (int i = 0; i < 100; i++) {
    if (i * i > 1000) break;
    printf("%d\n", i);
}

/* continue — skip to next iteration */
for (int i = 0; i < 20; i++) {
    if (i % 2 == 0) continue;
    printf("%d ", i);  /* odd numbers only */
}

/* goto — use sparingly (error cleanup is a valid use) */
int *p = malloc(100 * sizeof(int));
if (!p) goto cleanup;

int *q = malloc(200 * sizeof(int));
if (!q) goto cleanup;

/* ... use p and q ... */

cleanup:
    free(p);
    free(q);
```

## Lab Exercise
1. Print all prime numbers from 2 to 100 using nested loops and `break`
2. Implement a simple calculator with `switch` for +, -, *, /
3. Use `goto` for multi-resource cleanup in an error path
