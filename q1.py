import qiskit as q
from qiskit import * 
from qiskit.visualization import *
from qiskit.quantum_info import Statevector

xz = q.QuantumCircuit(2,2)  # 1 qubit, 1 classical bit
xz.h(0)  # Apply H-gate to the 0th qubit
xz.z(0)
xz.h(0)
xz.measure(0, 0)  # Measure the 0th qubit and store result in 0th classical bit
xz.h(1)  # Apply H-gate to the 0th qubit
xz.x(1)
xz.h(1)
xz.measure(1, 1)  # Measure the 0th qubit and store result in 0th classical bit

print(xz)
xz.draw('mpl')



plot_bloch_vector([1,0,0])


job = q.execute(xz, backend=q.Aer.get_backend('qasm_simulator'), shots=1024)

result = job.result()
counts = result.get_counts(xz)
print(counts)

plot_histogram(counts)

job2 = q.execute(xz, backend=q.Aer.get_backend('statevector_simulator'), shots=1024)

result2 = job2.result()
counts2 = result2.get_statevector()
print(counts2)



plot_state_qsphere(counts2)