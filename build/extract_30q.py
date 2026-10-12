"""Parse the 30-Q practice paper (keyed, with rationales)."""
import re

LINES = open("build/_raw_30q.txt", encoding="utf-8").read().split("\n")

QNUM = re.compile(r"^(\d+)\.\s+(.+)$")
OPT = re.compile(r"^([A-H])\.\s+(.*)$")
INSTR_RANK = re.compile(r"Rank in order")
INSTR_MCQ = re.compile(r"Choose the THREE")
FOOTER = re.compile(r"^(Page \d+ of \d+|©.*)$")

def extract_30q():
    qs = []
    cur = None
    for ln in LINES:
        if FOOTER.match(ln.strip()):
            continue
        am = re.match(r"^Answer:\s*([A-H]+)\s*$", ln.strip())
        if am:
            if cur:
                cur["key"] = am.group(1)
                qs.append(cur)
                cur = None
            continue
        if cur is None:
            m = QNUM.match(ln.strip())
            if m:
                cur = {"num": m.group(1), "scenario": [m.group(2)], "instruction": None,
                       "options": [], "rationale": []}
            continue
        rm = re.match(r"^Rationale:\s*(.*)$", ln.strip())
        if rm:
            cur["rationale"].append(rm.group(1))
            continue
        om = OPT.match(ln.strip())
        if om:
            cur["options"].append({"letter": om.group(1), "text": [om.group(2)]})
            continue
        if cur["options"]:
            cur["options"][-1]["text"].append(ln.strip())
        elif cur["instruction"] is not None:
            continue  # instruction continuation — skip
        elif INSTR_RANK.search(ln):
            cur["instruction"] = "rank5"
        elif INSTR_MCQ.search(ln):
            cur["instruction"] = "mcq3"
        else:
            cur["scenario"].append(ln.strip())

    out = []
    for q in qs:
        qtype = q["instruction"]
        if qtype is None:
            qtype = "rank5" if len(q["key"]) == 5 else "mcq3"
        out.append({
            "id": f"30q-{q['num']}",
            "source": "30q",
            "type": qtype,
            "scenario": " ".join(x for x in q["scenario"] if x).strip(),
            "options": [o["text"][0] + (" " + " ".join(o["text"][1:]) if len(o["text"]) > 1 else "")
                        for o in q["options"]],
            "key": q["key"],
            "explanation": " ".join(q["rationale"]).strip(),
            "provisional": False,
        })
    return out

if __name__ == "__main__":
    qs = extract_30q()
    from collections import Counter
    print("total:", len(qs))
    print("types:", Counter(q["type"] for q in qs))
    bad = [q for q in qs if (q["type"] == "rank5" and (len(q["key"]) != 5 or len(q["options"]) != 5))
           or (q["type"] == "mcq3" and (len(q["key"]) != 3 or len(q["options"]) != 8))]
    print("malformed:", len(bad), [q["id"] for q in bad])
    import json
    print("\nsample:", json.dumps(qs[0], indent=1)[:700])
