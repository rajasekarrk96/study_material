#!/usr/bin/env python3
"""
Bytes and Boards Solutions — Markdown ILF Layout Converter.
Reads all lesson files in a folder and automatically maps their 20-section structure
into the simplified 5-section Interactive Learning Format (ILF).
"""
import re
import sys
import yaml
from pathlib import Path

def parse_markdown_sections(content: str) -> tuple:
    """Extracts YAML frontmatter and split sections by heading anchors."""
    yaml_match = re.search(r"```yaml\n(.*?)\n```", content, re.DOTALL)
    if not yaml_match:
        return {}, ""

    frontmatter_str = yaml_match.group(1)
    try:
        metadata = yaml.safe_load(frontmatter_str)
    except Exception as e:
        print(f"Error parsing YAML: {e}")
        return {}, ""

    body_text = content[yaml_match.end():]

    section_pattern = re.compile(
        r"^##\s+\d+\.\s+(.*?)\s+\[id:\s*([\w_]+)\]\s*\n",
        re.MULTILINE
    )

    matches = list(section_pattern.finditer(body_text))
    sections = {}

    for i, match in enumerate(matches):
        section_type = match.group(2).strip()
        start_idx = match.end()
        end_idx = matches[i + 1].start() if i + 1 < len(matches) else len(body_text)
        sections[section_type] = body_text[start_idx:end_idx].strip()

    return metadata, sections

def build_ilf_content(title_line: str, metadata: dict, sections: dict) -> str:
    """Builds a new markdown string structured in the ILF format."""
    
    # 1. Frontmatter
    meta_str = yaml.dump(metadata, sort_keys=False, default_flow_style=False).strip()
    
    # 2. Extract sections
    overview = sections.get("overview", "").strip()
    outcomes = sections.get("outcomes", "").strip()
    concept = sections.get("concept", "").strip()
    terminology = sections.get("terminology", "").strip()
    examples = sections.get("examples", "").strip()
    exercises = sections.get("exercises", "").strip()
    cheatsheet = sections.get("cheatsheet", "").strip()
    
    # 3. Assemble sections
    # Topics Covered
    topics_content = ""
    if overview:
        topics_content += overview + "\n\n"
    if outcomes:
        topics_content += "### Learning Outcomes\n" + outcomes

    # Definitions & Core Concepts
    definitions_content = ""
    if concept:
        definitions_content += concept + "\n\n"
    if terminology:
        definitions_content += "### Terminology & Glossary\n" + terminology

    # Practical Examples
    examples_content = examples if examples else "*No examples available for this topic.*"

    # Workouts
    workouts_content = exercises if exercises else "*No workouts available for this topic.*"

    # Answers
    answers_content = cheatsheet if cheatsheet else "*Solutions can be found in the cheatsheet reference section.*"

    new_content = f"""{title_line}

---

```yaml
{meta_str}
```

---

## 1. Topics Covered [id: topics]
{topics_content.strip()}

## 2. Definitions & Core Concepts [id: definitions]
{definitions_content.strip()}

## 3. Practical Code Examples [id: examples]
{examples_content.strip()}

## 4. Hands-on Workouts [id: workouts]
{workouts_content.strip()}

## 5. Workout Answers & Solutions [id: answers]
{answers_content.strip()}
"""
    return new_content

def convert_folder(folder_path: Path):
    """Scan and convert all markdown files in a folder to ILF."""
    print(f"Scanning folder: {folder_path.name}")
    for file in sorted(folder_path.glob("*.md")):
        if "curriculum" in file.name.lower() or "placeholder" in file.name.lower() or "template" in file.name.lower():
            continue

        print(f"  Converting file: {file.name}")
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        # Find first line (Title line)
        title_line_match = re.match(r"^(#\s+.*?)\n", content)
        title_line = title_line_match.group(1) if title_line_match else f"# {file.stem}"

        metadata, sections = parse_markdown_sections(content)
        if not metadata or not sections:
            print(f"    [SKIP] Failed to parse structure of {file.name}")
            continue

        new_markdown = build_ilf_content(title_line, metadata, sections)
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_markdown)
        print(f"    [SUCCESS] Converted {file.name} to ILF format.")

if __name__ == "__main__":
    base_dir = Path("docs/notes preparing implementation")
    # Convert git notes
    convert_folder(base_dir / "_01_git")
    print("ILF conversion complete!")
