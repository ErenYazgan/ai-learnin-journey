def dot_product(vector_a, vector_b):
    """Calculates the dot product of two vectors of equal dimension."""
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same dimension.")
    
    total = 0
    for i in range(len(vector_a)):
        total += vector_a[i] * vector_b[i]
    return total


def scalar_multiply(vector, scalar):
    """Multiplies a vector by a scalar value."""
    result = []
    for i in range(len(vector)):
        result.append(vector[i] * scalar)
    return result


if __name__ == "__main__":
    # --- Dot Product Test ---
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    print(f"Dot Product of {v1} and {v2}: {dot_product(v1, v2)}")

    # --- Scalar Multiplication Test ---
    v3 = [3, -1]
    lambda_val = -0.3
    print(f"Scalar Multiplication of {v3} with {lambda_val}: {scalar_multiply(v3, lambda_val)}")