"""Probe the 382-page SJT paper: section markers, keys, and thin pages."""
import fitz, re
from collections import Counter

DOC = "source/pdf-uk-foundation-programme-sjt-questions-pdf_compress.pdf"

doc = fitz.open(DOC)
print("== page 1 (first 800 chars) ==")
print(doc[0].get_text("text")[:800])

print("\n== thin pages ==")
for i in [1, 3, 7, 9, 11, 131, 179, 323]:
    t = doc[i].get_text("text")
    print(f"p{i+1}: {len(t.strip())} chars | images: {len(doc[i].get_images(full=True))}")

print("\n== page 100 (the page read_file choked on) ==")
t = doc[99].get_text("text")
print(f"chars: {len(t.strip())}")
print(t[:700])

# markers across whole doc
full = "\n".join(doc[i].get_text("text") for i in range(doc.page_count))
print("\n== markers ==")
for pat, label in [
    (r"Answer:\s*[A-E]{5}", "rank answers (Answer: XXXXX)"),
    (r"Correct key", "correct keys"),
    (r"Choose the THREE", "mcq3 stems"),
    (r"Rank in order", "ranking prompts"),
    (r"Rate the", "rating prompts"),
    (r"Practice Paper", "practice paper title"),
    (r"Situational Judgement Test", "SJT title refs"),
]:
    print(f"{label:32s}: {len(re.findall(pat, full))}")
