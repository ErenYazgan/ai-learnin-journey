import numpy as np
import matplotlib.pyplot as plt

lambdas = np.linspace(0, 0.1, 30)

avg_dets = np.zeros(len(lambdas))

print("1000x simulation starting, matrices being recovered...")

for i, lam in enumerate(lambdas):
    dets = np.zeros(1000) 
    
    for j in range(1000):
       
        M = np.random.randn(20, 20)
        
        M[:, 1] = M[:, 0]
        
        M_shifted = M + lam * np.eye(20)
        
        dets[j] = np.abs(np.linalg.det(M_shifted))
        
    avg_dets[i] = np.mean(dets)

plt.plot(lambdas, avg_dets, 's-', linewidth=2, markerfacecolor='black')
plt.title("Ridge Regularization: Volume (Det) Recovery via Shifting")
plt.xlabel("Lambda (Shift Amount)")
plt.ylabel("Average Absolute Determinant (Volume)")
plt.grid(True)
plt.show()