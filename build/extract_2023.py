"""Parse the UK 2023 SJT practice paper (75 questions, unkeyed -> provisional)."""
import re

LINES = open("build/_raw_2023_sorted.txt", encoding="utf-8").read().split("\n")

# question starts
QNUM = re.compile(r'^\s*(\d{1,2})\.\s+([A-Z\u201c].+)$')          # "41. You are on a busy..."
PART_A = re.compile(r"^\s*(\d{1,2})\. Part [AB]( \(for reference\))?\s*:?\s*$")
PART_B = re.compile(r"^\s*Part B:\s*$")
# options
OPT_DOT = re.compile(r"^\s*([A-H])\.\s+(.+)$")                # "A. text" (rating)
OPT_OPT = re.compile(r"^\s*[•●]?\s*Option ([A-H]):\s*(.*)$")  # "Option A: text"
BULLET = re.compile(r"^\s*[•●]\s*$")
# instructions
INSTR_RATE = re.compile(r"Rate the")
INSTR_MCQ = re.compile(r"Choose the THREE")
INSTR_RANK = re.compile(r"Rank in order")
# junk
PART_HEAD = re.compile(r"^PART (ONE|TWO|THREE)")
PAGENUM = re.compile(r"^\s*\d{1,3}\s*$")

def extract_2023():
    qs = []
    cur = None
    pending_partb = None  # number for an upcoming "Part B:"

    def start_question(num):
        nonlocal cur
        if cur:
            qs.append(cur)
        cur = {"num": num, "scenario": [], "instruction": None, "options": []}

    for ln in LINES:
        s = ln.strip()
        if not s or PAGENUM.match(s) or PART_HEAD.match(s):
            continue
        if BULLET.match(s):
            continue
        # part markers
        pa = PART_A.match(s)
        if pa:
            if "(for reference)" in pa.group(0):
                # repeated scenario ahead; the following "Part B:" is a new question
                pending_partb = pa.group(1)
            else:
                start_question(f"{pa.group(1)}A")
            continue
        pb = PART_B.match(s)
        if pb:
            start_question(f"{pending_partb or '?'}B")
            pending_partb = None
            continue
        # generic question start
        qm = QNUM.match(s)
        if qm:
            start_question(qm.group(1))
            cur["scenario"].append(qm.group(2).strip())
            continue
        # skip repeated reference scenarios until Part B arrives
        if pending_partb:
            continue
        if cur is None:
            continue
        om = OPT_OPT.match(s)
        if om:
            cur["options"].append({"letter": om.group(1), "text": [om.group(2).strip()]})
            continue
        om2 = OPT_DOT.match(s)
        if om2:
            cur["options"].append({"letter": om2.group(1), "text": [om2.group(2).strip()]})
            continue
        if cur["options"]:
            cur["options"][-1]["text"].append(s)
        elif cur["instruction"] is None and INSTR_RATE.search(s):
            cur["instruction"] = "rate"
        elif cur["instruction"] is None and INSTR_MCQ.search(s):
            cur["instruction"] = "mcq3"
        elif cur["instruction"] is None and INSTR_RANK.search(s):
            cur["instruction"] = "rank5"
        else:
            cur["scenario"].append(s)
    if cur:
        qs.append(cur)

    # assemble output, infer type from option counts if instruction missing
    out = []
    for i, q in enumerate(qs):
        qtype = q["instruction"]
        if qtype is None:
            n = len(q["options"])
            qtype = "rank5" if n == 5 else ("mcq3" if n == 8 else "rate" if 4 <= n <= 8 else "unknown")
        out.append({
            "id": f"fp2023-{i + 1}",
            "source": "fp2023",
            "type": qtype,
            "scenario": " ".join(x for x in q["scenario"] if x).strip(),
            "options": [o["text"][0] + (" " + " ".join(o["text"][1:]) if len(o["text"]) > 1 else "")
                        for o in q["options"]],
            "key": None,  # unkeyed — provisional AI keys later
            "explanation": "",
            "provisional": True,
            "paperNum": q["num"],
        })
    return out

if __name__ == "__main__":
    qs = extract_2023()
    from collections import Counter
    print("total:", len(qs))
    print("types:", Counter(q["type"] for q in qs))
    print("paper num sample:", [(q["paperNum"], q["type"], len(q["options"])) for q in qs[:10]])
    q = qs[0]
    print("\nsample:", q["scenario"][:120])
