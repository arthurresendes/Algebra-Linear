import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,-1],[0,-2]])
res1 = a @ b
print(res1)


c = np.array([[1,3,5],[2,4,6]])
d = np.array([[3],[2],[1]])
res2 = np.matmul(c,d)
print(res2)