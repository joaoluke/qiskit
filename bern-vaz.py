from qiskit import *

n = 3
s = '101'

qc = QuantumCircuit(n+1, n)

qc.h(range(n))
qc.x(n)
for i in range(n):
    if s[::-1][i] == '1':
        qc.cx(i, n)
qc.h(range(n))
qc.measure(range(n), range(n))

backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend, shots=1).result()
print(result.get_counts(qc))