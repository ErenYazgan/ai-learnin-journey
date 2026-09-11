import numpy as np

A = np.random.randn(6, 6)
det_orig = np.linalg.det(A)
print(f"Original Determinant: {det_orig}")

A_swap_1 = A.copy()
A_swap_1[[0, 1]] = A_swap_1[[1, 0]]
det_1 = np.linalg.det(A_swap_1)
print(f"Single-Line Change: {det_1}")

A_swap_2 = A_swap_1.copy()
A_swap_2[[2, 3]] = A_swap_2[[3, 2]]
det_2 = np.linalg.det(A_swap_2)
print(f"Swap Two Lines (Reverts to Original): {det_2}")