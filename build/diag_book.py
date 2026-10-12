"""Diagnose: questions with no instruction, and Ch4 missing answer."""
import re
from extract_book import parse_questions, parse_answers, LINES, CH, ANS_END

# find None-instruction questions
all_q = []
for ci, (qstart, aheader) in enumerate(CH):
    qs = parse_questions(LINES[qstart:aheader-1])
    all_q += qs

print("== questions with instruction=None ==")
for q in all_q:
    if q["instruction"] is None:
        print(f"  {q['num']} {q['title']!r}")
        print("   scenario tail:", q["scenario"][-3:])

# Ch4 answers
qstart, aheader = CH[3]
ans = parse_answers(LINES[aheader:ANS_END[3]])
print("\n== Ch4 answer nums (first/last) ==")
nums = sorted(ans.keys(), key=lambda s: float(s))
print("  count:", len(nums), "first:", nums[:3], "last:", nums[-3:])

# Ch4 question nums
qs4 = parse_questions(LINES[qstart:aheader-1])
qnums = sorted({q["num"] for q in qs4}, key=lambda s: float(s))
print("  question count:", len(qnums))
missing = [n for n in qnums if n not in ans]
print("  questions missing answers:", missing)
