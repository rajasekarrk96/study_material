"""
rename_curriculum.py
────────────────────────────────────────────────────────────────
Fixes all curriculum folder naming issues:
  1. Removes junk empty sub-folders inside courses
  2. Renames all 31 course folders to a clean sequential scheme
  3. Fixes supervised_learning nested sub-folder issue

RENAMING MAP (logical learning order):
  Foundation  → 01 git
  Web         → 02 html5, 03 css3, 04 bootstrap, 05 jquery, 06 javascript
  Languages   → 07 python, 08 java, 09 c, 10 cpp
  Databases   → 11 mysql, 12 sql_server, 13 mongodb
  Frameworks  → 14 flask, 15 fastapi
  Testing     → 16 selenium
  IoT Track   → 17 iot_hardware, 18 pcb, 19 iot_projects
  Data Science→ 20 ds_math, 21 python_data_science, 22 power_bi
  AI/ML Track → 23 machine_learning, 24 deep_learning, 25 computer_vision,
                26 nlp, 27 generative_ai_llms, 28 rag_engineering,
                29 ai_agents, 30 mlops_ai_deployment
  Advanced    → 31 prompt_engineering
"""
import os, shutil

BASE = r'd:\My Drive\all files\PROJECT FILES\notes\docs\curriculum'

# ── STEP 1: Delete junk empty sub-folders ────────────────────────
JUNK_DIRS = [
    r'_02_python\css',
    r'_02_python\js',
    r'_04_selenium\content',
    r'_04_selenium\css',
    r'_04_selenium\js',
    r'_04_selenium\worksheets',
    r'_05_mysql\topics',
    r'_03_java\shared',
]

print("=" * 60)
print("STEP 1: Removing junk empty folders")
print("=" * 60)

for rel in JUNK_DIRS:
    p = os.path.join(BASE, rel)
    if os.path.exists(p):
        # Only delete if truly empty (no md files inside)
        mds = [f for r, d, files in os.walk(p) for f in files if f.endswith('.md')]
        if not mds:
            shutil.rmtree(p)
            print(f"[DELETE] {rel}")
        else:
            print(f"[SKIP]   {rel} — has .md files, not deleting")
    else:
        print(f"[MISS]   {rel} — already gone")

# ── STEP 2: Fix _10_06_supervised_learning nested sub-dirs ───────
print()
print("=" * 60)
print("STEP 2: Fix supervised_learning module structure")
print("=" * 60)

sup_path = os.path.join(BASE, "_10_machine_learning", "_10_06_supervised_learning")
if os.path.exists(sup_path):
    sub_dirs = [d for d in os.listdir(sup_path) if os.path.isdir(os.path.join(sup_path, d))]
    print(f"  Sub-dirs in _10_06: {sub_dirs}")
    for sd in sub_dirs:
        sdp = os.path.join(sup_path, sd)
        mds = [f for f in os.listdir(sdp) if f.endswith('.md')]
        if not mds:
            shutil.rmtree(sdp)
            print(f"  [DELETE] {sd}")
        else:
            print(f"  [KEEP]   {sd} — has .md files")
else:
    print("  _10_06_supervised_learning not found")

# ── STEP 3: Rename all course folders ────────────────────────────
print()
print("=" * 60)
print("STEP 3: Renaming course folders")
print("=" * 60)

# Map: old_name -> new_name
RENAME_MAP = [
    # Foundation
    ("_01_git",                  "_01_git"),               # already correct
    # Web Fundamentals
    ("_01_html5",                "_02_html5"),
    ("_02_css3",                 "_03_css3"),
    ("_18_bootstrap",            "_04_bootstrap"),
    ("_19_jquery",               "_05_jquery"),
    ("_03_javascript",           "_06_javascript"),
    # Programming Languages
    ("_02_python",               "_07_python"),
    ("_03_java",                 "_08_java"),
    ("_06_c",                    "_09_c"),
    ("_07_cpp",                  "_10_cpp"),
    # Databases
    ("_05_mysql",                "_11_mysql"),
    ("_20_sql_server",           "_12_sql_server"),
    ("_21_mongodb",              "_13_mongodb"),
    # Frameworks
    ("_04_flask",                "_14_flask"),
    ("_05_fastapi",              "_15_fastapi"),
    # Testing
    ("_04_selenium",             "_16_selenium"),
    # IoT Track
    ("_06_iot_hardware",         "_17_iot_hardware"),
    ("_09_pcb",                  "_18_pcb"),
    ("_10_iot_projects",         "_19_iot_projects"),
    # Data Science
    ("_08_ds_math",              "_20_ds_math"),
    ("_09_python_data_science",  "_21_python_data_science"),
    ("_23_power_bi",             "_22_power_bi"),
    # AI/ML Track
    ("_10_machine_learning",     "_23_machine_learning"),
    ("_11_deep_learning",        "_24_deep_learning"),
    ("_12_computer_vision",      "_25_computer_vision"),
    ("_13_nlp",                  "_26_nlp"),
    ("_14_generative_ai_llms",   "_27_generative_ai_llms"),
    ("_15_rag_engineering",      "_28_rag_engineering"),
    ("_16_ai_agents",            "_29_ai_agents"),
    ("_17_mlops_ai_deployment",  "_30_mlops_ai_deployment"),
    # Advanced
    ("_22_prompt_engineering",   "_31_prompt_engineering"),
]

# Use a temp prefix to avoid collisions during rename (e.g., _01 -> _02 would conflict if _02 exists)
TEMP_PREFIX = "_TEMP_RENAME_"

# Phase A: rename all to temp names
print("  Phase A: Rename to temp names...")
for old, new in RENAME_MAP:
    old_path = os.path.join(BASE, old)
    tmp_path = os.path.join(BASE, TEMP_PREFIX + old)
    if os.path.exists(old_path):
        os.rename(old_path, tmp_path)
        print(f"  [TEMP] {old} -> {TEMP_PREFIX+old}")
    else:
        print(f"  [MISS] {old} not found")

# Phase B: rename from temp to final names
print()
print("  Phase B: Rename to final names...")
for old, new in RENAME_MAP:
    tmp_path = os.path.join(BASE, TEMP_PREFIX + old)
    new_path = os.path.join(BASE, new)
    if os.path.exists(tmp_path):
        if os.path.exists(new_path) and old != new:
            print(f"  [CONFLICT] {new} already exists! Skipping.")
        else:
            os.rename(tmp_path, new_path)
            if old != new:
                print(f"  [RENAME] {old:35s} -> {new}")
            else:
                print(f"  [KEEP]   {old}")
    else:
        print(f"  [MISS]   temp not found for {old}")

# ── STEP 4: Final count ───────────────────────────────────────────
print()
print("=" * 60)
print("STEP 4: Final state")
print("=" * 60)

folders = sorted([d for d in os.listdir(BASE) if os.path.isdir(os.path.join(BASE, d))])
total_files = 0
for f in folders:
    cnt = sum(1 for root, dirs, files in os.walk(os.path.join(BASE, f)) for fn in files if fn.endswith('.md'))
    total_files += cnt
    print(f"  {f}  [{cnt}]")

print()
print(f"  TOTAL: {len(folders)} courses | {total_files} lesson files")
print("=" * 60)
