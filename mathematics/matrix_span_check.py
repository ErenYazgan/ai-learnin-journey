import numpy as np

v = np.array([[1, 2, 3, 4]]).T

S = np.column_stack(([4, 3, 6, 2], [0, 4, 0, 1]))
T = np.column_stack(([1, 2, 2, 2], [0, 0, 1, 2]))

Sv = np.concatenate((S, v), axis=1)
Tv = np.concatenate((T, v), axis=1)

def check_span(original_matrix, augmented_matrix, name):
    rank_orig = np.linalg.matrix_rank(original_matrix)
    rank_aug = np.linalg.matrix_rank(augmented_matrix)
    
    if rank_aug == rank_orig:
        print(f"[{name}] In the span. (Rank {rank_orig} no new info)")
    else:
        print(f"[{name}] Not in the span (Rank {rank_orig} -> {rank_aug} added new info)")

check_span(S, Sv, "S Matrix")
check_span(T, Tv, "T Matrix")