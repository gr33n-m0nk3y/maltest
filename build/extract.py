"""Combine all source extractors + starter SBA set into app/data/questions.json."""
import json, sys
from pathlib import Path

from extract_book import extract_book
from extract_30q import extract_30q
from extract_malta import extract_malta
from sba_a import PART as SBA_A
from sba_b import PART as SBA_B
from sba_c import PART as SBA_C

def main():
    bank = []
    bank += extract_book()
    bank += extract_30q()
    bank += extract_malta()
    bank += json.load(open("build/worked_manual.json", encoding="utf-8"))

    # starter SBA clinical set (AI-drafted, provisional — user reviews)
    for i, s in enumerate(SBA_A + SBA_B + SBA_C):
        bank.append({
            "id": f"clin-{i + 1}",
            "source": "clinical",
            "topic": s["topic"],
            "type": "sba",
            "scenario": s["scenario"],
            "options": s["options"],
            "key": s["key"],
            "explanation": s["rationale"],
            "provisional": True,
            "generated": False,
        })

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
