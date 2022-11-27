import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def isBalanced(counts):
    if '00000' in counts.keys():
        print("Es constante.")
    else:
        print("Es balanceada.")

def Test():
    res = []
    print("\n1. Funcion Balanceada.\n")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(5, 5)

    circuit.barrier()
    circuit.cx(0, 4)
    circuit.cx(1, 4)
    circuit.cx(2, 4)
    circuit.cx(3, 4)
    circuit.barrier()

    circuit.x(0)
    circuit.x(2)
    circuit.barrier()

    circuit.measure([0, 1, 2, 3], [3, 2, 1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()

    counts = result.get_counts(circuit)
    res.append(counts)
    isBalanced(counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()

    print("2. Funcion Balanceada.\n")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(5, 5)

    circuit.barrier()
    circuit.x(2)
    circuit.x(4)
    circuit.cx(3, 4)
    circuit.barrier()

    circuit.measure([0, 1, 2, 3], [3, 2, 1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    res.append(counts)
    isBalanced(counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()

    print("3. Funcion Balanceada.\n")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(5, 5)

    circuit.barrier()
    circuit.x(1)
    circuit.cx(3, 4)
    circuit.cx(2, 4)
    circuit.barrier()

    circuit.measure([0, 1, 2, 3], [3, 2, 1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    res.append(counts)
    isBalanced(counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()

    print("4. Funcion Constante.\n")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(5, 5)

    circuit.barrier()
    circuit.ccx(0, 1, 3)
    circuit.barrier()

    circuit.measure([0, 1, 2, 3], [3, 2, 1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    res.append(counts)
    isBalanced(counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()

    res = list(res)
    return res