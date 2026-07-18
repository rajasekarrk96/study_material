import nbformat as nbf

# ==========================================================
# FILE CONFIG
# ==========================================================
TOPIC_INDEX = "01"
TOPIC_NAME = "Python_Patterns"

filename = f"{TOPIC_INDEX}_{TOPIC_NAME}.ipynb"

nb = nbf.v4.new_notebook()
cells = []

# ==========================================================
# CELL 1: TITLE
# ==========================================================
cells.append(nbf.v4.new_markdown_cell("""
# 🧠 Python Pattern Programming (Basics → Advanced)

## What you will learn
- How to think in pattern problems
- Loop structuring (row vs column logic)
- Star, number, and character patterns
- Pyramid, diamond, and advanced structures
- Real-world logical thinking for interviews
"""))

# ==========================================================
# CELL 2: INTRODUCTION
# ==========================================================
cells.append(nbf.v4.new_markdown_cell("""
## 📌 Introduction

### What is Pattern Programming?
Pattern programming is the process of printing structured outputs using loops and conditions.

### Why it is used?
- Builds logical thinking
- Strengthens nested loop understanding
- Common in coding interviews

### Real-world relevance
- Matrix problems
- Game grid design
- Data visualization logic
"""))

# ==========================================================
# CELL 3: BASIC SYNTAX
# ==========================================================
cells.append(nbf.v4.new_markdown_cell("""
## 🔹 Basic Syntax Explanation

- Outer loop → Controls rows
- Inner loop → Controls columns
- print(..., end="") → Avoid newline
- print() → Move to next row
"""))

# ==========================================================
# CELL 4: BASIC EXAMPLE
# ==========================================================
cells.append(nbf.v4.new_code_cell("""
# Basic Square Pattern

n = 4  # number of rows and columns

for i in range(n):  # loop for rows
    for j in range(n):  # loop for columns
        print("*", end=" ")  # print star without newline
    print()  # move to next line after each row
"""))

# ==========================================================
# CONCEPT: RIGHT TRIANGLE
# ==========================================================
cells.append(nbf.v4.new_markdown_cell("""
## ▶ Right Triangle Pattern

Logic:
- Number of stars increases with row number
- Row i → i+1 stars
"""))

cells.append(nbf.v4.new_code_cell("""
n = 5  # total rows

for i in range(n):  # iterate rows
    for j in range(i+1):  # columns depend on row index
        print("*", end=" ")  # print star
    print()  # move to next row
"""))

# ==========================================================
# CONCEPT: INVERTED TRIANGLE
# ==========================================================
cells.append(nbf.v4.new_markdown_cell("""
## ▶ Inverted Triangle Pattern

Logic:
- Number of stars decreases with each row
- Row i → n-i stars
"""))

cells.append(nbf.v4.new_code_cell("""
n = 5

for i in range(n):  # loop rows
    for j in range(n-i):  # decreasing stars
        print("*", end=" ")
    print()
"""))

# ==========================================================
# CONCEPT: PYRAMID
# ==========================================================
cells.append(nbf.v4.new_markdown_cell("""
## ▶ Pyramid Pattern

Logic:
- Spaces decrease
- Stars increase symmetrically
- stars = 2*i + 1
"""))

cells.append(nbf.v4.new_code_cell("""
n = 5

for i in range(n):
    spaces = " " * (n-i-1)  # leading spaces
    stars = "*" * (2*i+1)   # odd number of stars
    print(spaces + stars)   # combine and print
"""))

# ==========================================================
# CONCEPT: NUMBER TRIANGLE
# ==========================================================
cells.append(nbf.v4.new_markdown_cell("""
## ▶ Number Triangle

Logic:
- Print numbers from 1 to i
"""))

cells.append(nbf.v4.new_code_cell("""
n = 5

for i in range(n):
    for j in range(1, i+2):  # numbers from 1 to row index
        print(j, end=" ")
    print()
"""))

# ==========================================================
# CONCEPT: CONTINUOUS NUMBERS
# ==========================================================
cells.append(nbf.v4.new_markdown_cell("""
## ▶ Continuous Number Pattern

Logic:
- Maintain a global counter
- Increment continuously
"""))

cells.append(nbf.v4.new_code_cell("""
n = 5
num = 1  # starting number

for i in range(n):
    for j in range(i+1):
        print(num, end=" ")
        num += 1  # increment after each print
    print()
"""))

# ==========================================================
# CONCEPT: HOLLOW SQUARE
# ==========================================================
cells.append(nbf.v4.new_markdown_cell("""
## ▶ Hollow Square

Logic:
- Print star only at borders
- Inside remains empty
"""))

cells.append(nbf.v4.new_code_cell("""
n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")  # border
        else:
            print(" ", end=" ")  # inside
    print()
"""))

# ==========================================================
# CONCEPT: DIAMOND
# ==========================================================
cells.append(nbf.v4.new_markdown_cell("""
## ▶ Diamond Pattern

Logic:
- Combine pyramid + inverted pyramid
"""))

cells.append(nbf.v4.new_code_cell("""
n = 5

# Upper half
for i in range(n):
    print(" "*(n-i-1) + "*"*(2*i+1))

# Lower half
for i in range(n-1):
    print(" "*(i+1) + "*"*(2*(n-i-1)-1))
"""))

# ==========================================================
# EDGE CASES
# ==========================================================
cells.append(nbf.v4.new_markdown_cell("""
## ⚠ Edge Cases

- n = 0 → No output
- n = 1 → Single element
- Large n → performance considerations
"""))

# ==========================================================
# COMMON MISTAKES
# ==========================================================
cells.append(nbf.v4.new_markdown_cell("""
## ❌ Common Mistakes

- Wrong loop ranges
- Misplacing print()
- Forgetting end=""
- Incorrect space calculation
"""))

# ==========================================================
# ADVANCED USAGE
# ==========================================================
cells.append(nbf.v4.new_markdown_cell("""
## 🚀 Advanced Usage

- Pattern transformations (stars → numbers)
- Symmetry-based logic
- Nested condition optimization
"""))

# ==========================================================
# REAL WORLD EXAMPLE
# ==========================================================
cells.append(nbf.v4.new_markdown_cell("""
## 🌍 Real-world Example

- Game boards (grid rendering)
- UI layout simulation
- Matrix-based problems
"""))

cells.append(nbf.v4.new_code_cell("""
# Example: Grid rendering

rows, cols = 3, 3

for i in range(rows):
    for j in range(cols):
        print(f"[{i},{j}]", end=" ")
    print()
"""))

# ==========================================================
# FINALIZE
# ==========================================================
nb['cells'] = cells

with open(filename, "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print(f"Notebook '{filename}' generated successfully!")
