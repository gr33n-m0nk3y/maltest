# Malta Foundation Training 1 — Learning Platform (rev 2)

> **For Hermes:** implement this plan phase-by-phase; each phase independently verifiable.

**Goal:** Static, local-first learning platform for the Malta Foundation Training 1: (1) learn the 39-topic clinical core in depth, (2) self-test against the official sample questions from the source PDFs, (3) practice situational-judgement questions, (4) sit a Malta-format mock exam, (5) generate new in-depth clinical and situational questions. Repo/project name: **maltest**. Hosted on GitHub Pages.

**Architecture:** Pure static site (HTML/CSS/JS, no build step) reusing the proven onco pattern: extracted JSON banks + vanilla-JS engine + OpenRouter key in localStorage. The clinical core (39 topics) is **authored content** (AI-drafted, user-reviewed) — the source PDFs do NOT cover it; they feed Sections 2 and 3 only.

**Tech stack:** Python 3 (extraction/OCR/validation), vanilla JS engine, localStorage (progress + user banks), GitHub Pages, OpenRouter (DeepSeek default) for generation + clinical-note drafting.

---

## 1. Syllabus — the 39 clinical topics (Section 1: Learning)

Exam questions come **only** from these topics, but are **in-depth** within them. Canonical list → `data/topics.json` (id, slug, name, group) + per-topic notes. Draft grouping (user-adjustable):

| Group | Topics |
|---|---|
| Cardiovascular | Anticoagulation management (INR/APTT), Chest pain, Common arrhythmias, Collapse and shock, Syncope, Acute limb ischaemia, Chronic limb ischaemia (ulcers and gangrene), DVT and Pulmonary embolism |
| Respiratory | Shortness of breath, Oxygen management in wards, Arterial blood gas interpretation |
| Renal, fluids & electrolytes | Electrolyte management, Low urine output, Intravenous fluid prescription |
| Gastrointestinal & hepatology | Gastrointestinal bleeds, Hepatic encephalopathy, Ascites, Jaundice |
| Haematology & acute oncology | Neutropenic sepsis, Congenital bleeding disorders, Spinal cord compression |
| Endocrine & metabolic | Diabetes control, Hypoglycaemia, Diabetic foot complications + sepsis |
| Neurology & elderly | Acute confusional states, Falls in elderly persons |
| Obstetrics & gynaecology | Gynaecology and Obstetric emergencies |
| Dermatology | Skin rashes in the acute setting |
| Infection & sepsis | The febrile patient, Infection control on the ward |
| Resuscitation & emergencies | Cardiopulmonary resuscitation, Anaphylaxis, Overdoses |
| Surgery & peri-operative | Post-operative complications, Urine retention |
| Ward systems & patient safety | Medication administration errors, The Early Warning Score, Management of venous access lines |
| Miscellaneous | Issues around COVID-19 |

