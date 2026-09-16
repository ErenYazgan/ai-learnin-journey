import numpy as np

n = 100
A = np.random.randn(n, n)

A_inv_classic = np.linalg.inv(A)

Q, R = np.linalg.qr(A)

A_inv_qr = np.linalg.inv(R) @ Q.T

difference_matrix = A_inv_classic - A_inv_qr

max_deviation = np.max(np.abs(difference_matrix))

print("100x100 Matrix Inversion Test:")
print(f"Maximum Mathematical Deviation Between Classic and QR: {max_deviation}")