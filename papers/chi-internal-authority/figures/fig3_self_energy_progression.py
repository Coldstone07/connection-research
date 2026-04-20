"""
Figure 3: Aggregated Client Progression — Self-Energy Level (Spring 2026 Cohort)
Self-energy coded from cohort synthesis documentation:
  1 = Low (Manager dominant; significant blocks)
  2 = Fluctuating (emerging but inconsistent)
  3 = High/Emerging (consistent access, some fragmentation)
  4 = High/Stabilising (reliably accessible; transpersonal states)

Sorted by final level to show distribution.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Data from cohort synthesis (anonymised P01–P18)
# Coded from "Self-energy" field in per-client profiles
clients = [
    "P01", "P02", "P03", "P04", "P05", "P06",
    "P07", "P08", "P09", "P10", "P11", "P12",
    "P13", "P14", "P15", "P16", "P17", "P18",
]

# Mid-cohort (session ~4–6) vs. end-cohort (session ~8–10)
# Based on session arc descriptions: "progressed", "fluctuating", "emerging", etc.
self_energy_start = [2, 1, 2, 1, 2, 2, 1, 2, 3, 2, 1, 1, 2, 2, 2, 3, 1, 1]
self_energy_end   = [4, 3, 2, 2, 3, 3, 1, 2, 4, 4, 1, 2, 4, 3, 2, 4, 2, 2]

# Sort by end value
order = np.argsort(self_energy_end)[::-1]
clients_s   = [clients[i] for i in order]
start_s     = [self_energy_start[i] for i in order]
end_s       = [self_energy_end[i] for i in order]

# Colour by end level
level_colors = {1: "#C0392B", 2: "#E67E22", 3: "#2980B9", 4: "#1A7A4A"}
bar_colors = [level_colors[v] for v in end_s]

fig, ax = plt.subplots(figsize=(11, 6))

x = np.arange(len(clients_s))
w = 0.35

bars_start = ax.bar(x - w/2, start_s, w, color="#CCCCCC", edgecolor="#999999",
                    linewidth=0.8, label="Entry (session ~3)", zorder=2)
bars_end   = ax.bar(x + w/2, end_s,   w, color=bar_colors, edgecolor="#555555",
                    linewidth=0.8, label="Exit (session ~10)", zorder=2, alpha=0.92)

# Change arrows between start and end bars
for xi, s, e in zip(x, start_s, end_s):
    if e > s:
        color = "#1A7A4A"
        marker = "▲"
    elif e < s:
        color = "#C0392B"
        marker = "▼"
    else:
        color = "#888888"
        marker = "—"
    ax.text(xi, e + w + 0.07, marker, ha="center", va="bottom",
            fontsize=8, color=color)

ax.set_xticks(x)
ax.set_xticklabels(clients_s, fontsize=9, rotation=45, ha="right")
ax.set_yticks([1, 2, 3, 4])
ax.set_yticklabels(
    ["1 — Low\n(Manager dominant)", "2 — Fluctuating", "3 — High/Emerging", "4 — High/Stabilising"],
    fontsize=9,
)
ax.set_ylim(0, 5.2)
ax.set_xlim(-0.7, len(clients_s) - 0.3)
ax.set_ylabel("Self-Energy Level", fontsize=10)
ax.set_xlabel("Participant (sorted by exit level)", fontsize=10)

ax.yaxis.grid(True, color="#EEEEEE", zorder=0)
ax.set_axisbelow(True)
ax.spines[["top", "right"]].set_visible(False)

# Legend
legend_elements = [
    mpatches.Patch(facecolor="#CCCCCC", edgecolor="#999999", label="Entry level (~session 3)"),
    mpatches.Patch(facecolor="#1A7A4A", edgecolor="#555555", label="Exit: High/Stabilising (4)"),
    mpatches.Patch(facecolor="#2980B9", edgecolor="#555555", label="Exit: High/Emerging (3)"),
    mpatches.Patch(facecolor="#E67E22", edgecolor="#555555", label="Exit: Fluctuating (2)"),
    mpatches.Patch(facecolor="#C0392B", edgecolor="#555555", label="Exit: Low (1)"),
]
ax.legend(handles=legend_elements, loc="upper right", fontsize=8.5,
          framealpha=0.9, edgecolor="#CCCCCC")

# Summary annotation
n_improved = sum(1 for s, e in zip(start_s, end_s) if e > s)
n_same     = sum(1 for s, e in zip(start_s, end_s) if e == s)
n_declined = sum(1 for s, e in zip(start_s, end_s) if e < s)
ax.text(
    0.02, 0.97,
    f"N=18  |  Improved: {n_improved}  |  Stable: {n_same}  |  Declined: {n_declined}",
    transform=ax.transAxes,
    ha="left", va="top",
    fontsize=9, color="#555555",
    bbox=dict(facecolor="white", edgecolor="#CCCCCC", alpha=0.8, pad=3),
)

ax.set_title(
    "Figure 3. Self-Energy Progression Across the Spring 2026 Cohort (N=18)\n"
    "Coded from facilitator documentation; 4-level ordinal scale derived from IFS self-energy descriptors",
    fontsize=11, pad=10,
)

plt.tight_layout()
plt.savefig(
    "/Users/jatinalla/Desktop/AutoResearchClaw/artifacts/chi-paper/figures/fig3_self_energy_progression.png",
    dpi=300, bbox_inches="tight", facecolor="white"
)
plt.close()
print("fig3 saved")
