/* Malta Foundation Training 1 — scoring engine.
 * Mirrors the official SJT/SJCT scoring conventions:
 *  - rank5: near-miss matrix (ideal rank 1->4 pts ... rank 5->0), no tied ranks
 *  - mcq3 : +4 per correct option (max 12), over-select = question scored 0
 *  - tf   : +2 per correct statement (max 10), both T&F = 0
 *  - rate : exact=4, off-by-1=2, else 0 (approximation; official near-miss unpublished)
 *  - sba  : 1 correct / 0
 */
"use strict";

const Engine = (() => {
  // --- rank5: near-miss matrix ---
  // For ideal rank i (1..5), a candidate placing the option at rank j scores:
  //   |i-j|==0 -> 4, |i-j|==1 -> 3, |i-j|==2 -> 2, |i-j|==3 -> 1, |i-j|==4 -> 0
  function rank5Matrix(idealRank, candidateRank) {
    const d = Math.abs(idealRank - candidateRank);
    return [4, 3, 2, 1, 0][d] ?? 0;
  }

  // ideal: "BADCE" (option at position 0 is rank 1). given: candidate permutation.
  function scoreRank5(ideal, given) {
    if (!ideal || !given || ideal.length !== 5 || given.length !== 5) {
      return { score: 0, max: 20, perOption: [], valid: false };
    }
    const perOption = [];
    let score = 0;
    for (let i = 0; i < 5; i++) {
      const idealRank = i + 1;
      const candRank = given.indexOf(ideal[i]) + 1;
      const pts = rank5Matrix(idealRank, candRank);
      perOption.push({ option: ideal[i], idealRank, candRank, pts });
      score += pts;
    }
    return { score, max: 20, perOption, valid: true };
  }

  // --- mcq3: choose 3 of 8 ---
  function scoreMcq3(key, chosen) {
    const max = 12;
    if (!key || !chosen) return { score: 0, max, valid: false };
    if (chosen.length !== 3) return { score: 0, max, valid: false }; // disqualify
    const keySet = new Set(key.split(""));
    let score = 0;
    for (const c of chosen) if (keySet.has(c)) score += 4;
    return { score, max, valid: true };
  }

  // --- tf: 5 statements, key "FTFTF" ---
  function scoreTf(key, answers) {
    const max = 10;
    if (!key || !answers || key.length !== 5 || answers.length !== 5) {
      return { score: 0, max, valid: false };
    }
    let score = 0;
    for (let i = 0; i < 5; i++) if (key[i] === answers[i]) score += 2;
    return { score, max, valid: true };
  }

  // --- rate: per-option 1-4. key is array of ideal values. ---
  function scoreRate(key, chosen) {
    if (!key || !chosen || key.length !== chosen.length) {
      return { score: 0, max: key ? key.length * 4 : 0, valid: false };
    }
    let score = 0;
    for (let i = 0; i < key.length; i++) {
      const d = Math.abs(key[i] - chosen[i]);
      score += d === 0 ? 4 : d === 1 ? 2 : 0;
    }
    return { score, max: key.length * 4, valid: true };
  }

  // --- sba: single best answer ---
  function scoreSba(key, chosen) {
    return { score: key === chosen ? 1 : 0, max: 1, valid: !!key && !!chosen };
  }

  // --- generic dispatcher ---
  function score(q, answer) {
    switch (q.type) {
      case "rank5": return scoreRank5(q.key, answer);
      case "mcq3":  return scoreMcq3(q.key, answer);
      case "tf":    return scoreTf(q.key, answer);
      case "rate":  return scoreRate(q.key, answer);
      case "sba":   return scoreSba(q.key, answer);
      default:      return { score: 0, max: 0, valid: false };
    }
  }

  // --- mock assembler: Malta format 60 Q / 140 min ---
  // Section A (situational): A1 = 25 rank5, A2 = 15 mcq3
  // Section B (clinical):   B1 = 10 mcq3, B2 = 10 tf
  function buildMock(bank, opts = {}) {
    const durationMin = opts.durationMin || 140;
    // only keyed questions can be scored — exclude unkeyed (provisional) items
    const keyed = (q) => q.key != null && !(typeof q.key === "string" && q.key === "");
    const byType = (t) => bank.filter((q) => q.type === t && keyed(q));
    const pick = (pool, n) => {
      const shuffled = [...pool].sort(() => Math.random() - 0.5);
      return shuffled.slice(0, n);
    };
    const sections = [
      { id: "A1", name: "Situational Judgement — Ranking", type: "rank5", count: 25 },
      { id: "A2", name: "Situational Judgement — MCQ (3 of 8)", type: "mcq3", count: 15 },
      { id: "B1", name: "Situational Clinical — MCQ (3 of 8)", type: "mcq3", count: 10 },
      { id: "B2", name: "Situational Clinical — True/False", type: "tf", count: 10 },
    ];
    const questions = [];
    const used = new Set();
    const shortfall = {};
    for (const s of sections) {
      const pool = byType(s.type).filter((q) => !used.has(q.id));
      const chosen = pick(pool, s.count);
      chosen.forEach((q) => used.add(q.id));
      questions.push(...chosen.map((q) => ({ ...q, _section: s.id })));
      if (chosen.length < s.count) shortfall[s.id] = s.count - chosen.length;
    }
    return { sections, questions, durationMin, shortfall };
  }

  return { scoreRank5, scoreMcq3, scoreTf, scoreRate, scoreSba, score, buildMock };
})();

if (typeof module !== "undefined" && module.exports) module.exports = Engine;
