import os
import re

TOPICS = [
    "Arrays",
    "BinarySearch",
    "DynamicProgramming",
    "Graphs",
    "HashMap",
    "LinkedList",
    "Queue",
    "Stack",
    "Strings",
    "Trees",
    "TwoPointers"
]

counts = {}
total = 0

for topic in TOPICS:
    if os.path.isdir(topic):
        files = [
            f for f in os.listdir(topic)
            if f.endswith(".py") and f != "__init__.py"
        ]
        counts[topic] = len(files)
        total += len(files)
    else:
        counts[topic] = 0

readme = f"""# 🚀 LeetCode Solutions

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![LeetCode](https://img.shields.io/badge/Platform-LeetCode-orange)
![Problems Solved](https://img.shields.io/badge/Problems-{total}-success)

This repository contains my LeetCode solutions organized by topic.

---

## 📊 Progress

| Topic | Solved |
|--------|--------|
"""

for topic in TOPICS:
    name = topic.replace("HashMap", "Hash Map") \
                .replace("BinarySearch", "Binary Search") \
                .replace("DynamicProgramming", "Dynamic Programming") \
                .replace("LinkedList", "Linked List") \
                .replace("TwoPointers", "Two Pointers")

    readme += f"| {name} | {counts[topic]} |\n"

readme += f"""

**Total Solved:** {total}

---

## 📂 Folder Structure
