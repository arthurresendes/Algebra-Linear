import numpy as np

A = np.array([[1, 1, 1, 2, 2],
              [1, 2, 2, 2, 1],
              [1, 2, 1, 2, 2],
              [1, 2, 1, 2, 1]])
y = np.array([127.35, 128.10, 134.85, 119.85])

np.random.seed(6)

W_1 = np.random.randn(5, 4)
b_1 = np.random.randn(4)

out_1 = np.dot(A, W_1) + b_1
W_2 = np.random.rand(4, 1)

b_2 = np.random.rand(1)
out_2 = np.dot(out_1, W_2) + b_2
error = y - out_2.reshape(y.shape)

print(error)
print(error.mean())