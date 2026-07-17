#!/usr/bin/env python3
"""
Bytes and Boards Solutions — Markdown Heading Refactoring.
Removes legacy "Lesson X:" prefixes from the main H1 headings in our markdown files.
"""
from pathlib import Path
import re

def clean_headings():
    base_dir = Path("docs/notes preparing implementation")
    files = list(base_dir.rglob("*.md"))
    
    for file_path in files:
        if "curriculum" in file_path.name.lower() or "placeholder" in file_path.name.lower() or "template" in file_path.name.lower():
            continue

        print(f"Cleaning H1 in {file_path.name}...")
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        if not lines:
            continue

        first_line = lines[0]
        # Matches: # Lesson 1: Topic OR # Upgraded Lesson 3: Topic
        cleaned_line = re.sub(r"^#\s*(?:Upgraded\s+)?Lesson\s+\d+[a-zA-Z]?:\s*", "# ", first_line)
        # Also clean optional dash/emdash formats: "# Lesson 1: Topic — Subtopic" -> "# Topic — Subtopic"
        
        if cleaned_line != first_line:
            lines[0] = cleaned_line
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(lines)
            print(f"  [CLEANED] -> {cleaned_line.strip()}")
        else:
            print("  [OK] Already clean.")

if __name__ == "__main__":
    clean_headings()
