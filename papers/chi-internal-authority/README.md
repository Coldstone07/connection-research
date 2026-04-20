# Designing for Internal Authority

**Full title:** Designing for Internal Authority: AI Coaching Systems as a Counter to the Nodding Mirror  
**Authors:** Jatin Alla  
**Target venue:** ACM CHI 2027 (Human Factors in Computing Systems)  
**Status:** Pre-submission draft — ethics review and participant consent in progress

## Files

| File | Description |
|------|-------------|
| `paper.md` | Full paper (Markdown, working draft) |
| `paper.tex` | LaTeX source (ACM sigchi format) |
| `bib/references_merged.bib` | 29 BibTeX entries |
| `figures/` | All 4 figures (300 DPI PNG + Python source) |

## Figures

- `fig1_system_architecture` — Five-layer system stack
- `fig2_mirror_problem` — Design comparison: engagement-optimised vs. authority-building
- `fig3_self_energy_progression` — Self-energy progression across Spring 2026 cohort (N=18)
- `fig4_peer_coherence` — Peer coherence transition arc

## Building the PDF

Requires a LaTeX installation (e.g. `brew install --cask mactex` or upload to Overleaf):

```bash
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

## Pre-submission note

The submitted version will include an institutional ethics reference number and confirmation that retroactive research consent was obtained from all Spring 2026 cohort participants. The paper will not be formally submitted to CHI while either process remains incomplete.
