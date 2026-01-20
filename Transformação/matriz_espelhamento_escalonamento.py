import numpy as np
from .plotagem import plot_vectors

A = np.array([[-1, 0],
              [ 0, 1]])

B = np.array([[1,  0],
              [0, -1]])

array_1 = np.array([1, 2])
array_2 = np.array([3, 4])

array_1_transformed = np.matmul(A, array_1)
print(array_1_transformed)
plot_vectors([array_1], A)
plot_vectors([array_1], B)

plot_vectors([array_2], B)

C = np.array([[3, 0],
              [0, 3]])
plot_vectors([array_1], C)