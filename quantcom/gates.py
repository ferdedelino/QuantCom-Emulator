import numpy as np

IDENTITY = np.array([
    [1, 0],
    [0, 1]], dtype=complex)

HADAMARD = np.array([
    [1, 1],
    [1, -1]], dtype=complex) / np.sqrt(2)

PAULI_X = np.array([
    [0, 1],
    [1, 0]], dtype=complex)

PAULI_Y = np.array([
    [0, -1j],
    [1j,  0]], dtype=complex)

PAULI_Z = np.array([
    [1,  0],
    [0, -1]], dtype=complex)
