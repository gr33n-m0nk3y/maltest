"""Inspect remaining malformed mcq3 questions (7 options)."""
import re
from extract_book import parse_questions, LINES, CH

for ci, (qstart, aheader) in enumerate(CH):
    qs = parse_questions(LINES[qstart:aheader-1])
    for q in qs:
        if q["num"] in ("1.5", "1.15", "1.93", "2.3", "5.17"):
            print(f"=== {q['num']} {q['title']} — {len(q['options'])} options ===")
            print("letters:", [o["letter"] for o in q["options"]])
            # find raw region
            for i, ln in enumerate(LINES[qstart:aheader-1]):
                if ln.startswith(q["num"] + " "):
                    print("raw:")
                    for j in range(i, i+30):
                        print("  ", repr(LINES[qstart+j]))
                    break
            print()
