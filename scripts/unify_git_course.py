#!/usr/bin/env python3
"""
Bytes and Boards Solutions — Markdown Course Unifier.
Standardizes the course metadata of all 14 Git markdown files to 'Git Fundamentals'
so they are grouped into a single unified learning path.
"""
from pathlib import Path
import re

def unify_course():
    git_dir = Path("docs/notes preparing implementation/_01_git")
    files = list(git_dir.glob("*.md"))
    
    for file_path in files:
        if "curriculum" in file_path.name.lower() or "placeholder" in file_path.name.lower() or "template" in file_path.name.lower():
            continue

        print(f"Unifying course metadata in {file_path.name}...")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Replace course: "Git Collaboration" / "Advanced Git" with "Git Fundamentals"
        new_content = re.sub(
            r'course:\s*[\"\']?(?:Git Collaboration|Advanced Git|Git Fundamentals)[\"\']?',
            'course: "Git Fundamentals"',
            content
        )

        if new_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print("  [UPDATED] -> Git Fundamentals")
        else:
            print("  [OK] Already Git Fundamentals")

if __name__ == "__main__":
    unify_course()
