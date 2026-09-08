import numpy as np

m = 30
A_raw = np.random.randn(m, m)
A = np.round(10 * (A_raw.T @ A_raw))

A[:, 0] = A[:, 1]

print("Expected Capacity: 30")
print("New rank after sabotage:", np.linalg.matrix_rank(A)) 

lmbda = 0.01

B = A + (lmbda * np.eye(m))

print("New rank after shifting:", np.linalg.matrix_rank(B)) 