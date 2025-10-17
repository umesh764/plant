import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Sample rolling passes
passes = [
    {"stage": "R1", "shape": "square", "desc": "150x150", "x": 1, "y": 9},
    {"stage": "R2", "shape": "round", "desc": "Oval", "x": 2, "y": 9},
    {"stage": "R3", "shape": "square", "desc": "100x100", "x": 3, "y": 9},
    {"stage": "R4", "shape": "round", "desc": "Oval", "x": 4, "y": 9},
    {"stage": "R5", "shape": "square", "desc": "70x70", "x": 5, "y": 9},
    {"stage": "R6", "shape": "round", "desc": "Oval", "x": 6, "y": 9},
    {"stage": "R7", "shape": "square", "desc": "55x55", "x": 7, "y": 9},
    {"stage": "R8", "shape": "round", "desc": "Oval", "x": 8, "y": 9},
    {"stage": "R9", "shape": "round", "desc": "Round", "x": 9, "y": 9},
]

# Output TMT sizes
outputs = [
    {"desc": "8mm", "x": 7.5, "y": 6},
    {"desc": "10mm", "x": 8.5, "y": 6},
    {"desc": "12mm", "x": 9.5, "y": 6},
    {"desc": "16mm", "x": 10.5, "y": 6},
    {"desc": "20mm", "x": 11.5, "y": 6},
    {"desc": "25mm", "x": 12.5, "y": 6},
]

fig, ax = plt.subplots(figsize=(15, 8))
ax.set_xlim(0, 14)
ax.set_ylim(4, 11)
ax.axis("off")

# Draw passes
for p in passes:
    if p["shape"] == "square":
        rect = patches.Rectangle((p["x"], p["y"]), 0.8, 0.8, edgecolor="blue", facecolor="lightblue")
        ax.add_patch(rect)
    elif p["shape"] == "round":
        circ = patches.Circle((p["x"] + 0.4, p["y"] + 0.4), 0.4, edgecolor="orange", facecolor="moccasin")
        ax.add_patch(circ)

    ax.text(p["x"] + 0.4, p["y"] + 0.9, p["stage"], ha="center", fontsize=10, weight="bold")
    ax.text(p["x"] + 0.4, p["y"] - 0.1, p["desc"], ha="center", fontsize=9)

# Arrows between stages
for i in range(len(passes) - 1):
    start = passes[i]
    end = passes[i + 1]
    ax.annotate("",
                xy=(end["x"], end["y"] + 0.4),
                xytext=(start["x"] + 0.8, start["y"] + 0.4),
                arrowprops=dict(arrowstyle="->", color="green", lw=2))

# Output TMT connections
for o in outputs:
    rect = patches.Rectangle((o["x"], o["y"]), 0.8, 0.6, edgecolor="darkred", facecolor="mistyrose")
    ax.add_patch(rect)
    ax.text(o["x"] + 0.4, o["y"] + 0.3, o["desc"], ha="center", fontsize=10, weight="bold")

    ax.annotate("",
                xy=(o["x"] + 0.4, o["y"] + 0.6),
                xytext=(9.4, 9),
                arrowprops=dict(arrowstyle="->", color="purple", lw=1.5, linestyle="dashed"))

plt.tight_layout()
plt.show()
