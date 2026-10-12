"""Locate answers-section boundary and chapter headers in the cleaned book."""
import re
full = open("build/_book_clean.txt", encoding="utf-8").read()
lines = full.split("\n")

# find first answer-key line (letter-only, 3 or 5 letters) and its context
for i, ln in enumerate(lines):
    if re.fullmatch(r"[A-H](?: [A-H]){2,4}", ln.strip()):
        print(f"first key line at {i}: {ln!r}")
        print("context:")
        for j in range(max(0, i-6), i+2):
            print(f"  {j}: {lines[j]!r}")
        break

# chapter headers: look for 'Chapter N' lines
print("\n== 'Chapter N' lines (first 40) ==")
n = 0
for i, ln in enumerate(lines):
    if re.match(r"^Chapter \d+", ln.strip()):
        print(f"  {i}: {ln!r}")
        n += 1
        if n >= 40:
            break
