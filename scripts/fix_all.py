"""
fix_all.py
Comprehensive fix for phase3_python_content.py:
1. Replaces embedded triple-double-quotes inside content blocks with triple-single-quotes
2. Replaces backslash-U and backslash-N sequences that cause unicodeescape errors
"""
import re

FILE = r'scripts\phase3_python_content.py'

with open(FILE, encoding='utf-8') as f:
    src = f.read()

# Step 1: Fix lines with embedded triple-double-quotes (not boundary lines)
lines = src.split('\n')
fixed = []
for i, line in enumerate(lines):
    ln = i + 1
    stripped = line.strip()
    is_open  = stripped.endswith('+ """') or stripped == '+ """'
    is_close = stripped == '""")' or stripped.startswith('""")')
    is_module_doc = ln <= 10
    
    if '"""' in line and not is_open and not is_close and not is_module_doc:
        line = line.replace('"""', "'''")
        print(f"  [QUOTE-FIX] line {ln}")
    fixed.append(line)

src = '\n'.join(fixed)

# Step 2: Fix problematic raw-string examples inside triple-quoted content
# The issue: r"C:\Users\Raja\Documents" inside """ content
# \U is unicode escape, \N is named escape
# Replace backslash sequences in path examples with escaped backslashes

# Specific known problem patterns in the content strings:
replacements = [
    # In strings lesson - raw string example
    (r'r"C:\\Users\\Raja\\Documents"', r'r"C:/Users/Raja/Documents"'),
    # yaml multiline string example
    (
        'config = yaml.safe_load("""\ndatabase:\n  host: localhost\n  port: 5432\n  name: mydb\ndebug: false\n""")',
        "config = yaml.safe_load('''\ndatabase:\n  host: localhost\n  port: 5432\n  name: mydb\ndebug: false\n''')"
    ),
]

for old, new in replacements:
    if old in src:
        src = src.replace(old, new)
        print(f"  [PATH-FIX] replaced: {old[:40]}...")

# Step 3: Verify
import ast
try:
    ast.parse(src)
    print("\nSUCCESS: Source parses correctly!")
    with open(FILE, 'w', encoding='utf-8') as f:
        f.write(src)
    print(f"Written to {FILE}")
except SyntaxError as e:
    print(f"\nSTILL BROKEN at line {e.lineno}: {e.msg}")
    src_lines = src.split('\n')
    for ln in range(max(0, e.lineno-5), min(len(src_lines), e.lineno+3)):
        print(f"  {ln+1}: {src_lines[ln]}")
