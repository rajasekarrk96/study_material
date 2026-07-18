"""
Learning OS — Lab Validation Engine
"""
import os
import subprocess
import logging

logger = logging.getLogger("learning_os.lab_validation")

class LabValidationError(Exception):
    pass

class LabValidationEngine:
    @staticmethod
    def validate_local_git_repo(repo_path: str, rule: str, expected_value: str = None) -> tuple[bool, str]:
        """
        Validates a local Git repository path against a specific curriculum rule.
        Returns (success_boolean, status_message).
        """
        if not repo_path or not os.path.exists(repo_path):
            return False, f"Directory path '{repo_path}' does not exist on your computer. Please check the path."
        
        # Security: verify .git exists and path is a directory
        if not os.path.isdir(repo_path):
            return False, f"Path '{repo_path}' is not a directory."
            
        git_dir = os.path.join(repo_path, ".git")
        if not os.path.exists(git_dir):
            return False, f"No Git repository found at '{repo_path}' (missing .git directory)."

        try:
            if rule == "git_init":
                # Check if it is initialized and has a branch or status runs
                res = subprocess.run(["git", "status"], cwd=repo_path, capture_output=True, text=True, check=True)
                return True, "Git repository initialized successfully!\n" + res.stdout

            elif rule == "git_commit":
                # Check if there is at least one commit
                res = subprocess.run(["git", "log", "--oneline"], cwd=repo_path, capture_output=True, text=True)
                if res.returncode != 0:
                    return False, "No commits found in the repository yet. Create a commit to pass this step."
                commits = res.stdout.strip().split("\n")
                if len(commits) < 1:
                    return False, "No commits found in this repository."
                
                # If an expected commit message snippet is provided, check for it
                if expected_value:
                    matched = any(expected_value.lower() in c.lower() for c in commits)
                    if not matched:
                        return False, f"Found commits, but none matched the expected message: '{expected_value}'"
                
                return True, f"Found {len(commits)} commit(s) in repository history:\n" + res.stdout

            elif rule == "git_stage":
                # Check if there are staged changes (cached)
                res = subprocess.run(["git", "diff", "--cached", "--name-only"], cwd=repo_path, capture_output=True, text=True, check=True)
                staged_files = res.stdout.strip().split("\n")
                staged_files = [f for f in staged_files if f]
                if not staged_files:
                    return False, "No files currently in the staging area. Use 'git add <filename>' to stage changes."
                
                if expected_value:
                    if expected_value not in staged_files:
                        return False, f"Expected file '{expected_value}' is not staged. Current staged files: {', '.join(staged_files)}"
                
                return True, f"Staging area verification succeeded. Staged files:\n" + "\n".join(staged_files)

            elif rule == "git_branch":
                # Check if branch exists
                res = subprocess.run(["git", "branch", "--list"], cwd=repo_path, capture_output=True, text=True, check=True)
                branches = [b.replace("*", "").strip() for b in res.stdout.strip().split("\n") if b]
                if not expected_value:
                    return False, "Target branch name not specified for validation."
                if expected_value not in branches:
                    return False, f"Branch '{expected_value}' not found. Current branches: {', '.join(branches)}"
                return True, f"Branch '{expected_value}' verified successfully.\n" + res.stdout

            elif rule == "git_merge":
                # Check if target branch is merged into current branch (or log has it)
                if not expected_value:
                    return False, "Source branch name not specified for validation."
                # Checks if expected_value is merged into HEAD
                res = subprocess.run(["git", "branch", "--merged"], cwd=repo_path, capture_output=True, text=True, check=True)
                merged_branches = [b.replace("*", "").strip() for b in res.stdout.strip().split("\n") if b]
                if expected_value not in merged_branches:
                    # Let's check git log for merges as fallback
                    res_log = subprocess.run(["git", "log", "--merges", "--oneline"], cwd=repo_path, capture_output=True, text=True)
                    if expected_value.lower() in res_log.stdout.lower():
                        return True, f"Verified branch '{expected_value}' merge via merge commits:\n" + res_log.stdout
                    return False, f"Branch '{expected_value}' has not been merged into your current branch."
                return True, f"Verified branch '{expected_value}' is merged.\n" + res.stdout

            else:
                return False, f"Unknown validation rule: {rule}"

        except subprocess.CalledProcessError as e:
            logger.error(f"Git command failed in validation: {e.cmd}, stderr={e.stderr}")
            return False, f"Git validation command failed. Error details:\n{e.stderr or e.stdout}"
        except Exception as e:
            logger.error(f"Unexpected error validating repo path {repo_path}: {str(e)}")
            return False, f"An unexpected error occurred during validation: {str(e)}"
