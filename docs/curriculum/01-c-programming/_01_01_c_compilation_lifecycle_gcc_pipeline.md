# C Compilation Lifecycle & GCC Pipeline

> **Course**: C Programming | **Module**: Module Introduction & Basics | **Difficulty**: beginner

---

- Overview of the 4 compilation phases
- Preprocessing and Macro expansion
- Code translation to assembly language
- Assembling into relocatable binary object files
- Linking and symbol resolution

---

- **Preprocessing**: The first stage where `#include` statements are replaced by actual header file code, and `#define` macros are expanded.
- **Compiling**: The stage that translates preprocessed code (`.i` files) into target-specific assembly code (`.s` files).
- **Assembling**: The translation of assembly text instructions into raw machine binary instructions (`.o` object files).
- **Linking**: The final phase combining object files and static library files into one executable binary.
- **Compiler Error**: Syntax or structure violations detected during compiling.
- **Linker Error**: Failure to resolve external symbol references or duplicate definitions.

---

### Example A: Macro Expansion Verification
- **Code**:
  ```c
  #define MAX_LIMIT 100
  int main() {
      int limit = MAX_LIMIT;
      return 0;
  }
  ```
- **Input (i/p)**: Compile with `-E` to inspect preprocessor output.
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ gcc -E macro.c | tail -n 4                           │
  │ int main() {                                           │
  │     int limit = 100;                                   │
  │     return 0;                                          │
  │ }                                                      │
  └────────────────────────────────────────────────────────┘
  ```

### Example B: Simulating a Linker Error
- **Code**:
  ```c
  // main.c
  void calculate(); // Declared only, not defined

  int main() {
      calculate();
      return 0;
  }
  ```
- **Input (i/p)**: Compile and link directly.
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ gcc main.c -o app                                    │
  │ /tmp/ccX29a.o: In function `main':                     │
  │ main.c:(.text+0x5): undefined reference to `calculate' │
  │ collect2: error: ld returned 1 exit status             │
  └────────────────────────────────────────────────────────┘
  ```

---

- **Workout 1**: Write a C script using a macro `#define MULTIPLY(a,b) (a*b)`. Compile only to the preprocessed stage (`-E`) and check how it expands in the code.
- **Workout 2**: Compile a single file `hello.c` step-by-step, capturing the `.i`, `.s`, `.o` files on your disk.

---

### Solution to Workout 1:
- **Code**:
  ```c
  #define MULTIPLY(a,b) (a*b)
  int main() {
      int result = MULTIPLY(5, 10);
      return 0;
  }
  ```
- **Output (o/p) after `gcc -E`**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ gcc -E test.c | tail -n 4                            │
  │ int main() {                                           │
  │     int result = (5*10);                               │
  │     return 0;                                          │
  │ }                                                      │
  └────────────────────────────────────────────────────────┘
  ```

### Solution to Workout 2 (Commands to run):
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ gcc -E hello.c -o hello.i                            │
  │ $ gcc -S hello.i -o hello.s                            │
  │ $ gcc -c hello.s -o hello.o                            │
  │ $ gcc hello.o -o hello                                 │
  └────────────────────────────────────────────────────────┘
  ```

---
