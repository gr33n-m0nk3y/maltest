"""Search all pages of the 2023 paper for Q41's scenario (sorted extraction)."""
import pymupdf
DOC = "source/pdf-ukfp-sjt-practice-paper-2023_compress.pdf"
doc = pymupdf.open(DOC)
for i in range(doc.page_count):
    t = doc[i].get_text("text", sort=True)
    if "You are on a busy medical rotation" in t:
        print(f"== page {i+1} (sorted) ==")
        print(t[:2400])
        break
else:
    print("not found in sorted; trying unsorted")
    for i in range(doc.page_count):
        t = doc[i].get_text("text")
        if "You are on a busy medical rotation" in t:
            print(f"== page {i+1} (unsorted) ==")
            print(t[:2400])
            break
