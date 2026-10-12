"""Combine all source extractors into app/data/questions.json."""
import json, sys
from pathlib import Path

from extract_book import extract_book
from extract_30q import extract_30q
from extract_malta import extract_malta

def main():
    bank = []
    bank += extract_book()
    bank += extract_30q()
    bank += extract_malta()
    # worked samples are hand-curated (per-option rating schema)
    bank += json.load(open("build/worked_manual.json", encoding="utf-8"))

    # normalize: ensure every item has the fields the engine expects
    for q in bank:
        q.setdefault("topic", None)
        q.setdefault("chapter", None)
        q.setdefault("provisional", False)
        q.setdefault("generated", False)
        q.setdefault("difficulty", None)

    out = Path("app/data/questions.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(bank, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {out} — {len(bank)} questions")

if __name__ == "__main__":
    main()
