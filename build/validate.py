"""Validate the question bank: schema, counts, key/option consistency."""
import json, sys
from collections import Counter

def main():
    bank = json.load(open("app/data/questions.json", encoding="utf-8"))
    errors = []
    types = Counter()
    sources = Counter()

    for q in bank:
        types[q["type"]] += 1
        sources[q["source"]] += 1
        for f in ("id", "source", "type", "scenario", "options", "key", "provisional"):
            if f not in q:
                errors.append(f"{q.get('id')}: missing field {f}")
        t, opts, key = q["type"], q.get("options", []), q.get("key")
        unkeyed = q.get("provisional") and key is None  # provisional unkeyed items allowed
        if t == "rank5":
            if len(opts) != 5 or (not unkeyed and len(key) != 5):
                errors.append(f"{q['id']}: rank5 needs 5 options & 5-letter key (got {len(opts)}/{len(key)})")
            if not unkeyed and (not isinstance(key, str) or not set(key) <= set("ABCDE")):
                errors.append(f"{q['id']}: bad rank5 key {key!r}")
        elif t == "mcq3":
            if len(opts) != 8 or (not unkeyed and len(key) != 3):
                errors.append(f"{q['id']}: mcq3 needs 8 options & 3-letter key (got {len(opts)}/{len(key)})")
            if not unkeyed and (not isinstance(key, str) or not set(key) <= set("ABCDEFGH")):
                errors.append(f"{q['id']}: bad mcq3 key {key!r}")
        elif t == "tf":
            if len(opts) != 5 or (not unkeyed and len(key) != 5):
                errors.append(f"{q['id']}: tf needs 5 options & 5-char key (got {len(opts)}/{len(key)})")
            if not unkeyed and (not isinstance(key, str) or not set(key) <= set("TF")):
                errors.append(f"{q['id']}: bad tf key {key!r}")
        elif t == "rate":
            if not unkeyed and (not isinstance(key, list) or len(key) != len(opts)):
                errors.append(f"{q['id']}: rate key list must match option count")
            if not unkeyed and any(not (1 <= k <= 4) for k in (key if isinstance(key, list) else [])):
                errors.append(f"{q['id']}: rate keys must be 1-4")
        elif t == "sba":
            if len(opts) < 4 or len(opts) > 5:
                errors.append(f"{q['id']}: sba needs 4-5 options (got {len(opts)})")
            if not unkeyed and (not isinstance(key, str) or len(key) != 1 or key not in "ABCDE"):
                errors.append(f"{q['id']}: bad sba key {key!r}")
        else:
            errors.append(f"{q['id']}: unknown type {t!r}")

    print(f"total: {len(bank)}")
    print("types:", dict(types))
    print("sources:", dict(sources))
    if errors:
        print(f"\nERRORS ({len(errors)}):")
        for e in errors[:40]:
            print("  ", e)
        sys.exit(1)
    print("\nOK — bank valid")

if __name__ == "__main__":
    main()
