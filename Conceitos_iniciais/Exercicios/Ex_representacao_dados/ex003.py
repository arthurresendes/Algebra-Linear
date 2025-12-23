import numpy as np

x = np.array([2,-1,3])
w = np.array([1,0,2])
b = -1
y = x[0] * w[0] + x[1] * w[1]  + x[2] * w[2] + b
print(y)