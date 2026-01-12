import numpy as np

print("Operação de redução")
print("Vetor")

op_reducaov1 = sum(np.array([1,2,3]))
print(op_reducaov1)
op_reducaov2 = np.array([1,2,3]).sum()
print(op_reducaov2)

print("\nMatriz:")

op_reducaom = np.array([[1,2,3],[4,5,6],[7,8,9]]).sum()
print(op_reducaom)
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
op_reducaom = np.sum(matriz,axis=0)
print(op_reducaom)

matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
op_reducaom = np.sum(matriz,axis=1)
print(op_reducaom)
print("\n")