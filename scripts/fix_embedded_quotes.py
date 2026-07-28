"""
fix_embedded_quotes.py
Replaces triple-double-quotes INSIDE lesson content strings with triple-single-quotes.
Targets specific known problem locations identified by line number.
"""
import sys

FILE = r'scripts\phase3_python_content.py'

with open(FILE, encoding='utf-8') as f:
    lines = f.readlines()

# Problem locations (0-indexed line numbers where embedded """ appear inside content):
# Line 554 (0-indexed 553): """
# Line 570 (0-indexed 569): """
# Plus any others from the 90 positions vs expected 84 analysis
# Expected blocks: 1 module docstring + 39 write blocks = 40 blocks = 80 triple-quotes
# Actual: 90 = 5 extra embedded triple-quotes

# Find all lines that have triple-double-quotes and mark them
# Then determine which ones are "inside" a write() content block

# State machine to identify which """ are embedded
in_write_block = False
write_block_depth = 0
problematic_lines = []

# These are the line numbers (1-indexed) we found are problematic from the analysis:
# pos[13] = line 554 (open of embedded docstring)
# pos[14] = line 570 (close of embedded docstring)
# Also check pos[31], pos[32], pos[33], pos[34] around line 1398-1433
# And pos[37], pos[38] around line 1515

# From the analysis:
# pos[12] opens at 504, should close at 617 (pos[15])
# But pos[13] (line 554) and pos[14] (line 570) are INSIDE - they are the embedded ones
# Similarly pos[31] line 1398 and pos[32] line 1400 are embedded
# And pos[33] line 1423 and pos[34] line 1426 are embedded  
# And pos[37] line 1515 and pos[38] line 1515 are embedded

# Strategy: for each line, check if it contains """ and is NOT a write/fm open or close
# A line that is a "content boundary" looks like:
#   ) + """           <- opening of content
#   """)              <- closing of content  
#   """               <- could be embedded (inside code block)

fixed_lines = []
for i, line in enumerate(lines):
    line_num = i + 1  # 1-indexed
    stripped = line.strip()
    
    # Check if this is a content boundary (open or close)
    is_open_boundary = stripped.endswith('+ """') or stripped == '+ """'
    is_close_boundary = stripped == '""")' or stripped.startswith('""")')
    
    # If it has """ but is NOT a boundary, it's an embedded one
    if '"""' in line and not is_open_boundary and not is_close_boundary:
        # Check it's not the module docstring (lines 1-4)
        if line_num > 10:
            # Replace embedded """ with '''
            new_line = line.replace('"""', "'''")
            fixed_lines.append(new_line)
            print(f"  [FIX] line {line_num}: {stripped[:60]}")
            continue
    
    fixed_lines.append(line)

new_src = ''.join(fixed_lines)

# Verify it parses
import ast
try:
    ast.parse(new_src)
    print("\nSUCCESS: Fixed source parses correctly!")
    with open(FILE, 'w', encoding='utf-8') as f:
        f.write(new_src)
    print(f"Written back to {FILE}")
except SyntaxError as e:
    print(f"\nSTILL BROKEN at line {e.lineno}: {e.msg}")
    src_lines = new_src.split('\n')
    for ln in range(max(0, e.lineno-5), min(len(src_lines), e.lineno+3)):
        print(f"  {ln+1}: {src_lines[ln]}")
