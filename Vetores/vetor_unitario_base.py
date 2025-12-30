import numpy as np

vetor = np.array([7.5,8.25])
print(np.linalg.norm(vetor))

normalizacao_vetor = vetor/np.linalg.norm(vetor)
print(normalizacao_vetor)
print(np.linalg.norm(normalizacao_vetor))

vetor_i = np.array([1,0])
vetor_j = np.array([0,1])

calculo = vetor[0] * vetor_i + vetor[1] * vetor_j
print(calculo)