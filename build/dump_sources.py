"""Dump raw text of the 4 non-book sources for parser design."""
import pymupdf

SOURCES = {
    "30q": "source/pdf-p-classtruncatedtext-module-lineclamped-85ulhh-style-max-lines5fy1-sjt-practice-paper-answer-and-rationales-large-print-p_compress.pdf",
    "worked": "source/pdf-ukfpo-sjt-practice-paper-sample-questions_compress.pdf",
    "malta": "source/pdf-sjct-pilot-test-guidelines-for-malta_compress.pdf",
    "2023": "source/pdf-ukfp-sjt-practice-paper-2023_compress.pdf",
}
for key, path in SOURCES.items():
    doc = pymupdf.open(path)
    txt = "\n".join(p.get_text("text") for p in doc)
    open(f"build/_raw_{key}.txt", "w", encoding="utf-8").write(txt)
    print(f"{key}: {doc.page_count} pages, {len(txt)} chars -> build/_raw_{key}.txt")
