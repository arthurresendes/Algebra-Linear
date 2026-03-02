import numpy as np

A = np.array([[1, 2], [3, 4]])

try:
    A_inv = np.linalg.inv(A)
    print("Matriz Inversa:\n", A_inv)
except np.linalg.LinAlgError:
    print("A matriz não possui inversa.")


matriz_identidade = np.round(A @ A_inv)
print(matriz_identidade)