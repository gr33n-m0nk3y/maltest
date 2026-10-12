"""Merge the three note parts into app/data/notes.json."""
import json, sys
from pathlib import Path
from notes_a import PART as A
from notes_b import PART as B
from notes_c import PART as C

def main():
    merged = {}
    for part in (A, B, C):
        for slug, note in part.items():
            if slug in merged:
                print(f"WARN: duplicate slug {slug}")
            merged[slug] = note
    out = Path("app/data/notes.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(merged, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {out} — {len(merged)} notes")

    # cross-check against topics.json
    topics = json.load(open("app/data/topics.json", encoding="utf-8"))
    missing = [t["slug"] for t in topics if t["slug"] not in merged]
    extra = [s for s in merged if s not in {t["slug"] for t in topics}]
    print("topics:", len(topics), "| notes missing:", missing, "| extra notes:", extra)

if __name__ == "__main__":
    main()
