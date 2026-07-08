from pathlib import Path
import json
import re
import subprocess

# Repository root
REPO_ROOT = Path(__file__).resolve().parent.parent

# Load problem → topic mapping
with open(REPO_ROOT / "scripts" / "problem_topics.json", "r") as f:
    topic_map = json.load(f)

# Match folders like 0001-two-sum
problem_pattern = re.compile(r"^\d{4}-")

print(f"Repository: {REPO_ROOT}\n")

for item in REPO_ROOT.iterdir():

    # Ignore non-problem folders
    if not item.is_dir() or not problem_pattern.match(item.name):
        continue

    problem = item.name

    # Skip if problem is not in mapping
    if problem not in topic_map:
        print(f"⚠ No topic found for {problem}")
        continue

    topic = topic_map[problem]
    destination = REPO_ROOT / topic

    # Create topic folder if needed
    destination.mkdir(exist_ok=True)

    target = destination / problem

    # Skip if already moved
    if target.exists():
        print(f"✓ {problem} already organized")
        continue

    print(f"Moving {problem} → {topic}")

    subprocess.run(
        ["git", "mv", str(item), str(target)],
        cwd=REPO_ROOT,
        check=True
    )

print("\nDone!")