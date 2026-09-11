import numpy as np

A = np.array([[2, 4], 
              [4, 8]])
det_A = np.linalg.det(A)
print(f"2x2 Matrix Determinant: {det_A}")

m_small = 5
B = np.random.randn(m_small, m_small)
B[:, 1] = B[:, 0]  
det_B = np.linalg.det(B)
print(f"\nSmall (5x5) Matrix Determinant: {det_B}")

m_large = 50
C = np.random.randn(m_large, m_large)
C[:, 1] = C[:, 0]  
det_C = np.linalg.det(C)
print(f"Big (50x50) Matrix Determinant: {det_C}")