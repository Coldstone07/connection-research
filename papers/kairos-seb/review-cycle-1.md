# Review Cycle 1 — Kairos-SEB

**Date:** 2026-04-28
**Reviewer agent:** chi-paper-reviewer (EMNLP 2027 Resource/Dataset brief)
**Draft version:** stage-17/paper_draft.md (manual draft, v1)
**Verdict:** **Weak Accept**

---

## MUST FIX Items

**W1. V2 results are informal and cannot bear multi-model universality claim.**
- V2 (~45 scenarios) has no per-model breakdown, no CIs, no formal protocol description.
- The claim "~50% ceiling is not a model-specific limitation but a class-level limitation" requires per-model data.
- Fix: Rename §6.4 "Preliminary V2 Observation," remove multi-model universality claim, adjust Abstract.

**W2. T2–T4 have zero empirical validation despite anchoring 75% of DEVA.**
- Only SSR (T1) has been validated; ESR, DA, FPC have no empirical grounding.
- Fix: Reframe DEVA as "proposed multi-dimensional framework"; position T1/SSR as the validated component; T2–T4 as forward roadmap.

**W3. Annotation base is single-reviewer for non-ambiguous majority.**
- kappa=0.79 applies only to the ambiguous-scenario subset, not the full dataset.
- Fix: Add sentence clarifying kappa scope; prevent inference that 0.79 characterizes full benchmark.

**W4. 2026-dated citations unverifiable; model identifiers non-standard.**
- KardiaBench (Zhao et al., 2026), HumDial (Chen et al., 2026), Alla et al. (2026b) need status notes.
- claude-sonnet-4-6, claude-opus-4-6, GPT-5.4 are non-standard identifiers; reproducibility note needed.
- Fix: Add publication status footnotes; model version footnote.

## SHOULD FIX Items

**W5. FPC novelty claim may be overstated.**
- "Not present in any prior emotional AI benchmark" needs therapy/MI dialogue benchmark scan.
- Fix: Soften to "not present in the five benchmarks compared in Table 1."

**W6. Difficulty calibration circularity not acknowledged.**
- Models used to assign difficulty tiers overlap with models evaluated on benchmark.
- Fix: Add note in §5.3 and Limitations acknowledging circularity.

---

## Revision Plan

All MUST FIX and SHOULD FIX applied in v2 draft (stage-17/paper_draft.md).

Key changes made:
1. §6.4 renamed "Preliminary V2 Observation" — multi-model universality claim removed
2. Abstract adjusted to distinguish V1/Gemini evidence from V2 preliminary observation
3. §3.3 DEVA reframed as "proposed framework" with T1/SSR as validated component
4. §4.1 T2–T4 framing aligned — "planned future evaluation" made explicit upfront, not buried
5. §5.2 kappa scope clarified with explicit percentage
6. References: footnote on publication status; model ID footnote added
7. FPC claim softened to Table 1 benchmark scope
8. §5.3 and §8 acknowledge calibration circularity

---

## Word Count Delta
v1: ~5,800 words
v2: ~6,000 words (additions to Limitations, Abstract, §5.2, §5.3)
