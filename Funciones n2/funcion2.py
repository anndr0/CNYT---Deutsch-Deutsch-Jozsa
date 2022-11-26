import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

"""| 000 >"""
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(3, 3)

circuit.id(0)
circuit.id(1)
circuit.id(2)

circuit.barrier(0,1,2)
circuit.x(0)
circuit.cx(0, 2)
circuit.x(0)
circuit.barrier(0,1,2)
#####
# Map the quantum measurement to the classical bits
circuit.measure([0,1,2], [2,1,0])

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()

counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)

print(circuit)
plot_histogram(counts)
plt.show()

"""| 001 >"""
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(3, 3)

circuit.id(0)
circuit.id(1)
circuit.x(2)

circuit.barrier(0,1,2)

circuit.x(0)
circuit.cx(0, 2)
circuit.x(0)

circuit.barrier(0,1,2)
#####
# Map the quantum measurement to the classical bits
circuit.measure([0,1,2], [2,1,0])

compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

"""| 010 >"""
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(3, 3)

circuit.id(0)
circuit.id(2)
circuit.x(1)

circuit.barrier(0,1,2)

circuit.x(0)
circuit.cx(0, 2)
circuit.x(0)

circuit.barrier(0,1,2)
#####
# Map the quantum measurement to the classical bits
circuit.measure([0,1,2], [2,1,0])

compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

"""| 011 >"""
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(3, 3)

circuit.id(0)
circuit.x(1)
circuit.x(2)

circuit.barrier(0,1,2)

circuit.x(0)
circuit.cx(0, 2)
circuit.x(0)

circuit.barrier(0,1,2)
#####
# Map the quantum measurement to the classical bits
circuit.measure([0,1,2], [2,1,0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)

print(circuit)
plot_histogram(counts)
plt.show()

"""""""| 100 >"""""""
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(3, 3)

circuit.id(1)
circuit.id(2)
circuit.x(0)

circuit.barrier(0,1,2)

circuit.x(0)
circuit.cx(0, 2)
circuit.x(0)

circuit.barrier(0,1,2)
#####
# Map the quantum measurement to the classical bits
circuit.measure([0,1,2], [2,1,0])

compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

"""""""| 101 >"""""""
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(3, 3)

circuit.x(0)
circuit.id(1)
circuit.x(2)

circuit.barrier(0,1,2)

circuit.x(0)
circuit.cx(0, 2)
circuit.x(0)

circuit.barrier(0,1,2)
#####
# Map the quantum measurement to the classical bits
circuit.measure([0,1,2], [2,1,0])

compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

"""""""| 110 >"""""""
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(3, 3)

circuit.id(2)
circuit.x(0)
circuit.x(1)

circuit.barrier(0,1,2)

circuit.x(0)
circuit.cx(0, 2)
circuit.x(0)

circuit.barrier(0,1,2)
#####
# Map the quantum measurement to the classical bits
circuit.measure([0,1,2], [2,1,0])

compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

"""""""| 111 >"""""""
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(3, 3)

circuit.x(0)
circuit.x(1)
circuit.x(2)

circuit.barrier(0,1,2)
circuit.x(0)
circuit.cx(0, 2)
circuit.x(0)
circuit.barrier(0,1,2)
#####
# Map the quantum measurement to the classical bits
circuit.measure([0,1,2], [2,1,0])

compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()