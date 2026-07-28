---
id: "09_04_03"
title: "C for Embedded Systems"
course: "C"
module: 4
module_title: "Systems Programming"
lesson: 3
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["embedded", "microcontroller", "volatile", "register", "bit-manipulation", "memory-mapped-IO", "interrupt", "watchdog", "MISRA"]
prerequisites: []
lab_required: true
---

# C for Embedded Systems

## Embedded C Concepts

```c
/* volatile — prevents compiler optimization for hardware registers */
volatile uint32_t *GPIO_PORT = (volatile uint32_t *)0x40020000;

/* Reading a hardware register (compiler won't cache this) */
uint32_t status = *GPIO_PORT;

/* Writing to hardware register */
*GPIO_PORT |= (1 << 5);   /* set bit 5 (enable pin) */
*GPIO_PORT &= ~(1 << 5);  /* clear bit 5 */
*GPIO_PORT ^= (1 << 5);   /* toggle bit 5 */
```

## Bit Manipulation

```c
#include <stdint.h>

uint8_t flags = 0;

/* Set bit n */
#define BIT_SET(reg, n)   ((reg) |=  (1U << (n)))
/* Clear bit n */
#define BIT_CLR(reg, n)   ((reg) &= ~(1U << (n)))
/* Toggle bit n */
#define BIT_TOG(reg, n)   ((reg) ^=  (1U << (n)))
/* Test bit n */
#define BIT_TST(reg, n)   (((reg) >> (n)) & 1U)

BIT_SET(flags, 3);    /* flags = 0b00001000 */
BIT_CLR(flags, 3);    /* flags = 0b00000000 */
```

## Fixed-Width Types (stdint.h)

```c
#include <stdint.h>

int8_t   a;   /* exactly 8-bit signed */
uint8_t  b;   /* exactly 8-bit unsigned */
int16_t  c;
uint16_t d;
int32_t  e;
uint32_t f;
int64_t  g;
uint64_t h;

/* Use these instead of int/long in embedded code */
```

## Memory-Mapped I/O Structure

```c
/* GPIO register map */
typedef struct {
    volatile uint32_t MODER;    /* offset 0x00 */
    volatile uint32_t OTYPER;   /* offset 0x04 */
    volatile uint32_t OSPEEDR;  /* offset 0x08 */
    volatile uint32_t PUPDR;    /* offset 0x0C */
    volatile uint32_t IDR;      /* offset 0x10 — input data */
    volatile uint32_t ODR;      /* offset 0x14 — output data */
    volatile uint32_t BSRR;     /* offset 0x18 — bit set/reset */
} GPIO_TypeDef;

#define GPIOA ((GPIO_TypeDef *)0x40020000)
GPIOA->ODR |= (1 << 5);   /* set pin 5 */
```

## Lab Exercise
1. Write a `ring_buffer_t` implementation for UART receive (used in ISR context)
2. Implement a software debounce for a button using a timer counter in C
3. Create a bit-field struct for a register map and verify its size equals the hardware spec
