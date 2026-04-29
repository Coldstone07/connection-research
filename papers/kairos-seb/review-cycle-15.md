# Review Cycle 15 — Kairos-SEB (3-Reviewer Panel, ACII 2027)

**Date:** 2026-04-29
**Reviewer structure:** 3 independent parallel reviewers (Methodologist, Benchmark Expert, Skeptic)
**Draft version:** stage-17/paper_draft.md (post-Cycle-14 fixes applied)
**Panel verdict:** A — Weak Reject; B — Weak Reject; C — Weak Reject

---

## Panel Findings Summary

| Reviewer | Verdict | MUST FIX |
|----------|---------|----------|
| A — Methodologist | Weak Reject | 3: §4.2 Fisher overclaim; Table 4/Table 7 inconsistency; §4.1 calibration language |
| B — Benchmark Expert | Weak Reject | 5: §4.2 Fisher overclaim (concordant A+C); §4.1 calibration language (concordant A); §6.5 "demonstrates" (concordant C); MCIP sign error; paraphrase sensitivity |
| C — Skeptic | Weak Reject | 3: §4.2 Fisher overclaim (concordant A+B); §6.5 "demonstrates" (concordant B); §9 "establish" + "frontier LLMs" overgeneralisation |

---

## Cycle 14 Resolution Scorecard

| Item | Status |
|------|--------|
| A/B/C-C14: Abstract restructured, 1.71× removed | FULLY RESOLVED |
| B/C-C14: Calibration reframed as null observation (abstract, §6.3, §6.5, §7, §9) | PARTIALLY RESOLVED → §4.1 and §3.1 not updated |
| C-C14-MF3: Non-monotonic tier sequence disclosed in §6.3 | FULLY RESOLVED |
| B-C14: paraphrase_flag hard-tier distribution noted in §5.1 | FULLY RESOLVED |

---

## 7 MUST FIX Items — All Applied

**A/B/C-C15-MF1 (3-way concordant): §4.2 uses one-tailed p = 0.037 to claim "Fisher's exact test confirms as statistically significant" when the paper's own primary two-tailed test gives p ≈ 0.053 (boundary of significance, not confirmed).**
The paper states explicitly in §6.3, Table 7, and the Abstract that the two-tailed p ≈ 0.053 is primary and "does not reach α = 0.05." Yet §4.2 writes "a gap that Fisher's exact test confirms as statistically significant (p = 0.037)" — citing only the one-tailed value and using the word "confirms," creating a materially more assertive impression than the paper warrants. A reader of §4.2 without §6.3 context infers a confirmed significant result.
Fix applied: §4.2 changed to "a gap that Fisher's exact test identifies (one-tailed $p = 0.037$; primary two-tailed $p \approx 0.053$, at the boundary of conventional significance — see §6.3)."

**A-C15-MF2 (Methodologist): Table 4 (§6.3) shows "*" significance for Gem-Med vs. Gem-Hrd, inconsistent with Table 7 (§6.5) which shows "marginal†" for the identical comparison.**
Table 4 displays "* p < 0.05" in its footnote — standard convention for significance at α = 0.05 — applied to the one-tailed p = 0.037. Table 7 correctly uses "marginal†" with a nuanced two-tail/one-tail footnote. A reader reaching §6.3 before §6.5 forms an incorrect impression of significance. Table 4 also only shows the one-tailed p-value without a two-tailed column, further obscuring the distinction.
Fix applied: Table 4 updated to show two-tailed p (≈0.053) and one-tailed p (0.037) in separate columns; significance code changed from "*" to "marginal†"; footnote updated to match Table 7's definition ("marginal† = primary two-tailed p at boundary of conventional significance; direction from tier-construction, not independent pre-registration").

**A/B-C15-MF3 (Methodologist + Benchmark Expert, concordant): §4.1 still reads "constituting a preliminary signal of calibration resolution failure" — the null observation calibration reframing applied in Cycle 14 was not extended to §4.1.**
Cycle 14 fixed calibration language in the Abstract, §6.3, §6.5, §7, and §9. §4.1 was missed. "Preliminary signal of calibration resolution failure" contradicts the null observation framing ("insufficient to confirm or rule out calibration resolution failure") now used in all other sections. The same issue exists in §3.1: "constitutes directional evidence rather than a statistical test of this condition" — the null observation is not directional evidence; it is within CI and indistinguishable from zero in either direction.
Fix applied: §4.1 changed to "a preliminary finding from Gemini 2.5 Flash that, at n=6 errors, constitutes a null pilot observation on confidence differentiation — insufficient to confirm or rule out calibration resolution failure — but one that, if confirmed at adequate scale across multiple models, would carry direct safety implications for AI coaching deployments (see §6.3)."
§3.1 changed: "constitutes directional evidence rather than a statistical test of this condition" → "constitutes a pilot observation insufficient to formally test this condition, reported in §6.3 with full evidential scope."

