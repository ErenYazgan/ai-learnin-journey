import numpy as np

m = 1000
n = 5
X = np.random.randn(m, n)
y = np.random.randn(m, 1)

beta_classic = np.linalg.inv(X.T @ X) @ X.T @ y

Q, R = np.linalg.qr(X)

beta_qr_slide = np.linalg.inv(R.T @ R) @ (Q @ R).T @ y

beta_qr_real = np.linalg.inv(R) @ Q.T @ y

gap = beta_classic - beta_qr_real
maximum_deviation = np.max(np.abs(gap))

print("Least-Squares Model Training Test:")
print(f"Maximum Deviation Between the Classical Method and the QR Method: {maximum_deviation}")