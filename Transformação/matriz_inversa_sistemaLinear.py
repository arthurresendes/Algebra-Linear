import numpy as np
from plotagem import plot_vectors

array = np.array([3, 5, -2])
A = np.array([[3,  2,  1],
              [0,  4, -1],
              [7, -3,  0]])

array_transformed = np.matmul(A, array)
print(array_transformed)

A_inv = np.linalg.inv(A)
print(A_inv)

array_detransformed = np.matmul(A_inv, array_transformed)
print(array_detransformed)

prices = np.array([7.5, 8.25, 35.8, 15])
consumption = np.array([[1, 1, 2, 2],
                        [2, 2, 2, 1],
                        [2, 1, 2, 2],
                        [2, 1, 2, 1]])

bill = np.matmul(consumption, prices)
print(bill)
