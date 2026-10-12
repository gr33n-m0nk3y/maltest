"""Inspect the problem questions: 3.60, 4.22, and the stray 6.4."""
import re
LINES = open("build/_book_clean.txt", encoding="utf-8").read().split("\n")

def show(num, region):
    for i, ln in enumerate(region):
        if ln.startswith(num + " "):
            print(f"--- {num} at line {i} ---")
            for j in range(i, min(i+14, len(region))):
                print(f"  {region[j]!r}")
            return

# 3.60 in Ch3 questions (7308-8660)
show("3.60", LINES[7308:8660])
# 4.22 in Ch4 questions (10337-11753)
show("4.22", LINES[10337:11753])
# stray 6.4 in Ch4 questions
for i, ln in enumerate(LINES[10337:11753]):
    if ln.startswith("6.4 "):
        print(f"--- 6.4 at {i} ---")
        for j in range(i, i+6):
            print(f"  {LINES[10337+j]!r}")
