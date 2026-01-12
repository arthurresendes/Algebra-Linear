import numpy as np

print("Multiplicação Matriarcal")
array1 = np.array([[1,3] ,[ 4,6] ,[7,9]])
array2 = np.array([[2,3,4],[2,3,4]])
print(np.matmul(array1,array2))