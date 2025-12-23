import numpy as np

x = np.array([1,-2,0])
w = np.array([[2,1],[-1,0],[0,3]])
b = [1,-1]
y1 = x[0] * w[0,0] + x[1] * w[1,0] + x[2] * w[2,0] + b[0]
y2 = x[0] * w[0,1] + x[1] * w[1,1] + x[2] * w[2,1] + b[1]

print(y1,y2)