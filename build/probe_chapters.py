"""Map chapters + answer format of the 350-Q SJT book."""
import fitz, re

DOC = "source/pdf-uk-foundation-programme-sjt-questions-pdf_compress.pdf"
doc = fitz.open(DOC)
full = "\n".join(doc[i].get_text("text") for i in range(doc.page_count))

print("== chapter headings ==")
for m in re.finditer(r"Chapter \d+:\s*[A-Z][^\n]{3,60}", full):
    s = m.group(0).replace("\n", " ").strip()
    if len(s) < 70:
        print(s)

print("\n== answer-section markers ==")
for pat in [r"Answers", r"Answer [0-9]+", r"The correct answer", r"1st.{0,40}B", r"e.g\.\s*[A-E]"]:
    ms = re.findall(pat, full)
    print(f"{pat!r}: {len(ms)}")

# sample: a ranking question + surrounding answer text
i = full.find("Rank in order")
print("\n== sample around first 'Rank in order' ==")
print(full[i-200:i+1500])
