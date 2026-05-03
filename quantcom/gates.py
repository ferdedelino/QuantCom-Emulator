import numpy as np


class Gate:
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
        [1j, 0]], dtype=complex)

    PAULI_Z = np.array([
        [1, 0],
        [0, -1]], dtype=complex)

    T = np.array([
        [1, 0],
        [0, np.exp(-1j * np.pi / 4)]], dtype=complex)

    @staticmethod
    def ROTATION_X(phi: float) -> np.ndarray:
        cos: complex = np.cos(phi / 2)
        sin: complex = np.sin(phi / 2)
        return np.array([
            [cos, -1j * sin],
            [-1j * sin, cos]], dtype=complex)

    @staticmethod
    def ROTATION_Y(phi: float) -> np.ndarray:
        cos: complex = np.cos(phi / 2)
        sin: complex = np.sin(phi / 2)
        return np.array([
            [cos, -sin],
            [sin, cos]], dtype=complex)

    @staticmethod
    def ROTATION_Z(phi: float) -> np.ndarray:
        exp1: complex = np.exp(-1j * phi / 2)
        exp2: complex = np.exp(1j * phi / 2)
        return np.array([
            [exp1, 0],
            [0, exp2]], dtype=complex)
