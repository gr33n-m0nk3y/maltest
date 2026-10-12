# Clinical notes part 3: obs/gynae, dermatology, infection, resuscitation, surgery, ward systems, covid.
PART = {
  "obs-gynae-emergencies": {
    "name": "Gynaecology and Obstetric emergencies",
    "group": "Obstetrics & gynaecology",
    "essentials": [
      "Ectopic pregnancy: pregnancy + abdominal pain/bleeding/collapse. Ruptured ectopic is a surgical emergency (haemorrhagic shock). Always consider in any woman of reproductive age with abdominal pain — do a pregnancy test.",
      "Miscarriage: vaginal bleeding in early pregnancy; threatened, inevitable, missed, complete. USS confirms. Manage expectantly/medically/surgically (ERPC).",
      "Antepartum haemorrhage (APH): bleeding after 24 weeks — placenta praevia (painless) vs placental abruption (painful, rigid uterus, fetal distress). Both are emergencies.",
      "Postpartum haemorrhage (PPH): >500 mL (vaginal) or >1000 mL (CS) blood loss. Treat: call for help, IV access, fluids/blood, uterotonics (oxytocin, ergometrine), massage, identify cause (4 Ts: tone, trauma, tissue, thrombin).",
      "Pre-eclampsia/eclampsia: hypertension + proteinuria after 20 weeks; headache, visual disturbance, epigastric pain are red flags. Treat with magnesium sulfate (eclampsia), control BP, deliver."
    ],
    "keyValues": [
      ["Ectopic", "Pregnancy + pain/bleeding/collapse — emergency"],
      ["PPH", ">500 mL (vaginal) / >1000 mL (CS)"],
      ["PPH 4 Ts", "Tone, trauma, tissue, thrombin"],
      ["Pre-eclampsia", "HTN + proteinuria after 20 weeks"],
      ["Eclampsia Rx", "Magnesium sulfate"]
    ],
    "redFlags": [
      "Ruptured ectopic (collapse, shoulder-tip pain) — immediate surgery.",
      "Placental abruption (painful, rigid abdomen, fetal distress) — emergency delivery.",
      "Eclampsia (seizures) — magnesium sulfate, control BP, urgent delivery."
    ],
    "management": [
      "Always pregnancy-test women of reproductive age with abdominal pain.",
      "Ectopic: IV access, crossmatch, urgent gynae/surgery.",
      "PPH: call for help, fluids/blood, uterotonics, massage, treat the cause.",
      "Pre-eclampsia: monitor BP, magnesium for eclampsia, control BP, deliver."
    ]
  },
  "skin-rashes": {
    "name": "Skin rashes in the acute setting",
    "group": "Dermatology",
    "essentials": [
      "Identify life-threatening rashes first: meningococcal septicaemia (non-blanching purpura, fever, ill), toxic epidermal necrolysis/Stevens-Johnson (blistering, mucosal involvement, drug-induced), necrotising fasciitis (severe pain, rapidly spreading), anaphylaxis (urticaria + systemic).",
      "Non-blanching purpura + fever = meningococcal until proven otherwise — IV antibiotics immediately.",
      "Common rashes: urticaria (allergic, itchy, blanch), cellulitis (erythema, warmth, pain, fever), shingles (vesicular, dermatomal, painful), scabies (itchy, burrows), drug eruptions.",
      "Assess: distribution, morphology (macule, papule, vesicle, bulla, purpura), mucosal involvement, systemic symptoms, drug history.",
      "Cellulitis: IV/oral antibiotics, mark the edge, monitor. Erysipelas: superficial, well-demarcated."
    ],
    "keyValues": [
      ["Meningococcal", "Non-blanching purpura + fever → IV antibiotics"],
      ["TEN/SJS", "Blistering + mucosal involvement, drug-induced"],
      ["Cellulitis", "Erythema + warmth + pain + fever"],
      ["Shingles", "Vesicular, dermatomal, painful"]
    ],
    "redFlags": [
      "Non-blanching rash + fever/ill — meningococcal, treat immediately.",
      "Rapidly spreading painful erythema — necrotising fasciitis.",
      "Blistering + mucosal involvement — SJS/TEN, stop culprit drug."
    ],
    "management": [
      "ABC; treat life-threatening rashes immediately (meningococcal antibiotics).",
      "Cellulitis: antibiotics, mark edge, monitor response.",
      "Urticaria: antihistamines, remove trigger, treat anaphylaxis if systemic.",
      "Identify and stop culprit drugs in drug eruptions."
    ]
  },
  "febrile-patient": {
    "name": "The febrile patient",
    "group": "Infection & sepsis",
    "essentials": [
      "Fever = temperature ≥38°C. Assess for sepsis (infection + organ dysfunction) using NEWS2 and clinical judgement. Sepsis is time-critical — treat within 1 hour.",
      "Sepsis Six: oxygen, blood cultures, IV antibiotics, IV fluids, lactate, urine output. Give antibiotics within 1 hour of suspected sepsis.",
      "Find the source: respiratory (cough, sputum, chest signs), urinary (dysuria, loin pain), skin/soft tissue, line, abdominal, CNS (meningitis), endocarditis.",
      "Risk factors for poor outcome: elderly, immunocompromised (neutropenia, steroids, HIV), malignancy, diabetes, pregnancy, indwelling devices.",
      "Monitor: observations (NEWS2), lactate, cultures, response to antibiotics. Escalate if deteriorating or not improving."
    ],
    "keyValues": [
      ["Sepsis", "Infection + organ dysfunction"],
      ["Antibiotics within", "1 hour of suspected sepsis"],
      ["Sepsis Six", "O2, cultures, antibiotics, fluids, lactate, urine output"],
      ["Lactate", ">2 mmol/L suggests hypoperfusion"]
    ],
    "redFlags": [
      "NEWS2 ≥ 5 or lactate > 2 — sepsis, treat urgently.",
      "Hypotension/shock — aggressive resuscitation + antibiotics.",
      "Fever in neutropenic/immunocompromised — treat as sepsis immediately."
    ],
    "management": [
      "Sepsis Six within 1 hour: O2, cultures, antibiotics, fluids, lactate, urine output.",
      "Identify and treat the source.",
      "Monitor response; escalate if deteriorating.",
      "Consider immunocompromise and adjust accordingly."
    ]
  },
  "infection-control": {
    "name": "Infection control on the ward",
    "group": "Infection & sepsis",
    "essentials": [
      "Hand hygiene is the single most important measure — 'bare below the elbows', alcohol hand rub, wash with soap/water for C. difficile and norovirus.",
      "Standard precautions: gloves, aprons, safe sharps disposal, correct waste segregation, respiratory hygiene (cough etiquette).",
      "Transmission-based precautions: contact (MRSA, C. difficile, ESBL — gloves/aprons, isolation), droplet (influenza, meningococcal — surgical mask), airborne (TB, measles, chickenpox — negative pressure, FFP3).",
      "Isolate patients with suspected/confirmed transmissible infections; notify infection control.",
      "Antimicrobial stewardship: prescribe antibiotics appropriately, review at 48h, use narrow-spectrum where possible, document indication and duration."
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
      "Meningococcal — droplet precautions + urgent antibiotics + prophylaxis for contacts."
    ],
    "management": [
      "Hand hygiene and standard precautions always.",
      "Isolate and apply appropriate precautions for transmissible infections.",
      "Notify infection control; follow local policy.",
      "Antimicrobial stewardship: document indication, review at 48h."
    ]
  },
  "cpr": {
    "name": "Cardiopulmonary resuscitation",
    "group": "Resuscitation & emergencies",
    "essentials": [
      "Recognise cardiac arrest: unresponsive + not breathing normally (agonal gasps count as not breathing). Call for help, start CPR immediately.",
      "Adult CPR: 30:2 compressions:ventilation, rate 100-120/min, depth 5-6 cm, minimise interruptions. Use AED/defibrillator as soon as available.",
      "Shockable rhythms (VF/pulseless VT): defibrillate, then CPR, adrenaline 1 mg after 2nd shock, repeat adrenaline every 3-5 min, amiodarone after 3rd shock.",
      "Non-shockable (PEA/asystole): adrenaline 1 mg immediately, then every 3-5 min. Find and treat reversible causes (4 Hs and 4 Ts).",
      "4 Hs: hypoxia, hypovolaemia, hyper/hypokalaemia, hypothermia. 4 Ts: tension pneumothorax, tamponade, toxins, thrombosis (PE/MI)."
    ],
    "keyValues": [
      ["CPR ratio", "30:2, 100-120/min, depth 5-6 cm"],
      ["Adrenaline", "1 mg IV every 3-5 min"],
      ["Shockable", "VF/pulseless VT → defibrillate"],
      ["4 Hs / 4 Ts", "Hypoxia, hypovolaemia, K+, hypothermia / tension, tamponade, toxins, thrombosis"]
    ],
    "redFlags": [
      "VF/pulseless VT — defibrillate immediately, don't delay for drugs.",
      "Tension pneumothorax during arrest — needle decompression.",
      "Reversible causes — treat them (the only way to achieve ROSC in PEA)."
    ],
    "management": [
      "Call for help, start high-quality CPR, attach defibrillator.",
      "Follow the ALS algorithm (shockable vs non-shockable).",
      "Give adrenaline per protocol; treat reversible causes.",
      "Post-ROSC: ABC, targeted temperature management, treat the cause, ICU."
    ]
  },
  "anaphylaxis": {
    "name": "Anaphylaxis",
    "group": "Resuscitation & emergencies",
    "essentials": [
      "Anaphylaxis = severe, life-threatening systemic hypersensitivity reaction. Rapid onset: airway (stridor, swelling), breathing (wheeze, dyspnoea), circulation (hypotension, collapse), plus skin (urticaria, angioedema).",
      "Immediate: remove trigger, call for help, IM adrenaline 500 mcg (0.5 mL of 1:1000) anterolateral thigh, repeat after 5 min if no improvement.",
      "Adjunctive: high-flow oxygen, IV fluids (for hypotension), antihistamine (chlorphenamine), steroid (hydrocortisone) — but adrenaline is first-line and life-saving.",
      "Position: lie flat with legs raised (unless breathing difficulty — sit up); do not sit/stand a hypotensive patient abruptly.",
      "Observe for biphasic reaction (recurrence hours later) — monitor for at least 6-12h. Arrange follow-up and an adrenaline auto-injector."
    ],
    "keyValues": [
      ["Adrenaline (IM)", "500 mcg (0.5 mL 1:1000), repeat after 5 min"],
      ["Adrenaline site", "Anterolateral thigh"],
      ["Adjunctive", "O2, IV fluids, chlorphenamine, hydrocortisone"],
      ["Observation", "≥6-12h for biphasic reaction"]
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
    ]
  },
  "overdoses": {
    "name": "Overdoses",
    "group": "Resuscitation & emergencies",
    "essentials": [
      "Assess ABC and treat the patient, not just the poison. Identify the substance, dose, time, and co-ingestants (paracetamol + alcohol common).",
      "Paracetamol overdose: hepatotoxic. Treat with N-acetylcysteine (NAC) if levels above the treatment line or staggered/late presentation. Check paracetamol level at 4h.",
      "Opioid overdose: respiratory depression, pinpoint pupils. Treat with naloxone (IV/IM), repeat as needed (shorter than opioid).",
      "Benzodiazepine overdose: sedation, respiratory depression. Supportive care; flumazenil only in specific cases (risk of seizures).",
      "Tricyclic antidepressants: arrhythmias, seizures, anticholinergic. Sodium bicarbonate for wide QRS. Serotonin syndrome: hyperthermia, agitation, clonus."
    ],
    "keyValues": [
      ["Paracetamol", "NAC if level above treatment line (4h level)"],
      ["Opioid", "Naloxone IV/IM, repeat"],
      ["TCA", "Sodium bicarbonate for wide QRS"],
      ["Activated charcoal", "Within 1h of ingestion (if indicated)"]
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
    ]
  },
  "post-op-complications": {
    "name": "Post-operative complications",
    "group": "Surgery & peri-operative",
    "essentials": [
      "Common early post-op complications: bleeding, infection (wound, chest, urine, line), VTE, urinary retention, ileus, anastomotic leak, cardiac (MI, arrhythmia, AF), respiratory (atelectasis, pneumonia, PE).",
      "Assess the deteriorating post-op patient systematically: ABC, observations (NEWS2), wound, drains, urine output, pain, fluid balance.",
      "Bleeding: falling Hb, hypotension, tachycardia, distended abdomen, bloody drains — resuscitate, consider return to theatre.",
      "Anastomotic leak: fever, peritonitis, rising inflammatory markers, usually days 3-7 — urgent CT/surgery.",
      "Ileus: abdominal distension, no bowel sounds, nausea — NBM, NG tube, correct electrolytes, mobilise. Distinguish from obstruction."
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
    ]
  },
  "urine-retention": {
    "name": "Urine retention",
    "group": "Surgery & peri-operative",
    "essentials": [
      "Acute urinary retention = painful inability to pass urine, usually with a palpable bladder. Common causes: BPH, post-op (anaesthesia, analgesia), constipation, drugs (anticholinergics), neurological, urethral stricture.",
      "Chronic retention: painless, often with overflow incontinence and renal impairment (high-pressure retention is dangerous).",
      "Management: catheterise (urethral or suprapubic if urethral route fails), drain the bladder, measure residual volume, send urine for analysis.",
      "After catheterisation: monitor for post-obstructive diuresis and haematuria; check renal function.",
      "Investigate the cause: PSA, renal USS, flow studies, urology referral. Trial without catheter after treating the cause."
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
    ]
  },
  "medication-errors": {
    "name": "Medication administration errors",
    "group": "Ward systems & patient safety",
    "essentials": [
      "Medication errors are common and preventable. Common types: wrong drug, wrong dose, wrong route, wrong patient, wrong time, omission, prescribing errors, drug interactions.",
      "Prevent: check the '5 rights' (patient, drug, dose, route, time), use the BNF/formulary, check allergies, double-check high-risk drugs (insulin, opiates, anticoagulants, chemotherapy), use electronic prescribing where available.",
      "If an error occurs: assess the patient immediately (harm?), stop the drug, treat any adverse effects, inform the patient, report the incident (datix), document.",
      "High-risk situations: look-alike/sound-alike drugs, decimal point errors, abbreviations, verbal orders, handover.",
      "Report and learn from errors — a 'no blame' culture improves safety. Involve pharmacy and senior staff."
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
      "On error: assess patient, stop drug, treat harm, inform patient.",
      "Report the incident and document.",
      "Review systems to prevent recurrence."
    ]
  },
  "early-warning-score": {
    "name": "The Early Warning Score",
    "group": "Ward systems & patient safety",
    "essentials": [
      "NEWS2 (National Early Warning Score) aggregates physiological parameters to identify deteriorating patients: respiratory rate, oxygen saturations, oxygen requirement, systolic BP, heart rate, consciousness (AVPU), temperature.",
      "Each parameter scores 0-3; total score triggers a response: low (1-4) → increased monitoring; medium (5-6) → urgent review; high (≥7) → emergency response (often critical care outreach).",
      "NEWS2 ≥5 is a trigger for sepsis screening. A single score of 3 in any parameter also warrants attention.",
      "Escalate promptly: call for help, use SBAR (Situation, Background, Assessment, Recommendation) to communicate.",
      "The score guides, but clinical judgement overrides — a patient who looks unwell needs review regardless of score."
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
      "Deteriorating trend — escalate even if score not yet high."
    ],
    "management": [
      "Measure and record NEWS2 regularly.",
      "Escalate per the score using SBAR.",
      "Screen for sepsis if NEWS2 ≥5.",
      "Clinical judgement overrides the score."
    ]
  },
  "venous-access-lines": {
    "name": "Management of venous access lines",
    "group": "Ward systems & patient safety",
    "essentials": [
      "Central venous catheters (CVC), PICC lines, and peripheral cannulae are sources of infection (line sepsis) and complications (thrombosis, air embolism, dislodgement).",
      "Line sepsis: fever + line in situ → take blood cultures (peripheral + line), consider removing the line, treat with antibiotics. Exit-site infection: erythema, discharge.",
      "Line thrombosis: arm/neck swelling, pain — USS, anticoagulation, consider line removal.",
      "Air embolism: sudden collapse, hypoxia — clamp the line, left lateral/head-down position, 100% oxygen.",
      "Care: aseptic technique for insertion and access, daily review of line necessity, remove when no longer needed, document."
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
    ]
  },
  "covid-19": {
    "name": "Issues around COVID-19",
    "group": "Miscellaneous",
    "essentials": [
      "COVID-19: SARS-CoV-2 infection causing respiratory illness; spectrum from asymptomatic to severe pneumonia/ARDS. Risk factors: age, obesity, diabetes, cardiovascular disease, immunocompromise.",
      "Presentation: fever, cough, dyspnoea, anosmia, fatigue. Severe: hypoxia, respiratory distress, bilateral infiltrates.",
      "Assess severity: oxygen saturations, respiratory rate, NEWS2, chest X-ray, inflammatory markers (CRP, ferritin, D-dimer).",
      "Management: oxygen to target, dexamethasone (for those needing oxygen), consider remdesivir/anticoagulation per protocol, treat complications (thrombosis, secondary infection).",
      "Infection control: isolation, PPE, vaccination. Monitor for deterioration (silent hypoxia)."
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
    ]
  },
}
