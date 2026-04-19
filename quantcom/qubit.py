import numpy as np
import random


class Qubit:
    def __init__(self, alpha: complex, beta: complex):
        norm = abs(alpha) ** 2 + abs(beta) ** 2
        assert np.isclose(norm, 1.0), "Qubit state must be normalized!"
        self.state = np.array([alpha, beta], dtype=complex)

    @classmethod
    def zero(cls):
        return cls(1, 0)

    @classmethod
    def one(cls):
        return cls(0, 1)

    def measure(self):
        alpha = self.state[0]
        if random.random() < abs(alpha) ** 2:
            return 0
        else:
            return 1
