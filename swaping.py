import qiskit as q
from qiskit import * 
from qiskit.visualization import *

# Create a Quantum Circuit acting on the q register
x = input("Enter number of qubits...")
x = int(x)
circ = QuantumCircuit(x, x)

# Add a H gate on qubit 0
circ.x(0)
circ.x(1)


circ.draw('mpl')

xy =int((x-1)/2)
print(xy)
    # Add a CX (CNOT) gate on control qubit 0 and target qubit 1
for i in range(0, xy):
    circ.swap(i, x-1-i)
    

circ.barrier(range(x))

circ.measure(range(x), range(x))


# Draw the circuit

circ.draw('mpl')


job = q.execute(circ, backend=q.Aer.get_backend('qasm_simulator'), shots=1024).result().get_counts()
    
print(job)
