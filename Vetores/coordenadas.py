import numpy as np

A = np.array([[1, 2], [3, 4]])

b = np.array([5, 11])

coordenadas = np.linalg.solve(A, b)

print("Coordenadas:", coordenadas)
