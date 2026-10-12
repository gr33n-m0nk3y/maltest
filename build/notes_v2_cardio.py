# Enhanced notes v2 — exam-focused depth + clinical scenarios. Cardiovascular batch (8 topics).
PART = {
  "anticoagulation": {
    "name": "Anticoagulation management: INR and APTT",
    "group": "Cardiovascular",
    "overview": "Every ward has patients on anticoagulants, and the exam tests whether you can interpret the monitoring tests (INR/APTT), match the drug to the indication, and reverse bleeding safely. The trap is choosing the wrong anticoagulant for a given scenario (e.g. a DOAC in a mechanical valve).",
    "essentials": [
      "Warfarin inhibits vitamin K-dependent factors (II, VII, IX, X) plus proteins C and S. Full effect is delayed, so acute thrombosis needs bridging with a rapidly-acting agent (LMWH/heparin) until the INR is therapeutic.",
      "Heparin (unfractionated) works via antithrombin III and is monitored by APTT; LMWH (enoxaparin) is weight-dosed and usually needs no monitoring. APTT is also prolonged in DIC and factor deficiencies.",
      "Target INR: 2.0-3.0 for most indications (AF, VTE); 2.5-3.5 for a mechanical mitral valve or recurrent thrombosis on warfarin.",
      "The route of monitoring drives the choice: warfarin needs regular INR; DOACs do not need routine monitoring but are contraindicated in mechanical valves and antiphospholipid syndrome.",
      "Reversal is drug-specific: warfarin → vitamin K + PCC; heparin → protamine; dabigatran → idarucizumab; Xa inhibitors → andexanet alfa (or PCC if unavailable)."
    ],
    "drugs": [
      {"name": "Warfarin", "when": "AF, VTE, mechanical heart valves, antiphospholipid syndrome", "notes": "Target INR 2-3 (2.5-3.5 mechanical mitral); needs monitoring; many food/drug interactions; teratogenic (avoid in pregnancy)"},
      {"name": "Apixaban / Rivaroxaban (Xa inhibitors)", "when": "Non-valvular AF; VTE treatment and prophylaxis; rivaroxaban also post-ACS", "notes": "No routine INR; dose-adjusted for renal function/age; contraindicated in mechanical valves and APS"},
      {"name": "Dabigatran (direct thrombin inhibitor)", "when": "Non-valvular AF; VTE", "notes": "Caution if CrCl <30; dyspepsia common; reversal = idarucizumab"},
      {"name": "Edoxaban", "when": "Non-valvular AF; VTE (after initial parenteral therapy)", "notes": "Reduce dose if CrCl 15-50"},
      {"name": "LMWH (enoxaparin)", "when": "VTE treatment/prophylaxis; pregnancy (drug of choice); cancer-associated VTE; bridging warfarin", "notes": "Weight-based; reduce/avoid if CrCl <30; monitor anti-Xa only in special cases (pregnancy, renal impairment, obesity)"},
      {"name": "Unfractionated heparin (UFH)", "when": "ACS; when rapid on/off is needed; severe renal impairment; during procedures", "notes": "Monitor APTT (target 1.5-2.5x control); reversal = protamine sulfate"},
      {"name": "Reversal agents", "when": "Major bleeding on anticoagulation", "notes": "Warfarin → IV vitamin K + PCC; heparin → protamine; dabigatran → idarucizumab; Xa inhibitors → andexanet alfa"}
    ],
    "clinicalScenarios": [
      {"scenario": "A 70-year-old with AF has a mechanical mitral valve. Which anticoagulant?", "answer": "Warfarin (target INR 2.5-3.5). DOACs are contraindicated in mechanical valves."},
      {"scenario": "A pregnant woman (12 weeks) has a confirmed DVT.", "answer": "LMWH — it does not cross the placenta. Warfarin (teratogenic) and DOACs (avoid) are contraindicated."},
      {"scenario": "New AF in a 62-year-old with normal renal function and no valve disease.", "answer": "A DOAC is now preferred over warfarin (no monitoring, fewer interactions); anticoagulate per CHA2DS2-VASc."},
      {"scenario": "INR 8.4 with no bleeding.", "answer": "Withhold warfarin, give oral vitamin K, recheck INR. No PCC unless bleeding."},
      {"scenario": "INR 6.8 with haematemesis and hypotension.", "answer": "Major bleeding — IV vitamin K + prothrombin complex concentrate (PCC) + resuscitate."},
      {"scenario": "AF with CrCl 20 mL/min.", "answer": "Apixaban (dose-reduced) or warfarin; avoid dabigatran (renally cleared)."}
    ],
    "keyValues": [
      ["INR therapeutic (most indications)", "2.0-3.0"],
      ["INR therapeutic (mechanical mitral valve, recurrent VTE)", "2.5-3.5"],
      ["APTT therapeutic (UFH)", "1.5-2.5 × control"],
      ["Warfarin reversal (major bleeding)", "IV vitamin K + PCC"],
      ["Dabigatran reversal", "Idarucizumab"],
      ["Xa inhibitor reversal", "Andexanet alfa (or PCC)"],
      ["Heparin reversal", "Protamine sulfate"]
    ],
    "redFlags": [
      "Major bleeding on any anticoagulant (intracranial, GI, retroperitoneal) — reverse urgently, don't just withhold.",
      "INR > 5.0 with bleeding — emergency, give PCC.",
      "New thrombosis despite therapeutic anticoagulation — consider compliance, drug interaction, or occult malignancy."
    ],
    "management": [
      "Bleeding on warfarin: stop warfarin, IV vitamin K, PCC, recheck INR.",
      "Bleeding on heparin: stop infusion, give protamine sulfate.",
      "Bleeding on dabigatran: idarucizumab. On a Xa inhibitor: andexanet alfa.",
      "Subtherapeutic INR with high thrombotic risk: re-dose warfarin, consider bridging with LMWH.",
      "Always check for interacting drugs (antibiotics, amiodarone, NSAIDs) when INR swings."
    ],
    "pitfalls": [
      "DOACs are NOT interchangeable with warfarin — they are contraindicated in mechanical valves and antiphospholipid syndrome.",
      "Warfarin takes days for full effect — never rely on it alone for acute thrombosis.",
      "APTT does not monitor DOACs or warfarin — don't be misled by a normal APTT in a patient on apixaban."
    ]
  },

  "chest-pain": {
    "name": "Chest pain",
    "group": "Cardiovascular",
    "overview": "Chest pain is a 'rule out the killers first' topic. The exam expects you to identify ACS and the other immediately life-threatening causes within the first minutes, then treat.",
    "essentials": [
      "First exclude the life-threatening causes: acute coronary syndrome, aortic dissection, pulmonary embolism, tension pneumothorax, oesophageal rupture.",
      "ACS: central crushing pain radiating to arm/jaw, with sweating/nausea; may be atypical in women, diabetics and the elderly. ECG changes + troponin rise confirm.",
      "Aortic dissection: sudden severe 'tearing' pain radiating to the back, with a pulse/BP differential and widened mediastinum — a surgical emergency.",
      "PE: pleuritic pain, dyspnoea, hypoxia, tachycardia, with risk factors (immobility, surgery, malignancy, OCP).",
      "Non-cardiac causes: musculoskeletal, GORD, anxiety, and pericarditis (positional/pleuritic, relieved by leaning forward)."
    ],
    "drugs": [
      {"name": "Aspirin", "when": "Suspected ACS", "notes": "300 mg chewed/loading dose — give early unless true allergy"},
      {"name": "GTN / nitrates", "when": "ACS, ischaemic pain, pulmonary oedema", "notes": "Contraindicated in hypotension, severe aortic stenosis, and on PDE5 inhibitors (sildenafil)"},
      {"name": "Morphine", "when": "Severe ischaemic pain unresponsive to nitrates", "notes": "IV, titrated; may cause hypotension and vomiting"},
      {"name": "Beta-blocker", "when": "ACS (if no contraindication), aortic dissection (rate control)", "notes": "Avoid in cardiogenic shock, severe asthma, high-grade heart block"},
      {"name": "Anticoagulant (LMWH/heparin)", "when": "ACS, confirmed PE", "notes": "Per ACS pathway; do not delay reperfusion for it"}
    ],
    "clinicalScenarios": [
      {"scenario": "58-year-old, central crushing chest pain, ST elevation in II/III/aVF.", "answer": "STEMI — activate primary PCI immediately; give aspirin. Do not wait for troponin."},
      {"scenario": "65-year-old, sudden tearing chest pain radiating to the back, 30 mmHg BP difference between arms.", "answer": "Aortic dissection — control BP/HR with a beta-blocker, urgent CT aortogram, surgical referral."},
      {"scenario": "30-year-old on the OCP with pleuritic pain, dyspnoea and hypoxia.", "answer": "Suspected PE — Wells score, CTPA (or D-dimer if low probability), anticoagulate if high probability."},
      {"scenario": "Sharp pleuritic pain worse lying flat, relieved by leaning forward, with a rub.", "answer": "Pericarditis — NSAIDs + colchicine; look for a cause (viral, post-MI, autoimmune)."},
      {"scenario": "Chest pain that is worse on palpation and movement, in a well 25-year-old.", "answer": "Musculoskeletal — reassure and treat symptomatically after excluding serious causes."}
    ],
    "keyValues": [
      ["Troponin", "Rises 3-6 h after ACS; use serial samples/high-sensitivity assay"],
      ["ECG timing in suspected ACS", "Within 10 minutes of arrival"],
      ["STEMI reperfusion", "Primary PCI within 120 min of diagnosis"],
      ["D-dimer (PE)", "Negative rules out PE in low/intermediate probability"],
      ["Aspirin loading dose", "300 mg"]
    ],
    "redFlags": [
      "Haemodynamic instability + new murmur / unequal pulses — think dissection.",
      "ST elevation — STEMI pathway (primary PCI).",
      "Chest pain with hypoxia and tachycardia — consider PE."
    ],
    "management": [
      "Immediate: ABC, oxygen only if hypoxic, IV access, 12-lead ECG within 10 min, cardiac monitoring.",
      "ACS: aspirin, nitrates, analgesia; antiplatelet + anticoagulant per pathway; STEMI → primary PCI.",
      "Dissection: heart-rate/BP control (beta-blocker), urgent CT aortogram, cardiothoracic surgery.",
      "PE: risk-stratify (Wells), D-dimer/CTPA, LMWH if high probability.",
      "Pericarditis: NSAIDs + colchicine."
    ],
    "pitfalls": [
      "A normal troponin early does not exclude ACS — repeat it.",
      "Do not give nitrates in hypotension or suspected severe aortic stenosis.",
      "'Tearing' to the back + BP differential = dissection, not ACS — the treatments differ."
    ]
  },

  "arrhythmias": {
    "name": "Common arrhythmias",
    "group": "Cardiovascular",
    "overview": "The first branch point in any arrhythmia is haemodynamic stability: unstable = electricity (cardioversion/pacing), stable = drugs and rate/rhythm control. The exam tests AF, SVT, VT and bradyarrhythmias.",
    "essentials": [
      "Assess stability first: an unstable patient with any tachy- or bradyarrhythmia needs urgent treatment (synchronised DC cardioversion or pacing), not just drugs.",
      "Atrial fibrillation: irregularly irregular. Causes: ischaemia, sepsis, thyrotoxicosis, alcohol, valvular disease. Manage rate (beta-blocker/CCB) or rhythm, and assess stroke risk (CHA2DS2-VASc).",
      "SVT (AVNRT/AVRT): regular narrow-complex tachycardia — vagal manoeuvres, then adenosine, then CCB/beta-blocker.",
      "VT: broad-complex tachycardia — pulseless → arrest algorithm; stable → amiodarone/lidocaine and treat the cause (ischaemia, electrolytes).",
      "Bradyarrhythmias and heart block: if symptomatic/unstable → atropine then pacing; complete heart block needs pacing."
    ],
    "drugs": [
      {"name": "Adenosine", "when": "Stable regular narrow-complex SVT", "notes": "6 mg then 12 mg rapid IV bolus; warn about transient chest tightness/flushing; avoid in severe asthma"},
      {"name": "Bisoprolol / metoprolol (beta-blocker)", "when": "AF rate control, SVT, ACS", "notes": "Avoid in severe asthma, decompensated heart failure, high-grade block"},
      {"name": "Diltiazem / verapamil (CCB)", "when": "AF rate control, SVT (if no heart failure)", "notes": "Avoid in heart failure with reduced EF and in broad-complex tachycardia of uncertain origin"},
      {"name": "Amiodarone", "when": "Stable VT, AF rhythm control; during cardiac arrest (shockable)", "notes": "300 mg IV over 10-20 min in arrest; long-term: thyroid/lung/liver toxicity"},
      {"name": "Digoxin", "when": "Rate control in AF, especially with heart failure or sedentary patients", "notes": "Narrow therapeutic window; renal clearance"},
      {"name": "Atropine", "when": "Symptomatic bradycardia", "notes": "500 mcg IV, repeat to 3 mg; then pacing"},
      {"name": "Magnesium sulfate", "when": "Torsades de pointes", "notes": "IV; correct K+ and Mg2+"}
    ],
    "clinicalScenarios": [
      {"scenario": "Irregularly irregular pulse, rate 110, haemodynamically stable.", "answer": "AF — rate control (beta-blocker/CCB) + assess CHA2DS2-VASc for anticoagulation."},
      {"scenario": "Regular narrow-complex tachycardia at 180, hypotensive and dizzy.", "answer": "Unstable SVT — synchronised DC cardioversion (not adenosine)."},
      {"scenario": "Regular narrow-complex tachycardia at 180, stable.", "answer": "Vagal manoeuvres → adenosine 6 mg → 12 mg → CCB/beta-blocker."},
      {"scenario": "Broad-complex tachycardia, no pulse.", "answer": "Pulseless VT — defibrillate immediately, CPR, adrenaline per ALS."},
      {"scenario": "Complete heart block with syncope.", "answer": "Atropine then transcutaneous/transvenous pacing; involve cardiology."},
      {"scenario": "Polymorphic VT in a patient on QT-prolonging drugs.", "answer": "Torsades de pointes — IV magnesium, stop the culprit drug, correct K+/Mg2+."}
    ],
    "keyValues": [
      ["CHA2DS2-VASc", "≥2 (men) / ≥3 (women) → anticoagulate"],
      ["Adenosine dose", "6 mg then 12 mg rapid IV"],
      ["Amiodarone (arrest)", "300 mg IV bolus"],
      ["Atropine (bradycardia)", "500 mcg IV, up to 3 mg"],
      ["Torsades treatment", "IV magnesium sulfate"]
    ],
    "redFlags": [
      "Pulseless VT/VF — defibrillate immediately.",
      "Unstable tachyarrhythmia (shock, chest pain, syncope, heart failure) — synchronised cardioversion.",
      "Complete heart block with bradycardia — pacing."
    ],
    "management": [
      "Unstable: synchronised DC cardioversion (tachy) or atropine/pacing (brady).",
      "Stable AF: rate control (beta-blocker/CCB); anticoagulate per score; consider rhythm control if symptomatic/recent onset.",
      "Stable SVT: vagal manoeuvres → adenosine → CCB/beta-blocker.",
      "Stable VT: amiodarone/lidocaine, correct electrolytes, treat ischaemia.",
      "Torsades: IV magnesium, stop QT-prolonging drugs."
    ],
    "pitfalls": [
      "Don't cardiovert a stable patient or drug-treat an unstable one — stability decides the route.",
      "Verapamil/diltiazem are dangerous in broad-complex tachycardia you think might be VT.",
      "Always anticoagulate AF per stroke risk, not just control the rate."
    ]
  },

  "collapse-shock": {
    "name": "Collapse and shock",
    "group": "Cardiovascular",
    "overview": "Shock is inadequate tissue perfusion — not just a low BP. The exam expects you to classify the type (hypovolaemic, cardiogenic, obstructive, distributive) because the treatment differs completely.",
    "essentials": [
      "Shock = inadequate tissue perfusion. Types: hypovolaemic (haemorrhage, dehydration), cardiogenic (MI, arrhythmia, tamponade), obstructive (PE, tension pneumothorax), distributive (sepsis, anaphylaxis).",
      "Recognise early: tachycardia, cool peripheries, prolonged capillary refill, reduced urine output, altered consciousness, rising lactate — BP falls late.",
      "Hypovolaemic shock is the most common — treat with rapid fluid/blood and control the source of loss.",
      "Cardiogenic shock is pump failure — adding fluid can worsen it; needs inotropes and treatment of the cause.",
      "Septic shock is distributive — early antibiotics + fluids + lactate-guided resuscitation (Sepsis Six)."
    ],
    "drugs": [
      {"name": "IV crystalloid (balanced)", "when": "Hypovolaemic and septic shock", "notes": "250-500 mL boluses, reassess after each; avoid in cardiogenic shock"},
      {"name": "Blood products", "when": "Haemorrhagic shock", "notes": "Cross-matched or O-negative in extremis; activate major haemorrhage protocol"},
      {"name": "Noradrenaline (vasopressor)", "when": "Septic shock not responding to fluids; MAP target ≥65", "notes": "Central line preferred; first-line vasopressor"},
      {"name": "Adrenaline", "when": "Anaphylaxis (IM); cardiac arrest", "notes": "Anaphylaxis: 500 mcg IM anterolateral thigh"},
      {"name": "Dobutamine (inotrope)", "when": "Cardiogenic shock", "notes": "Increases contractility; monitor for arrhythmia"},
      {"name": "Broad-spectrum antibiotics", "when": "Septic shock", "notes": "Within 1 hour; per local policy"}
    ],
    "clinicalScenarios": [
      {"scenario": "Stab wound to the abdomen, hypotensive, tachycardic, cool peripheries.", "answer": "Haemorrhagic (hypovolaemic) shock — rapid fluids/blood + urgent surgery; don't delay for imaging."},
      {"scenario": "Post-MI patient with hypotension, crackles, raised JVP.", "answer": "Cardiogenic shock — cautious fluids, inotropes, treat ischaemia/arrhythmia; fluids alone worsen it."},
      {"scenario": "Sepsis with lactate 4.2 and hypotension.", "answer": "Septic shock — Sepsis Six within 1 hour; noradrenaline if MAP <65 despite fluids."},
      {"scenario": "Sudden collapse with absent breath sounds on one side and tracheal shift.", "answer": "Tension pneumothorax — immediate needle decompression, then chest drain."},
      {"scenario": "Collapse after a bee sting with wheeze and hypotension.", "answer": "Anaphylaxis — IM adrenaline 500 mcg, high-flow oxygen, IV fluids."}
    ],
    "keyValues": [
      ["Lactate", ">2 mmol/L suggests hypoperfusion"],
      ["MAP target (sepsis)", "≥65 mmHg"],
      ["Urine output target", "≥0.5 mL/kg/h"],
      ["Fluid bolus", "250-500 mL crystalloid, reassess"],
      ["Anaphylaxis adrenaline", "500 mcg IM anterolateral thigh"]
    ],
    "redFlags": [
      "Unresponsive or agonal breathing — cardiac arrest pathway.",
      "Tension pneumothorax (absent breath sounds, tracheal shift) — needle decompression.",
      "Cardiac tamponade (muffled heart sounds, raised JVP, hypotension) — pericardiocentesis."
    ],
    "management": [
      "ABC, high-flow oxygen, IV access, monitoring, treat the specific cause.",
      "Hypovolaemic: rapid crystalloid/blood, control haemorrhage.",
      "Septic: Sepsis Six — cultures, antibiotics, fluids, lactate; noradrenaline if refractory.",
      "Cardiogenic: treat arrhythmia/ischaemia, cautious fluids, inotropes, cardiology review."
    ],
    "pitfalls": [
      "BP is a late sign — a normal BP does not exclude shock; use lactate, urine output and perfusion.",
      "Giving large fluid boluses in cardiogenic shock can precipitate pulmonary oedema.",
      "Do not wait for imaging before treating tension pneumothorax or haemorrhage."
    ]
  },

  "syncope": {
    "name": "Syncope",
    "group": "Cardiovascular",
    "overview": "Syncope = transient loss of consciousness from cerebral hypoperfusion, with rapid spontaneous recovery. The exam's key skill is separating benign reflex syncope from dangerous cardiac syncope.",
    "essentials": [
      "Syncope is transient LOC due to cerebral hypoperfusion with rapid recovery. Distinguish from seizure (post-ictal confusion, tongue biting, tonic-clonic movements) and drop attacks (no LOC).",
      "Reflex (vasovagal) syncope is most common — triggered by pain, emotion, standing or micturition, with a prodrome of light-headedness, sweating, nausea.",
      "Orthostatic hypotension: on standing, especially in the elderly, dehydrated, or on antihypertensives.",
      "Cardiac syncope (arrhythmia, aortic stenosis, HCM, PE) is the dangerous type — may occur on exertion with no prodrome.",
      "Investigations: ECG, lying/standing BP, echo, Holter, tilt test. Admit if a cardiac cause is suspected."
    ],
    "drugs": [
      {"name": "Midodrine / fludrocortisone", "when": "Refractory reflex or orthostatic syncope (specialist)", "notes": "Vasoconstrictor/volume expander; specialist initiation"},
      {"name": "IV fluids", "when": "Volume depletion causing orthostatic syncope", "notes": "Crystalloid; treat the underlying cause"},
      {"name": "Rate/rhythm drugs", "when": "Arrhythmic syncope", "notes": "Per cardiology; pacemaker for bradyarrhythmic syncope"}
    ],
    "clinicalScenarios": [
      {"scenario": "Young woman faints after a blood test, with light-headedness and sweating, quick recovery.", "answer": "Vasovagal (reflex) syncope — reassure, fluids, avoid triggers, counter-pressure manoeuvres."},
      {"scenario": "55-year-old collapses on exertion with no prodrome; father died suddenly at 50.", "answer": "Suspected cardiac syncope — ECG + cardiology assessment (arrhythmia, HCM, aortic stenosis)."},
      {"scenario": "Elderly patient faints on standing shortly after starting an antihypertensive.", "answer": "Orthostatic hypotension — review drugs, lying/standing BP, hydration."},
      {"scenario": "Witnessed collapse with tongue biting and post-ictal confusion.", "answer": "This is a seizure, not syncope — investigate for epilepsy/cause (EEG, imaging, glucose)."}
    ],
    "keyValues": [
      ["Orthostatic hypotension", "SBP drop ≥20 mmHg on standing"],
      ["ECG red flags", "Heart block, long QT, Brugada pattern, ischaemia"],
      ["High-risk features", "Exertional, no prodrome, family history of sudden death, abnormal ECG"],
      ["DVLA advice", "Group 1: stop driving after unexplained syncope until assessed"]
    ],
    "redFlags": [
      "Syncope during exertion — think cardiac.",
      "Abnormal ECG, structural heart disease, or family history of sudden cardiac death.",
      "Recurrent unexplained syncope — needs cardiology assessment."
    ],
    "management": [
      "ABC, check glucose, ECG, lying/standing BP.",
      "Reassure and advise for reflex syncope (fluids, avoid triggers, counter-pressure manoeuvres).",
      "Cardiac syncope: treat the arrhythmia/structural cause; admit for monitoring.",
      "Advise driving restrictions per DVLA after syncope."
    ],
    "pitfalls": [
      "Exertional syncope with no prodrome = cardiac until proven otherwise.",
      "A 'funny turn' with a long post-ictal phase is more likely a seizure.",
      "Always check lying/standing BP — orthostatic hypotension is easy to miss."
    ]
  },

  "acute-limb-ischaemia": {
    "name": "Acute limb ischaemia",
    "group": "Cardiovascular",
    "overview": "A time-critical vascular emergency — irreversible damage begins within hours. The exam tests recognising the '6 Ps' and knowing not to delay the vascular team for imaging.",
    "essentials": [
      "Acute limb ischaemia = sudden loss of limb perfusion, usually embolism (AF, recent MI) or in-situ thrombosis (atherosclerosis). The '6 Ps': pain, pallor, pulselessness, paraesthesia, paralysis, perishing cold.",
      "Time-critical: irreversible muscle/nerve damage within 4-6 hours. Paralysis and paraesthesia indicate advanced ischaemia.",
      "Embolic (sudden, no prior claudication, normal contralateral pulses) vs thrombotic (background of chronic peripheral arterial disease).",
      "Examine and document: pulses (femoral, popliteal, DP, PT), capillary refill, sensation, motor function, level of the block.",
      "Immediate: heparin, analgesia, keep the limb warm, urgent vascular referral — do not delay for imaging if the limb is threatened."
    ],
    "drugs": [
      {"name": "IV unfractionated heparin", "when": "Immediate, once acute limb ischaemia is suspected", "notes": "Prevents clot propagation; give before imaging/surgery"},
      {"name": "Analgesia (opioid)", "when": "Severe ischaemic pain", "notes": "IV titrated morphine"},
      {"name": "Thrombolysis (intra-arterial alteplase)", "when": "Selected cases (specialist decision)", "notes": "Catheter-directed; watch for bleeding/reperfusion injury"}
    ],
    "clinicalScenarios": [
      {"scenario": "78-year-old with AF: sudden painful, pale, cold right leg with absent pulses and no prior claudication.", "answer": "Acute embolic limb ischaemia — IV heparin, analgesia, urgent vascular surgery."},
      {"scenario": "Acutely ischaemic leg with new paralysis and paraesthesia.", "answer": "Advanced ischaemia with imminent irreversible damage — immediate vascular review; do not delay for imaging."},
      {"scenario": "A patient known to have claudication develops sudden worsening rest pain and mottling.", "answer": "Acute-on-chronic (thrombotic) ischaemia — anticoagulate and refer urgently."}
    ],
    "keyValues": [
      ["Ischaemia time", "Irreversible damage after 4-6 hours"],
      ["6 Ps", "Pain, pallor, pulselessness, paraesthesia, paralysis, perishing cold"],
      ["Immediate treatment", "IV heparin, analgesia, urgent vascular review"],
      ["Post-reperfusion", "Watch for compartment syndrome and rhabdomyolysis"]
    ],
    "redFlags": [
      "Paralysis or paraesthesia — advanced ischaemia, imminent irreversible damage.",
      "Cold, mottled, pulseless limb — surgical emergency.",
      "Rhabdomyolysis after reperfusion — check K+ and CK, watch renal function."
    ],
    "management": [
      "ABC, IV heparin, analgesia, keep the limb warm, NBM, urgent vascular referral.",
      "Do not delay for imaging if the limb is threatened.",
      "Post-reperfusion: monitor for compartment syndrome and rhabdomyolysis."
    ],
    "pitfalls": [
      "Do not elevate the limb or apply heat — keep it warm and dependent but not raised.",
      "A 'pulseless leg' is not the same as chronic claudication — the sudden onset is the clue.",
      "Never wait for an angiogram in a threatened limb — the vascular team decides."
    ]
  },

  "chronic-limb-ischaemia": {
    "name": "Chronic limb ischaemia – ulcers and gangrene",
    "group": "Cardiovascular",
    "overview": "Chronic limb-threatening ischaemia and the diabetic foot are common ward problems. The exam tests recognising the type of ulcer and knowing when to escalate (infection, gangrene).",
    "essentials": [
      "Chronic limb-threatening ischaemia (CLTI): rest pain, non-healing ulcers, or gangrene due to peripheral arterial disease. Rest pain is worse at night, relieved by hanging the leg down.",
      "Risk factors: smoking, diabetes, hypertension, hyperlipidaemia, age. Diabetic foot disease involves both neuropathic and ischaemic components.",
      "Ulcer types: arterial (punched-out, painful, pale base, on toes/heel), venous (gaiter area, shallow, wet, painless), neuropathic (plantar, painless, at pressure points).",
      "Assess: ABPI, pulses, monofilament sensation, ulcer characteristics, signs of infection.",
      "Management: best medical therapy, revascularisation for CLTI, wound care, and amputation if unsalvageable."
    ],
    "drugs": [
      {"name": "Antiplatelet (clopidogrel/aspirin)", "when": "All peripheral arterial disease", "notes": "Secondary prevention; part of best medical therapy"},
      {"name": "Statin (atorvastatin)", "when": "All PAD", "notes": "High-intensity dose regardless of cholesterol level"},
      {"name": "Antibiotics", "when": "Infected ulcer / diabetic foot infection", "notes": "Per local policy; wound swab; IV if systemically unwell"},
      {"name": "Analgesia", "when": "Rest pain", "notes": "Regular paracetamol/opioid; improve perfusion to relieve it"},
      {"name": "Prostanoids / specialist agents", "when": "Critical ischaemia (specialist)", "notes": "Iloprost in selected patients"}
    ],
    "clinicalScenarios": [
      {"scenario": "Diabetic with a painless punched-out plantar ulcer and loss of monofilament sensation.", "answer": "Neuropathic (diabetic) ulcer — offloading, podiatry, glycaemic control."},
      {"scenario": "Rest pain and ABPI 0.4 with a non-healing heel ulcer.", "answer": "Chronic limb-threatening ischaemia — best medical therapy + vascular referral for revascularisation."},
      {"scenario": "Diabetic foot ulcer with crepitus, spreading infection and fever.", "answer": "Necrotising infection — IV antibiotics + urgent surgical debridement."},
      {"scenario": "Deep ulcer with positive probe-to-bone.", "answer": "Suspect osteomyelitis — MRI, prolonged antibiotics, consider amputation."},
      {"scenario": "Painless shallow ulcer in the gaiter area with surrounding pigmentation and oedema.", "answer": "Venous ulcer — compression therapy, wound care, elevate the leg."}
    ],
    "keyValues": [
      ["ABPI", ">0.9 normal; <0.5 severe ischaemia; >1.3 suggests calcified vessels (diabetes)"],
      ["Rest pain", "Worse at night, relieved by dependency"],
      ["Arterial ulcer", "Punched-out, painful, on toes/heel"],
      ["Neuropathic ulcer", "Painless, plantar, at pressure points"]
    ],
    "redFlags": [
      "Gangrene or necrotic tissue — urgent vascular review, possible amputation.",
      "Infected diabetic foot with systemic sepsis — emergency, IV antibiotics + debridement.",
      "Rapid deterioration or acute-on-chronic ischaemia."
    ],
    "management": [
      "Best medical therapy: antiplatelet, statin, smoking cessation, tight diabetes/BP control.",
      "CLTI: refer to vascular surgery for revascularisation.",
      "Infected ulcer: swab, antibiotics, debridement, offloading (diabetic).",
      "Wound care: keep clean, moist, offload pressure; tissue viability/podiatry."
    ],
    "pitfalls": [
      "A painless ulcer is not always benign — in diabetes it is neuropathic and risk of infection is high.",
      "An ABPI >1.3 in diabetes is falsely reassuring — vessels are calcified; use toe pressures.",
      "Do not use compression on an ischaemic (arterial) ulcer."
    ]
  },

  "dvt-pe": {
    "name": "Deep Venous thrombosis and Pulmonary embolism",
    "group": "Cardiovascular",
    "overview": "VTE is a spectrum (DVT → PE) and a top cause of preventable hospital death. The exam tests risk stratification (Wells), the D-dimer vs imaging decision, and treating massive PE.",
    "essentials": [
      "VTE = DVT + PE, one disease. Risk factors: immobility, surgery, malignancy, pregnancy/OCP, thrombophilia, previous VTE, obesity.",
      "DVT: unilateral leg swelling, pain, erythema, warmth, dilated superficial veins. Wells score; D-dimer rules out in low probability; USS confirms.",
      "PE: dyspnoea, pleuritic pain, hypoxia, tachycardia, haemoptysis, collapse. Massive PE → obstructive shock.",
      "Anticoagulation is the mainstay (LMWH → DOAC or warfarin); massive PE with shock → thrombolysis.",
      "Prevention: VTE prophylaxis (LMWH, TEDs, early mobilisation) for all at-risk inpatients."
    ],
    "drugs": [
      {"name": "LMWH (enoxaparin)", "when": "Initial treatment of confirmed/high-probability VTE; VTE prophylaxis; pregnancy; cancer-associated VTE", "notes": "Weight-based; reduce in renal impairment"},
      {"name": "DOAC (apixaban/rivaroxaban)", "when": "Long-term VTE treatment (non-cancer)", "notes": "No monitoring; avoid in APS/mechanical valves"},
      {"name": "Warfarin", "when": "Long-term VTE (with initial LMWH bridging), APS", "notes": "Target INR 2-3; needs monitoring"},
      {"name": "Alteplase (thrombolysis)", "when": "Massive PE with haemodynamic instability", "notes": "IV bolus/infusion; contraindicated in recent surgery/bleeding"},
      {"name": "VTE prophylaxis", "when": "All at-risk inpatients", "notes": "LMWH + mechanical (TEDs/compression); early mobilisation"}
    ],
    "clinicalScenarios": [
      {"scenario": "30-year-old on the OCP with sudden dyspnoea, pleuritic pain and hypoxia; Wells 5.", "answer": "Suspected PE with high Wells — CTPA (not D-dimer); anticoagulate if high probability while awaiting."},
      {"scenario": "Confirmed massive PE with hypotension and shock.", "answer": "Thrombolysis (alteplase); consider surgical/mechanical embolectomy."},
      {"scenario": "Unilateral leg swelling after a long-haul flight; Wells 3.", "answer": "Likely DVT — USS; anticoagulate if high probability while awaiting."},
      {"scenario": "Post-operative patient with a low Wells score for PE.", "answer": "D-dimer — a negative result rules out PE in low/intermediate probability."},
      {"scenario": "Cancer patient with a recurrent VTE.", "answer": "LMWH is preferred over DOACs in cancer-associated thrombosis (per guidance)."}
    ],
    "keyValues": [
      ["Wells DVT", "≥2 = likely → USS"],
      ["Wells PE", ">4 = likely → CTPA"],
      ["D-dimer", "Negative rules out VTE in low/intermediate probability"],
      ["Massive PE", "Shock/hypotension → thrombolysis"],
      ["Treatment duration", "3 months (provoked); longer/indefinite if unprovoked or cancer"]
    ],
    "redFlags": [
      "PE with hypotension/shock — massive PE, thrombolyse.",
      "Phlegmasia cerulea dolens (tense, blue, painful leg) — venous gangrene risk.",
      "Sudden collapse with risk factors — consider PE."
    ],
    "management": [
      "Suspected DVT: Wells score, D-dimer, USS; anticoagulate if high probability.",
      "Suspected PE: Wells, D-dimer/CTPA, LMWH if high probability.",
      "Confirmed VTE: therapeutic anticoagulation (LMWH → DOAC or warfarin), duration by cause.",
      "Massive PE: thrombolysis; consider embolectomy.",
      "Prevention: LMWH + TEDs + early mobilisation for at-risk inpatients."
    ],
    "pitfalls": [
      "Do not order D-dimer when Wells is high — go straight to imaging.",
      "Massive PE with shock needs thrombolysis, not just heparin.",
      "In pregnancy, imaging (CTPA or V/Q) — do not avoid it out of radiation concern."
    ]
  },
}
