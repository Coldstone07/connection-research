# Review Cycle 11 — Kairos-SEB (3-Reviewer Panel, ACII 2027)

**Date:** 2026-04-28
**Reviewer structure:** 3 independent parallel reviewers (Methodologist, Benchmark Expert, Skeptic)
**Draft version:** stage-17/paper_draft.md (post-Cycle-10 fixes applied)
**Panel verdict:** All 3 — **Weak Accept** (MUST FIX items present)

---

## Panel Findings Summary

| Reviewer | Verdict | MUST FIX |
|----------|---------|----------|
| A — Methodologist | Weak Accept | 1: adjudicated item count and tier distribution absent from §5.2 and §8 Limitation 2 |
| B — Benchmark Expert | Weak Accept | 2: abstract Fisher attribution not qualified with construct-validity reading; `paraphrase_flag` dataset card commitment absent |
| C — Skeptic | Weak Accept | 2: abstract one-tailed p lacks "direction design-determined" qualifier; §8 Limitation 2 presents 0.81 without not-comparable disclaimer |

---

## Cycle 10 Resolution Scorecard

| Item | Status |
|------|--------|
| A-C10-MF1 = B-MF11 (Table 7 "(\*)†" undefined notation) | FULLY RESOLVED |
| B-MF10 (abstract lacks boundary-significance qualifier) | FULLY RESOLVED |
| C10-MF1 (Fisher result framing: construct validity vs. capability) | FULLY RESOLVED |
| C10-MF2 (MCCIP ≈ 0.94 not ≈ 0.93 in abstract/§9) | FULLY RESOLVED |
| C10-MF3 (Benner/Hagberg attribution overstatement) | FULLY RESOLVED |

---

## 5 New MUST FIX Items — All Applied

**A-C11-MF1 (Methodologist): §5.2 and §8 Limitation 2 never report how many of the 43 scenarios received the `adjudicated` flag, nor whether adjudicated items are concentrated in the hard tier.**
The adjudication procedure is now fully specified (Cycle 9 fix), and the `adjudicated` flag is committed to the dataset release — but the count is absent from both the method section and the limitations. Without the count and tier distribution, a reader cannot assess how much of the hard-tier Fisher result is confounded by below-threshold-reliability labels.
Fix applied: §5.2 now states "Of the 43 released scenarios, 7 received the `adjudicated` flag: 4 from V1 Extended hard tier, 2 from V1 Extended medium tier, and 1 from V1 Core — a concentration in the hard tier consistent with the theoretical prediction that Stage 1/Stage 4 and Stage 2/Stage 3 boundary scenarios pose the greatest annotator difficulty." §8 Limitation 2 updated to include the same count and explicitly flag that 4 of 12 hard-tier scenarios are adjudicated — making the annotation-reliability confound on the Fisher result visible.

**B-MF12 (Benchmark Expert): Abstract attributes Fisher's exact test to the developmental ceiling (capability reading) without the construct-validity qualifier now present in §9.**
Post-Cycle-10, §9 correctly states the Fisher result "primarily validating that the difficulty-tier stratification captures a genuine performance gradient." The abstract still presented the test as evidence for the capability claim without this qualification, creating an inconsistency between the abstract and the body.
Fix applied: Abstract Fisher parenthetical expanded to: "(two-tailed p ≈ 0.053, at the boundary of conventional significance; one-tailed p = 0.037, direction design-determined — see §6.3), primarily validating that the difficulty-tier stratification captures a genuine performance gradient (secondary reading: a frontier model capability gap at hard developmental stage boundaries)."

**B-MF13 (Benchmark Expert): Paper commits to a versioned public dataset release but the dataset card cannot satisfy the provenance commitment without a `paraphrase_flag` field.**
The paper discloses that per-scenario paraphrase provenance records were not maintained and marks this as a limitation. But the camera-ready dataset release is imminent, and no mechanism exists in the dataset card to convey per-scenario provenance to downstream users — creating a gap between the paper's epistemic disclosure and what users of the released dataset can actually verify.
Fix applied: §5.1 now includes: "the HuggingFace dataset card (coldstone7/kairos-seb) will include a `paraphrase_flag` field at camera-ready: scenarios with confirmed or probable LLM-paraphrase involvement will be marked `paraphrase_flag=1`; original author-drafted scenarios will be marked `paraphrase_flag=0`; scenarios where provenance could not be reconstructed will be marked `paraphrase_flag=unknown`. This flag will allow downstream users to restrict evaluation to provenance-confirmed original scenarios for independent replication."

**C11-MF1 (Skeptic): Abstract one-tailed p = 0.037 uses "under the directional assumption from tier construction" — ambiguous phrasing that does not make explicit that the direction follows from the benchmark's own design rather than from an independent pre-registration.**
The full disambiguation ("follows from the benchmark's own tier-label construction rather than from an independent prospective pre-registration") is in §6.3 but absent from the abstract. A reader of the abstract alone cannot determine the inferential status without following the §6.3 cross-reference.
Fix applied: Abstract now reads "one-tailed p = 0.037, direction design-determined — see §6.3" replacing the prior "under the directional assumption from tier construction."

**C11-MF2 (Skeptic): §8 Limitation 2 presents "κ = 0.72 below threshold; post-consensus 0.81" without the not-comparable disclaimer co-located with the 0.81 figure, implying the missed threshold is addressed by the post-consensus rise.**
The disclaimer that post-consensus 0.81 is not a Cohen's κ estimate exists in §5.2, but §8 Limitation 2 still wrote "Post-adjudication agreement rises to κ = 0.81" — reintroducing the κ symbol and omitting the disclaimer, creating the false impression that the 0.81 resolves the 0.72 threshold miss.
Fix applied: §8 Limitation 2 now reads "Post-adjudication agreement rises to 0.81 (not directly comparable to κ thresholds — this figure reflects convergence under structured three-party discussion, not independent re-annotation; see §5.2)" — removing the κ symbol and co-locating the disclaimer.

---

## Cycle 12 Panel: Run 3 independent reviewers again
