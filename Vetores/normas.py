import numpy as np

vetor = np.array([7.5,8.25])
print(f"Norma 1 (distancia manhattan): {np.linalg.norm(vetor,ord=1)}")
print(f"Norma 2 (distancia euclediana): {np.linalg.norm(vetor,ord=2)}")