"""Analyze the 350-Q book: question types, chapter boundaries, answer keys."""
import re

full = open("build/_book_clean.txt", encoding="utf-8").read()
lines = full.split("\n")

# find answers section start (first standalone 'Answers' chapter header)
ans_start = None
for i, ln in enumerate(lines):
    if ln.strip() == "Answers" and i > 8000:
        ans_start = i
        break
print("answers section starts at line", ans_start)

# question types in questions section
qs = "\n".join(lines[:ans_start])
for pat, label in [
    (r"Rank in order", "rank5"),
    (r"Choose the THREE", "mcq3"),
    (r"Rate the", "rate"),
    (r"True or False|True/False|True or false", "tf"),
    (r"Which of the following", "which"),
    (r"Select the", "select"),
]:
    print(f"{label:8s}: {len(re.findall(pat, qs))}")

# chapter headers in questions section
print("\n== chapter headers ==")
for m in re.finditer(r"^Chapter (\d+):\s*([A-Z][^\n]{2,50})$", qs, re.M):
    print(m.group(1), m.group(2).strip())

# answer key lines in answers section (letter-only lines)
ans = "\n".join(lines[ans_start:])
keys = re.findall(r"^([A-H](?: [A-H]){1,7})$", ans, re.M)
print("\n== answer key lines in answers section:", len(keys))
from collections import Counter
lens = Counter(len(k.split()) for k in keys)
print("key lengths:", dict(lens))
print("sample keys:", keys[:8])
