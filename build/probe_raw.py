"""Dump raw (un-deduped) text of a question page to study the overlay pattern."""
import pymupdf
DOC = "source/pdf-uk-foundation-programme-sjt-questions-pdf_compress.pdf"
doc = pymupdf.open(DOC)
# page 17 (index 16) = 1.1 Relationships
t = doc[16].get_text("text")
print(repr(t[:2000]))
