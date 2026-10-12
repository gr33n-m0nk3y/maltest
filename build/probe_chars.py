"""Test char-level positional dedupe on a question page."""
import pymupdf
DOC = "source/pdf-uk-foundation-programme-sjt-questions-pdf_compress.pdf"
doc = pymupdf.open(DOC)

def clean_page_char(page, y_tol=3.0):
    d = page.get_text("rawdict")
    chars = []
    for b in d["blocks"]:
        for l in b.get("lines", []):
            for s in l.get("spans", []):
                for ch in s.get("chars", []):
                    chars.append((ch["origin"][0], ch["origin"][1], ch["c"]))
    # dedupe by rounded position
    seen = {}
    for x, y, c in chars:
        key = (round(x), round(y))
        if key not in seen:
            seen[key] = c
    # sort by (y, x)
    items = sorted(seen.items(), key=lambda kv: (kv[0][1], kv[0][0]))
    # group into lines
    lines = []
    cur = []
    cur_y = None
    for (x, y), c in items:
        if cur_y is None or abs(y - cur_y) <= y_tol:
            cur.append((x, c))
            cur_y = y if cur_y is None else cur_y
        else:
            lines.append(cur)
            cur = [(x, c)]
            cur_y = y
    if cur:
        lines.append(cur)
    out = []
    for ln in lines:
        ln.sort(key=lambda t: t[0])
        out.append("".join(c for _, c in ln))
    return "\n".join(out)

t = clean_page_char(doc[16])
print(t[:1800])
