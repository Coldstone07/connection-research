# Review Cycle 16 — Kairos-SEB (3-Reviewer Panel, ACII 2027)

**Date:** 2026-04-29
**Reviewer structure:** 3 independent parallel reviewers (Methodologist, Benchmark Expert, Skeptic)
**Draft version:** stage-17/paper_draft.md (post-Cycle-15 fixes applied + 4 pre-panel corrections)
**Panel verdict:** A — Weak Accept; B — Weak Reject; C — Weak Accept

---

## Panel Findings Summary

| Reviewer | Verdict | MUST FIX |
|----------|---------|----------|
| A — Methodologist | Weak Accept | 2: one-tailed p repeated throughout (concordant B+C); n=6 bootstrap CI statistically unreliable |
| B — Benchmark Expert | Weak Reject | 2: one-tailed p in Abstract without pre-registration (concordant A+C); GPT-5.4 calibration circularity not strongly enough remediated in §6.2 |
| C — Skeptic | Weak Accept | 2: one-tailed p in Abstract and §9 (concordant A+B); "genuine performance gradient" / "genuine capability boundary" overclaim |

---

## Cycle 15 Resolution Scorecard

| Item | Status |
|------|--------|
| A/B/C-C15-MF1 (§4.2 Fisher overclaim "confirms as statistically significant") | FULLY RESOLVED |
| A-C15-MF2 (Table 4 vs Table 7 inconsistency) | FULLY RESOLVED |
| A/B-C15-MF3 (§4.1 calibration "preliminary signal") | FULLY RESOLVED |
| B/C-C15-MF4 (§6.5 "demonstrates") | FULLY RESOLVED |
| B-C15-MF5 (MCIP sign error) | FULLY RESOLVED |
| B-C15-MF6 (paraphrase sensitivity note) | FULLY RESOLVED |
| C-C15-MF7 (§9 "establish that frontier LLMs") | FULLY RESOLVED |

---

## Pre-Panel Corrections (identified before panel run)

- §6.3 opening: "statistically significant performance collapse" → "performance collapse (primary two-tailed p ≈ 0.053 — see statistical discussion below)"
- Figure 1 caption: "benchmark-validated across the frontier model generation" → "formally measured for Gemini; informally observed across all five models — requiring formal multi-model replication"
- §3.1: "Preliminary results from Gemini 2.5 Flash suggest that frontier models may fail to suppress confidence" → null pilot observation framing; removed "frontier models" generalisation
- §6.5 end: "statistically significant Gemini medium-versus-hard contrast (p = 0.037)" → "two-tailed p ≈ 0.053, at the boundary; one-tailed p = 0.037"

---

## 4 MUST FIX Items — All Applied

**A/B/C-C16-MF1 (3-way concordant): One-tailed p = 0.037 appears in the Abstract and §9 Conclusion — the two highest-visibility locations — without sufficient protection against selective reading.**
The Abstract presents "one-tailed p = 0.037, direction design-determined and not independently pre-registered" as if the reader will follow the caveat. In practice, reviewers and practitioners read p = 0.037 and see a significant result. The one-tailed value does not satisfy pre-registration requirements for confirmatory use; the paper itself says so. The two-tailed primary result (p ≈ 0.053) does not clear α = 0.05. Keeping the one-tailed value in high-visibility locations undermines the paper's own discipline. §6.3 with its full methodological argument is the appropriate home for both values.
Fix applied: Abstract — removed one-tailed p; retained two-tailed with cross-reference "see §6.3 for full statistical discussion including one-tailed p." §9 — same treatment. §6.3, §4.2, Table 4 retain both values with full contextualisation.

**C-C16-MF2 (Skeptic, concordant with A concern): "captures a genuine performance gradient" (Abstract) and "produces a genuine capability boundary" (§6.5) assert confirmed construct validity when the primary test is at the boundary of significance and no external tier validation has been conducted.**
"Genuine" does active epistemic work: it converts a directional marginal result into a confirmed structural property. Given p ≈ 0.053 (primary) and no independent external tier validation, "genuine" overstates the evidence. The appropriate framing is that the data are consistent with a performance gradient, not that the gradient has been confirmed as genuine.
Fix applied: "genuine performance gradient" → "observed performance gradient" in Abstract and §9. "genuine capability boundary" → "observed capability gap" in §6.5.

**A-C16-MF3 (Methodologist): "approximate 95% bootstrap CI for MCIP over n=6: ±0.08" lends false precision at n=6.**
With n=6 continuous confidence values, the bootstrap distribution has limited reliability regardless of whether the data are binary or continuous. The ±0.08 figure appears precise enough to draw meaningful interpretive conclusions (the paper uses it to say the Δ=0.01 difference is "within CI"), but at n=6 the CI width is dominated by the small sample and should be treated as an order-of-magnitude bound rather than a calibrated interval. The paper already hedges with "approximate" but does not explicitly flag the reliability limitation.
Fix applied: changed to "approximate 95% bootstrap CI for MCIP over n=6: ±0.08 (note: this CI has limited reliability at n=6 and should be treated as an order-of-magnitude bound only; it is reported solely to confirm the trivial magnitude of the observed difference)."

**B-C16-MF4 (Benchmark Expert): §6.2 reports GPT-5.4's 91.7% V1 Core result without in-paragraph disclosure that this result is subject to calibration circularity and should not be treated as independent.**
The paper discloses calibration circularity in §5.3 and §8, with a cross-reference in §6.1. However, §6.2 — where the primary per-model accuracy numbers appear — presents GPT-5.4's 91.7% alongside Qwen3-Plus's 91.7% without flagging that GPT-5.4's result is confounded while Qwen3-Plus's is not. A reader who focuses on Table 2 without cross-referencing §6.1 or §8 would incorrectly treat both results as equally independent. The fix does not require new analysis — it requires in-table and in-paragraph clarity.
Fix applied: Table 2 footnote updated to explicitly flag "GPT-5.4 is subject to calibration circularity (§5.3, §8) — its V1 Core accuracy is disclosed for completeness but should not be interpreted as an independent evaluation result; only Qwen3-Plus and Claude Opus 4.6 provide fully unconfounded V1 Core baselines." §6.2 text updated accordingly.

---

## SHOULD FIX Items (noted for camera-ready)

- A/C-C16-SF1: "Developmental ceiling" label applied to all five models in §6.5 while multi-model data is informal; restrict or qualify.
- A-C16-SF2: Null calibration observation cited in §3.1, §4.1, §4.2, §6.3, §6.5, §7, §9 — creates impression of accumulated evidence; consolidate and replace non-§6.3 instances with single forward-reference.
- B-C16-SF3: V2 disclaimer in §6.5 appears after the sentence it qualifies; move to paragraph opening.
- B-C16-SF4: Adjudicated-item n=4 subgroup — describe as purely descriptive, no significance language.
- C-C16-SF5: §7 null calibration framing "motivates formal replication" should explicitly state n=6 licenses no inference, positive or null.

---

## Cycle 17 Panel: Run 3 independent reviewers again
