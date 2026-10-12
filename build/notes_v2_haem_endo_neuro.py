# Enhanced notes v2 — haematology/oncology, endocrine, neuro/elderly, obs/gynae, dermatology (batch 3).
PART = {
  "neutropenic-sepsis": {
    "name": "Neutropenic sepsis",
    "group": "Haematology & acute oncology",
    "overview": "A haematological emergency where the usual signs of infection may be absent. The exam tests the rule: any fever in a neutropenic patient is sepsis until proven otherwise, and antibiotics must not wait.",
    "essentials": [
      "Neutropenic sepsis = temperature ≥38°C (or sepsis signs) with neutrophils <0.5 × 10^9/L, in a patient on chemotherapy or with haematological malignancy. A medical emergency.",
      "Neutropenic patients mount no inflammatory response — they may look deceptively well with minimal signs.",
      "Immediate management (within 1 hour): blood cultures, FBC, U&E, LFT, CRP, lactate, then IV broad-spectrum antibiotics — do not wait for results.",
      "Look for a source: line infection, chest, urine, skin, perianal. Consider antifungal if fever persists despite antibiotics.",
      "Monitor temperature, observations, cultures and response; escalate if deteriorating."
    ],
    "drugs": [
      {"name": "IV broad-spectrum antibiotics", "when": "Neutropenic sepsis — immediately", "notes": "Piperacillin-tazobactam (or per local policy); within 1 hour"},
      {"name": "Antifungal (e.g. amphotericin/caspofungin)", "when": "Persistent fever after 48-72 h of antibiotics", "notes": "Covers fungal infection; specialist input"},
      {"name": "G-CSF (granulocyte colony-stimulating factor)", "when": "Selected cases (prophylaxis or treatment, specialist)", "notes": "Stimulates neutrophil recovery"},
      {"name": "IV fluids", "when": "Hypotension/sepsis", "notes": "Part of Sepsis Six resuscitation"}
    ],
    "clinicalScenarios": [
      {"scenario": "Chemotherapy patient, temperature 38.5°C, neutrophils 0.3.", "answer": "Neutropenic sepsis — blood cultures then IV broad-spectrum antibiotics within 1 hour."},
      {"scenario": "Neutropenic patient with a central line and fever.", "answer": "Consider line sepsis — cultures (peripheral + line), antibiotics, consider line removal."},
      {"scenario": "Fever persists after 72 h of appropriate antibiotics.", "answer": "Consider fungal infection — add antifungal; re-image and re-culture."},
      {"scenario": "Neutropenic patient with hypotension and lactate 3.", "answer": "Septic shock — Sepsis Six, aggressive fluids, early senior/ICU involvement."}
    ],
    "keyValues": [
      ["Neutropenia", "Neutrophils <0.5 × 10^9/L"],
      ["Fever threshold", "≥38°C (or any sepsis sign)"],
      ["Antibiotics within", "1 hour of presentation"],
      ["First-line", "IV broad-spectrum (e.g. piperacillin-tazobactam)"]
    ],
    "redFlags": [
      "Any fever in a neutropenic patient — treat as sepsis immediately.",
      "Hypotension/shock — aggressive resuscitation + antibiotics.",
      "Persistent fever despite 48-72 h of antibiotics — consider fungal infection."
    ],
    "management": [
      "Sepsis Six + blood cultures, FBC, lactate, then IV antibiotics within 1 hour.",
      "Look for and treat the source (line, chest, urine, skin).",
      "Monitor response; add antifungal if fever persists.",
      "Involve the haematology/oncology team early."
    ],
    "pitfalls": [
      "A well-looking neutropenic patient can be profoundly septic — do not be reassured.",
      "Never delay antibiotics to wait for cultures or imaging.",
      "Remember line sepsis as a source — examine the central line site."
    ]
  },

  "congenital-bleeding": {
    "name": "Congenital bleeding disorders",
    "group": "Haematology & acute oncology",
    "overview": "Haemophilia and von Willebrand disease present with bleeding into joints/muscles or mucocutaneous bleeding. The exam tests recognising the pattern and replacing the missing factor.",
    "essentials": [
      "Haemophilia A (factor VIII deficiency) and B (factor IX deficiency): X-linked, bleeding into joints (haemarthrosis) and muscles; severity by factor level.",
      "von Willebrand disease: the most common inherited bleeding disorder — mucocutaneous bleeding (epistaxis, menorrhagia, easy bruising), prolonged bleeding time, low vWF.",
      "Acute bleeding in haemophilia: replace the missing factor urgently. Avoid IM injections, aspirin and NSAIDs.",
      "Haemarthrosis: factor replacement + analgesia + rest; avoid joint aspiration unless tense.",
      "Carriers/affected patients need specialist haematology input for surgery, dental work and major bleeding."
    ],
    "drugs": [
      {"name": "Factor VIII concentrate", "when": "Haemophilia A bleeding", "notes": "Urgent replacement; dose by severity/weight"},
      {"name": "Factor IX concentrate", "when": "Haemophilia B bleeding", "notes": "Urgent replacement"},
      {"name": "Desmopressin (DDAVP)", "when": "Mild haemophilia A / mild von Willebrand disease", "notes": "Releases stored factor VIII/vWF; not for severe disease"},
      {"name": "Tranexamic acid", "when": "Mucosal bleeding (e.g. epistaxis, dental, menorrhagia)", "notes": "Antifibrinolytic; adjunct"},
      {"name": "Tranexamic acid / von Willebrand factor concentrate", "when": "vWD bleeding (major)", "notes": "vWF-containing factor concentrate for severe bleeding"}
    ],
    "clinicalScenarios": [
      {"scenario": "Known haemophilia A with a swollen, painful knee after minor trauma.", "answer": "Haemarthrosis — factor VIII replacement + analgesia + rest (avoid aspirin/NSAIDs)."},
      {"scenario": "Haemophiliac with a head injury after a fall.", "answer": "Urgent factor replacement and imaging — intracranial bleed is life-threatening."},
      {"scenario": "Young woman with heavy periods, easy bruising and epistaxis; prolonged bleeding time.", "answer": "von Willebrand disease — check vWF antigen/activity; desmopressin or vWF concentrate for bleeding."},
      {"scenario": "Patient with vWD needing a dental extraction.", "answer": "Plan with haematology — tranexamic acid ± desmopressin/factor cover."}
    ],
    "keyValues": [
      ["Haemophilia A", "Factor VIII deficiency (X-linked)"],
      ["Haemophilia B", "Factor IX deficiency (X-linked)"],
      ["vWD", "vWF deficiency; mucocutaneous bleeding"],
      ["Haemarthrosis treatment", "Factor replacement + analgesia + rest"]
    ],
    "redFlags": [
      "Major bleeding or head injury in a haemophiliac — urgent factor replacement.",
      "Intracranial bleed — factor replacement + urgent imaging.",
      "Bleeding not controlled by factor — consider inhibitors."
    ],
    "management": [
      "Acute bleed: replace the deficient factor urgently.",
      "Haemarthrosis: factor + analgesia + rest; avoid aspiration.",
      "Avoid aspirin/NSAIDs/IM injections.",
      "Involve haematology for all significant bleeds and procedures."
    ],
    "pitfalls": [
      "Do not give IM injections or NSAIDs in haemophilia.",
      "Desmopressin works only in mild haemophilia A and mild vWD — not severe disease.",
      "Always consider an intracranial bleed after head injury in a bleeding disorder."
    ]
  },

  "spinal-cord-compression": {
    "name": "Spinal cord compression",
    "group": "Haematology & acute oncology",
    "overview": "An oncological emergency where outcome depends on how early you act. The exam tests recognising the red flags and starting dexamethasone before imaging.",
    "essentials": [
      "Malignant spinal cord compression (MSCC): cord/cauda equina compression by tumour (metastatic — prostate, breast, lung, myeloma).",
      "Red flags: new back pain (especially thoracic), progressive neurological deficit, sensory level, bladder/bowel dysfunction, gait disturbance. Back pain + neurological symptoms in a cancer patient = MSCC until proven otherwise.",
      "Immediate: high-dose dexamethasone (reduces oedema), urgent MRI whole spine (within 24 h), oncology/neurosurgery referral.",
      "Do not delay treatment for the diagnosis — treat empirically if suspicion is high.",
      "Outcome depends on pre-treatment neurological status — early recognition is critical."
    ],
    "drugs": [
      {"name": "Dexamethasone", "when": "Suspected MSCC — start immediately", "notes": "High-dose (e.g. 16 mg/day) with gastric protection; reduces cord oedema"},
      {"name": "Analgesia", "when": "Pain control", "notes": "Regular paracetamol/opioid; avoid NSAIDs if thrombocytopenia"},
      {"name": "LMWH", "when": "VTE prophylaxis (unless bleeding risk)", "notes": "Immobility risk"},
      {"name": "Bisphosphonate / denosumab", "when": "Bone metastases (specialist)", "notes": "Reduces skeletal events"}
    ],
    "clinicalScenarios": [
      {"scenario": "Patient with metastatic prostate cancer develops new thoracic back pain and leg weakness.", "answer": "MSCC — high-dose dexamethasone + urgent MRI whole spine (within 24 h), oncology/neurosurgery referral."},
      {"scenario": "Cancer patient with saddle anaesthesia and urinary retention.", "answer": "Cauda equina syndrome — emergency MRI and urgent surgical referral."},
      {"scenario": "Known lung cancer with a sensory level and gait disturbance.", "answer": "MSCC — dexamethasone, urgent MRI, radiotherapy/surgery per team."}
    ],
    "keyValues": [
      ["Dexamethasone", "High-dose (e.g. 16 mg/day) urgently"],
      ["MRI whole spine", "Within 24 h of suspicion"],
      ["Common primaries", "Prostate, breast, lung, myeloma"],
      ["Red flags", "Back pain + neuro deficit, sensory level, sphincter dysfunction"]
    ],
    "redFlags": [
      "Back pain + any neurological symptom in a cancer patient — MSCC until proven otherwise.",
      "Sensory level, leg weakness, or bladder/bowel dysfunction — emergency.",
      "Cauda equina (saddle anaesthesia, urinary retention) — surgical emergency."
    ],
    "management": [
      "High-dose dexamethasone immediately.",
      "Urgent MRI whole spine (within 24 h).",
      "Oncology/neurosurgery referral; treat the primary malignancy.",
      "Analgesia, log-roll care, monitor neurology."
    ],
    "pitfalls": [
      "Do not wait for imaging to start dexamethasone if suspicion is high.",
      "A normal plain X-ray does not exclude MSCC — it needs MRI.",
      "Bladder/bowel dysfunction is a late sign — act on back pain + neurology earlier."
    ]
  },

  "diabetes-control": {
    "name": "Diabetes control",
    "group": "Endocrine & metabolic",
    "overview": "Diabetic emergencies (DKA, HHS) and inpatient glycaemic control are heavily examined. The exam tests safe management — especially potassium handling in DKA.",
    "essentials": [
      "Type 1 (insulin deficiency, autoimmune) vs type 2 (insulin resistance + relative deficiency). Acute complications: DKA, HHS, hypoglycaemia.",
      "DKA (type 1): hyperglycaemia + ketonaemia + acidosis. Precipitants: infection, missed insulin, MI, stress. Treat: IV fluids, fixed-rate insulin infusion, potassium replacement, treat precipitant.",
      "HHS (type 2): severe hyperglycaemia without significant ketosis/acidosis, marked dehydration. Treat: large-volume fluids, cautious insulin, correct electrolytes.",
      "Inpatient glycaemic control: monitor glucose, basal-bolus insulin, avoid prolonged hypo/hyperglycaemia; involve the diabetes team.",
      "Sick-day rules: never stop insulin in type 1, increase monitoring, seek help if vomiting/unwell."
    ],
    "drugs": [
      {"name": "Fixed-rate IV insulin", "when": "DKA / HHS", "notes": "0.1 unit/kg/h (DKA); monitor glucose and K+ hourly"},
      {"name": "IV fluids (0.9% saline)", "when": "DKA/HHS resuscitation", "notes": "Rapid initial resuscitation, then guided by status"},
      {"name": "Potassium replacement", "when": "DKA — replace if K+ <5.5", "notes": "Insulin drives K+ down; replace before/with insulin if low"},
      {"name": "Basal-bolus insulin", "when": "Inpatient glycaemic control", "notes": "Long-acting basal + short-acting mealtime doses"},
      {"name": "Metformin", "when": "Type 2 diabetes (not in DKA/renal failure)", "notes": "Hold in acute illness/contrast (lactic acidosis risk)"}
    ],
    "clinicalScenarios": [
      {"scenario": "Type 1 diabetes with DKA and K+ 3.2.", "answer": "Replace potassium before/with insulin — insulin shifts K+ intracellularly and can cause dangerous hypokalaemia."},
      {"scenario": "Type 2 diabetes, glucose 38 mmol/L, marked dehydration, no significant ketosis.", "answer": "HHS — aggressive fluids, cautious insulin, correct electrolytes."},
      {"scenario": "Type 1 diabetic vomiting with high glucose and ketones.", "answer": "Sick-day rules — never stop insulin, monitor glucose/ketones, seek help; treat as DKA if severe."},
      {"scenario": "Inpatient with erratic glucose on the ward.", "answer": "Basal-bolus insulin regimen + monitor + diabetes team input."}
    ],
    "keyValues": [
      ["DKA", "Glucose + ketones + acidosis (pH <7.3, HCO3 <18)"],
      ["HHS", "Glucose often >30 mmol/L, no significant ketosis"],
      ["DKA treatment", "IV fluids, fixed-rate insulin, K+ replacement"],
      ["Inpatient glucose target", "6-10 mmol/L"]
    ],
    "redFlags": [
      "DKA with K+ <3.5 — replace K+ before insulin.",
      "HHS with severe dehydration — large-volume fluid resuscitation.",
      "Recurrent hypoglycaemia — review the insulin regimen."
    ],
    "management": [
      "DKA: fluids, fixed-rate insulin, K+ replacement, treat precipitant, monitor glucose/ketones/K+.",
      "HHS: aggressive fluids, cautious insulin, correct electrolytes.",
      "Inpatient: basal-bolus insulin, monitor glucose, diabetes team input.",
      "Educate on sick-day rules and never stopping insulin in type 1."
    ],
    "pitfalls": [
      "Insulin without potassium replacement in DKA can cause fatal hypokalaemia.",
      "HHS needs much larger fluid volumes than DKA.",
      "Do not stop a type 1 diabetic's insulin because they are 'not eating'."
    ]
  },

  "hypoglycaemia": {
    "name": "Hypoglycaemia",
    "group": "Endocrine & metabolic",
    "overview": "A common inpatient emergency where the treatment depends on whether the patient can swallow. The exam tests the conscious vs unconscious pathway.",
    "essentials": [
      "Hypoglycaemia = glucose <4.0 mmol/L (in diabetics) with symptoms. Causes: excess insulin/oral hypoglycaemics, missed meals, exercise, alcohol, sepsis, renal/hepatic failure.",
      "Symptoms: autonomic (sweating, tremor, palpitations, hunger) and neuroglycopenic (confusion, drowsiness, seizures, coma).",
      "Treatment: if conscious and able to swallow → oral fast-acting carbohydrate, then long-acting starchy food. If unconscious/unable → IV glucose (10%) or IM glucagon.",
      "Recheck glucose 10-15 min after treatment; repeat if still low; identify and treat the cause.",
      "Inpatients: review the insulin regimen, monitor glucose, involve the diabetes team."
    ],
    "drugs": [
      {"name": "Oral glucose (glucose tablets/sugary drink)", "when": "Conscious, able to swallow", "notes": "Follow with long-acting carbohydrate"},
      {"name": "IV glucose 10%", "when": "Unconscious / unable to swallow / severe", "notes": "100-200 mL bolus, then monitor; protect the airway"},
      {"name": "IM glucagon", "when": "No IV access / unconscious (first aid)", "notes": "1 mg IM; works only with stored glycogen (less effective in alcohol/fasting)"},
      {"name": "Long-acting carbohydrate", "when": "After acute correction", "notes": "Prevents recurrence (e.g. toast, biscuit)"}
    ],
    "clinicalScenarios": [
      {"scenario": "Diabetic found unconscious with glucose 1.8 mmol/L.", "answer": "IV 10% glucose (or IM glucagon) with airway protection; recheck 10-15 min later."},
      {"scenario": "Diabetic patient conscious with a glucose of 3.2 after a missed meal.", "answer": "Oral fast-acting carbohydrate then long-acting starchy food; review the regimen."},
      {"scenario": "Non-diabetic patient with recurrent hypoglycaemia.", "answer": "Investigate — insulinoma, adrenal insufficiency, sepsis, alcohol; check insulin/C-peptide levels."},
      {"scenario": "Recurrent hypoglycaemia in a hospital patient on insulin.", "answer": "Review the insulin dose and regimen; consider causes and involve the diabetes team."}
    ],
    "keyValues": [
      ["Hypoglycaemia", "Glucose <4.0 mmol/L"],
      ["Conscious treatment", "Oral fast-acting carbohydrate"],
      ["Unconscious treatment", "IV 10% glucose or IM glucagon"],
      ["Recheck", "Glucose 10-15 min after treatment"]
    ],
    "redFlags": [
      "Unconscious/seizing — IV glucose/glucagon, protect the airway.",
      "Recurrent hypoglycaemia — review medication and look for the cause.",
      "Hypoglycaemia in a non-diabetic — investigate (insulinoma, adrenal, sepsis)."
    ],
    "management": [
      "Conscious: oral glucose, then long-acting carbohydrate.",
      "Unconscious: IV 10% glucose or IM glucagon, recheck.",
      "Identify and treat the cause (insulin dose, missed meal, sepsis).",
      "Review and adjust the diabetes regimen; involve the diabetes team."
    ],
    "pitfalls": [
      "Oral treatment for an unconscious patient risks aspiration — use IV glucose/glucagon.",
      "Glucagon is less effective in alcohol-related or prolonged fasting hypoglycaemia (low glycogen).",
      "Always recheck glucose — a single treatment may not be enough."
    ]
  },

  "diabetic-foot": {
    "name": "Diabetic foot complications + sepsis",
    "group": "Endocrine & metabolic",
    "overview": "A common and dangerous problem where neuropathy, ischaemia and infection combine. The exam tests recognising the infected foot and escalating to surgery.",
    "essentials": [
      "Diabetic foot disease = neuropathy (loss of protective sensation) + ischaemia (PAD) + infection. Ulcers are often painless and on pressure points.",
      "Assess: neurovascular status (monofilament, pulses, ABPI), ulcer depth, signs of infection (erythema, discharge, odour, crepitus), systemic sepsis.",
      "Infected diabetic foot is a surgical emergency — deep infection, osteomyelitis and gangrene progress rapidly. IV antibiotics + urgent surgical debridement.",
      "Classify severity (Wagner / IDSA / IWGDF) to guide management; osteomyelitis via probe-to-bone, MRI, prolonged antibiotics.",
      "Prevention: foot examination at every diabetes review, podiatry, offloading, glycaemic control, smoking cessation."
    ],
    "drugs": [
      {"name": "IV antibiotics", "when": "Infected diabetic foot / systemic sepsis", "notes": "Broad-spectrum per local policy; guided by wound swabs"},
      {"name": "Analgesia", "when": "Painful ulcer/ischaemia", "notes": "Regular; neuropathy may mask pain"},
      {"name": "Antiplatelet + statin", "when": "Associated peripheral arterial disease", "notes": "Secondary prevention"},
      {"name": "Insulin optimisation", "when": "Poor glycaemic control", "notes": "Aids wound healing"}
    ],
    "clinicalScenarios": [
      {"scenario": "Diabetic foot ulcer with crepitus, spreading infection and fever.", "answer": "Necrotising infection — IV antibiotics + urgent surgical debridement."},
      {"scenario": "Deep ulcer with positive probe-to-bone.", "answer": "Suspect osteomyelitis — MRI, prolonged antibiotics, consider amputation."},
      {"scenario": "Painless plantar ulcer with loss of monofilament sensation.", "answer": "Neuropathic ulcer — offloading, podiatry, glycaemic control, foot care."},
      {"scenario": "Diabetic with rest pain and an ABPI of 0.4.", "answer": "Ischaemic component — vascular review for revascularisation; best medical therapy."}
    ],
    "keyValues": [
      ["Monofilament", "Loss = neuropathy (at risk)"],
      ["Probe-to-bone", "Suggests osteomyelitis"],
      ["Infected foot", "IV antibiotics + urgent debridement"],
      ["ABPI", "Assess ischaemia (calcified vessels may over-read in diabetes)"]
    ],
    "redFlags": [
      "Systemic sepsis from a diabetic foot — emergency, IV antibiotics + surgery.",
      "Crepitus, gas on X-ray — necrotising infection, urgent debridement.",
      "Deep ulcer with exposed bone — osteomyelitis."
    ],
    "management": [
      "Assess neurovascular status and ulcer characteristics.",
      "Infected: wound swab, IV antibiotics, urgent surgical debridement.",
      "Osteomyelitis: MRI, prolonged antibiotics, consider amputation.",
      "Prevention: podiatry, offloading, glycaemic control, smoking cessation."
    ],
    "pitfalls": [
      "A painless foot ulcer is not benign — neuropathy hides severe infection.",
      "An ABPI >1.3 in diabetes is falsely reassuring (calcified vessels).",
      "Never delay surgery in a foot with spreading infection or gas."
    ]
  },

  "acute-confusional-states": {
    "name": "Acute confusional states",
    "group": "Neurology & elderly",
    "overview": "Delirium is common, serious and usually reversible. The exam tests recognising it, hunting for the cause (PINCH ME), and avoiding sedation.",
    "essentials": [
      "Delirium = acute, fluctuating disturbance of consciousness/attention, common in the elderly and acutely ill. Distinguish from dementia (chronic, progressive) and psychiatric illness.",
      "Causes (PINCH ME / DIMS): infection, drugs, metabolic (electrolytes, glucose, hypoxia), constipation, urinary retention, pain, dehydration, sensory impairment, sleep deprivation.",
      "Assess: history (onset, fluctuation), cognitive testing (AMT4/6-CIT), observations, bloods (FBC, U&E, glucose, LFT, TFT, CRP), urine, ECG, sepsis screen.",
      "Management: treat the underlying cause, non-pharmacological measures first (reorientation, family, sensory aids, mobilisation, sleep), avoid sedatives.",
      "Prevent: early mobilisation, hydration, avoid unnecessary catheters/drugs, good sleep hygiene."
    ],
    "drugs": [
      {"name": "Treat the cause (antibiotics etc.)", "when": "Always — delirium is a symptom", "notes": "Infection, dehydration, constipation, retention are common"},
      {"name": "Haloperidol (cautious)", "when": "Severe distress/risk not controlled by non-drug measures", "notes": "Low dose; avoid in Parkinson's/dementia with Lewy bodies (use quetiapine); ECG monitoring"},
      {"name": "Avoid benzodiazepines", "when": "Generally", "notes": "Worsen delirium; except in alcohol withdrawal"}
    ],
    "clinicalScenarios": [
      {"scenario": "Elderly patient with acute fluctuating confusion and inattention.", "answer": "Delirium — hunt for the cause (PINCH ME); treat the underlying problem."},
      {"scenario": "Confused patient with a raised WCC and fever.", "answer": "Delirium from infection — treat sepsis, reorient, avoid sedation."},
      {"scenario": "Confused elderly patient with a palpable bladder.", "answer": "Urinary retention — catheterise; retention is a common reversible cause of delirium."},
      {"scenario": "Agitated delirious patient at risk of falling.", "answer": "Non-pharmacological measures first; use a low-dose antipsychotic only if severe distress/risk persists."}
    ],
    "keyValues": [
      ["Delirium", "Acute, fluctuating, inattention"],
      ["Common causes", "Infection, drugs, metabolic, constipation, retention, pain"],
      ["AMT4", "Age, date of birth, place, year"],
      ["Avoid", "Sedatives unless severe distress"]
    ],
    "redFlags": [
      "New confusion + fever — sepsis, treat urgently.",
      "Hypoglycaemia, hypoxia, or hypotension causing confusion — correct immediately.",
      "Focal neurology or head injury — consider intracranial bleed."
    ],
    "management": [
      "Screen for and treat the underlying cause (PINCH ME).",
      "Non-pharmacological measures first (reorientation, family, sensory aids).",
      "Avoid sedatives; use cautiously only for severe distress/risk.",
      "Prevent: mobilisation, hydration, avoid catheters, good sleep."
    ],
    "pitfalls": [
      "Delirium is a symptom — always find and treat the cause.",
      "Do not sedate a delirious patient as a first response.",
      "Avoid antipsychotics in Parkinson's disease and Lewy body dementia."
    ]
  },

  "falls-elderly": {
    "name": "Falls in elderly persons",
    "group": "Neurology & elderly",
    "overview": "Falls are multifactorial and often a marker of serious underlying disease. The exam tests the causes (including cardiac and drug-related) and the injury/complication screen.",
    "essentials": [
      "Falls in the elderly are multifactorial: intrinsic (postural hypotension, gait/balance, visual, cognitive, medication, cardiac syncope) + extrinsic (environmental hazards).",
      "Assess the cause: circumstances, loss of consciousness, prodrome, medications (antihypertensives, sedatives), mobility, vision, cognition, cardiac causes.",
      "Examine for injury: head injury, fracture (hip, wrist, pelvis), soft tissue. Check for 'long lie' (rhabdomyolysis, hypothermia, pressure injury).",
      "Investigations: FBC, U&E, glucose, ECG, lying/standing BP; cardiac monitoring if syncope suspected.",
      "Prevention: multifactorial intervention — medication review, strength/balance exercise, vision, home hazard reduction, treat postural hypotension."
    ],
    "drugs": [
      {"name": "Review culprit drugs", "when": "All falls", "notes": "Antihypertensives, sedatives, anticholinergics, hypoglycaemics"},
      {"name": "Analgesia", "when": "Injury/pain", "notes": "Regular; avoid over-sedation"},
      {"name": "Calcium/vitamin D", "when": "Osteoporosis risk", "notes": "Bone health; assess fracture risk (FRAX)"},
      {"name": "Treatment of postural hypotension", "when": "Confirmed on lying/standing BP", "notes": "Fludrocortisone/midodrine (specialist) + lifestyle measures"}
    ],
    "clinicalScenarios": [
      {"scenario": "Elderly patient found on the floor several hours later.", "answer": "Look for 'long lie' complications — rhabdomyolysis, hypothermia, pressure injury; check CK and renal function."},
      {"scenario": "Elderly patient on an antihypertensive with recurrent falls and a 25 mmHg BP drop on standing.", "answer": "Postural hypotension — review the drug, hydration, and lying/standing BP."},
      {"scenario": "Fall with a head injury in a patient on anticoagulation.", "answer": "CT head and reverse anticoagulation — high risk of intracranial bleed."},
      {"scenario": "Fall with hip pain and inability to weight-bear.", "answer": "X-ray to exclude hip fracture; analgesia and orthopaedic referral."},
      {"scenario": "Recurrent unexplained falls with no prodrome.", "answer": "Consider cardiac cause (arrhythmia) — ECG and cardiac monitoring."}
    ],
    "keyValues": [
      ["Postural hypotension", "SBP drop ≥20 mmHg on standing"],
      ["Long lie", ">1 h on floor — rhabdo, hypothermia, pressure injury"],
      ["Common fractures", "Hip, wrist, pelvis"],
      ["Prevention", "Medication review, exercise, vision, home safety"]
    ],
    "redFlags": [
      "Fall with head injury on anticoagulation — CT head, reverse anticoagulation.",
      "Fall with hip pain/inability to weight-bear — X-ray, exclude fracture.",
      "Recurrent falls or syncope — cardiac assessment."
    ],
    "management": [
      "Assess and treat any injury (fracture, head injury).",
      "Identify the cause (postural hypotension, medication, cardiac, gait).",
      "Multifactorial prevention: medication review, exercise, vision, home safety.",
      "Check for long-lie complications."
    ],
    "pitfalls": [
      "Always check lying/standing BP — postural hypotension is a common, treatable cause.",
      "Do not dismiss a fall as 'mechanical' — look for syncope and cardiac causes.",
      "In the elderly, a fall may be the presenting sign of sepsis, MI or a new medication effect."
    ]
  },

  "obs-gynae-emergencies": {
    "name": "Gynaecology and Obstetric emergencies",
    "group": "Obstetrics & gynaecology",
    "overview": "Bleeding in pregnancy, ectopic pregnancy and postpartum haemorrhage are the key emergencies. The exam tests thinking of pregnancy in any woman of reproductive age with abdominal pain.",
    "essentials": [
      "Ectopic pregnancy: pregnancy + abdominal pain/bleeding/collapse. Ruptured ectopic is a surgical emergency (haemorrhagic shock). Always do a pregnancy test in any woman of reproductive age with abdominal pain.",
      "Miscarriage: vaginal bleeding in early pregnancy — threatened, inevitable, missed, complete. USS confirms; manage expectantly/medically/surgically (ERPC).",
      "Antepartum haemorrhage (APH): bleeding after 24 weeks — placenta praevia (painless) vs placental abruption (painful, rigid uterus, fetal distress). Both emergencies.",
      "Postpartum haemorrhage (PPH): >500 mL (vaginal) or >1000 mL (CS). Treat: call for help, IV access, fluids/blood, uterotonics, identify cause (4 Ts: tone, trauma, tissue, thrombin).",
      "Pre-eclampsia/eclampsia: hypertension + proteinuria after 20 weeks; headache, visual disturbance, epigastric pain are red flags."
    ],
    "drugs": [
      {"name": "Oxytocin", "when": "PPH (first-line uterotonic)", "notes": "IV/IM; also used for induction/augmentation"},
      {"name": "Ergometrine", "when": "PPH (if not hypertensive/pre-eclamptic)", "notes": "Contraindicated in hypertension/pre-eclampsia"},
      {"name": "Carboprost (prostaglandin)", "when": "PPH refractory to first-line", "notes": "Contraindicated in asthma"},
      {"name": "Magnesium sulfate", "when": "Eclampsia / severe pre-eclampsia", "notes": "IV; prevents/treats seizures; monitor reflexes and respiratory rate"},
      {"name": "Antihypertensives (labetalol/nifedipine)", "when": "Severe hypertension in pre-eclampsia", "notes": "Control BP; hydralazine IV in crisis"},
      {"name": "Anti-D immunoglobulin", "when": "Rh-negative women with bleeding/sensitising events", "notes": "Prevents haemolytic disease of the newborn"},
      {"name": "Methotrexate", "when": "Selected stable ectopic pregnancies", "notes": "Specialist; not for ruptured ectopic"}
    ],
    "clinicalScenarios": [
      {"scenario": "Woman of reproductive age with lower abdominal pain, PV bleeding and collapse.", "answer": "Ruptured ectopic pregnancy — pregnancy test, resuscitate, urgent gynae/surgery."},
      {"scenario": "PPH of 1200 mL after delivery.", "answer": "Call for help, IV access, fluids/blood, oxytocin, identify the cause (4 Ts)."},
      {"scenario": "Painless PV bleeding at 34 weeks with placenta praevia on USS.", "answer": "Antepartum haemorrhage — admit, monitor mother and fetus, plan delivery; avoid PV examination."},
      {"scenario": "Painful bleeding with a rigid uterus and fetal distress.", "answer": "Placental abruption — emergency, resuscitate and arrange urgent delivery."},
      {"scenario": "34-week pregnant patient with headache, visual disturbance and BP 170/110.", "answer": "Severe pre-eclampsia — control BP, magnesium sulfate, urgent obstetric review/delivery."}
    ],
    "keyValues": [
      ["Ectopic", "Pregnancy + pain/bleeding/collapse — emergency"],
      ["PPH", ">500 mL (vaginal) / >1000 mL (CS)"],
      ["PPH 4 Ts", "Tone, trauma, tissue, thrombin"],
      ["Pre-eclampsia", "HTN + proteinuria after 20 weeks"],
      ["Eclampsia treatment", "Magnesium sulfate"]
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
    ],
    "pitfalls": [
      "Never miss an ectopic — always check a pregnancy test.",
      "Do not perform a PV examination in suspected placenta praevia.",
      "Ergometrine is contraindicated in hypertension/pre-eclampsia."
    ]
  },

  "skin-rashes": {
    "name": "Skin rashes in the acute setting",
    "group": "Dermatology",
    "overview": "Most rashes are benign, but a few are emergencies. The exam tests recognising the life-threatening rashes first (meningococcal, SJS/TEN, necrotising fasciitis).",
    "essentials": [
      "Identify life-threatening rashes first: meningococcal septicaemia (non-blanching purpura, fever, ill), SJS/TEN (blistering, mucosal involvement, drug-induced), necrotising fasciitis (severe pain, rapidly spreading), anaphylaxis (urticaria + systemic).",
      "Non-blanching purpura + fever = meningococcal until proven otherwise — IV antibiotics immediately.",
      "Common rashes: urticaria (allergic, itchy, blanch), cellulitis (erythema, warmth, pain, fever), shingles (vesicular, dermatomal, painful), scabies (itchy, burrows), drug eruptions.",
      "Assess: distribution, morphology (macule, papule, vesicle, bulla, purpura), mucosal involvement, systemic symptoms, drug history.",
      "Cellulitis: IV/oral antibiotics, mark the edge, monitor. Erysipelas: superficial, well-demarcated."
    ],
    "drugs": [
      {"name": "IV antibiotics (e.g. ceftriaxone)", "when": "Suspected meningococcal sepsis", "notes": "Immediately — do not wait for confirmation"},
      {"name": "Antihistamines", "when": "Urticaria/allergic rash", "notes": "Symptomatic; remove the trigger"},
      {"name": "Antibiotics (flucloxacillin/penicillin)", "when": "Cellulitis", "notes": "Per local policy; mark the edge and monitor"},
      {"name": "Aciclovir", "when": "Shingles (within 72 h, or severe)", "notes": "Antiviral; analgesia important"},
      {"name": "Stop the culprit drug", "when": "SJS/TEN / drug eruption", "notes": "Immediate drug withdrawal is the key step"},
      {"name": "Adrenaline (IM)", "when": "Anaphylaxis with urticaria", "notes": "500 mcg IM; first-line"}
    ],
    "clinicalScenarios": [
      {"scenario": "Febrile, unwell child with a non-blanching purpuric rash.", "answer": "Meningococcal sepsis — IV antibiotics immediately."},
      {"scenario": "Patient on a new drug with widespread blistering and oral mucosal involvement.", "answer": "SJS/TEN — stop the culprit drug and seek urgent specialist care."},
      {"scenario": "Rapidly spreading painful erythema with crepitus.", "answer": "Necrotising fasciitis — urgent surgical debridement + IV antibiotics."},
      {"scenario": "Unilateral painful vesicular rash in a dermatomal distribution.", "answer": "Shingles — aciclovir (± within 72 h) and analgesia."},
      {"scenario": "Well patient with itchy blanching wheals after a new food.", "answer": "Urticaria — antihistamines, remove the trigger; treat anaphylaxis if systemic."}
    ],
    "keyValues": [
      ["Meningococcal", "Non-blanching purpura + fever → IV antibiotics"],
      ["SJS/TEN", "Blistering + mucosal involvement, drug-induced"],
      ["Cellulitis", "Erythema + warmth + pain + fever"],
      ["Shingles", "Vesicular, dermatomal, painful"]
    ],
    "redFlags": [
      "Non-blanching rash + fever/illness — meningococcal, treat immediately.",
      "Rapidly spreading painful erythema — necrotising fasciitis.",
      "Blistering + mucosal involvement — SJS/TEN, stop the culprit drug."
    ],
    "management": [
      "ABC; treat life-threatening rashes immediately (meningococcal antibiotics).",
      "Cellulitis: antibiotics, mark the edge, monitor response.",
      "Urticaria: antihistamines, remove the trigger, treat anaphylaxis if systemic.",
      "Identify and stop culprit drugs in drug eruptions."
    ],
    "pitfalls": [
      "A non-blanching rash in a febrile patient is an emergency — act before the diagnosis is confirmed.",
      "Do not miss mucosal involvement in a blistering rash — it suggests SJS/TEN.",
      "Always take a drug history — many acute rashes are drug-induced."
    ]
  },
}
