"""List unique tokens containing PUA chars, to build the ligature fixup map."""
import re
from collections import Counter

full = open("build/_book_clean.txt", encoding="utf-8").read()
toks = re.findall(r"[A-Za-z0-9'’\-]*[\uE000\uE001][A-Za-z0-9'’\-]*", full)
c = Counter(toks)
print("== E001 tokens (top 60) ==")
for t, n in c.most_common(60):
    if "\uE001" in t:
        print(f"{n:5d}  {t!r}")
print("\n== E000 tokens (all) ==")
for t, n in sorted(c.items(), key=lambda x: -x[1]):
    if "\uE000" in t:
        print(f"{n:5d}  {t!r}")
