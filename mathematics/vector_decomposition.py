import numpy as np
import matplotlib.pyplot as plt

w = np.array([2, 3])  
v = np.array([4, 0])  

beta = np.dot(w, v) / np.dot(v, v)
w_par = beta * v  

w_perp = w - w_par

sum_w = w_par + w_perp
print(f"Original w: {w}")
print(f"Sum of Parallel + Perpendicular: {sum_w}")

dot_product = np.round(np.dot(w_par, w_perp), 5)
print(f"Product of Estimate and Error (Dot Product): {dot_product} -> (0 ise sistem kusursuz yalıtılmıştır)")

plt.figure(figsize=(8, 8))

plt.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='black', label='w (Raw Data)')
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', alpha=0.3, label='v (Model Space)')
plt.quiver(0, 0, w_par[0], w_par[1], angles='xy', scale_units='xy', scale=1, color='red', label='w_par (Estimate)')

plt.quiver(w_par[0], w_par[1], w_perp[0], w_perp[1], angles='xy', scale_units='xy', scale=1, color='green', label='w_perp (Residual)')

plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(0, color='gray', linestyle='--')
plt.grid(True)
plt.legend()
plt.title("Vector Decomposition: Prediction (Red) and Error (Green)")
plt.show()