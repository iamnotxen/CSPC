"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)
data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)
t = data[:, 0]
y  = data [:, 1]
# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?

v = np.gradient ( y, t)
a = np.gradient (v , t)

mean = np.mean (a)
dev = np.std(a)
print (mean)
print (dev)

# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)

v_rec = cumulative_trapezoid( a,  t, initial = 0) + v[0]

y_rec = cumulative_trapezoid ( v_rec, t , initial = 0) + y[0]
max_diff = np.max(np.abs(y - y_rec))

print(f" difference is {max_diff:.3f} meters")

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
# Create 3 stacked subplots sharing the x-axis
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 9), sharex=True)

ax1.plot(t, y, label="measured position $y(t)$", color="tab:blue")
ax1.plot(t, y_rec, "--", label="reconstructed $y_{rec}(t)$", color="tab:cyan", alpha=0.8)
ax1.set_ylabel("position")
ax1.set_title("feefall motion analysis")
ax1.grid(True, linestyle="--", alpha=0.5)
ax1.legend()

ax2.plot(t, v, label="velocity $v(t)$", color="tab:orange")
ax2.set_ylabel("velocity (m/s)")
ax2.grid(True, linestyle="--", alpha=0.5)
ax2.legend()

ax3.plot(t, a, label="acceleration $a(t)$", color="tab:red", alpha=0.7)
ax3.axhline(-9.81, color="black", linestyle="--", linewidth=1.5, label="theoretical $-g$ (-9.81 m/s)")
ax3.set_xlabel("time")
ax3.set_ylabel("acceleration")
ax3.grid(True, linestyle="--", alpha=0.5)
ax3.legend()

plt.tight_layout()
plt.savefig("motion.png", dpi=300)
