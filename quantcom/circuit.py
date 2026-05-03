import numpy as np

from quantcom.gates import Gate
from quantcom.qubit import Qubit


class Circuit:
    def __init__(self, num_qubits: int):
        self.num_qubits = num_qubits
        self.dimension = 2 ** num_qubits
        self.gates: list[np.ndarray] = []

    def add_gate(self, gate: np.ndarray) -> None:
        shape = gate.shape
        assert len(shape) == 2, "Gate must be 2-dimensional array"
        assert shape[0] == shape[1] == self.dimension, "Gate must match circuit dimension"
        self.gates.insert(0, gate)

    def apply_gates(self, qubit: Qubit) -> Qubit:
        # todo: more than one qubit (not done in the lecture yet)
        mat = Gate.IDENTITY
        for gate in self.gates:
            mat = np.matmul(mat, gate)
        state = np.matmul(mat, qubit.state)
        return Qubit(state[0], state[1])

    def readout(self, qubit: Qubit, n: int = 1) -> list[int]:
        final_state = self.apply_gates(qubit)
        probabilities = np.abs(final_state.state) ** 2
        return np.random.choice([0, 1], p=probabilities, size=n).tolist()

    def readout_one(self, qubit: Qubit) -> int:
        return self.readout(qubit, 1)[0]
