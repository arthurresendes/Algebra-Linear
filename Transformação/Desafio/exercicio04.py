import numpy as np

vetor = np.array([[2,0],
                  [0,3]])

# Eixo x estica 2 vezes e eixo y estica 3, values = [2,3]
eigenvalue,eigenvector = np.linalg.eig(vetor)
print(eigenvalue)
print(eigenvector)