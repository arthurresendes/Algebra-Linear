import numpy as np

print("Operações escalares")
print("Vetor: ")
op_escalarv = np.array([1,2,3]) + 2
print(op_escalarv)
op_escalarv = np.array([1,2,3]) -2
print(op_escalarv)
op_escalarv = np.array([1,2,3]) *2
print(op_escalarv)
op_escalarv = np.array([1,2,3]) / 2
print(op_escalarv)

print("\nMatriz:")

op_escalarm = np.array([[1,2,3],[4,5,6],[7,8,9]]) + 2
print(op_escalarm)
op_escalarm = np.array([[1,2,3],[4,5,6],[7,8,9]]) - 2
print(op_escalarm)
op_escalarm = np.array([[1,2,3],[4,5,6],[7,8,9]]) * 2
print(op_escalarm)
op_escalarm = np.array([[1,2,3],[4,5,6],[7,8,9]]) / 2
print(op_escalarm)


print("\n")