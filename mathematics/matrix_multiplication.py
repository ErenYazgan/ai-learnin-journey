import numpy as np

if __name__ == "__main__":
    # --- 41. Standard Matrix Multiplication (Dot Product) ---
    
    matrix_A = np.array([[1, 2, 3],
                         [4, 5, 6]])
    
    matrix_B = np.array([[7, 8],
                         [9, 1],
                         [2, 3]])
                         
    result = matrix_A @ matrix_B
    
    print(f"Matrix A Shape: {matrix_A.shape}")
    print(f"Matrix B Shape: {matrix_B.shape}")
    print(f"\nResulting Matrix Shape: {result.shape}")
    print(f"Result Matrix:\n{result}")

    A = np.array([[1, 2],
                  [3, 4]])
    B = np.array([[5, 6],
                  [7, 8]])

    hadamard_result = A * B

    dot_result = A @ B

    print("Hadamard (Element-wise) (*):\n", hadamard_result)
    print("\nReal Matrix Multiplication (@):\n", dot_result)

    # --- Matrix-Vector Multiplication ---
   
    weights = np.array([[0.1, 0.2, 0.3, 0.4],
                        [0.5, 0.6, 0.7, 0.8],
                        [0.9, 0.1, 0.2, 0.3]])

    x_input = np.array([100, 5, 120, 3]).reshape(4, 1)

    bias = np.array([0.5, 
                     -1.2, 
                     0.8]).reshape(3, 1)

    # Forward Pass
    neuron_outputs = (weights @ x_input) + bias

    print("Weights Shape:", weights.shape)
    print("Input Shape:", x_input.shape)
    print("Bias Shape:", bias.shape)
    print("\nNeuron Outputs (Before Activation):\n", neuron_outputs)