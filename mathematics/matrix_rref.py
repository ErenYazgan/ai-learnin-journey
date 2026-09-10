import numpy as np
import sympy as sym

# 1. Square Matrix 
print("--- 1. SQUARE MATRIX (4x4) ---")
mat_sq = np.random.randint(1, 10, (4, 4))
rref_sq = sym.Matrix(mat_sq).rref()[0]
print(np.array(rref_sq))

# 2. Rectangular Matrices 
print("\n--- 2. TALL MATRIX (5x3) ---")
mat_tall = np.random.randint(1, 10, (5, 3))
print(np.array(sym.Matrix(mat_tall).rref()[0]))

print("\n--- 2. WIDE MATRIX (3x5) ---")
mat_wide = np.random.randint(1, 10, (3, 5))
print(np.array(sym.Matrix(mat_wide).rref()[0]))

# 3. Linear Dependencies 
print("\n--- 3. LINEAR DEPENDENCY (4x4) ---")
mat_dep = np.random.randint(1, 10, (4, 4))
mat_dep[:, 1] = mat_dep[:, 0]  
mat_dep[3, :] = mat_dep[2, :]  
print(np.array(sym.Matrix(mat_dep).rref()[0]))