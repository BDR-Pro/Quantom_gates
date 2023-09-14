import qiskit as q
from qiskit import * 
from qiskit.visualization import *
from qiskit.quantum_info import Statevector

xyz = [[],[1],[0],[0,1]]
values = ["[0,0]","[0,1]","[1,0]","[1,1]"]
print("NAND GATE")
for i in xyz:
    z = xyz.index(i)
    xz = q.QuantumCircuit(3,1)  # 3 qubit, 1 classical bit
    if i != []:
        xz.x(i)
    xz.ccx(0,1,2)
    xz.x(2)
    xz.measure(2, 0)  # Measure the 0th qubit and store result in 0th classical bit\
        
    job = q.execute(xz, backend=q.Aer.get_backend('qasm_simulator'), shots=1024)
        
    result = job.result()
    counts = result.get_counts(xz)

    print(f"{values[z]} : {counts}")


    xz.draw('mpl')
