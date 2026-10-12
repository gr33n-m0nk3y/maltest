"""Inspect one full question block incl. its answer/explanation layout."""
import fitz, re

DOC = "source/pdf-uk-foundation-programme-sjt-questions-pdf_compress.pdf"
doc = fitz.open(DOC)
# find the page containing 'Police caution'
for i in range(10, 40):
    t = doc[i].get_text("text")
    if "Police caution" in t:
        print(f"== p{i+1} ==")
        print(t[:3500])
        break