**B/C-C15-MF4 (Benchmark Expert + Skeptic, concordant): §6.5 "This convergence demonstrates that V1 Core performance reflects surface-vocabulary proficiency rather than genuine developmental reasoning capacity" — "demonstrates" draws a causal mechanism conclusion the data cannot support.**
§6.4 explicitly frames V2 data as an "informal observational record, not a formal evaluation... these observations are not cited as findings." Yet §6.5 uses "demonstrates" for a conclusion drawn from this uncitable data, alongside the informal V2 convergence. The data are consistent with the proficiency/capacity distinction but cannot demonstrate it without formal V2 evaluation and external tier validation.
Fix applied: changed to "This convergence is consistent with the hypothesis that V1 Core performance reflects surface-vocabulary proficiency rather than genuine developmental reasoning capacity — a hypothesis requiring formal V2 evaluation with per-scenario records and external tier validation to confirm. (V2 data cannot be cited as findings; see §6.4 disclaimer.)"

**B-C15-MF5 (Benchmark Expert): §6.3 states "MCIP − MCCIP ≈ 0.01" but the signed value is 0.93 − 0.94 = −0.01; the sign matters for interpretation.**
MCIP = 0.93 (mean confidence on incorrect predictions); MCCIP = 0.94 (mean confidence on correct predictions). MCIP − MCCIP = −0.01, not +0.01. The paper correctly reports Δ = 0.01 in the Abstract (absolute), but §6.3 writes the signed expression incorrectly. Notably, the signed direction (MCIP < MCCIP) is technically the ideal direction — the model shows marginally higher confidence on correct than incorrect predictions — though trivially and within CI. The framing should acknowledge this.
Fix applied: changed to "The absolute difference |MCIP − MCCIP| ≈ 0.01 (MCCIP = 0.94 slightly exceeds MCIP = 0.93 — technically the ideal direction for calibration, but the difference is within the bootstrap CI of ±0.08 on MCIP, making it indistinguishable from zero)."

**B-C15-MF6 (Benchmark Expert): No sensitivity analysis or text assurance that the hard-tier Fisher result holds on paraphrase_flag=0 items only.**
§5.1 discloses that the 12 hard-tier scenarios include approximately 3 paraphrase_flag=1 and ≤1 unknown. If LLM-paraphrased items carry inflated difficulty from paraphrase artefacts, the Fisher result could be partially paraphrase-driven. The paper currently provides adjudication-status stratification (§6.3) but not paraphrase-status stratification.
Fix applied: added note to §6.3 after the adjudication stratification paragraph: "A formal sensitivity analysis restricted to `paraphrase_flag=0` hard-tier scenarios only is deferred to the full dataset release evaluation, when per-scenario paraphrase records will be confirmed. The estimated 8 of 12 hard-tier scenarios that are original author-drafted (≈67%) suggests the Fisher result is not primarily driven by LLM-paraphrased items; the adjudication-status stratification above (non-adjudicated items: 37.5% error rate, above the 25% chance baseline) provides partial corroboration that the capability gap is not artefactual."

**C-C15-MF7 (Skeptic): §9 "These findings establish that frontier LLMs exhibit spiritual vocabulary fluency without developmental reasoning capacity" generalises from one model's formal result to the frontier class.**
The hard-tier formal result is from Gemini 2.5 Flash only. The V2 informal observation covers all five models but is explicitly non-citable. "Establish" + "frontier LLMs" (plural, general) is unsupported by the evidence available.
Fix applied: changed to "These results suggest that at least one evaluated frontier model (Gemini 2.5 Flash) exhibits spiritual vocabulary fluency without reliable developmental reasoning capacity at hard stage boundaries — with informal observations across five models consistent with a shared pattern that requires formal multi-model replication to confirm."

---

## SHOULD FIX Items (noted for camera-ready)

- A-C15-SF1: §6.3 one-tailed conditional clause "would apply if the tier-construction direction is accepted as a valid pre-specification" implicitly invites acceptance of an unjustified framing; consider striking the permissive conditional.
- A/B/C-C15-SF2: "developmental ceiling" in Abstract/body used as a coined term without a one-sentence definition at first use; define on first occurrence.
- B-C15-SF3: Bootstrap CI reported for MCIP (n=6, ±0.08) but not for MCCIP (n=25); asymmetry should be noted.
- C-C15-SF4: §6.5 "characteristic shape" implies replicability not supported by n=12 from one model; add "in the current sample."

---

## Cycle 16 Panel: Run 3 independent reviewers again
