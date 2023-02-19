from qiskit import QuantumCircuit, execute, Aer

qc = QuantumCircuit(2, 2)

qc.h(0)
qc.cx(0, 1)

qc.measure([0, 1], [0, 1])

backend = Aer.get_backend("qasm_simulator")
job = execute(qc, backend, shots=1024)
result = job.result()
counts = result.get_counts(qc)

print("Resultados:", counts)

qc.draw()
