import numpy as np
import scipy


matriz = np.array([[1, 1, 2, 2, 10, 127.35],
     [2, 2, 2, 1, 10, 128.10],
     [2, 1, 2, 2, 10, 134.85],
     [2, 1, 2, 1, 10, 119.85]])


matriz_transposta = np.transpose(matriz)
print(matriz_transposta)
#print(matriz.T)
#print(matriz.transpose())

matriz_simetrica = np.array([[1, 3, 2, 5],
     [3, 2, 8, 1],
     [2, 8, 6, 7],
     [5, 1, 7, 4]])

print(f"Eh simetrica: {scipy.linalg.issymmetric(matriz_simetrica)}")
print(matriz_simetrica == matriz_simetrica.T)
