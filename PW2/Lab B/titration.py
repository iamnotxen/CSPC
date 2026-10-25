"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# TODO 1: read titration.csv (columns volume_base, pH) into arrays V, pH.
data = pd.read_csv("titration.csv")
V = data["volume_base"].values
pH = data["pH"].values

# TODO 2: compute the slope of the pH curve with np.gradient(pH, V), and find
#         the volume where that slope is largest (np.argmax). That is the
#         equivalence point. Print it.
dpH_dV = np.gradient(pH, V)
max_slope_idx = np.argmax(dpH_dV)
equivalence_volume = V[max_slope_idx]

print(f"Equivalence point volume V ≈ {equivalence_volume:.2f} mL")

# TODO 3: make two plots side by side: (left) pH vs volume with a line at the
#         equivalence point; (right) the slope vs volume, showing it peaks
#         at the equivalence point. Save as titration.png.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(V, pH, color='purple', linewidth=2)
ax1.axvline(equivalence_volume, color='red', linestyle='--', label=f'Equivalence Point ({equivalence_volume:.1f} mL)')
ax1.set_xlabel("Volume Base ($V$) [mL]")
ax1.set_ylabel("pH")
ax1.set_title("Titration Curve")
ax1.legend()

ax2.plot(V, dpH_dV, color='teal', linewidth=2)
ax2.axvline(equivalence_volume, color='red', linestyle='--', label='Peak Slope')
ax2.set_xlabel("Volume Base ($V$) [mL]")
ax2.set_ylabel("Slope ($dpH / dV$)")
ax2.set_title("Titration Slope (Derivative)")
ax2.legend()

plt.tight_layout()
plt.savefig("titration.png")
plt.show()