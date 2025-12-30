import numpy as np

vetor = np.array([7.5,8.25])
print(np.transpose(vetor))
print(vetor.T)
print(vetor.transpose())

vetor_linha = np.array([[7.5,8.25]])
print(vetor_linha)
print(vetor_linha.shape)

vetor_coluna = np.array([[7.5],[8.25]])
print(vetor_coluna)
print(vetor_coluna.shape)

print(np.transpose(vetor_linha))
print(np.transpose(vetor_coluna))