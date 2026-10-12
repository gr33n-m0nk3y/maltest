"""Map all ANSWERS headers and chapter boundaries."""
import re
full = open("build/_book_clean.txt", encoding="utf-8").read()
lines = full.split("\n")

print("== all 'ANSWERS' headers ==")
for i, ln in enumerate(lines):
    if ln.strip() == "ANSWERS":
        print(f"  {i}: ANSWERS")

print("\n== all 'Chapter N' standalone lines ==")
for i, ln in enumerate(lines):
    if re.fullmatch(r"Chapter \d+", ln.strip()):
        print(f"  {i}: {ln!r}")

print("\n== context around each ANSWERS ==")
for i, ln in enumerate(lines):
    if ln.strip() == "ANSWERS":
        print(f"--- around {i} ---")
        for j in range(i-2, i+3):
            print(f"  {j}: {lines[j]!r}")
