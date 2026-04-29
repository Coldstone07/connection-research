# Review Cycle 12 — Kairos-SEB (3-Reviewer Panel, ACII 2027)

**Date:** 2026-04-28
**Reviewer structure:** 3 independent parallel reviewers (Methodologist, Benchmark Expert, Skeptic)
**Draft version:** stage-17/paper_draft.md (post-Cycle-11 fixes applied)
**Panel verdict:** All 3 — **Weak Accept** (MUST FIX items present)

---

## Panel Findings Summary

| Reviewer | Verdict | MUST FIX |
|----------|---------|----------|
| A — Methodologist | Weak Accept | 3: adjudicated-item accuracy stratification in hard tier; Fisher independence verification; MCIP precision + §3.1 formal notation |
| B — Benchmark Expert | Weak Accept | 1: abstract "reveals" (escalated from 4-cycle SHOULD FIX) |
| C — Skeptic | Weak Accept | 2: abstract one-tailed p "not independently pre-registered" absent; §8 κ disclaimer placement |

---

## Cycle 11 Resolution Scorecard

| Item | Status |
|------|--------|
| A-C11-MF1 (adjudicated item count and tier distribution in §5.2/§8) | FULLY RESOLVED |
| B-MF12 (abstract Fisher construct-validity qualifier) | FULLY RESOLVED |
| B-MF13 (paraphrase_flag dataset card commitment) | FULLY RESOLVED |
| C11-MF1 (abstract one-tailed p "direction design-determined") | PARTIALLY RESOLVED → escalated to C12-MF1 |
| C11-MF2 (§8 κ disclaimer placement) | PARTIALLY RESOLVED → escalated to C12-MF2 |

---

## 6 New MUST FIX Items — All Applied

**A-C12-MF1 (Methodologist): Hard-tier accuracy is stratified by adjudication status only in §8 (disclosure) but not in §6.3 (results), leaving the primary statistical claim's robustness unquantified.**
4 of 12 hard-tier scenarios carry the `adjudicated` flag. The Fisher test's construct-validity interpretation — that tier stratification works as intended — rests on hard-tier labels 33% of which were established by three-party adjudication rather than independent dual-annotator agreement. Without accuracy stratification by adjudication status, a reader cannot evaluate whether the 5 hard-tier errors are concentrated in annotation-contested items or occur across both subgroups.
Fix applied: §6.3 now includes a paragraph reporting: adjudicated hard-tier items (n=4): 2/4 correct (50%); non-adjudicated hard-tier items (n=8): 5/8 correct (62.5%). Text states that error rate on non-adjudicated items (37.5%) is substantially above chance (25%), confirming the capability gap is not artefactually produced by contested labels. Modestly higher error rate on adjudicated items (50%) consistent with Stage 1/Stage 4 boundary being genuinely the hardest developmental reasoning target.

**A-C12-MF2 (Methodologist): §6.1 never confirms that each V1 Extended scenario was an independent zero-context API call — the Fisher test independence assumption is unverified in the text.**
Fisher's exact test assumes independence of observations. Scenarios could have been batched or presented in sequence, in which case within-session context would violate the independence assumption. The paper did not address this.
Fix applied: §6.1 now states "Each of the 31 V1 Extended scenarios was presented as an independent, zero-context API call with no preceding scenario content — ensuring the independence of observations required by Fisher's exact test."

**A-C12-MF3 (Methodologist): §3.1 formal notation $\mathbb{E}[c \mid \hat{s} \neq s] \ll \mathbb{E}[c \mid \hat{s} = s]$ framed as a testable model criterion, but n=6 cannot formally test any $\ll$ relationship; and raw MCIP/MCCIP values at three decimal places overstate precision.**
The formal notation implies a testable criterion; the n=6 pilot cannot test it. Raw values 0.932/0.941 at three decimal places are inappropriate when the SE of a mean over 6 items is ±0.05–0.10.
Fix applied: §3.1 notation revised to "A model achieves ideal stage calibration when $\mathbb{E}[c \mid \hat{s} \neq s] \ll \mathbb{E}[c \mid \hat{s} = s]$; this is a design target... the pilot observation reported in §6.3 constitutes directional evidence rather than a statistical test." §6.3 raw values changed from 0.932/0.941 to "0.93/0.94" with added parenthetical "approximate 95% bootstrap CI for MCIP over n=6: ±0.08." Table 5 footnote updated to match.

**B-C12-MF1 (Benchmark Expert, escalated from 4-cycle SHOULD FIX): Abstract "Empirical evaluation reveals" — assertive discovery register inconsistent with "framework proposal and pilot evaluation" framing.**
"Reveals" was flagged as a framing-inconsistency in Cycles 8–11. It was deferred each cycle. Per protocol, four-cycle SHOULD FIX items escalate to MUST FIX at Cycle 12.
Fix applied: "reveals" → "identifies" in abstract opening sentence.

**C12-MF1 (Skeptic): Abstract one-tailed p qualifier "direction design-determined" doesn't foreclose unconditional significance reading.**
"Direction design-determined" is ambiguous — it can be read as "predicted by the design" (compatible with independent pre-registration) rather than "entailed by the design's own tier-label construction without independent pre-registration." The operative epistemic constraint (not independently pre-registered) is in §6.3 but not in the abstract parenthetical.
Fix applied: Abstract now reads "one-tailed $p = 0.037$, direction design-determined and not independently pre-registered — see §6.3."

**C12-MF2 (Skeptic): §8 Limitation 2 κ disclaimer appears after both numbers, allowing readers to form the inference "κ rose from 0.72 to 0.81, resolving the threshold miss" before encountering the caveat.**
Two-number-then-caveat structure in a Limitations section read quickly means the caveat arrives after the inference is already formed. Fix requires integrating the disclaimer into the 0.81 sentence.
Fix applied: §8 Limitation 2 restructured: "Following adjudication, post-consensus agreement rose to 0.81 — a figure that is not a Cohen's κ estimate and must not be compared against κ threshold scales, as it reflects convergence under structured three-party discussion rather than independent re-annotation (see §5.2 for the distinction). The initial κ of 0.72 remains the benchmark's inter-rater reliability estimate; the 0.81 post-consensus rate does not resolve the 0.72 threshold-miss."

---

## Cycle 13 Panel: Run 3 independent reviewers again
