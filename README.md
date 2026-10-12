# Malta F1 Prep — Malta Foundation Training 1 Study & Self-Test Platform

A local-first study platform for the **Malta Foundation Training 1** exam (Situational Judgement / Clinical Test format, per the Malta SJCT pilot blueprint: 60 questions / 140 minutes).

**Personal-study use only.** The question bank is extracted from commercially published SJT materials — do not redistribute. All AI-drafted clinical content is marked **provisional — verify against your own sources**; the user (a medical student) is the final medical authority.

## Sections

| Tab | Purpose |
|---|---|
| **Learn** | The 39 exam topics (grouped by system) with AI-drafted essentials notes: mechanisms, key values, red flags, first-line management. Plus the exam blueprint. |
| **Clinical** | In-depth single-best-answer questions from the 39 topics (starter set AI-drafted, provisional). Filter by topic or 🎯 weak topics. |
| **Self-Test** | Official source bank: 30-question practice paper (keyed + rationales), 5 worked samples (keyed, per-option rationales), 4 Malta examples, and the 2023 UKFPO paper (75 questions, unkeyed → provisional). |
| **Situational** | 352 questions from the *350 Questions for the SJT* book (keyed + rationales, by theme) + the 2023 paper, with near-miss scoring. |
| **Mock Exam** | Full Malta-format mock: 60 Q / 140 min — Section A (25 rank5 + 15 MCQ 3-of-8 situational), Section B (10 MCQ 3-of-8 + 10 True/False clinical), timer, per-section score report. Section B2 is short (bank has few True/False items) until you generate more. |
| **Generate** | AI question generator (OpenRouter): clinical questions from any of the 39 topics, or situational scenarios by theme. Review/approve before they join your bank; generated items carry `[AI-GENERATED]` + `provisional` flags. |
| **Settings** | OpenRouter API key + model (used by Generate). Shows saved-answer stats and a **Wipe all answers** button. |

Every practice mode has **prev / random / next** navigation, **per-section answer persistence** (your answers are saved in this browser and survive switching sections or reloading), a **Reset answered questions** button per section, near-miss scoring per the official conventions, and rationale display. The mock exam does not persist (each attempt starts fresh).

## Question bank (544)

| Source | Count | Keyed |
|---|---|---|
| *350 Questions for the SJT* (Craig et al.) | 352 | ✅ + rationales |
| UKFPO 2023 practice paper | 75 | ❌ provisional |
| 30-Q practice paper | 30 | ✅ + rationales |
| Clinical starter SBA set (AI-drafted) | 78 | ✅ provisional |
| 5 worked sample questions | 5 | ✅ + rationales |
| Malta SJCT examples | 4 | ✅ |

Types: 286 rank5 · 158 mcq3 · 78 sba · 21 rate · 1 tf

## Run locally

```bash
cd app
python -m http.server 8873
# open http://localhost:8873
```

The OpenRouter API key for the generator lives in **your browser's localStorage only** — never in the repo. Default model: DeepSeek.

## Build / data pipeline

```bash
python -m venv .venv && .venv/Scripts/pip install pymupdf   # one-time
.venv/Scripts/python build/clean_text.py    # char-level overlay dedupe + ligature fixup (book)
.venv/Scripts/python build/extract.py       # PDFs + starter SBA -> app/data/questions.json
.venv/Scripts/python build/validate.py      # schema/count/key checks
node tests/test_engine.js                   # scoring engine unit tests (official matrices)
```

Notes:
- `source/` (PDFs) and `.venv/` are git-ignored — the copyrighted source materials stay out of the repo.
- The book PDF has a duplicated-text overlay and ligature glyphs; `clean_text.py` handles both.
- The 2023 paper needed position-sorted extraction (`sort=True`) to restore reading order.

## Live site

**https://gr33n-m0nk3y.github.io/maltest/** (repo: https://github.com/gr33n-m0nk3y/maltest)

Deployed with GitHub Actions (`.github/workflows/pages.yml`), which publishes the `app/` folder on every push to `main`.
Pages source = **GitHub Actions** (set once via the API; the workflow's own token cannot create the Pages site).

To redeploy: just `git push` to `main` — the workflow rebuilds and republishes automatically.

## Scoring conventions (matches the official sources)

- **rank5**: near-miss matrix — |ideal−candidate rank| = 0→4, 1→3, 2→2, 3→1, 4→0 (max 20). No tied ranks.
- **mcq3**: +4 per correct option (max 12); selecting ≠3 disqualifies the question.
- **tf**: +2 per correct statement (max 10).
- **rate**: exact=4, off-by-1=2, else 0 — approximation, the official 4-scale near-miss is unpublished.
- **sba**: 1 / 0.
- No negative marking anywhere (per the exam rules).

## Roadmap status

P0–P6 complete (inventory, extraction, clinical core, engine, practice modes, mock exam, Learn tab, generator) + P8 core (navigation/random, weak-topic drills, validators, README). Remaining: **P7 GitHub Pages deploy** (needs the repo) and polish items (2023-paper provisional AI keys review pass, more True/False items for mock Section B2 via the generator).
