"""Find why mcq3 questions lose an option (7 instead of 8)."""
import re
from extract_book import parse_questions, LINES, CH

# parse chapter 1 questions
qs = parse_questions(LINES[300:2447])
mcq = [q for q in qs if q["instruction"] == "mcq3"]
print("mcq3 in ch1:", len(mcq))
q = mcq[0]
print("num:", q["num"], "title:", q["title"])
print("option letters:", [o["letter"] for o in q["options"]])
print("option count:", len(q["options"]))

# find the raw region for this question and print all option-marker lines
start = None
for i, ln in enumerate(LINES[300:2447]):
    if ln.startswith(q["num"] + " "):
        start = i
        break
region = LINES[300+start:300+start+60]
print("\n== raw lines after title ==")
for ln in region[:40]:
    print(repr(ln))
