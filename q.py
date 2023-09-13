import qiskit as q
from qiskit import * 
from qiskit.visualization import *

hadamard = q.QuantumCircuit(3, 3)  # 1 qubit, 1 classical bit
hadamard.h(0)  # Apply H-gate to the 0th qubit
hadamard.x(0)
hadamard.x(1)
hadamard.ccx(0, 1, 2)
hadamard.measure(0, 0)  # Measure the 0th qubit and store result in 0th classical bit
hadamard.measure(2, 0)  # Measure the 0th qubit and store result in 0th classical bit

print(hadamard)
hadamard.draw('mpl')


plot_bloch_vector([1,0,0])


job = q.execute(hadamard, backend=q.Aer.get_backend('qasm_simulator'), shots=1000)

result = job.result()
counts = result.get_counts(hadamard)
print(counts)

plot_histogram(counts)

job2 = q.execute(hadamard, backend=q.Aer.get_backend('statevector_simulator'), shots=1000)

result2 = job2.result()
counts2 = result2.get_counts(hadamard)
print(counts2)

plot_histogram(counts2)

