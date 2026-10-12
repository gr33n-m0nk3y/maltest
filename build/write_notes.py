"""Merge clinical note parts into app/data/notes.json.
v1 (notes_a/b/c) provides all 39 topics; v2 parts (enhanced) override per slug."""
import json, sys
from pathlib import Path
from notes_a import PART as A
from notes_b import PART as B
from notes_c import PART as C
from notes_v2_cardio import PART as V2_CARDIO

def main():
    merged = {}
    for part in (A, B, C):
        merged.update(part)
    v2 = {}
    v2.update(V2_CARDIO)
    for slug, note in v2.items():
        if slug not in merged:
            print(f"WARN: v2 slug not in topics: {slug}")
        merged[slug] = note
    out = Path("app/data/notes.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(merged, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {out} — {len(merged)} notes ({len(v2)} enhanced)")

    topics = json.load(open("app/data/topics.json", encoding="utf-8"))
    missing = [t["slug"] for t in topics if t["slug"] not in merged]
    print("topics:", len(topics), "| missing:", missing)

if __name__ == "__main__":
    main()
