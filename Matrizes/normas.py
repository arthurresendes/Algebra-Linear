import numpy as np
import scipy


matriz = np.array([[1, 1, 2, 2, 10, 127.35],
     [2, 2, 2, 1, 10, 128.10],
     [2, 1, 2, 2, 10, 134.85],
     [2, 1, 2, 1, 10, 119.85]])

print(matriz.ndim)
print(matriz.shape)
print(matriz.size)
print(f"Norma 2: {np.linalg.norm(matriz)}")
