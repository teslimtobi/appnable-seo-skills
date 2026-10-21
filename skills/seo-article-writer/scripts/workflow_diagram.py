#!/usr/bin/env python3
"""Draw a 4-step workflow illustration (Trigger -> Automation action -> Approval / validation -> Business outcome).

Usage:
  python workflow_diagram.py out.png \
    --steps "Signed engagement letter arrives in a shared mailbox" \
            "Flow files it to the matter folder and extracts the details" \
            "Risk team checks conflicts and confirms the details" \
            "Matter opens the same day, with every step logged for audit" \
    [--titles "Trigger" "Automation action" "Approval / validation" "Business outcome"] \
    [--footer "People keep the judgement at step 3. Automation handles the rest."]

Output is a compressed PNG (well under 200 KB). Drawn, not AI-generated.
"""
import argparse, textwrap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument('out')
ap.add_argument('--steps', nargs=4, required=True)
ap.add_argument('--titles', nargs=4, default=['Trigger', 'Automation action', 'Approval / validation', 'Business outcome'])
ap.add_argument('--footer', default='People keep the judgement at step 3. Automation handles the rest.')
a = ap.parse_args()
# Appnable brand: green #A0C63F, grey #818181, dark #1A1A1A, light #E8E9E4
colours = [('#F3F4F0', '#818181', '#1A1A1A'), ('#F3F4F0', '#818181', '#1A1A1A'), ('#EEF5DD', '#A0C63F', '#4F6B12'), ('#A0C63F', '#7FA22B', '#1A1A1A')]
fig, ax = plt.subplots(figsize=(11, 3.4), dpi=110)
ax.set_xlim(0, 110); ax.set_ylim(0, 32); ax.axis('off')
w, gap, y, h, x0 = 23, 4.5, 6, 21, 2.5
for i, (t, sub, (fill, col, txt)) in enumerate(zip(a.titles, a.steps, colours)):
    x = x0 + i * (w + gap)
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.3,rounding_size=1.5', fc=fill, ec=col, lw=1.2))
    ax.text(x + w / 2, y + h - 3.2, str(i + 1), ha='center', va='center', fontsize=9, color=txt)
    ax.text(x + w / 2, y + h - 6.8, t, ha='center', va='center', fontsize=9.8, fontweight='bold', color=txt)
    ax.text(x + w / 2, y + 7, '\n'.join(textwrap.wrap(sub, 22)[:4]), ha='center', va='center', fontsize=9, color='#1A1A1A' if fill == '#A0C63F' else '#333333', linespacing=1.45)
    if i < 3:
        ax.add_patch(FancyArrowPatch((x + w + 0.7, y + h / 2), (x + w + gap - 0.7, y + h / 2), arrowstyle='-|>', mutation_scale=15, color='#818181', lw=1.4))
if a.footer:
    ax.text(55, 1.8, a.footer, ha='center', fontsize=9.5, style='italic', color='#818181')
tmp = a.out + '.tmp.png'
plt.savefig(tmp, bbox_inches='tight', facecolor='white')
Image.open(tmp).convert('P', palette=Image.ADAPTIVE, colors=128).save(a.out, optimize=True)
import os; os.remove(tmp)
print(a.out, os.path.getsize(a.out) // 1024, 'KB')
