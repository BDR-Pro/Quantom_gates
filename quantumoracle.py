import qiskit as q
from qiskit import *
from qiskit.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
import random



def circprint():
    # Execute the circuit on the qasm simulator
    job = q.execute(circ, backend=q.Aer.get_backend('qasm_simulator'), shots=1024)
    print(job.result().get_counts(circ))
    circ.draw(output='mpl')

def or1():
    circ.cx(1, 0)


def or2():
    circ.cx(1, 0)
    circ.x(1)

def or3():
    circ.i(0)
    circ.x(1)

def or4():
    circ.i(0)
    circ.i(1)

def oracle():
    x=random.randint(1,4)
    if(x=1):
        or1()
    elif(x=2):
        or2()
    elif(x=3):
        or3()
    else:
        or4()

 

# define oracle function deutch
for num in range(5):
    # Create a Quantum Circuit acting on the q register
    circ = QuantumCircuit(2, 1)
    # Add a H gate on qubit 0 and 1
    circ.x(1)
    circ.h(0)
    circ.h(1)

    # Add a barrier to the circuit
    circ.barrier()
    # Add the oracle
    oracle()

    # Add a barrier to the circuit

    circ.barrier()

    # Add a H gate on qubit 0

    circ.h(0)
    circ.measure(0,0)

    # Draw the circuit
    circprint()


  






