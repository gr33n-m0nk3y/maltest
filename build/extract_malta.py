"""Parse the Malta SJCT doc: 4 worked examples + exam blueprint facts."""
import re

LINES = open("build/_raw_malta.txt", encoding="utf-8").read().split("\n")

EX = re.compile(r"^(A1|A2|B1|B2)\.\s+(.+)$")
OPT_UP = re.compile(r"^([A-H])\.\s+(.*)$")
OPT_LO = re.compile(r"^([a-h])[\.\)]\s+(.*)$")
BARE = re.compile(r"^([a-h])[\.\)]\s*$")
INSTR_RANK = re.compile(r"Rank in order")
INSTR_MCQ = re.compile(r"Choose the three")
INSTR_TF = re.compile(r"Which of the following actions would be appropriate")
# real section boundaries — finalize the current block here
STOP = re.compile(r"^(Glossary:|Correct answers|ANSWER SCRIPTS|TEST INSTRUCTIONS)")
# running page header (repeats on every page) — skip, never append to options
SKIP = re.compile(r"^(SJCT Pilot Test information|April 2016|Malta Foundation School)")

def extract_malta():
    blocks = {}
    cur = None
    for ln in LINES:
        if SKIP.match(ln.strip()):
            continue
        if cur is not None and STOP.match(ln.strip()):
            blocks[cur["id"]] = cur
            cur = None
            continue
        m = EX.match(ln.strip())
        if m:
            if cur:
                blocks[cur["id"]] = cur
            cur = {"id": m.group(1), "scenario": [m.group(2)], "instruction": None,
                   "options": []}
            continue
        if cur is None:
            continue
        om = OPT_UP.match(ln.strip()) or OPT_LO.match(ln.strip())
        if om:
            cur["options"].append({"letter": om.group(1).upper(), "text": [om.group(2)]})
            continue
        bm = BARE.match(ln.strip())
        if bm:
            cur["options"].append({"letter": bm.group(1).upper(), "text": []})
            continue
        if cur["options"]:
            cur["options"][-1]["text"].append(ln.strip())
        elif cur["instruction"] is None and INSTR_RANK.search(ln):
            cur["instruction"] = "rank5"
        elif cur["instruction"] is None and INSTR_MCQ.search(ln):
            cur["instruction"] = "mcq3"
        elif cur["instruction"] is None and INSTR_TF.search(ln):
            cur["instruction"] = "tf"
        else:
            cur["scenario"].append(ln.strip())
    if cur:
        blocks[cur["id"]] = cur

    keys = {}
    in_ans = False
    for ln in LINES:
        if "Correct answers" in ln:
            in_ans = True
            continue
        if in_ans:
            m = re.match(r"^(A1|A2|B1|B2):\s*(.*)$", ln.strip())
            if m:
                keys[m.group(1)] = m.group(2).strip()

    out = []
    for bid, b in blocks.items():
        raw = keys.get(bid, "")
        if b["instruction"] == "rank5":
            pairs = re.findall(r"(\d+):\s*([A-E])", raw)
            pairs.sort(key=lambda p: int(p[0]))
            key = "".join(p[1] for p in pairs)
        elif b["instruction"] == "tf":
            key = "".join("T" if "True" in part else "F"
                          for part in re.findall(r"[A-E]:\s*(True|False)", raw))
        else:
            key = raw.replace(" ", "")
        out.append({
            "id": f"malta-{bid}",
            "source": "malta",
            "type": b["instruction"],
            "scenario": " ".join(x for x in b["scenario"] if x).strip(),
            "options": [o["text"][0] + (" " + " ".join(o["text"][1:]) if len(o["text"]) > 1 else "")
                        for o in b["options"]],
            "key": key,
            "explanation": "",
            "provisional": False,
        })
    return out

if __name__ == "__main__":
    qs = extract_malta()
    for q in qs:
        print(q["id"], q["type"], "key=", q["key"], "options=", len(q["options"]))
        for i, o in enumerate(q["options"]):
            print(f"  {chr(65+i)}: {o[:70]}")
