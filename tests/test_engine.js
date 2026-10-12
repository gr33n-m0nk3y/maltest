/* Engine unit tests — fixtures are the OFFICIAL matrices from the 30-Q paper. */
"use strict";
const E = require("../app/js/engine.js");
let pass = 0, fail = 0;
function eq(name, got, want) {
  if (JSON.stringify(got) === JSON.stringify(want)) { pass++; }
  else { fail++; console.log(`FAIL ${name}: got ${JSON.stringify(got)}, want ${JSON.stringify(want)}`); }
}

// --- rank5: official matrix for ideal BADCE (30-Q Q1) ---
// ideal rank: B=1,A=2,D=3,C=4,E=5
// candidate "BADCE" (exact) -> 20
eq("rank5 exact", E.scoreRank5("BADCE", "BADCE").score, 20);
// candidate "BACDE": B1,A2,C3,D4,E5 -> B4+A4+D3+C3+E4 = 18
eq("rank5 near-miss (swap D/C)", E.scoreRank5("BADCE", "BACDE").score, 18);
// candidate "EDCBA" (reverse): B4,A5,D2,C3,E1 -> 1+1+3+3+0 = 8
eq("rank5 reverse", E.scoreRank5("BADCE", "EDCBA").score, 8);
// candidate "ABCDE": B2,A1,D4,C3,E5 -> 3+3+3+3+4 = 16
eq("rank5 shifted", E.scoreRank5("BADCE", "ABCDE").score, 16);
// max
eq("rank5 max", E.scoreRank5("BADCE", "BADCE").max, 20);
// invalid length
eq("rank5 invalid", E.scoreRank5("BADCE", "BADC").valid, false);

// --- mcq3 ---
eq("mcq3 exact", E.scoreMcq3("BGH", ["B", "G", "H"]).score, 12);
eq("mcq3 partial 2", E.scoreMcq3("BGH", ["B", "G", "A"]).score, 8);
eq("mcq3 partial 1", E.scoreMcq3("BGH", ["B", "A", "C"]).score, 4);
eq("mcq3 none", E.scoreMcq3("BGH", ["A", "C", "D"]).score, 0);
eq("mcq3 over-select -> 0", E.scoreMcq3("BGH", ["B", "G", "H", "A"]).score, 0);
eq("mcq3 under-select -> 0", E.scoreMcq3("BGH", ["B", "G"]).score, 0);
eq("mcq3 max", E.scoreMcq3("BGH", ["B", "G", "H"]).max, 12);

// --- tf ---
eq("tf exact", E.scoreTf("FTFTF", ["F", "T", "F", "T", "F"]).score, 10);
eq("tf partial", E.scoreTf("FTFTF", ["F", "T", "T", "T", "F"]).score, 8);
eq("tf none", E.scoreTf("FTFTF", ["T", "F", "T", "F", "T"]).score, 0);
eq("tf max", E.scoreTf("FTFTF", ["F", "T", "F", "T", "F"]).max, 10);

// --- rate (approximation) ---
eq("rate exact", E.scoreRate([1, 2, 4], [1, 2, 4]).score, 12);
eq("rate off-by-1", E.scoreRate([1, 2, 4], [2, 1, 3]).score, 6);
eq("rate wrong", E.scoreRate([1, 2, 4], [4, 4, 1]).score, 0);
eq("rate max", E.scoreRate([1, 2, 4], [1, 2, 4]).max, 12);

// --- sba ---
eq("sba correct", E.scoreSba("C", "C").score, 1);
eq("sba wrong", E.scoreSba("C", "A").score, 0);

// --- mock assembler ---
const bank = [
  ...Array.from({ length: 30 }, (_, i) => ({ id: `r${i}`, type: "rank5", key: "ABCDE" })),
  ...Array.from({ length: 30 }, (_, i) => ({ id: `m${i}`, type: "mcq3", key: "ABC" })),
  ...Array.from({ length: 12 }, (_, i) => ({ id: `t${i}`, type: "tf", key: "FTFTF" })),
];
const mock = E.buildMock(bank);
const secCounts = {};
mock.questions.forEach((q) => { secCounts[q._section] = (secCounts[q._section] || 0) + 1; });
eq("mock total 60", mock.questions.length, 60);
eq("mock A1=25 rank5", secCounts["A1"], 25);
eq("mock A2=15 mcq3", secCounts["A2"], 15);
eq("mock B1=10 mcq3", secCounts["B1"], 10);
eq("mock B2=10 tf", secCounts["B2"], 10);
eq("mock duration", mock.durationMin, 140);
// no duplicate ids
eq("mock no dupes", new Set(mock.questions.map((q) => q.id)).size, 60);

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
