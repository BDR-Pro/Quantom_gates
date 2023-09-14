import qiskit as q
from qiskit import * 
from qiskit.visualization import *


circ = QuantumCircuit(2,1)

circ.x(0)
circ.i(1)
circ.measure(0,0)
circ.draw('mpl')

job = q.execute(circ, backend=q.Aer.get_backend('qasm_simulator'), shots=1024).result().get_counts()

print(job)

circ.cx(1,0)
circ.cx(0,1)
circ.cx(1,0)

circ.measure(1,0)


circ.draw('mpl')

job = q.execute(circ, backend=q.Aer.get_backend('qasm_simulator'), shots=1024).result().get_counts()

print(job)
