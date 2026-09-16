import numpy as np

n = 5
A = np.random.randn(n, n)          
A_inv = np.linalg.inv(A)           

u = np.random.randn(n, 1)
v = np.random.randn(n, 1)

A_new = A + (u @ v.T)

inv_classic = np.linalg.inv(A_new)

numerator = (A_inv @ u) @ (v.T @ A_inv)
denominator = 1 + (v.T @ A_inv @ u)
inv_sherman = A_inv - (numerator / denominator)

difference = inv_classic - inv_sherman

max_deviation = np.max(np.abs(difference))

print("Live System Matrix Update Test:")
print(f"The Deviation Between the Classical Method and Sherman-Morrison: {max_deviation}")