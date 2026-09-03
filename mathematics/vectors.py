import math
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
    """Calculates the Euclidean length (L2 Norm) of a vector """

    squared_sum = dot_product(vector, vector)

    return math.sqrt(squared_sum)

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
        results.append(dot_product(col_a, col_b))
        
    return results

def cosine_similarity(vector_a, vector_b):
    """Calculates the cosine similarity score (-1 to 1) between two vectors."""

    numerator = dot_product(vector_a, vector_b)
    
    denominator = vector_length(vector_a) * vector_length(vector_b)
    
    if denominator == 0:
        raise ValueError("Zero vectors have no defined cosine similarity.")
        
    return numerator / denominator

def hadamard_product(vector_a, vector_b):
    """Calculates element-wise multiplication (masking) of two vectors."""
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same dimension.")
        
    result = []
    for i in range(len(vector_a)):
        result.append(vector_a[i] * vector_b[i])  
    return result

def outer_product(vector_a, vector_b):
    """Calculates the outer product of two vectors, returning a 2D matrix."""
    matrix = []
    
    for i in range(len(vector_a)):
        row = [] 
        
        for j in range(len(vector_b)):
            
            row.append(vector_a[i] * vector_b[j])
            
        matrix.append(row)
        
    return matrix

def create_unit_vector(vector):
    """Converts a vector into a unit vector (length of 1) by preserving its direction."""
    
    length = vector_length(vector)
    
    if length == 0:
        raise ValueError("Cannot create a unit vector from a zero vector.")
        
    unit_vector = []
    for i in range(len(vector)):
        unit_vector.append(vector[i] / length)
        
    return unit_vector

if __name__ == "__main__":
    # --- Unit vector Test ---
    v_test = [3, 4]
    print(f"unit vector:\n{create_unit_vector(v_test)}")

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

    # --- -1 to 1 similarity score ---
    vector_a = np.random.randn(2)
    vector_b = np.random.randn(2)

    print(f"similarity score of random vectors:\n{cosine_similarity(vector_a, vector_b)}")
 
    # --- hadamard product ---

    vector_a = [4,5,1]
    vector_b = [3,1,4]

    print(f"multiplication (masking) of two vectors:\n{hadamard_product(vector_a, vector_b)}")

    # --- Outer Product Test ---
    v_vertical = [1, 2, 3]    
    v_horizontal = [4, 5]     

    print(f"Outer Product Matrix:\n{outer_product(v_vertical, v_horizontal)}")

    # --- Code Challenge: Dot Product with Unit Vectors ---
    v1_challenge = [3, 4]
    v2_challenge = [5, 12]

    normal_similarity = cosine_similarity(v1_challenge, v2_challenge)

    unit_v1 = create_unit_vector(v1_challenge)
    unit_v2 = create_unit_vector(v2_challenge)

    optimized_similarity = dot_product(unit_v1, unit_v2)

    print(f"\nNormal Kosinüs Benzerliği Skoru: {normal_similarity}")
    print(f"Optimize Skor (Birim Vektör Nokta Çarpımı): {optimized_similarity}")