"""Dump 2023 paper with position-sorted extraction."""
import pymupdf
DOC = "source/pdf-ukfp-sjt-practice-paper-2023_compress.pdf"
doc = pymupdf.open(DOC)
full = "\n".join(p.get_text("text", sort=True) for p in doc)
open("build/_raw_2023_sorted.txt", "w", encoding="utf-8").write(full)
print(f"wrote {len(full)} chars")
