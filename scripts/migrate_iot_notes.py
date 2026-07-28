"""
migrate_iot_notes.py
Migrates existing backend/concept notes into proper curriculum files
and adds migration references to all Python/MySQL stubs.
"""
import os, re, shutil

BASE   = r'd:\My Drive\all files\PROJECT FILES\notes\docs\curriculum'
OLD_BC = r'd:\My Drive\all files\PROJECT FILES\notes\docs\old and reference and future studies\_05_backend_concepts\API Design and Architecture - Backend Engineering'

# ─────────────────────────────────────────────────────────────────────────────
# STEP 1: Migrate _05_backend_concepts notes into FastAPI curriculum
# These are full content notes — inject them directly into matching FastAPI files
# ─────────────────────────────────────────────────────────────────────────────

BACKEND_MAP = {
    # old note file -> target curriculum file
    "_01_01_API_Design_and_Architecture_Notes.md":       ("_05_fastapi", "_05_32_openapi_standard_and_interactive_ui.md"),
    "_02_01_REST_API_Design_and_Constraints_Notes.md":   ("_05_fastapi", "_05_01_asgi_architecture_uvicorn_and_fastapi_basics.md"),
    "_03_01_API_Architecture_and_Patterns_Notes.md":     ("_05_fastapi", "_05_11_apirouter_architecture_and_prefixes.md"),
    "_05_01_OpenAPI_and_Documentation_Notes.md":         ("_05_fastapi", "_05_32_openapi_standard_and_interactive_ui.md"),
    "_06_01_The_HTTP_Protocol_Notes.md":                 ("_05_fastapi", "_05_02_fastapi_app_instantiation_routing_and_openapi.md"),
    "_07_01_API_Status_Codes_Notes.md":                  ("_05_fastapi", "_05_26_response_models_and_status_codes.md"),
    "_08_01_FastAPI_and_CRUD_Notes.md":                  ("_05_fastapi", "_05_03_path_and_query_parameters.md"),
    "_09_01_Request_Lifecycle_and_Middleware_Notes.md":  ("_05_fastapi", "_05_13_asynchronous_middleware_and_cors.md"),
    "_10_01_Pagination_Notes.md":                        ("_05_fastapi", "_05_22_query_parameters_and_validation.md"),
    "_11_01_Authentication_and_JWT_Notes.md":            ("_05_fastapi", "_05_10_jwt_authentication_and_current_user.md"),
    "_12_01_OAuth2_and_Sessions_Notes.md":               ("_05_fastapi", "_05_09_oauth2_password_bearer_and_hashing.md"),
    "_13_01_Validation_and_Exceptions_Notes.md":         ("_05_fastapi", "_05_30_custom_exception_handling.md"),
    "_14_01_Database_Relationships_and_Normalization_Notes.md": ("_05_fastapi", "_05_07_sqlalchemy_20_async_engine_and_asyncpg.md"),
    "_15_01_Database_Indexes_and_Transactions_Notes.md": ("_05_fastapi", "_05_08_async_crud_operations_and_asyncsession.md"),
    "_16_01_Performance_Redis_and_Rate_Limiting_Notes.md": ("_05_fastapi", "_05_14_request_timing_headers_and_performance_logging.md"),
    "_17_01_Testing_Pytest_and_Mocking_Notes.md":        ("_05_fastapi", "_05_19_async_testing_with_pytest_and_httpx.md"),
    "_18_01_Deployment_and_Docker_Notes.md":             ("_05_fastapi", "_05_20_production_deployment_gunicorn_uvicorn_docker.md"),
}

migrated = 0
appended = 0
skipped  = 0

print("=" * 60)
print("STEP 1: Migrating backend concept notes into FastAPI files")
print("=" * 60)

for old_fname, (folder, target_fname) in BACKEND_MAP.items():
    old_path    = os.path.join(OLD_BC, old_fname)
    target_path = os.path.join(BASE, folder, target_fname)

    if not os.path.exists(old_path):
        print(f"[MISS]   Source missing: {old_fname}")
        skipped += 1
        continue

    old_content = open(old_path, encoding="utf-8").read().strip()

    if not os.path.exists(target_path):
        print(f"[SKIP]   Target missing: {target_fname}")
        skipped += 1
        continue

    target_content = open(target_path, encoding="utf-8").read()

    # Only append if not already migrated
    if "## Migrated Notes" in target_content or old_content[:50] in target_content:
        print(f"[DUP]    Already migrated: {target_fname}")
        skipped += 1
        continue

    # Append old notes as a new section
    appended_block = f"""

---

## Migrated Notes

> **Source**: `{old_fname}` (from backend concepts archive)
> This content was migrated from existing study notes. Review and merge with topics above.

{old_content}
"""
    with open(target_path, "a", encoding="utf-8") as f:
        f.write(appended_block)
    print(f"[APPEND] {old_fname} -> {target_fname}")
    appended += 1

