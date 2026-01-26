import numpy as np

vetor_a = np.array([[1, 3],
              [2, 5],
              [0, 2]])

u,s,vh = np.linalg.svd(vetor_a,full_matrices=False)
print(u,s,vh)
a_reconstructed = u @ np.diag(s) @ vh.T
print(a_reconstructed)

print(np.allclose(vetor_a, a_reconstructed))