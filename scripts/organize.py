from pathlib import Path
import re

# Repository root (parent of the scripts folder)
REPO_ROOT = Path(__file__).resolve().parent.parent

# Pattern for LeetCode problem folders (e.g., 0001-two-sum)
problem_pattern = re.compile(r"^\d{4}-")

print(f"Repository: {REPO_ROOT}\n")

print("Problems found:")
for item in REPO_ROOT.iterdir():
    if item.is_dir() and problem_pattern.match(item.name):
        print(f" - {item.name}")
