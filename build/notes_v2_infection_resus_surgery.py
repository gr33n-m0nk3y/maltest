# Enhanced notes v2 — infection, resuscitation, surgery, ward systems, covid (batch 4).
PART = {
  "febrile-patient": {
    "name": "The febrile patient",
    "group": "Infection & sepsis",
    "overview": "Fever plus organ dysfunction is sepsis, and sepsis is time-critical. The exam tests the Sepsis Six and finding the source within the first hour.",
    "essentials": [
      "Fever = temperature ≥38°C. Assess for sepsis (infection + organ dysfunction) using NEWS2 and clinical judgement. Sepsis is time-critical — treat within 1 hour.",
      "Sepsis Six: oxygen, blood cultures, IV antibiotics, IV fluids, lactate, urine output. Give antibiotics within 1 hour of suspected sepsis.",
      "Find the source: respiratory (cough, sputum, chest signs), urinary (dysuria, loin pain), skin/soft tissue, line, abdominal, CNS (meningitis), endocarditis.",
      "Risk factors for poor outcome: elderly, immunocompromised (neutropenia, steroids, HIV), malignancy, diabetes, pregnancy, indwelling devices.",
      "Monitor: observations (NEWS2), lactate, cultures, response to antibiotics. Escalate if deteriorating or not improving."
    ],
    "drugs": [
      {"name": "IV broad-spectrum antibiotics", "when": "Suspected sepsis — within 1 hour", "notes": "Per local policy; do not delay for cultures"},
      {"name": "IV crystalloid", "when": "Sepsis with hypoperfusion (lactate >2, hypotension)", "notes": "Fluid boluses, reassess; noradrenaline if MAP <65"},
      {"name": "Oxygen", "when": "Hypoxia / as part of Sepsis Six", "notes": "Target 94-98% (88-92% if hypercapnia risk)"},
      {"name": "Paracetamol", "when": "Symptomatic fever/comfort", "notes": "Does not treat the cause; avoid masking deterioration"}
    ],
    "clinicalScenarios": [
      {"scenario": "Temperature 38.5°C, NEWS2 6, lactate 3.5.", "answer": "Suspected sepsis — Sepsis Six within 1 hour (cultures, IV antibiotics, fluids, oxygen, lactate, urine output)."},
      {"scenario": "Fever with cough, sputum and focal chest signs.", "answer": "Pneumonia — assess severity (CURB-65), antibiotics, oxygen; find the organism where possible."},
      {"scenario": "Fever with dysuria and loin pain.", "answer": "Pyelonephritis/UTI — urine culture, antibiotics; consider obstruction with USS if not improving."},
      {"scenario": "Fever in a patient with a central line.", "answer": "Consider line sepsis — cultures (peripheral + line), antibiotics, consider line removal."},
      {"scenario": "Fever with neck stiffness and photophobia.", "answer": "Meningitis — immediate IV antibiotics + consider dexamethasone; do not delay for LP."}
    ],
    "keyValues": [
      ["Sepsis", "Infection + organ dysfunction"],
      ["Antibiotics within", "1 hour of suspected sepsis"],
      ["Sepsis Six", "O2, cultures, antibiotics, fluids, lactate, urine output"],
      ["Lactate", ">2 mmol/L suggests hypoperfusion"]
    ],
    "redFlags": [
      "NEWS2 ≥5 or lactate >2 — sepsis, treat urgently.",
      "Hypotension/shock — aggressive resuscitation + antibiotics.",
      "Fever in neutropenic/immunocompromised — treat as sepsis immediately."
    ],
    "management": [
      "Sepsis Six within 1 hour: O2, cultures, antibiotics, fluids, lactate, urine output.",
      "Identify and treat the source.",
      "Monitor response; escalate if deteriorating.",
      "Consider immunocompromise and adjust accordingly."
    ],
    "pitfalls": [
      "Never delay antibiotics in sepsis to wait for cultures or imaging.",
      "A normal temperature does not exclude sepsis — the elderly and immunocompromised may be afebrile.",
      "Always look for and treat the source, not just the fever."
    ]
  },

  "infection-control": {
    "name": "Infection control on the ward",
    "group": "Infection & sepsis",
    "overview": "Preventing healthcare-associated infection is tested through hand hygiene and precautions. The exam tests matching the right precautions to the right organism.",
    "essentials": [
      "Hand hygiene is the single most important measure — 'bare below the elbows', alcohol rub, soap/water for C. difficile and norovirus.",
      "Standard precautions: gloves, aprons, safe sharps disposal, correct waste segregation, respiratory hygiene.",
      "Transmission-based precautions: contact (MRSA, C. difficile, ESBL — gloves/aprons, isolation), droplet (influenza, meningococcal — surgical mask), airborne (TB, measles, chickenpox — negative pressure, FFP3).",
      "Isolate patients with suspected/confirmed transmissible infections; notify infection control.",
      "Antimicrobial stewardship: prescribe appropriately, review at 48 h, use narrow-spectrum where possible, document indication and duration."
    ],
    "drugs": [
      {"name": "Alcohol hand rub / soap & water", "when": "Hand hygiene", "notes": "Soap and water for C. difficile and norovirus (spores not killed by alcohol)"},
      {"name": "PPE (gloves, apron, mask, FFP3)", "when": "Per precautions", "notes": "FFP3 for airborne (TB, measles); surgical mask for droplet"},
      {"name": "Antimicrobials (appropriate)", "when": "Confirmed/probable infection", "notes": "Stewardship — narrow spectrum, documented indication, review at 48 h"}
    ],
    "clinicalScenarios": [
      {"scenario": "Patient with Clostridium difficile diarrhoea.", "answer": "Contact precautions + soap/water handwashing, isolate; review/stop culprit antibiotics."},
      {"scenario": "Patient with suspected pulmonary TB.", "answer": "Airborne precautions (negative pressure, FFP3) and isolation; notify infection control."},
      {"scenario": "Patient with meningococcal sepsis.", "answer": "Droplet precautions + urgent antibiotics; provide prophylaxis for close contacts."},
      {"scenario": "MRSA-colonised patient on the ward.", "answer": "Contact precautions (gloves/apron, isolation), hand hygiene, decolonisation per policy."}
    ],
    "keyValues": [
      ["Hand hygiene", "Alcohol rub; soap/water for C. diff & norovirus"],
      ["Contact precautions", "MRSA, C. difficile, ESBL"],
      ["Droplet precautions", "Influenza, meningococcal"],
      ["Airborne precautions", "TB, measles, chickenpox (FFP3)"]
    ],
    "redFlags": [
      "Suspected TB/measles/chickenpox — airborne precautions + isolation immediately.",
      "C. difficile — isolate, soap/water handwashing, stop culprit antibiotics.",
      "Meningococcal — droplet precautions + urgent antibiotics + contact prophylaxis."
    ],
    "management": [
      "Hand hygiene and standard precautions always.",
      "Isolate and apply appropriate precautions for transmissible infections.",
      "Notify infection control; follow local policy.",
      "Antimicrobial stewardship: document indication, review at 48 h."
    ],
    "pitfalls": [
      "Alcohol rub does not kill C. difficile spores — use soap and water.",
      "Airborne precautions need FFP3 and a negative-pressure room, not a surgical mask.",
      "Do not forget contact prophylaxis for meningococcal contacts."
    ]
  },

  "cpr": {
    "name": "Cardiopulmonary resuscitation",
    "group": "Resuscitation & emergencies",
    "overview": "ALS is a core competency. The exam tests the arrest sequence, the shockable vs non-shockable algorithm, and the reversible causes (4 Hs and 4 Ts).",
    "essentials": [
      "Recognise cardiac arrest: unresponsive + not breathing normally (agonal gasps count as not breathing). Call for help, start CPR immediately.",
      "Adult CPR: 30:2 compressions:ventilations, rate 100-120/min, depth 5-6 cm, minimise interruptions. Attach AED/defibrillator as soon as available.",
      "Shockable rhythms (VF/pulseless VT): defibrillate, then CPR; adrenaline 1 mg after 2nd shock; repeat adrenaline every 3-5 min; amiodarone after 3rd shock.",
      "Non-shockable (PEA/asystole): adrenaline 1 mg immediately, then every 3-5 min. Find and treat reversible causes.",
      "4 Hs: hypoxia, hypovolaemia, hypo/hyperkalaemia, hypothermia. 4 Ts: tension pneumothorax, tamponade, toxins, thrombosis (PE/MI)."
    ],
    "drugs": [
      {"name": "Adrenaline", "when": "All cardiac arrests (ALS)", "notes": "1 mg IV every 3-5 min; after 2nd shock in shockable, immediately in non-shockable"},
      {"name": "Amiodarone", "when": "Refractory VF/pulseless VT", "notes": "300 mg IV after 3rd shock, then 150 mg after 5th"},
      {"name": "Defibrillation", "when": "VF/pulseless VT", "notes": "Biphasic 150-200 J; minimise interruption"},
      {"name": "Reversible-cause treatments", "when": "Per cause", "notes": "Fluids/blood (hypovolaemia), calcium (hyperkalaemia), needle decompression (tension pneumothorax), thrombolysis (PE)"}
    ],
    "clinicalScenarios": [
      {"scenario": "Patient in pulseless VT on the monitor.", "answer": "Shockable — defibrillate immediately, then CPR; adrenaline after the 2nd shock."},
      {"scenario": "PEA arrest with distended neck veins and muffled heart sounds.", "answer": "Consider tamponade as a reversible cause — pericardiocentesis if suspected; continue ALS."},
      {"scenario": "PEA arrest in a patient post-op with signs of bleeding.", "answer": "Hypovolaemia — resuscitate with fluids/blood alongside ALS."},
      {"scenario": "Arrest in a patient with severe hyperkalaemia.", "answer": "Treat the reversible cause — calcium gluconate, insulin+dextrose alongside ALS."}
    ],
    "keyValues": [
      ["CPR ratio", "30:2, 100-120/min, depth 5-6 cm"],
      ["Adrenaline", "1 mg IV every 3-5 min"],
      ["Shockable", "VF/pulseless VT → defibrillate"],
      ["4 Hs / 4 Ts", "Hypoxia, hypovolaemia, K+, hypothermia / tension, tamponade, toxins, thrombosis"]
    ],
    "redFlags": [
      "VF/pulseless VT — defibrillate immediately, do not delay for drugs.",
      "Tension pneumothorax during arrest — needle decompression.",
      "Reversible causes — treat them (the only way to achieve ROSC in PEA)."
    ],
    "management": [
      "Call for help, start high-quality CPR, attach defibrillator.",
      "Follow the ALS algorithm (shockable vs non-shockable).",
      "Give adrenaline per protocol; treat reversible causes.",
      "Post-ROSC: ABC, targeted temperature management, treat the cause, ICU."
    ],
    "pitfalls": [
      "In shockable rhythms, defibrillation comes before drugs.",
      "In PEA, ROSC is only achieved by treating the reversible cause.",
      "Do not forget agonal gasps count as 'not breathing normally' — start CPR."
    ]
  },

  "anaphylaxis": {
    "name": "Anaphylaxis",
    "group": "Resuscitation & emergencies",
    "overview": "A life-threatening emergency where adrenaline is first-line and must not be delayed. The exam tests the immediate response and the post-event observation.",
    "essentials": [
      "Anaphylaxis = severe, life-threatening systemic hypersensitivity reaction. Rapid onset: airway (stridor, swelling), breathing (wheeze, dyspnoea), circulation (hypotension, collapse), plus skin (urticaria, angioedema).",
      "Immediate: remove the trigger, call for help, IM adrenaline 500 mcg (0.5 mL of 1:1000) anterolateral thigh, repeat after 5 min if no improvement.",
      "Adjunctive: high-flow oxygen, IV fluids (for hypotension), antihistamine (chlorphenamine), steroid (hydrocortisone) — but adrenaline is first-line and life-saving.",
      "Position: lie flat with legs raised (unless breathing difficulty — sit up); do not sit/stand a hypotensive patient abruptly.",
      "Observe for biphasic reaction (recurrence hours later) — monitor ≥6-12 h; arrange follow-up and an adrenaline auto-injector."
    ],
    "drugs": [
      {"name": "Adrenaline (IM)", "when": "Anaphylaxis — first-line, immediately", "notes": "500 mcg (0.5 mL 1:1000) anterolateral thigh; repeat after 5 min"},
      {"name": "High-flow oxygen", "when": "All anaphylaxis", "notes": "15 L/min via non-rebreathe"},
      {"name": "IV fluids", "when": "Hypotension", "notes": "Rapid crystalloid bolus"},
      {"name": "Chlorphenamine (antihistamine)", "when": "Adjunct (skin symptoms)", "notes": "IV/IM 10 mg; does not treat airway/circulation"},
      {"name": "Hydrocortisone", "when": "Adjunct", "notes": "IV 200 mg; does not replace adrenaline"},
      {"name": "IV adrenaline infusion", "when": "Refractory anaphylaxis (specialist)", "notes": "After 2 IM doses with no response; senior/ICU"}
    ],
    "clinicalScenarios": [
      {"scenario": "Stridor, wheeze and hypotension after a bee sting.", "answer": "Anaphylaxis — IM adrenaline 500 mcg, high-flow oxygen, IV fluids; repeat adrenaline if no improvement."},
      {"scenario": "Only urticaria with no airway or circulatory involvement after an allergen.", "answer": "Allergic reaction (not anaphylaxis) — antihistamine, monitor; be ready with adrenaline if it progresses."},
      {"scenario": "No response to 2 doses of IM adrenaline.", "answer": "Refractory anaphylaxis — escalate for IV adrenaline infusion and airway support (ICU)."},
      {"scenario": "Anaphylaxis patient improves but you are unsure when to discharge.", "answer": "Observe ≥6-12 h for a biphasic reaction; arrange follow-up and an adrenaline auto-injector."}
    ],
    "keyValues": [
      ["Adrenaline (IM)", "500 mcg (0.5 mL 1:1000), repeat after 5 min"],
      ["Adrenaline site", "Anterolateral thigh"],
      ["Adjuncts", "O2, IV fluids, chlorphenamine, hydrocortisone"],
      ["Observation", "≥6-12 h for biphasic reaction"]
    ],
    "redFlags": [
      "Stridor, hoarse voice, or airway swelling — impending airway obstruction.",
      "Hypotension/collapse — IV fluids + adrenaline, lie flat.",
      "No response to 2 doses of adrenaline — escalate, consider IV adrenaline infusion."
    ],
    "management": [
      "Remove trigger, call for help, IM adrenaline immediately.",
      "High-flow oxygen, IV fluids, position appropriately.",
      "Repeat adrenaline if no improvement; adjuncts (antihistamine, steroid).",
      "Observe for biphasic reaction; arrange auto-injector and follow-up."
    ],
    "pitfalls": [
      "Antihistamines and steroids do not replace adrenaline — give adrenaline first.",
      "Do not stand a hypotensive anaphylaxis patient up — keep them flat.",
      "Remember the biphasic reaction — observe for hours."
    ]
  },

  "overdoses": {
    "name": "Overdoses",
    "group": "Resuscitation & emergencies",
    "overview": "Treat the patient, not the poison. The exam tests recognising toxidromes and giving the correct antidote (NAC, naloxone, bicarbonate).",
    "essentials": [
      "Assess ABC and treat the patient, not just the poison. Identify the substance, dose, time, and co-ingestants (paracetamol + alcohol common).",
      "Paracetamol overdose: hepatotoxic. Treat with N-acetylcysteine (NAC) if levels are above the treatment line, or if staggered/late presentation. Check the paracetamol level at 4 h.",
      "Opioid overdose: respiratory depression, pinpoint pupils. Treat with naloxone, repeat as needed (shorter acting than most opioids).",
      "Benzodiazepine overdose: sedation, respiratory depression. Supportive care; flumazenil only in specific cases (risk of seizures).",
      "Tricyclic antidepressants: arrhythmias, seizures, anticholinergic features — sodium bicarbonate for a wide QRS. Serotonin syndrome: hyperthermia, agitation, clonus."
    ],
    "drugs": [
      {"name": "N-acetylcysteine (NAC)", "when": "Paracetamol overdose above the treatment line (or staggered/late)", "notes": "IV (or oral); most effective early; replenishes glutathione"},
      {"name": "Naloxone", "when": "Opioid overdose with respiratory depression", "notes": "IV/IM; short-acting — may need repeat/infusion"},
      {"name": "Sodium bicarbonate", "when": "TCA overdose with wide QRS/arrhythmia", "notes": "IV boluses; monitor pH and potassium"},
      {"name": "Flumazenil", "when": "Selected benzodiazepine toxicity", "notes": "Risk of seizures in chronic users/mixed overdose — rarely used"},
      {"name": "Activated charcoal", "when": "Early (<1 h) significant ingestion (specialist advice)", "notes": "Not for corrosives/hydrocarbons or impaired airway"}
    ],
    "clinicalScenarios": [
      {"scenario": "5 hours after a paracetamol overdose.", "answer": "Check the paracetamol level and give NAC if above the treatment line (or if staggered/late)."},
      {"scenario": "Opioid overdose with respiratory depression and pinpoint pupils.", "answer": "Naloxone IV/IM + airway support; repeat as naloxone is short-acting."},
      {"scenario": "TCA overdose with a widened QRS.", "answer": "Sodium bicarbonate boluses for cardiac protection; monitor for arrhythmia/seizures."},
      {"scenario": "Agitated, hyperthermic patient with clonus on serotonergic drugs.", "answer": "Serotonin syndrome — stop the offending drugs, supportive care, consider cyproheptadine (specialist)."},
      {"scenario": "Patient who took mixed drugs and is drowsy.", "answer": "Support the airway and breathing; avoid flumazenil; treat specific toxidromes; involve toxicology."}
    ],
    "keyValues": [
      ["Paracetamol", "NAC if above the treatment line (4 h level)"],
      ["Opioid", "Naloxone IV/IM, repeat"],
      ["TCA", "Sodium bicarbonate for wide QRS"],
      ["Activated charcoal", "Within 1 h of ingestion (if indicated)"]
    ],
    "redFlags": [
      "Paracetamol overdose — NAC urgently, don't wait for symptoms.",
      "Opioid with respiratory depression — naloxone, airway support.",
      "TCA with wide QRS/arrhythmia — sodium bicarbonate."
    ],
    "management": [
      "ABC, IV access, monitoring, identify the poison(s).",
      "Paracetamol: NAC per protocol, check levels.",
      "Opioid: naloxone, airway support.",
      "TCA: sodium bicarbonate for arrhythmia, treat seizures.",
      "Psychiatric assessment after medical stabilisation."
    ],
    "pitfalls": [
      "Paracetamol overdose can be asymptomatic early — always check the level.",
      "Avoid flumazenil in mixed overdoses and chronic benzodiazepine users (seizure risk).",
      "Naloxone's effect can wear off before the opioid does — watch for re-sedation."
    ]
  },

  "post-op-complications": {
    "name": "Post-operative complications",
    "group": "Surgery & peri-operative",
    "overview": "A deteriorating post-op patient has a defined differential (bleeding, infection, leak, PE, cardiac). The exam tests the systematic assessment and the red flags for return to theatre.",
    "essentials": [
      "Common early post-op complications: bleeding, infection (wound/chest/urine/line), VTE, urinary retention, ileus, anastomotic leak, cardiac (MI/arrhythmia/AF), respiratory (atelectasis, pneumonia, PE).",
      "Assess the deteriorating post-op patient systematically: ABC, observations (NEWS2), wound, drains, urine output, pain, fluid balance.",
      "Bleeding: falling Hb, hypotension, tachycardia, distended abdomen, bloody drains — resuscitate, consider return to theatre.",
      "Anastomotic leak: fever, peritonitis, rising inflammatory markers, usually days 3-7 — urgent CT/surgery.",
      "Ileus: abdominal distension, no bowel sounds, nausea — NBM, NG tube, correct electrolytes, mobilise. Distinguish from obstruction."
    ],
    "drugs": [
      {"name": "IV fluids/blood", "when": "Bleeding/hypovolaemia", "notes": "Resuscitate; crossmatch"},
      {"name": "IV antibiotics", "when": "Infection/leak", "notes": "Broad-spectrum; per local policy"},
      {"name": "LMWH (VTE prophylaxis)", "when": "All post-op patients unless contraindicated", "notes": "With TEDs and early mobilisation"},
      {"name": "Analgesia", "when": "Pain", "notes": "Multimodal; effective analgesia aids mobilisation and prevents ileus"},
      {"name": "Antiemetics", "when": "Nausea (ileus)", "notes": "With NG decompression and electrolyte correction"}
    ],
    "clinicalScenarios": [
      {"scenario": "Day 5 post-bowel surgery: fever, peritonism, rising CRP.", "answer": "Anastomotic leak — NBM, IV antibiotics, urgent CT/surgical review."},
      {"scenario": "Post-op hypotension, tachycardia and falling Hb with a distended abdomen.", "answer": "Post-operative bleeding — resuscitate, correct coagulopathy, consider return to theatre."},
      {"scenario": "Post-op distension, nausea and absent bowel sounds.", "answer": "Ileus — NBM, NG tube, correct electrolytes, mobilise; exclude obstruction."},
      {"scenario": "Sudden dyspnoea and hypoxia on day 3 post-op.", "answer": "Consider PE — assess and image (CTPA); also consider atelectasis/pneumonia."},
      {"scenario": "Post-op patient with new AF and tachycardia.", "answer": "Common after thoracic/cardiac surgery — treat the cause, rate-control, correct electrolytes."}
    ],
    "keyValues": [
      ["Anastomotic leak", "Fever + peritonitis, days 3-7 post-op"],
      ["Post-op AF", "Common after cardiac/thoracic surgery"],
      ["VTE prophylaxis", "LMWH + TEDs + early mobilisation"],
      ["Ileus", "NBM, NG, electrolytes, mobilise"]
    ],
    "redFlags": [
      "Hypotension + tachycardia + falling Hb — bleeding, resuscitate + return to theatre.",
      "Peritonitis/rigid abdomen post-op — anastomotic leak, urgent surgery.",
      "Sudden dyspnoea/hypoxia — PE, urgent assessment."
    ],
    "management": [
      "Systematic assessment (ABC, NEWS2, wound, drains, urine, fluids).",
      "Bleeding: resuscitate, correct coagulopathy, consider re-operation.",
      "Leak: NBM, IV antibiotics, urgent CT/surgery.",
      "Ileus: NBM, NG, electrolytes, mobilise; VTE prophylaxis."
    ],
    "pitfalls": [
      "A falling Hb and tachycardia are more reliable than BP for occult bleeding.",
      "Post-op fever has a differential — don't assume it is just a wound infection.",
      "Ileus can be prolonged — correct electrolytes and mobilise rather than simply starving."
    ]
  },

  "urine-retention": {
    "name": "Urine retention",
    "group": "Surgery & peri-operative",
    "overview": "A common ward problem that is usually easy to fix but can hide serious pathology. The exam tests recognising acute vs chronic retention and the dangers of high-pressure retention.",
    "essentials": [
      "Acute urinary retention = painful inability to pass urine with a palpable bladder. Causes: BPH, post-op (anaesthesia, analgesia), constipation, drugs (anticholinergics), neurological, urethral stricture.",
      "Chronic retention: painless, often with overflow incontinence and renal impairment (high-pressure retention is dangerous).",
      "Management: catheterise (urethral or suprapubic if urethral route fails), drain the bladder, measure residual volume, send urine for analysis.",
      "After catheterisation: monitor for post-obstructive diuresis and haematuria; check renal function.",
      "Investigate the cause: PSA, renal USS, flow studies, urology referral. Trial without catheter after treating the cause."
    ],
    "drugs": [
      {"name": "Urethral catheter / suprapubic catheter", "when": "Acute retention", "notes": "Drain <1 L at first to avoid decompression haematuria/haemodynamic shifts (protocol-dependent)"},
      {"name": "Tamsulosin (alpha-blocker)", "when": "BPH-related retention", "notes": "Relaxes prostatic smooth muscle; aids trial without catheter"},
      {"name": "Finasteride (5-alpha reductase inhibitor)", "when": "BPH (longer-term)", "notes": "Reduces prostate size over months"},
      {"name": "Treat constipation", "when": "Contributing cause", "notes": "Laxatives; constipation precipitates retention"}
    ],
    "clinicalScenarios": [
      {"scenario": "Post-op patient with a painful, palpable bladder unable to pass urine.", "answer": "Acute retention — catheterise and drain; measure residual; investigate the cause."},
      {"scenario": "Painless chronic retention with overflow incontinence and raised creatinine.", "answer": "High-pressure retention causing renal impairment — urgent drainage and renal assessment."},
      {"scenario": "Patient with retention and new neurological signs.", "answer": "Consider spinal cord cause (cauda equina) — urgent assessment and imaging."},
      {"scenario": "Elderly man with BPH in retention after a trial without catheter fails.", "answer": "Start an alpha-blocker (± 5-ARI), treat constipation, retry TWOC or plan urology review."}
    ],
    "keyValues": [
      ["Acute retention", "Painful, palpable bladder"],
      ["Chronic retention", "Painless, overflow, renal impairment risk"],
      ["Residual volume", ">300 mL suggests retention"],
      ["Post-obstructive diuresis", "Monitor fluid balance after drainage"]
    ],
    "redFlags": [
      "High-pressure chronic retention with renal failure — urgent drainage.",
      "Retention with neurological signs — spinal cause, urgent assessment.",
      "Post-obstructive diuresis — monitor for hypovolaemia."
    ],
    "management": [
      "Catheterise and drain the bladder; measure residual.",
      "Monitor for post-obstructive diuresis and haematuria.",
      "Investigate the cause (PSA, renal USS, urology).",
      "Trial without catheter after treating the cause."
    ],
    "pitfalls": [
      "Rapidly draining a chronically distended bladder can cause decompression haematuria/haemodynamic shifts — follow local volume guidance.",
      "Chronic retention can silently damage kidneys — always check renal function.",
      "Retention with back pain/neurology is a spinal emergency, not a simple catheter problem."
    ]
  },

  "medication-errors": {
    "name": "Medication administration errors",
    "group": "Ward systems & patient safety",
    "overview": "A patient-safety topic where the exam tests prevention (the 5 rights) and the correct response when an error happens (assess, treat, inform, report).",
    "essentials": [
      "Common error types: wrong drug, wrong dose, wrong route, wrong patient, wrong time, omission, prescribing errors, drug interactions.",
      "Prevent: check the '5 rights' (patient, drug, dose, route, time), use the BNF/formulary, check allergies, double-check high-risk drugs (insulin, opiates, anticoagulants, chemotherapy).",
      "If an error occurs: assess the patient immediately, stop the drug, treat any harm, inform the patient, report the incident (datix), document.",
      "High-risk situations: look-alike/sound-alike drugs, decimal-point errors, abbreviations, verbal orders, handover.",
      "Report and learn from errors — a 'no blame' culture improves safety. Involve pharmacy and senior staff."
    ],
    "drugs": [
      {"name": "Stop the drug / antidote if available", "when": "Error identified", "notes": "e.g. naloxone for opioid error, glucose for insulin error"},
      {"name": "Treat adverse effects", "when": "Harm from the error", "notes": "e.g. anaphylaxis protocol for a drug allergy given in error"},
      {"name": "Reporting (datix)", "when": "Every medication error", "notes": "Not punitive — improves system safety"}
    ],
    "clinicalScenarios": [
      {"scenario": "You gave a patient the wrong dose of insulin.", "answer": "Assess and monitor the patient (hypoglycaemia), treat harm, inform the patient, report (datix), document."},
      {"scenario": "A patient is given a drug they are allergic to.", "answer": "Stop the drug, assess for anaphylaxis, treat (IM adrenaline if needed), inform patient, report."},
      {"scenario": "You realise you prescribed a 10-fold overdose of an anticoagulant.", "answer": "Assess bleeding risk, stop/reverse as needed, inform the patient and senior staff, report the incident."},
      {"scenario": "Preventing errors during a busy drug round.", "answer": "Use the 5 rights, check allergies, avoid interruptions, double-check high-risk drugs."}
    ],
    "keyValues": [
      ["5 rights", "Patient, drug, dose, route, time"],
      ["High-risk drugs", "Insulin, opiates, anticoagulants, chemotherapy"],
      ["On error", "Assess, stop, treat, inform, report, document"],
      ["Report", "Datix/incident reporting"]
    ],
    "redFlags": [
      "Wrong drug/dose given to a patient — assess for harm immediately.",
      "Insulin or anticoagulant error — can be life-threatening, urgent review.",
      "Known allergy given — treat anaphylaxis if present."
    ],
    "management": [
      "Prevent: 5 rights, check allergies, double-check high-risk drugs.",
      "On error: assess the patient, stop the drug, treat harm, inform the patient.",
      "Report the incident and document.",
      "Review systems to prevent recurrence."
    ],
    "pitfalls": [
      "Never hide a medication error — reporting protects future patients.",
      "Decimal-point and look-alike/sound-alike drug errors are common — double-check high-risk drugs.",
      "Always check allergies before administering any drug."
    ]
  },

  "early-warning-score": {
    "name": "The Early Warning Score",
    "group": "Ward systems & patient safety",
    "overview": "NEWS2 is the backbone of recognising deterioration. The exam tests the scoring thresholds and the correct escalation response.",
    "essentials": [
      "NEWS2 aggregates: respiratory rate, oxygen saturations, oxygen requirement, systolic BP, heart rate, consciousness (AVPU), temperature.",
      "Each parameter scores 0-3; the total triggers a response: low (1-4) increased monitoring; medium (5-6) urgent review; high (≥7) emergency response.",
      "NEWS2 ≥5 is a trigger for sepsis screening. A single parameter scoring 3 also warrants attention.",
      "Escalate promptly: call for help, use SBAR (Situation, Background, Assessment, Recommendation) to communicate.",
      "The score guides, but clinical judgement overrides — a patient who looks unwell needs review regardless of score."
    ],
    "drugs": [
      {"name": "Oxygen", "when": "Hypoxia on the score", "notes": "Titrate to target"},
      {"name": "IV fluids", "when": "Hypoperfusion/hypotension", "notes": "Per assessment"},
      {"name": "Sepsis Six", "when": "NEWS2 ≥5 with suspected infection", "notes": "Cultures, antibiotics, fluids, lactate, oxygen, urine output"},
      {"name": "Escalation (SBAR)", "when": "Score rises", "notes": "Structured communication to the senior/outreach team"}
    ],
    "clinicalScenarios": [
      {"scenario": "NEWS2 of 8.", "answer": "Emergency response — call for help immediately (critical care outreach); assess and treat."},
      {"scenario": "NEWS2 of 5 in a patient with a cough.", "answer": "Urgent review + sepsis screening (Sepsis Six if criteria met)."},
      {"scenario": "A single parameter (respiratory rate) scores 3.", "answer": "Warrants attention even if the total is low — escalate and reassess."},
      {"scenario": "A patient looks unwell but the NEWS2 is low.", "answer": "Clinical judgement overrides the score — escalate for review."}
    ],
    "keyValues": [
      ["NEWS2 low", "1-4 → increased monitoring"],
      ["NEWS2 medium", "5-6 → urgent review"],
      ["NEWS2 high", "≥7 → emergency response"],
      ["Sepsis trigger", "NEWS2 ≥5 → screen for sepsis"],
      ["SBAR", "Situation, Background, Assessment, Recommendation"]
    ],
    "redFlags": [
      "NEWS2 ≥7 — emergency response, call for help immediately.",
      "Single parameter score of 3 — warrants attention.",
      "Deteriorating trend — escalate even if the score is not yet high."
    ],
    "management": [
      "Measure and record NEWS2 regularly.",
      "Escalate per the score using SBAR.",
      "Screen for sepsis if NEWS2 ≥5.",
      "Clinical judgement overrides the score."
    ],
    "pitfalls": [
      "A rising trend matters even below the threshold — don't wait for a high score.",
      "Incomplete observations invalidate the score — always record all parameters.",
      "Don't let a 'normal' score override a patient who looks unwell."
    ]
  },

  "venous-access-lines": {
    "name": "Management of venous access lines",
    "group": "Ward systems & patient safety",
    "overview": "Central lines, PICCs and cannulae cause infection and mechanical complications. The exam tests recognising line sepsis and the air embolism emergency.",
    "essentials": [
      "Central venous catheters, PICC lines and peripheral cannulae are sources of infection (line sepsis) and complications (thrombosis, air embolism, dislodgement).",
      "Line sepsis: fever + line in situ — take blood cultures (peripheral + line), consider removing the line, treat with antibiotics.",
      "Line thrombosis: arm/neck swelling/pain — USS, anticoagulation, consider line removal.",
      "Air embolism: sudden collapse, hypoxia — clamp the line, left lateral/head-down position, 100% oxygen.",
      "Care: aseptic technique for insertion and access, daily review of line necessity, remove when no longer needed, document."
    ],
    "drugs": [
      {"name": "IV antibiotics", "when": "Line sepsis", "notes": "After cultures; per local policy; consider line removal"},
      {"name": "Anticoagulation", "when": "Line-associated thrombosis", "notes": "Per protocol; consider line removal"},
      {"name": "Sexual/mucosal line locks (selected)", "when": "Specific catheters (specialist)", "notes": "e.g. taurolidine/ethanol locks for recurrent infection"},
      {"name": "High-flow oxygen + left lateral positioning", "when": "Air embolism", "notes": "Clamp the line first"}
    ],
    "clinicalScenarios": [
      {"scenario": "Fever in a patient with a central line.", "answer": "Consider line sepsis — blood cultures (peripheral + line), antibiotics, consider line removal."},
      {"scenario": "Sudden collapse with hypoxia while a central line is being used.", "answer": "Air embolism — clamp the line, head-down/left lateral, 100% oxygen, call for help."},
      {"scenario": "Arm swelling and pain in a patient with a PICC line.", "answer": "Line-associated thrombosis — USS, anticoagulation, consider removal."},
      {"scenario": "A cannula has been in situ for several days with no ongoing need.", "answer": "Remove it — daily review of line necessity reduces infection."}
    ],
    "keyValues": [
      ["Line sepsis", "Fever + line → cultures, consider removal"],
      ["Air embolism", "Clamp, head-down/left lateral, 100% O2"],
      ["Line thrombosis", "USS, anticoagulation"],
      ["Review", "Daily — remove when no longer needed"]
    ],
    "redFlags": [
      "Fever in a patient with a line — line sepsis, cultures + consider removal.",
      "Sudden collapse with a line — air embolism, emergency.",
      "Arm/neck swelling — line thrombosis."
    ],
    "management": [
      "Aseptic technique for insertion and access.",
      "Line sepsis: cultures, antibiotics, consider removal.",
      "Thrombosis: USS, anticoagulation.",
      "Daily review; remove lines when no longer needed."
    ],
    "pitfalls": [
      "Air embolism is the classic 'clamp first, then position' emergency — act immediately.",
      "Unnecessary lines cause infection — review daily and remove early.",
      "Always culture both peripheral and line blood in suspected line sepsis."
    ]
  },

  "covid-19": {
    "name": "Issues around COVID-19",
    "group": "Miscellaneous",
    "overview": "A systemic respiratory illness with thrombotic and secondary-infection complications. The exam tests severity assessment (silent hypoxia) and evidence-based treatment (dexamethasone when oxygen needed).",
    "essentials": [
      "COVID-19: SARS-CoV-2 infection causing respiratory illness — spectrum from asymptomatic to severe pneumonia/ARDS. Risk factors: age, obesity, diabetes, cardiovascular disease, immunocompromise.",
      "Presentation: fever, cough, dyspnoea, anosmia, fatigue. Severe: hypoxia, respiratory distress, bilateral infiltrates ('silent hypoxia' can occur).",
      "Assess severity: oxygen saturations, respiratory rate, NEWS2, chest X-ray, inflammatory markers (CRP, ferritin, D-dimer).",
      "Management: oxygen to target, dexamethasone for those needing oxygen, antivirals/anticoagulation per protocol, treat complications (thrombosis, secondary infection).",
      "Infection control: isolation, PPE, vaccination. Monitor for deterioration."
    ],
    "drugs": [
      {"name": "Dexamethasone", "when": "COVID-19 requiring oxygen (or ventilated)", "notes": "Reduces mortality; not for those not needing oxygen"},
      {"name": "Remdesivir / other antivirals", "when": "Selected patients (protocol)", "notes": "Per local/national guidance"},
      {"name": "Prophylactic/therapeutic anticoagulation", "when": "COVID-19 (thrombotic risk)", "notes": "Per protocol; higher dose if confirmed thrombosis"},
      {"name": "Oxygen (escalating devices)", "when": "Hypoxia", "notes": "Target 94-98% (88-92% if hypercapnia risk); consider CPAP/HFNO, then NIV/ICU"},
      {"name": "Antibiotics", "when": "Secondary bacterial infection", "notes": "Not routine in pure viral infection"}
    ],
    "clinicalScenarios": [
      {"scenario": "COVID-19 patient with saturations 90% on air.", "answer": "Oxygen to target 94-98%; start dexamethasone (needs oxygen); monitor and consider escalation."},
      {"scenario": "COVID-19 patient with a rising oxygen requirement and tachypnoea.", "answer": "Worsening ARDS — escalate (CPAP/HFNO/ICU); treat thrombosis risk; involve critical care."},
      {"scenario": "COVID-19 patient with pleuritic pain and hypoxia beyond the pneumonia.", "answer": "Consider PE (increased thrombotic risk) — assess and image per protocol."},
      {"scenario": "COVID-19 patient with new fever and purulent sputum later in admission.", "answer": "Consider secondary bacterial infection — cultures and targeted antibiotics."}
    ],
    "keyValues": [
      ["O2 target", "94-98% (88-92% if hypercapnia risk)"],
      ["Dexamethasone", "For patients needing oxygen"],
      ["Risk factors", "Age, obesity, diabetes, CVD, immunocompromise"],
      ["Complications", "Thrombosis, ARDS, secondary infection"]
    ],
    "redFlags": [
      "Hypoxia (silent) — check saturations, escalate.",
      "Rapid deterioration or rising oxygen requirement — ARDS, ICU.",
      "Thrombosis (PE, stroke) — anticoagulation."
    ],
    "management": [
      "Oxygen to target, monitor saturations and NEWS2.",
      "Dexamethasone for those needing oxygen; other antivirals per protocol.",
      "Anticoagulation for thrombosis risk.",
      "Isolation + PPE; escalate to ICU if deteriorating."
    ],
    "pitfalls": [
      "'Silent hypoxia' — patients can be profoundly hypoxic without feeling breathless; rely on saturations.",
      "Dexamethasone only helps those needing oxygen — not for mild disease.",
      "Remember the thrombotic risk — consider PE in a deteriorating COVID-19 patient."
    ]
  },
}
