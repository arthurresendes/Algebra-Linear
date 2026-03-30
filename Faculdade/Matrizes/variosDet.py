import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
soma = a + b
print(soma)

c = np.array([[1,2,3],[4,5,6]])
d = np.array([[1,2],[3,4],[5,6]])

multi = c @ d
print(multi)

matriz2x2 = np.array([[1,2],[3,4]])
print(round(np.linalg.det(matriz2x2)))

matriz3x3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(round(np.linalg.det(matriz3x3)))

matriz4x4 = np.array([[2,0,3,1], [0,1,0,0], [4,2,1,0], [1,0,2,1]])
print(round(np.linalg.det(matriz4x4)))