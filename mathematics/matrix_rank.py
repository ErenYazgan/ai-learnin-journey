import numpy as np

# 1. Full-Rank Matris (Her satır ve sütun birbirinden tamamen bağımsız yeni bilgi taşıyor)
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]])

# 2. Rank-Deficient Matris (3. satır, 1. ve 2. satırın toplamından ibaret - sahte bilgi)
B = np.array([[1, 2, 3],
              [4, 5, 6],
              [5, 7, 9]]) 

print("A Matrisinin Rank'i (Tam Bilgi):", np.linalg.matrix_rank(A)) # Çıktı: 3
print("B Matrisinin Rank'i (Kopya Bilgi):", np.linalg.matrix_rank(B)) # Çıktı: 2 (Sistem 3. satırı çöpe attı)