# Review Cycle 17 — Kairos-SEB (3-Reviewer Panel, ACII 2027)

**Date:** 2026-04-29
**Reviewer structure:** 3 independent parallel reviewers (Methodologist, Benchmark Expert, Skeptic)
**Draft version:** stage-17/paper_draft.md (post-Cycle-16 fixes + 2 pre-panel grounding corrections)
**Panel verdict:** A — Weak Accept; B — Weak Reject; C — Weak Accept

---

## Panel Findings Summary

| Reviewer | Verdict | MUST FIX |
|----------|---------|----------|
| A — Methodologist | Weak Accept | 2: one-tailed p should be removed from all sections (concordant C); bootstrap CI on n=6 invalid |
| B — Benchmark Expert | Weak Reject | 3: Fisher result unaffected by calibration circularity not explicitly stated; "consistent with statistically significant" is false at p=0.053; §6.5 surface-proficiency hypothesis still anchored on V2 data |
| C — Skeptic | Weak Accept | 2: one-tailed p justification circular — remove or add non-endorsement (concordant A); §9 drops "preliminary"/"requires external tier validation" qualifiers from capability inference |

---

## Cycle 16 Resolution Scorecard

| Item | Status |
|------|--------|
| A/B/C-C16-MF1 (one-tailed p removed from Abstract and §9) | FULLY RESOLVED |
| C-C16-MF2 ("genuine" → "observed") | FULLY RESOLVED |
| A-C16-MF3 (bootstrap CI limited reliability caveat) | PARTIALLY RESOLVED → A judges caveat insufficient; full removal required |
| B-C16-MF4 (GPT-5.4 calibration circularity in Table 2) | FULLY RESOLVED |

---

## Pre-Panel Grounding Corrections (applied before panel)

- §6.3 confusion matrix: narrative covered only 4 of 6 errors; added explicit statement that remaining 2 (S2, S3 single errors) are in the evaluation log but don't exhibit the outer-stage pattern
- §6.4: Sonnet 100% cited as data point without paraphrase-circularity caveat; added "withheld as independent benchmark measure due to paraphrase circularity; see §6.2"

---

## 6 MUST FIX Items — All Applied

**A/C-C17-MF1 (concordant Methodologist + Skeptic): One-tailed p = 0.037 must be removed from §4.2 and Table 4; the paper's own logic disqualifies it from carrying inferential weight anywhere outside the full methodological discussion in §6.3 body text.**
The paper states "the directional prediction follows from the benchmark's own tier-label construction rather than from an independent prospective pre-registration, which limits the grounds for a one-tailed test." If the paper disavows the test, reporting it "for reference" in §4.2 and Table 4 allows selective citation — readers who want to claim p = 0.037 "significant" will simply assert the direction was pre-specified. The one-tailed value is retained in §6.3 body text only, where it is accompanied by an explicit non-endorsement statement. The abstract cross-reference is simplified from "including one-tailed p" to "full statistical discussion."
Fix applied: Removed one-tailed p from §4.2. Table 4 restructured to show only two-tailed p with single Significance column. §6.3 body text retains both values but adds: "The authors do not endorse citation of the one-tailed p = 0.037 as a 'significant' result; the operative inferential value is the two-tailed p ≈ 0.053." Abstract cross-reference simplified.

**A-C17-MF2 (Methodologist): Bootstrap CI ±0.08 on n=6 carries no meaningful coverage guarantee and must be removed.**
A bootstrap CI derived from 6 observations has no reliable coverage properties regardless of whether the underlying values are binary or continuous. Reporting "±0.08" implies calibrated precision that the procedure cannot deliver at n=6. The null observation argument does not require a CI — it rests on n=6 being too small to draw conclusions, which is self-evident. The CI is removed; text is replaced with a direct statement that n=6 is insufficient for any interval estimate.
Fix applied: All occurrences of "bootstrap CI of ±0.08" and "order-of-magnitude bound only" replaced with: "n=6 is insufficient for a meaningful interval estimate; the observed |Δ| ≈ 0.01 is a purely descriptive value." Abstract updated: "(Δ = 0.01; n=6 errors from one model — insufficient for any interval estimate)."

