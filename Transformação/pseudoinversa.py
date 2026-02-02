import numpy as np

vetor_a = np.array([[1, 3],
              [2, 5],
              [0, 2]])

a_pinv = np.linalg.pinv(vetor_a)
print(f"Matriz pseudo inversa: {a_pinv}")

u,s,vh = np.linalg.svd(vetor_a,full_matrices=False)
d_plus = np.diag(1/s) # Matriz s transformado d+

a_pinv_svd = u @ d_plus @vh.T
print(a_pinv_svd)