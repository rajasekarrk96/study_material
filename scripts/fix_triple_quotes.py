"""
fix_triple_quotes.py
Finds and replaces embedded triple-double-quotes inside outer triple-double-quoted
strings in phase3_python_content.py, so it parses correctly.
"""

SRC_FILE = r'scripts\phase3_python_content.py'

with open(SRC_FILE, encoding='utf-8') as f:
    src = f.read()

# We need to find all the write() + fm() + """ ... """ blocks.
# Inside those content blocks, any """ that is PART OF LESSON TEXT
# (i.e., used as docstring examples in code blocks) needs escaping.
#
# Strategy: walk through character by character tracking whether we are
# inside a top-level triple-quoted string or not. When inside, replace
# any encountered """ with ''' (triple single quote) so it's valid Python.

result = []
i = 0
src_len = len(src)
in_triple = False
block_count = 0

while i < src_len:
    if src[i:i+3] == '"""':
        if not in_triple:
            # Opening delimiter of a content block
            in_triple = True
            block_count += 1
            result.append('"""')
            i += 3
        else:
            # Could be closing OR an embedded triple-quote
            # If this """ is followed immediately by ) or + or \n and we
            # are actually at a closing position (look ahead for typical patterns)
            # Closing delimiters in this file are: """)\n  or """\n  or """.strip
            # Embedded ones appear inside code blocks and are followed by things like:
            # content (docstring text) or another """ closing
            
            # Simple heuristic: check if this looks like a closing delimiter
            # A closing """ is followed by: ), \n, .strip, .format, whitespace+)
            after = src[i+3:i+10].lstrip()
            is_closing = (
                src[i+3:i+4] in (')', '\n', '+', ' ', '\r') or
                after.startswith(')') or
                after.startswith('+') or
                src[i+3:i+5] == ')\n' or
                src[i+3:i+6] == ').st'
            )
            
            # Also check if this is truly at end of a write() block
            # by seeing if the line context says this is a closing
            # Look backwards for the write( call context
            
            if is_closing:
                # This is the closing delimiter
                in_triple = False
                result.append('"""')
                i += 3
            else:
                # Embedded triple-quote inside content — replace with '''
                result.append("'''")
                i += 3
    else:
        result.append(src[i])
        i += 1

new_src = ''.join(result)

# Verify it parses
import ast
try:
    ast.parse(new_src)
    print("SUCCESS: New source parses correctly!")
    with open(SRC_FILE, 'w', encoding='utf-8') as f:
        f.write(new_src)
    print(f"Written back to {SRC_FILE}")
    print(f"Processed {block_count} triple-quoted blocks")
except SyntaxError as e:
    print(f"STILL BROKEN at line {e.lineno}: {e.msg}")
    # Show context
    lines = new_src.split('\n')
    for ln in range(max(0, e.lineno-5), min(len(lines), e.lineno+3)):
        print(f"  {ln+1}: {lines[ln]}")
