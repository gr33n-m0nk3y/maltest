"""Clean the 350-Q book text: char-level positional dedupe (overlay copies
share char coordinates), line reconstruction, PUA ligature fixup."""
import pymupdf

DOC = "source/pdf-uk-foundation-programme-sjt-questions-pdf_compress.pdf"
OUT = "build/_book_clean.txt"

# E001 = single 'f' (safe). E000 = 'f' in most words, but 'ff'/'ffi'/'fl' in a
# few where one glyph collapsed. Map both to 'f', then fix known collapsed words.
PUA_MAP = {"\uE000": "f", "\uE001": "f"}
FIXUP = {
    # ff / ffi collapses
    "Efective": "Effective", "Efectively": "Effectively", "Efect": "Effect",
    "offcer": "officer", "offcers": "officers", "efts": "effects", "Efects": "Effects",
    # fl collapses (ligature 'fl' -> 'f')
    "fattered": "flattered", "fowers": "flowers", "profle": "profile",
    "fll": "fill", "flling": "filling", "flled": "filled", "fuid": "fluid",
    "fexible": "flexible", "foor": "floor", "fag": "flag", "fash": "flash",
    "faw": "flaw", "fesh": "flesh", "fying": "flying", "fight": "flight",
    "fow": "flow", "fowchart": "flowchart", "favour": "flavour",
    "fame": "flame", "fap": "flap", "fexion": "flexion", "fexibility": "flexibility",
    "fowever": "however", "fooring": "flooring", "fuidly": "fluidly",
}

def fix_text(s):
    for k, v in PUA_MAP.items():
        s = s.replace(k, v)
    for k, v in FIXUP.items():
        s = s.replace(k, v)
    return s

def clean_page(page, y_tol=3.0):
    d = page.get_text("rawdict")
    chars = []
    for b in d["blocks"]:
        for l in b.get("lines", []):
            for s in l.get("spans", []):
                for ch in s.get("chars", []):
                    chars.append((ch["origin"][0], ch["origin"][1], ch["c"]))
    seen = {}
    for x, y, c in chars:
        key = (round(x), round(y))
        if key not in seen:
            seen[key] = c
    items = sorted(seen.items(), key=lambda kv: (kv[0][1], kv[0][0]))
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
    return fix_text("\n".join(out))

def main():
    doc = pymupdf.open(DOC)
    pages = [clean_page(p) for p in doc]
    full = "\n".join(pages)
    open(OUT, "w", encoding="utf-8").write(full)
    print(f"wrote {OUT} ({len(full)} chars, {doc.page_count} pages)")

if __name__ == "__main__":
    main()
