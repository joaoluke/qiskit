# Importar o Qiskit
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

# Criar um registrador quântico com um qubit
q = QuantumRegister(1)

# Criar um registrador clássico com um bit
c = ClassicalRegister(1)

# Criar um circuito quântico
qc = QuantumCircuit(q, c)

# Adicionar uma porta Hadamard ao qubit
qc.h(q[0])

# Medir o qubit e armazenar o resultado no registrador clássico
qc.measure(q, c)

# Executar o circuito em um simulador
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend)
result = job.result()

# Imprimir o resultado da medição
print(result.get_counts(qc))
