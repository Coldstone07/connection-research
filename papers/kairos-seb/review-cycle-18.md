# Review Cycle 18 — Kairos-SEB (3-Reviewer Panel, ACII 2027)

**Date:** 2026-04-29
**Reviewer structure:** 3 independent parallel reviewers (Methodologist, Benchmark Expert, Skeptic)
**Draft version:** stage-17/paper_draft.md (post-Cycle-17 fixes applied)
**Panel verdict:** A — Weak Accept; B — Weak Accept; C — Weak Accept

---

## Panel Findings Summary

| Reviewer | Verdict | MUST FIX |
|----------|---------|----------|
| A — Methodologist | Weak Accept | 3: Fisher 2×2 contingency table absent; "not a surface linguistic complexity gradient" causal overclaim; MCIP/MCCIP undefined at first abstract use |
| B — Benchmark Expert | Weak Accept | 3: paraphrase sensitivity analysis cannot be deferred; calibration circularity scope for GPT-5.4 unknown within hard tier; "shared ceiling near 50%" ungrounded in abstract |
| C — Skeptic | Weak Accept | 2: Abstract "identifies a developmental ceiling" asserts confirmation; §9 fuses single-model formal inference and five-model informal observation in same grammatical breath |

---

## Cycle 17 Resolution Scorecard

| Item | Status |
|------|--------|
| A/C-C17-MF1 (one-tailed p removed from §4.2 and Table 4) | FULLY RESOLVED |
| A-C17-MF2 (bootstrap CI ±0.08 removed) | FULLY RESOLVED |
| B-C17-MF3 ("consistent with statistically significant" → honest framing) | FULLY RESOLVED |
| B-C17-MF4 (§6.3 opening: Fisher result unaffected by calibration circularity) | FULLY RESOLVED |
| B-C17-MF5 (§6.5 surface-proficiency hypothesis re-anchored in V1 Extended) | FULLY RESOLVED |
| C-C17-MF6 (§9 "preliminary"/"requires external tier validation" restored) | FULLY RESOLVED |

---

## 8 MUST FIX Items — All Applied

**A-C18-MF1 (Methodologist): The Fisher 2×2 contingency table — all 4 cells — must appear in the paper for any reader to verify the test input.**
The paper reports the Fisher result (p ≈ 0.053) and discusses the medium-vs-hard gap extensively, but never presents the raw 2×2 count table from which the test is computed. Reviewers and readers cannot verify the test without these four numbers: Medium correct (12), Medium incorrect (0), Hard correct (7), Hard incorrect (5). The table must appear in §6.3 at the point of the primary statistical result.
Fix applied: Added explicit 2×2 contingency table in §6.3 immediately before the Fisher p-value sentence, labelled "Table 4a: Fisher 2×2 Contingency Table — Medium vs. Hard Accuracy (Gemini 2.5 Flash, V1 Extended)."

**A-C18-MF2 (Methodologist): "the difficulty stratification produces an observed capability gap, not a surface linguistic complexity gradient" is a causal claim that p ≈ 0.053 cannot support.**
The phrase "not a surface linguistic complexity gradient" performs a negative causal exclusion — it rules out an alternative mechanism. The data show an accuracy gap; they do not permit ruling out surface complexity as a contributor. The honest framing is that the results are consistent with a capability gap rather than a surface complexity gradient, but this cannot be established from the current evidence alone.
Fix applied: Changed to "the difficulty stratification produces an observed accuracy gap consistent with, but not establishing, a developmental capability gap rather than a surface linguistic complexity gradient; distinguishing between these mechanisms requires external tier validation."

**A-C18-MF3 (Methodologist): MCIP and MCCIP appear undefined at first use in the Abstract.**
MCIP and MCCIP are formally defined in §6.1 with mathematical formulas. However, the Abstract — the paper's highest-visibility section — uses both acronyms without expansion: "MCIP ≈ 0.93 vs. MCCIP ≈ 0.94." A reader who reads only the Abstract cannot decode these acronyms. At first use in the Abstract, both acronyms must be expanded.
Fix applied: Abstract now reads "Mean Confidence on Incorrect Predictions (MCIP) ≈ 0.93 vs. Mean Confidence on Correct Predictions (MCCIP) ≈ 0.94."

