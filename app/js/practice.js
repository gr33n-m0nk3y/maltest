/* Practice engine: question-by-question with prev/random/next navigation,
 * answer persistence, scoring, and rationale display. */
"use strict";
const Practice = (() => {
  const RATE_LABELS = ["Very appropriate", "Somewhat appropriate", "Somewhat inappropriate", "Inappropriate"];
  const RATE_IMPORT = ["Very important", "Important", "Of minor importance", "Not at all important"];

  function esc(s) {
    return String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  }

  function renderQuestion(q) {
    const badges = [];
    if (q.provisional) badges.push('<span class="badge provisional">provisional key</span>');
    if (q.generated) badges.push('<span class="badge generated">AI-GENERATED</span>');
    if (q.topic) badges.push(`<span class="badge topic">${esc(q.topic)}</span>`);
    const badgeHtml = badges.join("");

    let body = "";
    if (q.type === "rank5") {
      body = q.options.map((o, i) => `
        <div class="option" data-i="${i}">
          <span class="letter">${String.fromCharCode(65 + i)}</span>
          <span class="text">${esc(o)}</span>
          <select class="rank" data-i="${i}">
            <option value="">Rank</option>
            ${[1, 2, 3, 4, 5].map((r) => `<option value="${r}">${r}</option>`).join("")}
          </select>
        </div>`).join("");
    } else if (q.type === "mcq3") {
      body = q.options.map((o, i) => `
        <div class="option" data-i="${i}">
          <input type="checkbox" data-i="${i}">
          <span class="letter">${String.fromCharCode(65 + i)}</span>
          <span class="text">${esc(o)}</span>
        </div>`).join("");
    } else if (q.type === "tf") {
      body = q.options.map((o, i) => `
        <div class="option" data-i="${i}">
          <span class="letter">${String.fromCharCode(65 + i)}</span>
          <span class="text">${esc(o)}</span>
          <span style="margin-left:auto;display:flex;gap:8px">
            <label><input type="radio" name="tf${i}" value="T"> True</label>
            <label><input type="radio" name="tf${i}" value="F"> False</label>
          </span>
        </div>`).join("");
    } else if (q.type === "rate") {
      const labels = /importance/i.test(q.scenario) ? RATE_IMPORT : RATE_LABELS;
      body = q.options.map((o, i) => `
        <div class="option" data-i="${i}">
          <span class="letter">${String.fromCharCode(65 + i)}</span>
          <span class="text">${esc(o)}</span>
          <span style="margin-left:auto;display:flex;gap:6px">
            ${[1, 2, 3, 4].map((r) => `<label title="${esc(labels[r - 1])}"><input type="radio" name="rate${i}" value="${r}"> ${r}</label>`).join("")}
          </span>
        </div>`).join("");
    } else if (q.type === "sba") {
      body = q.options.map((o, i) => `
        <div class="option" data-i="${i}">
          <input type="radio" name="sba" value="${String.fromCharCode(65 + i)}">
          <span class="letter">${String.fromCharCode(65 + i)}</span>
          <span class="text">${esc(o)}</span>
        </div>`).join("");
    }

    const checkArea = q.key
      ? `<button id="checkBtn">Check answer</button>`
      : `<span class="badge provisional">Unkeyed question — official key unavailable (provisional keys come later)</span>`;

    return `
      <div class="card">
        <div class="scenario">${esc(q.scenario)}${badgeHtml}</div>
        <div class="instruction">${instruction(q)}</div>
        ${body}
        <div class="controls" id="controls">
          ${checkArea}
        </div>
        <div id="feedback"></div>
      </div>`;
  }

  function instruction(q) {
    switch (q.type) {
      case "rank5": return "Rank in order of appropriateness (1 = most appropriate; 5 = least appropriate). Use each rank once.";
      case "mcq3": return "Choose the THREE most appropriate options.";
      case "tf": return "For each statement, indicate whether it is True or False.";
      case "rate": return "Rate each option (1 = very appropriate/important; 4 = inappropriate/not at all important).";
      case "sba": return "Choose the single best answer.";
    }
  }

  function collectAnswer(q) {
    if (q.type === "rank5") {
      const ranks = {};
      document.querySelectorAll(".rank").forEach((s) => { if (s.value) ranks[s.dataset.i] = parseInt(s.value); });
      if (Object.keys(ranks).length !== 5) return { error: "Assign a rank to all 5 options." };
      const vals = Object.values(ranks);
      if (new Set(vals).size !== 5) return { error: "Each rank (1-5) must be used exactly once." };
      const arr = new Array(5);
      for (const [i, r] of Object.entries(ranks)) arr[r - 1] = String.fromCharCode(65 + parseInt(i));
      return { answer: arr.join("") };
    }
    if (q.type === "mcq3") {
      const chosen = [...document.querySelectorAll('input[type="checkbox"]:checked')].map((c) => String.fromCharCode(65 + parseInt(c.dataset.i)));
      if (chosen.length !== 3) return { error: `Select exactly 3 options (you chose ${chosen.length}).` };
      return { answer: chosen };
    }
    if (q.type === "tf") {
      const ans = [];
      for (let i = 0; i < q.options.length; i++) {
        const r = document.querySelector(`input[name="tf${i}"]:checked`);
        if (!r) return { error: "Answer all statements." };
        ans.push(r.value);
      }
      return { answer: ans };
    }
    if (q.type === "rate") {
      const ans = [];
      for (let i = 0; i < q.options.length; i++) {
        const r = document.querySelector(`input[name="rate${i}"]:checked`);
        if (!r) return { error: "Rate all options." };
        ans.push(parseInt(r.value));
      }
      return { answer: ans };
    }
    if (q.type === "sba") {
      const r = document.querySelector('input[name="sba"]:checked');
      if (!r) return { error: "Select an answer." };
      return { answer: r.value };
    }
    return { error: "Unknown type" };
  }

  function prefill(q, answer) {
    if (q.type === "rank5") {
      answer.split("").forEach((letter, i) => {
        const sel = document.querySelector(`.rank[data-i="${letter.charCodeAt(0) - 65}"]`);
        if (sel) sel.value = String(i + 1);
      });
    } else if (q.type === "mcq3") {
      answer.forEach((letter) => {
        const cb = document.querySelector(`input[type="checkbox"][data-i="${letter.charCodeAt(0) - 65}"]`);
        if (cb) cb.checked = true;
      });
    } else if (q.type === "tf") {
      answer.forEach((v, i) => {
        const r = document.querySelector(`input[name="tf${i}"][value="${v}"]`);
        if (r) r.checked = true;
      });
    } else if (q.type === "rate") {
      answer.forEach((v, i) => {
        const r = document.querySelector(`input[name="rate${i}"][value="${v}"]`);
        if (r) r.checked = true;
      });
    } else if (q.type === "sba") {
      const r = document.querySelector(`input[name="sba"][value="${answer}"]`);
      if (r) r.checked = true;
    }
  }

  function showFeedback(q, result) {
    const fb = document.getElementById("feedback");
    const pct = Math.round((result.score / result.max) * 100);
    const cls = pct >= 60 ? "good" : "bad";
    let html = `<div class="feedback ${cls}">
      <span class="score">${result.score} / ${result.max} (${pct}%)</span>`;
    if (q.type === "rank5") {
      html += `<div class="rationale">Correct order: ${q.key.split("").join(" \u2192 ")}</div>`;
    } else if (q.type === "mcq3") {
      html += `<div class="rationale">Correct: ${q.key.split("").join(", ")}</div>`;
    } else if (q.type === "tf") {
      html += `<div class="rationale">Correct: ${q.key.split("").map((c, i) => `${String.fromCharCode(65 + i)}: ${c === "T" ? "True" : "False"}`).join("; ")}</div>`;
    } else if (q.type === "rate") {
      html += `<div class="rationale">Correct ratings: ${q.key.map((k, i) => `${String.fromCharCode(65 + i)}: ${k}`).join("; ")}</div>`;
    } else if (q.type === "sba") {
      html += `<div class="rationale">Correct: ${q.key}</div>`;
    }
    if (q.explanation) html += `<div class="rationale"><strong>Rationale:</strong> ${esc(q.explanation)}</div>`;
    html += `</div>`;
    fb.innerHTML = html;
  }

  function markOptions(q) {
    if (q.type === "rank5") {
      document.querySelectorAll(".option").forEach((el) => {
        const i = parseInt(el.dataset.i);
        const letter = String.fromCharCode(65 + i);
        const idealPos = q.key.indexOf(letter);
        const sel = [...document.querySelectorAll(".rank")].find((s) => s.dataset.i == i);
        const chosen = sel ? sel.value : "";
        if (chosen && parseInt(chosen) - 1 === idealPos) el.classList.add("correct");
        else if (chosen) el.classList.add("wrong");
      });
    } else if (q.type === "mcq3") {
      document.querySelectorAll('input[type="checkbox"]').forEach((c) => {
        const letter = String.fromCharCode(65 + parseInt(c.dataset.i));
        const el = c.closest(".option");
        if (q.key.includes(letter)) el.classList.add("correct");
        else if (c.checked) el.classList.add("wrong");
      });
    } else if (q.type === "tf") {
      q.options.forEach((_, i) => {
        const el = document.querySelector(`.option[data-i="${i}"]`);
        const chosen = document.querySelector(`input[name="tf${i}"]:checked`);
        if (chosen && chosen.value === q.key[i]) el.classList.add("correct");
        else if (chosen) el.classList.add("wrong");
      });
    } else if (q.type === "rate") {
      q.options.forEach((_, i) => {
        const el = document.querySelector(`.option[data-i="${i}"]`);
        const chosen = document.querySelector(`input[name="rate${i}"]:checked`);
        if (chosen && parseInt(chosen.value) === q.key[i]) el.classList.add("correct");
        else if (chosen) el.classList.add("wrong");
      });
    } else if (q.type === "sba") {
      document.querySelectorAll('input[name="sba"]').forEach((r) => {
        const el = r.closest(".option");
        if (r.value === q.key) el.classList.add("correct");
        else if (r.checked) el.classList.add("wrong");
      });
    }
  }

  function run(container, questions, opts = {}) {
    const allowNav = opts.allowNav !== false;
    const showRandom = opts.showRandom !== false;
    const onFinish = opts.onFinish || (() => {});
    const onQuestion = opts.onQuestion || (() => {});

    let idx = 0;
    let total = 0, max = 0, correct = 0;
    const answers = {};
    const recorded = {};

    function finish() {
      const pct = max ? Math.round((total / max) * 100) : 0;
      const answered = Object.keys(answers).length;
      const detail = max
        ? `${pct}% \u2014 ${correct} of ${questions.length} questions fully correct`
        : `You didn't answer any of the ${questions.length} questions yet \u2014 use Check answer on each one.`;
      container.innerHTML = `
        <div class="card results">
          <div class="big">${total} / ${max}</div>
          <div class="detail">${detail}</div>
          <div class="controls" style="justify-content:center">
            <button onclick="location.reload()">Practice again</button>
          </div>
        </div>`;
      onFinish({ total, max, pct, correct });
    }

    function go(i) {
      if (i < 0) return;
      if (i >= questions.length) { finish(); return; }
      idx = i;
      render();
    }

    // append a Next/Finish button after the check button (needed when nav bar is hidden)
    function addAdvanceButton(isLast) {
      const controls = document.getElementById("controls");
      if (!controls || controls.querySelector("#advanceBtn")) return;
      const nb = document.createElement("button");
      nb.id = "advanceBtn";
      nb.textContent = isLast ? "Finish \u2726" : "Next question \u2192";
      nb.onclick = () => (isLast ? finish() : go(idx + 1));
      controls.appendChild(nb);
    }

    function render() {
      if (questions.length === 0) {
        container.innerHTML = `<div class="card"><p>No questions match.</p></div>`;
        return;
      }
      if (idx >= questions.length) return finish();
      const q = questions[idx];
      const saved = answers[idx];
      const isLast = idx === questions.length - 1;

      const navHtml = allowNav ? `
        <div class="controls" style="margin-top:0">
          <button class="ghost" id="prevBtn" ${idx === 0 ? "disabled" : ""}>\u2190 Previous</button>
          ${showRandom ? `<button class="ghost" id="randBtn">\uD83C\uDFB2 Random</button>` : ""}
          <button class="ghost" id="navNextBtn">${isLast ? "Finish \u2726" : "Next \u2192"}</button>
        </div>` : "";

      container.innerHTML = `
        <div class="progress">Question ${idx + 1} of ${questions.length} \u2014 running score ${total}/${max}</div>
        ${navHtml}
        ${renderQuestion(q)}`;

      if (allowNav) {
        const pb = document.getElementById("prevBtn");
        if (pb) pb.onclick = () => go(idx - 1);
        document.getElementById("navNextBtn").onclick = () => go(idx + 1);
        const rb = document.getElementById("randBtn");
        if (rb) rb.onclick = () => { let r; do { r = Math.floor(Math.random() * questions.length); } while (r === idx && questions.length > 1); go(r); };
      }

      if (saved) {
        prefill(q, saved.answer);
        showFeedback(q, saved.result);
        markOptions(q);
        const cb0 = document.getElementById("checkBtn");
        if (cb0) cb0.disabled = true;
        if (!allowNav) addAdvanceButton(isLast);
        return;
      }

      const cb = document.getElementById("checkBtn");
      if (!cb) { // unkeyed — allow advancing without scoring
        if (!allowNav) addAdvanceButton(isLast);
        return;
      }
      cb.onclick = () => {
        const { answer, error } = collectAnswer(q);
        if (error) { document.getElementById("feedback").innerHTML = `<div class="feedback bad">${esc(error)}</div>`; return; }
        const result = Engine.score(q, answer);
        answers[idx] = { answer, result };
        if (!recorded[idx]) {
          recorded[idx] = true;
          total += result.score; max += result.max;
          if (result.score === result.max) correct++;
          Progress.record(q.id, result.score === result.max);
          onQuestion(q, result);
        }
        showFeedback(q, result);
        markOptions(q);
        cb.disabled = true;
        if (!allowNav) addAdvanceButton(isLast);
      };
    }

    render();
    return { go, restart: () => { idx = 0; render(); } };
  }

  return { run };
})();
