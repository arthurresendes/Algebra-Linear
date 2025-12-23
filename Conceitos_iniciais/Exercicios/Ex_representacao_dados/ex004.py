import numpy as np

x = np.array([1,2])
w = np.array([
    [1,0],
    [2,1]])
b = [0,1]

y1 = x[0] * w[0,0] + x[1] * w[1,0] + b[0]
print(y1)
y2 = x[0] * w[0,1] + x[1] * w[1,1] + b[1]
print(y2)