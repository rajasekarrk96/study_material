#!/usr/bin/env python3
"""
Bytes and Boards Solutions — Markdown Lesson Title Updater.
Appends clean, descriptive lesson titles directly to the YAML frontmatter of our notes.
"""
from pathlib import Path
import re

TITLE_MAP = {
    # Git
    "_01_07_git_fundamentals_lesson1_history.md": "Version Control History & Evolution",
    "_01_03_git_fundamentals_lesson1.md": "Git Architecture & Three States",
    "_01_05_git_fundamentals_lesson2.md": "Local Workflow: Init, Stage & Commit",
    "_01_06_git_fundamentals_lesson3.md": "Inspecting History: Log & Diff",
    "_01_09_git_fundamentals_lesson4_undo.md": "Undoing Changes: Reset, Revert & Restore",
    "_01_10_git_fundamentals_lesson5_branch.md": "Branching Basics & Conflict Resolution",
    "_01_11_git_collaboration_lesson1_remotes.md": "Remote Repositories & Origin Config",
    "_01_12_git_collaboration_lesson2_sync.md": "Syncing Data: Fetch, Pull & Push",
    "_01_13_git_collaboration_lesson3_conflicts.md": "Merge Conflict Handling in Teams",
    "_01_14_git_collaboration_lesson4_forks.md": "Forking & Upstream Workflows",
    "_01_15_advanced_git_lesson1_internals.md": "Git Internals: Blobs, Trees & Commits",
    "_01_16_advanced_git_lesson2_history.md": "Rewriting History: Amend, Rebase & Squash",
    "_01_17_advanced_git_lesson3_helpers.md": "Workspace Helpers: Stash, Bisect & Worktree",
    "_01_18_advanced_git_lesson4_hooks.md": "Git Customization: Hooks & Aliases",
    # C
    "_06_02_c_fundamentals_lesson1.md": "Introduction to C: History, Setup & Hello World",
    "_06_03_c_fundamentals_lesson2.md": "C Compilation Lifecycle & GCC Pipeline",
    # C++
    "_07_02_cpp_oop_lesson1.md": "Transition to C++: Namespaces & Streams",
    "_07_03_cpp_oop_lesson2.md": "Classes, Objects & Constructor Overloading"
}

def update_titles():
    base_dir = Path("docs/notes preparing implementation")
    for file_name, clean_title in TITLE_MAP.items():
        # Find file in subdirectories
        matches = list(base_dir.glob(f"**/_{file_name.lstrip('_')}")) + list(base_dir.glob(f"**/{file_name}"))
        if not matches:
            print(f"File not found: {file_name}")
            continue
        
        file_path = matches[0]
        print(f"Updating {file_path.name} -> {clean_title}")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Insert lesson_title under lesson_id in yaml frontmatter
        # Finds lesson_id: "xyz" or lesson_id: xyz
        yaml_match = re.search(r"(lesson_id:\s*[\"\']?[\w-]+[\"\']?)", content)
        if yaml_match:
            target = yaml_match.group(1)
            replacement = f"{target}\nlesson_title: \"{clean_title}\""
            content = content.replace(target, replacement, 1)
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  [SUCCESS] Appended title.")
        else:
            print(f"  [ERROR] lesson_id not found in {file_path.name}")

if __name__ == "__main__":
    update_titles()
