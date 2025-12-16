import numpy as np


escalar = 5**(1/2)
escalar1 = np.array(8)
print(escalar1)
print(type(escalar1))
print("Numero escalar ndim: ")
print(escalar1.ndim)


vetor = np.array([0,10,20,30,40,50])
print(vetor)
print(type(vetor))
print("Numero vetor ndim: ")
print(vetor.ndim)

matriz = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(matriz)
print(type(matriz))
print("Numero matriz ndim: ")
print(matriz.ndim)
matriz *= 2
print(matriz)


