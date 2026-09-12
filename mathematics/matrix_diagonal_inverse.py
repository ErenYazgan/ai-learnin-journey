import numpy as np

diag_elements = np.array([2, 4, 5])
D = np.diag(diag_elements)

print("--- Original Diagonal Matrix ---")
print(D)

D_inv_numpy = np.linalg.inv(D)
print("\n--- Inverted Version Using NumPy---")
print(D_inv_numpy)

D_inv_cheap = np.diag(1 / diag_elements)
print("\n--- Manual Trick (Simply by calculating 1/x) ---")
print(D_inv_cheap)

bad_elements = np.array([2, 0, 5])
D_bad = np.diag(bad_elements)

print("\n--- How system lock ?---")
try:
    np.linalg.inv(D_bad)
except np.linalg.LinAlgError as e:
    print(f"Error Caught: {e} -> Because 1/0 is undefined!")