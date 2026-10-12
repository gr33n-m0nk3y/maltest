"""Phase 0 inventory: per-source page stats, text vs scanned-page detection."""
import json, sys
from pathlib import Path
import fitz

SRC = Path("source")

def page_stats(pdf_path):
    doc = fitz.open(pdf_path)
    stats = {"file": pdf_path.name, "pages": doc.page_count,
             "text_pages": 0, "thin_pages": [], "img_pages": []}
    for i, page in enumerate(doc):
        txt = page.get_text("text")
        n = len(txt.strip())
        if n >= 80:
            stats["text_pages"] += 1
        else:
            stats["thin_pages"].append((i + 1, n, len(page.get_images(full=True))))
    return stats

def main():
    report = [page_stats(p) for p in sorted(SRC.glob("*.pdf"))]
    for r in report:
        print(f"{r['file']}: {r['pages']} pages, {r['text_pages']} text-rich, "
              f"{len(r['thin_pages'])} thin/scanned candidates")
        if r["thin_pages"] and len(r["thin_pages"]) <= 12:
            for pg, n, imgs in r["thin_pages"]:
                print(f"    p{pg}: {n} chars, {imgs} images")
        elif r["thin_pages"]:
            print(f"    first thin pages: {r['thin_pages'][:5]}")
    json.dump(report, open("build/_inventory.json", "w"), indent=1)
    print("wrote build/_inventory.json")

if __name__ == "__main__":
    main()
