import ast

path = r'd:\My Drive\all files\PROJECT FILES\notes\scripts\phase4_content.py'

with open(path, encoding='utf-8') as f:
    content = f.read()

# Replace Groovy sh ''' in Jenkins snippet
content = content.replace("sh '''", 'sh """').replace("                '''\n            }", '                """\n            }')

try:
    ast.parse(content)
    print("SUCCESS! phase4_content.py is 100% valid Python AST!")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
except SyntaxError as e:
    print(f"Error at line {e.lineno}, col {e.offset}: {e.msg}")
    lines = content.split('\n')
    for i in range(max(0, e.lineno-5), min(len(lines), e.lineno+5)):
        print(f"{i+1:4d}: {lines[i]}")