**B-C17-MF3 (Benchmark Expert): "The 41.7 percentage-point medium-to-hard gap is consistent with a statistically significant difficulty effect" is false — p ≈ 0.053 does not reach α = 0.05.**
"Consistent with a statistically significant effect" reads as claiming the data support significance, but the primary test does not clear the conventional threshold. The honest statement is: the test does not reach conventional significance, the effect size is large, and the direction is theoretically predicted.
Fix applied: Changed to "The 41.7 percentage-point medium-to-hard gap does not reach conventional statistical significance under the primary two-tailed test (Fisher's exact, p ≈ 0.053; α = 0.05 threshold not met). The effect size is large and the direction is theoretically predicted by the tier-construction design, but the result should be treated as a directional pilot finding pending replication with a larger sample."

**B-C17-MF4 (Benchmark Expert): The primary Fisher result is entirely unaffected by calibration circularity — this is not stated explicitly enough and leaves the reader uncertain.**
The paper says calibration circularity "affects the interpretation of these two models' difficulty-tier performance specifically" and that "the Gemini 2.5 Flash difficulty-gap finding (§6.3) is not affected, as Gemini was not a calibration participant" — but this appears only in §8. Readers of §6.3 who are aware of the §5.3 calibration disclosure need reassurance at the point of the primary result.
Fix applied: Added sentence to §6.3 opening: "Note: the V1 Extended analysis uses only Gemini 2.5 Flash, which was not a participant in the difficulty calibration procedure (§5.3); the primary Fisher result is therefore entirely unaffected by calibration circularity."

**B-C17-MF5 (Benchmark Expert): §6.5 surface-proficiency hypothesis is anchored on "this convergence" — meaning the V2 informal data — despite V2 being disclaimed as non-citable.**
The V2 data cannot anchor an interpretive hypothesis. However, the surface-proficiency hypothesis is independently grounded in V1 Extended: the medium-to-hard accuracy collapse and the outer-stage confusion pattern (Stage 4 misclassified as Stage 2 due to overlapping surface vocabulary) directly support it without requiring V2. The fix re-anchors the hypothesis on V1 Extended evidence only; V2 is retained as supplementary directional context but explicitly cannot serve as supporting evidence.
Fix applied: Revised §6.5 paragraph to: "The V1 Extended hard-tier performance collapse — and specifically the outer-stage confusion pattern in which Stage 4 utterances are misclassified as Stage 2 due to overlapping acceptance vocabulary (§6.3) — is consistent with the hypothesis that stage detection at medium difficulty relies on surface vocabulary markers while hard-tier performance requires structural developmental reasoning that the model cannot reliably perform. If confirmed by external tier validation, this would suggest that medium-tier performance reflects surface-vocabulary proficiency rather than genuine developmental reasoning capacity. The informal V2 convergence (§6.4) provides additional directional context for this hypothesis but cannot serve as supporting evidence." The prior sentence beginning "This convergence is consistent with the hypothesis that V1 Core performance..." is removed.

**C-C17-MF6 (Skeptic): §9 Conclusion drops "preliminary" and "requires external tier validation" qualifiers from the capability inference, making it stronger than §6.3 warrants.**
§6.3 frames the capability inference as "a reasonable but preliminary extension that requires external tier validation to confirm." §9 states "these results suggest that at least one evaluated frontier model exhibits spiritual vocabulary fluency without reliable developmental reasoning capacity" without these qualifiers, upgrading a preliminary inference to an apparent finding.
Fix applied: §9 changed to "These results are consistent with the preliminary hypothesis that at least one evaluated frontier model (Gemini 2.5 Flash) may exhibit spiritual vocabulary fluency without reliable developmental reasoning capacity at hard stage boundaries — an inference that requires external tier validation to confirm — with informal observations across five models consistent with a shared pattern that requires formal multi-model replication."

---

## SHOULD FIX Items (noted for camera-ready)

- B/C-C17-SF1: "Developmental ceiling" label (all five models) overstates multi-model evidence; consider "difficulty-stratification effect" as primary label
- A-C17-SF2: Redundant hedging — "at the boundary of conventional significance" repeated verbatim 5+ times; consolidate to §6.3 and use forward-references elsewhere
- C-C17-SF3: MCIP/MCCIP null result headline placement in Abstract — consider moving to limitations or framing as motivating observation only
- B-C17-SF4: Sonnet 100% withheld from Table 2 but mentioned in §6.4 — either add to Table 2 with double-flag (paraphrase + calibration circularity) or remove from §6.4

---

## Cycle 18 Panel: Run 3 independent reviewers again
