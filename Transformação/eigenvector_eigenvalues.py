import numpy as np
from plotagem import plot_vectors
import sklearn
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
import scipy

vetor_a = np.array([[3,2], [7,-1]])
# print(np.linalg.eig(vetor_a))

eigenvalues, eigenvector = np.linalg.eig(vetor_a)
print(eigenvalues,eigenvector)

eigenvector = eigenvector.T
print("\n")
print(eigenvector)

eigenvector_1, eigenvector_2 = eigenvector
print("\n")
print(eigenvector_1,eigenvector_2)

eigenvalue_1, eigenvalue_2 = eigenvalues
print("\n")
print(eigenvalue_1,eigenvalue_2)

eigenvector_1_transformed = np.matmul(vetor_a,eigenvector_1)
eigenvector_2_transformed = np.matmul(vetor_a,eigenvector_2)
print("\n")
print(eigenvector_1_transformed,eigenvector_2_transformed)

plot_vectors([eigenvector_1,eigenvector_2],vetor_a)

vetor_b = np.array([[1, 3, 2,  5],
              [3, 2, 8,  1],
              [2, 6, 4, 10],
              [5, 1, 7,  4]])

eigenvalues, eigenvectors = np.linalg.eig(vetor_b)
print("\n")
print(eigenvalues,eigenvector)

vetor_c = np.array([[ 3,-1, 2, 0],
              [-1, 4, 7, 1],
              [ 2, 7, 5, 2],
              [ 0, 1, 2, 0]])
print(f"\n{scipy.linalg.issymmetric(vetor_c)}")

eigenvalues, eigenvectors = np.linalg.eigh(vetor_c)
eigenvectors = eigenvectors.T
print("\n")
print(eigenvectors)

for i, _ in enumerate(eigenvectors):
  for j, _ in enumerate(eigenvectors[i + 1:], start = i + 1):
    print(f'eigenvector_{i+1} norm:', np.linalg.norm(eigenvectors[i]))
    print(f'dot_product with eigenvector_{j+1}:', np.dot(eigenvectors[i], eigenvectors[j]))
    print()

print("\n")
print(np.linalg.det(vetor_c))
print("\n")
print(np.prod(eigenvalues))
