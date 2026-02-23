import numpy as np

A = np.array([[1,1,1],[1,-1,1],[2,1,-1]])

determinante = np.linalg.det(A)
print(f"Determinante: {determinante}")
