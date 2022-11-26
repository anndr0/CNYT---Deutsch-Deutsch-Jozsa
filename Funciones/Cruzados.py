import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

""" Entrada |0 >, |0 >"""

simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(2, 2)
# Add a X gate on qubit 0
circuit.x(0)
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)
# Add a X gate on qubit 0
circuit.x(0)

# Map the quantum measurement to the classical bits
circuit.measure([0, 1], [1, 0])

compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:", counts)
print(circuit)
plot_histogram(counts)
plt.show()

""" Entrada |0 >, |1 > """

circuit = QuantumCircuit(2, 2)

# Add a X gate on qubit 1
circuit.x(1)
# Add a X gate on qubit 0
circuit.x(0)
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)
# Add a X gate on qubit 0
circuit.x(0)

# Map the quantum measurement to the classical bits
circuit.measure([0, 1], [1, 0])

compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:", counts)
print(circuit)
plot_histogram(counts)
plt.show()

""" Entrada |1 >, |0 > """

circuit = QuantumCircuit(2, 2)

# Add a X gate on qubit 0
circuit.x(0)
# Add a X gate on qubit 0
circuit.x(0)
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)
# Add a X gate on qubit 0
circuit.x(0)

# Map the quantum measurement to the classical bits
circuit.measure([0, 1], [1, 0])

compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:", counts)
print(circuit)
plot_histogram(counts)
plt.show()

"""" Entrada |1 >, |1 > """

circuit = QuantumCircuit(2, 2)

# Add a X gate on qubit 0
circuit.x(0)
# Add a X gate on qubit 1
circuit.x(1)

# Add a X gate on qubit 0
circuit.x(0)
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)
# Add a X gate on qubit 0
circuit.x(0)

# Map the quantum measurement to the classical bits
circuit.measure([0, 1], [1, 0])

compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:", counts)
print(circuit)
plot_histogram(counts)
plt.show()