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

array_1 = [3, 0]
array_2 = [0, 3]

A = np.array([[0.8, 0.3],
              [0.1, 0.7]])

array_1_transformed = np.matmul(A, array_1)
array_2_transformed = np.matmul(A, array_2)
print(array_1_transformed,array_2_transformed)

plot_vectors([array_1, array_2], A)
area = np.linalg.norm(np.cross(array_1, array_2))
print(area)
area_transformed = np.linalg.norm(np.cross(array_1_transformed, array_2_transformed))
print(area_transformed)

det  = np.linalg.det(A)
print(det)