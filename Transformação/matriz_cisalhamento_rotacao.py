import numpy as np
from plotagem import plot_vectors

array_1 = np.array([1, 2])
array_2 = np.array([3, 4])

D = np.array([[1,0],[0,0.25]])
plot_vectors([array_1],D)

# Rotacionando 10 graus
degrees = 10
E = np.array([[np.cos(np.deg2rad(degrees)), -np.sin(np.deg2rad(degrees))],
              [np.sin(np.deg2rad(degrees)),  np.cos(np.deg2rad(degrees))]])
print(E)

array_1_transformed = np.matmul(E, array_1)
print(f"Rotação em 10 graus: {array_1_transformed}")

plot_vectors([array_1], E)