# ─────────────────────────────────────────────────────────────────────────────
# STEP 2: Update Python stubs with topic references from old 01_python.md
# The old note is a topic-list roadmap — add it as a reference section
# ─────────────────────────────────────────────────────────────────────────────
print()
print("=" * 60)
print("STEP 2: Adding Python topic references from old notes")
print("=" * 60)

OLD_PY = r'd:\My Drive\all files\PROJECT FILES\notes\docs\old and reference and future studies\_01_data_analyst_&_science\study material for data analyst and data science\01_python.md'

# Mapping of old Python sections to new curriculum files
PYTHON_TOPIC_MAP = {
    "01. Basics, Data Types": "_02_02_built_in_primitive_data_types.md",
    "03. Control Flow":       "_02_03_conditional_execution.md",
    "04. Data Structures":    "_02_04_lists_and_sequence_operations.md",
    "05. Lists And Tuples":   "_02_04_tuples_and_immutable_sequences.md",
    "06. Sets And Dictionaries": "_02_04_sets_and_frozensets.md",
    "07. Functions And Modules": "_02_05_functions_and_arguments.md",
    "08. Functional Programming": "_02_05_functional_programming.md",
    "09. Classes And Objects": "_02_07_classes_and_instance_mechanics.md",
    "10. Advanced OOP":       "_02_07_inheritance_and_polymorphism.md",
    "11. Exceptions":         "_02_08_exception_handling.md",
    "13. Advanced Concepts":  "_02_06_closures_and_decorators.md",
    "14. Iterators And Generators": "_02_06_generators_and_iterators.md",
    "15. Decorators":         "_02_06_closures_and_decorators.md",
    "17. New Python Features": "_02_01_cpython_architecture_and_execution.md",
    "18. Regular Expressions": "_02_10_regular_expressions.md",
    "19. Concurrency And Asyncio": "_02_12_asyncio_and_async_await.md",
    "20. Testing And Logging": "_02_14_testing_with_pytest.md",
}

if os.path.exists(OLD_PY):
    old_py_content = open(OLD_PY, encoding="utf-8").read()
    py_folder = os.path.join(BASE, "_02_python")

    for section_key, target_fname in PYTHON_TOPIC_MAP.items():
        target_path = os.path.join(py_folder, target_fname)
        if not os.path.exists(target_path):
            print(f"[SKIP] Target not found: {target_fname}")
            skipped += 1
            continue
        content = open(target_path, encoding="utf-8").read()
        if "## Migrated Notes" in content:
            print(f"[DUP]  Already has reference: {target_fname}")
            skipped += 1
            continue
        # Extract the section from old notes
        pattern = re.compile(
            r'(## ' + re.escape(section_key) + r'.+?)(?=^## |\Z)',
            re.DOTALL | re.MULTILINE
        )
        match = pattern.search(old_py_content)
        if match:
            section_text = match.group(1).strip()
            block = f"""

---

## Migrated Notes

> **Source**: `01_python.md` (from data analyst notes archive — topic reference list)
> Existing Jupyter notebooks available in the Python study folder.

{section_text}
"""
            with open(target_path, "a", encoding="utf-8") as f:
                f.write(block)
            print(f"[APPEND] Python section '{section_key}' -> {target_fname}")
            appended += 1
        else:
            print(f"[MISS]   Section not found: '{section_key}'")

# ─────────────────────────────────────────────────────────────────────────────
# STEP 3: Update MySQL stubs with topic references
# ─────────────────────────────────────────────────────────────────────────────
print()
print("=" * 60)
print("STEP 3: Adding MySQL topic references from old notes")
print("=" * 60)

OLD_MY  = r'd:\My Drive\all files\PROJECT FILES\notes\docs\old and reference and future studies\_01_data_analyst_&_science\study material for data analyst and data science\02_mysql.md'
OLD_MYP = r'd:\My Drive\all files\PROJECT FILES\notes\docs\old and reference and future studies\_01_data_analyst_&_science\study material for data analyst and data science\03_mysql_with_python.md'

