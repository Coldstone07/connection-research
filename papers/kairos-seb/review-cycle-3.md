# Review Cycle 3 — Kairos-SEB (Adversarial)

**Date:** 2026-04-28
**Reviewer type:** Adversarial — full EMNLP main-track standards, no pilot accommodation
**Draft version:** stage-17/paper_draft.md (v2)
**Verdict:** **Reject** (for EMNLP main Resource/Dataset)

---

## MUST FIX Items (7 — each individually blocking)

**M1. Dataset not publicly available at review time.**
EMNLP Resource/Dataset requires the resource accessible to reviewers. `coldstone7/kairos-seb` is private. Cannot be reviewed without access.

**M2. Scale (43 scenarios, 1/4 tasks) below EMNLP main standard.**
EmoBench = 400. Paper's own §8 says "robust statistical analysis requires the planned 200+ scenario expansion" — self-certifying insufficiency for main track.

**M3. "Safety-critical" overconfidence claim based on n=6 errors, single model.**
"Safety-critical calibration failure" requires multi-model, multi-scenario evidence. Current evidence is 5–6 wrong answers from Gemini 2.5 Flash.

**M4. V2 (~50%) cited in Abstract/Conclusion without formal protocol.**
Informal observations without per-model breakdowns, CIs, or documented protocol cannot anchor the paper's central "developmental ceiling" claim.

**M5. T2–T4 (75% of DEVA) have zero empirical grounding.**
Proposing a 4-task benchmark and evaluating 1 task is a specification document, not a resource paper.

**M6. `GPT-5.4` and `Qwen3.6-plus` are unverifiable model identifiers.**
Do not match publicly documented OpenAI/Alibaba naming conventions as of Aug 2025. Experiments are irreproducible in principle.

**M7. No random baseline (25%) in any results table.**
Without chance-level reference, accuracy numbers are uninterpretable for 4-class classification.

---

## SHOULD FIX Items

**S1.** "First benchmark" claim lacks documented systematic literature search across CHI, CSCW, ACII, pastoral care AI venues.
**S2.** Scenario designer = annotator = difficulty calibrator = evaluator — conflict of interest not framed as a validity threat.
**S3.** Fowler/Peck four-stage fusion asserted without derivation; Fowler's contested cross-cultural validity not addressed.
**S4.** 1.71× difficulty gap is a calibration-circularity tautology — hard scenarios were defined by the same models that failed on them.

---

## Venue Recommendation

| Venue | What's needed |
|-------|--------------|
| EMNLP 2027 main Resource/Dataset | 200+ scenarios, T1+T2 evaluated, full-dataset kappa, dataset public, model IDs verified, V2 formalized |
| EMNLP/ACL Findings | 150+ scenarios, T1 fully evaluated all 5 models w/ CIs, T2 partial, kappa full-dataset, items 5–8 |
| **ACII 2027** | **Fix M3, M4 (partial), M6, M7; reposition as pilot evaluation framework — feasible at current scale** |
| Workshop (EVAL4NLP, NLP4PI) | Fix M6, M7, M3 only — minimum threshold |

---

## Minimum Viable Revision for ACII 2027 / Workshop

1. Public dataset release (or explicit pre-camera-ready commitment + reviewer access link)
2. Replace `GPT-5.4` / `Qwen3.6-plus` with verifiable API identifiers
3. Add random baseline (25%) to Tables 2 and 3
4. Remove "safety-critical" language; replace with "preliminary signal requiring multi-model replication"
5. Remove V2 from Abstract/Conclusion; relegate to §8/§9 Future Work
6. Reposition title/abstract to "framework and pilot evaluation" not "benchmark"
7. Soften "first benchmark" to "first pilot evaluation framework, to our knowledge in..."

---

## Revision Applied

Repositioning to **ACII 2027** (8-page full paper). ACII regularly publishes pilot affective computing benchmarks with small n; developmental framing is novel for that community.
