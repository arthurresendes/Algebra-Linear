import numpy as np

vetor_a = np.array([[ 3,-1, 2, 0],
              [-1, 4, 7, 1],
              [ 2, 7, 5, 2],
              [ 0, 1, 2, 0]])
l, q = np.linalg.eig(vetor_a)
print(l,q)

m = np.diag(l)
print(m)
q_inv = np.linalg.inv(q)
print(q)

a_reconstructed = q @ m @ q_inv
print(vetor_a,a_reconstructed)

print(np.allclose(vetor_a, a_reconstructed))

a_reconstructed_transposed = q @ m @ q.T
print(np.allclose(vetor_a, a_reconstructed_transposed))