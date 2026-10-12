# Clinical notes part 2: GI/hepatology, haematology/oncology, endocrine, neuro/elderly.
PART = {
  "gi-bleeds": {
    "name": "Gastrointestinal bleeds",
    "group": "Gastrointestinal & hepatology",
    "essentials": [
      "Upper GI bleed (haematemesis, melaena): most commonly peptic ulcer, varices (in cirrhosis), Mallory-Weiss tear, gastritis. Lower GI bleed (fresh PR bleeding): diverticular, angiodysplasia, colorectal cancer, haemorrhoids.",
      "Assess severity: haemodynamic status, Hb drop, shock. A patient with melaena + haemodynamic compromise has a significant upper GI bleed.",
      "Resuscitate first: IV access (2 large-bore), bloods (FBC, U&E, LFT, crossmatch), fluids/blood, correct coagulopathy. Consider tranexamic acid.",
      "Upper GI: urgent endoscopy (within 24h; within 1h for variceal/significant). Variceal bleed: terlipressin + antibiotics + endoscopic banding.",
      "Risk scores (Rockall, Glasgow-Blatchford) guide need for endoscopy and admission. Re-bleeding or haemodynamic instability → repeat endoscopy/surgery/IR."
    ],
    "keyValues": [
      ["Glasgow-Blatchford", "≥1 → endoscopy; high score → urgent"],
      ["Variceal bleed Rx", "Terlipressin + antibiotics + banding"],
      ["Endoscopy timing", "Within 24h (1h if variceal/severe)"],
      ["Transfusion trigger", "Hb < 70-80 g/L (higher if cardiac)"]
    ],
    "redFlags": [
      "Haematemesis with shock — massive bleed, resuscitate aggressively.",
      "Variceal bleed (cirrhosis) — high mortality, terlipressin + antibiotics urgently.",
      "Re-bleeding after endoscopy — escalate."
    ],
    "management": [
      "ABC, 2 large-bore IVs, bloods + crossmatch, fluids/blood, correct coagulopathy.",
      "Upper GI: urgent endoscopy; variceal → terlipressin + antibiotics + banding.",
      "Lower GI: resuscitate, identify source (colonoscopy/CT), treat cause.",
      "Monitor Hb, haemodynamics; repeat endoscopy if re-bleeding."
    ]
  },
  "hepatic-encephalopathy": {
    "name": "Hepatic encephalopathy",
    "group": "Gastrointestinal & hepatology",
    "essentials": [
      "Neuropsychiatric syndrome in liver failure due to accumulation of ammonia and other toxins (impaired hepatic clearance). Precipitants: GI bleed, infection, constipation, electrolyte disturbance, sedatives, dehydration, high protein load.",
      "Grading: I (mild confusion, altered sleep), II (lethargy, disorientation), III (somnolent but rousable), IV (coma).",
      "Clinical: altered consciousness, asterixis (flapping tremor), confusion, personality change, fetor hepaticus.",
      "Management: identify and treat the precipitant (bleed, infection, constipation), lactulose (reduces ammonia via gut), rifaximin (add-on), correct electrolytes, avoid sedatives.",
      "Exclude other causes of confusion (hypoglycaemia, sepsis, intracranial bleed, Wernicke's)."
    ],
    "keyValues": [
      ["Ammonia", "Elevated in hepatic encephalopathy"],
      ["Lactulose", "First-line; titrate to 2-3 stools/day"],
      ["Rifaximin", "Add-on for recurrent encephalopathy"],
      ["West Haven grade", "I-IV (I mild confusion → IV coma)"]
    ],
    "redFlags": [
      "Grade III-IV encephalopathy — airway protection, ICU.",
      "New confusion in cirrhosis — always exclude GI bleed, sepsis, hypoglycaemia.",
      "Deterioration despite treatment — re-evaluate for precipitants."
    ],
    "management": [
      "Treat the precipitant (bleed, infection, constipation, electrolytes).",
      "Lactulose (oral/enema), add rifaximin if recurrent.",
      "Correct electrolytes, avoid sedatives and high protein load acutely.",
      "Exclude other causes of altered consciousness."
    ]
  },
  "ascites": {
    "name": "Ascites",
    "group": "Gastrointestinal & hepatology",
    "essentials": [
      "Ascites = accumulation of fluid in the peritoneal cavity. Most common cause is portal hypertension (cirrhosis); other causes: malignancy, heart failure, nephrotic syndrome, TB, pancreatitis.",
      "Diagnosis: clinical (shifting dullness, fluid thrill), USS, diagnostic paracentesis. SAAG (serum-ascites albumin gradient) distinguishes portal hypertension (SAAG ≥ 11 g/L) from other causes.",
      "Cirrhotic ascites: sodium restriction, spironolactone (aldosterone antagonist), furosemide. Large-volume paracentesis with albumin for tense ascites.",
      "Complications: spontaneous bacterial peritonitis (SBP) — fever, abdominal pain, rising WCC; refractory ascites; hepatorenal syndrome.",
      "SBP: diagnostic paracentesis (neutrophils > 250/mm3), IV antibiotics (cefotaxime), albumin."
    ],
    "keyValues": [
      ["SAAG", "≥11 g/L = portal hypertension"],
      ["SBP diagnosis", "Ascitic neutrophils > 250/mm3"],
      ["SBP Rx", "IV cefotaxime + albumin"],
      ["First-line diuretic", "Spironolactone"]
    ],
    "redFlags": [
      "Fever/abdominal pain in ascites — SBP, urgent paracentesis + antibiotics.",
      "Rising creatinine with ascites — hepatorenal syndrome.",
      "Tense ascites with respiratory compromise — therapeutic paracentesis + albumin."
    ],
    "management": [
      "Diagnostic paracentesis: SAAG, cell count, culture, albumin.",
      "Cirrhotic ascites: sodium restriction, spironolactone ± furosemide.",
      "Tense ascites: large-volume paracentesis with IV albumin.",
      "SBP: IV antibiotics + albumin; treat the underlying liver disease."
    ]
  },
  "jaundice": {
    "name": "Jaundice",
    "group": "Gastrointestinal & hepatology",
    "essentials": [
      "Jaundice = yellow discolouration from hyperbilirubinaemia. Classify: pre-hepatic (haemolysis — unconjugated), hepatic (hepatocellular — mixed), post-hepatic (obstructive — conjugated, cholestatic).",
      "Pre-hepatic: haemolysis (raised unconjugated bilirubin, normal LFTs, reticulocytosis, low haptoglobin).",
      "Hepatic: viral hepatitis, alcohol, drugs, autoimmune, cirrhosis — raised transaminases (ALT/AST).",
      "Post-hepatic/obstructive: gallstones, malignancy (pancreatic head), stricture — raised ALP/GGT, conjugated bilirubin, pale stools, dark urine.",
      "Investigations: LFTs, bilirubin (total/conjugated), FBC, USS (biliary dilatation), viral serology, autoimmune screen. Urgent if cholangitis (Charcot's triad: fever, jaundice, RUQ pain)."
    ],
    "keyValues": [
      ["Pre-hepatic", "Unconjugated bilirubin, normal LFTs, haemolysis"],
      ["Hepatic", "Raised ALT/AST (hepatocellular)"],
      ["Obstructive", "Raised ALP/GGT, conjugated bilirubin"],
      ["Cholangitis", "Fever + jaundice + RUQ pain (Charcot's triad)"]
    ],
    "redFlags": [
      "Cholangitis — IV antibiotics + urgent biliary drainage (ERCP).",
      "Acute liver failure (coagulopathy, encephalopathy) — urgent hepatology/ICU.",
      "Painless jaundice in elderly — think pancreatic malignancy."
    ],
    "management": [
      "Classify the type of jaundice (pre-hepatic/hepatic/post-hepatic).",
      "LFTs, bilirubin, FBC, USS; further tests by suspected cause.",
      "Obstructive: treat cause (ERCP for stones, drainage for malignancy).",
      "Cholangitis: IV antibiotics, urgent biliary drainage."
    ]
  },
  "neutropenic-sepsis": {
    "name": "Neutropenic sepsis",
    "group": "Haematology & acute oncology",
    "essentials": [
      "Neutropenic sepsis = temperature ≥38°C (or signs of sepsis) with neutrophil count < 0.5 × 10^9/L, in a patient on chemotherapy or with haematological malignancy. A medical emergency.",
      "Neutropenic patients have no inflammatory response — they may present with minimal signs. Any fever or feeling unwell in a neutropenic patient is treated as sepsis until proven otherwise.",
      "Immediate management (within 1 hour): blood cultures, FBC, U&E, LFT, CRP, lactate, then IV broad-spectrum antibiotics (per local policy, e.g. piperacillin-tazobactam) WITHOUT waiting for results.",
      "Look for a source: line infection, chest, urine, skin, perianal. Consider antifungal if persistent fever despite antibiotics.",
      "Monitor: temperature, observations, cultures, response to antibiotics. Escalate if deteriorating."
    ],
    "keyValues": [
      ["Neutropenia", "Neutrophils < 0.5 × 10^9/L"],
      ["Fever threshold", "≥38°C (or any sepsis signs)"],
      ["Antibiotics within", "1 hour of presentation"],
      ["First-line", "IV broad-spectrum (e.g. piperacillin-tazobactam)"]
    ],
    "redFlags": [
      "Any fever in a neutropenic patient — treat as sepsis immediately.",
      "Hypotension/shock — aggressive resuscitation + antibiotics.",
      "Persistent fever despite 48-72h antibiotics — consider fungal infection."
    ],
    "management": [
      "Sepsis Six + blood cultures, FBC, lactate, then IV antibiotics within 1 hour.",
      "Look for and treat the source (line, chest, urine, skin).",
      "Monitor response; add antifungal if persistent fever.",
      "Involve haematology/oncology team early."
    ]
  },
  "congenital-bleeding": {
    "name": "Congenital bleeding disorders",
    "group": "Haematology & acute oncology",
    "essentials": [
      "Haemophilia A (factor VIII deficiency) and B (factor IX deficiency): X-linked, bleeding into joints (haemarthrosis) and muscles. Severity by factor level.",
      "von Willebrand disease: most common inherited bleeding disorder; mucocutaneous bleeding (epistaxis, menorrhagia, easy bruising); prolonged bleeding time, low vWF.",
      "Acute bleeding in haemophilia: replace the missing factor (factor VIII/IX concentrate) urgently. Avoid IM injections, aspirin, NSAIDs.",
      "Haemarthrosis: factor replacement + analgesia + rest; avoid joint aspiration unless tense.",
      "Carrier/affected patients need specialist haematology input for surgery, dental work, and major bleeding."
    ],
    "keyValues": [
      ["Haemophilia A", "Factor VIII deficiency (X-linked)"],
      ["Haemophilia B", "Factor IX deficiency (X-linked)"],
      ["vWD", "vWF deficiency; mucocutaneous bleeding"],
      ["Haemarthrosis Rx", "Factor replacement + analgesia + rest"]
    ],
    "redFlags": [
      "Major bleeding or head injury in a haemophiliac — urgent factor replacement.",
      "Intracranial bleed — factor replacement + urgent imaging.",
      "Bleeding not controlled by factor — check for inhibitors."
    ],
    "management": [
      "Acute bleed: replace the deficient factor urgently.",
      "Haemarthrosis: factor + analgesia + rest, avoid aspiration.",
      "Avoid aspirin/NSAIDs/IM injections.",
      "Involve haematology for all significant bleeds and procedures."
    ]
  },
  "spinal-cord-compression": {
    "name": "Spinal cord compression",
    "group": "Haematology & acute oncology",
    "essentials": [
      "Malignant spinal cord compression (MSCC) is an oncological emergency: cord/cauda equina compression by tumour (metastatic, especially prostate, breast, lung, myeloma).",
      "Red flags: new back pain (especially thoracic), progressive neurological deficit, sensory level, bladder/bowel dysfunction, gait disturbance. Back pain + neurological symptoms in a cancer patient = MSCC until proven otherwise.",
      "Immediate: high-dose dexamethasone (reduces oedema), urgent MRI whole spine (within 24h), oncology/neurosurgery referral.",
      "Do not delay imaging for the diagnosis — treat empirically if high suspicion.",
      "Outcome depends on pre-treatment neurological status — early recognition is critical."
    ],
    "keyValues": [
      ["Dexamethasone", "High-dose (e.g. 16 mg/day) urgently"],
      ["MRI whole spine", "Within 24h of suspicion"],
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
      "Urgent MRI whole spine (within 24h).",
      "Oncology/neurosurgery referral; treat the primary malignancy.",
      "Analgesia, log-roll care, monitor neurology."
    ]
  },
  "diabetes-control": {
    "name": "Diabetes control",
    "group": "Endocrine & metabolic",
    "essentials": [
      "Diabetes: type 1 (insulin deficiency, autoimmune) vs type 2 (insulin resistance + relative deficiency). Acute complications: DKA, HHS, hypoglycaemia.",
      "DKA (type 1): hyperglycaemia + ketonaemia + acidosis. Precipitants: infection, missed insulin, MI, stress. Treat: IV fluids, fixed-rate insulin infusion, potassium replacement, treat precipitant.",
      "HHS (type 2): severe hyperglycaemia without significant ketosis/acidosis, marked dehydration. Treat: fluids (often large volumes), insulin cautiously, correct electrolytes.",
      "Inpatient glycaemic control: monitor glucose, adjust insulin (basal-bolus), avoid prolonged hypoglycaemia/hyperglycaemia, involve diabetes team.",
      "Sick-day rules: never stop insulin in type 1, increase monitoring, seek help if vomiting/unwell."
    ],
    "keyValues": [
      ["DKA", "Glucose + ketones + acidosis (pH < 7.3, HCO3 < 18)"],
      ["HHS", "Glucose often > 30 mmol/L, no significant ketosis"],
      ["DKA Rx", "IV fluids, fixed-rate insulin, K+ replacement"],
      ["Glucose target (inpatient)", "6-10 mmol/L"]
    ],
    "redFlags": [
      "DKA with K+ < 3.5 — replace K+ before insulin (insulin drops K+).",
      "HHS with severe dehydration — large fluid resuscitation.",
      "Recurrent hypoglycaemia — review insulin regimen."
    ],
    "management": [
      "DKA: fluids, fixed-rate insulin, K+ replacement, treat precipitant, monitor glucose/ketones/K+.",
      "HHS: aggressive fluids, cautious insulin, correct electrolytes.",
      "Inpatient: basal-bolus insulin, monitor glucose, diabetes team input.",
      "Educate on sick-day rules and never stopping insulin in type 1."
    ]
  },
  "hypoglycaemia": {
    "name": "Hypoglycaemia",
    "group": "Endocrine & metabolic",
    "essentials": [
      "Hypoglycaemia = glucose < 4.0 mmol/L (in diabetics) with symptoms. Causes: excess insulin/oral hypoglycaemics, missed meals, exercise, alcohol, sepsis, renal/hepatic failure.",
      "Symptoms: autonomic (sweating, tremor, palpitations, hunger) and neuroglycopenic (confusion, drowsiness, seizures, coma).",
      "Treatment: if conscious and able to swallow → oral fast-acting carbohydrate (glucose tablets, sugary drink), then long-acting (starchy food). If unconscious/unable → IV glucose (10%) or IM glucagon.",
      "Recheck glucose after treatment; repeat if still low. Identify and treat the cause.",
      "Inpatients: review insulin regimen, consider reducing doses, monitor glucose, involve diabetes team."
    ],
    "keyValues": [
      ["Hypoglycaemia", "Glucose < 4.0 mmol/L"],
      ["Conscious Rx", "Oral fast-acting carbohydrate"],
      ["Unconscious Rx", "IV 10% glucose or IM glucagon"],
      ["Recheck", "Glucose 10-15 min after treatment"]
    ],
    "redFlags": [
      "Unconscious/seizuring — IV glucose/glucagon, protect airway.",
      "Recurrent hypoglycaemia — review medication, look for cause.",
      "Hypoglycaemia in a non-diabetic — investigate (insulinoma, adrenal, sepsis)."
    ],
    "management": [
      "Conscious: oral glucose, then long-acting carbohydrate.",
      "Unconscious: IV 10% glucose or IM glucagon, recheck.",
      "Identify and treat the cause (insulin dose, missed meal, sepsis).",
      "Review and adjust the diabetes regimen; involve diabetes team."
    ]
  },
  "diabetic-foot": {
    "name": "Diabetic foot complications + sepsis",
    "group": "Endocrine & metabolic",
    "essentials": [
      "Diabetic foot disease results from neuropathy (loss of protective sensation) + ischaemia (PAD) + infection. Ulcers are often painless and on pressure points.",
      "Assess: neurovascular status (monofilament, pulses, ABPI), ulcer depth, signs of infection (erythema, discharge, odour, crepitus), systemic sepsis.",
      "Infected diabetic foot is a surgical emergency — deep infection, osteomyelitis, and gangrene can progress rapidly. IV antibiotics + urgent surgical debridement.",
      "Classify severity (e.g. Wagner, IDSA/IWGDF) to guide management. Osteomyelitis: probe-to-bone, MRI, prolonged antibiotics.",
      "Prevention: foot examination at every diabetes review, podiatry, offloading, tight glycaemic control, smoking cessation."
    ],
    "keyValues": [
      ["Monofilament", "Loss = neuropathy (at risk)"],
      ["Probe-to-bone", "Suggests osteomyelitis"],
      ["Infected foot", "IV antibiotics + urgent debridement"],
      ["ABPI", "Assess ischaemia (caution: calcified vessels in diabetes)"]
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
    ]
  },
  "acute-confusional-states": {
    "name": "Acute confusional states",
    "group": "Neurology & elderly",
    "essentials": [
      "Delirium = acute, fluctuating disturbance of consciousness/attention, common in the elderly and acutely ill. Distinguish from dementia (chronic, progressive) and psychiatric illness.",
      "Causes (PINCH ME / DIMS): infection, drugs, metabolic (electrolytes, glucose, hypoxia), constipation, urinary retention, pain, dehydration, sensory impairment, sleep deprivation.",
      "Assess: history (onset, fluctuation), cognitive testing (AMT4/6-CIT), observations, bloods (FBC, U&E, glucose, LFT, TFT, CRP), urine, ECG, consider sepsis screen.",
      "Management: treat the underlying cause, non-pharmacological (reorientation, family, sensory aids, mobilisation, sleep), avoid sedatives unless severe distress/risk.",
      "Prevent: early mobilisation, hydration, avoid unnecessary catheters/drugs, good sleep hygiene."
    ],
    "keyValues": [
      ["Delirium", "Acute, fluctuating, inattention"],
      ["Common causes", "Infection, drugs, metabolic, constipation, retention, pain"],
      ["AMT4", "Age, DOB, place, year"],
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
    ]
  },
  "falls-elderly": {
    "name": "Falls in elderly persons",
    "group": "Neurology & elderly",
    "essentials": [
      "Falls in the elderly are common and multifactorial: intrinsic (postural hypotension, gait/balance, visual, cognitive, medication, cardiac syncope) + extrinsic (environmental hazards).",
      "Assess the cause: circumstances of the fall, loss of consciousness, prodrome, medications (antihypertensives, sedatives), mobility, vision, cognition, cardiac (arrhythmia, syncope).",
      "Examine for injury: head injury, fracture (hip, wrist, pelvis), soft tissue. Check for 'long lie' (rhabdomyolysis, hypothermia, pressure injury).",
      "Investigations: FBC, U&E, glucose, ECG, lying/standing BP, consider cardiac monitoring if syncope suspected.",
      "Prevention: multifactorial intervention — medication review, strength/balance exercise, vision, home hazard reduction, treat postural hypotension."
    ],
    "keyValues": [
      ["Postural hypotension", "SBP drop ≥20 mmHg on standing"],
      ["Long lie", ">1h on floor — rhabdo, hypothermia, pressure injury"],
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
      "Check for long-lie complications (rhabdo, hypothermia)."
    ]
  },
}
