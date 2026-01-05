import numpy as np

matriz_simetrica = np.array([[1, 3, 2, 5],
     [3, 2, 8, 1],
     [2, 8, 6, 7],
     [5, 1, 7, 4]])


simetrica_matriz_inversa = np.linalg.inv(matriz_simetrica)
print(simetrica_matriz_inversa)
print(f"Matriz identidade (inversa * normal): \n{np.dot(matriz_simetrica,simetrica_matriz_inversa)}")
print(np.allclose(np.dot(matriz_simetrica,simetrica_matriz_inversa), np.identity(4)))