**B-C18-MF1 (Benchmark Expert): "A formal sensitivity analysis ... is deferred to the full dataset release evaluation" cannot stand as a submission commitment.**
The paper promises a paraphrase_flag=0 sensitivity analysis at dataset release. At submission, this analysis has not been completed. Deferring an analysis that directly bears on the validity of the paper's central statistical result (the hard-tier Fisher finding) to a post-acceptance deliverable is not an acceptable scientific commitment. The honest treatment is to acknowledge this as an open limitation without implying it will be resolved before camera-ready.
Fix applied: Changed to "A formal sensitivity analysis restricted to `paraphrase_flag=0` hard-tier scenarios only cannot be completed for this submission, as per-scenario paraphrase records have not been confirmed at item level. This is an open limitation. The estimated 8 of 12 hard-tier scenarios that are original author-drafted (§5.1, ≈67%) is a descriptive estimate only and does not substitute for a completed audit."

**B-C18-MF2 (Benchmark Expert): §8 Calibration circularity does not disclose that the specific items GPT-5.4 influenced during calibration cannot be identified, and therefore the scope of circularity within the hard tier is unknown.**
The §8 limitation states that GPT-5.4 results are subject to calibration circularity. However, the specific scenarios that GPT-5.4's calibration outputs affected are not documented. Without this mapping, it is unknowable whether GPT-5.4's calibration outputs were concentrated in hard-tier scenarios — which would mean the hard-tier scenario labels themselves carry GPT-5.4 influence — or in other tiers. This is a stronger limitation than the text currently acknowledges.
Fix applied: Added to §8 Calibration circularity: "The specific scenarios that GPT-5.4 influenced through calibration outputs cannot be identified at this stage; no item-level mapping from calibration runs to difficulty-tier assignments was maintained. The scope of calibration circularity for GPT-5.4's hard-tier performance is therefore unknown, not merely acknowledged."

**B-C18-MF3 (Benchmark Expert): "Informal observation across all five models suggests a shared ceiling near 50%, requiring formal multi-model confirmation" should not appear in the Abstract.**
The Abstract is the paper's authoritative summary of findings. The "shared ceiling near 50%" is an informal observational estimate with no per-scenario records, no CIs, and explicitly non-citable status (§6.4). Abstract-level claims must be formally grounded. The informal observation belongs in §6.4 and §7, not in the abstract summary of findings.
Fix applied: Removed from Abstract. The abstract now ends the findings summary with the formal Gemini result and null calibration observation; the informal multi-model observation is retained in §6.4 only.

**C-C18-MF1 (Skeptic): "Empirical evaluation identifies a developmental ceiling" — "identifies" asserts confirmed detection when the primary result does not reach α = 0.05.**
"Identifies" is an active verb that asserts the empirical evaluation has located and confirmed the developmental ceiling. With p ≈ 0.053 (primary, two-tailed, not reaching α = 0.05) and no external tier validation, "identifies" overclaims. The appropriate framing is that the evaluation provides directional evidence for or is consistent with a developmental ceiling.
Fix applied: Changed to "Empirical evaluation provides directional evidence for a **developmental ceiling**."

**C-C18-MF2 (Skeptic): §9 fuses the formally grounded single-model inference (Gemini 2.5 Flash, p ≈ 0.053) and the five-model informal observation (§6.4, non-citable) in a single grammatical construction with the same epistemic status.**
"These results are consistent with the preliminary hypothesis that at least one evaluated frontier model (Gemini 2.5 Flash) may exhibit ... — a preliminary inference that requires external tier validation to confirm — with informal observations across five models consistent with a shared pattern that requires formal multi-model replication to confirm." The em-dash construction grammatically chains a formally-grounded inference and an informally-grounded observation as though they carry equal weight. They do not. These must be separated into distinct sentences with explicit epistemic labels.
Fix applied: Split into two sentences: (1) the formal single-model inference with full hedging; (2) a separate sentence explicitly labelled as informal, directional context only, with no evidentiary weight claimed.

---

## SHOULD FIX Items (noted for camera-ready)

- A/B/C-C18-SF1: Redundant double-appearance of "Two additional interpretive caveats..." paragraph in §6.3 — duplicated block should be removed
- B-C18-SF2: Table 5 V2 Hard row shows "≈50.0%" in bold — bold conventionally denotes best result per axis, but this is an informal estimate; remove bold or add footnote clarifying the bold convention does not apply to informal rows
- C-C18-SF3: §6.5 "characteristic shape" (Figure 1 caption reference) — "characteristic shape" implies replicability not supported by n=12 from one model; add "in the current sample"

---

## Cycle 19 Panel: Run 3 independent reviewers again
