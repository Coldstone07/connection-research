"""
Figure 2: The Mirror Problem vs. Design Response
Two-column comparison: engagement-optimised AI vs. autonomy-preserving design.
Each row is a design decision with opposite choices highlighted.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(12, 8.5))
ax.set_xlim(0, 12)
ax.set_ylim(0, 11)
ax.axis("off")

LEFT_COL  = 0.4
RIGHT_COL = 6.2
COL_W     = 5.5
HEADER_Y  = 10.3

RED   = "#C0392B"
GREEN = "#1A7A4A"
GRAY  = "#444444"
LIGHT_RED   = "#FCEAEA"
LIGHT_GREEN = "#EAF5EE"

rows = [
    {
        "dimension": "Training objective",
        "bad":  "Maximise engagement / thumbs-up signal",
        "good": "Maximise expressed internal authority",
    },
    {
        "dimension": "Response to distress",
        "bad":  "Validate immediately → relief on demand",
        "good": "Reflect and name → hold space for discomfort",
    },
    {
        "dimension": "Session closure",
        "bad":  "Keep conversation going; re-engage prompts",
        "good": "Synthesise; hand off to human peer or journaling",
    },
    {
        "dimension": "Outcome metric",
        "bad":  "Daily active users; session length; retention",
        "good": "Client-reported need for AI support over time (↓)",
    },
    {
        "dimension": "Exit strategy",
        "bad":  "None — system is designed to be irreplaceable",
        "good": "Peer coherence architecture scaffolds AI exit",
    },
    {
        "dimension": "Mirror artifact",
        "bad":  "Sycophantic summary: confirms user's framing",
        "good": "CCM: surfaces patterns and open questions",
    },
    {
        "dimension": "Design intent",
        "bad":  "Be the safest, most available confidant",
        "good": "Build capacity to find that human in real life",
    },
]

ROW_H = 1.0
START_Y = 9.2

# Column headers
for x, label, color in [
    (LEFT_COL  + COL_W / 2, "Engagement-Optimised AI\n(The Nodding Mirror)", RED),
    (RIGHT_COL + COL_W / 2, "Autonomy-Preserving Design\n(This Paper's Response)", GREEN),
]:
    box = FancyBboxPatch(
        (x - COL_W / 2, HEADER_Y - 0.55), COL_W, 0.95,
        boxstyle="round,pad=0.1",
        facecolor=color, edgecolor="none", zorder=2
    )
    ax.add_patch(box)
    ax.text(x, HEADER_Y - 0.07, label,
            ha="center", va="center",
            fontsize=11, fontweight="bold", color="white",
            linespacing=1.4, zorder=3)

# Dimension label column header
ax.text(
    (LEFT_COL + RIGHT_COL) / 2 - 0.1, HEADER_Y - 0.07,
    "Design\nDimension",
    ha="center", va="center",
    fontsize=9, fontweight="bold", color=GRAY,
)

# Rows
for i, row in enumerate(rows):
    y = START_Y - i * ROW_H
    shade = "#F9F9F9" if i % 2 == 0 else "white"

    # Row background
    ax.add_patch(FancyBboxPatch(
        (0.1, y - ROW_H + 0.1), 11.8, ROW_H - 0.1,
        boxstyle="round,pad=0.05",
        facecolor=shade, edgecolor="#EEEEEE", linewidth=0.5
    ))

    mid_y = y - ROW_H / 2 + 0.05

    # Dimension
    ax.text(
        (LEFT_COL + RIGHT_COL) / 2 - 0.1, mid_y,
        row["dimension"],
        ha="center", va="center",
        fontsize=9, fontstyle="italic", color=GRAY,
        wrap=True,
    )

    # Bad (left)
    ax.add_patch(FancyBboxPatch(
        (LEFT_COL, y - ROW_H + 0.18), COL_W, ROW_H - 0.28,
        boxstyle="round,pad=0.07",
        facecolor=LIGHT_RED, edgecolor=RED, linewidth=0.8
    ))
    ax.text(
        LEFT_COL + COL_W / 2, mid_y,
        row["bad"],
        ha="center", va="center",
        fontsize=9, color=RED,
        wrap=True,
    )

    # Good (right)
    ax.add_patch(FancyBboxPatch(
        (RIGHT_COL, y - ROW_H + 0.18), COL_W, ROW_H - 0.28,
        boxstyle="round,pad=0.07",
        facecolor=LIGHT_GREEN, edgecolor=GREEN, linewidth=0.8
    ))
    ax.text(
        RIGHT_COL + COL_W / 2, mid_y,
        row["good"],
        ha="center", va="center",
        fontsize=9, color=GREEN,
        wrap=True,
    )

# Title
ax.text(
    6.0, 10.82,
    "Figure 2. The Mirror Problem and the Design Response",
    ha="center", va="center",
    fontsize=13, fontweight="bold", color=GRAY,
)
ax.text(
    6.0, 10.58,
    "Seven design dimensions contrasting engagement-optimised AI with autonomy-preserving design",
    ha="center", va="center",
    fontsize=9, color="#777777",
)

plt.tight_layout(pad=0.1)
plt.savefig(
    "/Users/jatinalla/Desktop/AutoResearchClaw/artifacts/chi-paper/figures/fig2_mirror_problem.png",
    dpi=300, bbox_inches="tight", facecolor="white"
)
plt.close()
print("fig2 saved")
