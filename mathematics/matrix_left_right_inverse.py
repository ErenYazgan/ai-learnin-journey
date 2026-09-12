import numpy as np
import matplotlib.pyplot as plt

tall_A = np.random.randn(50, 10)

left_inv = np.linalg.inv(tall_A.T @ tall_A) @ tall_A.T

I_left = left_inv @ tall_A 

wide_B = np.random.randn(10, 50)

right_inv = wide_B.T @ np.linalg.inv(wide_B @ wide_B.T)

I_right = wide_B @ right_inv

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(I_left, cmap='gray')
axes[0].set_title('Left Inverse @ Tall Matrix')

axes[1].imshow(I_right, cmap='gray')
axes[1].set_title('Wide Matrix @ Right Inverse')

plt.show()