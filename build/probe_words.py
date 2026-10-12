"""Check whether the duplicated text copies share word coordinates (for positional dedupe)."""
import pymupdf
DOC = "source/pdf-uk-foundation-programme-sjt-questions-pdf_compress.pdf"
doc = pymupdf.open(DOC)
words = doc[16].get_text("words")  # (x0,y0,x1,y1,word,block,line,wordno)
print("total words:", len(words))
# look for near-duplicate positions
from collections import Counter
pos = Counter((round(w[0]), round(w[1])) for w in words)
dups = {p: n for p, n in pos.items() if n > 1}
print("positions with >1 word:", len(dups))
# sample a duplicated position
for p, n in list(dups.items())[:5]:
    ws = [w[4] for w in words if (round(w[0]), round(w[1])) == p]
    print(p, n, ws)
