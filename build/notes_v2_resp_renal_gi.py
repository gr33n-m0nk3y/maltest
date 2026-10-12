# Enhanced notes v2 — respiratory, renal/fluids/electrolytes, GI/hepatology (batch 2).
PART = {
  "shortness-of-breath": {
    "name": "Shortness of breath",
    "group": "Respiratory",
    "overview": "Dyspnoea is the most common acute medical presentation — the exam wants you to pick out the immediately life-threatening causes (PE, tension pneumothorax, severe asthma, pulmonary oedema, anaphylaxis) and treat before you diagnose.",
    "essentials": [
      "Life-threatening causes to exclude first: PE, tension pneumothorax, severe asthma/COPD, acute pulmonary oedema, anaphylaxis, foreign body.",
      "Assess severity: ability to speak in sentences, accessory muscle use, respiratory rate, saturations, ABG. A silent chest in asthma is ominous (no air entry).",
      "Pulmonary oedema (heart failure): orthopnoea, paroxysmal nocturnal dyspnoea, basal crackles, raised JVP, S3 — treat with oxygen, diuretics, nitrates, CPAP.",
      "COPD exacerbation: increased breathlessness, wheeze, sputum change — bronchodilators, steroids, antibiotics if infective, controlled oxygen.",
      "Pneumothorax: sudden pleuritic pain + dyspnoea; tension variant (tracheal shift, haemodynamic compromise) needs immediate needle decompression."
    ],
    "drugs": [
      {"name": "Salbutamol (nebulised)", "when": "Acute asthma / COPD exacerbation", "notes": "2.5-5 mg; titrate; watch for tremor and hypokalaemia"},
      {"name": "Ipratropium (nebulised)", "when": "Acute severe asthma / COPD exacerbation", "notes": "Add to salbutamol; 500 mcg"},
      {"name": "Prednisolone / hydrocortisone", "when": "Asthma/COPD exacerbation", "notes": "Oral prednisolone 40-50 mg (or IV hydrocortisone)"},
      {"name": "Magnesium sulfate", "when": "Severe/life-threatening asthma not responding", "notes": "IV 1.2-2 g over 20 min"},
      {"name": "Furosemide", "when": "Acute pulmonary oedema", "notes": "IV 40-80 mg; monitor urine output and renal function"},
      {"name": "Nitrates (GTN)", "when": "Pulmonary oedema with hypertension", "notes": "IV/oral; avoid if hypotensive"},
      {"name": "Antibiotics", "when": "Infective exacerbation of COPD", "notes": "Per local policy if increased sputum purulence"}
    ],
    "clinicalScenarios": [
      {"scenario": "Sudden pleuritic pain and dyspnoea with unilateral absent breath sounds and tracheal deviation in an unstable patient.", "answer": "Tension pneumothorax — immediate needle decompression (2nd intercostal space, mid-clavicular), then chest drain."},
      {"scenario": "Orthopnoea with bibasal crackles, raised JVP and a third heart sound.", "answer": "Acute pulmonary oedema — oxygen, IV furosemide, nitrates, consider CPAP."},
      {"scenario": "Asthma patient with a silent chest and drowsiness.", "answer": "Near-fatal asthma — call for help, nebulised salbutamol + ipratropium, steroids, IV magnesium; consider ICU."},
      {"scenario": "COPD patient with purulent sputum, increased breathlessness and wheeze.", "answer": "Infective exacerbation — controlled oxygen (88-92%), bronchodilators, steroids, antibiotics."},
      {"scenario": "Elderly patient with sudden dyspnoea, hypoxia and tachycardia after recent surgery.", "answer": "Consider PE — Wells score, CTPA, anticoagulate if high probability."}
    ],
    "keyValues": [
      ["O2 target (COPD/at risk of hypercapnia)", "88-92%"],
      ["O2 target (other acutely ill)", "94-98%"],
      ["Tension pneumothorax decompression", "2nd ICS mid-clavicular line"],
      ["Severe asthma features", "Cannot complete sentences, RR>25, HR>110, PEF<50%"]
    ],
    "redFlags": [
      "Silent chest, exhaustion, or reduced consciousness in asthma — peri-arrest.",
      "Tension pneumothorax — decompress immediately, do not wait for X-ray.",
      "Hypoxia refractory to oxygen — think PE, shunt, or severe disease."
    ],
    "management": [
      "ABC, target oxygen, sit the patient up, IV access, monitoring.",
      "Asthma: salbutamol, ipratropium, steroids, magnesium; escalate if severe.",
      "Pulmonary oedema: furosemide, nitrates, CPAP, treat the cause.",
      "Pneumothorax: aspirate or drain per size/clinical state; tension → decompress first."
    ],
    "pitfalls": [
      "Do not give uncontrolled high-flow oxygen to a COPD patient at risk of hypercapnia.",
      "A normal chest X-ray does not exclude PE — go on to CTPA if clinical suspicion is high.",
      "In tension pneumothorax, treat clinically — imaging would delay life-saving decompression."
    ]
  },

  "oxygen-management": {
    "name": "Oxygen management in wards",
    "group": "Respiratory",
    "overview": "Oxygen is a drug: it needs a prescribed target, an appropriate device, and monitoring. The exam tests the two targets (94-98% vs 88-92%) and the danger of over-oxygenating COPD.",
    "essentials": [
      "Prescribe oxygen with a target saturation range, not 'as required'. Over-oxygenation in COPD can suppress the hypoxic drive and cause hypercapnia.",
      "Targets: 94-98% for most acutely ill patients; 88-92% for those at risk of hypercapnic respiratory failure (COPD, obesity hypoventilation, neuromuscular disease).",
      "Delivery devices: nasal cannulae (low flow), simple face mask, Venturi mask (precise FiO2, 24-60%), non-rebreathe mask (high flow ~15 L/min) for emergencies.",
      "Monitor the response: saturations and ABG if hypercapnia is suspected or the target is not met. Reassess regularly.",
      "Document the prescription, target range, device, and a weaning plan; escalate if saturations fall below target."
    ],
    "drugs": [
      {"name": "Oxygen (nasal cannulae)", "when": "Mild hypoxia, stable patient", "notes": "1-6 L/min; ~24-44% FiO2 (variable)"},
      {"name": "Venturi mask", "when": "Precise FiO2 needed (e.g. COPD)", "notes": "24%, 28%, 35%, 40%, 60% — controlled delivery"},
      {"name": "Non-rebreathe mask", "when": "Emergency / severe hypoxia", "notes": "15 L/min, ~85-95% FiO2; humidify if prolonged"},
      {"name": "NIV (BiPAP/CPAP)", "when": "Hypercapnic respiratory failure (COPD) or type 2 failure", "notes": "Consider if pH<7.35 and PaCO2 high; strict monitoring"}
    ],
    "clinicalScenarios": [
      {"scenario": "Known COPD with an exacerbation, saturations 90% on air.", "answer": "Controlled oxygen to 88-92% via Venturi mask; recheck ABG (risk of CO2 retention)."},
      {"scenario": "A healthy 30-year-old with pneumonia and saturations 90%.", "answer": "Target 94-98%; titrate oxygen and treat the pneumonia; check ABG if not improving."},
      {"scenario": "COPD patient on high-flow oxygen becomes drowsy with a rising PaCO2.", "answer": "Reduce FiO2 to target 88-92%, check ABG, consider NIV — this is hypercapnic respiratory failure."},
      {"scenario": "Saturations 85% despite a non-rebreathe mask at 15 L/min.", "answer": "Refractory hypoxia — call for help, ABG, look for the cause (PE, pneumothorax, oedema, shunt)."}
    ],
    "keyValues": [
      ["Normal target", "94-98%"],
      ["COPD/at-risk target", "88-92%"],
      ["Non-rebreathe mask", "15 L/min (~85-95% FiO2)"],
      ["Venturi mask", "Precise FiO2 24-60%"]
    ],
    "redFlags": [
      "Falling saturations despite high-flow oxygen — call for help, consider ABG.",
      "Rising CO2 or drowsiness in COPD on oxygen — reduce FiO2, consider NIV.",
      "Hypoxia with no improvement — look for the cause rather than simply increasing flow."
    ],
    "management": [
      "Prescribe oxygen with a target range and device.",
      "Start at an appropriate FiO2 and titrate to target; monitor saturations.",
      "Check ABG if hypercapnia risk or the target is not achieved.",
      "Wean oxygen as the patient improves; document the plan."
    ],
    "pitfalls": [
      "'Oxygen as required' is not a prescription — always state a target range and device.",
      "Beware over-oxygenation in COPD — high flow can cause dangerous CO2 retention.",
      "Do not delay NIV in hypercapnic respiratory failure while waiting for a repeat ABG."
    ]
  },

  "abg-interpretation": {
    "name": "Arterial blood gas interpretation",
    "group": "Respiratory",
    "overview": "ABGs are examined constantly — the exam expects a systematic read (oxygenation → pH → PaCO2 → HCO3 → compensation) and matching the pattern to a cause.",
    "essentials": [
      "Systematic approach: (1) oxygenation (PaO2), (2) pH (acidaemia/alkalaemia), (3) PaCO2 (respiratory), (4) HCO3 (metabolic), (5) compensation.",
      "Respiratory acidosis: high PaCO2 (hypoventilation — COPD, sedation, neuromuscular). Respiratory alkalosis: low PaCO2 (hyperventilation — pain, anxiety, PE, sepsis).",
      "Metabolic acidosis: low HCO3 — anion gap (lactate, ketoacidosis, renal failure, toxins) vs non-anion gap (diarrhoea, renal tubular acidosis).",
      "Metabolic alkalosis: high HCO3 (vomiting, diuretics, hypokalaemia).",
      "Compensation: respiratory compensates metabolic quickly (change in PaCO2); metabolic compensates respiratory slowly (change in HCO3). Check whether compensation is adequate."
    ],
    "drugs": [
      {"name": "Oxygen", "when": "Hypoxaemia on the ABG", "notes": "Titrate to target; beware CO2 retention in COPD"},
      {"name": "Naloxone", "when": "Opioid-induced respiratory acidosis", "notes": "IV; reverses sedation/hypoventilation"},
      {"name": "NIV (BiPAP)", "when": "Hypercapnic respiratory acidosis from COPD", "notes": "Reduces PaCO2 and work of breathing; monitor closely"},
      {"name": "Sodium bicarbonate", "when": "Severe metabolic acidosis (selected, specialist)", "notes": "Reserved for e.g. TCA toxicity or severe acidaemia; not routine"}
    ],
    "clinicalScenarios": [
      {"scenario": "pH 7.28, PaCO2 8.0 kPa, HCO3 24.", "answer": "Respiratory acidosis (hypoventilation) — improve ventilation, treat the cause."},
      {"scenario": "pH 7.30, PaCO2 3.5 kPa, HCO3 12, lactate 6.", "answer": "High anion-gap metabolic acidosis (lactic acidosis) — look for sepsis/ischaemia, resuscitate."},
      {"scenario": "pH 7.48, PaCO2 3.0 kPa, HCO3 24 in an anxious patient with a PE.", "answer": "Respiratory alkalosis (hyperventilation) — treat the underlying cause (PE, pain, sepsis)."},
      {"scenario": "pH 7.50, HCO3 32 in a patient who has been vomiting.", "answer": "Metabolic alkalosis — replace fluids/electrolytes, treat the cause."},
      {"scenario": "pH 7.20, PaCO2 6.5, HCO3 18 in a COPD patient.", "answer": "Decompensated respiratory acidosis — consider NIV, controlled oxygen; this is type 2 respiratory failure."}
    ],
    "keyValues": [
      ["Normal pH", "7.35-7.45"],
      ["Normal PaCO2", "4.7-6.0 kPa (35-45 mmHg)"],
      ["Normal HCO3", "22-26 mmol/L"],
      ["Normal PaO2 (on air)", "10-13 kPa"],
      ["Anion gap", "Na - (Cl + HCO3); normal 8-12"]
    ],
    "redFlags": [
      "pH < 7.2 — severe acidaemia, consider ICU/bicarbonate.",
      "Lactic acidosis (lactate >4) — sepsis/ischaemia, treat the cause.",
      "Rising PaCO2 with falling pH in COPD — hypercapnic respiratory failure, consider NIV."
    ],
    "management": [
      "Interpret systematically: oxygenation → pH → PaCO2 → HCO3 → compensation.",
      "Treat the underlying cause, not just the numbers.",
      "Respiratory acidosis: improve ventilation (bronchodilators, NIV, treat cause).",
      "Metabolic acidosis: identify the anion gap and treat the cause (fluids, insulin for DKA, sepsis)."
    ],
    "pitfalls": [
      "Always check compensation — a normal pH can hide a mixed picture.",
      "Calculate the anion gap in every metabolic acidosis — it points to the cause.",
      "A normal PaO2 on oxygen can mask severe disease — interpret in context of FiO2."
    ]
  },

  "electrolytes": {
    "name": "Electrolyte management",
    "group": "Renal, fluids & electrolytes",
    "overview": "Electrolyte emergencies (especially hypo/hyperkalaemia) cause arrhythmias and arrest. The exam tests safe correction — rate of change matters as much as the target.",
    "essentials": [
      "Sodium: hyponatraemia (common) — assess volume status and osmolality; causes include SIADH, hypovolaemia, heart failure, adrenal insufficiency. Correct slowly (risk of osmotic demyelination). Hypernatraemia = water deficit.",
      "Potassium: hypokalaemia (diuretics, vomiting, diarrhoea) risks arrhythmia — replace. Hyperkalaemia (renal failure, ACEi, K+-sparing diuretics, cell lysis) is a cardiac emergency.",
      "Calcium: hypercalcaemia (malignancy, hyperparathyroidism) — hydrate + bisphosphonate. Hypocalcaemia (post-thyroidectomy, hypoparathyroidism) — tetany, Chvostek/Trousseau signs.",
      "Magnesium: hypomagnesaemia (diuretics, alcohol) associates with hypokalaemia/hypocalcaemia and arrhythmia; hypermagnesaemia occurs in renal failure.",
      "Phosphate: hypophosphataemia (refeeding, dialysis) causes muscle weakness and rhabdomyolysis."
    ],
    "drugs": [
      {"name": "Calcium gluconate 10%", "when": "Hyperkalaemia with ECG changes (cardiac protection)", "notes": "IV 10-30 mL; stabilises myocardium but does not lower K+"},
      {"name": "Insulin + dextrose", "when": "Hyperkalaemia", "notes": "Shifts K+ into cells; monitor glucose closely"},
      {"name": "Salbutamol (nebulised)", "when": "Hyperkalaemia (adjunct)", "notes": "Shifts K+ intracellularly"},
      {"name": "Potassium chloride", "when": "Hypokalaemia", "notes": "Oral or IV (max 10 mmol/h peripherally, 20 mmol/h central with monitoring)"},
      {"name": "Spironolactone / furosemide", "when": "Fluid overload with electrolytes", "notes": "K+-sparing vs K+-wasting — choose to correct the K+"},
      {"name": "IV fluids / bisphosphonate", "when": "Hypercalcaemia", "notes": "Aggressive saline + zoledronic acid/pamidronate"},
      {"name": "Magnesium sulfate", "when": "Hypomagnesaemia", "notes": "IV; often needed alongside K+ replacement"}
    ],
    "clinicalScenarios": [
      {"scenario": "K+ 7.0 with peaked T waves on ECG.", "answer": "Hyperkalaemia emergency — calcium gluconate (myocardial protection), insulin+dextrose, salbutamol, then removal (resonium/dialysis)."},
      {"scenario": "K+ 2.8 on a thiazide diuretic.", "answer": "Hypokalaemia — replace K+ (oral/IV) and review the diuretic; check Mg2+."},
      {"scenario": "Na+ 118 with confusion and seizures.", "answer": "Severe hyponatraemia — hypertonic saline for seizures, but correct slowly (≤8-10 mmol/L/24 h) to avoid osmotic demyelination."},
      {"scenario": "Post-thyroidectomy patient with tingling and muscle twitching.", "answer": "Hypocalcaemia — IV calcium gluconate; check corrected calcium, magnesium and PTH."},
      {"scenario": "Malignancy patient with confusion, thirst and a calcium of 3.2 mmol/L.", "answer": "Hypercalcaemia — IV fluids then a bisphosphonate; treat the underlying malignancy."}
    ],
    "keyValues": [
      ["Normal Na", "135-145 mmol/L"],
      ["Normal K", "3.5-5.0 mmol/L"],
      ["Hyperkalaemia emergency", "K >6.5 or ECG changes"],
      ["Hyponatraemia correction rate", "≤8-10 mmol/L per 24 h"],
      ["Normal corrected calcium", "2.2-2.6 mmol/L"]
    ],
    "redFlags": [
      "Hyperkalaemia with ECG changes (peaked T, wide QRS) — treat immediately.",
      "Severe hyponatraemia with seizures — hypertonic saline, but correct slowly.",
      "Symptomatic hypocalcaemia (tetany, laryngospasm) — IV calcium."
    ],
    "management": [
      "Hyperkalaemia: calcium gluconate (protection), insulin+dextrose, salbutamol, then K+ removal.",
      "Hypokalaemia: oral/IV potassium replacement and treat the cause; check magnesium.",
      "Hyponatraemia: treat the cause and correct slowly with frequent monitoring.",
      "Hypercalcaemia: IV fluids, bisphosphonate, treat malignancy."
    ],
    "pitfalls": [
      "Calcium gluconate protects the heart but does not lower potassium — always follow with a shifting/removal strategy.",
      "Correcting hyponatraemia too fast causes osmotic demyelination — go slowly.",
      "Always check magnesium when treating hypokalaemia — low Mg2+ makes K+ hard to correct."
    ]
  },

  "low-urine-output": {
    "name": "Low urine output",
    "group": "Renal, fluids & electrolytes",
    "overview": "Oliguria is a common ward call and often reversible. The exam tests classifying AKI (pre-renal / intrinsic / post-renal) and the safe first step.",
    "essentials": [
      "Oliguria = urine output <0.5 mL/kg/h (or <400 mL/24h). Anuria (<100 mL/24h) suggests obstruction or severe renal failure.",
      "Classify AKI: pre-renal (hypovolaemia, sepsis, heart failure — most common), intrinsic renal (ATN, glomerulonephritis, interstitial nephritis), post-renal (obstruction — catheter, prostate, stones).",
      "Assess: fluid balance, weight, JVP, BP, urine output, urinalysis, U&Es, creatinine; renal USS for obstruction.",
      "Pre-renal AKI responds to fluid resuscitation; intrinsic/post-renal need specific treatment. Watch for hyperkalaemia, acidosis and fluid overload.",
      "Prevent: adequate hydration, avoid nephrotoxins (NSAIDs, ACEi in dehydration, contrast), monitor high-risk patients."
    ],
    "drugs": [
      {"name": "IV crystalloid", "when": "Pre-renal (hypovolaemic) AKI", "notes": "Balanced crystalloid boluses, reassess after each"},
      {"name": "Furosemide", "when": "Fluid overload with AKI (not for pre-renal oliguria)", "notes": "Does not treat AKI itself; avoid in hypovolaemia"},
      {"name": "Stop nephrotoxins", "when": "Any AKI", "notes": "NSAIDs, ACEi/ARB, aminoglycosides, contrast"},
      {"name": "Catheterisation", "when": "Suspected bladder outlet obstruction", "notes": "Relieves post-renal AKI; monitor for post-obstructive diuresis"},
      {"name": "Treatment of hyperkalaemia", "when": "AKI with raised K+", "notes": "Calcium gluconate, insulin+dextrose — see electrolytes"}
    ],
    "clinicalScenarios": [
      {"scenario": "Post-operative patient with urine output 0.2 mL/kg/h, tachycardic and hypotensive with dry mucous membranes.", "answer": "Pre-renal AKI — IV fluid challenge and reassess; do not give diuretics."},
      {"scenario": "Anuria after pelvic surgery.", "answer": "Check the catheter (blockage) and do a renal USS for obstruction; assess renal function."},
      {"scenario": "Rising creatinine with a nephrotoxic drug started recently.", "answer": "Intrinsic AKI — stop the nephrotoxin (e.g. NSAID, aminoglycoside), monitor U&Es."},
      {"scenario": "Enlarged prostate with chronic retention and renal impairment.", "answer": "Post-renal AKI — catheterise urgently, monitor for post-obstructive diuresis."},
      {"scenario": "AKI with K+ 6.8 and pulmonary oedema.", "answer": "Refractory AKI with hyperkalaemia/overload — consider urgent dialysis; involve renal team."}
    ],
    "keyValues": [
      ["Oliguria", "<0.5 mL/kg/h"],
      ["Anuria", "<100 mL/24h"],
      ["AKI (KDIGO)", "Cr rise ≥26.5 µmol/L in 48 h or 1.5× baseline"],
      ["Urine output target", "≥0.5 mL/kg/h"]
    ],
    "redFlags": [
      "Anuria — think obstruction, needs urgent renal USS + catheter.",
      "Hyperkalaemia or severe acidosis in AKI — may need dialysis.",
      "Pulmonary oedema from fluid overload — stop fluids, diurese."
    ],
    "management": [
      "Assess volume status; fluid challenge if hypovolaemic (pre-renal).",
      "Catheterise to measure output accurately and exclude obstruction.",
      "Stop nephrotoxins, treat the cause, monitor U&Es and output.",
      "Escalate for dialysis if refractory hyperkalaemia, acidosis, or overload."
    ],
    "pitfalls": [
      "Do not give furosemide for oliguria from hypovolaemia — it worsens pre-renal AKI.",
      "Anuria is not 'low output' — it suggests obstruction and needs urgent action.",
      "A 'normal' creatinine can hide significant AKI in low-muscle-mass patients — use trends."
    ]
  },

  "iv-fluids": {
    "name": "Intravenous fluid prescription",
    "group": "Renal, fluids & electrolytes",
    "overview": "IV fluids are drugs with indications, doses and harms. The exam tests assessing the patient's fluid status first, then choosing the right fluid and monitoring.",
    "essentials": [
      "Prescribe IV fluids like a drug: assess fluid status (hypovolaemic, euvolaemic, overloaded), then choose fluid, rate and monitoring.",
      "Crystalloids are first-line: balanced solutions (Hartmann's, Plasma-Lyte) preferred over 0.9% saline (which can cause hyperchloraemic acidosis). Dextrose is for water replacement.",
      "Maintenance: ~25-30 mL/kg/day water with Na+ and K+ (~1 mmol/kg/day each). Adjust for losses (vomiting, diarrhoea, drains, fever).",
      "Resuscitation: rapid boluses (250-500 mL) for hypovolaemia/shock, reassess after each. Avoid over-resuscitation.",
      "Monitor: fluid balance, weight, urine output, U&Es and clinical signs; reassess daily and stop when no longer needed."
    ],
    "drugs": [
      {"name": "Hartmann's / balanced crystalloid", "when": "Resuscitation and maintenance (first-line)", "notes": "Closest to plasma; avoids hyperchloraemic acidosis"},
      {"name": "0.9% sodium chloride", "when": "Resuscitation; when a balanced solution is unavailable; with blood products", "notes": "Large volumes cause hyperchloraemic acidosis"},
      {"name": "5% dextrose", "when": "Free water replacement / maintenance", "notes": "Poor resuscitation fluid (distributes across all compartments)"},
      {"name": "Potassium chloride (in fluids)", "when": "Maintenance with hypokalaemia", "notes": "Add per renal function; max rates apply"},
      {"name": "4% albumin / colloid", "when": "Selected cases (e.g. SBP, large-volume paracentesis)", "notes": "Not routine for resuscitation"}
    ],
    "clinicalScenarios": [
      {"scenario": "Hypovolaemic patient needing resuscitation — which fluid first?", "answer": "Balanced crystalloid (Hartmann's) boluses, reassessing after each."},
      {"scenario": "Adult needing maintenance fluids.", "answer": "~25-30 mL/kg/day water with ~1 mmol/kg/day Na+ and K+; use a balanced solution."},
      {"scenario": "Patient with heart failure becoming breathless after IV fluids.", "answer": "Fluid overload — stop fluids, consider diuresis; reassess the plan and weight."},
      {"scenario": "Large-volume paracentesis for ascites.", "answer": "Give IV albumin alongside to prevent circulatory dysfunction."}
    ],
    "keyValues": [
      ["Maintenance water", "25-30 mL/kg/day"],
      ["Maintenance Na+/K+", "~1 mmol/kg/day each"],
      ["Resuscitation bolus", "250-500 mL, reassess"],
      ["First-line fluid", "Balanced crystalloid (Hartmann's)"]
    ],
    "redFlags": [
      "Signs of fluid overload (pulmonary oedema, raised JVP) — stop fluids, diurese.",
      "Hypovolaemic shock — rapid resuscitation, not slow maintenance.",
      "Heart or renal failure — fluids can worsen; be cautious and reassess."
    ],
    "management": [
      "Assess volume status; prescribe a clear plan (resuscitation vs maintenance vs replacement).",
      "Choose balanced crystalloid; add K+ as needed (check renal function).",
      "Monitor fluid balance, weight and U&Es; reassess daily.",
      "Stop IV fluids as soon as the patient can drink."
    ],
    "pitfalls": [
      "Never prescribe '1 L over 24 h' for a shocked patient — resuscitation is bolus-based.",
      "Large volumes of 0.9% saline cause hyperchloraemic acidosis — prefer balanced solutions.",
      "Always reassess after each bolus rather than following a fixed prescription."
    ]
  },

  "gi-bleeds": {
    "name": "Gastrointestinal bleeds",
    "group": "Gastrointestinal & hepatology",
    "overview": "A major GI bleed is a resuscitation first, diagnosis second. The exam tests recognising the severity, resuscitating, and differentiating upper (variceal) from lower bleeding.",
    "essentials": [
      "Upper GI bleed (haematemesis, melaena): peptic ulcer, varices (cirrhosis), Mallory-Weiss tear, gastritis. Lower GI bleed (fresh PR): diverticular, angiodysplasia, colorectal cancer, haemorrhoids.",
      "Assess severity: haemodynamic status, Hb drop, shock. Melaena + compromise = significant upper GI bleed.",
      "Resuscitate first: 2 large-bore IVs, bloods (FBC, U&E, LFT, crossmatch), fluids/blood, correct coagulopathy. Consider tranexamic acid.",
      "Upper GI: urgent endoscopy (within 24 h; within 1 h for variceal/severe). Variceal bleed: terlipressin + antibiotics + endoscopic banding.",
      "Risk scores (Glasgow-Blatchford, Rockall) guide admission and endoscopy timing; re-bleeding escalates to repeat endoscopy/IR/surgery."
    ],
    "drugs": [
      {"name": "Terlipressin", "when": "Suspected variceal bleed (cirrhosis)", "notes": "IV; reduces portal pressure; watch for ischaemia/hyponatraemia"},
      {"name": "Prophylactic antibiotics", "when": "Variceal bleed / cirrhosis with GI bleed", "notes": "Reduces mortality and re-bleeding; per local policy"},
      {"name": "Proton pump inhibitor (IV)", "when": "Non-variceal upper GI bleed / after endoscopic therapy", "notes": "IV omeprazole/esomeprazole"},
      {"name": "Tranexamic acid", "when": "Significant GI bleeding (selected)", "notes": "Consider early; per local policy"},
      {"name": "Blood products", "when": "Haemodynamic compromise / significant Hb drop", "notes": "Restrictive transfusion (Hb <70-80 g/L) unless cardiac"},
      {"name": "Vitamin K / PCC", "when": "Coagulopathy or anticoagulation", "notes": "Reverse if bleeding"}
    ],
    "clinicalScenarios": [
      {"scenario": "Cirrhotic patient with haematemesis, tachycardic and hypotensive.", "answer": "Variceal bleed — resuscitate, terlipressin + antibiotics, urgent endoscopy for banding."},
      {"scenario": "Melaena with haemodynamic compromise.", "answer": "Significant upper GI bleed — IV access, bloods/crossmatch, fluids/blood, then urgent endoscopy."},
      {"scenario": "Patient on warfarin with a GI bleed and INR 4.", "answer": "Reverse with IV vitamin K + PCC while resuscitating; urgent endoscopy."},
      {"scenario": "Fresh PR bleeding in a stable 55-year-old.", "answer": "Lower GI bleed — resuscitate, identify source (colonoscopy/CT), treat the cause."},
      {"scenario": "Re-bleeding after endoscopic therapy.", "answer": "Escalate — repeat endoscopy, consider IR embolisation or surgery."}
    ],
    "keyValues": [
      ["Glasgow-Blatchford", "≥1 → endoscopy; high score → urgent"],
      ["Variceal bleed treatment", "Terlipressin + antibiotics + banding"],
      ["Endoscopy timing", "Within 24 h (1 h if variceal/severe)"],
      ["Transfusion trigger", "Hb <70-80 g/L (higher if cardiac)"]
    ],
    "redFlags": [
      "Haematemesis with shock — massive bleed, resuscitate aggressively.",
      "Variceal bleed in cirrhosis — high mortality, terlipressin + antibiotics urgently.",
      "Re-bleeding after endoscopy — escalate."
    ],
    "management": [
      "ABC, two large-bore IVs, bloods + crossmatch, fluids/blood, correct coagulopathy.",
      "Upper GI: urgent endoscopy; variceal → terlipressin + antibiotics + banding.",
      "Lower GI: resuscitate, identify source (colonoscopy/CT), treat the cause.",
      "Monitor Hb and haemodynamics; repeat endoscopy if re-bleeding."
    ],
    "pitfalls": [
      "Do not scope an unstable patient — resuscitate first.",
      "A normal Hb early in a bleed is misleading — it falls with fluid resuscitation.",
      "In cirrhosis, always consider variceal bleeding and give antibiotics — not just a PPI."
    ]
  },

  "hepatic-encephalopathy": {
    "name": "Hepatic encephalopathy",
    "group": "Gastrointestinal & hepatology",
    "overview": "A neuropsychiatric syndrome of liver failure driven by ammonia and other toxins. The exam tests finding the precipitants — treating them is the priority.",
    "essentials": [
      "Neuropsychiatric syndrome in liver failure due to accumulation of ammonia and other toxins (impaired hepatic clearance).",
      "Precipitants: GI bleed, infection, constipation, electrolyte disturbance, sedatives, dehydration, high protein load, portosystemic shunting.",
      "Grading (West Haven): I mild confusion/altered sleep, II lethargy/disorientation, III somnolent but rousable, IV coma.",
      "Clinical: altered consciousness, asterixis (flapping tremor), confusion, personality change, fetor hepaticus.",
      "Exclude other causes of confusion (hypoglycaemia, sepsis, intracranial bleed, Wernicke's) — never assume HH is the whole story."
    ],
    "drugs": [
      {"name": "Lactulose", "when": "Hepatic encephalopathy (first-line)", "notes": "Oral/enema; titrate to 2-3 soft stools/day; reduces ammonia via the gut"},
      {"name": "Rifaximin", "when": "Recurrent/chronic encephalopathy (add-on)", "notes": "Non-absorbed antibiotic reducing ammonia-producing gut flora"},
      {"name": "Avoid sedatives", "when": "All encephalopathy", "notes": "Benzodiazepines/opiates worsen it"},
      {"name": "Treat the precipitant", "when": "Always", "notes": "Antibiotics for SBP, terlipressin for varices, correct electrolytes"}
    ],
    "clinicalScenarios": [
      {"scenario": "Cirrhotic patient becomes confused and asterixic after a GI bleed.", "answer": "Hepatic encephalopathy precipitated by the bleed — lactulose + treat the bleed (terlipressin, antibiotics, banding)."},
      {"scenario": "Grade IV encephalopathy (coma) in liver failure.", "answer": "Airway protection, ICU, lactulose/rifaximin, treat the precipitant; consider liver unit transfer."},
      {"scenario": "New confusion in cirrhosis with no obvious cause.", "answer": "Screen for precipitants — infection (SBP), GI bleed, constipation, electrolytes, drugs."},
      {"scenario": "Confusion in a malnourished alcoholic patient.", "answer": "Consider Wernicke's encephalopathy — give parenteral thiamine before glucose; also check for other causes."}
    ],
    "keyValues": [
      ["Ammonia", "Elevated in hepatic encephalopathy"],
      ["Lactulose", "First-line; titrate to 2-3 stools/day"],
      ["Rifaximin", "Add-on for recurrent encephalopathy"],
      ["West Haven grade", "I-IV (I mild confusion → IV coma)"]
    ],
    "redFlags": [
      "Grade III-IV encephalopathy — airway protection, ICU.",
      "New confusion in cirrhosis — always exclude GI bleed, sepsis and hypoglycaemia.",
      "Deterioration despite treatment — re-evaluate for precipitants."
    ],
    "management": [
      "Treat the precipitant (bleed, infection, constipation, electrolytes).",
      "Lactulose (oral/enema); add rifaximin if recurrent.",
      "Correct electrolytes, avoid sedatives and a high protein load acutely.",
      "Exclude other causes of altered consciousness."
    ],
    "pitfalls": [
      "Never sedate a confused cirrhotic patient — it worsens encephalopathy.",
      "Encephalopathy is a diagnosis of exclusion — always look for a precipitant.",
      "Give thiamine before glucose in at-risk patients (Wernicke's)."
    ]
  },

  "ascites": {
    "name": "Ascites",
    "group": "Gastrointestinal & hepatology",
    "overview": "Ascites usually reflects portal hypertension (cirrhosis). The exam tests diagnostic paracentesis (SAAG, SBP) and the diuretic/paracentesis strategy.",
    "essentials": [
      "Ascites = peritoneal fluid accumulation. Most commonly portal hypertension (cirrhosis); other causes: malignancy, heart failure, nephrotic syndrome, TB, pancreatitis.",
      "Diagnosis: clinical (shifting dullness, fluid thrill), USS, diagnostic paracentesis.",
      "SAAG (serum-ascites albumin gradient): ≥11 g/L indicates portal hypertension; <11 g/L suggests another cause (malignancy, TB, pancreatitis).",
      "Cirrhotic ascites: sodium restriction, spironolactone (aldosterone antagonist) ± furosemide. Large-volume paracentesis with albumin for tense ascites.",
      "Complications: SBP (fever, abdominal pain, rising WCC), refractory ascites, hepatorenal syndrome."
    ],
    "drugs": [
      {"name": "Spironolactone", "when": "Cirrhotic ascites (first-line diuretic)", "notes": "Start 100 mg; titrate; watch for hyperkalaemia and renal impairment"},
      {"name": "Furosemide", "when": "Add-on to spironolactone", "notes": "Usually 40 mg; monitor U&Es and weight"},
      {"name": "IV albumin", "when": "Large-volume paracentesis / SBP", "notes": "Prevents circulatory dysfunction; 20% albumin"},
      {"name": "IV antibiotics (cefotaxime)", "when": "Spontaneous bacterial peritonitis", "notes": "With albumin; per local policy"},
      {"name": "Vasoconstrictors (terlipressin)", "when": "Hepatorenal syndrome (specialist)", "notes": "With albumin; specialist use"}
    ],
    "clinicalScenarios": [
      {"scenario": "Cirrhotic patient with ascites develops fever and abdominal pain; ascitic neutrophils 400/mm3.", "answer": "SBP — IV cefotaxime + albumin; secondary prophylaxis afterwards."},
      {"scenario": "Tense ascites causing respiratory compromise.", "answer": "Large-volume paracentesis with IV albumin."},
      {"scenario": "New ascites in a patient with known malignancy.", "answer": "Consider malignant ascites — diagnostic paracentesis with cytology; SAAG <11 g/L."},
      {"scenario": "Cirrhotic ascites not responding to spironolactone/furosemide.", "answer": "Refractory ascites — consider regular paracentesis, TIPS assessment, or transplant referral."}
    ],
    "keyValues": [
      ["SAAG", "≥11 g/L = portal hypertension"],
      ["SBP diagnosis", "Ascitic neutrophils >250/mm3"],
      ["SBP treatment", "IV cefotaxime + albumin"],
      ["First-line diuretic", "Spironolactone"]
    ],
    "redFlags": [
      "Fever/abdominal pain with ascites — SBP, urgent paracentesis + antibiotics.",
      "Rising creatinine with ascites — hepatorenal syndrome.",
      "Tense ascites with respiratory compromise — therapeutic paracentesis + albumin."
    ],
    "management": [
      "Diagnostic paracentesis: SAAG, cell count, culture, albumin.",
      "Cirrhotic ascites: sodium restriction, spironolactone ± furosemide.",
      "Tense ascites: large-volume paracentesis with IV albumin.",
      "SBP: IV antibiotics + albumin; treat the underlying liver disease."
    ],
    "pitfalls": [
      "Always do a diagnostic paracentesis — SBP can be subtle and is easily missed.",
      "Do not drain large volumes without albumin — risk of circulatory collapse.",
      "Ascites in cirrhosis is not 'just third-spacing' — it signals advanced disease and complications."
    ]
  },

  "jaundice": {
    "name": "Jaundice",
    "group": "Gastrointestinal & hepatology",
    "overview": "Jaundice is classified pre-hepatic, hepatic or post-hepatic, and the pattern of LFTs points to the cause. The exam tests spotting obstructive jaundice and the cholangitis emergency.",
    "essentials": [
      "Jaundice = yellow discolouration from hyperbilirubinaemia. Classify: pre-hepatic (haemolysis — unconjugated), hepatic (hepatocellular — mixed), post-hepatic (obstructive — conjugated).",
      "Pre-hepatic: haemolysis (raised unconjugated bilirubin, normal LFTs, reticulocytosis).",
      "Hepatic: viral hepatitis, alcohol, drugs, autoimmune, cirrhosis — raised transaminases (ALT/AST).",
      "Post-hepatic/obstructive: gallstones, malignancy (pancreatic head), stricture — raised ALP/GGT, conjugated bilirubin, pale stools, dark urine.",
      "Investigations: LFTs, bilirubin (total/conjugated), FBC, USS (biliary dilatation), viral serology, autoimmune screen."
    ],
    "drugs": [
      {"name": "IV antibiotics", "when": "Cholangitis", "notes": "Broad-spectrum per local policy; then urgent biliary drainage"},
      {"name": "Vitamin K", "when": "Obstructive jaundice with coagulopathy", "notes": "Fat-soluble vitamin malabsorption — correct before procedures"},
      {"name": "Analgesia (avoid hepatotoxic)", "when": "Biliary colic", "notes": "NSAIDs/paracetamol per liver function; avoid opioids that worsen spasm (pethidine debated)"},
      {"name": "Ursodeoxycholic acid", "when": "Selected cholestatic conditions", "notes": "Specialist; e.g. primary biliary cholangitis"}
    ],
    "clinicalScenarios": [
      {"scenario": "Jaundice with pale stools, dark urine, raised ALP/GGT and dilated ducts on USS.", "answer": "Obstructive jaundice — find the cause (gallstone/malignancy); may need ERCP or drainage."},
      {"scenario": "Fever, jaundice and RUQ pain (Charcot's triad).", "answer": "Cholangitis — IV antibiotics and urgent biliary drainage (ERCP)."},
      {"scenario": "Painless jaundice in an elderly patient with weight loss.", "answer": "Suspect pancreatic (head) malignancy — urgent imaging (CT/USS) and referral."},
      {"scenario": "Jaundice with very high ALT after starting a new drug.", "answer": "Hepatocellular (drug-induced) jaundice — stop the culprit, check viral/autoimmune causes."},
      {"scenario": "Unconjugated hyperbilirubinaemia with a normal blood film otherwise well.", "answer": "Consider Gilbert's syndrome (benign) or haemolysis — check LFTs and haemolysis screen."}
    ],
    "keyValues": [
      ["Pre-hepatic", "Unconjugated bilirubin, normal LFTs, haemolysis"],
      ["Hepatic", "Raised ALT/AST (hepatocellular)"],
      ["Obstructive", "Raised ALP/GGT, conjugated bilirubin"],
      ["Charcot's triad", "Fever + jaundice + RUQ pain (cholangitis)"]
    ],
    "redFlags": [
      "Cholangitis — IV antibiotics + urgent biliary drainage (ERCP).",
      "Acute liver failure (coagulopathy, encephalopathy) — urgent hepatology/ICU.",
      "Painless jaundice in the elderly — think pancreatic malignancy."
    ],
    "management": [
      "Classify the type of jaundice (pre-hepatic/hepatic/post-hepatic).",
      "LFTs, bilirubin, FBC, USS; further tests by suspected cause.",
      "Obstructive: treat the cause (ERCP for stones, drainage for malignancy).",
      "Cholangitis: IV antibiotics, urgent biliary drainage."
    ],
    "pitfalls": [
      "Always check conjugated vs unconjugated bilirubin — it directs the classification.",
      "Charcot's triad may be incomplete — a fever with obstructive jaundice is still cholangitis until proven otherwise.",
      "Do not overlook drug-induced liver injury — take a full drug history."
    ]
  },
}
