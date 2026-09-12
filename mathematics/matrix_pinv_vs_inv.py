import numpy as np

A = np.random.randn(5, 5)

inv_A = np.linalg.inv(A)   
pinv_A = np.linalg.pinv(A) 

difference_matrix = inv_A - pinv_A

print("Difference Matrix (inv_A - pinv_A):")

print(np.round(difference_matrix, 5))

print(f"\nThe maximum mathematical deviation between the two methods: {np.max(np.abs(
difference_matrix))}")