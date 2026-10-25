"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
#         It equals zero exactly at equilibrium
def k_imbalance(x):
    x_val = np.clip(x, 0.0, 0.999)
    return ((2 * x_val)**2 / ((a - x_val) * (b - x_val))) - K

# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance
#         (start x0=0.5). This is root-finding.
x_newton = newton(k_imbalance, x0=0.5)

# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
#         (method "SLSQP", bounds [(0, 0.999)], x0=[0.5]). Print both answers
#         and confirm they agree.
def objective(x):
    return k_imbalance(x)**2

res_slsqp = minimize(objective, x0=[0.5], method="SLSQP", bounds=[(0.0, 0.999)])
x_slsqp = res_slsqp.x[0]

print(f"Newton extent x ≈ {x_newton:.4f}")
print(f"SLSQP extent x  ≈ {x_slsqp:.4f}")

# TODO 4: report the equilibrium amounts (H2, I2, HI), and plot how the three
#         amounts change with the extent x, marking the equilibrium. Save
#         equilibrium.png.
eq_H2 = a - x_newton
eq_I2 = b - x_newton
eq_HI = 2.0 * x_newton

print(f"\nEquilibrium Composition:")
print(f"  n(H2) = {eq_H2:.3f} mol")
print(f"  n(I2) = {eq_I2:.3f} mol")
print(f"  n(HI) = {eq_HI:.3f} mol")

x_vals = np.linspace(0, 0.99, 200)
h2_vals = a - x_vals
i2_vals = b - x_vals
hi_vals = 2.0 * x_vals

plt.figure(figsize=(7, 5))
plt.plot(x_vals, h2_vals, label='$H_2$', color='blue')
plt.plot(x_vals, i2_vals, label='$I_2$', color='green')
plt.plot(x_vals, hi_vals, label='$HI$', color='red', linewidth=2)
plt.axvline(x_newton, color='black', linestyle='--', label=f'Equilibrium ($x$={x_newton:.2f})')
plt.xlabel("Reaction Extent ($x$)")
plt.ylabel("Amount (moles)")
plt.title("Chemical Equilibrium Composition (K = 15.6)")
plt.legend()
plt.tight_layout()
plt.savefig("equilibrium.png")
plt.show()