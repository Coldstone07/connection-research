"""
Figure 1: Kairos System Architecture
Shows the five-layer experiential + technical stack:
  Input → AI Processing → CCM (mirror artifact) → Group Session → Peer Network
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

COLORS = {
    "user":    "#4A6FA5",   # blue  — user input
    "ai":      "#7B5EA7",   # purple — AI processing
    "ccm":     "#B07D62",   # amber  — CCM mirror artifact
    "group":   "#4A8A6E",   # green  — group session
    "peer":    "#5B8DB8",   # light blue — peer network
    "arrow":   "#555555",
    "label":   "#222222",
    "sublabel":"#666666",
}

layers = [
    {
        "y": 8.3,
        "color": COLORS["user"],
        "title": "Client Input",
        "subtitle": "Text / voice / journal entry\n(synchronous + asynchronous)",
        "icon": "①",
    },
    {
        "y": 6.5,
        "color": COLORS["ai"],
        "title": "AI Mediation Layer",
        "subtitle": "Reflective questions • Affect labeling\nNon-sycophantic response protocol",
        "icon": "②",
    },
    {
        "y": 4.7,
        "color": COLORS["ccm"],
        "title": "Consciousness Cartography Map (CCM)",
        "subtitle": "Post-session synthesised mirror artifact\n(IFS map • patterns • open questions)",
        "icon": "③",
    },
    {
        "y": 2.9,
        "color": COLORS["group"],
        "title": "Facilitated Group Session",
        "subtitle": "Human-led • cross-client resonance\nFacilitator A + Facilitator B",
        "icon": "④",
    },
    {
        "y": 1.1,
        "color": COLORS["peer"],
        "title": "Peer Coherence Network",
        "subtitle": "Peer pairs • accountability dyads\nAI dependency exit scaffold",
        "icon": "⑤",
    },
]

BOX_W = 7.0
BOX_H = 1.1
LEFT_X = 1.5

for layer in layers:
    y = layer["y"] - BOX_H / 2
    box = FancyBboxPatch(
        (LEFT_X, y), BOX_W, BOX_H,
        boxstyle="round,pad=0.08",
        linewidth=1.5,
        edgecolor=layer["color"],
        facecolor=layer["color"] + "22",
    )
    ax.add_patch(box)

    # Icon circle
    ax.add_patch(plt.Circle(
        (LEFT_X + 0.55, layer["y"]), 0.32,
        color=layer["color"], zorder=3
    ))
    ax.text(
        LEFT_X + 0.55, layer["y"], layer["icon"],
        ha="center", va="center",
        fontsize=11, color="white", fontweight="bold", zorder=4
    )

    # Title
    ax.text(
        LEFT_X + 1.2, layer["y"] + 0.18,
        layer["title"],
        ha="left", va="center",
        fontsize=11, fontweight="bold", color=layer["color"]
    )
    # Subtitle
    ax.text(
        LEFT_X + 1.2, layer["y"] - 0.22,
        layer["subtitle"],
        ha="left", va="center",
        fontsize=8.5, color=COLORS["sublabel"],
        linespacing=1.4,
    )

# Arrows between layers
arrow_x = LEFT_X + BOX_W / 2
for i in range(len(layers) - 1):
    y_start = layers[i]["y"] - BOX_H / 2 - 0.02
    y_end   = layers[i + 1]["y"] + BOX_H / 2 + 0.02
    ax.annotate(
        "",
        xy=(arrow_x, y_end),
        xytext=(arrow_x, y_start),
        arrowprops=dict(
            arrowstyle="-|>",
            color=COLORS["arrow"],
            lw=1.5,
            mutation_scale=14,
        ),
    )

# Side label: "Increasing autonomy →"
ax.annotate(
    "",
    xy=(0.6, layers[-1]["y"]),
    xytext=(0.6, layers[0]["y"]),
    arrowprops=dict(arrowstyle="-|>", color="#999999", lw=1.2, mutation_scale=12),
)
ax.text(
    0.35, (layers[0]["y"] + layers[-1]["y"]) / 2,
    "Increasing\nuser\nautonomy",
    ha="center", va="center", fontsize=8.5, color="#888888",
    rotation=90, linespacing=1.5,
)

# Title
ax.text(
    5.0, 9.7,
    "Figure 1. Kairos System Architecture",
    ha="center", va="center",
    fontsize=13, fontweight="bold", color=COLORS["label"],
)
ax.text(
    5.0, 9.35,
    "Five-layer stack designed for internal-authority building rather than engagement retention",
    ha="center", va="center",
    fontsize=9, color=COLORS["sublabel"],
)

plt.tight_layout(pad=0.2)
plt.savefig(
    "/Users/jatinalla/Desktop/AutoResearchClaw/artifacts/chi-paper/figures/fig1_system_architecture.png",
    dpi=300, bbox_inches="tight", facecolor="white"
)
plt.close()
print("fig1 saved")
