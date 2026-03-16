import numpy as np

matriz4x4 = np.array([[2,0,3,1], [0,1,0,0], [4,2,1,0], [1,0,2,1]])
print(round(np.linalg.det(matriz4x4)))