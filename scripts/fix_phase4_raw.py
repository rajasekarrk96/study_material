import ast

path = r'd:\My Drive\all files\PROJECT FILES\notes\scripts\phase4_content.py'

with open(path, encoding='utf-8') as f:
    src = f.read()

# Replace + ''' with + r''' and ,''' with ,r'''
fixed = src.replace("+ '''", "+ r'''").replace(",'''", ",r'''")

try:
    ast.parse(fixed)
    print("SUCCESS: phase4_content.py parsed successfully with raw strings!")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(fixed)
except SyntaxError as e:
    print(f"Error at line {e.lineno}, col {e.offset}: {e.msg}")
    lines = fixed.split('\n')
    for i in range(max(0, e.lineno-5), min(len(lines), e.lineno+5)):
        print(f"{i+1:4d}: {lines[i]}")
