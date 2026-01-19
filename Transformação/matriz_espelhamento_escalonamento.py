import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sklearn
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
import scipy

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