import numpy as np
import matplotlib.pyplot as plt


def plot_vectors(arrays, transformation_matrix):
    plt.figure(figsize=(5, 5))
    plt.axhline(y=0, linestyle='--')
    plt.axvline(x=0, linestyle='--')
    plt.xticks(np.arange(-10, 10, 0.5))
    plt.yticks(np.arange(-10, 10, 0.5))
    color_palete = [('blue', 'orange'), ('green', 'brown')]
    for i, array in enumerate(arrays):
        array_transformed = np.matmul(transformation_matrix, array)
        plt.arrow(0, 0, *array, length_includes_head=True, head_width=0.05, color=color_palete[i][0], label=f'array_{i+1}')
        plt.arrow(0, 0, *array_transformed, length_includes_head=True, head_width=0.05, color=color_palete[i][1], label=f'array_{i+1}_transformed')
    plt.show()

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