mysql_intro_target = os.path.join(BASE, "_05_mysql", "_05_01_database_architecture_and_relational_concepts.md")
mysql_python_target = os.path.join(BASE, "_05_mysql", "_05_12_mysql_integration_with_python.md")

for old_path, target_path, label in [
    (OLD_MY, mysql_intro_target, "MySQL Roadmap reference"),
    (OLD_MYP, mysql_python_target, "MySQL with Python reference"),
]:
    if os.path.exists(old_path) and os.path.exists(target_path):
        old_content = open(old_path, encoding="utf-8").read().strip()
        content = open(target_path, encoding="utf-8").read()
        if "## Migrated Notes" not in content:
            block = f"""

---

## Migrated Notes

> **Source**: `{os.path.basename(old_path)}` (from data analyst notes archive)
> {label}

{old_content}
"""
            with open(target_path, "a", encoding="utf-8") as f:
                f.write(block)
            print(f"[APPEND] {os.path.basename(old_path)} -> {os.path.basename(target_path)}")
            appended += 1
        else:
            print(f"[DUP]    Already has notes: {os.path.basename(target_path)}")
            skipped += 1

# ─────────────────────────────────────────────────────────────────────────────
# STEP 4: Add "old notebooks exist" reference block to ALL Python stubs
# ─────────────────────────────────────────────────────────────────────────────
print()
print("=" * 60)
print("STEP 4: Adding Jupyter notebook reference to all Python stubs")
print("=" * 60)

py_dir = os.path.join(BASE, "_02_python")
NOTEBOOK_REF = """

---

## Existing Jupyter Notebooks

> **Note**: Comprehensive Jupyter notebooks exist for this topic in the Python study folder.
> Reference the notebooks when authoring full lesson content.
> Notebooks follow the pattern: `_NN_00_topic.ipynb` (notes), `_NN_01_topic_Questions.ipynb`, `_NN_02_topic_Answers.ipynb`
"""

for fname in os.listdir(py_dir):
    if not fname.endswith(".md") or fname == "README.md":
        continue
    fpath = os.path.join(py_dir, fname)
    content = open(fpath, encoding="utf-8").read()
    if "Existing Jupyter Notebooks" not in content:
        with open(fpath, "a", encoding="utf-8") as f:
            f.write(NOTEBOOK_REF)
        print(f"[REF]    Added notebook ref: {fname}")
        migrated += 1

# ─────────────────────────────────────────────────────────────────────────────
# STEP 5: Add SQL reference to ALL MySQL stubs  
# ─────────────────────────────────────────────────────────────────────────────
print()
print("=" * 60)
print("STEP 5: Adding SQL note reference to all MySQL stubs")
print("=" * 60)

OLD_SQL_DIR = r'd:\My Drive\all files\PROJECT FILES\notes\docs\old and reference and future studies\_02_python_full_stack\_02_sqlserver'
my_dir = os.path.join(BASE, "_05_mysql")

# Get list of available SQL reference files
sql_files = []
if os.path.exists(OLD_SQL_DIR):
    sql_files = [f for f in os.listdir(OLD_SQL_DIR) if f.endswith(".sql")]

SQL_INVENTORY = "\n".join(f"  - `{f}`" for f in sorted(sql_files))

SQL_REF = f"""

---

## Existing SQL Reference Files

> **Note**: SQL Server reference scripts exist in the archive. Review and adapt for MySQL syntax.
> Location: `docs/old and reference and future studies/_02_python_full_stack/_02_sqlserver/`
>
{SQL_INVENTORY}
"""

for fname in os.listdir(my_dir):
    if not fname.endswith(".md"):
        continue
    fpath = os.path.join(my_dir, fname)
    content = open(fpath, encoding="utf-8").read()
    if "Existing SQL Reference Files" not in content:
        with open(fpath, "a", encoding="utf-8") as f:
            f.write(SQL_REF)
        print(f"[REF]    Added SQL ref: {fname}")
        migrated += 1

print()
print("=" * 60)
print(f"MIGRATION COMPLETE")
print(f"  Appended old content : {appended}")
print(f"  Added references     : {migrated}")
print(f"  Skipped/duplicate    : {skipped}")
print("=" * 60)
