from qiskit import *
import numpy as np

def deueth_joza(n):
    qc = QuantumCircuit(n, n-1)
    a = np.random.randint(1, 2**n)
    oracleType, oracleValue = np.random.randint(2), np.random.randint(2)
    if oracleType == 0:#If the oracleType is "0", the oracle returns oracleValue for all input. 
        if oracleValue == 1:
            qc.x(n-1)
        else:
            qc.i(n-1)
    else: # Otherwise, it returns the inner product of the input with a (non-zero bitstring) 
        for i in range(n):
            if (a & (1 << i)):
                qc.cx([i], n-1)
        qc.barrier()
    for i in range(n):
        qc.h(i)
    qc.barrier()
    for i in range(n-1):
        qc.cx(i, n-1)
    qc.barrier()
    for i in range(n):
        qc.h(i)
    qc.barrier()
    for i in range(n-1):
        qc.measure(i, i)
    return qc



qc = deueth_joza(8)

qc.draw(output='mpl')
count = execute(qc, Aer.get_backend('qasm_simulator')).result().get_counts()

print(count)