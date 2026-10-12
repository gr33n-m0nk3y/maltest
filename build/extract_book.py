"""Parse the 350-Q book into structured questions (production parser)."""
import re, json

LINES = open("build/_book_clean.txt", encoding="utf-8").read().split("\n")

# question number + title; title must start with an uppercase letter (excludes
# stray "6.4 mmol/L." scenario lines)
QNUM = re.compile(r"^(\d+)\.(\d+)\s+([A-Z][^\n]*)$")
OPT = re.compile(r"^\xa0([A-H])\s*(.*)$")            # "\xa0A Explain..."
INSTR_RANK = re.compile(r"Rank\s*in\s*order")
INSTR_MCQ = re.compile(r"Choose\s*the\s*THREE")
REC_READ = re.compile(r"^Recommended reading")
# running page headers / footers to strip
RUNNING = re.compile(r"^(Questions \d+|Answers \d+|\d+ Chapter \d+:.*|Chapter \d+:.*|\d+ \d+ [A-Z])")
# garbage: short all-lowercase lines with no vowel (overlay remnants like "yypy")
GARBAGE = re.compile(r"^[a-z]{2,8}$")

# chapter boundaries: (questions_start, answers_header) from map_sections.py
CH = [(300, 2448), (5265, 6146), (7308, 8660), (10337, 11753), (13506, 14570)]
ANS_END = [5265, 7308, 10337, 13506, len(LINES)]
CHAPTER_NAMES = {
    1: "Commitment to Professionalism", 2: "Coping with Pressure",
    3: "Effective Communication", 4: "Patient Focus",
    5: "Working Effectively as Part of a Team",
}

def parse_questions(region):
    qs = []
    cur = None
    for ln in region:
        if RUNNING.match(ln) or GARBAGE.match(ln):
            continue
        m = QNUM.match(ln)
        if m:
            if cur:
                qs.append(cur)
            cur = {"num": f"{m.group(1)}.{m.group(2)}", "title": m.group(3).strip(),
                   "scenario": [], "instruction": None, "options": []}
            continue
        if cur is None:
            continue
        om = OPT.match(ln)
        if om:
            cur["options"].append({"letter": om.group(1), "text": [om.group(2)]})
            continue
        # nbsp-prefixed line: lost-letter option (letter dropped in typesetting)
        # or an empty separator — assign the next letter if it has text
        if ln.startswith("\xa0"):
            body = ln.strip("\xa0").strip()
            if body and cur["options"]:
                prev = cur["options"][-1]["letter"]
                cur["options"].append({"letter": chr(ord(prev) + 1), "text": [body]})
            continue
        if cur["options"]:
            # option line without nbsp prefix (page-break artifact): "H Write..."
            last = cur["options"][-1]["letter"]
            nxt = chr(ord(last) + 1)
            nm = re.match(rf"^{nxt}\s+(.+)$", ln)
            if nm:
                cur["options"].append({"letter": nxt, "text": [nm.group(1)]})
                continue
            cur["options"][-1]["text"].append(ln)
        elif cur["instruction"] is not None:
            # continuation of the instruction line(s) — skip until first option
            continue
        elif INSTR_RANK.search(ln):
            cur["instruction"] = "rank5"
        elif INSTR_MCQ.search(ln):
            cur["instruction"] = "mcq3"
        else:
            cur["scenario"].append(ln)
    if cur:
        qs.append(cur)
    return qs

def parse_answers(region):
    ans = {}
    cur = None
    for ln in region:
        if RUNNING.match(ln) or GARBAGE.match(ln):
            continue
        m = QNUM.match(ln)
        if m:
            if cur:
                ans[cur["num"]] = cur
            cur = {"num": f"{m.group(1)}.{m.group(2)}", "title": m.group(3).strip(),
                   "key": None, "explanation": []}
            continue
        if cur is None:
            continue
        if cur["key"] is None and re.fullmatch(r"[A-H](?: [A-H]){1,7}", ln.strip()):
            cur["key"] = ln.strip().replace(" ", "")
            continue
        cur["explanation"].append(ln)
    if cur:
        ans[cur["num"]] = cur
    return ans

def extract_book():
    all_q, all_a = [], {}
    for ci, (qstart, aheader) in enumerate(CH):
        chapter = ci + 1
        qs = parse_questions(LINES[qstart:aheader - 1])
        ans = parse_answers(LINES[aheader:ANS_END[ci]])
        for q in qs:
            q["chapter"] = chapter
            q["topic"] = CHAPTER_NAMES[chapter]
        all_q += qs
        all_a.update(ans)

    out = []
    for q in all_q:
        a = all_a.get(q["num"])
        if a is None:
            continue
        qtype = q["instruction"]
        if qtype is None:
            qtype = "rank5" if len(a["key"]) == 5 else "mcq3"
        out.append({
            "id": f"book-{q['num']}",
            "source": "book",
            "chapter": q["chapter"],
            "topic": q["topic"],
            "type": qtype,
            "scenario": " ".join(q["scenario"]).strip(),
            "options": [o["text"][0] + (" " + " ".join(o["text"][1:]) if len(o["text"]) > 1 else "")
                        for o in q["options"]],
            "key": a["key"],
            "explanation": " ".join(a["explanation"]).strip(),
            "provisional": False,
        })
    return out

if __name__ == "__main__":
    qs = extract_book()
    from collections import Counter
    print("total:", len(qs))
    print("types:", Counter(q["type"] for q in qs))
    print("per chapter:", Counter(q["chapter"] for q in qs))
    bad = [q for q in qs if (q["type"] == "rank5" and (len(q["key"]) != 5 or len(q["options"]) != 5))
           or (q["type"] == "mcq3" and (len(q["key"]) != 3 or len(q["options"]) != 8))]
    print("malformed:", len(bad), [q["id"] for q in bad][:10])
    print("option counts:", Counter(len(q["options"]) for q in qs))
    print("\nsample:", json.dumps(qs[0], indent=1)[:900])
