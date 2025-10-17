import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Ellipse, Circle, FancyArrow
import os
import math

def calc_area_rect(w, h):
    return w * h

def calc_reduction(old_area, new_area):
    if old_area == 0:
        return 0
    return ((old_area - new_area) / old_area) * 100

def draw_stage(stage_info, old_w, old_h, new_w, new_h, filename):
    # stage_info: dict with stage name etc.
    old_area = calc_area_rect(old_w, old_h)
    new_area = calc_area_rect(new_w, new_h)
    reduction = calc_reduction(old_area, new_area)

    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_facecolor('black')
    ax.axis('off')

    # Draw old rectangle
    ax.add_patch(Rectangle((0.1, 0.7), 0.35, 0.2, edgecolor='white', fill=False))
    ax.text(0.275, 0.92, f"{old_w}×{old_h} mm", color='white', ha='center')
    ax.text(0.275, 0.68, "Old", color='white', ha='center')

    # Arrow
    ax.add_patch(FancyArrow(0.45, 0.8, 0.1, 0, width=0.01, color='green'))

    # Draw new shape
    aspect = new_w / new_h if new_h != 0 else 1
    cx, cy = 0.7, 0.8
    box_w, box_h = 0.35, 0.2
    # scale factor
    max_dim = max(old_w, old_h, new_w, new_h)
    scale = max_dim if max_dim != 0 else 1
    if abs(aspect - 1) < 0.3:
        side_w = box_w * (new_w / scale)
        side_h = box_h * (new_h / scale)
        ax.add_patch(Rectangle((cx - side_w/2, cy - side_h/2), side_w, side_h, color='skyblue'))
    else:
        ax.add_patch(Ellipse((cx, cy),
                             box_w * (new_w / scale),
                             box_h * (new_h / scale),
                             color='lightgreen'))

    ax.text(cx, cy + 0.15, f"{new_w}×{new_h} mm", color='white', ha='center')
    ax.text(cx, cy - 0.15, f"Red: {reduction:.1f} %", color='yellow', ha='center')
    ax.text(0.5, 0.4, f"Stage: {stage_info['stage']}", color='white', ha='center', fontsize=14)
    ax.text(0.5, 0.3, f"Old Area: {old_area} | New Area: {new_area}", color='white', ha='center')

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()
