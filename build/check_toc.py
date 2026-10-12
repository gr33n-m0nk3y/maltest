"""Check TOC chapter list and the document tail."""
import re
full = open("build/_book_clean.txt", encoding="utf-8").read()
lines = full.split("\n")

print("== TOC region (lines 150-210) ==")
for j in range(150, 210):
    print(f"  {j}: {lines[j]!r}")

print("\n== last 40 lines ==")
for j in range(len(lines)-40, len(lines)):
    print(f"  {j}: {lines[j]!r}")
