import numpy as np

def dot_product(vector_a, vector_b):
    """Calculates the dot product of two vectors of equal dimension."""
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same dimension.")
    
    total = 0
    for i in range(len(vector_a)):
        total += vector_a[i] * vector_b[i]
    return total

def vector_length(vector):
    """Calculates the Euclidean length (L2 Norm) of a vector from the dot product function i made"""

    squared_sum = dot_product(vector, vector)

    return math.sqrt(squared_sum)

def vector_length(vector):
    """Calculates vector length"""
    total = 0
    for i in range(len(vector)):
        total += vector[i] * vector[i]
    return total


def scalar_multiply(vector, scalar):
    """Multiplies a vector by a scalar value."""
    result = []
    for i in range(len(vector)):
        result.append(vector[i] * scalar)
    return result

def matrix_column_dot_product(matrix_a, matrix_b):
    """Calculates the dot product of corresponding columns between two matrices."""
    results = []
    
    num_cols = matrix_a.shape[1]
    
    for i in range(num_cols):
        col_a = matrix_a[:, i]
        col_b = matrix_b[:, i]
        results.append(np.dot(col_a, col_b))
        
    return results

if __name__ == "__main__":
    # --- Dot Product Test ---
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    print(f"Dot Product of {v1} and {v2}: {dot_product(v1, v2)}")

    # --- Scalar Multiplication Test ---
    v3 = [3, -1]
    lambda_val = -0.3
    print(f"Scalar Multiplication of {v3} with {lambda_val}: {scalar_multiply(v3, lambda_val)}")

    # --- Matrix Column Dot Product Test ---
    matrix_A = np.random.randn(4, 6)
    matrix_B = np.random.randn(4, 6)

    print(f"Dot product results of each pair of columns:\n{matrix_column_dot_product(matrix_A, matrix_B)}")

    # --- Vector Length Test From dot product Function i made ---
    v_test = [3, 4]
    print(f"Vector Length of {v_test}: {vector_length(v_test)}")

    # Random length test
    v_random = np.random.randn(2)
    print(f"Random Vector Length: {vector_length(v_random)}")

    # --- vector length test ---
    vector = [3,4]
   
    print(f"vector length:\n{np.sqrt(vector_length(vector))}")
