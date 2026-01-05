import numpy as np

matriz_simetrica = np.array([[1, 3, 2, 5],
     [3, 2, 8, 1],
     [2, 8, 6, 7],
     [5, 1, 7, 4]])

print(np.linalg.det(matriz_simetrica))