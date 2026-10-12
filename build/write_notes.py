"""Merge clinical note parts into app/data/notes.json.
v1 (notes_a/b/c) provides all 39 topics; v2 batches (enhanced) override per slug."""
import json, sys
from pathlib import Path
from notes_a import PART as A
from notes_b import PART as B
from notes_c import PART as C
from notes_v2_cardio import PART as V2_CARDIO
from notes_v2_resp_renal_gi import PART as V2_RRG
from notes_v2_haem_endo_neuro import PART as V2_HEN
from notes_v2_infection_resus_surgery import PART as V2_IRS

def main():
    merged = {}
    for part in (A, B, C):
        merged.update(part)
    v2 = {}
    for part in (V2_CARDIO, V2_RRG, V2_HEN, V2_IRS):
        v2.update(part)
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
    # which topics are still v1 (not enhanced)?
    still_v1 = [t["slug"] for t in topics if t["slug"] not in v2]
    print("topics:", len(topics), "| missing:", missing)
    print("still v1 (not enhanced):", still_v1)

if __name__ == "__main__":
    main()