**Per-topic content** (why-focused, mechanisms not rote lists — matches user's study style):
- **Essentials note**: mechanisms, red flags, first-line management.
- **Key values/tables** (INR/APTT interpretation, EWS thresholds, ABG patterns, IV fluid composition…).
- **In-depth question pool** per topic, linked from the topic page.

**Content authority:** AI-drafted (OpenRouter) from standard guidelines, saved as **editable** notes, user-reviewed/corrected — the user (a medical student) is final medical authority. Clinical questions are similarly AI-authored + reviewed, tagged `domain: clinical, topic: <slug>`.

## 2. Source inventory — feeds Sections 2 & 3 only

| File | Role |
|---|---|
| `pdf-sjct-pilot-test-guidelines-for-malta` | Exam blueprint: 60 Q / 140 min. Section A: Q1-25 rank5, Q26-40 3-of-8 situational; Section B: Q41-50 3-of-8 clinical, Q51-60 TF. Near-miss, no negative marking, no tied ranks, over-select = question scored zero. 4 keyed worked examples (A1/A2/B1/B2). |
| `pdf-ukfpo-sjt-practice-paper-sample-questions` | 5 worked questions, official keys + rationales → Section 2 core + generator few-shot exemplars. |
| `pdf-...-answer-and-rationales-large-print` | 30-Q practice paper, official keys + rationales + ideal-rank matrices (16 rank5 + 14 mcq3) → Section 2 ground truth + engine test fixtures. |
| `pdf-ukfp-sjt-practice-paper-2023` | 75-Q paper (18 rate + 22 mcq3 + 35 rank5), **no official keys** → Section 3 pool, provisional AI keys. |
| `pdf-uk-foundation-programme-sjt-questions` (382 pp) | **"350 Questions for the SJT"** (Craig et al.): keyed situational question book, chapters = themes (1 Commitment to Professionalism, 2 Coping with Pressure, 3 Effective Communication, 4 Patient Focus, 5 Teamwork, …10 Competence, 11 Relating to Colleagues), ~350 mixed-format questions with inline answers + explanations. Text quirks: duplicated lines + ligature PUA glyphs → fixed in P1. |

Expected extracted bank: **≈465 items** — keyed: ~350 (book) + 30 (practice paper) + 5 (worked samples) + 4 (Malta examples); unkeyed: 75 (2023 paper). **No OCR required** (382-pager has only 8 blank/image pages).

## 3. App layout — 5 mandatory sections + analytics

| Tab | File | Contents |
|---|---|---|
| 1. **Learn** | `index.html` | 39-topic browser (grouped), per-topic essentials notes + tables, link to per-topic in-depth quiz, blueprint explainer + glossary |
| 2. **Self-Test** | `self-test.html` | Official source bank (5 worked + 30-Q + 4 Malta examples): practice with official keys/rationales/near-miss matrices |
| 3. **Situational** | `situational.html` | SJT engine: rank5 / rate / mcq3 scenarios (2023 paper w/ provisional keys + generated), near-miss scoring, rationale display, scenario-type drills |
| 4. **Mock Exam** | `mock.html` | 60 Q / 140 min Malta format: Section A = situational (25 rank5 + 15 mcq3), Section B = clinical (10 mcq3 + 10 TF). Timer, section score report, disqualification rules |
| 5. **Generate** | `generate.html` | Two engines: Clinical (pick topic → in-depth SBA/3-of-8/TF), Situational (source-grounded scenarios). Review/approve → bank, `[AI-GENERATED]` flags |
| — **Progress** | integrated | Per-topic mastery, weak-topic drill (onco weak-mode pattern), attempt history |

## 4. Question schema (revised)

`{id, domain: clinical|source|situational, type: rank5|rate|mcq3|tf|sba, topic?: <slug>, source, stem, options[], key, rationale, difficulty, generated, provisional}`

| Type | Options | Key | Scoring |
|---|---|---|---|
| `rank5` | 5 | permutation `"BADCE"` | near-miss matrix 4-3-2-1-0 (official tables) |
| `mcq3` | 8 | 3 letters `"BGH"` | +4 per hit (max 12) |
| `tf` | 5 statements | `"FTFTF"` | +2 per hit (max 10) |
| `rate` | 4-8 | per-option 1-4 | exact=4, off-by-1=2, else 0 (approximation — see Risks) |
| `sba` | 4-5 | single letter | 1 correct / 0 — **for in-depth clinical knowledge; format PENDING USER** |

## 5. Phases (revised order)

**P0 — Inventory (DONE).** All 5 PDFs verified extractable via pymupdf; the 382-pager identified as the 350-Q keyed SJT book (chapter themes = situational taxonomy). No OCR pass needed. Tooling: `build/inventory.py`, `build/probe_*.py`.

**P1 — Extraction pipeline (DONE).** `build/extract.py` → `app/data/questions.json`: **391 keyed questions** (book 352 + 30-Q 30 + Malta 4 + worked 5), validated by `build/validate.py` (0 errors). Book parser handles char-level overlay dedupe, ligature fixup, lost-letter options, running-header stripping. **2023 paper (75, unkeyed) deferred** to a later pass — its fragmented multi-part rating format needs dedicated parsing and it's provisional-keyed anyway.

**P2 — Clinical core (DONE).** `data/topics.json` (39 topics, 14 groups) + `data/notes.json` (39 AI-drafted essentials notes: mechanisms, key values, red flags, management) + **78 starter SBA questions** (`source: clinical`, provisional). All cross-checked (39/39 topics matched). *User reviews the AI-drafted notes/questions.*

**P3 — Engine + Sections 2 & 3 (DONE).** `js/engine.js` (5 scorers + mock assembler), 30 unit tests green vs official matrices. `self-test.html` + `situational.html` practice modes (rationale display, provisional-key toggle, theme/type filters). Verified in browser.

**P4 — Mock exam (DONE).** `mock.html`: 60/140 Malta format, timer, section score report, shortfall reporting (B2 short — 1 tf in bank; generator fills it).

**P5 — Learn tab (DONE).** `index.html`: 39-topic grouped browser + per-topic notes + blueprint + glossary. Verified.

**P6 — Generator (DONE).** `generate.html`: two engines (clinical-by-topic SBA/mcq3/tf; situational rank5/mcq3), OpenRouter (localStorage key, DeepSeek default), strict output schema + client validation, review/approve/edit before saving, `[AI-GENERATED]` + provisional flags, export/import JSON. Generated bank merges into practice/mock via `loader.js`. *User generates the full clinical bank with their key.*

**P7 — GitHub Pages deploy.** git init, commit, create repo `maltest`, push, enable Pages, relative asset paths. Key stays in localStorage. *Verify: live URL loads; all tabs functional.*

**P8 — Polish.** 2023 provisional-key review pass (user approves each), weak-topic drill, progress stats, README + deploy notes.

## 6. Risks & open questions

1. **PENDING USER — In-depth clinical question format for the 39 topics:** single-best-answer (SBA, recommended), 3-of-8, True/False, or mix? (SBA best for depth; TF/3-of-8 kept for mock Section B fidelity regardless.)
2. **PENDING USER — Topic groupings above** (approve or adjust — e.g. Syncope under Neurology vs Cardiovascular).
3. **Content authority:** AI-drafted clinical notes/questions need the user's medical review; accuracy caveat shown in UI ("AI-drafted — verify").
4. **2023 paper unkeyed** → provisional AI keys, visibly flagged, user-approved in P8 (recommended) vs study-only.
5. **Rating near-miss not published** → exact=4 / off-by-1=2 / else 0, labelled approximation.
6. **Text-layer quirks in the 350-Q book:** duplicated lines + ligature glyphs (0xE000/0xE001→f) with some collapsed double-f words ("Profesionalism") — fixed via mapping + token dictionary; residual cosmetic artifacts acceptable.
7. **Copyright:** the 350-Q book is commercial — platform stays personal-study use: `source/` excluded from git (`.gitignore`), recommend a private repo, README carries a "personal use only" note.
8. **Malta format drift:** blueprint is the 2016 pilot doc; section composition is configurable in `buildMock` if user has newer info.
9. **Repo `maltest`** — user creates it (or gives account/org); verify OpenRouter CORS from Pages origin once live.

## 7. Execution handoff

Execute per phase, commit at each green milestone; onco project (`D:\projects\onco`) is the UI/UX reference; generator/notes default DeepSeek via OpenRouter; local serve `python -m http.server 8873` in `app/`.
