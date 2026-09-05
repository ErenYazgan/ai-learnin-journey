import numpy as np

if __name__ == "__main__":
    # 1. Terminology & Dimensionality 

    matrix_a = np.array([[1, 2, 3], 
                         [4, 5, 6]])
    
    print(f"Matrix A Shape (Satır, Sütun): {matrix_a.shape}") 

    # 2. Zoo of Matrices 
    identity_matrix = np.eye(3)           # Birim Matris (Çaprazı 1, gerisi 0)
    zero_matrix = np.zeros((2, 4))        # Sıfır Matrisi (Tamamen boş tablo)
    diag_matrix = np.diag([5, 10, 15])    # Sadece köşegeninde veri olan matris
    random_square = np.random.randn(4, 4) # 4x4 rastgele sayılardan oluşan kare matris

    print(f"\nIdentity Matrix:\n{identity_matrix}")

    # 3. Concatenation 
    matrix_b = np.array([[7, 8, 9], 
                         [10, 11, 12]]) # matrix_a ile aynı boyutta (2x3)
    
    # vertical stack
    vertical_concat = np.vstack((matrix_a, matrix_b))
    print(f"\nVertical Stack (Alt Alta 4x3):\n{vertical_concat}")
    
    # horizontal stack
    horizontal_concat = np.hstack((matrix_a, matrix_b))
    print(f"\nHorizontal Stack (Yan Yana 2x6):\n{horizontal_concat}")

    # --- Matrix Arithmetic & Linearity Code Challenge ---
    
    # 1. We define two matrices of identical dimensions (shape) and a scalar.
    matrix_X = np.array([[1, 2], [3, 4]])
    matrix_Y = np.array([[5, 6], [7, 8]])
    scalar_val = 3

    # 2. Left Side Of the Equation: s * (A + B)
    # Rule: The addition (+) operation works only if the dimensions match perfectly.
    left_side = scalar_val * (matrix_X + matrix_Y)

    # 3. Right Side Of the Equation: (s * A) + (s * B)
    # Rule: Scalar multiplication (*) distributes the number to each cell of the table individually.
    right_side = (scalar_val * matrix_X) + (scalar_val * matrix_Y)

    print(f"\nLeft Side (s * (A+B)):\n{left_side}")
    print(f"Right Side (sA + sB):\n{right_side}")
    
    # 4. Engineering Verification (Linearity Proof)
    
    is_linear = np.array_equal(left_side, right_side)
    print(f"Is Matrix-Scalar Multiplication Linear? : {is_linear}")

    # --- Transpose ---
    
    matrix_original = np.array([[1, 2, 3], 
                                [4, 5, 6]])
    
    matrix_transposed = matrix_original.T
    
    print(f"\nOriginal Shape: {matrix_original.shape}")
    print(f"Transposed Shape: {matrix_transposed.shape}")
    print(f"Transposed Matrix (3x2):\n{matrix_transposed}")

    matrix_sym = np.array([[1, 7], 
                           [7, 1]])
    
    is_symmetric = np.array_equal(matrix_sym, matrix_sym.T)
    print(f"\nIs the matrix symmetric? : {is_symmetric}")

   # ---  Broadcasting  ---
    
    data_matrix = np.array([[10, 20, 30],  
                            [40, 50, 60],  
                            [70, 80, 90]]) 
    
    bias_vector = np.array([1, 2, 3])      
    
    broadcast_result = data_matrix + bias_vector
    
    print(f"\nBroadcasting Result:\n{broadcast_result}")