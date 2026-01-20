import matplotlib.pyplot as plt
import numpy as np

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