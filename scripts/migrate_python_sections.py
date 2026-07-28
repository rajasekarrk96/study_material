"""
migrate_python_sections.py  
Fixed version: matches exact headings from 01_python.md
"""
import os, re

BASE   = r'd:\My Drive\all files\PROJECT FILES\notes\docs\curriculum\_02_python'
OLD_PY = r'd:\My Drive\all files\PROJECT FILES\notes\docs\old and reference and future studies\_01_data_analyst_&_science\study material for data analyst and data science\01_python.md'

PYTHON_TOPIC_MAP = {
    "00. Environment Setup":                  "_02_01_environment_setup_and_tooling.md",
    "01. Basics, Data Types, Operators, ASCII, And Strings": "_02_02_built_in_primitive_data_types.md",
    "02. Control Flow":                        "_02_03_conditional_execution.md",
    "03. Data Structures":                     "_02_04_lists_and_sequence_operations.md",
    "04. Lists And Tuples":                    "_02_04_tuples_and_immutable_sequences.md",
    "05. Sets And Dictionaries":               "_02_04_sets_and_frozensets.md",
    "06. Functions And Modules":               "_02_05_functions_and_arguments.md",
    "07. Functional Programming":              "_02_05_functional_programming.md",
    "08. Classes And Objects":                 "_02_07_classes_and_instance_mechanics.md",
    "09. Advanced OOP":                        "_02_07_inheritance_and_polymorphism.md",
    "10. Exceptions And File Handling":        "_02_08_exception_handling.md",
    "12. Advanced Concepts":                   "_02_06_closures_and_decorators.md",
    "13. Iterators And Generators":            "_02_06_generators_and_iterators.md",
    "14. Decorators":                          "_02_07_magic_dunder_methods.md",
    "16. New Python Features":                 "_02_01_cpython_architecture_and_execution.md",
    "17. Regular Expressions":                 "_02_10_regular_expressions.md",
    "19. Concurrency And Asyncio":             "_02_12_asyncio_and_async_await.md",
    "20. Testing And Logging":                 "_02_14_testing_with_pytest.md",
    "22. MySQL Database Connectivity":         "_02_13_hardware_interfacing_python.md",
}

old_py_content = open(OLD_PY, encoding="utf-8").read()
appended = 0
skipped  = 0

for section_key, target_fname in PYTHON_TOPIC_MAP.items():
    target_path = os.path.join(BASE, target_fname)
    if not os.path.exists(target_path):
        print(f"[SKIP] Target not found: {target_fname}")
        skipped += 1
        continue

    content = open(target_path, encoding="utf-8").read()
    if f"Section '{section_key}'" in content or f"## {section_key}" in content:
        print(f"[DUP]  Already has: {section_key}")
        skipped += 1
        continue

    # Extract section
    pattern = re.compile(
        r'(?:^|\n)(## ' + re.escape(section_key) + r'\n.+?)(?=\n## |\Z)',
        re.DOTALL
    )
    match = pattern.search(old_py_content)
    if match:
        section_text = match.group(1).strip()
        block = f"""

---

## Migrated Notes — Section '{section_key}'

> **Source**: `01_python.md` from data analyst notes archive (topic reference list)
> Jupyter notebooks: `docs/old and reference and future studies/_01_data_analyst_&_science/`

{section_text}
"""
        with open(target_path, "a", encoding="utf-8") as f:
            f.write(block)
        print(f"[APPEND] '{section_key}' -> {target_fname}")
        appended += 1
    else:
        print(f"[MISS]   Could not extract: '{section_key}'")

print(f"\nDONE — Appended: {appended}  Skipped: {skipped}")
