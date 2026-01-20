import numpy as np
from plt import plot_vectors

matriz = np.array([[1,2],[3,4]])
comprimido_25 = np.array([[1,0],[0,0.25]])
plot_vectors(matriz,comprimido_25)


graus = 30
e = np.array([[np.cos(np.deg2rad(graus)), -np.sin(np.deg2rad(graus))],
              [np.sin(np.deg2rad(graus)),  np.cos(np.deg2rad(graus))]])

array = np.matmul(e,matriz)
print(array)