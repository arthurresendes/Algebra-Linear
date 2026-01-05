import numpy as np
import scipy


matriz = np.array([[1, 1, 2, 2, 10, 127.35],
     [2, 2, 2, 1, 10, 128.10],
     [2, 1, 2, 2, 10, 134.85],
     [2, 1, 2, 1, 10, 119.85]])



matriz_diagonal = np.array([[1, 0, 0, 0],
     [0, 2, 0, 0],
     [0, 0, 6, 0],
     [0, 0, 0, 4]])

elementos_diagonais = np.diag(matriz_diagonal)
print(matriz_diagonal)

nova_diag_matriz = np.diag(elementos_diagonais)
print(np.all(nova_diag_matriz == matriz_diagonal))


elementos_diagonais_reciprocal = np.reciprocal(elementos_diagonais.astype(float))
print(elementos_diagonais_reciprocal)


diagonal_matriz_inversa = np.linalg.inv(matriz_diagonal)
print(diagonal_matriz_inversa)
print(np.all(np.diag(diagonal_matriz_inversa) == elementos_diagonais_reciprocal))

print(np.identity(n=3))