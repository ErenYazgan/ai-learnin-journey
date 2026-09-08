import numpy as np

# 1. Full-Rank Matris 
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]])

# 2. Rank-Deficient Matris 
B = np.array([[1, 2, 3],
              [4, 5, 6],
              [5, 7, 9]]) 

print("A Rank of the Matrix (Full Information):", np.linalg.matrix_rank(A)) 
print("B Rank of the Matrix (Copy Information):", np.linalg.matrix_rank(B)) 


# Code challenge: reduced-rank matrix via multiplication

A = np.random.randn(10,4)
B = np.random.randn(4,10)
C = A@B
print(np.linalg.matrix_rank(C))
print(np.shape(C))

a=33
b=4
c=7

B= np.random.randn(33,4) @ np.random.randn(4,7)

print(np.linalg.matrix_rank(B))
print(np.shape(B))


