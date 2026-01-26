import numpy as np

vetor = np.array([[0,0],
                  [1,0]])

# Eixo x estica 2 vezes e eixo y estica 3, values = [2,3]
eigenvalue,eigenvector = np.linalg.eig(vetor)
print(eigenvalue)
print(eigenvector)
print(np.linalg.det(vetor))