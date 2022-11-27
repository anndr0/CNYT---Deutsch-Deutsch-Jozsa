import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def Test():
    print("\nPRUEBAS FUNCION CRUZADOS")
    res3 = []

    """ Entrada |0 >, |0 >"""

    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 2)

    circuit.x(0)
    circuit.cx(0, 1)
    circuit.x(0)

    circuit.measure([0, 1], [1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    res3.append(counts)
    print("\nTotal count for 00 and 11 are:", counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()

    """ Entrada |0 >, |1 > """

    circuit = QuantumCircuit(2, 2)

    circuit.x(1)
    circuit.x(0)
    circuit.cx(0, 1)
    circuit.x(0)

    circuit.measure([0, 1], [1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    res3.append(counts)
    print("\nTotal count for 00 and 11 are:", counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()

    """ Entrada |1 >, |0 > """

    circuit = QuantumCircuit(2, 2)

    circuit.x(0)
    circuit.x(0)
    circuit.cx(0, 1)
    circuit.x(0)

    circuit.measure([0, 1], [1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    res3.append(counts)
    print("\nTotal count for 00 and 11 are:", counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()

    """" Entrada |1 >, |1 > """

    circuit = QuantumCircuit(2, 2)

    circuit.x(0)
    circuit.x(1)
    circuit.x(0)
    circuit.cx(0, 1)
    circuit.x(0)

    circuit.measure([0, 1], [1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    res3.append(counts)
    print("\nTotal count for 00 and 11 are:", counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()

    res3 = list(res3)
    return res3