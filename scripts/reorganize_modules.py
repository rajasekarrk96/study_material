import os
import re

directory = "docs/curriculum/_01_git"

mappings = {
    "GIT-FND-001a": {"module": "Git Foundations", "title": "Version Control History & Evolution"},
    "GIT-FND-001": {"module": "Git Foundations", "title": "Git Architecture & Three States"},
    "GIT-FND-002": {"module": "Git Foundations", "title": "Local Workflow: Init, Stage & Commit"},
    "GIT-FND-003a": {"module": "History Management", "title": "Interactive Staging: Patch Mode & Partial Commits"},
    "GIT-FND-003": {"module": "History Management", "title": "Inspecting History: Log & Diff"},
    "GIT-FND-004": {"module": "History Management", "title": "Undoing Changes: Reset, Restore & Revert"},
    "GIT-FND-005": {"module": "Branching & Merging", "title": "Branching Basics & Conflict Resolution"},
    "GIT-COL-003": {"module": "Branching & Merging", "title": "Merge Conflict Handling in Teams"},
    "GIT-COL-001": {"module": "Remote Collaboration", "title": "Remote Repositories & Origin Config"},
    "GIT-COL-002": {"module": "Remote Collaboration", "title": "Syncing Data: Fetch, Pull & Push"},
    "GIT-COL-004": {"module": "Remote Collaboration", "title": "Forking & Upstream Workflows"},
    "GIT-ADV-005": {"module": "Advanced Workflows", "title": "Cherry-picking & Backporting"},
    "GIT-ADV-002": {"module": "Advanced Workflows", "title": "Rewriting History: Amend, Rebase & Squash"},
    "GIT-ADV-003": {"module": "Advanced Workflows", "title": "Workspace Helpers: Stash, Bisect & Worktree"},
    "GIT-ADV-007": {"module": "Advanced Workflows", "title": "Branching Strategies for Teams"},
    "GIT-ADV-006": {"module": "Advanced Workflows", "title": "Tags & Release Management"},
    "GIT-ADV-001": {"module": "Git Internals", "title": "Git Internals: Blobs, Trees & Commits"},
    "GIT-ADV-004": {"module": "Automation & Security", "title": "Git Customization: Hooks & Aliases"},
    "GIT-ADV-008": {"module": "Automation & Security", "title": "Credential Management & Security"},
    "GIT-ADV-009": {"module": "Troubleshooting", "title": "Diagnostic & Troubleshooting Guide"}
}

for filename in os.listdir(directory):
    if not filename.endswith(".md") or filename.startswith("README") or filename.startswith("_01_01") or filename.startswith("_01_02"):
        continue
    filepath = os.path.join(directory, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Parse YAML frontmatter
    match = re.search(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL | re.MULTILINE)
    if not match:
        print(f"No YAML header found in {filename}")
        continue
    
    yaml_block = match.group(1)
    
    # Extract lesson_id
    id_match = re.search(r"lesson_id:\s*\"?([A-Z0-9a-z-]+)\"?", yaml_block)
    if not id_match:
        print(f"No lesson_id found in {filename}")
        continue
    
    lesson_id = id_match.group(1)
    if lesson_id not in mappings:
        print(f"Unknown lesson_id {lesson_id} in {filename}")
        continue
    
    meta = mappings[lesson_id]
    
    # Replace module and lesson_title
    new_yaml = yaml_block
    new_yaml = re.sub(r"lesson_title:\s*.*", f'lesson_title: "{meta["title"]}"', new_yaml)
    new_yaml = re.sub(r"module:\s*.*", f'module: "{meta["module"]}"', new_yaml)
    
    # Replace heading H1
    new_content = content.replace(yaml_block, new_yaml)
    new_content = re.sub(r"^#\s+.*", f'# {meta["title"]}', new_content, count=1)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"Updated {filename}: title='{meta['title']}', module='{meta['module']}'")

print("Reorganization completed!")
