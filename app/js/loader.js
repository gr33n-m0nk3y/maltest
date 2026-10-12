/* Loader: fetch the question bank + merge the user's generated bank + shared helpers. */
"use strict";
const Bank = (() => {
  let _all = null;
  async function load() {
    if (_all) return _all;
    const res = await fetch("data/questions.json");
    const staticBank = await res.json();
    // merge user-generated bank (localStorage) so generated questions appear in practice/mock
    let gen = [];
    try { gen = JSON.parse(localStorage.getItem("maltest_generated_bank")) || []; } catch {}
    const seen = new Set(staticBank.map((q) => q.id));
    const merged = staticBank.concat(gen.filter((q) => !seen.has(q.id)));
    _all = merged;
    return _all;
  }
  function all() { return _all || []; }
  return { load, all };
})();

// localStorage progress: { [qid]: {correct, attempts, lastScore} }
const Progress = (() => {
  const KEY = "maltest_progress";
  function get() { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch { return {}; } }
  function record(qid, correct) {
    const p = get();
    const e = p[qid] || { correct: 0, attempts: 0 };
    e.attempts += 1;
    if (correct) e.correct += 1;
    p[qid] = e;
    localStorage.setItem(KEY, JSON.stringify(p));
  }
  function weakTopics(questions) {
    const p = get();
    const byTopic = {};
    for (const q of questions) {
      const t = q.topic || "untagged";
      const e = p[q.id];
      if (e && e.attempts >= 2) {
        byTopic[t] = byTopic[t] || { correct: 0, attempts: 0 };
        byTopic[t].correct += e.correct;
        byTopic[t].attempts += e.attempts;
      }
    }
    return Object.entries(byTopic)
      .filter(([, v]) => v.correct / v.attempts < 0.6)
      .map(([t]) => t);
  }
  return { get, record, weakTopics };
})();
