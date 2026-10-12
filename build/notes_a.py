# Clinical notes part 1: cardiovascular, respiratory, renal/fluids/electrolytes.
PART = {
  "anticoagulation": {
    "name": "Anticoagulation management: INR and APTT",
    "group": "Cardiovascular",
    "essentials": [
      "Warfarin acts by inhibiting vitamin K-dependent clotting factors (II, VII, IX, X) and proteins C and S; its effect is monitored by INR. Onset is delayed (factor VII has a short half-life but full effect needs factors II/X), so acute anticoagulation requires bridging with a rapidly-acting agent.",
      "Heparin (unfractionated) acts via antithrombin III and is monitored by APTT; LMWH (e.g. enoxaparin) is given by weight and usually needs no monitoring. APTT is prolonged in heparin effect, DIC, and factor deficiencies.",
      "Therapeutic INR targets: 2.0-3.0 for most indications (AF, VTE); 2.5-3.5 for mechanical mitral valves. Subtherapeutic INR risks thrombosis; supratherapeutic INR risks bleeding.",
      "Reversal: warfarin over-anticoagulation with bleeding → vitamin K + prothrombin complex concentrate (PCC) or FFP; heparin bleeding → protamine sulfate.",
      "DOACs (apixaban, rivaroxaban, dabigatran, edoxaban) are direct factor inhibitors; they do not require routine INR/APTT monitoring but have specific reversal agents (idarucizumab for dabigatran, andexanet alfa for Xa inhibitors)."
    ],
    "keyValues": [
      ["INR therapeutic (most indications)", "2.0-3.0"],
      ["INR therapeutic (mechanical mitral valve)", "2.5-3.5"],
      ["APTT therapeutic (heparin)", "1.5-2.5 × control"],
      ["Warfarin reversal (bleeding)", "IV vitamin K + PCC/FFP"]
    ],
    "redFlags": [
      "Major bleeding on anticoagulation (intracranial, GI, retroperitoneal) — reverse urgently, not just withhold.",
      "INR > 5.0 with bleeding — treat as emergency.",
      "Thrombosis despite therapeutic anticoagulation — consider compliance, drug interaction, or malignancy."
    ],
    "management": [
      "Bleeding on warfarin: stop warfarin, give IV vitamin K, PCC (or FFP if unavailable), recheck INR.",
      "Bleeding on heparin: stop infusion, give protamine sulfate (dose by heparin dose/time).",
      "Subtherapeutic INR: re-dose warfarin per protocol, consider bridging if high thrombotic risk.",
      "Always check for drug interactions (antibiotics, amiodarone) that alter warfarin effect."
    ]
  },
  "chest-pain": {
    "name": "Chest pain",
    "group": "Cardiovascular",
    "essentials": [
      "First priority is to exclude life-threatening causes: acute coronary syndrome (ACS), aortic dissection, pulmonary embolism, tension pneumothorax, oesophageal rupture.",
      "ACS: cardiac chest pain is central, crushing, radiating to arm/jaw, with sweating/nausea; may be atypical (especially in women, diabetics, elderly). ECG changes (ST elevation, depression, T inversion) and troponin rise confirm.",
      "Aortic dissection: sudden severe 'tearing' pain radiating to the back, with pulse/BP differential, widened mediastinum — a surgical emergency.",
      "PE: pleuritic pain, dyspnoea, hypoxia, tachycardia; risk factors (immobility, surgery, malignancy, OCP).",
      "Non-cardiac causes: musculoskeletal, GORD, anxiety, pericarditis (positional, pleuritic, relieved by leaning forward)."
    ],
    "keyValues": [
      ["Troponin", "Rises 3-6h after ACS; serial sampling"],
      ["ECG in STEMI", "ST elevation in contiguous leads"],
      ["D-dimer (PE)", "Negative rules out PE in low/intermediate risk"],
      ["Wells score (PE)", "Stratifies pre-test probability"]
    ],
    "redFlags": [
      "Haemodynamic instability, new murmur, unequal pulses, BP differential — think dissection.",
      "ST elevation — activate STEMI pathway (primary PCI).",
      "Chest pain with hypoxia/tachycardia — consider PE."
    ],
    "management": [
      "Immediate: ABC, oxygen if hypoxic, IV access, 12-lead ECG within 10 min, cardiac monitoring.",
      "Suspected ACS: aspirin, nitrates, analgesia (morphine), consider antiplatelet + anticoagulant per protocol.",
      "Suspected dissection: control BP/heart rate (beta-blocker), urgent CT aortogram, surgical referral.",
      "Suspected PE: risk-stratify (Wells), D-dimer or CTPA, LMWH if high probability."
    ]
  },
  "arrhythmias": {
    "name": "Common arrhythmias",
    "group": "Cardiovascular",
    "essentials": [
      "Assess haemodynamic stability first: an unstable patient with any tachy/bradyarrhythmia needs urgent treatment (often synchronised DC cardioversion or pacing), not just drugs.",
      "Atrial fibrillation: irregularly irregular; causes include ischaemia, sepsis, thyrotoxicosis, alcohol, valvular disease. Manage rate (beta-blocker/CCB) or rhythm, and assess stroke risk (CHA2DS2-VASc) for anticoagulation.",
      "Supraventricular tachycardia (AVNRT/AVRT): regular narrow-complex tachycardia; treat with vagal manoeuvres, adenosine, then CCB/beta-blocker.",
      "Ventricular tachycardia: broad-complex tachycardia; if pulseless → cardiac arrest algorithm; if stable → amiodarone/lidocaine, treat cause (ischaemia, electrolytes).",
      "Bradyarrhythmias (heart block, sinus bradycardia): if symptomatic/unstable → atropine, then pacing. Complete heart block needs pacing."
    ],
    "keyValues": [
      ["CHA2DS2-VASc", "≥2 (men) / ≥3 (women) → anticoagulate AF"],
      ["Adenosine dose", "6 mg then 12 mg rapid IV"],
      ["Amiodarone (VT)", "300 mg IV over 10-20 min"],
      ["Atropine (bradycardia)", "500 mcg IV, repeat to 3 mg"]
    ],
    "redFlags": [
      "Pulseless VT/VF — defibrillate immediately.",
      "Unstable tachyarrhythmia (shock, chest pain, syncope, heart failure) — synchronised cardioversion.",
      "Complete heart block with bradycardia — pacing."
    ],
    "management": [
      "Unstable: synchronised DC cardioversion (tachy) or atropine/pacing (brady).",
      "Stable AF: rate control (beta-blocker/CCB), anticoagulate per CHA2DS2-VASc.",
      "Stable SVT: vagal manoeuvres → adenosine → CCB/beta-blocker.",
      "Stable VT: amiodarone, correct K+/Mg2+, treat ischaemia."
    ]
  },
  "collapse-shock": {
    "name": "Collapse and shock",
    "group": "Cardiovascular",
    "essentials": [
      "Shock = inadequate tissue perfusion, not just low BP. Types: hypovolaemic (haemorrhage, dehydration), cardiogenic (MI, arrhythmia, tamponade), obstructive (PE, tension pneumothorax), distributive (sepsis, anaphylaxis).",
      "Recognise early: hypotension, tachycardia, cool peripheries, prolonged capillary refill, reduced urine output, altered consciousness, rising lactate.",
      "Hypovolaemic shock: the most common; treat with rapid IV fluid/blood, find and stop the source of loss.",
      "Cardiogenic shock: pump failure; fluids may worsen it — need inotropes, treat the cause (ACS, arrhythmia).",
      "Septic shock: distributive; early antibiotics + fluids + lactate-guided resuscitation (Sepsis Six)."
    ],
    "keyValues": [
      ["Lactate", ">2 mmol/L suggests hypoperfusion"],
      ["MAP target", "≥65 mmHg"],
      ["Urine output target", "≥0.5 mL/kg/h"],
      ["Sepsis Six", "O2, cultures, antibiotics, fluids, lactate, urine output"]
    ],
    "redFlags": [
      "Unresponsive, agonal breathing — cardiac arrest pathway.",
      "Tension pneumothorax (absent breath sounds, tracheal shift) — needle decompression.",
      "Cardiac tamponade (muffled heart sounds, JVP, hypotension) — pericardiocentesis."
    ],
    "management": [
      "ABC, high-flow oxygen, IV access, monitoring, treat the specific cause.",
      "Hypovolaemic: rapid crystalloid/blood, control haemorrhage.",
      "Septic: Sepsis Six — cultures, broad-spectrum antibiotics, fluids, lactate.",
      "Cardiogenic: treat arrhythmia/ischaemia, cautious fluids, inotropes, cardiology review."
    ]
  },
  "syncope": {
    "name": "Syncope",
    "group": "Cardiovascular",
    "essentials": [
      "Syncope = transient loss of consciousness due to cerebral hypoperfusion, with rapid, spontaneous recovery. Distinguish from seizure (post-ictal confusion, tongue biting, tonic-clonic movements) and from 'drop attacks' (no LOC).",
      "Reflex (vasovagal) syncope: the most common; triggered by pain, emotion, standing, micturition; prodrome of light-headedness, sweating, nausea.",
      "Orthostatic hypotension: on standing, especially in elderly, dehydrated, or on antihypertensives.",
      "Cardiac syncope: arrhythmias (brady/tachy), structural disease (aortic stenosis, HCM), PE — the dangerous causes; may have no prodrome and occur on exertion.",
      "Key investigations: ECG, lying/standing BP, consider echo, Holter, tilt test. Admit if cardiac cause suspected, abnormal ECG, or high-risk features."
    ],
    "keyValues": [
      ["Orthostatic hypotension", "SBP drop ≥20 mmHg on standing"],
      ["ECG", "Look for heart block, long QT, Brugada, ischaemia"],
      ["High-risk features", "Exertional, no prodrome, family history of sudden death, abnormal ECG"]
    ],
    "redFlags": [
      "Syncope during exertion — think cardiac (aortic stenosis, HCM, arrhythmia).",
      "Abnormal ECG, family history of sudden cardiac death, or structural heart disease.",
      "Recurrent unexplained syncope — needs cardiology assessment."
    ],
    "management": [
      "ABC, check glucose, ECG, lying/standing BP.",
      "Reassure and advise for reflex syncope (fluid, avoid triggers, counter-pressure manoeuvres).",
      "Cardiac syncope: treat the arrhythmia/structural cause, admit for monitoring.",
      "Advise driving restrictions per DVLA rules after syncope."
    ]
  },
  "acute-limb-ischaemia": {
    "name": "Acute limb ischaemia",
    "group": "Cardiovascular",
    "essentials": [
      "Sudden reduction in limb perfusion, usually from embolism (AF, recent MI) or in-situ thrombosis (atherosclerosis). The '6 Ps': pain, pallor, pulselessness, paraesthesia, paralysis, perishing cold.",
      "Time-critical: irreversible muscle/nerve damage occurs within 4-6 hours. Paralysis and paraesthesia indicate advanced ischaemia.",
      "Distinguish embolic (sudden, no prior claudication, contralateral pulses normal) from thrombotic (on background of chronic PAD).",
      "Examine: pulses (femoral, popliteal, DP, PT), capillary refill, sensation, motor function, skin colour/temperature. Document the level of the block.",
      "Immediate: heparin, analgesia, keep limb warm (not hot), urgent vascular referral. Do not delay imaging if the limb is threatened."
    ],
    "keyValues": [
      ["Ischaemia time", "Irreversible damage after 4-6 hours"],
      ["6 Ps", "Pain, pallor, pulselessness, paraesthesia, paralysis, perishing cold"],
      ["Immediate Rx", "IV heparin, analgesia, urgent vascular review"]
    ],
    "redFlags": [
      "Paralysis or paraesthesia — advanced ischaemia, imminent irreversible damage.",
      "Cold, mottled, pulseless limb — surgical emergency.",
      "Rhabdomyolysis risk after reperfusion (check K+, CK, renal function)."
    ],
    "management": [
      "ABC, IV heparin, analgesia, keep limb warm, NBM, urgent vascular surgery referral.",
      "Do not delay for imaging if limb is threatened — go straight to vascular team.",
      "Post-reperfusion: monitor for compartment syndrome and rhabdomyolysis."
    ]
  },
  "chronic-limb-ischaemia": {
    "name": "Chronic limb ischaemia – ulcers and gangrene",
    "group": "Cardiovascular",
    "essentials": [
      "Chronic limb-threatening ischaemia (CLTI): rest pain, non-healing ulcers, or gangrene due to peripheral arterial disease (PAD). Rest pain is worse at night, relieved by dependency.",
      "Risk factors: smoking, diabetes, hypertension, hyperlipidaemia, age. Diabetic foot disease is a major cause of ulcers (neuropathic + ischaemic).",
      "Ulcer types: arterial (punched-out, on toes/heel, painful, pale base), venous (gaiter area, shallow, wet, painless), neuropathic (plantar, painless, on pressure points).",
      "Assess: ankle-brachial pressure index (ABPI), pulses, sensation (monofilament), ulcer characteristics, signs of infection.",
      "Management: best medical therapy (antiplatelet, statin, smoking cessation, diabetes control), revascularisation (angioplasty/bypass) for CLTI, wound care, amputation if unsalvageable."
    ],
    "keyValues": [
      ["ABPI", ">0.9 normal; <0.5 severe ischaemia; >1.3 suggests calcified vessels (diabetes)"],
      ["Rest pain", "Worse at night, relieved by hanging leg down"],
      ["Arterial ulcer", "Punched-out, painful, on toes/heel"]
    ],
    "redFlags": [
      "Gangrene or necrotic tissue — urgent vascular review, may need amputation.",
      "Infected diabetic foot with systemic sepsis — emergency, IV antibiotics, surgical debridement.",
      "Rapid deterioration or acute-on-chronic ischaemia."
    ],
    "management": [
      "Best medical therapy: antiplatelet, statin, smoking cessation, tight diabetes/BP control.",
      "CLTI: refer to vascular surgery for revascularisation.",
      "Infected ulcer: wound swab, antibiotics, debridement, offloading (diabetic).",
      "Wound care: keep clean, moist, pressure offloading; refer to tissue viability/podiatry."
    ]
  },
  "dvt-pe": {
    "name": "Deep Venous thrombosis and Pulmonary embolism",
    "group": "Cardiovascular",
    "essentials": [
      "VTE = DVT + PE, a spectrum of the same disease. Risk factors: immobility, surgery, malignancy, pregnancy/OCP, thrombophilia, previous VTE, obesity.",
      "DVT: unilateral leg swelling, pain, erythema, warmth, dilated superficial veins. Wells score stratifies probability; D-dimer rules out in low probability; USS confirms.",
      "PE: dyspnoea, pleuritic chest pain, hypoxia, tachycardia, haemoptysis, collapse. Massive PE → obstructive shock. Wells score + D-dimer/CTPA.",
      "Anticoagulation is the mainstay: LMWH/DOAC. Massive PE with shock → thrombolysis.",
      "Prevention: VTE prophylaxis (LMWH, TEDs, early mobilisation) for all at-risk inpatients."
    ],
    "keyValues": [
      ["Wells DVT", "≥2 = likely → USS"],
      ["Wells PE", ">4 = likely → CTPA"],
      ["D-dimer", "Negative rules out VTE in low/intermediate risk"],
      ["Massive PE", "Shock/hypotension → thrombolysis"]
    ],
    "redFlags": [
      "PE with hypotension/shock — massive PE, thrombolyse.",
      "DVT with phlegmasia (tense, blue, painful leg) — venous gangrene risk.",
      "Sudden collapse with risk factors — consider PE."
    ],
    "management": [
      "Suspected DVT: Wells score, D-dimer, USS; anticoagulate if high probability while awaiting.",
      "Suspected PE: Wells, D-dimer/CTPA, LMWH if high probability.",
      "Confirmed VTE: therapeutic anticoagulation (LMWH → DOAC or warfarin), duration by cause.",
      "Massive PE: thrombolysis (alteplase), consider surgical/mechanical embolectomy."
    ]
  },
  "shortness-of-breath": {
    "name": "Shortness of breath",
    "group": "Respiratory",
    "essentials": [
      "Dyspnoea has cardiac, respiratory, and other causes. Life-threatening: PE, tension pneumothorax, severe asthma/COPD, pulmonary oedema, anaphylaxis, foreign body.",
      "Assess severity: speaking in sentences, accessory muscle use, oxygen saturations, respiratory rate, ABG. Silent chest in asthma is ominous (no air entry).",
      "Pulmonary oedema (heart failure): orthopnoea, PND, crackles, raised JVP, S3 — treat with oxygen, diuretics, nitrates, CPAP.",
      "COPD exacerbation: increased breathlessness, wheeze, sputum; treat with bronchodilators, steroids, antibiotics if infective, controlled oxygen (target 88-92%).",
      "Pneumothorax: sudden pleuritic pain + dyspnoea; tension (tracheal shift, haemodynamic compromise) needs needle decompression."
    ],
    "keyValues": [
      ["O2 target (COPD)", "88-92%"],
      ["O2 target (other)", "94-98%"],
      ["Tension pneumothorax", "Needle decompression (2nd ICS mid-clavicular)"],
      ["Pulmonary oedema", "O2, furosemide, nitrates, CPAP"]
    ],
    "redFlags": [
      "Silent chest, exhaustion, or reduced consciousness in asthma — peri-arrest.",
      "Tension pneumothorax — decompress immediately.",
      "Hypoxia refractory to oxygen — think PE, shunt, or severe disease."
    ],
    "management": [
      "ABC, oxygen to target, sit patient up, IV access, monitoring.",
      "Asthma: salbutamol (nebulised), ipratropium, steroids, consider magnesium.",
      "Pulmonary oedema: furosemide, nitrates, CPAP, treat the cause.",
      "Pneumothorax: size/clinical assessment; aspiration or chest drain; tension → decompress."
    ]
  },
  "oxygen-management": {
    "name": "Oxygen management in wards",
    "group": "Respiratory",
    "essentials": [
      "Oxygen is a drug — prescribe it with a target range, not 'as required'. Over-oxygenation in COPD can suppress hypoxic drive and cause hypercapnia.",
      "Targets: 94-98% for most acutely ill patients; 88-92% for those at risk of hypercapnic respiratory failure (COPD, obesity hypoventilation, neuromuscular disease).",
      "Delivery: nasal cannulae (low flow), simple face mask, Venturi mask (precise FiO2), non-rebreathe (high flow, 15 L/min) for emergencies.",
      "Monitor response: saturations, ABG if hypercapnia suspected or target not met. Reassess regularly.",
      "Document the oxygen prescription, target range, and weaning plan. Escalate if saturations fall below target."
    ],
    "keyValues": [
      ["Normal target", "94-98%"],
      ["COPD/at-risk target", "88-92%"],
      ["Non-rebreathe", "15 L/min (emergency)"],
      ["Venturi mask", "Precise FiO2 (24-60%)"]
    ],
    "redFlags": [
      "Falling saturations despite high-flow oxygen — call for help, consider ABG.",
      "Rising CO2 or drowsiness in COPD on oxygen — reduce FiO2, consider NIV.",
      "Hypoxia with no improvement — look for the cause (PE, pneumothorax, oedema)."
    ],
    "management": [
      "Prescribe oxygen with a target range and delivery device.",
      "Start at appropriate FiO2, titrate to target, monitor saturations.",
      "Check ABG if hypercapnia risk or target not achieved.",
      "Wean oxygen as the patient improves; document the plan."
    ]
  },
  "abg-interpretation": {
    "name": "Arterial blood gas interpretation",
    "group": "Respiratory",
    "essentials": [
      "Systematic approach: (1) oxygenation (PaO2), (2) pH (acidaemia/alkalaemia), (3) PaCO2 (respiratory), (4) HCO3 (metabolic), (5) compensation.",
      "Respiratory acidosis: high PaCO2 (hypoventilation — COPD, sedation, neuromuscular). Respiratory alkalosis: low PaCO2 (hyperventilation — pain, anxiety, PE, sepsis).",
      "Metabolic acidosis: low HCO3 — anion gap (lactate, ketoacidosis, renal failure, toxins) vs non-anion gap (diarrhoea, renal tubular acidosis).",
      "Metabolic alkalosis: high HCO3 (vomiting, diuretics, hypokalaemia).",
      "Compensation: respiratory compensates metabolic quickly (change PaCO2), metabolic compensates respiratory slowly (change HCO3). Check if compensation is adequate."
    ],
    "keyValues": [
      ["Normal pH", "7.35-7.45"],
      ["Normal PaCO2", "4.7-6.0 kPa (35-45 mmHg)"],
      ["Normal HCO3", "22-26 mmol/L"],
      ["Normal PaO2", "10-13 kPa on air"],
      ["Anion gap", "Na - (Cl + HCO3); normal 8-12"]
    ],
    "redFlags": [
      "pH < 7.2 — severe acidaemia, consider bicarbonate/ICU.",
      "Lactic acidosis (lactate > 4) — sepsis/ischaemia, treat the cause.",
      "Rising PaCO2 with falling pH in COPD — hypercapnic respiratory failure, consider NIV."
    ],
    "management": [
      "Interpret systematically: oxygenation → pH → PaCO2 → HCO3 → compensation.",
      "Treat the underlying cause, not just the numbers.",
      "Respiratory acidosis: improve ventilation (bronchodilators, NIV, treat cause).",
      "Metabolic acidosis: identify anion gap, treat cause (fluids, insulin for DKA, treat sepsis)."
    ]
  },
  "electrolytes": {
    "name": "Electrolyte management",
    "group": "Renal, fluids & electrolytes",
    "essentials": [
      "Sodium: hyponatraemia (most common) — assess volume status and osmolality; causes include SIADH, hypovolaemia, heart failure, adrenal insufficiency. Correct slowly (risk of osmotic demyelination). Hypernatraemia = water deficit.",
      "Potassium: hypokalaemia (diuretics, vomiting, diarrhoea) — cardiac arrhythmia risk; replace orally/IV. Hyperkalaemia (renal failure, ACEi, K+-sparing diuretics, cell lysis) — cardiac emergency, treat with calcium gluconate, insulin+dextrose, nebulised salbutamol, then removal.",
      "Calcium: hypercalcaemia (malignancy, primary hyperparathyroidism) — hydrate + bisphosphonate. Hypocalcaemia (post-thyroidectomy, hypoparathyroidism) — tetany, Chvostek/Trousseau signs.",
      "Magnesium: hypomagnesaemia (diuretics, alcohol) — associated with hypokalaemia/hypocalcaemia, arrhythmia. Hypermagnesaemia (renal failure).",
      "Phosphate: hypophosphataemia (refeeding, dialysis) — muscle weakness, rhabdomyolysis."
    ],
    "keyValues": [
      ["Normal Na", "135-145 mmol/L"],
      ["Normal K", "3.5-5.0 mmol/L"],
      ["Hyperkalaemia emergency", "K > 6.5 or ECG changes"],
      ["Hyperkalaemia Rx", "Calcium gluconate, insulin+dextrose, salbutamol"],
      ["Hyponatraemia correction", "≤8-10 mmol/L per 24h"]
    ],
    "redFlags": [
      "Hyperkalaemia with ECG changes (peaked T, wide QRS) — treat immediately.",
      "Severe hyponatraemia with seizures — hypertonic saline, but correct slowly.",
      "Symptomatic hypocalcaemia (tetany, laryngospasm) — IV calcium."
    ],
    "management": [
      "Hyperkalaemia: calcium gluconate (cardiac protection), insulin+dextrose, salbutamol, then K+ removal (resonium, dialysis).",
      "Hypokalaemia: oral/IV potassium replacement, treat cause.",
      "Hyponatraemia: correct the cause, replace slowly, monitor Na frequently.",
      "Hypercalcaemia: IV fluids, bisphosphonate, treat malignancy."
    ]
  },
  "low-urine-output": {
    "name": "Low urine output",
    "group": "Renal, fluids & electrolytes",
    "essentials": [
      "Oliguria = urine output < 0.5 mL/kg/h (or < 400 mL/24h). Anuria (< 100 mL/24h) suggests obstruction or severe renal failure.",
      "Classify AKI: pre-renal (hypovolaemia, sepsis, heart failure — most common), intrinsic renal (ATN, glomerulonephritis, interstitial nephritis), post-renal (obstruction — catheter, prostate, stones).",
      "Assess: fluid balance, weight, JVP, BP, urine output, urinalysis, U&Es, creatinine, consider renal USS for obstruction.",
      "Pre-renal AKI responds to fluid resuscitation; intrinsic/post-renal need specific treatment. Monitor for hyperkalaemia, acidosis, fluid overload.",
      "Prevent: adequate hydration, avoid nephrotoxins (NSAIDs, ACEi in dehydration, contrast), monitor high-risk patients."
    ],
    "keyValues": [
      ["Oliguria", "< 0.5 mL/kg/h"],
      ["Anuria", "< 100 mL/24h"],
      ["AKI (KDIGO)", "Cr rise ≥26.5 µmol/L in 48h or 1.5× baseline"],
      ["Urine output target", "≥ 0.5 mL/kg/h"]
    ],
    "redFlags": [
      "Anuria — think obstruction, needs urgent renal USS + catheter.",
      "Hyperkalaemia or severe acidosis in AKI — may need dialysis.",
      "Pulmonary oedema from fluid overload — stop fluids, diurese."
    ],
    "management": [
      "Assess volume status; fluid challenge if hypovolaemic (pre-renal).",
      "Catheterise to measure output accurately; check for obstruction.",
      "Stop nephrotoxins, treat the cause, monitor U&Es and output.",
      "Escalate for dialysis if refractory hyperkalaemia, acidosis, or fluid overload."
    ]
  },
  "iv-fluids": {
    "name": "Intravenous fluid prescription",
    "group": "Renal, fluids & electrolytes",
    "essentials": [
      "Prescribe IV fluids like a drug: assess the patient's fluid status (hypovolaemic, euvolaemic, overloaded), then choose the right fluid, rate, and monitoring.",
      "Crystalloids are first-line: balanced solutions (Hartmann's, Plasma-Lyte) preferred over 0.9% saline (which can cause hyperchloraemic acidosis). Dextrose for water loss.",
      "Maintenance: ~25-30 mL/kg/day water, with Na+ and K+ (~1 mmol/kg/day each). Adjust for losses (vomiting, diarrhoea, drains, fever).",
      "Resuscitation: rapid boluses (250-500 mL) for hypovolaemia/shock, reassess after each bolus. Avoid over-resuscitation (pulmonary oedema).",
      "Monitor: fluid balance charts, weight, urine output, U&Es, clinical signs. Reassess daily and stop when no longer needed."
    ],
    "keyValues": [
      ["Maintenance water", "25-30 mL/kg/day"],
      ["Maintenance Na/K", "~1 mmol/kg/day each"],
      ["Resuscitation bolus", "250-500 mL crystalloid, reassess"],
      ["First-line fluid", "Balanced crystalloid (Hartmann's)"]
    ],
    "redFlags": [
      "Signs of fluid overload (pulmonary oedema, raised JVP) — stop fluids, diurese.",
      "Hypovolaemic shock — rapid resuscitation, not slow maintenance.",
      "Heart failure/renal failure — fluids can worsen; be cautious."
    ],
    "management": [
      "Assess volume status and prescribe a clear plan (resuscitation vs maintenance vs replacement).",
      "Choose balanced crystalloid; add K+ as needed (check renal function).",
      "Monitor fluid balance, weight, U&Es; reassess daily.",
      "Stop IV fluids as soon as the patient can drink."
    ]
  },
}
