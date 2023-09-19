from qiskit import qiskit, QuantumCircuit, assemble, Aer, execute

from qiskit.visualization import plot_histogram, plot_bloch_vector, plot_bloch_multivector

#task 1

def NAND(inp1,inp2):

    qc = QuantumCircuit(3, 1) 


    if inp1=='1':
        qc.x(0)
    if inp2=='1':
        qc.x(1)

    qc.barrier()



    qc.ccx(0,1,2)
    qc.x(2)

    qc.barrier()
    qc.measure(2, 0) 

    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc,backend)
    output = (job.result().get_counts())

    return qc, output

tt = [(f'{inp1} {inp2}:{NAND(inp1, inp2)[1]}') for inp1 in ['0', '1'] for inp2 in ['0', '1']]

for t in tt:
    print(t)

#task 2


def swap(n):

    qc = QuantumCircuit(n)

    for i in range(n):
        if i >= n-1-i:
            break
        qc.swap(i, n-1-i)

    qc.measure_all()
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc,backend)
    output = (job.result().get_counts())
    qc.draw('mpl')

swap(10)
