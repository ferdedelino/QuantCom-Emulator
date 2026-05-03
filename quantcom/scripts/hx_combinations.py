from functools import reduce

import numpy as np

from itertools import product
from quantcom.gates import Gate


def combination_to_matrix(combination):
    gate_map = {"H": Gate.HADAMARD, "X": Gate.PAULI_X}
    matrices = [gate_map[m] for m in combination]
    return reduce(np.matmul, matrices)


def hx_combinations(k: int) -> int:
    combinations = product("HX", repeat=k)
    all_matrices = []
    for combination in combinations:
        mat = combination_to_matrix(combination)
        if not any(np.allclose(mat, existing) for existing in all_matrices):
            all_matrices.append(mat)
    return len(all_matrices)


for k in range(2, 15):
    print(f"Combinations of size {k}: {hx_combinations(k)}")
