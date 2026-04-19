import random

from quantcom import gates
from quantcom.circuit import Circuit
from quantcom.qubit import Qubit


def one_round():
    # Alice initializes
    a = random.choice([0, 1])
    r = random.choice([0, 1])
    r_state = Qubit.zero() if r == 0 else Qubit.one()
    circuit = Circuit(1)
    if a == 0:
        circuit.add_gate(gates.IDENTITY)
    else:
        circuit.add_gate(gates.HADAMARD)

    # Eves attack
    v = random.choice([gates.IDENTITY, gates.HADAMARD])
    v_prime = random.choice([gates.IDENTITY, gates.HADAMARD])
    circuit.add_gate(v)
    t = circuit.readout(r_state, 1)[0]
    t_state = Qubit.zero() if t == 0 else Qubit.one()
    circuit = Circuit(1)  # Reset circuit - old gates are no longer relevant after readout
    circuit.add_gate(v_prime)

    # Bob reads
    b = random.choice([0, 1])
    if b == 0:
        circuit.add_gate(gates.IDENTITY)
    else:
        circuit.add_gate(gates.HADAMARD)
    s = circuit.readout(t_state, 1)[0]
    return a, b, r, t, s


total = 0
eve_detected = 0
eve_correct = 0
for i in range(100000):
    a, b, r, t, s = one_round()
    if a != b:
        continue
    total += 1
    if r != s:
        eve_detected += 1
    if t == r:
        eve_correct += 1

print(f"Eve detected chance: {eve_detected / total}")
print(f"Eve correct: {eve_correct / total}")
