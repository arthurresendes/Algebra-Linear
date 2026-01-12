import numpy as np

print("Operação elemento a elemento")
print("Vetor")
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)

print("\nMatriz:")

matriz1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
matriz2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz1 + matriz2)
print(matriz1 - matriz2)
print(matriz1 * matriz2)
print(matriz1 / matriz2)