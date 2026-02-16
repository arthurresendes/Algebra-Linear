import numpy as np

# Sistema:
# 3x + y = 9
# x + 2y = 8

A = np.array([[3, 1], [1, 2]])

B = np.array([9, 8])

solucao = np.linalg.solve(A, B)

print(f"Solução: x = {solucao[0]:.2f}, y = {solucao[1]:.2f}")