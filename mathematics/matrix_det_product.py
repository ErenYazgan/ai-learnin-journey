import numpy as np

A = np.random.randn(4, 4)
B = np.random.randn(4, 4)

det_A_times_det_B = np.linalg.det(A) * np.linalg.det(B)

det_AB = np.linalg.det(A @ B)


print(f"Separate Product: {det_A_times_det_B}")
print(f"Matrix Multiplication: {det_AB}")