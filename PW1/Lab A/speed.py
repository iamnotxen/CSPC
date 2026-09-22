import time
from decay import simulate, simulate_loop

N0 = 200000 
lam = 0.4
dt = 0.05
steps = 200

t0 = time.perf_counter()
simulate_loop(N0, lam, dt=dt, steps=steps)
t1 = time.perf_counter()
loop_time = t1 - t0

t0 = time.perf_counter()
simulate(N0, lam, dt=dt, steps=steps)
t1 = time.perf_counter()
numpy_time = t1 - t0

speedup = loop_time / numpy_time

print(f"Pure-Python loop time: {loop_time:.4f} s")
print(f"NumPy vectorized time: {numpy_time:.4f} s")
print(f"NumPy is {speedup:.2f}x faster")