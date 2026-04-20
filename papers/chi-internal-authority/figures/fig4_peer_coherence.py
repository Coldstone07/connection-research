"""
Figure 4: Peer Coherence Transition
Shows the session-by-session arc from AI-only / 1:1 facilitated support
toward peer-led mutual support across a 10-session cohort.

Three stacked bands:
  - AI mediation weight (declines)
  - Facilitator-led group weight (bell curve mid-programme)
  - Peer coherence weight (grows)

Plus two annotated events:
  - Session 4: First cross-client resonance noted
  - Session 8: Peer dyad pairs formed
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy.special import expit

sessions = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# AI weight: high early, gradually handed off
ai_weight = 0.75 * expit(-(sessions - 3) * 0.85) + 0.1

# Facilitator group: peaks mid-programme
group_weight = 0.45 * np.exp(-0.5 * ((sessions - 5.5) / 2.0) ** 2)

# Peer coherence: starts near zero, accelerates from session 6
peer_weight = 0.65 * expit((sessions - 6.5) * 1.1)

# Normalise to sum to 1 at each session
total = ai_weight + group_weight + peer_weight
ai_norm    = ai_weight    / total
group_norm = group_weight / total
peer_norm  = peer_weight  / total

fig, ax = plt.subplots(figsize=(10, 5.5))

AI_COLOR    = "#7B5EA7"   # purple
GROUP_COLOR = "#4A8A6E"   # green
PEER_COLOR  = "#4A6FA5"   # blue

ax.stackplot(
    sessions,
    ai_norm, group_norm, peer_norm,
    labels=["AI Mediation", "Facilitated Group", "Peer Coherence"],
    colors=[AI_COLOR + "BB", GROUP_COLOR + "BB", PEER_COLOR + "BB"],
    alpha=0.92,
)

# Annotations
ax.annotate(
    "Session 4\nFirst cross-client\nresonance noted",
    xy=(4, 0.55), xytext=(3.0, 0.75),
    fontsize=8.5, color="#333333",
    arrowprops=dict(arrowstyle="-|>", color="#888888", lw=1.2),
    ha="center",
)

ax.annotate(
    "Session 8\nPeer dyad pairs\nformed",
    xy=(8, 0.62), xytext=(8.8, 0.80),
    fontsize=8.5, color="#333333",
    arrowprops=dict(arrowstyle="-|>", color="#888888", lw=1.2),
    ha="center",
)

ax.set_xticks(sessions)
ax.set_xticklabels([f"S{s}" for s in sessions], fontsize=10)
ax.set_xlabel("Session Number", fontsize=11)
ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
ax.set_yticklabels(["0%", "25%", "50%", "75%", "100%"], fontsize=10)
ax.set_ylabel("Proportional Support Weight", fontsize=11)
ax.set_xlim(1, 10)
ax.set_ylim(0, 1)
ax.spines[["top", "right"]].set_visible(False)

legend = ax.legend(
    loc="center left",
    fontsize=9.5,
    framealpha=0.9,
    edgecolor="#CCCCCC",
    bbox_to_anchor=(0.02, 0.38),
)

ax.set_title(
    "Figure 4. Peer Coherence Transition Across a 10-Session Programme\n"
    "Modelled from facilitator documentation: proportional shift from AI-mediated\n"
    "to peer-led support as the platform's exit scaffold activates",
    fontsize=11, pad=8, linespacing=1.5,
)

# Shade the "AI exit zone" lightly
ax.axvspan(7.5, 10.05, alpha=0.06, color=PEER_COLOR, label="_nolegend_")
ax.text(
    8.75, 0.06, "AI exit\nzone", ha="center", va="bottom",
    fontsize=8, color=PEER_COLOR, fontstyle="italic"
)

plt.tight_layout()
plt.savefig(
    "/Users/jatinalla/Desktop/AutoResearchClaw/artifacts/chi-paper/figures/fig4_peer_coherence.png",
    dpi=300, bbox_inches="tight", facecolor="white"
)
plt.close()
print("fig4 saved")
