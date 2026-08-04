# Data Types and Operators

> **Course**: C Programming | **Module**: C Fundamentals | **Difficulty**: beginner

---

```c
#include <stdio.h>
#include <limits.h>
#include <float.h>

/* Integer types */
char   c = 'A';         /* 1 byte  (-128 to 127) */
short  s = 30000;       /* 2 bytes */
int    i = 2147483647;  /* 4 bytes (typical) */
long   l = 9223372036854775807L;  /* 8 bytes on 64-bit */
long long ll = -9223372036854775807LL - 1;

/* Unsigned variants */
unsigned int  ui = 4294967295U;
unsigned char uc = 255;

/* Floating point */
float  f = 3.14f;
double d = 3.14159265358979;
long double ld = 3.14159265358979323846L;

/* sizeof operator */
printf("int: %zu bytes\n", sizeof(int));    /* zu = size_t */
printf("double: %zu bytes\n", sizeof(double));
```

---

```c
printf("%d\n",  42);         /* int */
printf("%ld\n", 123456789L); /* long */
printf("%u\n",  42u);        /* unsigned */
printf("%f\n",  3.14f);      /* float/double (default 6 decimal) */
printf("%.2f\n",3.14159);    /* 2 decimal places */
printf("%e\n",  1.23e10);    /* scientific */
printf("%c\n",  'A');        /* char */
printf("%s\n",  "hello");    /* string */
printf("%p\n",  &x);         /* pointer address */
printf("%x\n",  255);        /* hex: ff */
printf("%-10s|\n","left");   /* left-align 10 chars */
```

---

```c
int age;
double salary;
char name[50];

printf("Enter age: ");
scanf("%d", &age);           /* & for address */

printf("Enter name: ");
scanf("%49s", name);         /* limit string length */

printf("Enter salary: ");
scanf("%lf", &salary);       /* %lf for double */
```

---

```c
/* Arithmetic */
5 / 2     /* 2 (integer division) */
5 % 2     /* 1 */
5.0 / 2   /* 2.5 */

/* Bitwise */
0xFF & 0x0F   /* 0x0F (AND) */
0xF0 | 0x0F   /* 0xFF (OR) */
0xFF ^ 0xF0   /* 0x0F (XOR) */
~0x00         /* 0xFF...FF (NOT) */
1 << 4        /* 16  (left shift) */
256 >> 2      /* 64  (right shift) */

/* Increment / decrement */
i++;   /* post-increment: use then increment */
++i;   /* pre-increment: increment then use */

/* Cast */
int x = (int)3.99;   /* 3 — truncates */
double y = (double)5 / 2;   /* 2.5 */
```

---

1. Print size of all primitive types on your system using `sizeof`
2. Read two integers, print their sum, difference, product, quotient, remainder
3. Demonstrate integer overflow: what happens when you add 1 to `INT_MAX`?

---
